"""Literal modulo-four unit geometry and independent bitset Dyck closure/ports.
No author implementation is imported. Every asserted maximum has a finite proof.
"""
from pathlib import Path
from array import array
from functools import lru_cache
from collections import Counter
import json,hashlib,sys,time
B=Path(__file__).resolve().parents[1];R=B/'core_periodicity_new/low_residue_frozen_20261023_0714';old=B/'core_periodicity_new/low_summary_frozen_20261023_0648';k=int(sys.argv[1]);tag=f'low_k{k}_residue';start=time.monotonic()
M=json.loads((R/'manifest.json').read_text())
for f in M['files']:
 p=R/Path(f['frozen']).name;assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256']
with (R/(tag+'_unit.dat')).open()as f:n,m=map(int,next(f).split());E=[tuple(map(int,line.split()))for line in f]
assert len(E)==m and all(len(e)==5 and 0<=e[0]<n and 0<=e[1]<n and e[2]in(-1,0,1) and 0<=e[3]<=2 and 0<=e[4]<4 and(e[2]-e[4])%2==0 for e in E)
U=json.loads((R/(tag+'_unit.json')).read_text());D=json.loads((R/f'literal_factor_dfa_k{k}.json').read_text());J=json.loads((R/f'v1_k{k}.json').read_text());G=json.loads((R/'literal_residual_geometry.json').read_text())['geometry'];nd=len(D['transitions']);no=4*nd;L=M['low_cutoff'];W=8;phase=J['phase'];dirs=(1j,1,-1j,-1)
assert E==list(map(tuple,U['edges']))and n==len(U['nodes'])and U['original_controls']==no
expected={(h,d,a)for h in range(4)for d,row in enumerate(D['transitions'])for a,to in zip(D['keep'],row)if to>=0};seen=set();used=Counter();private=Counter()
for p in U['packet_expansions']:
 h,d=p['source'];a=p['packet'];assert(h,d,a)in expected and(h,d,a)not in seen;seen.add((h,d,a));g=G[a];z=0j;heading=dirs[(h+phase)%4]
 for c in g['word']:heading*=(-1j if c=='R'else 1j);z+=heading
 dq=int(z.real+z.imag);dt=int(z.real-z.imag);dh=(dirs.index(heading)-h-phase)%4;count=g['name'].count('C');to=D['transitions'][d][D['keep'].index(a)]
 assert p['target']==[(h+dh)%4,to]and p['head_delta']==dq and p['transverse_delta']==dt and p['C_count']==count
 u=h*nd+d;weight=change=residue=0;ids=p['unit_edges'];assert len(ids)==max(1,abs(dq))
 for j,eid in enumerate(ids):
  used[eid]+=1;x,y,step,w,t=E[eid];assert x==u and step==(-1 if dq>0 else 1 if dq<0 else 0)and w==(count if j==0 else 0)
  assert t==((dt-(len(ids)-1))%4 if j==len(ids)-1 else 1)
  weight+=w;change+=step;residue+=t;u=y
  if j<len(ids)-1:assert u>=no;private[u]+=1
 assert u==((h+dh)%4)*nd+to and weight==count and change==-dq and residue%4==dt%4
 for xy in g['inputs']+g['outputs']:
  z=complex(*xy)*(-1j)**(h+phase);assert L+int(z.real+z.imag)<=J['initial_bound']
assert seen==expected and used==Counter(range(m))and private==Counter(range(no,n))
print('literal unit graph',k,n,m,flush=True)
weights=array('b',[-1])*(2*n*n);roots=array('i');sparse=[[array('i'),array('i')]for _ in range(n)];ge=[[[0]*5 for _ in range(2)]for _ in range(n)]
def ix(u,v,p):return 2*(u*n+v)+p
with (R/(tag+'_dyck.sparse')).open()as f:
 name,nn,nr,mod=next(f).split();assert name=='RESIDUE_BALANCED'and int(nn)==n and int(mod)==4;nr=int(nr)
 for line in f:
  u,v,t,w,proof=map(int,line.split());assert 0<=u<n and 0<=v<n and t in(0,2)and 0<=w<=4 and weights[ix(u,v,t//2)]==-1
  p=t//2;weights[ix(u,v,p)]=w;roots.extend((u,v,t,w,proof));sparse[u][p].extend((v,w))
  for j in range(w+1):ge[u][p][j]|=1<<v
assert len(roots)==5*nr
proofs=array('i')
def item(p):return tuple(proofs[4*p:4*p+4])
with (R/(tag+'_dyck.proof')).open()as f:
 nn,np,mod=map(int,next(f).split());assert(nn,mod)==(n,4)
 for i,line in enumerate(f):
  u,v,t,w,kind,a,b,c=map(int,line.split());assert 0<=u<n and 0<=v<n and t in(0,2)and 0<=w<=4
  if kind==0:assert u==v and t==w==0
  elif kind==1:assert 0<=a<m and E[a]==(u,v,0,w,t)
  elif kind==2:
   assert 0<=a<i and 0<=b<i;x=item(a);y=item(b);assert x[1]==y[0]and(x[0],y[1],(x[2]+y[2])%4,min(4,x[3]+y[3]))==(u,v,t,w)
  elif kind==3:
   assert 0<=a<m and 0<=c<m and 0<=b<i;x=E[a];y=item(b);z=E[c]
   assert x[2]==1 and z[2]==-1 and x[1]==y[0]and y[1]==z[0]and(x[0],z[1],(x[4]+y[2]+z[4])%4,min(4,x[3]+y[3]+z[3]))==(u,v,t,w)
  else:raise AssertionError(kind)
  proofs.extend((u,v,t,w))
assert len(proofs)==4*np
for j in range(0,len(roots),5):
 u,v,t,w,p=roots[j:j+5];assert 0<=p<np and item(p)==(u,v,t,w)
for u in range(n):assert weights[ix(u,u,0)]>=0
for u,v,d,w,t in E:
 if d==0:assert weights[ix(u,v,t//2)]>=w
checks=0
for u in range(n):
 for p in range(2):
  sp=sparse[u][p]
  for i in range(0,len(sp),2):
   mid,a=sp[i:i+2]
   for q in range(2):
    for b in range(5):assert ge[mid][q][b]&~ge[u][p^q][min(4,a+b)]==0;checks+=1
pop={}
for y,v,d,c,t in E:
 if d==-1:pop.setdefault(y,[]).append((v,c,t))
for u,x,d,c,t in E:
 if d==1:
  for p in range(2):
   sp=sparse[x][p]
   for i in range(0,len(sp),2):
    y,a=sp[i:i+2]
    for v,b,tt in pop.get(y,[]):assert weights[ix(u,v,((t+2*p+tt)%4)//2)]>=min(4,c+a+b);checks+=1
# Independent projection to the previously signed exact unannotated relation.
with (old/f'low_k{k}_dyck.summary').open()as f:
 assert int(next(f))==n
 for u,line in enumerate(f):
  row=list(map(int,line.split()));assert len(row)==n
  assert all(max(weights[ix(u,v,0)],weights[ix(u,v,1)])==w for v,w in enumerate(row))
print('balanced exact',k,nr,np,checks,'seconds',time.monotonic()-start,flush=True)
def bits(z):
 while z:
  t=z&-z;yield t.bit_length()-1;z-=t
@lru_cache(maxsize=20000)
def advance(vect,delta):
 mid=[[0]*5 for _ in range(4)]
 for u,v,d,c,t in E:
  if d!=delta:continue
  for r in range(4):
   if(vect[5*r]>>u)&1:
    a=max(j for j in range(5)if(vect[5*r+j]>>u)&1);mid[(r+t)%4][min(4,a+c)]|=1<<v
 for r in range(4):
  for j in range(3,-1,-1):mid[r][j]|=mid[r][j+1]
 out=[[0]*5 for _ in range(4)]
 for r in range(4):
  for a in range(5):
   for u in bits(mid[r][a]&~(mid[r][a+1]if a<4 else 0)):
    for p in range(2):
     dest=out[(r+2*p)%4]
     for b in range(5-a):dest[a+b]|=ge[u][p][b]
 for r in range(4):
  for j in range(3,-1,-1):out[r][j]|=out[r][j+1]
 return tuple(b for row in out for b in row)
with (R/(tag+'_dyck.ports')).open()as f:
 name,npports,ne,ni,mod=next(f).split();assert name=='RESIDUE_PORTS'and int(mod)==4;npports,ne,ni=map(int,(npports,ne,ni));initial=set(map(int,next(f).split()));ports=[tuple(map(int,next(f).split()))for _ in range(npports)]
 expected=array('b',[-1])*(npports*npports*4);records=0
 for line in f:
  u,v,t,w=map(int,line.split());assert 0<=u<npports and 0<=v<npports and 0<=t<4 and 0<=w<=4;idx=4*(u*npports+v)+t;assert expected[idx]==-1;expected[idx]=w;records+=1
 assert records==ne and len(initial)==ni
wanted=[(h,d,z)for h in range(4)for d in range(nd)for z in range(W)if(L-z-h)%2==0];assert ports==wanted;ids={p:i for i,p in enumerate(ports)};pairchecks=0
for u in range(no):
 zero=[0]*20
 for p in range(2):zero[10*p:10*p+5]=ge[u][p]
 tab={(0,0):tuple(zero)}
 for a in range(1,W):tab[a,0]=advance(tab[a-1,0],-1)
 for a in range(W):
  for b in range(1,W):tab[a,b]=advance(tab[a,b-1],1)
 for d in range(W):
  source=ids.get((u//nd,u%nd,d))
  if source is None:continue
  for target,(h,s,e)in enumerate(ports):
   v=h*nd+s
   for t in range(4):
    w=-1
    for a in range(d+1):
     b=e-d+a
     if b>=0:
      vec=tab[a,b]
      if(vec[5*t]>>v)&1:w=max(w,max(j for j in range(5)if(vec[5*t+j]>>v)&1))
    assert w==expected[4*(source*npports+target)+t],(source,target,t,w);pairchecks+=1
 if u%100==0:print('ports',k,u,no,'cache',advance.cache_info(),'seconds',time.monotonic()-start,flush=True)
# Every projected port weight and initial port must coincide with prior KG.
with(old/f'low_k{k}_dyck.ports').open()as f:
 nn,oldne,oldni=map(int,next(f).split());assert nn==npports and oldni==ni and set(map(int,next(f).split()))==initial
 assert [tuple(map(int,next(f).split()))for _ in range(nn)]==ports
 got=0
 for line in f:
  u,v,w=map(int,line.split());assert max(expected[4*(u*npports+v):4*(u*npports+v)+4])==w;got+=1
 assert got==oldne
 assert sum(any(w>=0 for w in expected[i:i+4])for i in range(0,len(expected),4))==oldne
# Projected KG initial set permits BOTH residues consistent with each final
# physical height; an arbitrary initial t supplies either after the same path.
for h,s,d in ports:assert(L-d-h)%2==0
out=dict(status='PASS independent literal unit geometry, finite derivations, every residue grammar closure and every port profile',window=k,vertices=n,unit_edges=m,packet_transitions=len(seen),balanced_residue_pairs=nr,finite_proofs=np,grammar_checks=checks,ports=npports,all_port_profiles=pairchecks,residue_edges=ne,initial_low_ports=ni,seconds=time.monotonic()-start,manifest_sha256=hashlib.sha256((R/'manifest.json').read_bytes()).hexdigest(),scope='Exact low-counter packet-DFA relaxation with transverse modulo4 and saturated C ages. No low color legality, integrated record exclusion or capture theorem.')
p=B/'audits'/f'low_k{k}_residue_independent.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
