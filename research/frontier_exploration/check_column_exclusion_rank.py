#!/usr/bin/env python3
"""Exhaustive local identities, independent physical one-step simulator."""
import json
from itertools import product
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
records=[]
for entered_from in ('left','right'):
 for cH,cV in product((0,1),repeat=2):
  h=1 if entered_from=='left' else 3;x=0;y=2
  h1=(h+(1 if cH==0 else -1))%4;y1=y+D[h1][1]
  assert D[h1][0]==0 and abs(y1-y)==1
  h2=(h1+(1 if cV==0 else -1))%4
  assert D[h2][1]==0
  reflected=(h2-h)%4==2
  before={y:cH,y1:1-cV};after={y:1-cH,y1:cV}
  deltaN=sum(after.values())-sum(before.values())
  deltaJ=sum(k*v for k,v in after.items())-sum(k*v for k,v in before.items())
  if reflected:assert deltaN==0 and deltaJ==(1 if entered_from=='left' else -1)
  else:assert abs(deltaN)==2
  records.append(dict(side=entered_from,cH=cH,cV=cV,Hrow=y,Vrow=y1,reflection=reflected,deltaN=deltaN,deltaJ=deltaJ))
for H in range(1,100):
 for N in range(H+1):
  lo=sum(range(N));hi=sum(range(H-N,H));assert hi-lo==N*(H-N)<=H*H//4
out=dict(status='PASS',local_cases=records,rank_checks=sum(range(2,101)))
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
