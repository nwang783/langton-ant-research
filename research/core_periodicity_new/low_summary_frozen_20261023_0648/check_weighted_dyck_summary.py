"""Separate finite derivation-DAG and complete fixed-point check for Dyck1."""
from pathlib import Path
import sys,json,numpy as np
src,pre=map(Path,sys.argv[1:3]);z=list(map(int,src.read_text().split()));n,m=z[:2];E=[z[2+4*k:6+4*k]for k in range(m)];ss=list(map(int,pre.with_suffix('.summary').read_text().split()));assert ss[0]==n;R=np.array(ss[1:],dtype=np.int8).reshape(n,n);roots=np.array(list(map(int,pre.with_suffix('.roots').read_text().split()))).reshape(n,n);proof=[]
with pre.with_suffix('.proof').open()as f:
 nn,nnodes=map(int,next(f).split());assert nn==n
 for idx,line in enumerate(f):
  u,v,w,k,a,b,c=map(int,line.split());assert 0<=u<n and 0<=v<n and 0<=w<=4
  if k==0:assert u==v and w==0
  elif k==1:assert E[a]==[u,v,0,w]
  elif k==2:
   assert 0<=a<idx and 0<=b<idx;A=proof[a];B=proof[b];assert A[0]==u and A[1]==B[0]and B[1]==v and w==min(4,A[2]+B[2])
  elif k==3:
   assert 0<=b<idx;A=E[a];B=proof[b];C=E[c];assert A[0]==u and A[1]==B[0]and B[1]==C[0]and C[1]==v and A[2]==1 and C[2]==-1 and w==min(4,A[3]+B[2]+C[3])
  else:assert False
  proof.append((u,v,w))
assert len(proof)==nnodes
for u in range(n):
 assert R[u,u]>=0
 for v in range(n):
  p=roots[u,v]
  if R[u,v]<0:assert p==-1
  else:assert 0<=p<len(proof)and proof[p]==(u,v,int(R[u,v]))
for u,v,k,c in E:
 if k==0:assert R[u,v]>=c
for k in range(n):
 left=np.flatnonzero(R[:,k]>=0);right=np.flatnonzero(R[k,:]>=0)
 if len(left)and len(right):
  aa=R[left,k].astype(np.int16)[:,None];bb=R[k,right].astype(np.int16)[None,:]
  assert np.all(R[np.ix_(left,right)]>=np.minimum(4,aa+bb))
for u,x,k,c in E:
 if k!=1:continue
 for y,v,kk,cc in E:
  if kk==-1 and R[x,y]>=0:assert R[u,v]>=min(4,c+int(R[x,y])+cc)
O={'status':'PASS_EXACT_WEIGHTED_DYCK_CLOSURE','vertices':n,'unit_edges':m,'finite_derivation_nodes':len(proof),'balanced_pairs':int(np.count_nonzero(R>=0)),'scope':'Every finite summary has a checked finite balanced path derivation; the matrix is checked closed under every grammar rule. This establishes exact least weighted closure, without a stack-depth cap. No ant record exclusion.'};pre.with_suffix('.check.json').write_text(json.dumps(O,indent=2)+'\n');print(O)
