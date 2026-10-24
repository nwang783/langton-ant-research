#!/usr/bin/env python3
"""Complete bounded-first-L prefix tree, with at most two reads per cell.
Capped searches are explicitly unknown, never exclusions.
"""
import json,sys,time
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
def test(mass,nodecap=1000000,depthcap=10000):
 reads={};word=[];nodes=0;longest='';status=None;leaves=0
 def go(x,y,h,fuel):
  nonlocal nodes,longest,status,leaves
  nodes+=1
  if len(word)>len(longest):longest=''.join(word)
  if nodes>=nodecap:status='NODE_CAP_UNKNOWN';return
  if len(word)>=depthcap:status='DEPTH_CAP_UNKNOWN';return
  v=reads.get((x,y),0)
  if abs(v)==2:leaves+=1;return
  if v:opts=(-v,)
  elif fuel:opts=(1,-1)
  else:opts=(1,)
  for c in opts:
   reads[x,y]=2*v if v else c
   word.append('R'if c==1 else'L');hh=(h+c)%4;dx,dy=D[hh]
   go(x+dx,y+dy,hh,fuel-int(not v and c==-1))
   word.pop()
   if v:reads[x,y]=v
   else:del reads[x,y]
   if status:return
 go(0,0,0,mass)
 return dict(mass=mass,status=status or'EXHAUSTED',nodes=nodes,leaves=leaves,max_reads=len(longest),longest=longest)
if __name__=='__main__':
 sys.setrecursionlimit(20000);out=[]
 for m in range(7):
  r=test(m);out.append(r);print(json.dumps({k:v for k,v in r.items()if k!='longest'}),flush=True)
  Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
  if r['status']!='EXHAUSTED':break
