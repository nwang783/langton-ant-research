"""Independent exhaustive finite-graph truth and explicit infinite controls.
Imports only the candidate solver under test, not its controls/reference search.
"""
from pathlib import Path
import importlib.util,itertools,json,hashlib
R=Path(__file__).resolve().parents[1];source=R/'computability/finite_power_exact_validator/bounded_seed_graph.py'
spec=importlib.util.spec_from_file_location('candidate',source);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
# All edge-labelled undirected three-vertex graphs: absent, zero, one, or both.
verts=tuple(range(3));pairs=tuple(itertools.combinations_with_replacement(verts,2));checks=0;minimums=0
for labels in itertools.product(range(4),repeat=len(pairs)):
 zero=[p for p,c in zip(pairs,labels)if c&1];one=[p for p,c in zip(pairs,labels)if c&2]
 adj={u:set()for u in verts}
 for u,v in zero:adj[u].add(v);adj[v].add(u)
 # Three representative pin regimes, including a contradiction and white pin.
 for pins in ([],[(0,1)],[(0,0),(2,1)]):
  truth=[]
  for bits in itertools.product((0,1),repeat=3):
   if any(bits[u]!=bits[v]for u,v in zero):continue
   if any(bits[u]==bits[v]for u,v in one):continue
   if any(bits[u]!=v for u,v in pins):continue
   truth.append(sum(bits))
  least=min(truth)if truth else None
  for M in range(4):
   ans=mod.solve(lambda u:adj.get(u,()),one,pins,M)
   assert ans['possible']==(least is not None and least<=M),(labels,pins,M,ans,least)
   if ans['possible']:
    assert ans.get('mass',0)==least;B=set(ans['board']);assert len(B)==least
    assert all((u in B)==(v in B)for u,v in zero)
    assert all((u in B)!=(v in B)for u,v in one)
    assert all(int(u in B)==v for u,v in pins);minimums+=1
   checks+=1
# Two disconnected infinite lines and a remote four-cycle plus isolated vertex.
BIG=10**120
cycle={(BIG,0):[(BIG+1,0),(BIG,1)],(BIG+1,0):[(BIG,0),(BIG+1,1)],(BIG,1):[(BIG,0),(BIG+1,1)],(BIG+1,1):[(BIG,1),(BIG+1,0)]}
def adj(u):
 x,y=u
 if y in(7,9):return[(x-1,y),(x+1,y)]
 return cycle.get(u,[])
controls=0
for M in range(11):
 cases=[([], [((0,7),1)],False),([((0,7),(0,9))],[],False),([((0,7),(BIG,0))],[],M>=4),([], [((BIG,0),1),((BIG+1,1),0)],False)]
 for one,pins,want in cases:
  got=mod.solve(adj,one,pins,M);assert got['possible']==want,(M,one,pins,got);controls+=1
out={'status':'PASS independent exhaustive reference comparison','finite_graphs':4**6,'pin_regimes':3,'mass_bounds':4,'comparisons':checks,'minimum_mass_matches':minimums,'infinite_remote_controls':controls,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'scope':'Bounded-support graph solver only; no ant-to-automatic-graph compiler tested.'}
(R/'audits/bounded_seed_graph_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
