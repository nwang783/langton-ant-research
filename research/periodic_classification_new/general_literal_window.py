#!/usr/bin/env python3
"""Literal proper-path rank/winding necessity for a supplied full drift."""
def bad_window(hs,p,geometry):
 H=len(hs);n=geometry.a;events=[];ins={};outs={}
 for y,row in enumerate(hs):
  for x,h in enumerate(row):
   for j,a in enumerate(h):
    e=(y,x,j);events.append(e);ins.setdefault((y,x,a),[]).append(e);g=(a+(1 if j%2==0 else -1))%4;outs.setdefault((y,x,g),[]).append(e)
 succ={}
 for y in range(H):
  for x,xx,d,k,dr in geometry.arcs[(p+y)%2]:
   yy=y+dr
   if not 0<=yy<H:continue
   es=outs.get((y,x,d),[]);ts=ins.get((yy,xx,d),[]);assert len(es)==len(ts)
   for a,b in zip(es,ts):succ[a]=(b,k)
 for start in events:
  cur=start;w=0;seen={start}
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
   if cur[:2]==start[:2] and ((cur[2]>start[2] and w>0) or (cur[2]<start[2] and w<=0)):return 'wrong_order_segment'
 return None

