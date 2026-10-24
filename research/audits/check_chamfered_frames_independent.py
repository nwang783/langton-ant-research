"""Independent symbolic literal-family proof, with no constructor imports.
Each LRRL read remains its own affine family, rather than merged row segments.
"""
from pathlib import Path
from itertools import product
import sys,json,hashlib
import sympy as S
B=Path('/workspace/shared/langton');sys.path.insert(0,str(B/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
C=Context(max_operations=50000000);r,k,i=S.symbols('r k i',integer=True)
def rotate(v):return (v[1],-v[0])
def add(a,b):return tuple(S.expand(x+y) for x,y in zip(a,b))
def mul(n,a):return tuple(S.expand(n*x) for x in a)
def word(word,h):
 p=(0,0);reads=[]
 for c in word:
  reads.append((p,c));h=rotate(h) if c=='R' else mul(-1,rotate(h));p=add(p,h)
 return reads,p,h
families=[];p=(0,0);h=(1,0)
for side in range(4):
 for text,length in [('LRRL',r),('RL',k)]:
  reads,d,g=word(text,h);assert g==h
  for z,c in reads:families.append((add(add(p,mul(i,d)),z),c,length))
  p=add(p,mul(length,d))
 reads,d,h=word('R',h);families.append((p,'R',None));p=add(p,d)
assert p==(0,0) and h==(1,0) and len(families)==28

def make(fam,dk=0,shift=(0,0),rotations=0):
 z,c,length=fam;z=tuple(v.subs(k,k+dk) if hasattr(v,'subs') else v for v in z);z=add(z,shift)
 center=(r-S.Rational(1,2),-r-k-S.Rational(1,2))
 for _ in range(rotations):z=add(center,mul(-1,rotate(add(z,mul(-1,center)))))
 bounds='true' if length is None else f'0<=i<{S.expand(length.subs(k,k+dk))}'
 eq=f'x={S.expand(z[0])} and y={S.expand(z[1])}'
 return C.set('[r,k]->{[x,y]:r>=0 and k>=0 and exists(i:'+bounds+' and '+eq+')}')
sets=[make(f) for f in families];checks=0
for a in range(len(sets)):
 for b in range(a):assert sets[a].intersect(sets[b]).is_empty(),(a,b);checks+=1
empty=C.set('[r,k]->{[x,y]:false}')
def union(turn,**kwargs):
 ans=empty
 for f in families:
  if f[1]==turn:ans=ans.union(make(f,**kwargs))
 return ans.coalesce()
I=union('L');O=union('R');assert O.is_equal(union('L',dk=1,shift=(0,1)))
assert I.is_equal(union('L',rotations=1))
# Literal coordinate and complete-field comparisons, not symbolic-family reuse.
literal=0
for rr,kk in product(range(13),range(13)):
 text=(('LRRL'*rr)+('RL'*kk)+'R')*4;z=0j;h=1+0j;black=set();reads=[];out=set()
 for c in text:
  assert z not in reads;reads.append(z)
  if c=='L':black.add(z)
  else:out.add(z)
  h*=(-1j if c=='R' else 1j);z+=h
 assert z==0j and h==1 and len(black)==8*rr+4*kk and len(out)==8*rr+4*kk+4
 symbolic={'L':set(),'R':set()}
 for p,c,n in families:
  stop=1 if n is None else int(n.subs({r:rr,k:kk}))
  for j in range(stop):symbolic[c].add(complex(*(int(S.sympify(v).subs({r:rr,k:kk,i:j})) for v in p)))
 assert symbolic['L']==black and symbolic['R']==out
 # Build target independently from the literal next word.
 target=set();z=1j;h=1
 for c in (('LRRL'*rr)+('RL'*(kk+1))+'R')*4:
  if c=='L':target.add(z)
  h*=(-1j if c=='R' else 1j);z+=h
 assert target==out
 literal+=len(reads)
# Sector of ALL same-center quarter rotated target starts, for each residue.
sectorchecks=0
for rr,kk in product(range(4),range(4)):
 center=complex(rr-.5,-rr-kk-.5);z=1j;heading=1
 for j in range(4):
  assert int(z.real+z.imag+heading)%2==0 # actual starting (0,0,E) has sector1
  z=center+1j*(z-center);heading=(heading-1)%4;sectorchecks+=1
result=dict(status='PASS independent symbolic literal traces and complete all-parameter field identities',domain='r,k nonnegative integers',affine_read_families=28,exact_disjoint_pairs=checks,complete_output_equals_next_input_north=True,input_quarter_symmetry=True,literal_read_checks=literal,rotated_sector_controls=sectorchecks,scope='Prepared self-avoiding closed-pose family and exact field matching. Matching next pose is in the opposite invariant sector; no renewable model or actual continuation capture claimed.',subject_sha256=hashlib.sha256((B/'causal_reduction/unit_scale/check_chamfered_frames.py').read_bytes()).hexdigest(),input_relation=str(I),output_relation=str(O))
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if not k.endswith('_relation')},indent=2))
