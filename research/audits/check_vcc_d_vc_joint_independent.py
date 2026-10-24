"""Independent literal historical patch, convex exterior abstraction, and cube proof."""
from pathlib import Path
import json,hashlib,time
from collections import defaultdict
from check_dcuv_patch_model_independent import raws,mark
ROOT=Path(__file__).resolve().parents[1];F=ROOT/'core_periodicity_new/vcc_d_vc_joint_exclusion_frozen_20261023_0859';started=time.monotonic();M=json.loads((F/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((F/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((F/'04_model.json').read_text());ids=(0,1,4,5,6,7,8,9);cs={0:0,1:1,4:0,5:1,6:2,7:0,8:1,9:2}
def xy(z):return int(z.real),int(z.imag)
def rot(z,h):return z*(-1j)**(h%4)
def trace(w):
 p=0j;h=0;req={};last={};odd=set()
 for c in w:
  assert last.get(p)!=c
  req.setdefault(p,c=='L');last[p]=c;odd.symmetric_difference_update([p]);h=(h+(1 if c=='R'else -1))%4;p+=1j*(-1j)**h
 return p,h,req,odd
raw=[trace(w)for w in raws];ctx={a:trace(raws[a]+mark)[2]for a in ids}
assert trace(raws[6]+raws[5])[:2]==(-1+0j,1)
history=raws[6]+raws[5]+raws[0];_,_,_,odd=trace(history);_,_,entry,_=trace(history+mark)
norm=lambda z:rot(z+1,-1)
points=sorted(map(norm,entry),key=xy);ix={p:i for i,p in enumerate(points)};assert list(map(xy,points))==list(map(tuple,J['points'])) and len(points)==43
color=sum(int(entry[z]^(z in odd))<<ix[norm(z)]for z in entry)
sensitive=set()
for a in ids:
 for h in range(4):
  for z in ctx[a]:
   for q in points:
    p=q-rot(z,h);x,y=xy(p)
    if(x+y-h)%2==0:sensitive.add((x,y,h))
box=[min(x for x,y,h in sensitive),max(x for x,y,h in sensitive),min(y for x,y,h in sensitive),max(y for x,y,h in sensitive)]
assert box==[-13,10,-9,11] and box==J['head_box']
heads=[(x,y,h)for x in range(box[0],box[1]+1)for y in range(box[2],box[3]+1)for h in range(4)if(x+y-h)%2==0];assert heads==list(map(tuple,J['heads']))
N=len(heads);idx={v:i for i,v in enumerate(heads)};assert N==1008
far=lambda h,flag:N+2*h+flag
node=lambda base,c:4*base+c
goal=4*(N+8);assert goal==J['goal'] and J['Nbase']==N+8
start=[node(idx[1,1,0],0),(1<<43)-1,color];assert start==J['start']
pdeny={tuple(map(int,l.split()[:7]))for l in(F/'11_protected_patch2.tsv').read_text().splitlines()};assert hashlib.sha256((F/'11_protected_patch2.tsv').read_bytes()).hexdigest()=='edd8d83e17ddaa220c17960315c235ca90fa2fde9045007efabf824d580f74fd'
watch=2+0j;target=1j;th=1;assert watch in ix
edges=set();reentries=set()
for sid,(x,y,h)in enumerate(heads):
 p=complex(x,y)
 for a in ids:
  ep,dh,_,flip=raw[a];cc=cs[a];dest=(xy(p+rot(ep,h))+(h+dh,));dest=dest[:2]+(dest[2]%4,)
  to=idx.get(dest,far(dest[2],int(cc>0)))
  known=value=toggles=0
  for z,b in ctx[a].items():
   q=p+rot(z,h)
   if q in ix:known|=1<<ix[q];value|=int(b)<<ix[q]
  for z in flip:
   q=p+rot(z,h)
   if q in ix:toggles^=1<<ix[q]
  local=rot(watch-p,-h);target_local=rot(target-p,-h)
  forbidden=(0,a,x,y,h,2,0)in pdeny or(a,5,*xy(target_local),(th-h)%4,*xy(local))in pdeny
  for c in range(4):
   if(a,x,y,h,c)==(5,0,1,1,3):edges.add((node(sid,c),goal,a,0,known,value,toggles,0,0))
   if local not in ctx[a] and not forbidden and c+cc<=3:edges.add((node(sid,c),node(to,c+cc),a,0,known,value,toggles,0,0))
  oldh=(h-dh)%4;oldp=p-rot(ep,oldh)
  if(*xy(oldp),oldh)not in idx:reentries.add(sid)
for h in range(4):
 for flag in range(2):
  for c in range(4):
   for a in ids:
    cc=cs[a]
    if cc>0 and c+cc<=3:edges.add((node(far(h,flag),c),node(far((h-cc)%4,1),c+cc),a,0,0,0,0,0,0))
   if flag:
    for sid in reentries:
     if heads[sid][2]==h:edges.add((node(far(h,flag),c),node(sid,c),99,0,0,0,0,0,0))
assert len(edges)==26215 and edges==set(map(tuple,J['edges'])) and len(edges)==len(J['edges'])
# Zero-C endpoint monotonicity in incoming coordinates is exact literal data.
for a in(0,4,7):
 ep,h,*_=raw[a];assert h==0 and ep.real>=0 and ep.imag>=0 and ep!=0
# The explicit text model must be identical, not a different solver input.
lines=(F/'05_model.dat').read_text().splitlines();assert lines[0]==f'COLOROPS 0 {goal+1} {len(edges)} 1 1 1 43';assert list(map(int,lines[1].split()))==start;assert lines[2]==str(goal)and lines[3]=='0';assert set(tuple(map(int,l.split()))for l in lines[4:])==edges
rows=(F/'06_basis.txt').read_text().splitlines();m,np,nb,nlab=map(int,rows[0].split());assert(m,np,nb,nlab)==(0,goal+1,43,len(rows)-1)
basis=defaultdict(list)
for line in rows[1:]:
 p,k,v=map(int,line.split());assert 0<=p<=goal and 0<=k<1<<43 and v&~k==0;basis[p].append((k,v))
assert any(k==0 for k,v in basis[goal]);assert all((color&k)!=v for k,v in basis[start[0]])
checks=nonempty=0
# Independent exact pullback: output cube under XOR, intersect literal guard.
for fr,to,a,op,K,V,X,clear,reset in edges:
 assert op==clear==reset==0 and V&~K==0
 for k,v in basis[to]:
  checks+=1;required=(v^X)&k
  if(required^V)&k&K:continue
  mask=k|K;bits=required|(V&~k)
  assert bits&~mask==0
  assert any((sm&mask)==sm and ((bits^sv)&sm)==0 for sm,sv in basis[fr]),(fr,to,mask,bits)
  nonempty+=1
out={'status':'PASS independent literal model and unrestricted backward cube invariant','manifest_sha256':hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),'bits':43,'heads':N,'controls':goal+1,'edges':len(edges),'basis_cubes':nlab,'edge_cube_checks':checks,'nonempty_preimages':nonempty,'start_excluded':True,'goal_included':True,'seconds':time.monotonic()-started,'scope':'Only the precise LG-forced VCC→D→VC selected-token chain at C gaps3,3; convex exterior overapproximation covers arbitrarily long zero-C excursions. No general role-cycle or capture conclusion without separate graph analysis.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
