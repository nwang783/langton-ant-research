#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
import json
from frontier_drift_geometry import Geometry
from first_read_backbone_frontier import transition
D=((0,1),(1,0),(0,-1),(-1,0));root=Path(__file__).parent;word=(root.parent/'word_stabilization/standard_word.txt').read_text().strip();out=[]
def row(cs):
 rr=[]
 for h in cs:
  ins=[h.count(d) for d in range(4)];outs=[sum((x+(1 if j%2==0 else-1))%4==d for j,x in enumerate(h)) for d in range(4)]
  rr.append(dict(h=h,ins=ins,outs=outs))
 return rr
for copies in(1,2,3):
 P=104*copies;a=2*copies
 for sign in(1,-1):
  b=sign*a;g=Geometry(a,b);p,h=((-1,0),0) if sign==1 else((0,0),1);start=p;hist=defaultdict(list)
  for t,ch in enumerate(word*copies):
   k=p[0]//a;q=p[0]-k*a,p[1]-k*b;hist[q].append((t-k*P,h,ch));h=(h+(1 if ch=='R' else-1))%4;dx,dy=D[h];p=p[0]+dx,p[1]+dy
  assert p==(start[0]+a,start[1]+b)
  lo=min(y-g.base[x] for x,y in hist);hi=max(y-g.base[x] for x,y in hist)
  for S in(16,64,120,512):
   state=();old=row([() for c in range(a)]);C=0
   for r in range(lo,hi+2):
    new=row([tuple(h for t,h,ch in sorted(hist[c,g.base[c]+r])) for c in range(a)])
    state,z,bad=transition(state,old,new,(r-1)%2,g,S);assert bad is None,(copies,sign,S,r,bad)
    C=max(C,z);assert C<=P;old=new
   assert state==() and C>0
   out.append(dict(period=P,drift=[a,b],saturation=S,first_cycle_period_lower=C,status='PASS'))
result=dict(status='AUTHOR_FIRST_READ_BACKBONE_POSITIVES_PASS',controls=out);(root/'first_read_backbone_positive.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
