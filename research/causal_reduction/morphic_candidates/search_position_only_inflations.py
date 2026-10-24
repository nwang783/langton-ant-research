"""Pure position-only inflation: NO heading equality assumption.
Every occurrence may choose any matching internally feasible image.
EXHAUSTED is a complete finite tree; a cap is UNKNOWN only.
"""
import json,pathlib,sys,collections,itertools,time
from free_inflation_generic_csp import trace,seed,rotate
HERE=pathlib.Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
def mul(a,p):return a[0]*p[0]-a[1]*p[1],a[0]*p[1]+a[1]*p[0]
def search(k,a,byend,nodecap=100000,depthcap=1000):
 poses=[(0,0,0)];letters=[];last={};choices=[];nodes=0;stop=None;maxdepth=0;latest=0;best=None;leaves=0
 def rollback(u,l,p):
  for q,v in reversed(u):
   if v is None:del last[q]
   else:last[q]=v
  del letters[l:];del poses[p:]
 def dfs(n):
  nonlocal nodes,stop,maxdepth,latest,best,leaves
  nodes+=1
  if n>maxdepth:maxdepth=n;best=dict(choices=choices.copy(),word=''.join(letters))
  if nodes>=nodecap:stop='NODE_CAP';return
  if n>=depthcap:stop='DEPTH_CAP';return
  for c in('RL'if n==0 else letters[n]):
   x,y,h=poses[n];H=poses[-1][2];dx,dy=D[(h+(1 if c=='R'else-1))%4];target=mul(a,(dx,dy));local=rotate(*target,(-H)%4)
   for w in byend.get(local,[]):
    if n==0 and w[0]!=c:continue
    u=[];l0=len(letters);p0=len(poses);okay=True
    for ch in w:
     X,Y,H=poses[-1];q=X,Y;old=last.get(q)
     if old==ch:latest=max(latest,len(letters));leaves+=1;okay=False;break
     u.append((q,old));last[q]=ch;letters.append(ch);H=(H+(1 if ch=='R'else-1))%4;DX,DY=D[H];poses.append((X+DX,Y+DY,H))
    if okay:
     assert poses[-1][:2]==mul(a,poses[n+1][:2]);choices.append(w);dfs(n+1);choices.pop()
    rollback(u,l0,p0)
    if stop:return
 dfs(0)
 return dict(scale=a,status=stop or'EXHAUSTED',nodes=nodes,max_macros=maxdepth,latest_conflict=latest,conflicts=leaves,best=best)
def run(k):
 by=collections.defaultdict(list);scales=set()
 for tup in itertools.product('RL',repeat=k):
  w=''.join(tup)
  if seed(w)is None:continue
  p=trace(w)[1][:2];by[p].append(w);sign=1 if w[0]=='R'else-1;a=sign*p[0],sign*p[1]
  if sum(x*x for x in a)>1:scales.add(a)
 results=[]
 for a in sorted(scales):
  r=search(k,a,by);results.append(r);print(k,a,r['status'],r['nodes'],r['max_macros'],flush=True)
  (HERE/f'position_only_k{k}.json').write_text(json.dumps(dict(k=k,results=results),indent=2))
 return results
if __name__=='__main__':
 sys.setrecursionlimit(10000)
 for k in range(int(sys.argv[1]),int(sys.argv[2])+1):run(k)
