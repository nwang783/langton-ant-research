#!/usr/bin/env python3
"""Exact event-permutation check for an explicit three-row axis candidate."""
import json,sys
from pathlib import Path
D=[(0,1),(1,0),(0,-1),(-1,0)]
def check(n,p,q):
 k=len(p);a=2*k;H={}
 for i in range(k):
  H[2*i,0]=[3];H[2*i+1,0]=[2]
  H[2*i,1]=[0 if j==p[i] else 2 for j in range(n)]
  H[2*i+1,1]=[(1 if j%2 else 3) if j!=q[i] else (3 if j%2 else 1) for j in range(n)]
  H[2*i,2]=[1 if j%2==0 else 3 for j in range(n-1)]
  H[2*i+1,2]=[0]*(n-1)
 inc={};out={};events=[]
 for (x,y),hs in H.items():
  for j,h in enumerate(hs):
   e=(x,y,j);events.append(e);inc.setdefault((x,y,h),[]).append(e)
   g=(h+(1 if j%2==0 else -1))%4;out.setdefault((x,y,g),[]).append(e)
 succ={};vs={};fail=[]
 for (x,y,g),es in out.items():
  dx,dy=D[g];xx=x+dx;yy=y+dy;v=-(xx//a);xx%=a;ts=inc.get((xx,yy,g),[])
  if len(es)!=len(ts):fail.append((x,y,g,len(es),len(ts)))
  for s,t in zip(es,ts):succ[s]=t;vs[s]=v
 if fail:return dict(status='EDGE_COUNT_FAIL',fail=fail)
 cycles=[];seen=set()
 for e in events:
  if e in seen:continue
  c=[];v=0;s=e
  while s not in seen:seen.add(s);c.append(s);v+=vs[s];s=succ[s]
  assert s==e
  cycles.append((c,v))
 result=dict(period=len(events),drift=[-a,0],cycle_data=[(len(c),v) for c,v in cycles])
 if len(cycles)!=1 or cycles[0][1]!=1:result['status']='NOT_ONE_VOLTAGE_ONE_CYCLE';return result
 clocks={};t=0
 for e in cycles[0][0]:clocks[e]=t;t+=1-vs[e]*len(events)
 assert t==0
 bad=[]
 for (x,y),hs in H.items():
  for j in range(len(hs)-1):
   if clocks[x,y,j]>=clocks[x,y,j+1]:bad.append(((x,y,j),clocks[x,y,j],clocks[x,y,j+1]))
 result['status']='ORDER_FAIL' if bad else 'EXACT_FRONT';result['bad_order']=bad
 result['clocks']={str(k):v for k,v in clocks.items()}
 return result
if __name__=='__main__':
 ans=check(16,[11,3],[15,7]);Path(__file__).with_name('axis_negative_three_row_n16_control.json').write_text(json.dumps(ans,indent=2)+'\n');print(json.dumps({k:v for k,v in ans.items() if k!='clocks'}))
