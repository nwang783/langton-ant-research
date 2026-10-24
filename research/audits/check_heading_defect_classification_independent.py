from pathlib import Path
from itertools import product,combinations
from collections import defaultdict,Counter
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[1];U=ROOT/'causal_reduction/unit_scale';O=U/'heading_defect_local_classification'
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];REV=''.join('L'if c=='R'else'R'for c in H[::-1])
def trace(word,p=(0,0),h=0):
 x,y=p;rows=[];D=((0,1),(1,0),(0,-1),(-1,0))
 for c in word:
  rows.append((x,y,h,c));h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return rows,(x,y),h
pal={}
for pair in map(''.join,product('RL',repeat=2)):
 _,end,hh=trace(pair);pal[pair]={}
 for eps in(0,1):
  reset=[];flip=[]
  for n in(2,6):
   for w in map(''.join,product('RL',repeat=n)):
    rr,e,h=trace(w,h=eps*2)
    if e!=end:continue
    if n==2 and h==hh:reset.append(w)
    if h==(hh+2)%4:
     assert n==6 and len({r[:2]for r in rr})==6;flip.append(w)
  assert len(reset)==1 and len(flip)==3
  pal[pair][str(eps)]={'reset':reset[0],'flip':flip}
assert pal==json.loads((U/'minimal_pair_heading_bridge.json').read_text())['palettes']
def cnfread(p):
 lines=[s for s in p.read_text().splitlines()if s and s[0]!='c'];head=lines.pop(0).split();C=[list(map(int,s.split()))[:-1]for s in lines];assert len(C)==int(head[3]);return int(head[2]),C
canon=lambda C:Counter(tuple(sorted(c))for c in C)
def fullhist(w,h):
 rr,e,eh=trace(w,h=h);hist=defaultdict(list)
 for x,y,g,c in rr:hist[x,y].append(c)
 legal=all(all(a!=b for a,b in zip(v,v[1:]))for v in hist.values());I={z for z,v in hist.items()if v[0]=='L'};Out={z for z,v in hist.items()if v[-1]=='R'}
 return legal,I,Out,hist,len(w)
ctrl=json.loads((O/'controls.json').read_text());results=[];saved={}
for cut in(0,1):
 h0=trace(REV,h=3)[0][cut][2];W=REV[cut:]+REV[:cut];coarse,e,hh=trace(W,h=h0);assert(e,hh)==((-2,-2),h0)
 names={};C=[]
 def var(s):
  if s not in names:names[s]=len(names)+1
  return names[s]
 bounds=[var(f'h{i}')for i in range(365)];groups=defaultdict(lambda:defaultdict(list));domains=[];levels=defaultdict(set)
 for r in range(7):
  row=[]
  for j in range(52):
   pair=W[2*j:2*j+2];x,y,h,_=coarse[2*j];p=(x-2*r,y-2*r);dom=[]
   for eps in(0,1):
    aa=pal[pair][str(eps)];dom.append((eps,0,aa['reset']));dom.extend((eps,1,w)for w in aa['flip'])
   row.append(dom);sels=[var(f'x{r}_{j}_{k}')for k in range(8)];C.append(sels);C.extend([[-a,-b]for a,b in combinations(sels,2)])
   for k,(eps,delta,w)in enumerate(dom):
    C.extend([[-sels[k],bounds[52*r+j]if eps else-bounds[52*r+j]],[-sels[k],bounds[52*r+j+1]if delta else-bounds[52*r+j+1]]])
    rr,ee,eh=trace(w,p,(h+2*eps)%4);ce,ch=trace(pair,p,h)[1:];assert(ee,eh)==(ce,(ch+2*delta)%4)
    for i,(xx,yy,g,c)in enumerate(rr):
     groups[xx,yy][r,j,i,c].append(sels[k])
     if r==0:levels[xx-yy,xx%2].add(xx//2)
  domains.append(row)
 assert len(C)==16380 and max(max(a)-min(a)for a in levels.values())==3
 gates=[];initial={}
 for cell,events in sorted(groups.items()):
  prev=var(f'input{len(initial)}');initial[cell]=prev;aidx=len(initial)-1
  for bidx,(ev,sels)in enumerate(sorted(events.items())):
   a=var(f'a{aidx}_{bidx}');b=var(f'b{aidx}_{bidx}');C.extend([[-s,a]for s in sels]);C.append(sels+[-a]);C.append([-a,prev if ev[-1]=='L'else-prev])
   for vp,va,vb in product((False,True),repeat=3):
    if vb!=(vp!=va):C.append([(-q if bit else q)for q,bit in zip((prev,a,b),(vp,va,vb))])
   gates.append((cell,ev,sels,prev,a,b));prev=b
 free=list(C);A=json.loads((O/f'cut{cut}.architecture.json').read_text());allowed=A['allowed_central_assignments'];assert allowed[0]==[0]*52 and len(allowed)==1+cut
 words=[]
 for choices in allowed:
  chosen=[domains[3][j][k]for j,k in enumerate(choices)]
  assert chosen[0][0]==0 and chosen[-1][1]==0 and all(a[1]==b[0]for a,b in zip(chosen,chosen[1:]))
  words.append(''.join(t[2]for t in chosen));C.append([-names[f'x3_{j}_{k}']for j,k in enumerate(choices)])
 assert words[0]==W
 if cut:assert W[30]=='L'and words[1]==W[:30]+'LRRRR'+W[31:]
 nv,actual=cnfread(O/f'cut{cut}.cnf');assert nv==len(names)and canon(C)==canon(actual)
 res=json.loads((O/f'cut{cut}.result.json').read_text())
 for key,fn in(('cnf_sha256',f'cut{cut}.cnf'),('rup_sha256',f'cut{cut}.rup')):assert hashlib.sha256((O/fn).read_bytes()).hexdigest()==res[key]
 pr=json.loads(subprocess.run([str(ROOT/'causal_reduction/morphic_candidates/check_drat'),str(O/f'cut{cut}.cnf'),str(O/f'cut{cut}.rup')],capture_output=True,text=True,check=True).stdout);assert pr['valid']and pr['RAT']==0 and pr['deletions']==0
 nc=0
 for z in ctrl['records']:
  if z['cut']!=cut:continue
  ks=z['choices'];chosen=[domains[r][j][ks[r][j]]for r in range(7)for j in range(52)];assert all(a[1]==b[0]for a,b in zip(chosen,chosen[1:]))
  ww=''.join(a[2]for a in chosen);legal,I,Out,history,length=fullhist(ww,(h0+2*chosen[0][0])%4);assert legal==z['legal']and length==z['length']and len(I)==z['input_mass']
  vals={names[f'x{r}_{j}_{k}']:k==ks[r][j]for r in range(7)for j in range(52)for k in range(8)}
  vals.update({bounds[i]:bool(a[0])for i,a in enumerate(chosen)});vals[bounds[-1]]=bool(chosen[-1][1]);vals.update({v:p in I for p,v in initial.items()});got=defaultdict(list)
  for p,ev,sels,prev,a,b in gates:
   vals[a]=any(vals[x]for x in sels);vals[b]=vals[prev]!=vals[a]
   if vals[a]:got[p].append(ev[-1])
  assert dict(got)==dict(history);assert all(any(vals[abs(t)]==(t>0)for t in cl)for cl in free)==legal
  if legal:assert len(Out)==z['output_mass']
  nc+=1
 saved[cut]=(W,h0,words);results.append(dict(cut=cut,variables=nv,clauses=len(C),physical_cells=len(groups),RUP=pr['RUP'],literal_circuit_controls=nc,allowed_words=words))
# Exact all-length binary field proof, separate from seven-period UNSAT.
W,h0,words=saved[1];assert h0==2;P108=words[1];base,_,_=trace(W,h=h0);support={r[:2]for r in base};first={}
for x,y,h,c in base:first.setdefault((x,y),c)
I={p for p,c in first.items()if c=='L'};assert len(I)==25
new=[]
for n in(1,2,3):
 past={(x+2*k,y+2*k)for k in range(1,n+1)for x,y in support};new.append(I-past)
assert new[0]==new[1]==new[2]and len(new[0])==12
points=((1,7),(0,7),(0,8),(1,8));hist={p:[]for p in points}
for k in range(-4,5):
 for t,(x,y,h,c)in enumerate(base):
  q=(x-2*k,y-2*k)
  if q in hist:hist[q].append((k,t,h,c))
expected={(1,7):[(-1,10,0,'R'),(-1,14,2,'L'),(-1,26,0,'R'),(0,30,0,'L')],(0,7):[(0,31,3,'L')],(0,8):[],(1,8):[(-1,13,3,'L')]};assert hist==expected
assert len({(x-y,x%2)for x,y in points})==4 # Distinct full-drift orbits, hence every translated patch disjoint.
for bits in product((0,1),repeat=7):
 ww=''.join(words[b]for b in bits);legal,inp,out,_,_=fullhist(ww,h0);assert legal and len(inp)==97-sum(bits)and len(out)==13+3*sum(bits)
 baselegal,bi,bo,_,_=fullhist(W*7,h0);selected=[k for k,b in enumerate(bits)if b]
 assert inp==bi-{(points[1][0]-2*k,points[1][1]-2*k)for k in selected}
 assert out==bo|{(points[j][0]-2*k,points[j][1]-2*k)for k in selected for j in(0,2,3)}
assert all(w.count('R')-w.count('L') in(-12,-8)for _,_,ww in saved.values()for w in ww)
result=dict(status='PASS independent minimal heading geometry, complete free-color chronology/CNF, RUP and disjoint binary-field proof',note_sha256=hashlib.sha256((U/'minimal_heading_defect_classification.md').read_bytes()).hexdigest(),results=results,binary_controls=128,baseline_input='12n+13',binary_input='12n+13-m',binary_output='13+3m',scope='Fixed inverse104 pairing and only minimal2-reset/6-flip transitions. Every infinite legal schedule eventually identity or identity/P108 periods and consumes>=8 black per period, impossible from finite support. Arbitrary infinite prepared binary words are positive, not finite-seed counterexamples.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items()if k!='results'});print([{k:v for k,v in r.items()if k!='allowed_words'}for r in results])
