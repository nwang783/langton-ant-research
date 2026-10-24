import sys,json
sys.path.insert(0,'audits');import check_genealogy_saturation_roles_independent as G
from pathlib import Path
F=G.ROOT/'core_periodicity_new/genealogy_role_speed_frozen_20261023_0840';P=json.loads((F/'optimal_speed_root_potential.json').read_text())['P'];E=[e for e in G.fundamental if 2*e[2]+P[e[0]]-P[e[1]]-3*e[3]==0]
adj=[set()for _ in G.roles]
for u,v,n,d in E:adj[u].add(v)
reach=[]
for u in range(len(adj)):
 seen=set();todo=[u]
 while todo:
  v=todo.pop()
  if v in seen:continue
  seen.add(v);todo+=list(adj[v]-seen)
 reach.append(seen)
unseen=set(range(len(adj)));components=[]
while unseen:
 u=next(iter(unseen));s={v for v in reach[u]if u in reach[v]};unseen-=s
 if len(s)>1 or u in adj[u]:components.append(s)
print('TIGHT',len(E),'CYCLIC_COMPONENTS',len(components))
for S in components:
 print('ROLES',[(i,(a,G.xy(z),h))for i in sorted(S)for a,z,h in[G.roles[i]]]);print('EDGES',sorted(e for e in E if e[0]in S and e[1]in S))
assert len(E)==205 and len(components)==1
expected={G.index[6,0j,2],G.index[0,2+0j,3],G.index[5,2+5j,0]}
assert components[0]==expected
u,v,w=G.index[6,0j,2],G.index[0,2+0j,3],G.index[5,2+5j,0]
# Keep one previous edge. Delete only the jointly forbidden consecutive pair.
from collections import deque
adj2=[set()for _ in E];indeg=[0]*len(E)
for i,a in enumerate(E):
 for j,b in enumerate(E):
  if a[1]==b[0] and not(a[0]==u and a[1]==v and b[1]==w):adj2[i].add(j);indeg[j]+=1
ready=deque(i for i,d in enumerate(indeg)if not d);order=[]
while ready:
 i=ready.popleft();order.append(i)
 for j in adj2[i]:
  indeg[j]-=1
  if not indeg[j]:ready.append(j)
assert len(order)==len(E)
rank=[0]*len(E)
for i in reversed(order):rank[i]=max([0]+[1+rank[j]for j in adj2[i]])
out={'status':'PASS exact2/3 zero-margin graph and one-edge-memory acyclicity','zero_margin_edges':len(E),'cyclic_components':[sorted(s)for s in components],'forbidden_consecutive_roles':[u,v,w],'max_consecutive_tight_edges':max(rank)+1,'scope':'Uses independently signed LH joint history exclusion. Individual edges are not deleted. No all-ancestry bound or capture.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
