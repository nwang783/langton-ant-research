#!/usr/bin/env python3
"""Sound finite block abstraction: arbitrary left re-entry, no right input."""
import json
from collections import deque
D=((0,1),(1,0),(0,-1),(-1,0))
def visit(mask,W,H,y,parity=0):
 x=0;h=1;word='';seen=set()
 while 0<=x<W and 0<=y<H:
  state=(mask,x,y,h)
  if state in seen:raise AssertionError('bounded periodic ant')
  seen.add(state);j=x*H+y;c=(mask>>j)&1;word+='L' if c else 'R';h=(h+(-1 if c else 1))%4;mask^=1<<j;x+=D[h][0];y+=D[h][1]
 return ('vertical' if not 0<=y<H else 'right' if x==W else 'left'),mask,y,word

def search(W,H,parity=0,cap=2000000):
 ys=[y for y in range(H) if (y+parity)%2==1];Q=deque([0]);pred={0:None}
 while Q:
  s=Q.popleft()
  for y in ys:
   side,t,z,word=visit(s,W,H,y,parity)
   if side=='right':
    path=[dict(entry=y,exit=z,word=word,side=side)];q=s
    while pred[q] is not None:
     q0,yy,zz,ww=pred[q];path.append(dict(entry=yy,exit=zz,word=ww,side='left'));q=q0
    return dict(W=W,H=H,parity=parity,status='transmits',states=len(pred),path=path[::-1])
   if side=='left' and t not in pred:
    pred[t]=(s,y,z,word);Q.append(t)
    if len(pred)>=cap:return dict(W=W,H=H,parity=parity,status='cap',states=len(pred))
 return dict(W=W,H=H,parity=parity,status='barrier',states=len(pred))
if __name__=='__main__':
 ans=[]
 for H in range(2,9):
  for W in range(1,7):
   a=search(W,H);ans.append(a);print(H,W,a['status'],a['states'],flush=True)
   if a['status']=='cap':break
 json.dump(ans,open('/workspace/shared/langton/frontier_exploration/blank_strip_barrier_search.json','w'),indent=2)
