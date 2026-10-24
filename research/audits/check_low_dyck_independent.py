"""Independent finite proof and bitset grammar closure, then exact port products.
No author engine or checker imports. All depth is unbounded in the theorem.
"""
from pathlib import Path
from array import array
from functools import lru_cache
import json,hashlib,sys,time
B=Path('/workspace/shared/langton');root=B/'core_periodicity_new/low_summary_frozen_20261023_0648';k=int(sys.argv[1]);tag=f'low_k{k}';start=time.monotonic()
manifest=json.loads((root/'manifest.json').read_text())
for a in manifest:assert hashlib.sha256((root/a['name']).read_bytes()).hexdigest()==a['sha256']
with (root/(tag+'_unit.dat')).open() as f:
 n,m=map(int,next(f).split());edges=[tuple(map(int,line.split())) for line in f]
assert len(edges)==m and all(len(e)==4 and 0<=e[0]<n and 0<=e[1]<n and e[2] in(-1,0,1) and 0<=e[3]<=2 for e in edges)
rows=[];ge=[];sparse=[]
with (root/(tag+'_dyck.summary')).open() as f:
 assert int(next(f))==n
 for line in f:
  row=array('b',map(int,line.split()));assert len(row)==n and all(-1<=x<=4 for x in row)
  bits=[0]*5;sp=[]
  for v,w in enumerate(row):
   if w>=0:
    sp.append((v,w))
    for j in range(w+1):bits[j]|=1<<v
  rows.append(row);ge.append(tuple(bits));sparse.append(sp)
assert len(rows)==n
proof=[]
with (root/(tag+'_dyck.proof')).open() as f:
 nn,np=map(int,next(f).split());assert nn==n
 for i,line in enumerate(f):
  u,v,w,kind,a,b,c=map(int,line.split());assert 0<=u<n and 0<=v<n and 0<=w<=4
  if kind==0:assert u==v and w==0
  elif kind==1:assert 0<=a<m and edges[a]==(u,v,0,w)
  elif kind==2:
   assert 0<=a<i and 0<=b<i;x=proof[a];y=proof[b];assert (x[0],y[1],min(4,x[2]+y[2]))==(u,v,w) and x[1]==y[0]
  elif kind==3:
   assert 0<=a<m and 0<=c<m and 0<=b<i;x=edges[a];y=proof[b];z=edges[c]
   assert x[2]==1 and z[2]==-1 and (x[0],z[1],min(4,x[3]+y[2]+z[3]))==(u,v,w) and x[1]==y[0] and y[1]==z[0]
  else:raise AssertionError(kind)
  proof.append((u,v,w))
assert len(proof)==np
with (root/(tag+'_dyck.roots')).open() as f:
 for u,line in enumerate(f):
  rs=list(map(int,line.split()));assert len(rs)==n and rows[u][u]>=0
  for v,p in enumerate(rs):
   if rows[u][v]<0:assert p==-1
   else:assert 0<=p<np and proof[p]==(u,v,rows[u][v])
 assert u+1==n
for u,v,d,c in edges:
 if d==0:assert rows[u][v]>=c
checks=0
for u in range(n):
 for mid,a in sparse[u]:
  for b in range(5):assert ge[mid][b]&~ge[u][min(4,a+b)]==0;checks+=1
pop={}
for y,v,d,c in edges:
 if d==-1:pop.setdefault(y,[]).append((v,c))
for u,x,d,c in edges:
 if d==1:
  for y,w in sparse[x]:
   for v,z in pop.get(y,[]):assert rows[u][v]>=min(4,c+w+z);checks+=1
print('balanced closure certified',n,m,np,checks,'seconds',time.monotonic()-start,flush=True)
# Independent exact weighted bitset path products at finite boundary depths.
def bits(z):
 while z:
  b=z&-z;yield b.bit_length()-1;z-=b
@lru_cache(None)
def advance(vect,delta):
 mid=[0]*5
 for u,v,d,c in edges:
  if d==delta and (vect[0]>>u)&1:
   a=max(j for j in range(5) if (vect[j]>>u)&1);mid[min(4,a+c)]|=1<<v
 for j in range(3,-1,-1):mid[j]|=mid[j+1]
 out=[0]*5
 for a in range(5):
  for u in bits(mid[a] & ~(mid[a+1] if a<4 else 0)):
   for b in range(5):out[min(4,a+b)]|=ge[u][b]
 for j in range(3,-1,-1):out[j]|=out[j+1]
 return tuple(out)
D=json.loads((root/f'literal_factor_dfa_k{k}.json').read_text());nd=len(D['transitions']);no=4*nd;L=-18;W=8
with (root/(tag+'_dyck.ports')).open() as f:
 count,ne,ni=map(int,next(f).split());initial=set(map(int,next(f).split()));ports=[tuple(map(int,next(f).split())) for _ in range(count)]
 expected={}
 for line in f:
  u,v,w=map(int,line.split());assert (u,v) not in expected;expected[u,v]=w
 assert len(expected)==ne and len(initial)==ni
wanted=[(h,d,z) for h in range(4) for d in range(nd) for z in range(W) if (L-z-h)%2==0]
assert ports==wanted;ids={t:i for i,t in enumerate(ports)};got={};portchecks=0
for u in range(no):
 tab={(0,0):ge[u]}
 for a in range(1,W):tab[a,0]=advance(tab[a-1,0],-1)
 for a in range(W):
  for b in range(1,W):tab[a,b]=advance(tab[a,b-1],1)
 for d in range(W):
  if (u//nd,u%nd,d) not in ids:continue
  source=ids[u//nd,u%nd,d]
  for target,(h,s,e) in enumerate(ports):
   v=h*nd+s;w=-1
   for a in range(d+1):
    b=e-d+a
    if b>=0:
     t=tab[a,b]
     if (t[0]>>v)&1:w=max(w,max(j for j in range(5) if (t[j]>>v)&1))
   assert w==expected.get((source,target),-1),(source,target,w);portchecks+=1
print('all finite port pairs',portchecks,'cached products',advance.cache_info(),flush=True)
vec=tuple(ge[D['initial_class']][j]|ge[nd+D['initial_class']][j]|ge[2*nd+D['initial_class']][j]|ge[3*nd+D['initial_class']][j] for j in range(5))
while True:
 nxt=advance(vec,-1);nxt=tuple(a|b for a,b in zip(vec,nxt))
 if nxt==vec:break
 vec=nxt
init=set();pref=vec
for d in range(W):
 if d:vec=advance(vec,1);pref=tuple(a|b for a,b in zip(pref,vec))
 for h in range(4):
  for s in range(nd):
   p=ids.get((h,s,d))
   if p is not None and (pref[0]>>(h*nd+s))&1:init.add(p)
assert init==initial
out=dict(status='PASS exact finite derivations and full grammar closure plus every unbounded-depth port query',window=k,vertices=n,unit_edges=m,derivation_nodes=np,balanced_pairs=sum(map(len,sparse)),grammar_checks=checks,ports=len(ports),all_port_pairs=portchecks,summary_edges=ne,initial_low_ports=ni,seconds=time.monotonic()-start,manifest_sha256=hashlib.sha256((root/'manifest.json').read_bytes()).hexdigest(),scope='Exact compiler layer on supplied unit graph; no record exclusion or restored transverse/color geometry.')
p=B/'audits'/f'low_k{k}_dyck_independent.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
