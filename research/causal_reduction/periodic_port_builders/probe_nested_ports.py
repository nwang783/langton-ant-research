"""Literal finite existence probe, not a renewable builder certificate."""
import json,pathlib
H=10;W=12;CAP=2000000;DEPTH=300;D=[(0,1),(1,0),(0,-1),(-1,0)];nodes=0;best=0;success=None
known={};seed=set();word=[]
def apply(w,x,y,h):
 for c in w:
  p=x,y;b=c=='L'
  if p in known and known[p]!=b:return None
  if p not in known:
   if b:seed.add(p)
  known[p]=not b;h=(h+(-1 if b else 1))%4;dx,dy=D[h];x+=dx;y+=dy
 return x,y,h
assert apply('LL',0,0,1)==(-1,1,3)
outer='LRLRLLRLRL';assert apply(outer,0,4,1)==(-1,9,3)
initial_known=dict(known);initial_seed=set(seed)
def dfs(x,y,h,depth):
 global nodes,best,success
 nodes+=1
 if nodes>CAP:return False
 if x<0:
  if y==5 and h==3:
   success=dict(words=['LL',outer,''.join(word)],seed=sorted(seed),nodes=nodes);return True
  return False
 if not(0<=y<H and x<W)or depth>=DEPTH:return False
 p=x,y;old=known.get(p,None)
 options=[old]if old is not None else[False,True]
 options.sort(key=lambda b:abs(x+D[(h+(-1 if b else 1))%4][0])+abs(y+D[(h+(-1 if b else 1))%4][1]-5))
 for b in options:
  known[p]=not b
  if old is None and b:seed.add(p)
  hh=(h+(-1 if b else 1))%4;dx,dy=D[hh];word.append('L'if b else'R')
  if dfs(x+dx,y+dy,hh,depth+1):return True
  word.pop()
  if old is None:
   del known[p]
   if b:seed.remove(p)
  else:known[p]=old
  if nodes>CAP:return False
 return False
dfs(0,8,1,0)
out=dict(status='FOUND_LITERAL_FINITE_PREFIX'if success else('NODE_CAP'if nodes>CAP else'DEPTH_BOUNDED_EXHAUSTED'),nodes=nodes,success=success)
p=pathlib.Path(__file__).resolve().parent;(p/'nested_port_probe.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
