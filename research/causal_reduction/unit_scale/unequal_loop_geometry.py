"""Geometry and literal whole-field helpers for alternating r,s,r,s104 loops.
No all-parameter legality or post-loop capture is asserted by this helper.
"""
from pathlib import Path
import json
from probe_perpendicular_highway_wake import H,shifted_seed,step
from certify_highway_wake_reflector import rot
P=Path(__file__).resolve().parent
K=list(map(tuple,json.loads((P/'single_turn_highway_corner_certificate.json').read_text())['corner_relative_black']))
def corner(j,r,s):
 x=y=0
 for k in range(j):
  n=r if k%2==0 else s;dx,dy=rot((2*n+3,2*n+6),k);x+=dx;y+=dy
 return x,y
def word(r,s):return ''.join('R'+H*(r if j%2==0 else s)+H[:68 if j<3 else 60]for j in range(4))
def seed(r,s):
 B=shifted_seed(2,(1,0))
 for j in range(1,4):
  p=corner(j,r,s)
  for q in K:
   a,b=rot(q,j);B.add((p[0]+a,p[1]+b))
 assert len(B)==43
 return B

def execute(r,s):
 B=seed(r,s);p=(0,0);h=0;w=word(r,s)
 for t,c in enumerate(w):
  p,h,a=step(B,p,h)
  if c!=a:raise AssertionError((r,s,t,c,a,p,h))
 assert(p,h)==((0,0),0);assert len(w)==208*(r+s)+268;assert len(B)==24*(r+s)+87
 return B
if __name__=='__main__':
 for r,s in((3,3),(3,10),(10,3),(4,50),(50,4),(10,30),(30,10),(50,100),(100,50)):
  B=execute(r,s);print(r,s,'PASS',len(B),flush=True)
