#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import json
out=[]
for parity in (0,1):
 a=1-parity;cases=[]
 for h in product((a,a+2),repeat=4):
  g=[(v+(1 if j%2==0 else -1))%4 for j,v in enumerate(h)]
  ins=[d for d in range(4) if h.count(d)==3];outs=[d for d in range(4) if g.count(d)==3]
  if not ins or not outs:continue
  A,B=ins[0],outs[0];turn=(B-A)%4;assert turn in (1,3)
  if turn==1:assert all(h[j]==A and g[j]==B for j in(0,2))
  else:assert all(h[j]==A and g[j]==B for j in(1,3))
  cases.append(dict(h=h,g=g,high_in=A,high_out=B,turn='R' if turn==1 else 'L'))
 assert len(cases)==8
 for h in product((a,a+2),repeat=3):
  g=[(v+(1 if j%2==0 else -1))%4 for j,v in enumerate(h)]
  assert not(any(h.count(d)==3 for d in range(4)) and any(g.count(d)==3 for d in range(4)))
 out.append(dict(parity=parity,cases=cases))
r=dict(status='AUTHOR_LOCAL_COUNT_THREE_ROUTING_PASS',scope='LOCAL_QUAD_TABLE_NOT_GLOBAL_PROOF',controls=out);Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
