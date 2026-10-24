"""Exact SCC condensation, black-mass rank, and compressed cap7 returns.
Bounded-core counting is CONDITIONAL on separately proved <=11 internal steps.
No first-return profile expansion.
"""
from pathlib import Path
from collections import deque
import json
P=Path(__file__).parent;J=json.loads((P/'component_kernel_M7_compact.json').read_text());T=J['transitions'];n=J['summary']['active_states'];Q=json.loads((P/'cap7_structure_probe.json').read_text())['cycle_witness'];cy=Q['indices'];S={T[z]['source']for z in cy};assert len(S)==6;g0=min(S);group={u:(g0 if u in S else u)for u in range(1,n)};G=set(group.values());adj={g:[]for g in G};indeg={g:0 for g in G};inner=[]
for z,t in enumerate(T):
 u,v=t['source'],t['target']
 if not u or not v:continue
 a,b=group[u],group[v]
 if a==b:assert u in S and v in S;inner.append(z)
 else:adj[a].append((z,b));indeg[b]+=1
assert sorted(inner)==sorted(cy)
queue=deque(sorted(g for g in G if not indeg[g]));order=[]
while queue:
 g=queue.popleft();order.append(g)
 for z,b in adj[g]:
  indeg[b]-=1
  if not indeg[b]:queue.append(b)
assert len(order)==len(G)
# Offsets make each of the six internal inequalities tight for multiplier3.
a={u:0 for u in range(1,n)};u=T[cy[0]]['source'];val=8
for z in cy:
 t=T[z];assert t['source']==u;a[u]=val;val-=4 if t['turn']=='R'else-2;u=t['target']
assert val==8 and min(a[u]for u in S)==0
b={}
for g in reversed(order):b[g]=max([0]+[(4 if T[z]['turn']=='R'else-2)+a[T[z]['target']]-a[T[z]['source']]+b[h]for z,h in adj[g]])
A=[0]+[b[group[u]]+a[u]for u in range(1,n)]
for t in T:
 if t['source']and t['target']:assert A[t['source']]-A[t['target']]-3*(1 if t['turn']=='R'else-1)>=1
# Count and bound empty-return paths in the graph with at most11 internal core edges.
fulladj=[[]for _ in range(n)]
for z,t in enumerate(T):fulladj[t['source']].append(z)
N=[0]*n;L=[0]*n;N[0]=1;inside={T[z]['source']:z for z in cy}
for g in reversed(order):
 if g!=g0:
  N[g]=sum(N[T[z]['target']]for z in fulladj[g]);L[g]=max([0]+[1+L[T[z]['target']]for z in fulladj[g]])
 else:
  for root in S:
   u=root;cnt=0;longest=0
   for k in range(12):
    for z in fulladj[u]:
     v=T[z]['target']
     if v not in S:cnt+=N[v];longest=max(longest,k+1+L[v])
    u=T[inside[u]]['target']
   N[root]=cnt;L[root]=longest
count=sum(N[T[z]['target']]for z in fulladj[0]);maxlen=max(1+L[T[z]['target']]for z in fulladj[0]);maxfringe=max(L)
# Longest nonempty walk with12 core cuts, using weighted condensation nodes.
F={}
for g in reversed(order):F[g]=(12 if g==g0 else 1)+max([0]+[F[h]for z,h in adj[g]])
out={'status':'AUTHOR_EXACT_SCC_AND_RANK_CERTIFICATES_PENDING_AUDIT','states':n,'edges':len(T),'unique_nonempty_scc':sorted(S),'internal_edge_indices':cy,'condensation_topological_order':order,'black_mass_multiplier':3,'nonempty_state_offsets':A,'maximum_offset':max(A),'conditional_core_internal_step_bound':11,'conditional_empty_return_path_count':count,'conditional_longest_return_path':maxlen,'conditional_maximum_nonempty_cuts':max(F.values()),'scope':'SCC/rank are pure kernel certificates. Bounded-core count and uniform fringe need the separate physical double-loop contradiction; no cap7 exit theorem.'}
(P/'cap7_core_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print({k:v for k,v in out.items()if k not in('condensation_topological_order','nonempty_state_offsets')})
