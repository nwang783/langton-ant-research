"""Falsification control for a proposed DC seed-hull confinement; no theorem."""
from pathlib import Path
import json
WORDS={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR'}
DIR=[(0,1),(1,0),(0,-1),(-1,0)]
NORMALS=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
def run(depth=60,fuel=12,limit=2000000):
 last={};seed=set();reads={};nodes=0;best=[-999]*8;witness=[None]*8;maxdep=0
 def rec(p,h,w):
  nonlocal nodes,maxdep
  nodes+=1;maxdep=max(maxdep,len(w))
  if seed:
   for k,(a,b) in enumerate(NORMALS):
    f=max(a*x+b*y for x,y in reads)-max(a*x+b*y for x,y in seed)
    if f>best[k]:best[k]=f;witness[k]={'word':w,'seed':sorted(seed),'head':p,'gap':f}
  if nodes>=limit or len(w)>=depth:return
  for letter,raw in WORDS.items():
   q=p;g=h;undo=[];added=[];ok=True
   for c in raw:
    old=last.get(q)
    if old==c:ok=False;break
    if old is None and c=='L':seed.add(q);added.append(q)
    undo.append((q,old));last[q]=c;reads[q]=reads.get(q,0)+1
    g=(g+(1 if c=='R' else-1))%4;dx,dy=DIR[g];q=(q[0]+dx,q[1]+dy)
    if len(seed)>fuel:ok=False;break
   if ok:rec(q,g,w+letter)
   for q,old in reversed(undo):
    reads[q]-=1
    if not reads[q]:del reads[q]
    if old is None:del last[q]
    else:last[q]=old
   for q in added:seed.remove(q)
   if nodes>=limit:break
 rec((0,0),0,'')
 return {'depth':depth,'fuel':fuel,'limit':limit,'nodes':nodes,'max_depth':maxdep,'complete':nodes<limit,'normals':NORMALS,'max_gaps':best,'witnesses':witness}
if __name__=='__main__':
 r=run();Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2));print({k:v for k,v in r.items() if k!='witnesses'})
