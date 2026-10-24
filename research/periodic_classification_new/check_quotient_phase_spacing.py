#!/usr/bin/env python3
from itertools import product
from collections import defaultdict
from pathlib import Path
import json
D=((0,1),(1,0),(0,-1),(-1,0));counts=defaultdict(int)
for P in range(4,19,2):
 for word in product((1,-1),repeat=P):
  if sum(word)%4:continue
  h=0;p=(0,0);trace=[]
  for turn in word:
   trace.append(p);h=(h+turn)%4;p=(p[0]+D[h][0],p[1]+D[h][1])
  a,b=p
  if abs(a)+abs(b)<4:continue
  assert P%4==(2*a)%4
  classes=defaultdict(list)
  for t,(x,y) in enumerate(trace):
   # Exact quotient by actual d: canonical Bezout-free key.
   if a:
    aa=abs(a);k=x//aa;q=(x-k*aa,y-k*(b if a>0 else -b))
   else:
    bb=abs(b);k=y//bb;q=(x,y-k*bb)
   classes[q].append(t)
  for ts in classes.values():
   assert 4*len(ts)<=P
   assert all((ts[(i+1)%len(ts)]-ts[i])%P>=4 or len(ts)==1 for i in range(len(ts)))
  counts[P]+=1
r=dict(status='AUTHOR_PHASE_SPACING_CONTROLS_PASS',word_counts=dict(counts),total=sum(counts.values()),scope='LITERAL_CONTROLS_NOT_PROOF');Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
