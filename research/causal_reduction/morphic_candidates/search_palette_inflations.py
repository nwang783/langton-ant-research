"""Arbitrary-control inflation with a bounded image palette, no automaton assumed."""
import json,pathlib,collections,sys,time
from search_complementary_roots import D
HERE=pathlib.Path(__file__).resolve().parent
sys.setrecursionlimit(10000)
def search(O,limits,depthcap=9,nodecap=1000000):
 poses=[(0,0,0)];letters=[];last={};used={'R':set(),'L':set()};choices=[];nodes=0;stop=None;latest=0;maxdepth=0;best=None;counts=collections.Counter()
 def rollback(undo,l0,p0):
  for p,v in reversed(undo):
   if v is None:del last[p]
   else:last[p]=v
  del letters[l0:];del poses[p0:]
 def append(w):
  nonlocal latest
  undo=[];l0=len(letters);p0=len(poses)
  for c in w:
   x,y,h=poses[-1];p=x,y;old=last.get(p)
   if old is not None and old[0]==c:
    latest=max(latest,len(letters));counts['conflicts']+=1;rollback(undo,l0,p0);return None
   undo.append((p,old));last[p]=(c,len(letters));letters.append(c);h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];poses.append((x+dx,y+dy,h))
  return undo,l0,p0
 def dfs(n):
  nonlocal nodes,stop,maxdepth,best
  nodes+=1
  if nodes%1000000==0:print('PROGRESS',nodes,maxdepth,flush=True)
  if n>maxdepth:maxdepth=n;best=dict(macros=n,choices=choices.copy(),word=''.join(letters),palette={c:sorted(v)for c,v in used.items()})
  if n>=depthcap:stop='DEPTH_CAP';return
  if nodes>=nodecap:stop='NODE_CAP';return
  for c in('RL'if n==0 else letters[n]):
   for w in O[c]:
    if n==0 and w[0]!=c:continue
    new=w not in used[c]
    if new and len(used[c])>=limits[c]:continue
    if new:used[c].add(w)
    sv=append(w)
    if sv is not None:
     choices.append(w);x,y,h=poses[n+1];assert poses[-1]==(3*x,3*y,h);dfs(n+1);choices.pop();rollback(*sv)
    if new:used[c].remove(w)
    if stop:return
 dfs(0)
 return dict(limits=limits,status=stop or'EXHAUSTED',nodes=nodes,maxdepth=maxdepth,latest_conflict=latest,counts=dict(counts),best=best)
if __name__=='__main__':
 a=int(sys.argv[1]);b=int(sys.argv[2]);depth=int(sys.argv[3])if len(sys.argv)>3 else 9;cap=int(sys.argv[4])if len(sys.argv)>4 else 1000000
 O=next(z['images']for z in json.load(open(HERE/'free_inflations_k9.json'))['results']if z['scale']==[3,0]);t=time.time();out=search(O,{'R':a,'L':b},depth,cap);out['seconds']=time.time()-t
 (HERE/f'palette_inflations_{a}_{b}.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items()if k!='best'},indent=2))
