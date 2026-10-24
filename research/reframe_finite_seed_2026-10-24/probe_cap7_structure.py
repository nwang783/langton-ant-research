"""Bounded structural probe only: no expansion of all first-return profiles."""
from component_kernel import kernel,OUT
from collections import deque
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
import json,time
st=time.time();states,mods,T=kernel(7);n=len(states);adj=[[]for _ in range(n)];indeg=[0]*n
for i,t in enumerate(T):
 adj[t['source']].append(i)
 if t['source']and t['target']:indeg[t['target']]+=1
q=deque(i for i in range(1,n)if not indeg[i]);order=[]
while q:
 u=q.popleft();order.append(u)
 for z in adj[u]:
  v=T[z]['target']
  if v:
   indeg[v]-=1
   if not indeg[v]:q.append(v)
result={'active_cap':7,'rooted_states':n,'passive_types':len(mods),'cap_preserving_transitions':len(T),'acyclic_after_deleting_empty':len(order)==n-1,'nonempty_kahn_processed':len(order),'elapsed_seconds':time.time()-st,'scope':'AUTHOR structural probe only; no physical recurrence or cap7 theorem.'}
if len(order)==n-1:
 count=[0]*n;longest=[0]*n
 for u in reversed(order):
  count[u]=sum(1 if T[z]['target']==0 else count[T[z]['target']]for z in adj[u]);longest[u]=max([0]+[1+(longest[T[z]['target']]if T[z]['target']else 0)for z in adj[u]])
 result['first_return_count_without_expanding']=sum(1 if T[z]['target']==0 else count[T[z]['target']]for z in adj[0]);result['longest_empty_avoiding_path']=max(longest)
 (OUT/'cap7_nonempty_dag_order.json').write_text(json.dumps(order,separators=(',',':'))+'\n')
else:
 tt=[t for t in T if t['source']and t['target']];g=csr_matrix(([1]*len(tt),([t['source']for t in tt],[t['target']for t in tt])),shape=(n,n));num,labels=connected_components(g,directed=True,connection='strong');cs={}
 for u,l in enumerate(labels):cs.setdefault(int(l),[]).append(u)
 cyc=[c for c in cs.values()if len(c)>1 or g[c[0],c[0]]!=0];result['nonempty_recurrent_scc_sizes']=sorted([len(c)for c in cyc]);result['nonempty_recurrent_scc_count']=len(cyc)
 # One shortest-edge-count witness found by DFS within the smallest cyclic SCC.
 S=set(min(cyc,key=len));on={};done=set();stack=[];path=[];found=None
 def dfs(u):
  global found
  on[u]=len(stack);stack.append(u)
  for z in adj[u]:
   v=T[z]['target']
   if v not in S:continue
   if v in on:found=path[on[v]:]+[z];return True
   if v not in done:
    path.append(z)
    if dfs(v):return True
    path.pop()
  stack.pop();on.pop(u);done.add(u);return False
 for u in S:
  if u not in done and dfs(u):break
 assert found is not None
 result['cycle_witness']={'indices':found,'word':''.join(T[z]['turn']for z in found),'transitions':[T[z]for z in found]}
(OUT/'cap7_structure_probe.json').write_text(json.dumps(result,indent=2)+'\n');(OUT/'component_kernel_M7_compact.json').write_text(json.dumps({'summary':{'active_states':n,'passive_types':len(mods),'transitions':len(T)},'transitions':T},separators=(',',':'))+'\n');print({k:v for k,v in result.items()if k!='cycle_witness'})
if 'cycle_witness'in result:print('cycle',result['cycle_witness']['word'])
