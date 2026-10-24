"""Lazy exact search for finite-control k9,a3 inflation candidates.
Control modes: heading or time index modulo q. A cap is UNKNOWN.
"""
import json,pathlib,sys,collections,time
from search_complementary_roots import D
HERE=pathlib.Path(__file__).resolve().parent
sys.setrecursionlimit(20000)
def search(opts,mode='heading',q=4,nodecap=1000000,depthcap=1000):
 poses=[(0,0,0)];letters=[];last={};assign={};choices=[];nodes=0;stop=None;leaves=[];counts=collections.Counter();maxdepth=0;best=None;latest_conflict=0
 def key(n,c):
  if mode=='heading':return c,poses[n][2]
  if mode=='time':return c,n%q
  z=0
  while n:
   n,d=divmod(n,9);z+=d if mode=='digit'else int(d!=0)
  return c,z%q
 def append(w):
  nonlocal latest_conflict
  undo=[];l0=len(letters);p0=len(poses)
  for c in w:
   x,y,h=poses[-1];p=x,y;old=last.get(p)
   if old is not None and old[0]==c:
    z=dict(assigned=[(a,b,v)for(a,b),v in sorted(assign.items())],time=len(letters),earlier=old[1],cell=p,turn=c)
    latest_conflict=max(latest_conflict,z['time'])
    if len(leaves)<10000:leaves.append(z)
    counts['conflict_leaves']+=1;counts['full_assignments_excluded']+=9**(2*q-len(assign))
    rollback(undo,l0,p0);return None
   undo.append((p,old));last[p]=(c,len(letters));letters.append(c);h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];poses.append((x+dx,y+dy,h))
  return undo,l0,p0
 def rollback(undo,l0,p0):
  for p,v in reversed(undo):
   if v is None:del last[p]
   else:last[p]=v
  del letters[l0:];del poses[p0:]
 def dfs(n):
  nonlocal nodes,stop,maxdepth,best
  nodes+=1
  if n>maxdepth:
   maxdepth=n;best=dict(macros=n,assigned=[(a,b,v)for(a,b),v in sorted(assign.items())],choices=choices.copy(),word=''.join(letters))
  if n>=depthcap:stop='DEPTH_CAP';return
  if nodes>=nodecap:stop='NODE_CAP';return
  cs='RL'if n==0 else letters[n]
  for c in cs:
   z=key(n,c);old=z in assign
   ws=[assign[z]]if old else opts[c]
   for w in ws:
    if n==0 and w[0]!=c:continue
    if not old:assign[z]=w
    sv=append(w)
    if sv is not None:
     choices.append(w);x,y,h=poses[n+1];assert poses[-1]==(3*x,3*y,h)
     dfs(n+1);choices.pop();rollback(*sv)
    if not old:del assign[z]
    if stop:return
 dfs(0)
 return dict(mode=mode,q=q,status=stop or'EXHAUSTED',nodes=nodes,maxdepth=maxdepth,counts=dict(counts),latest_conflict=latest_conflict,stored_leaf_limit=10000,best=best,leaves=leaves)
if __name__=='__main__':
 mode=sys.argv[1]if len(sys.argv)>1 else'heading';q=int(sys.argv[2])if len(sys.argv)>2 else 4;cap=int(sys.argv[3])if len(sys.argv)>3 else 1000000
 r=next(z for z in json.load(open(HERE/'free_inflations_k9.json'))['results']if z['scale']==[3,0]);start=time.time();out=search(r['images'],mode,q,cap);out['seconds']=time.time()-start
 name=f'controlled_inflations_{mode}{q}';(HERE/(name+'.json')).write_text(json.dumps(out));print(json.dumps({k:v for k,v in out.items()if k not in('leaves','best')},indent=2))
