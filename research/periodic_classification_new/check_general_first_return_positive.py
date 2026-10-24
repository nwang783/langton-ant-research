#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
import json
from frontier_drift_geometry import Geometry
from general_first_return_window import bad_window
D=((0,1),(1,0),(0,-1),(-1,0));root=Path(__file__).parent;word=(root.parent/'word_stabilization/standard_word.txt').read_text().strip();out=[]
for copies in(1,2,3):
 P=104*copies;a=2*copies
 for sign in(1,-1):
  b=sign*a;g=Geometry(a,b);p,h=((-1,0),0) if sign==1 else ((0,1),1);start=p;hist=defaultdict(list)
  for t,ch in enumerate(word*copies):
   k=p[0]//a;q=p[0]-k*a,p[1]-k*b;hist[q].append((t-k*P,h,ch));h=(h+(1 if ch=='R' else -1))%4;dx,dy=D[h];p=p[0]+dx,p[1]+dy
  assert p==(start[0]+a,start[1]+b)
  lo=min(y-g.base[x] for x,y in hist);hi=max(y-g.base[x] for x,y in hist);rows=[]
  for r in range(lo,hi+1):
   rr=[]
   for c in range(a):
    es=sorted(hist[c,g.base[c]+r]);assert all(ch==('R' if j%2==0 else 'L') for j,(t,h,ch) in enumerate(es));rr.append(tuple(h for t,h,ch in es))
   rows.append(rr)
  n=0
  for k in(2,3,4):
   for z in range(len(rows)-k+1):assert bad_window(rows[z:z+k],(lo+z)%2,g) is None,(copies,sign,k,z);n+=1
  out.append(dict(period=P,drift=[a,b],windows=n,status='ALL_REAL_FRONT_WINDOWS_ACCEPTED'))
r=dict(status='AUTHOR_GENERAL_WINDOW_POSITIVES_PASS',controls=out);(root/'general_first_return_positive.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
