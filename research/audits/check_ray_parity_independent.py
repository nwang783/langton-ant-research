"""Independent literal occupation and formal-series checks of the one-ray adapter."""
from pathlib import Path
from collections import defaultdict,Counter
import sys,json,random,hashlib
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'computability/finite_power_exact_validator'))
import ray_parity_extractor as R
import sympy as S
D=[1j,1,-1j,-1]

def typed_images(images):
 result=[]
 for s,word in enumerate(images):
  h=D[s//2];row=[]
  for c in word:
   row.append(2*D.index(h)+int(c=='L'));h*= -1j if c=='R' else 1j
  result.append(row)
 return result

def occupation(states):
 pos=0j;ans=Counter()
 for s in states:
  ans[(int(pos.real),int(pos.imag))]+=1 if s%2==0 else -1
  h=D[s//2]*(-1j if s%2==0 else 1j);pos+=h
 return {p:c for p,c in ans.items()if c}

def coefficients(p,h,N,mod2=False):
 def rows(poly):
  out=defaultdict(dict)
  for (r,x,y),c in poly.terms():
   if c:out[r][x,y]=int(c)if mod2 else S.Rational(c)
  return out
 pp=rows(p);hh=rows(h);assert set(hh[0])=={(0,0)};constant=hh[0][0,0];result=[]
 for r in range(N+1):
  vals=defaultdict(lambda:S.Integer(0));vals.update(pp[r])
  for depth,row in hh.items():
   if not 1<=depth<=r:continue
   for (x,y),c in row.items():
    for (u,v),b in result[r-depth].items():vals[x+u,y+v]-=c*b
  result.append({p:(int(c)%2 if mod2 else c/constant)for p,c in vals.items()if (int(c)%2 if mod2 else c)})
 return result

ctx=R.Context(max_operations=100000000);literal_checks=0;synthetic_checks=0;records=[]
for name,images in [('identity',['R','L']*4),('five',['RRRRR','LLLLL']*4),('nine',['RLLLLRRRR','LRRRRLLLL']*4)]:
 phi=typed_images(images);shift,rat=R.extract_rationals(images)
 for s,(p,h,p2,h2)in enumerate(rat):
  series=coefficients(S.Poly(p,*R.V),S.Poly(h,*R.V),3)
  w=[s]
  for depth in range(4):
   actual={(x+shift[0]*depth,y+shift[1]*depth):c for (x,y),c in occupation(w).items()}
   assert series[depth]==actual,(name,s,depth);literal_checks+=1
   w=[t for st in w for t in phi[st]]
  ctx.reset_operations();q,cert=R.parity_relation(ctx,p2,h2,shift)
  if q is not None:
   series2=coefficients(p2,h2,12,True)
   for depth,row in enumerate(series2):
    pts=[(x-shift[0]*depth,y-shift[1]*depth)for (x,y),c in row.items()if c]
    expected=ctx.set('{ [r,x,y] : r='+str(depth)+' and ('+(' or '.join(f'(x={x} and y={y})'for x,y in pts)or'0=1')+') }')
    assert q.intersect(ctx.set('{ [r,x,y] : r='+str(depth)+' }')).is_equal(expected);synthetic_checks+=1
  records.append([name,s,cert['status']])
random.seed(937)
for case in range(65):
 v=[random.randint(1,2),random.randint(0,2),random.randint(0,2)];mon=S.prod(x**a for x,a in zip(R.V,v));degree=random.randint(1,5)
 h=S.Poly(1+mon**degree+sum(mon**i for i in range(1,degree)if random.randrange(2)),*R.V,modulus=2)
 p=S.Poly(sum(S.prod(x**random.randint(0,2)for x in R.V)for _ in range(random.randint(0,4))),*R.V,modulus=2)
 shift=[random.randint(0,2),random.randint(0,2)];ctx.reset_operations();q,cert=R.parity_relation(ctx,p,h,shift);assert q is not None
 series=coefficients(p,h,15,True)
 for depth,row in enumerate(series):
  pts=[(x-shift[0]*depth,y-shift[1]*depth)for(x,y),c in row.items()if c]
  expected=ctx.set('{ [r,x,y] : r='+str(depth)+' and ('+(' or '.join(f'(x={x} and y={y})'for x,y in pts)or'0=1')+') }')
  assert q.intersect(ctx.set('{ [r,x,y] : r='+str(depth)+' }')).is_equal(expected),(case,depth);synthetic_checks+=1
res={'status':'PASS independent literal rational occupation and one-ray coefficient extraction','literal_integer_depth_fibers':literal_checks,'exact_parity_depth_fibers':synthetic_checks,'synthetic_ray_cases':65,'geometric_state_outcomes':records,'source_sha256':hashlib.sha256(Path(R.__file__).read_bytes()).hexdigest(),'scope':'Restricted one-ray extractor implementation, not full automatic forced-seed compiler or accepted growing ant.'}
(ROOT/'audits/ray_parity_independent.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
