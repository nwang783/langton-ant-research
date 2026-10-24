"""Independent bounded palette, full-history circuit/CNF and RUP replay."""
from pathlib import Path
from itertools import product,combinations
from collections import defaultdict,Counter
import json,hashlib,subprocess,random,time
ROOT=Path(__file__).resolve().parents[1];U=ROOT/'causal_reduction/unit_scale';DATA=json.loads((U/'short_refinement_scaffold_inputs.json').read_text());H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];REV=''.join('L'if c=='R'else'R'for c in H[::-1]);assert H==DATA['H']and REV==DATA['reverse104']
def walk(word,start=(0,0),h=0):
 p=complex(*start);D=(1j,1,-1j,-1);out=[]
 for c in word:
  out.append((int(p.real),int(p.imag),h,c));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return out,(int(p.real),int(p.imag)),h
palette={'R':[],'L':[]};wrong=[]
for n in range(1,10):
 for w in map(''.join,product('RL',repeat=n)):
  rr,p,h=walk(w);last={};legal=True
  for x,y,hh,c in rr:
   if last.get((x,y))==c:legal=False;break
   last[x,y]=c
  for coarse,target in [('R',((1,0),1)),('L',((-1,0),3))]:
   if (p,h)==target:
    assert n%4==1
    if legal:palette[coarse].append(w)
assert palette==DATA['local_images']
def fullhist(w,start,h):
 rows,p,hh=walk(w,start,h);assert p==(start[0]-2,start[1]-2)and hh==h
 g=defaultdict(list)
 for i,(x,y,_,c)in enumerate(rows):g[x-y,x%2].append((i+len(w)*(x//2),c))
 return {k:sorted(v)for k,v in g.items()}
# Independently construct mature NE writer from the actual H at E.
rr,p,h=walk(H,(0,0),1);assert p==(2,2)and h==1;g=defaultdict(list)
for i,(x,y,_,c)in enumerate(rr):g[x-y,x%2].append((i-104*(x//2),c))
wake=set()
for k,v in g.items():
 v.sort();assert [c for t,c in v]==['R'if i%2==0 else'L'for i in range(len(v))]
 if v[-1][1]=='R':wake.add(k)
assert sorted(map(list,wake))==DATA['wake_black_classes']

def build(word,start,inp,nontrivial):
 # Variable identities are explicitly reconstructed from semantic block order.
 clauses=[[1]];groups=defaultdict(lambda:defaultdict(list));coarse,p,h=walk(word,start,3);assert p==(start[0]-2,start[1]-2)and h==3
 for j,(x,y,hh,c)in enumerate(coarse):
  sels=[2+10*j+k for k in range(10)];clauses.append(sels)
  clauses.extend([[-a,-b]for a,b in combinations(sels,2)])
  target=walk(c,(x,y),hh)[1:]
  for k,w in enumerate(palette[c]):
   rr,e,eh=walk(w,(x,y),hh);assert (e,eh)==target
   for i,(qx,qy,qh,turn)in enumerate(rr):groups[qx-qy,qx%2][qx//2,j,i,turn].append(sels[k])
 if nontrivial:clauses.append([-2-10*j for j in range(104)])
 nv=1041;gates=[]
 for key,events in sorted(groups.items()):
  prev=1 if key in inp else -1
  for ev,xs in sorted(events.items()):
   active,nxt=nv+1,nv+2;nv+=2
   clauses.extend([[-x,active]for x in xs]);clauses.append([-active]+xs)
   clauses.append([-active,prev if ev[3]=='L'else-prev])
   # Full XOR truth table, independently generated rather than copied clauses.
   for bp,ba,bn in product((False,True),repeat=3):
    if bn!=(bp!=ba):clauses.append([(-lit if bit else lit)for lit,bit in zip((prev,active,nxt),(bp,ba,bn))])
   gates.append((key,ev,xs,prev,active,nxt));prev=nxt
 return nv,clauses,groups,gates

def read_cnf(path):
 clauses=[];nv=None
 for s in path.read_text().splitlines():
  if not s or s.startswith('c'):continue
  if s.startswith('p'):_,_,a,b=s.split();nv=int(a);count=int(b)
  else:
   v=list(map(int,s.split()));assert v[-1]==0;clauses.append(v[:-1])
 assert len(clauses)==count;return nv,clauses
canon=lambda cs:Counter(tuple(sorted(c))for c in cs)
# White palette semantic reconstruction and retained independent RUP checker.
records=[]
def verify(name,word,start,inp,nontrivial,cnf,rup,meta=None):
 nv,C,groups,gates=build(word,start,inp,nontrivial);n2,C2=read_cnf(cnf);assert nv==n2 and canon(C)==canon(C2),name
 if meta:
  assert hashlib.sha256(cnf.read_bytes()).hexdigest()==meta['cnf_sha256'];assert hashlib.sha256(rup.read_bytes()).hexdigest()==meta['rup_sha256']
 chk=ROOT/'causal_reduction/morphic_candidates/check_drat';res=subprocess.run([str(chk),str(cnf),str(rup)],capture_output=True,text=True,check=True);proof=json.loads(res.stdout);assert proof['valid']and proof['RAT']==0 and proof['deletions']==0
 records.append({'case':name,'variables':nv,'clauses':len(C),'RUP':proof['RUP'],'cnf_sha256':hashlib.sha256(cnf.read_bytes()).hexdigest(),'rup_sha256':hashlib.sha256(rup.read_bytes()).hexdigest()});print(records[-1],flush=True)
verify('white_nonidentity',H,(0,0),set(),True,U/'short_refinement_rup/white_short.cnf',U/'short_refinement_rup/white_short.rup')
manifest=json.loads((U/'reverse_short_all_translations/manifest.json').read_text());base=build(REV,(-1,0),wake,False)[2]
assert sorted(map(list,base))==manifest['base_read_orbits']
translations=sorted({((b[1]-a[1])%2,(b[1]-a[1])%2-(b[0]-a[0]))for a in base for b in wake if (b[0]-a[0])%2})
assert list(map(list,translations))==manifest['placements']and len(translations)==24
for i,tr in enumerate(translations+[None]):
 start=(-1+tr[0],tr[1])if tr is not None else(0,0);inp=wake if tr is not None else set();entry=manifest['results'][i]
 assert entry['translation']==(list(tr)if tr else None)
 verify('reverse_'+str(i),REV,start,inp,False,U/f'reverse_short_all_translations/case{i:02d}.cnf',U/f'reverse_short_all_translations/case{i:02d}.rup',entry)
# Nonvacuous circuit evaluations against separately flattened literal histories.
rng=random.Random(20261023);tests=[]
for word,start,sel in [(H,(0,0),[0]*104),(REV,(0,6),[2 if j==31 else 0 for j in range(104)])]+[(REV,(0,6),[rng.randrange(10)for _ in range(104)])for _ in range(24)]:
 expanded=''.join(palette[c][k]for c,k in zip(word,sel));hist=fullhist(expanded,start,3);inp={k for k,v in hist.items()if v[0][1]=='L'};legal=all(all(a[1]!=b[1]for a,b in zip(v,v[1:]))for v in hist.values())
 nv,C,groups,gates=build(word,start,inp,False);val={1:True};activewords=defaultdict(list)
 for j,k in enumerate(sel):
  for i in range(10):val[2+10*j+i]=(i==k)
 def lit(x):return val[abs(x)]if x>0 else not val[abs(x)]
 for key,ev,xs,prev,a,n in gates:
  val[a]=any(lit(x)for x in xs);val[n]=(lit(prev)!=val[a])
  if val[a]:activewords[key].append(ev[3])
 assert dict(activewords)=={k:[c for t,c in v]for k,v in hist.items()}
 satisfies=all(any(lit(l)for l in clause)for clause in C);assert satisfies==legal
 tests.append({'nonidentity':any(sel),'length':len(expanded),'legal':legal})
assert tests[0]['legal']and tests[1]['legal']and tests[1]['length']==108
out={'status':'PASS independent palette/chronology/CNF reconstruction and retained independent RUP replay','palette_counts':{k:len(v)for k,v in palette.items()},'cases':records,'circuit_controls':tests,'scaffold_sha256':hashlib.sha256((U/'short_refinement_scaffold_inputs.json').read_bytes()).hexdigest(),'manifest_sha256':hashlib.sha256((U/'reverse_short_all_translations/manifest.json').read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256((ROOT/'causal_reduction/morphic_candidates/check_drat').read_bytes()).hexdigest(),'scope':'Fixed104-phase exact-pose1/5/9 palette only; white scaffold identity unique, reverse scaffold has no same-sector mature-standard-input match at any translation. No longer images/different scaffold/general highway conclusion.'}
(ROOT/'audits/check_short_refinement_cnf_independent.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',flush=True)
