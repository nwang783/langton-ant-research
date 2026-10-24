"""Pure geometric inflation, with arbitrary image choices rather than a substitution.
Every complete search is finite exact branching; all capped searches are UNKNOWN.
"""
import sys,json,pathlib,collections,itertools,time
from search_complementary_roots import spec,D
sys.setrecursionlimit(20000)
HERE=pathlib.Path(__file__).resolve().parent

def search(k,a,b,opts,nodecap,depthcap):
 last={};letters=[];poses=[(0,0,0)];choices=[];firstL=set();nodes=0;maxdepth=0;best=None;counts=collections.Counter();levels=collections.Counter();stop=None;leaves=[]
 def rollback(undo,newL,p0,l0):
  for p,old in reversed(undo):
   if old is None:last.pop(p)
   else:last[p]=old
  for p in newL:firstL.remove(p)
  del poses[p0:];del letters[l0:]
 def append(w):
  undo=[];newL=[];p0=len(poses);l0=len(letters)
  for c in w:
   x,y,h=poses[-1];p=x,y;old=last.get(p)
   if old is not None and old[0]==c:
    counts['alternation_conflict']+=1
    if len(leaves)<100:leaves.append(dict(macros=choices+[w],time=len(letters),earlier=old[1],cell=p,turn=c))
    rollback(undo,newL,p0,l0);return None
   if old is None and c=='L':firstL.add(p);newL.append(p)
   undo.append((p,old));last[p]=(c,len(letters));letters.append(c);h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];poses.append((x+dx,y+dy,h))
  return undo,newL,p0,l0
 def dfs(n):
  nonlocal nodes,maxdepth,best,stop
  nodes+=1;levels[n]+=1
  if n>maxdepth:maxdepth=n;best=dict(macros=n,choices=list(choices),turns=''.join(letters),seed=sorted(firstL),pose=poses[-1])
  if n>=depthcap:stop='DEPTH_CAP';return
  if nodes>=nodecap:stop='NODE_CAP';return
  ws=([w for c in'RL'for w in opts[c]if w[0]==c]if n==0 else opts[letters[n]])
  for w in ws:
   saved=append(w)
   if saved is None:continue
   choices.append(w);x,y,h=poses[n+1];assert poses[-1]==(a*x-b*y,b*x+a*y,h)
   dfs(n+1);choices.pop();rollback(*saved)
   if stop:return
 dfs(0)
 return dict(status=stop or'EXHAUSTED',nodes=nodes,maxdepth=maxdepth,counts=dict(counts),levels=dict(levels),best=best,example_leaves=leaves)

if __name__=='__main__':
 k=int(sys.argv[1])if len(sys.argv)>1 else 7
 nodecap=int(sys.argv[2])if len(sys.argv)>2 else 200000
 depthcap=int(sys.argv[3])if len(sys.argv)>3 else 256
 groups=collections.defaultdict(list);results=[];start=time.time()
 for z in itertools.product('RL',repeat=k):
  w=''.join(z);g=spec(w)
  if g is not None:groups[g].append(w)
 for(h,a,b),us in sorted(groups.items()):
  if h!=1 or a*a+b*b<=1:continue
  vs=groups.get((3,-a,-b),[])
  if not vs:continue
  opts={'R':us,'L':vs};r=dict(scale=[a,b],images=opts)
  if max(2*w.count('R')-k for w in us)<=1 and max(2*w.count('R')-k for w in vs)<=-1:r.update(status='NONINCREASING_SCALE_MASS')
  else:r.update(search(k,a,b,opts,nodecap,depthcap))
  results.append(r);print('SCALE',k,a,b,r['status'],r.get('nodes'),r.get('maxdepth'),'fuel',len(r.get('best',{}).get('seed',[]))if r.get('best')else None,flush=True)
 out=dict(k=k,nodecap=nodecap,depthcap=depthcap,results=results,seconds=time.time()-start)
 (HERE/f'free_inflations_k{k}.json').write_text(json.dumps(out,indent=2));print('DONE',k,len(results),time.time()-start,flush=True)
