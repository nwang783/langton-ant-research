"""Independent finite algebra controls for the analytic all-layer charge lemma."""
import json
from collections import defaultdict
from pathlib import Path

def I(r,k):
 J=lambda p:(p[1],-p[0]);v=(2*r+k,-k-1);c=(0,0);L={(x,0)for x in range(2*r)}|{(2*r+s,-s-1)for s in range(k)};out=set()
 for j in range(4):
  for p in L:
   for _ in range(j):p=J(p)
   out.add((c[0]+p[0],c[1]+p[1]))
  q=v
  for _ in range(j):q=J(q)
  c=(c[0]+q[0],c[1]+q[1])
 return out

def charges(B):
 a=defaultdict(int);c=defaultdict(int)
 for x,y in B:a[y]+=(-1)**x;c[x]+=(-1)**y
 return ({k:int(v)%4 for k,v in a.items()if int(v)%4},{k:int(v)%4 for k,v in c.items()if int(v)%4})
def rowg(x,y,h,j):
 return (2*(y>j)+(0,(-1)**x,2,-(-1)**x)[h]*(y==j))%4

def poseg(x,y,h,j):return rowg(x,y,h,j),rowg(-y,x,(h-1)%4,j)
n=0
for r in range(8):
 for k in range(8):
  b=I(r,k)
  for s in range(9):
   target={(x,y+s)for x,y in I(r,k+s)}
   assert charges(b)==charges(target);n+=1
   if s==2 and r>=3 and k>=3:
    F={(1,0),(1,1),(-3,1),(-3,2)};assert not(F&target)
    q0=charges(b);q1=charges(target|F)
    for j in range(-50,51):
     a0,c0=poseg(0,0,1,j);a1,c1=poseg(0,2,1,j)
     assert(q0[0].get(j,0)+a0-q1[0].get(j,0)-a1)%4==0
     assert(q0[1].get(j,0)+c0-q1[1].get(j,0)-c1)%4==0
matches=[]
for x in range(-10,11):
 for y in range(-10,11):
  for h in range(4):
   if all(poseg(x,y,h,j)==poseg(0,0,1,j)for j in range(-12,13)):matches.append((x,y,h))
assert matches==[(-1,0,3),(0,0,1)]
out=dict(status='PASS finite controls, analytic proof separate',board_charge_equalities=n,matching_poses=matches,corrected_two_layer_controls=25)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
