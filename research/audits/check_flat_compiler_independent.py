from pathlib import Path
from collections import Counter
from itertools import product
from functools import lru_cache
import sys,json,hashlib
ROOT=Path('/workspace/shared/langton');sys.path.insert(0,str(ROOT/'computability/flat_exact_validator'))
import flat_forced_seed as A
P=[(h,t)for h in range(4)for t in(1,-1)];I=[[i]for i in range(8)]
def ids(w,h=0):
 out=[]
 for c in w:out.append(2*h+(c=='L'));h=(h+(1 if c=='R'else-1))%4
 return out
models=[]
def add(name,p,im,root):models.append((name,A.Model(p,im,root)))
add('two_state_square_cycle',P+[(0,1)]*2,I+[[9]+ids('RRRR',1),[8]+ids('RRRR',1)],8)
add('nested_square_cycles',P+[(0,1),(1,1)],I+[[8,9,4,6,0],[9]+ids('RRRR',2)],8)
U='RRLRRRRL';V='LLRLLRLL'
add('two_state_drifting_cycle',P+[(0,1)]*2,I+[ids(U)+[9]+ids(V,1),ids(U)+[8]+ids(V,1)],8)
add('transient_nested_cycles',P+[(0,1),(1,1),(0,1)],I+[[8,9,4,6,0],[9]+ids('RRRR',2),[8]],10)
rows=[]
for name,m in models:
 schemes=m.schemes()
 @lru_cache(None)
 def expand(s,r):
  return (s,)if r==0 else tuple(t for u in m.images[s] for t in expand(u,r-1))
 @lru_cache(None)
 def rawwalks(s,r):
  return ((),) if r==0 else tuple((j,)+tail for j,t in enumerate(m.images[s])for tail in rawwalks(t,r-1))
 checks=0;cover=0
 for depth in range(7):
  generated=Counter()
  for chunks,terminal in schemes:
   k=sum(c for c,_ in chunks)
   for ns in product(range(depth+1),repeat=k):
    path=[];at=0
    for cyc,edges in chunks:
     n=ns[at]if cyc else 1;at+=int(cyc)
     path += [e.index for e in edges]*n
    if len(path)==depth:generated[tuple(path)]+=1
  wanted=Counter(rawwalks(m.root,depth));assert generated==wanted,(name,depth,generated-wanted,wanted-generated)
  assert max(generated.values())==1;cover+=len(wanted)
 shift,machines,rat=m.parity_machines()
 for scheme in schemes:
  c=A.compile_scheme(m,scheme,shift,machines);chunks,terminal=scheme;k=len(c['variables'])
  for ns in product(range(4),repeat=k):
   path=[];at=0
   for cyc,edges in chunks:
    n=ns[at]if cyc else 1;at+=int(cyc);path +=[e.index for e in edges]*n
   depth=len(path);s=m.root;leaf=0
   for i,j in enumerate(path):
    leaf+=sum(len(expand(t,depth-i-1))for t in m.images[s][:j]);s=m.images[s][j]
   assert s==terminal
   word=expand(m.root,depth);assert word[leaf]==terminal
   z=0j;h=(1j,1,-1j,-1)[m.physical[m.root][0]];parity=set()
   for t in word[:leaf]:
    parity.symmetric_difference_update({z});head,turn=m.physical[t]
    assert h==(1j,1,-1j,-1)[head]
    h*=(-1j if turn==1 else 1j);z+=h
   vals=dict(zip(c['variables'],ns));want=z in parity
   assert c['prior'].eval(**vals)==want,(name,path,vals,z)
   assert c['black'].eval(**vals)==(want^(m.physical[terminal][1]==-1))
   for coord,actual in [('x',z.real),('y',z.imag),('length',depth)]:
    cf,cn=c[coord];assert sum(a*b for a,b in zip(cf,ns))+cn==actual
   checks+=1
 print(name,len(schemes),cover,checks,flush=True)
 rows.append(dict(name=name,schemes=len(schemes),exact_walks_through_depth6=cover,complete_prefix_parity_controls=checks))
res={'status':'PASS independent complete walk inventory and direct literal prefix parity on multistate/nested flat SCCs','controls':rows,'scope':'Checks the new scheme and compiler formulas; uses previously audited automata primitives, and imports the implementation under test only as a black-box producer. No growing model is accepted.','hashes':{'auditor':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'subject':hashlib.sha256((ROOT/'computability/flat_exact_validator/flat_forced_seed.py').read_bytes()).hexdigest()}}
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
