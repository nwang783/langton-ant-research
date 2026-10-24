"""Independent bounded-base/cycle cover reconstruction and literal scheme parity.
No supplied cover is assumed complete merely from a bounded simulation.
"""
from pathlib import Path
from collections import Counter
from itertools import product,islice
from functools import lru_cache
from types import SimpleNamespace
import random,sys,json,time,hashlib
ROOT=Path(__file__).resolve().parents[1];H=ROOT/'computability/flat_exact_validator';sys.path.insert(0,str(H))
import generated_cover_decider as G
start=time.monotonic();rng=random.Random(42017);graph_checks=0;maxbase=0
# Separate constructive proof witness: support-preserving deletion followed by
# a fresh greedy circulation decomposition. Compare against subject cycle stars.
def check_walk(m,word):
 global graph_checks,maxbase
 original=Counter(word);base=list(word)
 while True:
  vertices=[m.root]+[e.target for e in base];removed=False
  for i in range(len(base)):
   for j in range(i+1,len(base)+1):
    if vertices[i]==vertices[j] and set(base[:i]+base[j:])==set(base):
     base=base[:i]+base[j:];removed=True;break
   if removed:break
  if not removed:break
 bound=len(m.reach)*(sum(len(es)for es in m.phi)+1)-1
 assert len(base)<=bound;maxbase=max(maxbase,len(base));remaining=original-Counter(base);cyc_counts=Counter()
 while remaining:
  e=next(iter(remaining));v=e.source;path=[];at={}
  while v not in at:
   at[v]=len(path);choices=[e for e,n in remaining.items()if n and e.source==v];assert choices
   e=min(choices,key=lambda a:(a.source,a.index));path.append(e);v=e.target
  cyc=path[at[v]:];key=min((tuple(cyc[j:]+cyc[:j])for j in range(len(cyc))),key=lambda c:tuple((e.source,e.index)for e in c))
  cyc_counts[key]+=1
  for e in cyc:
   remaining[e]-=1
   if not remaining[e]:del remaining[e]
 chunks,end=G.support_scheme(m,tuple(base));built=[]
 for starred,edges in chunks:
  n=cyc_counts.pop(edges,0)if starred else 1;built.extend(edges*n)
 assert not cyc_counts and Counter(built)==original
 v=m.root
 for e in built:assert e.source==v;v=e.target
 assert v==(word[-1].target if word else m.root)==end
 graph_checks+=1
for g in range(12):
 n=1+g%4;phi=[]
 for s in range(n):
  targets=[(s+1)%n]+[rng.randrange(n)for _ in range(1+g%2)]
  phi.append(tuple(G.Edge(s,i,t,(rng.randrange(-2,3),rng.randrange(-2,3)))for i,t in enumerate(targets)))
 m=SimpleNamespace(root=0,reach=tuple(range(n)),phi=tuple(phi))
 walks=[()]
 for d in range(7):
  for w in walks:check_walk(m,w)
  if d<6:walks=[w+(e,)for w in walks for e in m.phi[w[-1].target if w else 0]]
print('constructive covers',graph_checks,flush=True)
P=G.standard_physical();I=[[s]for s in range(8)]
transient=G.GeneralUnitModel(P+[(0,1)],I+[G.word_states('RLLLLRRRR')],8)
models=[('branch_R5',G.from_strings(['RRRRR','LLLLL']*4)),('branch_R9',G.from_strings(['RLLLLRRRR','LRRRRLLLL']*4)),('transient_R9',transient)]
records=[]
for name,m in models:
 shift,machines,rat=m.parity_machines()
 @lru_cache(None)
 def expand(s,r):return (s,)if r==0 else tuple(v for t in m.images[s]for v in expand(t,r-1))
 checks=0;schemes=0
 for depth,scheme,bound in islice(G.bounded_schemes(m,max_length=3),40):
  C=G.compile_scheme(m,scheme,shift,machines);chunks,terminal=scheme;k=len(C['variables']);schemes+=1
  for ns in product(range(3),repeat=k):
   path=[];at=0
   for cyc,es in chunks:
    count=ns[at]if cyc else 1;at+=int(cyc);path.extend([e.index for e in es]*count)
   r=len(path)
   if r>4:continue
   leaf=0;s=m.root
   for depth,index in enumerate(path):
    leaf+=sum(len(expand(t,r-depth-1))for t in m.images[s][:index]);s=m.images[s][index]
   assert s==terminal;word=expand(m.root,r);assert word[leaf]==terminal
   p=0j;heading=(1j,1,-1j,-1)[m.physical[m.root][0]];odd=set()
   for t in word[:leaf]:
    h,turn=m.physical[t];assert heading==(1j,1,-1j,-1)[h];odd.symmetric_difference_update({p});heading*=(-1j if turn==1 else 1j);p+=heading
   values=dict(zip(C['variables'],ns));assert C['prior'].eval(**values)==(p in odd)
   assert C['black'].eval(**values)==((p in odd)^(m.physical[terminal][1]==-1))
   for coord,want in [('x',p.real),('y',p.imag),('length',r)]:
    coeff,const=C[coord];assert sum(a*b for a,b in zip(coeff,ns))+const==want
   checks+=1
 records.append(dict(name=name,schemes=schemes,literal_complete_prefix_checks=checks));print(name,checks,flush=True)
# Actual full positive cover enumeration, not a fixed depth bound.
positive=G.solve_generated(transient);assert positive['complete_generated_cover']and positive['possible']and positive['candidate_seed']==[(0,1),(1,0),(1,1)]
assert not positive['given_seed_validation']['accepted_growing_model']
limited=G.solve_generated(transient,max_schemes=1);assert limited['possible'] is None
negative=G.solve_generated(models[0][1]);assert negative['possible'] is False
res=dict(status='PASS independent constructive cover witnesses and literal branching-cycle parity',graph_walks=graph_checks,largest_reduced_base=maxbase,models=records,complete_positive=positive,explicit_cap=limited,negative_control=negative,seconds=time.monotonic()-start,subject_sha256=hashlib.sha256((H/'generated_cover_decider.py').read_bytes()).hexdigest(),scope='Generated exact additive-I unit presentation realization. Completeness uses independently reviewed finite support-preserving base/cycle lemma, not these finite controls. No accepted growing ant model.')
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
