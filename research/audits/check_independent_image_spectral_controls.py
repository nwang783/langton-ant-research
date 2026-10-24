"""Independent nonsymmetric four-direction incidence and seam controls."""
from pathlib import Path
from fractions import Fraction as F
import random,json,hashlib
rng=random.Random(23101986);vec=[(1,0),(0,1),(-1,0),(0,-1)];chi=[1,-1,1,-1]
def turn(a,b):
 dx,dy=vec[a];ex,ey=vec[b];assert dx*ex+dy*ey==0
 return -(dx*ey-dy*ex)
def curve(w):return sum(turn(a,b)for a,b in zip(w,w[1:]))
def decomp(t):return ((F(sum(t),4)),F(t[0]+t[2]-t[1]-t[3],4),F(t[0]-t[2],2),F(t[1]-t[3],2))
def apply(A,v):return tuple(sum(A[i][j]*v[j]for j in range(2))for i in range(2))
cases=[(7,((1,-2),(2,1)),-1),(9,((1,-2),(2,1)),1),(6,((1,-1),(1,1)),0)]
checks=letters=0;results=[]
for k,A,eps in cases:
 for trial in range(12):
  phi=[]
  for d in range(4):
   start=(d%2 if eps==1 else 1-d%2)if eps else trial%2
   axes=[(start+j)%2 for j in range(k)];target=apply(A,vec[d]);signs={}
   for axis in range(2):
    count=axes.count(axis);assert(count+target[axis])%2==0
    pos=(count+target[axis])//2;assert 0<=pos<=count
    signs[axis]=[axis]*pos+[axis+2]*(count-pos);rng.shuffle(signs[axis])
   w=[signs[a].pop()for a in axes];assert tuple(sum(vec[d][i]for d in w)for i in range(2))==target
   phi.append(w)
  # Counts are checked on the complete function basis, not only eigenvalues.
  for d,w in enumerate(phi):
   assert len(w)==k and sum(chi[a]for a in w)==eps*chi[d]
  old=[[d]for d in range(4)];oldc=(F(0),)*4
  for r in range(1,5):
   new=[[c for a in w for c in old[a]]for w in phi]
   seams=[sum(turn(old[a][-1],old[b][0])for a,b in zip(w,w[1:]))for w in phi]
   vals=[curve(w)for w in new];b=decomp(seams);c=decomp(vals)
   assert c[0]==k*oldc[0]+b[0] and c[1]==eps*oldc[1]+b[1]
   assert c[2]==A[0][0]*oldc[2]+A[1][0]*oldc[3]+b[2]
   assert c[3]==A[0][1]*oldc[2]+A[1][1]*oldc[3]+b[3]
   assert max(map(abs,seams))<=k-1
   for d,w in enumerate(new):
    target=vec[d]
    for _ in range(r):target=apply(A,target)
    assert tuple(sum(vec[a][i]for a in w)for i in range(2))==target
    checks+=1;letters+=len(w)
   old,oldc=new,c
 results.append({'radix':k,'matrix':A,'axis_eigenvalue':eps,'controllers':12,'depth':4})
note=Path(__file__).resolve().parents[1]/'computability/independent_image_spectral_cone_obstruction.md'
out={'status':'PASS independent four-direction incidence/curvature controls, without half-turn enforcement','families':results,'word_checks':checks,'literal_letters':letters,'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'scope':'Finite controls supplement the separate analytic spectral-cone proof.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
