"""Exact bounded-backbone search; UNKNOWNs are explicitly retained."""
import sys,time,json
from collections import Counter
from loop_decoration_solver import build,solve,assemble,verify,walk,HERE

def necklaces(n):
 a=[0]*(n+1)
 def rec(t,p):
  if t>n:
   if n%p==0:yield ''.join('RL'[z] for z in a[1:])
  else:
   a[t]=a[t-p];yield from rec(t+1,p)
   for j in range(a[t-p]+1,2):a[t]=j;yield from rec(t+1,t)
 yield from rec(1,1)

lo=int(sys.argv[1]) if len(sys.argv)>1 else 2;hi=int(sys.argv[2]) if len(sys.argv)>2 else 16
allresults=[];started=time.time()
for n in range(lo,hi+1,2):
 counts=Counter();unknown=[];sat=[];maxnodes=0;begin=time.time()
 for w in necklaces(n):
  counts['necklaces']+=1
  if (w.count('R')-w.count('L'))%4:continue
  ev,end=walk(w)
  if end[:2]==(0,0):continue
  counts['translating']+=1;o,eq,g,d=build(w,True);z,ans=solve(eq,g,False,limit=20000,timeout=2)
  counts[z['status']]+=1;maxnodes=max(maxnodes,z['nodes'])
  if ans is not None:
   ww=assemble(w,o,ans);v=verify(ww);rec=dict(backbone=w,word=ww,verified=v,solver=z);sat.append(rec);print('SAT',json.dumps(rec),flush=True)
  elif z['status']=='UNKNOWN':unknown.append(dict(backbone=w,solver=z))
  if counts['translating']%1000==0:print('PROGRESS',n,dict(counts),'elapsed',time.time()-begin,flush=True)
 rec=dict(backbone_length=n,counts=dict(counts),maximum_solver_nodes=maxnodes,seconds=time.time()-begin,unknown=unknown,sat=sat)
 allresults.append(rec);print('LENGTH',json.dumps(rec),flush=True)
 (HERE/f'backbones_{lo}_{hi}_results.json').write_text(json.dumps(dict(elapsed=time.time()-started,results=allresults),indent=2))
