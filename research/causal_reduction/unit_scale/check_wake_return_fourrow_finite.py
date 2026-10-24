"""Solver-free exhaustive chronology replay for the signed LK four-row caps.
The cap-free bound is a separate dependency. Here every possible per-site
incoming-heading history is enumerated, then actual ordinal edge matchings,
cycle winding, and strict local chronological order are checked literally.
No fixed output, head location, or positive use of the boundary is assumed.
"""
import itertools,json,collections
from pathlib import Path
P=Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
cert=json.loads((P/'wake_return_flow_bounds_h4_off-2.json').read_text())
ps=list(map(tuple,cert['positions']));ix={p:i for i,p in enumerate(ps)}
caps=[x['integer_upper']for x in cert['bounds'][1:]]
W=set(map(tuple,json.loads((P/'shifted_reverse104_bulk.json').read_text())['wake_black_classes']))
I=[int((x-y,x%2)in W)for x,y in ps]
opts=[]
for i,p in enumerate(ps):
 axis=(1-sum(p))%2;v=[]
 for n in range(caps[i]+1):
  for hs in itertools.product((axis,axis+2),repeat=n):
   outs=tuple((h+(1 if(j+I[i])%2==0 else-1))%4 for j,h in enumerate(hs))
   v.append((hs,outs))
 opts.append(v)
counts=collections.Counter();examples={};survivors=[]
for histories in itertools.product(*opts):
 counts['assignments']+=1
 N=sum(len(a)for a,b in histories)
 if not N or N>12 or N%4:
  counts['length_reject']+=1;continue
 # Each representative's h port streams match by their rank, in order.
 incoming={(i,h):[(i,j)for j,hh in enumerate(a)if hh==h]for i,(a,b)in enumerate(histories)for h in range(4)}
 outgoing={(i,h):[(i,j)for j,hh in enumerate(b)if hh==h]for i,(a,b)in enumerate(histories)for h in range(4)}
 graph={};bad=False
 for i,p in enumerate(ps):
  for h,(dx,dy)in enumerate(D):
   x,y=p[0]+dx,p[1]+dy;k=x//2;q=(x%2,y-2*k);v=-k
   target=ix.get(q);src=outgoing[i,h];dst=incoming.get((target,h),[])
   if len(src)!=len(dst):bad=True;break
   for u,w in zip(src,dst):graph[u]=(w,v)
  if bad:break
 if bad or len(graph)!=N or len({v[0]for v in graph.values()})!=N:
  counts['edge_reject']+=1;continue
 counts['edge_feasible']+=1
 todo=set(graph);cycles=[]
 while todo:
  u=min(todo);cycle=[];v=u
  while v in todo:
   todo.remove(v);w,z=graph[v];cycle.append((v,z));v=w
  assert v==u
  cycles.append(cycle)
 if len(cycles)!=1 or sum(z for u,z in cycles[0])!=1:
  counts['cycle_reject']+=1
  examples.setdefault('cycles',[]).append({'histories':histories,'cycles':cycles})
  continue
 counts['one_cycle']+=1
 t={cycles[0][0][0]:0}
 for u,z in cycles[0]:
  w,_=graph[u];tw=t[u]+1-z*N
  if w in t:assert t[w]==tw
  else:t[w]=tw
 if any(t[i,j+1]-t[i,j]<4 for i,(a,b)in enumerate(histories)for j in range(len(a)-1)):
  counts['chronology_reject']+=1;continue
 survivors.append({'histories':histories,'t':[[i,j,x]for(i,j),x in sorted(t.items())]})
out=dict(scope=__doc__,positions=ps,input=I,caps=caps,domain_sizes=list(map(len,opts)),counts=dict(counts),examples=examples,survivors=survivors)
(P/'wake_return_fourrow_finite.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in('examples',)},indent=2))
assert not survivors
