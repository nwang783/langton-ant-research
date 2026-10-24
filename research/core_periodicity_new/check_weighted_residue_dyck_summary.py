"""Separate derivation-DAG and ALL grammar-obligation residue closure check.
CLI UNIT.dat PREFIX [UNANNOTATED.summary]. No stack-depth truncation.
"""
from pathlib import Path
import sys,json,numpy as np,hashlib
src,pre=map(Path,sys.argv[1:3])
with src.open()as f:
 n,m=map(int,f.readline().split());E=[tuple(map(int,f.readline().split()))for _ in range(m)]
assert all(len(e)==5 and abs(e[2])<=1 and(e[4]-e[2])%2==0 for e in E)
R=np.full((n,n,2),-1,dtype=np.int8);roots={}
with pre.with_suffix('.sparse').open()as f:
 name,nn,nr,mod=next(f).split();assert name=='RESIDUE_BALANCED'and int(nn)==n and int(mod)==4
 for raw in f:
  u,v,t,w,p=map(int,raw.split());assert t in[0,2]and R[u,v,t//2]<0;R[u,v,t//2]=w;roots[u,v,t]=p
assert len(roots)==int(nr)
proof=[]
with pre.with_suffix('.proof').open()as f:
 nn,count,mod=map(int,next(f).split());assert(nn,mod)==(n,4)
 for ix,raw in enumerate(f):
  u,v,t,w,k,a,b,c=map(int,raw.split());assert 0<=u<n and 0<=v<n and t in[0,2]and 0<=w<=4
  if k==0:assert u==v and t==w==0
  elif k==1:assert E[a]==(u,v,0,w,t)
  elif k==2:
   assert 0<=a<ix and 0<=b<ix;A=proof[a];B=proof[b];assert A[0]==u and A[1]==B[0]and B[1]==v and t==(A[2]+B[2])%4 and w==min(4,A[3]+B[3])
  elif k==3:
   assert 0<=b<ix;A=E[a];B=proof[b];C=E[c];assert A[0]==u and A[1]==B[0]and B[1]==C[0]and C[1]==v and A[2]==1 and C[2]==-1 and t==(A[4]+B[2]+C[4])%4 and w==min(4,A[3]+B[3]+C[3])
  else:assert False
  proof.append((u,v,t,w))
assert len(proof)==count
for(u,v,t),p in roots.items():assert proof[p]==(u,v,t,int(R[u,v,t//2]))
assert all(R[u,u,0]>=0 for u in range(n))
for u,v,k,c,t in E:
 if k==0:assert R[u,v,t//2]>=c
for k in range(n):
 for p in[0,1]:
  left=np.flatnonzero(R[:,k,p]>=0)
  if not len(left):continue
  for q in[0,1]:
   right=np.flatnonzero(R[k,:,q]>=0)
   if not len(right):continue
   a=R[left,k,p].astype(np.int16)[:,None];b=R[k,right,q].astype(np.int16)[None,:]
   assert np.all(R[:,:,p^q][np.ix_(left,right)]>=np.minimum(4,a+b))
push=[e for e in E if e[2]==1];pop=[e for e in E if e[2]==-1]
for u,x,k,c,t in push:
 for y,v,kk,cc,tt in pop:
  for p in[0,1]:
   if R[x,y,p]>=0:assert R[u,v,((t+2*p+tt)%4)//2]>=min(4,c+int(R[x,y,p])+cc)
projection=False
if len(sys.argv)>3:
 data=list(map(int,Path(sys.argv[3]).read_text().split()));assert data[0]==n
 assert np.array_equal(np.max(R,axis=2),np.array(data[1:],dtype=np.int8).reshape(n,n));projection=True
O=dict(status='PASS_EXACT_WEIGHTED_RESIDUE_DYCK_CLOSURE',vertices=n,unit_edges=m,balanced_residue_pairs=len(roots),finite_derivation_nodes=len(proof),unannotated_projection_matches=projection,unit_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),scope='Every residue/C-age summary has a checked finite derivation, and all identity, zero, concatenation and push/interior/pop closure obligations are checked. This proves the exact least weighted balanced closure for the supplied unit graph, not a complete record model or ant exclusion.')
pre.with_suffix('.check.json').write_text(json.dumps(O,indent=2)+'\n');print(O)
