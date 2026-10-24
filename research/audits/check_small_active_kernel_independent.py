from pathlib import Path
from collections import Counter,deque
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'reframe_finite_seed_2026-10-24';p=SELF.parent/'check_cycle_birth_finite_fuel_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('cells=')[0],ns)
ends,component,step,wvertex=[ns[k]for k in('ends','component','step','wvertex')]
def xy(z):return(int(z.real),int(z.imag))
def key(C):return tuple(sorted(map(xy,C)))
root=1-1j;lattice=0
lev=[{frozenset()}]
for mass in range(1,5):
 nxt=set()
 for C in lev[-1]:
  vertices={root}|{v for q in C for v in ends(q,lattice)}
  for v in vertices:
   for dd in(1+1j,1-1j,-1+1j,-1-1j):
    q=(v+dd)/2;assert q.real.is_integer()and q.imag.is_integer()and v in ends(q,lattice)
    if q not in C:nxt.add(C|{q})
 lev.append(nxt)
assert list(map(len,lev))==[1,4,18,88,439]
allout={};transby={}
for M in(3,4):
 states=sorted(set().union(*lev[:M+1]),key=lambda C:(len(C),key(C)));ind={C:i for i,C in enumerate(states)};T=[]
 for C in states:
  V={root}|{v for q in C for v in ends(q,lattice)}
  ds=[frozenset()]
  if 0 not in C:
   a,b=ends(0,lattice);other=b if a==root else a
   if other not in V:
    delta=(other-root)/2
    for n in range(1,M-len(C)):
     for E in lev[n]:
      d=frozenset(q+delta for q in E)
      if not V&{v for q in d for v in ends(q,lattice)}:ds.append(d)
  for d in ds:
   B=set(C|d);assert component(B,lattice,root)[1]==C
   pn,hn,ch=step(B,0j,0);N=component(B,lattice,wvertex(pn,hn))[1]
   if len(N)>M:continue
   lost=B-N;normal=frozenset((q-pn)*1j**hn for q in N);assert normal in ind
   assert (ch=='L'and not d)or(ch=='R'and not lost)
   T.append({'source':ind[C],'target':ind[normal],'turn':ch,'input':key(C),'import':key(d),'active':key(N),'emit':key(lost),'pose':(xy(pn),hn)})
 saved=json.loads((D/f'component_kernel_M{M}.json').read_text());S=saved['summary'];assert len(states)==S['active_states']and len(T)==S['transitions']
 def trkey(z):return(z['source'],z['target'],z['turn'],tuple(z['input']),tuple(z['import']),tuple(z['active']),tuple(z['emit']),z['pose'])
 actual=Counter(trkey(z)for z in T)
 expected=Counter((z['source'],z['target'],z['turn'],tuple(map(tuple,z['input_component'])),tuple(map(tuple,z['imported_component'])),tuple(map(tuple,z['output_active'])),tuple(map(tuple,z['emitted_component'])),(tuple(z['output_pose'][0]),z['output_pose'][1]))for z in saved['transitions'])
 assert actual==expected
 ranks=None
 if M==3:
  ranks={tuple(map(tuple,z['C'])):z['weight']for z in S['active_ranks']};assert set(ranks)=={key(C)for C in states};assert min(ranks.values())==0 and max(ranks.values())==9 and all(z['weight']==0 for z in S['passive_weights'])
  assert all(ranks[z['input']]>=ranks[key(states[z['target']])]+1 for z in T)
 # Independently identify SCCs using reachability intersections on this small finite graph.
 adj=[set()for _ in states];rev=[set()for _ in states]
 for z in T:adj[z['source']].add(z['target']);rev[z['target']].add(z['source'])
 def reach(v,g):
  seen={v};todo=[v]
  for a in todo:
   for b in g[a]:
    if b not in seen:seen.add(b);todo.append(b)
  return seen
 unseen=set(range(len(states)));scc=[]
 while unseen:
  v=min(unseen);ss=reach(v,adj)&reach(v,rev);unseen-=ss
  if len(ss)>1 or v in adj[v]:scc.append(sorted(ss))
 allout[M]={'states':len(states),'transitions':len(T),'mass_level_counts':list(map(len,lev[:M+1])),'integer_rank_max':max(ranks.values())if ranks else None,'recurrent_sccs':scc};transby[M]=(states,T)
assert allout[3]['recurrent_sccs']==[] and len(allout[4]['recurrent_sccs'])==1
states,T=transby[4];cycle=allout[4]['recurrent_sccs'][0];inside=[z for z in T if z['source']in cycle and z['target']in cycle];assert len(cycle)==len(inside)==5
v=0;ordered=[]
for _ in range(5):
 z=next(z for z in inside if z['source']==v);ordered.append(z);v=z['target']
assert v==0 and ''.join(z['turn']for z in ordered)=='RRRRL'and all(not z['import']for z in ordered)and sum(len(z['emit'])for z in ordered)==3
obs=json.loads((D/'kernel_M4_rank_obstruction.json').read_text());assert obs['total_multiplicity']==5 and sum(z['multiplicity']for z in obs['used_transitions'])==5
assert Counter(z['source']for z in ordered)==Counter(z['target']for z in ordered)
# Direct blank prefix confirms why the relaxed active loop cannot repeat physically.
B=set();p=0j;h=0;imports=[]
for t in range(9):
 V,C=component(B,lattice,wvertex(p,h))
 if p not in B:
  aa,bb=ends(p,lattice);other=bb if aa==wvertex(p,h)else aa;old=component(B,lattice,other)[1]
  if old and old!=C:imports.append((t,len(C),len(old),len(C|old|{p})))
 p,h,ch=step(B,p,h)
assert imports==[(8,3,3,7)]
mp=D/'kernel_manifest.json';mf=json.loads(mp.read_text())
for f,h in mf['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out={'status':'PASS exhaustive cap-three integer exit rank and cap-four additive-rank obstruction','manifest_sha256':hashlib.sha256(mp.read_bytes()).hexdigest(),'note_sha256':mf['files']['CAP_THREE_AND_RANK_OBSTRUCTION.md'],'independent_kernels':allout,'exact_cap4_relaxed_cycle':ordered,'blank_first_import':imports,'analytic':['The rooted enumeration is exhaustive by adding incident edges from a rooted spanning tree then its remaining edges; no geometric radius cutoff is imposed. Rootw=(1,-1) in doubled coordinates is fixed lattice0. All quarter-normalized physical states have headingN and this lattice, so enumeration includes every actual orientation without reflection identification.','At R, every cap-preserving nonempty import is a complete connected graph rooted at the other endpoint with size at most M-|C|-1. Translating every rooted state of that size generates it; vertex disjointness from active C and w is necessary and sufficient. At L, deletion and actual arrival component uniquely determine the emitted component. Other background components are irrelevant to this one update; no spurious choice removes an actual transition.','All111 cap3 states and80 transitions reconstructed independently agree exactly with the author. The provided integer active ranks0..9 strictly decrease at every transition and every passive weight iszero. Thus ten consecutive cap-preserving updates are impossible on ANY background, even infinite; no finite-support escape theorem or floating LP is needed.','All550 cap4 states and432 transitions also reconstructed exactly. The five RRRRL edges form an active-state circulation consuming no archive and emitting a three-edge star. Summed strict additive rank decrease would force negative weight for that star. This rules out the stated nonnegative shape-plus-passive-type weighting class, not arbitrary spatial/stateful ranks.','The loop is only a relaxed local cycle. Direct complete blank evolution imports the previously emitted three-edge component at update8, giving active mass7, so it cannot repeat while respecting cap4. No actual nonzero translator or reusable writer is supplied.','Independent SCC inspection also finds exactly this one five-state recurrent cap4 SCC. This extra finite graph fact is recorded, but no new universal cap4 exit-time theorem is asserted in this report pending the author geometric iteration argument.'],'scope':'Universal cap3 active-mass exit bound10, plus impossibility of one scalar ranking class at cap4. No standard104 capture, general sustained cap or undecidability claim.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(allout)
