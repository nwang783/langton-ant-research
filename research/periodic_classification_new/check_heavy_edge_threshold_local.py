#!/usr/bin/env python3
from itertools import product
from collections import Counter
from pathlib import Path
import json
out=[]
for m in(1,2,3):
 for extra in(0,1):
  cap=4*m+extra;k=3*m+extra;states=0;types=Counter()
  # Turn-specific incoming counts suffice: enumerate R/L counts of first
  # possible heading. Any chosen totals have a literal alternating history.
  for n in range(cap+1):
   r=(n+1)//2;l=n//2
   for r0 in range(r+1):
    for l0 in range(l+1):
     h=[0 if (j%2==0 and j//2<r0) or (j%2==1 and j//2<l0) else 2 for j in range(n)]
     g=[(a+(1 if j%2==0 else -1))%4 for j,a in enumerate(h)]
     ins=[d for d in(0,2) if h.count(d)>=k];outs=[d for d in(1,3) if g.count(d)>=k]
     if not(ins and outs):continue
     states+=1;a,b=ins[0],outs[0];t=(b-a)%4;assert n==cap and h.count(a)==k and g.count(b)==k
     assert t in(1,3)
     js=range(0,n,2) if t==1 else range(1,n,2)
     assert all(h[j]==a and g[j]==b for j in js)
     if extra:assert t==1
     types['R' if t==1 else 'L']+=1
  out.append(dict(m=m,cap=cap,threshold=k,internal_count_states=states,types=dict(types)))
r=dict(status='AUTHOR_HEAVY_EDGE_COUNT_TABLE_PASS',scope='COUNT_NECESSITIES_NOT_GLOBAL_PROOF',cases=out);Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
