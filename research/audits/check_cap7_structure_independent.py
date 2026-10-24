from pathlib import Path
from collections import Counter,deque
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'reframe_finite_seed_2026-10-24'
s=(SELF.parent/'check_cap6_full_fuel_and_composition_independent.py').read_text().split('adj=[[]for _ in states]')[0]
s=s.replace('range(1,7)','range(1,8)').replace('M=6;','M=7;').replace('component_kernel_M6.json','component_kernel_M7_compact.json').replace('len(states)==14116 and len(T)==12060','len(states)==72284 and len(T)==63244')
ns={'__file__':str(SELF)};exec(s,ns);T,states,ends=ns['T'],ns['states'],ns['ends'];N=len(states)
# Passive shapes are complete edge components modulo lattice translations and rotations.
def typ(C):
 if not C:return None
 edges=[ends(complex(*q),0)for q in C];anchor=edges[0][0];base=[]
 for e in edges:
  row=[]
  for v in e:
   z=v-anchor;x=int(z.real+z.imag);y=int(z.real-z.imag);assert x%4==y%4==0;row.append(complex(x//4,y//4))
  base.append(row)
 ans=[]
 for h in range(4):
  e=[[v*1j**h for v in row]for row in base];x=min(v.real for row in e for v in row);y=min(v.imag for row in e for v in row)
  ans.append(tuple(sorted(tuple(sorted((int(v.real-x),int(v.imag-y))for v in row))for row in e)))
 return min(ans)
author=json.loads((D/'component_kernel_M7_compact.json').read_text());maps={};inverse={}
for t,z in zip(author['transitions'],T):
 for field,coords in [('consume',z[4]),('emit',z[6])]:
  tp=typ(coords);idx=t[field];assert(tp is None)==(idx is None)
  if idx is None:continue
  assert maps.setdefault(idx,tp)==tp and inverse.setdefault(tp,idx)==idx
assert len(maps)==550
# Independently obtain all nonempty SCCs rather than accepting the proposed six states.
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
pairs=[(z[0],z[1])for z in T if z[0]and z[1]];graph=csr_matrix(([1]*len(pairs),([a for a,b in pairs],[b for a,b in pairs])),shape=(N,N))
_,labs=connected_components(graph,directed=True,connection='strong');groups={}
for u,l in enumerate(labs):
 if u:groups.setdefault(int(l),[]).append(u)
cyclic=[v for v in groups.values()if len(v)>1 or graph[v[0],v[0]]];assert len(cyclic)==1;S=set(cyclic[0]);assert S=={98,299,635,6582,9707,41725}
inner=[i for i,z in enumerate(T)if z[0]in S and z[1]in S];assert len(inner)==6
cert=json.loads((D/'cap7_core_certificate.json').read_text());assert set(inner)==set(cert['internal_edge_indices']);A=cert['nonempty_state_offsets'];assert len(A)==N and min(A)==0 and max(A)==34
for z in T:
 if z[0]and z[1]:assert A[z[0]]-A[z[1]]-3*(1 if z[2]=='R'else-1)>=1
# Unroll each contiguous core visit to zero through eleven INTERNAL steps.
# This gives a separate finite DAG, not a materialized list of profiles.
nodes=[(u,0)for u in range(1,N)if u not in S]+[(u,k)for u in S for k in range(12)];ix={q:i for i,q in enumerate(nodes)};ad=[[]for q in nodes];deg=[0]*len(nodes);outgoing=[[]for u in range(N)]
for i,z in enumerate(T):outgoing[z[0]].append(i)
for i,(u,k)in enumerate(nodes):
 for ti in outgoing[u]:
  z=T[ti];v=z[1]
  if u in S and v in S:
   if k==11:continue
   target=ix[v,k+1]
  elif v:target=ix[v,0]
  else:target=None
  ad[i].append((target,z[2]));
  if target is not None:deg[target]+=1
queue=deque(i for i,d in enumerate(deg)if d==0);order=[]
while queue:
 i=queue.popleft();order.append(i)
 for v,c in ad[i]:
  if v is not None:
   deg[v]-=1
   if not deg[v]:queue.append(v)
assert len(order)==len(nodes)
counts=[0]*len(nodes);length=[0]*len(nodes);words=[None]*len(nodes)
for i in reversed(order):
 d=Counter()
 for v,c in ad[i]:
  if v is None:d[c]+=1
  else:
   for w,n in words[v].items():d[c+w]+=n
 words[i]=d;counts[i]=sum(d.values());length[i]=max(map(len,d),default=0)
root=Counter()
for ti in outgoing[0]:
 z=T[ti]
 if not z[1]:root[z[2]]+=1
 else:
  for w,n in words[ix[z[1],0]].items():root[z[2]+w]+=n
assert sum(root.values())==154794412 and len(root)==58 and max(map(len,root))==25
projection=json.loads((D/'cap7_turn_word_quotient.json').read_text());assert root==Counter(projection['word_counts'])
entries=1+sum(len(words[ix[u,0]])for u in range(1,N));maxwords=max([1]+[len(words[ix[u,0]])for u in range(1,N)])
assert(entries,maxwords)==(40432,22)
# Independent weighted condensation bound, permitting every nonempty start/end.
grp={u:min(S)if u in S else u for u in range(1,N)};gadj={g:set()for g in grp.values()};ind={g:0 for g in gadj}
for a,b in pairs:
 a,b=grp[a],grp[b]
 if a!=b and b not in gadj[a]:gadj[a].add(b);ind[b]+=1
queue=deque(g for g in gadj if not ind[g]);top=[]
while queue:
 g=queue.popleft();top.append(g)
 for v in gadj[g]:
  ind[v]-=1
  if not ind[v]:queue.append(v)
assert len(top)==len(gadj);long={}
for g in reversed(top):long[g]=(12 if g==min(S)else 1)+max([0]+[long[v]for v in gadj[g]])
assert max(long.values())==33
mf=json.loads((D/'cap7_structure_manifest.json').read_text())
for f,h in mf.items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
prior=SELF.with_name('check_cap7_nonempty_cycle_independent.json');assert hashlib.sha256(prior.read_bytes()).hexdigest()=='eeb583797cab6c2c09d3b5f6ee76b1035b49857e87a4b6b418d61299cf113dd8'
out={'status':'PASS exact cap-seven local kernel, unique core, rank and bounded-core word projection; NOT cap-seven exit','rooted_mass_counts':list(map(len,ns['lev'])),'states':N,'transitions':len(T),'passive_types':len(maps),'unique_nonempty_SCC':sorted(S),'internal_edges':inner,'mass_rank_multiplier':3,'max_offset':34,'unrolled_DAG_nodes':len(nodes),'bounded_return_count':sum(root.values()),'maximum_return_length':max(map(len,root)),'word_counts':dict(sorted(root.items(),key=lambda a:(len(a[0]),a[0]))),'word_entries':entries,'max_words_per_original_nonterminal':maxwords,'max_nonempty_cuts':max(long.values()),'source_hashes':mf,'analytic_review':[
'Rooted connected edge sets are freshly grown by adding every incident lattice edge. Every active cap7 state is covered, including isolated cursor/empty. Rotating/translating by actual physical pose preserves the fixed w lattice. R either joins an existing active vertex or imports ONE complete disjoint passive component from its opposite endpoint; L splits at most one complete passive component. Every possible allowed imported size and placement is freshly enumerated, not inferred from prior kernel counts.',
'Full geometric transition tuples match the author table as a multiset; the 550 passive type IDs agree bijectively with an independent translation/quarter-rotation canonicalization. Reflection is not silently identified.',
'The nonempty kernel has exactly one six-node cyclic SCC and exactly its six directed cycle edges. Every nonempty transition decreases A(C)+3*complete black mass by at least1. Finite support makes this a valid termination rank even if imports come from arbitrarily large historical archives, since each cap-preserving import is an explicitly complete bounded component and all other components are unchanged.',
'The previously independently replayed six-step component loop cannot be followed by its next required import. From an arbitrary cycle phase there are at most5 steps to the chosen anchor, then6 further internal steps before that contradiction. Thus at most11 internal steps,12 cuts per contiguous core visit. The condensation DAG prevents reentry without visiting empty. Independent weighted condensation gives33 total nonempty cuts.',
'An independently unrolled zero-through-eleven core-counter DAG gives154794412 abstract first-return paths and the exact58-word projection. These are overapproximations, not physical executions or composable resources. No154million-profile list is created. A rank/projection does not establish cap7 exit, attraction, or standard104 capture.'
]}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print({k:out[k]for k in ['states','transitions','passive_types','bounded_return_count','maximum_return_length','word_entries','max_nonempty_cuts']})
