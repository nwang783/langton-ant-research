from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import sys,json,hashlib
ROOT=Path('/workspace/shared/langton');sys.path.insert(0,str(ROOT/'computability/flat_exact_validator'))
import flat_forced_seed as A
import depth_requirements as D

def exact_fuel(relations,extra,alpha,beta,corr):
 blocks=[];n=0
 for b,w in relations.values():blocks.append((n,b));n+=len(b.tr)
 dim=n+4;trans=[[],[]]
 for bit in range(2):
  rows=[Counter()for _ in range(dim)]
  for offset,b in blocks:
   for q,row in enumerate(b.tr):
    for xx in range(2):
     for yy in range(2):
      vals={'r':bit,'x':xx,'y':yy};symbol=sum(vals[v]<<j for j,v in enumerate(b.vs));rows[offset+q][offset+row[symbol]]+=1
  # Independent target n, digit place, constant, zero indicator.
  rows[n][n]=1;rows[n+1][n]=bit;rows[n+1][n+1]=2;rows[n+2][n+2]=1;rows[n+3][n+3]=1-bit
  trans[bit]=rows
 end=[0]*dim;start=[F(0)]*dim
 for offset,b in blocks:
  v=[int(q in b.ac)for q in range(len(b.tr))]
  for _ in range(extra):v=[sum(count*v[d-offset]for d,count in trans[0][offset+q].items())for q in range(len(b.tr))]
  end[offset:offset+len(v)]=v;start[offset+b.start]=F(1)
 start[n+1]=start[n+2]=start[n+3]=F(1);end[n:]=[-alpha,0,-beta,-corr]
 basis={};queue=[start]
 for v in queue:
  v=list(v)
  for p,b in sorted(basis.items()):
   a=v[p]
   if a:v=[x-a*y for x,y in zip(v,b)]
  p=next((i for i,x in enumerate(v)if x),None)
  if p is None:continue
  v=[x/v[p]for x in v];assert sum(x*y for x,y in zip(v,end))==0
  basis[p]=v
  for bit in range(2):
   z=[F(0)]*dim
   for q,x in enumerate(v):
    if x:
     for d,k in trans[bit][q].items():z[d]+=x*k
   queue.append(z)
 return len(basis),dim
rows=[]
for name,m,fuel in [('identity_R',A.identity(0),(0,0,0)),('identity_L',A.identity(1),(0,1,0)),('oblique',A.hairpin('LRLLLLRRRRLRRL','RLRRLL'),(6,0,0)),('axial',A.hairpin('RRLRRRRL','LLRLLRLL'),(4,2,-2))]:
 rels,bad,rat=D.compile_depth(m);assert bad.witness()is None
 C=max(abs(a)for s in m.reach for e in m.phi[s]for a in e.offset);extra=C.bit_length()+1
 rank,states=exact_fuel(rels,extra,*fuel)
 checks=0
 for r in range(17):
  word=[m.root]
  for _ in range(r):word=[t for s in word for t in m.images[s]]
  z=0j;h=(1j,1,-1j,-1)[m.physical[m.root][0]];odd=set();req={}
  for s in word:
   need=(m.physical[s][1]==-1)^(z in odd)
   assert z not in req or req[z]==need;req[z]=need;odd.symmetric_difference_update({z})
   h*=(-1j if m.physical[s][1]==1 else 1j);z+=h
  for sx in(-1,1):
   for sy in(-1,1):
    b,w=rels[sx,sy]
    for x in range(C*r+1):
     for y in range(C*r+1):
      p=complex(sx*x,sy*y);valid=not(sx<0 and x==0 or sy<0 and y==0)
      assert b.eval(r=r,x=x,y=y)==(valid and p in req and req[p])
      assert w.eval(r=r,x=x,y=y)==(valid and p in req and not req[p]);checks+=1
  assert sum(req.values())==fuel[0]*r+fuel[1]+fuel[2]*(r==0)
 rows.append(dict(name=name,weighted_states=states,independent_reachable_rank=rank,complete_literal_cell_checks=checks));print(rows[-1],flush=True)
J={'status':'PASS independent exact rational row-space equality for every binary depth and complete finite literal cells','controls':rows,'scope':'Different depth blocks may require different entry boards. Fuel formulas are exact all-depth weighted-automaton equalities, not a seed or wrapper construction.','hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(Path(__file__),ROOT/'computability/flat_exact_validator/depth_requirements.py')}}
Path(__file__).with_suffix('.json').write_text(json.dumps(J,indent=2)+'\n');print(json.dumps(J))
