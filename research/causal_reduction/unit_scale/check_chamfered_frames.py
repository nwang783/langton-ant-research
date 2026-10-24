"""Exact two-parameter self-avoiding outward frames and their wrong-sector match."""
from pathlib import Path
import sys,json,hashlib
HERE=Path(__file__).parent
sys.path.insert(0,str(HERE.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
C=Context(max_operations=50000000)
# Affine vectors use coefficients of r,k,s,1.
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def rot(p,n):
 x,y=p
 for _ in range(n):x,y=y,neg(x)
 return x,y

def expr(v):return '('+'+'.join(f'{z}*{a}' for z,a in zip(v,('r','k','s','1')))+')'
def families(shift=0):
 v=((2,1,0,shift),(0,-1,0,-shift-1));start=((0,0,0,0),(0,0,0,0));F=[]
 base=[('L',((0,0,1,0),(0,0,0,0)),'0<=s<2r'),('R',((0,0,1,0),(0,0,0,1)),'0<=s<2r'),('L',((2,0,1,0),(0,0,-1,-1)),f'0<=s<k+{shift}'),('R',((2,0,1,0),(0,0,-1,0)),f'0<=s<=k+{shift}')]
 for j in range(4):
  for turn,p,bound in base:
   q=rot(p,j);q=tuple(plus(q[t],start[t])for t in(0,1));S=C.set('[r,k]->{[x,y]:r>=0 and k>=0 and exists(s:'+bound+f' and x={expr(q[0])} and y={expr(q[1])}' +')}')
   F.append((turn,S))
  d=rot(v,j);start=tuple(plus(start[t],d[t])for t in(0,1))
 assert start==((0,0,0,0),(0,0,0,0))
 return F
F=families();pair_checks=0
for i,(a,s)in enumerate(F):
 for b,t in F[:i]:assert s.intersect(t).is_empty(),(i,str(s.intersect(t)));pair_checks+=1
def union(turn,fs):
 z=C.set('[r,k]->{[x,y]:false}')
 for c,s in fs:
  if c==turn:z=z.union(s)
 return z.coalesce()
I=union('L',F);O=union('R',F);target=union('L',families(1));T=C.map('[r,k]->{[x,y]->[X,Y]:X=x and Y=y+1}');target=T.intersect_domain(target).range() if hasattr(T,'intersect_domain')else None
# Ownership wrapper exposes application on sets.
if target is None:
 from isl_exact import Object,_FUN
 target=Object(C,'map',_FUN['map','intersect_domain'](T._copy(),union('L',families(1))._copy())).range()
assert O.is_equal(target)
# Same-center quarter-turn symmetry: center=(r-1/2,-r-k-1/2).
# CCW rotation about it adds(-k-1,-2r-k), with odd coordinate sum.
R=C.map('[r,k]->{[x,y]->[X,Y]:X=-y-k-1 and Y=x-2r-k}')
from isl_exact import Object,_FUN
RI=Object(C,'map',_FUN['map','intersect_domain'](R._copy(),I._copy())).range();assert RI.is_equal(I)
res=dict(status='PASS exact all-r,k set identities',domain='integers r>=0,k>=0',word='((LRRL)^r (RL)^k R)^4',incoming_heading='E',final_pose=[0,0,'E'],length='16r+8k+4',input_mass='8r+4k',output_mass='8r+4k+4',complete_xor='16r+8k+4',all_reads_distinct=True,disjoint_family_pairs=pair_checks,output_equals_next_input_plus_north=True,next_pose_sector_opposite=True,input_relation=str(I),output_relation=str(O),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),isl_version=C.version)
HERE.joinpath('chamfered_frames_certificate.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items()if not k.endswith('_relation')},indent=2))
