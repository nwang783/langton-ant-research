from pathlib import Path
from collections import Counter,deque
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'word_stabilization/foreign_tangent_clock_frozen_20261023_2123';man=json.loads((D/'manifest.json').read_text());a=json.loads((D/'check_foreign_tangent_graph_clock.json').read_text())
for p,h in man['files'].items():assert hashlib.sha256((D/p).read_bytes()).hexdigest()==h
for p,h in man['dependencies'].items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==h
G=json.loads((R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text());N=G['classes']*2;edges=[]
for k,(s,l,t)in enumerate(G['quotient_edges']):
 for c in (0,1):edges.append((2*s+c,2*t+(l==1),int(l==1)+(2-4*c)*int(l>=4),int(l>=4),k))
assert N==428 and len(edges)==1986 and edges==list(map(tuple,a['lifted_edges']))
p=a['clock_potential'];e=a['foreign_rate_potential'];assert len(p)==len(e)==N
assert Counter(p)==Counter({0:222,-1:70,-2:136});assert max(e)-min(e)==857
assert all(w+p[s]-p[t]>=0 and N*w-f+e[s]-e[t]>=0 for s,t,w,f,k in edges)
tight=[x for x in edges if x[2]+p[x[0]]-p[x[1]]==0];assert len(tight)==746
adj=[set()for _ in range(N)]
for s,t,w,f,k in tight:adj[s].add(t)
reach=[]
for start in range(N):
 seen={start};todo=[start]
 while todo:
  s=todo.pop()
  for t in adj[s]-seen:seen.add(t);todo.append(t)
 reach.append(seen)
cl=a['zero_reduced_SCC_class']
assert all((cl[s]==cl[t])==(t in reach[s]and s in reach[t])for s in range(N)for t in range(N))
assert all(not f or s not in reach[t]for s,t,w,f,k in tight)
# Recompute finite potentials independently, reverse edge traversal order.
def pot(cost):
 d=[0]*N
 for k in range(N):
  changed=False
  for s,t,w,f,i in reversed(edges):
   x=d[s]+cost(w,f)
   if x<d[t]:d[t]=x;changed=True
  if not changed:return d
 raise AssertionError('negative cycle')
assert pot(lambda w,f:w)==p and pot(lambda w,f:N*w-f)==e
ids=[21,232,866]*2;state=(9,0,0);states=[state];W=T=0
for i in ids:
 s,l,t=G['quotient_edges'][i];q,c,h=state;assert s==q;W+=int(l==1)+(2-4*c)*int(l>=4);T+=int(l>=4);state=(t,int(l==1),(h+(3 if l==1 else 2 if l>=4 else 0))%4);states.append(state)
assert state==states[0]and(W,T)==(4,2);assert states==list(map(tuple,a['restored_heading_positive_graph_cycle']['states_q_prevC_heading']))
out=dict(status='PASS exact inherited graph no-negative/foreign-zero-cycle and path-rate certificates',manifest_sha256=hashlib.sha256((D/'manifest.json').read_bytes()).hexdigest(),states=N,edges=len(edges),tight_edges=len(tight),potential_histogram=dict(Counter(p)),path_rate_multiplier=N,path_fringe=857,positive_cycle=ids,analytic='Nonnegative reduced costs exclude negative cycles. Independent all-vertex reachability reconstructs the entire tight SCC equivalence and excludes every foreign tight edge from a cycle. The second potential sums on every finite walk to T_foreign<=428W+857. Infinite foreign count therefore forces unbounded positive W without a periodic-orbit assumption.',scope='Inherited214 graph only, not all physical seven-word factors. No physical realization, simple proxy or capture inference. A nonzero initial previous-C bit accounts for an incoming-boundary wrap; geometric finite-subpath tangent formulas must retain that endpoint convention.',reproduction='Frozen checker uses original two-level relative-root layout; replay original word_stabilization/check_foreign_tangent_graph_clock.py or this independent checker, rather than directly executing the deeper frozen copy.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(N,len(edges),len(tight),max(e)-min(e))
