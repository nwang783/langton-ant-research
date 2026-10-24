"""Independent literal macro-base and occurrence-prefix checks, with exact fuel.
Subject is imported only to produce automata; all physical traces are rebuilt.
"""
from pathlib import Path
from collections import Counter
from itertools import product
from functools import lru_cache
import ast,sys,json,hashlib
from fractions import Fraction as F
B=Path('/workspace/shared/langton');sys.path.insert(0,str(B/'computability/flat_exact_validator'))
import macro_forced_seed as A
# Reuse our independently signed sparse rational equivalence proof, not author code.
p=B/'audits/check_flat_depth_fuel_independent.py';tree=ast.parse(p.read_text());fun=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='exact_fuel');exec(compile(ast.Module(body=[fun],type_ignores=[]),str(p),'exec'))
dirs=(1j,1,-1j,-1)
models=[('rod_transport',A.capped_rod(),(2,3,0)),('rod_growth',A.capped_rod('LRRRRLLR'),(2,2,0)),('identity_multibase',A.MacroModel([(1,'LLLRRRRL')],[[0]]),(0,3,0)),('two_cycle_multibase',A.MacroModel([(1,'LLLRRRRL')]*2,[[1],[0]]),(0,3,0)),('nested_zero_macros',A.MacroModel([(0,'RRRR'),(1,'RRRR'),(0,'RRRR'),(0,'R')],[[0],[1],[0,2],[2,3,1]],3),None),('zero_parity_conflict',A.MacroModel([(0,'RRRRRRRR')],[[0]]),None)]
results=[]
for name,m,fuel in models:
 @lru_cache(None)
 def expand(s,r):return (s,) if not r else tuple(v for t in m.images[s] for v in expand(t,r-1))
 def literal(word):
  z=0j;h=dirs[m.bases[word[0]][0]];out=[]
  for s in word:
   assert h==dirs[m.bases[s][0]]
   for c in m.bases[s][1]:out.append((z,c));h*=(-1j if c=='R' else 1j);z+=h
  return out
 @lru_cache(None)
 def walks(s,r):return ((),) if not r else tuple((j,)+w for j,t in enumerate(m.images[s]) for w in walks(t,r-1))
 schemes=m.schemes();inventory=0
 for r in range(6):
  actual=Counter(walks(m.root,r));got=Counter()
  for chunks,s in schemes:
   k=sum(c for c,es in chunks)
   for ns in product(range(r+1),repeat=k):
    path=[];a=0
    for cyc,es in chunks:
     times=ns[a] if cyc else 1;a+=int(cyc);path += [e.index for e in es]*times
    if len(path)==r:got[tuple(path)]+=1
  assert actual==got and max(got.values())==1;inventory+=len(actual)
 shifts,machines,cert=m.parity_machines();priorchecks=0
 for scheme in schemes:
  chunks,terminal=scheme
  for j in range(len(m.bases[terminal][1])):
   c=A.compile_terminal(m,scheme,j,shifts,machines);k=len(c['variables'])
   for ns in product(range(3),repeat=k):
    path=[];a=0
    for cyc,es in chunks:
     times=ns[a] if cyc else 1;a+=int(cyc);path +=[e.index for e in es]*times
    depth=len(path);s=m.root;offset=0
    for i,ix in enumerate(path):
     offset+=sum(sum(len(m.bases[v][1]) for v in expand(t,depth-i-1)) for t in m.images[s][:ix]);s=m.images[s][ix]
    assert s==terminal
    reads=literal(expand(m.root,depth));q,turn=reads[offset+j];odd=sum(z==q for z,t in reads[:offset+j])%2;vals=dict(zip(c['variables'],ns))
    assert c['prior'].eval(**vals)==bool(odd)
    assert c['black'].eval(**vals)==bool(odd^(turn=='L'))
    for key,value in [('x',q.real),('y',q.imag),('length',depth)]:
     co,cn=c[key];assert sum(x*y for x,y in zip(co,ns))+cn==value
    priorchecks+=1
 result,rels,bad,compiled,_,_=A.compile_macro(m,True)
 rank=None
 if fuel:
  C=max(abs(x) for s in m.reach for e in m.phi[s] for x in e.offset);D=max(abs(x) for s in m.reach for p,t,h in m.traces[s] for x in p)
  rank,states=exact_fuel(rels,(C+D+1).bit_length()+1,*fuel)
 checks=0
 for r in range(13):
  reads=literal(expand(m.root,r));odd=set();need={};conflict=False
  for q,t in reads:
   x=(t=='L')^(q in odd)
   if q in need and need[q]!=x:conflict=True
   need.setdefault(q,x);odd.symmetric_difference_update({q})
  assert bad.eval(r=r)==conflict
  C=int(max(abs(z.real)+abs(z.imag) for z,t in reads))+1
  if not conflict:
   for x in range(-C,C+1):
    for y in range(-3,4):
     q=complex(x,y);sg=tuple(1 if v>=0 else -1 for v in(x,y));b,w=rels[sg];v=dict(r=r,x=abs(x),y=abs(y))
     assert b.eval(**v)==bool(need.get(q,False));assert w.eval(**v)==bool(q in need and not need[q]);checks+=1
  if fuel:assert sum(need.values())==fuel[0]*r+fuel[1]+fuel[2]*(r==0)
 results.append(dict(name=name,exact_occurrence_walks=inventory,prefix_parity_reads=priorchecks,complete_literal_cells=checks,independent_all_binary_fuel_rank=rank));print(results[-1],flush=True)
out=dict(status='PASS',controls=results,scope='Exact finite-base extension controls and independent all-binary fuel proof. No growing finite-seed acceptance.',subject_sha256=hashlib.sha256((B/'computability/flat_exact_validator/macro_forced_seed.py').read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
