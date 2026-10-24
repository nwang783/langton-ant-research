from pathlib import Path
from collections import Counter,defaultdict,deque
from fractions import Fraction
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();B=ROOT/'core_periodicity_new/causal_cycle_renewal_20261023_1841';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['path']).read_bytes()).hexdigest()==f['sha256']
ids=(0,1,4,5,6,7,8,9);K={q for q,v in walk(mark)[2].items()if v};Z={1+0j,1+1j,2+0j,2+1j};w=1j;G={};base={0:0,1:0,4:4,5:4,6:4,7:7,8:7,9:7};tail={0:0,1:1,4:0,5:1,6:2,7:0,8:1,9:2};C=raws[1][len(raws[0]):]
for s in ids:
 e,h,_,f=walk(raws[s]);req=walk(raws[s]+mark)[2];black={q for q,v in req.items()if v};G[s]=dict(I=black-K,O=(black^f)-{e+rotation(q,h)for q in K},ctx=set(req)|K,black=black,e=e,h=h)
def chord(s,p,h):return(2*p+rotation(-1-1j,h),2*(p+rotation(walk(raws[base[s]])[0],h))+rotation(-1-1j,h))
def det(a,b):return int(a.real*b.imag-a.imag*b.real)
def hit(A,B):
 a,b=A;c,d=B;u=b-a;v=d-c;z=det(u,v)
 if z:
  t=Fraction(det(c-a,v),z);s=Fraction(det(c-a,u),z)
  return(t,s)if 0<=t<=1 and 0<=s<=1 else None
 if det(c-a,u):return None
 use=(lambda q:int(q.real))if u.real else(lambda q:int(q.imag));ts=sorted((Fraction(use(c-a),use(u)),Fraction(use(d-a),use(u))));lo=max(ts[0],0);hi=min(ts[1],1)
 return('overlap',str(lo),str(hi))if lo<=hi else None
source=chord(7,0j,0)
# Independent cycle extraction from each complete output and literal tails.
for s in(7,8,9):
 O=G[s]['O'];assert Z|{w}<=O;edges={}
 for q in O:
  x,y=xy(q);v=1+1j if(x+y)%2==0 else 1-1j;edges[q]=(2*q-v,2*q+v)
 adj=defaultdict(set)
 for q,vs in edges.items():
  for v in vs:adj[v].add(q)
 alive=set(O);Q=deque(v for v in adj if len(adj[v])==1)
 while Q:
  v=Q.popleft()
  if len(adj[v])!=1:continue
  q=next(iter(adj[v]));alive.remove(q)
  for e in edges[q]:
   adj[e].remove(q)
   if len(adj[e])==1:Q.append(e)
 assert alive==Z
 p=0j;h=0
 for i,c in enumerate(raws[s]):
  if i>=len(raws[7]):assert p not in Z|{w}
  h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
# First retirement must start with all four old identities current.
first=[];candidates={}
for z in Z:
 for s in ids:
  for i in G[s]['I']:
   for h in range(4):
    p=z-rotation(i,h);ctx={p+rotation(x,h)for x in G[s]['ctx']};I={p+rotation(x,h)for x in G[s]['I']};core={p+rotation(x,h)for x in K};bl={p+rotation(x,h)for x in G[s]['black']}
    if(sum(xy(p))+h)%2:r='sector'
    elif core&Z:r='core'
    elif (ctx&Z)-bl:r='white'
    else:
     assert ctx&Z<=I;skey=(s,p,h);candidates[skey]=I&Z;r='candidate'
    first.append(r)
assert len(first)==368 and Counter(first)==dict(sector=184,core=20,white=140,candidate=24)
poses={(0j-1j,1),(2j,2),(3-1j,0),(3+2j,3)};assert set(candidates)=={(s,p,h)for s in(7,8,9)for p,h in poses}
for (s,p,h),I in candidates.items():
 inter=hit(source,chord(s,p,h))
 if(p,h)in((-1j,1),(3+2j,3)):assert inter is not None
 elif(p,h)==(2j,2):assert w in {p+rotation(x,h)for x in G[s]['ctx']} and w not in {p+rotation(x,h)for x in G[s]['black']}
 else:assert inter is None and I=={2+0j,2+1j}
# Mandatory old w cannot clear while every Z identity is protected.
block=[];survivors=set()
for s in ids:
 for i in G[s]['I']:
  for h in range(4):
   p=w-rotation(i,h);ctx={p+rotation(x,h)for x in G[s]['ctx']}
   if(sum(xy(p))+h)%2:r='sector'
   elif ctx&Z:r='protected'
   else:
    inter=hit(source,chord(s,p,h));assert inter is not None and ((inter[0]=='overlap' and Fraction(inter[1])<Fraction(inter[2])) or (inter[0]!='overlap' and 0<inter[0]<1));survivors.add((s,p,h));r='source_contact'
   block.append(r)
assert len(block)==92 and Counter(block)==dict(sector=46,protected=37,source_contact=9)
# Intervening single-producer support pair inventories.
paircounts={};goal=chord(7,3-1j,0)
for name,aa,bb in [('bc',2+3j,3+1j),('cd',3+1j,3+2j)]:
 seen={}
 for s in ids:
  for o in G[s]['O']:
   for h in range(4):
    p=aa-rotation(o,h)
    if(sum(xy(p))+h)%2:continue
    O={p+rotation(x,h)for x in G[s]['O']}
    if bb not in O:continue
    ctx={p+rotation(x,h)for x in G[s]['ctx']}
    if ctx&Z:r='protected'
    else:
     assert name=='cd'and s in(4,5,6,7,8,9);assert chord(s,p,h)[0]==goal[1];r='future_exit'
    seen[s,p,h]=r
 paircounts[name]=dict(Counter(seen.values()))
assert paircounts['cd'].get('future_exit')==6 and 'future_exit'not in paircounts['bc']
# Fresh exact 19-cell physical sharpness, preserving ordered cycle identities.
word=[9,4,1,0,5,0,7];raw=''.join(raws[s]for s in word);seed={q for q,v in walk(raw+mark)[2].items()if v};assert len(seed)==19
field=set(seed);tags={q:('root',q)for q in seed-K};p=0j;h=0;arcs=[];consumed=[];tick=0
for j,s in enumerate(word):
 assert field==set(tags)|{p+rotation(q,h)for q in K}
 ins={p+rotation(q,h)for q in G[s]['I']};old=[(q,tags.pop(q))for q in ins];consumed.append([(xy(q),tag[0],tag[1])for q,tag in old if tag[0]=='out'])
 if j==6:assert(p,h)==(3-1j,0)and{q for q,t in old if t==('out',0)}=={2+0j,2+1j}
 for q in G[s]['O']:
  x=p+rotation(q,h);assert x not in tags;tags[x]=('out',j)
 for atom in[raws[base[s]]]+[C]*tail[s]:
  start=2*p+rotation(-1-1j,h)
  for c in atom:
   assert(p in field)==(c=='L');field.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h];tick+=1
  arcs.append((start,2*p+rotation(-1-1j,h)))
 if j<6:assert all(tags.get(q)==('out',0)for q in Z)
assert tick==182 and(p,h)==(3+3j,0)and len(field)==47
for j in range(len(arcs)):
 for i in range(j):
  z=hit(arcs[i],arcs[j])
  if j==i+1:assert arcs[i][1]==arcs[j][0] and (z==(1,0) or z==('overlap','1','1'))
  else:assert z is None
for c in mark:
 assert(p in field)==(c=='L');field.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
out=dict(status='PASS independent directed first U-cycle retirement, east-pair survival, support pairs and physical sharpness',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),first_counts=dict(Counter(first)),first_distinct_candidates=len(candidates),blocker_counts=dict(Counter(block)),support_pair_counts=paircounts,physical_control=dict(initial_black=19,raw=182,marker=11,chords=11,raw_final_black=47),scope='Within one actual complete-eight factor, source U-entry suffix simplicity. Exact old identities, not reincarnated cells. Directed renewal paths have fixed heading and step(3,-1); no historical-component merger or finite U budget.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(paircounts)
