"""Joint synthesis of a two-state 9-automatic controller and four turn images.
T(0,0)=0; c(9n+j)=T(c(n),j). Unknown transitions and images branch lazily.
Finite conflicts are exact; node/depth caps are UNKNOWN.
"""
import json,pathlib,collections,time,sys
from search_complementary_roots import D
HERE=pathlib.Path(__file__).resolve().parent
sys.setrecursionlimit(20000)
def search(opts,nodecap=2000000,depthcap=1000):
 poses=[(0,0,0)];letters=[];last={};images={};T={(0,0):0};choices=[];nodes=0;stop=None;counts=collections.Counter();maxdepth=0;latest=0;best=None;examples=[]
 def controller(n):
  ds=[]
  while n:n,d=divmod(n,9);ds.append(d)
  s=0
  for d in reversed(ds):
   if(s,d)not in T:return None,(s,d)
   s=T[s,d]
  return s,None
 def rollback(undo,l0,p0):
  for p,v in reversed(undo):
   if v is None:del last[p]
   else:last[p]=v
  del letters[l0:];del poses[p0:]
 def snapshot():return dict(images=[(c,s,w)for(c,s),w in sorted(images.items())],controller=[(s,j,t)for(s,j),t in sorted(T.items())])
 def append(w):
  nonlocal latest
  undo=[];l0=len(letters);p0=len(poses)
  for c in w:
   x,y,h=poses[-1];p=x,y;old=last.get(p)
   if old is not None and old[0]==c:
    latest=max(latest,len(letters));counts['conflict_leaves']+=1;counts['full_rooted_models_excluded']+=9**(4-len(images))*2**(18-len(T))
    if len(examples)<100:examples.append(dict(**snapshot(),time=len(letters),earlier=old[1],cell=p,turn=c))
    rollback(undo,l0,p0);return None
   undo.append((p,old));last[p]=(c,len(letters));letters.append(c);h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];poses.append((x+dx,y+dy,h))
  return undo,l0,p0
 def dfs(n):
  nonlocal nodes,stop,maxdepth,best
  nodes+=1
  if n>maxdepth:maxdepth=n;best=dict(**snapshot(),macros=n,choices=choices.copy(),word=''.join(letters))
  if nodes>=nodecap:stop='NODE_CAP';return
  if n>=depthcap:stop='DEPTH_CAP';return
  phase,missing=controller(n)
  if missing is not None:
   for t in(0,1):
    T[missing]=t;dfs(n);del T[missing]
    if stop:return
   return
  for c in('RL'if n==0 else letters[n]):
   z=c,phase;old=z in images
   for w in([images[z]]if old else opts[c]):
    if n==0 and w[0]!=c:continue
    if not old:images[z]=w
    sv=append(w)
    if sv is not None:
     choices.append(w);x,y,h=poses[n+1];assert poses[-1]==(3*x,3*y,h);dfs(n+1);choices.pop();rollback(*sv)
    if not old:del images[z]
    if stop:return
 dfs(0)
 return dict(status=stop or'EXHAUSTED',nodes=nodes,maxdepth=maxdepth,latest_conflict=latest,counts=dict(counts),best=best,example_leaves=examples)
if __name__=='__main__':
 cap=int(sys.argv[1])if len(sys.argv)>1 else 2000000
 O=next(z['images']for z in json.load(open(HERE/'free_inflations_k9.json'))['results']if z['scale']==[3,0]);start=time.time();out=search(O,cap);out['seconds']=time.time()-start;out['complete_rooted_class_size']=10*9**3*2**17
 if out['status']=='EXHAUSTED':assert out['counts']['full_rooted_models_excluded']==out['complete_rooted_class_size']
 (HERE/'two_state_control_inflations.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items()if k not in('best','example_leaves')},indent=2))
