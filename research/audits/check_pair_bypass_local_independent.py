from pathlib import Path
from itertools import product,combinations
from collections import defaultdict,Counter
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[1];U=ROOT/'causal_reduction/unit_scale';O=U/'pair_bypass_local_window'
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];REV=''.join('L'if c=='R'else'R'for c in H[::-1])
def walk(w,start=(0,0),h=0):
 p=complex(*start);v=(1j,1,-1j,-1);out=[]
 for c in w:
  out.append((int(p.real),int(p.imag),h,c));h=(h+(1 if c=='R'else-1))%4;p+=v[h]
 return out,(int(p.real),int(p.imag)),h
pal={};enumeration={}
for pair in map(''.join,product('RL',repeat=2)):
 coarse,e,h=walk(pair);mid=coarse[1][:3];inv={}
 for n in(2,6,10):
  words=[]
  for w in map(''.join,product('RL',repeat=n)):
   rr,ee,hh=walk(w)
   if (ee,hh)==(e,h) and all(r[:3]!=mid for r in rr):words.append(w)
  inv[n]=words
 assert not inv[2] and not inv[6] and len(inv[10])==2
 for w in inv[10]:assert len({r[:2]for r in walk(w)[0]})==10
 pal[pair]=[pair]+inv[10];enumeration[pair]=inv
geom=json.loads((U/'minimal_pair_bypass_geometry.json').read_text());assert geom['inventories']==pal
canon=lambda cs:Counter(tuple(sorted(c))for c in cs)
def readcnf(f):
 lines=[l for l in f.read_text().splitlines()if l and not l.startswith('c')];p=lines.pop(0).split();cs=[list(map(int,l.split()))[:-1]for l in lines];assert len(cs)==int(p[3]);return int(p[2]),cs
controls=json.loads((O/'controls.json').read_text())['records'];results=[]
for cut in(0,1):
 A=json.loads((O/f'cut{cut}.architecture.json').read_text());res=json.loads((O/f'cut{cut}.result.json').read_text());h0=walk(REV,(0,0),3)[0][cut][2];word=REV[cut:]+REV[:cut];assert A['word']==word and A['start_heading']==h0 and A['palettes']==pal
 coarse,e,hh=walk(word,(0,0),h0);assert (e,hh)==((-2,-2),h0)
 groups=defaultdict(lambda:defaultdict(list));levels=defaultdict(set);C=[];central=[]
 for r in range(7):
  for j in range(52):
   x,y,h,_=coarse[2*j];pos=(x-2*r,y-2*r);pair=word[2*j:2*j+2];sels=[1+3*(52*r+j)+k for k in range(3)];C.append(sels);C.extend([[-a,-b]for a,b in combinations(sels,2)])
   if r==3:central+=sels[1:]
   for k,w in enumerate(pal[pair]):
    rr,ee,eh=walk(w,pos,h);assert(ee,eh)==walk(pair,pos,h)[1:]
    for t,(u,v,_,turn)in enumerate(rr):
     groups[u,v][r,j,t,turn].append(sels[k])
     if r==0:levels[u-v,u%2].add(u//2)
 C.append(central);assert max(max(v)-min(v)for v in levels.values())==3
 nv=1092;gates=[];initial={}
 for cell,events in sorted(groups.items()):
  nv+=1;prev=nv;initial[cell]=prev
  for ev,sels in sorted(events.items()):
   active,nxt=nv+1,nv+2;nv+=2
   C.extend([[-x,active]for x in sels]);C.append(sels+[-active]);C.append([-active,prev if ev[-1]=='L'else-prev])
   for bp,ba,bn in product((False,True),repeat=3):
    if bn!=(bp!=ba):C.append([(-lit if bit else lit)for lit,bit in zip((prev,active,nxt),(bp,ba,bn))])
   gates.append((cell,ev,sels,prev,active,nxt));prev=nxt
 n2,C2=readcnf(O/f'cut{cut}.cnf');assert nv==n2 and canon(C)==canon(C2) and len(C)==53145
 assert list(map(list,sorted(groups)))==A['physical_cells']
 for key,fn in [('cnf_sha256',f'cut{cut}.cnf'),('rup_sha256',f'cut{cut}.rup')]:assert hashlib.sha256((O/fn).read_bytes()).hexdigest()==res[key]
 chk=subprocess.run([str(ROOT/'causal_reduction/morphic_candidates/check_drat'),str(O/f'cut{cut}.cnf'),str(O/f'cut{cut}.rup')],capture_output=True,text=True,check=True);proof=json.loads(chk.stdout);assert proof['valid']and proof['RAT']==0 and proof['deletions']==0
 checks=[];freeC=canon(C)-canon([central])
 for ctrl in controls:
  if ctrl['cut']!=cut:continue
  ks=ctrl['choices'];ww=''.join(pal[word[2*j:2*j+2]][ks[r][j]]for r in range(7)for j in range(52));rr,ee,eh=walk(ww,(0,0),h0);assert (ee,eh)==((-14,-14),h0)
  lit=defaultdict(list)
  for x,y,h,c in rr:lit[x,y].append(c)
  legal=all(all(a!=b for a,b in zip(v,v[1:]))for v in lit.values());first={p for p,v in lit.items()if v[0]=='L'}
  vals={1+3*(52*r+j)+k:k==ks[r][j]for r in range(7)for j in range(52)for k in range(3)};vals.update({v:p in first for p,v in initial.items()});actual=defaultdict(list)
  for p,ev,xs,prev,a,b in gates:
   vals[a]=any(vals[x]for x in xs);vals[b]=vals[prev]!=vals[a]
   if vals[a]:actual[p].append(ev[-1])
  assert dict(actual)==dict(lit)
  sat=all(any(vals[abs(z)]==(z>0)for z in cc)for cc in freeC);assert sat==legal==ctrl['legal']
  assert len(ww)==ctrl['length']and len(first)==ctrl['input_mass']
  if legal:
   board=set(first)
   for x,y,h,c in rr:assert((x,y)in board)==(c=='L');board.symmetric_difference_update({(x,y)})
   assert len(board)==ctrl['output_mass'];assert len(first)==97 and len(board)==13
  checks.append({'length':len(ww),'legal':legal,'central_bypass':any(ks[3]),'input_mass':len(first)})
 results.append({'cut':cut,'variables':nv,'clauses':len(C),'physical_cells':len(groups),'max_orbit_span':3,'RUP':proof['RUP'],'controls':checks,'cnf_sha256':res['cnf_sha256'],'rup_sha256':res['rup_sha256']})
assert REV.count('R')-REV.count('L')==-12
out={'status':'PASS independent minimal geometric palette, full nonstationary physical chronology, complete CNF truth tables and RUP replay','note_sha256':hashlib.sha256((U/'minimal_pair_bypass_geometry.md').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256((U/'check_pair_bypass_local_window.py').read_bytes()).hexdigest(),'palettes':pal,'complete_geometric_lengths':enumeration,'results':results,'scope':'Every legal seven-period word in either fixed inverse104 pair alignment has identity central period, with arbitrary entry colors and independent pair choices. Infinite schedules are identity after period3 and impossible from finite black support by charge minus12. Different scaffolds, alignments varying in time, or other pair images are outside.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('results','complete_geometric_lengths')});print([{k:v for k,v in r.items()if k!='controls'}for r in results])
