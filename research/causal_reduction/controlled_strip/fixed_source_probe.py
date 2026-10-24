#!/usr/bin/env python3
"""Unbounded-height fixed-source discovery. Finite cap -> UNKNOWN, never proof."""
import json,sys
D=((0,1),(1,0),(0,-1),(-1,0))
B=set(); out=[]; steps_total=0; limit=int(sys.argv[1]) if len(sys.argv)>1 else 1000
for k in range(limit):
 x=y=0;h=1;steps=0;mx=0;lo=hi=0
 while x>=0 and steps<10000000:
  p=x,y; b=p in B
  if b:B.remove(p)
  else:B.add(p)
  h=(h+(-1 if b else 1))%4;dx,dy=D[h];x+=dx;y+=dy;steps+=1;mx=max(mx,x);lo=min(lo,y);hi=max(hi,y)
 if x>=0:
  print(json.dumps({'unknown_at':k,'steps':steps,'position':[x,y,h],'mass':len(B)}));break
 out.append({'exit':y,'steps':steps,'max_x':mx,'low_y':lo,'high_y':hi,'mass':len(B)})
 steps_total+=steps
 if k<64:print(k,y,steps,mx,lo,hi,len(B),flush=True)
json.dump({'count':len(out),'total_steps':steps_total,'records':out,'last_field':sorted(B)},open('/workspace/shared/langton/causal_reduction/controlled_strip/fixed_source_probe.json','w'))
