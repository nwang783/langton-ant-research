from pathlib import Path
from itertools import product
import random,json,hashlib
R=Path(__file__).resolve().parents[1];D=((0,1),(1,0),(0,-1),(-1,0))
def sector(p,h):return (-1)**(sum(p)+h%2)
def corr(p,h,line,axis,sigma):
 coord=p[axis]
 if coord<line:return 0
 if coord>line:return 2
 k=sigma*(-1)**line
 return ([k,0,-k,2]if axis==0 else[0,k,2,-k])[h]
def d4(v):return min(v%4,(-v)%4)
poses=[(p,h)for p in product(range(-3,4),repeat=2)for h in range(4)];posechecks=0
for p,h in poses:
 for q,g in poses:
  if sector(p,h)!=sector(q,g):continue
  sig=sector(p,h)
  for axis in(0,1):
   S=sum(d4(corr(p,h,l,axis,sig)-corr(q,g,l,axis,sig))for l in range(-4,5));mid=abs(2*(p[axis]-q[axis])-D[h][axis]+D[g][axis]);assert S>=mid
  posechecks+=1
rng=random.Random(20261023);cases=0
for trial in range(100):
 base={p for p in product(range(-5,6),repeat=2)if rng.randrange(7)==0};C={tuple(rng.randrange(-8,9)for _ in range(2))for j in range(rng.randrange(9))};p0=tuple(rng.randrange(-2,3)for _ in range(2));h0=rng.randrange(4)
 mode=trial%3
 def background(p):return p in base if mode==0 else (sum(p)%2==0 if mode==1 else p[0]-p[1]in(-1,0,2))
 def samples(extra):
  p=p0;h=h0;flips=set(extra);ss=[]
  for t in range(101):
   if t%10==0:ss.append((p,h,set(flips)))
   black=background(p)^(p in flips);flips.symmetric_difference_update({p});h=(h+(-1 if black else 1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
  return ss
 for p,h,fa in samples(C):
  for q,g,fr in samples(set()):
   E=fa^fr;rhs=len(C)+len(E);assert max(abs(2*(p[a]-q[a])-D[h][a]+D[g][a])for a in(0,1))<=rhs
   assert abs(p[0]-p[1]-q[0]+q[1])<=rhs+1;cases+=1
out=dict(status='PASS independent same-sector correction sums and asynchronous two-trajectory Hamming controls',note_sha256=hashlib.sha256((R/'nonlinear_global_budget_2026-10-23/relative_hamming_cursor_coercivity.md').read_bytes()).hexdigest(),pose_pairs=posechecks,trajectory_pairs=cases,scope='Analytic subtraction of exact row/column charges gives2*midpoint_Linf<=initial_XOR+current_COMPLETE_XOR for two actual trajectories from same pose, even infinite common Q by finite-history transfer. Best reference-orbit Hamming bound would imply read halo, but no bound on it or K is established.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
