#!/usr/bin/env python3
"""Literal proper-path chronology plus consecutive first physical returns."""
D=((0,1),(1,0),(0,-1),(-1,0))
def bad_window(hs):
 H=len(hs);n=4;events=[];ins={};outs={}
 for y,row in enumerate(hs):
  for x,h in enumerate(row):
   for j,a in enumerate(h):
    e=(y,x,j);events.append(e);ins.setdefault((y,x,a),[]).append(e);g=(a+(1 if j%2==0 else -1))%4;outs.setdefault((y,x,g),[]).append(e)
 succ={}
 for (y,x,g),es in outs.items():
  dx,dy=D[g];xx=x+dx;yy=y+dy
  if not 0<=yy<H:continue
  ts=ins.get((yy,xx%4,g),[]);assert len(es)==len(ts)
  for a,b in zip(es,ts):succ[a]=(b,xx//4)
 for start in events:
  cur=start;w=0;seen={start};physical_return_seen=False
  while cur in succ:
   cur,k=succ[cur];w+=k
   if cur in seen:
    cyc=[];a=cur;cw=0
    while True:
     cyc.append(a);a,k=succ[a];cw+=k
     if a==cur:break
    if len(cyc)!=len(events) or cw!=1:return 'closed_cycle'
    # Whole-window voltage-one cycle is not rejected as a proper subcycle.
    break
   seen.add(cur)
   if not physical_return_seen and cur[:2]==start[:2] and w==0:
    if cur[2]!=start[2]+1:return 'first_return_rank_skip'
    physical_return_seen=True
   if cur[:2]==start[:2] and ((cur[2]>start[2] and w>0) or (cur[2]<start[2] and w<=0)):return 'wrong_order_segment'
 return None

