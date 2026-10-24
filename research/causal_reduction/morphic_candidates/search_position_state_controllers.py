"""Constraint-guided synthesis of a heading-free phase controller with one
private finite-controller bit. Unassigned rule entries branch; assigned ones
are reused. EXHAUSTED covers all completions of unreached rule entries.
"""
import json,pathlib,sys,time
from search_position_phase_controllers import opts,D,HERE
sys.setrecursionlimit(10000)

def search(root,nodecap=1000000,depthcap=1000):
 letters=[];poses=[(0,0,0)];last={};rules={};nodes=0;conflicts=0;stop=None;best=None;maxdepth=0
 def dfs(n,state):
  nonlocal nodes,conflicts,stop,best,maxdepth
  nodes+=1
  if n>maxdepth:
   maxdepth=n;best=dict(word=''.join(letters),rules=[dict(key=k,choice=v,word=opts[k[0]][v//2],nextstate=v%2)for k,v in rules.items()])
  if nodes>=nodecap:stop='NODE_CAP';return
  if n>=depthcap:stop='HORIZON_ONLY';return
  c=root if n==0 else letters[n];x,y,h=poses[n];X,Y,H=poses[-1];delta=(H-h)%4
  key0=(0 if c=='R' else 2)+delta//2;key=(key0,state)
  fresh=key not in rules
  for choice in (range(30) if fresh else [rules[key]]):
   w=opts[key0][choice//2];nextstate=choice%2
   if n==0 and w[0]!=root:continue
   if fresh:rules[key]=choice
   l0=len(letters);p0=len(poses);undo=[];okay=True
   for ch in w:
    X,Y,H=poses[-1];p=X,Y;old=last.get(p)
    if old==ch:conflicts+=1;okay=False;break
    undo.append((p,old));last[p]=ch;letters.append(ch);H=(H+(1 if ch=='R' else -1))%4;dx,dy=D[H];poses.append((X+dx,Y+dy,H))
   if okay:
    assert poses[-1][:2]==(3*poses[n+1][0],3*poses[n+1][1]);dfs(n+1,nextstate)
   for p,old in reversed(undo):
    if old is None:del last[p]
    else:last[p]=old
   del letters[l0:];del poses[p0:]
   if fresh:del rules[key]
   if stop:return
 dfs(0,0)
 return dict(root=root,status=stop or 'EXHAUSTED',nodes=nodes,conflicts=conflicts,max_macros=maxdepth,best=best)
if __name__=='__main__':
 start=time.time();results=[]
 for root in 'RL':
  r=search(root);results.append(r);print({k:v for k,v in r.items()if k!='best'},flush=True)
 (HERE/'position_state_controllers.json').write_text(json.dumps(dict(results=results,seconds=time.time()-start),indent=2))
