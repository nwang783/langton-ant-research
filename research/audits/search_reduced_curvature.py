#!/usr/bin/env python3
"""Independent finite feasible-word search; only found witnesses are proofs."""
import argparse,json,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--depth',type=int,default=30);p.add_argument('--cap',type=int,default=5000000);p.add_argument('--mass',type=int,default=100);p.add_argument('--coefficient',type=int,default=2);a=p.parse_args()
last={};seed=set();stack=[];word=[];steps=0;best=-999;record=None;found=None;start=time.time();dirs=((0,1),(1,0),(0,-1),(-1,0))
def dfs(x,y,h,fuel,curv):
 global steps,best,record,found
 steps+=1
 score=curv-a.coefficient*fuel
 if score>best:
  best=score;record={'word':''.join(word),'seed':sorted(seed),'curvature':curv,'fuel':fuel,'score':score,'reduced':''.join(c*n for c,n in stack)}
  if score>3:found=record.copy();return True
 if len(word)>=a.depth:return False
 old=last.get((x,y));choices=('R','L') if old is None else ('L' if old=='R' else 'R',)
 for c in choices:
  extra=int(old is None and c=='L')
  if fuel+extra>a.mass:continue
  last[x,y]=c
  if extra:seed.add((x,y))
  word.append(c);delta=1 if c=='R' else -1
  if stack and stack[-1][0]==c:
   prev=stack.pop()
   if prev[1]<3:stack.append((c,prev[1]+1));undo=1;cc=curv+delta
   else:undo=2;cc=curv-3*delta
  else:prev=None;stack.append((c,1));undo=0;cc=curv+delta
  hh=(h+delta)%4;dx,dy=dirs[hh]
  stop=dfs(x+dx,y+dy,hh,fuel+extra,cc)
  if undo!=2:stack.pop()
  if prev is not None:stack.append(prev)
  word.pop()
  if extra:seed.remove((x,y))
  if old is None:del last[x,y]
  else:last[x,y]=old
  if stop or steps>=a.cap:return True
 return False
dfs(0,0,0,0,0)
out={'parameters':vars(a),'nodes':steps,'seconds':time.time()-start,'exhausted':steps<a.cap and found is None,'best':record,'counterexample':found}
if found:
 black=set(map(tuple,found['seed']));x=y=h=0
 for c in found['word']:
  assert c==('L' if (x,y) in black else 'R')
  black.symmetric_difference_update({(x,y)});h=(h+(1 if c=='R' else -1))%4;dx,dy=dirs[h];x+=dx;y+=dy
 out['counterexample']['literal_final_pose']=[x,y,h]
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
