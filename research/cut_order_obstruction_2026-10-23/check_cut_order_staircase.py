#!/usr/bin/env python3
"""Finite controls for analytic cut-order countermodel, independent of helper geometry."""
from collections import defaultdict
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
UNION={'RRRLLRLLRLR','LLRLRLLRRLL','RRRRLRLLRLL','RRRLRRRRLRL','RRRLRRRRLRR','LRRLRRRRLRR'}
W=(ROOT.parent/'word_stabilization/standard_word.txt').read_text().strip()
F={(W*2)[i:i+10] for i in range(104)}
assert len(W)==104 and len(F)==84
assert 'RLRLRLRLRL' not in F and 'LRLRLRLRLR' not in F
assert 'RLRLRLRLRLR' not in UNION and 'LRLRLRLRLRL' not in UNION

def eps(x,y): return -1 if (x+y)%2==0 else 1

def margins(B):
 r=defaultdict(int); c=defaultdict(int)
 for x,y in B:
  r[y]+=(-1)**x; c[x]+=(-1)**y
 return r,c

def G(r,p,h):
 if p[1]<r:return 0
 if p[1]>r:return 2
 return (0,(-1)**r,2,-(-1)**r)[h]

def Q(c,p,h):
 if p[0]<c:return 0
 if p[0]>c:return 2
 return ((-1)**c,0,-(-1)**c,2)[h]

def delta(v):
 v%=4
 return min(v,4-v)

def from_height(H):
 out=defaultdict(int)
 for x,y in H:
  for dx,dy,v in [(0,0,1),(1,0,-1),(0,1,-1),(1,1,1)]:out[x+dx,y+dy]+=v
 out={p:v for p,v in out.items() if v}
 assert all(v==eps(*p) for p,v in out.items())
 return set(out)

def completion(required,visited):
 # All source sites are inside a finite rectangle; distinct far rows/cols avoid reads.
 R=max([abs(a) for p in visited|required for a in p]+[1])+5
 B=set(); certificates=[]
 for i,(x,y) in enumerate(sorted(required)):
  X=R+4*i
  if (X-x)%2==0:X+=1
  Y=R+4*i
  if (Y-y)%2==0:Y+=1
  corners={(x,y),(X,y),(x,Y),(X,Y)}
  assert len(corners)==4 and not ((corners-{(x,y)})&visited)
  assert not (B&corners)
  B|=corners
  certificates.append((x,y,X,Y,eps(x,y)))
 r,c=margins(B)
 assert all(v==0 for v in list(r.values())+list(c.values()))
 assert B&visited==required
 assert len(B)==4*len(required)
 return B,certificates

seed_cases=0; steps=0; line_checks=0; defect_checks=0; previous=set()
for K in range(24):
 A=-2*K-1; Z=2*K+1; C=-2*K-2
 H={(x,y) for y in range(A,Z+1) for x in range(C,y+2)}
 if previous:assert previous<=H
 previous=H
 B=from_height(H)
 explicit={(C,A),(A+2,A),(C,Z+1),(Z+2,Z+1)}
 explicit|={(n+1,n) for n in range(A+1,Z+1)}
 explicit|={(n+2,n) for n in range(A+1,Z+1)}
 assert B==explicit and len(B)==8*K+8
 r,c=margins(B)
 assert all(v==0 for v in list(r.values())+list(c.values()))
 initial=set(B); p=(0,0); h=0; visited=[]; word=''
 # This is the guaranteed exact prefix, including its final move.
 T=4*K+6
 for t in range(T+1):
  assert p==((t+1)//2,t//2) and h==t%2
  E=B^initial
  assert len(E)==t
  # Twice midpoint displacements are integers and both equal t.
  dx=2*p[0]-D[h][0]
  dy=2*p[1]-D[h][1]+1
  assert dx==t and dy==t
  rr,cc=margins(E)
  for row in range(-1,p[1]+2):
   n=sum(y==row for x,y in E)
   assert n==delta(G(row,p,h)-G(row,(0,0),0)); line_checks+=1
  for col in range(-1,p[0]+2):
   n=sum(x==col for x,y in E)
   assert n==delta(Q(col,p,h)-Q(col,(0,0),0)); line_checks+=1
  actualr,actualc=margins(B)
  for row in actualr:
   assert (actualr[row]-G(row,p,h)+G(row,(0,0),0))%4==0
  for col in actualc:
   assert (actualc[col]-Q(col,p,h)+Q(col,(0,0),0))%4==0
  if t>=11:
   z=word[-11:]
   assert z[:10] not in F and z[1:] not in F and z not in UNION
   defect_checks+=1
  if t==T:break
  assert p not in visited
  visited.append(p)
  black=p in B
  assert black==(t%2==1)
  word+='L' if black else 'R'
  h=(h+(-1 if black else 1))%4
  if black:B.remove(p)
  else:B.add(p)
  p=(p[0]+D[h][0],p[1]+D[h][1]); steps+=1
 seed_cases+=1

# General margin completion controls on physically generated arbitrary finite words.
completion_cases=0
for length in [0,1,2,4,10,25,50,100,250,500]:
 B={(0,0),(3,1),(-2,4)}; p=(0,0); h=0; visited=set(); required=set(); reads=[]
 for t in range(length):
  black=p in B
  if p not in visited and black:required.add(p)
  visited.add(p); reads.append((p,black))
  h=(h+(-1 if black else 1))%4
  if black:B.remove(p)
  else:B.add(p)
  p=(p[0]+D[h][0],p[1]+D[h][1])
 padded,rectangles=completion(required,visited)
 for q,black in reads:
  assert (q in padded)==black
  if black:padded.remove(q)
  else:padded.add(q)
 completion_cases+=1

out={'status':'PASS','seed_cases':seed_cases,'literal_staircase_steps':steps,
 'sharp_per_line_checks':line_checks,'residual_union6_defect_windows':defect_checks,
 'arbitrary_prefix_margin_completions':completion_cases,
 'standard_word_sha256':hashlib.sha256(W.encode()).hexdigest(),
 'scope':'Finite controls of all-parameter formulas; no infinite finite-seed orbit claimed.'}
(ROOT/'check_cut_order_staircase.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
