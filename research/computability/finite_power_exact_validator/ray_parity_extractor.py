"""Exact image-to-rational-to-Presburger parity adapter for a stated subclass.
The reduced F2 denominator must be univariate in one nonnegative monomial.
Other denominators return unsupported, NEVER nonrealizability. No model found.
"""
import functools,math,pathlib,sys,time,json
import sympy as S
from sympy.polys.matrices import DomainMatrix
HERE=pathlib.Path(__file__).parent
sys.path.insert(0,str(HERE.parent/'unit_inductive_certificates'))
from check_read_sets import typed,literal,D
from presburger_template_validator import xor,periodic_set,read_parity
from presburger_bounded_seed import Context,solve
from binomial_denominator import denominator_test

Z,X,Y=S.symbols('z x y');V=(Z,X,Y)

def extract_rationals(images):
 if not isinstance(images,(tuple,list)) or len(images)!=8 or any(not isinstance(w,str) or not w or not set(w)<=set('RL') for w in images):
  raise ValueError('exactly eight nonempty R/L image strings are required')
 phi=typed(images)
 for s in range(8):
  _,p,h,_=literal(images,s,1);out=(s//2+(1 if s%2==0 else -1))%4
  if h!=out or p!=D[out]:raise ValueError('wrong unit-identity image geometry')
 C=max(0,-min(p[0] for row in phi for t,p in row));Dshift=max(0,-min(p[1] for row in phi for t,p in row))
 T=S.zeros(8)
 for s,row in enumerate(phi):
  for t,p in row:T[s,t]+=X**(p[0]+C)*Y**(p[1]+Dshift)
 M=DomainMatrix.from_Matrix(S.eye(8)-Z*T)
 rhs=DomainMatrix.from_Matrix(S.Matrix([1,-1]*4)).convert_to(M.domain)
 num,den=M.solve_den(rhs);N=num.to_Matrix();den=M.domain.to_sympy(den)
 out=[]
 for s in range(8):
  P,H=S.fraction(S.cancel(N[s]/den))
  p=S.Poly(P,*V,modulus=2);h=S.Poly(H,*V,modulus=2)
  if h.coeff_monomial((0,0,0))!=1:raise ValueError('odd unit denominator required for reduction')
  g=S.gcd(p,h);p=p.exquo(g);h=h.exquo(g)
  out.append((P,H,p,h))
 return (C,Dshift),out

def parity_relation(ctx,p,h,linear_shift):
 """Return (exact [r,x,y] set or None, certificate metadata)."""
 if tuple(p.gens)!=V or tuple(h.gens)!=V or p.get_modulus()!=2 or h.get_modulus()!=2:
  raise ValueError('three-variable polynomials over F2 are required')
 if h.coeff_monomial((0,0,0))!=1:raise ValueError('denominator constant must be one')
 if len(linear_shift)!=2 or any(type(a) is not int or a<0 for a in linear_shift):
  raise ValueError('two nonnegative integral linear shifts are required')
 g=S.gcd(p,h);p=p.exquo(g);h=h.exquo(g)
 if p.is_zero:
  result=ctx.set('{ [r,x,y] : 0=1 }')
  return result,dict(status='extracted',univariate_denominator=None,multiplicative_order=None,rays=[],relation=str(result))
 nz=[e for e in h.monoms() if any(e)];period=None;order=None;uni=None
 if nz:
  first=nz[0];div=functools.reduce(math.gcd,first);v=tuple(a//div for a in first)
  pivot=next(i for i,a in enumerate(v) if a);terms=[]
  for e,c in h.terms():
   n,rem=divmod(e[pivot],v[pivot])
   if rem or tuple(n*a for a in v)!=e:
    return None,dict(status='unsupported',reason='reduced F2 denominator is not one monomial ray')
   terms.append((n,int(c)%2))
  if v[0]<=0:return None,dict(status='unsupported',reason='denominator ray has no positive depth')
  t=S.Symbol('t');uni=S.Poly(sum(c*t**n for n,c in terms),t,modulus=2)
  # t is a unit in the finite quotient ring because uni(0)=1. Thus this
  # multiplicative-order loop terminates, with no numerical heuristic.
  rem=S.Poly(1,t,modulus=2);order=0
  while True:
   rem=(rem*S.Poly(t,t,modulus=2)).rem(uni);order+=1
   if rem==S.Poly(1,t,modulus=2):break
  q=(S.Poly(t**order+1,t,modulus=2)).exquo(uni)
  mon=S.prod(a**b for a,b in zip(V,v))
  multiplier=S.Poly(q.as_expr().subs(t,mon),*V,modulus=2)
  p=p*multiplier;period=tuple(order*a for a in v)
  assert h*multiplier==S.Poly(1+S.prod(a**b for a,b in zip(V,period)),*V,modulus=2)
 result=ctx.set('{ [r,x,y] : 0=1 }');records=[];C,Dshift=linear_shift
 for b,c in p.terms():
  assert int(c)%2==1
  physical=(b[0],b[1]-C*b[0],b[2]-Dshift*b[0])
  if period is None:
   formula=f'r={physical[0]} and x={physical[1]} and y={physical[2]}'
   velocity=None
  else:
   velocity=(period[0],period[1]-C*period[0],period[2]-Dshift*period[0])
   formula='exists (n : n>=0 and '+ ' and '.join(f'{a}={b0}{v0:+d}*n' for a,b0,v0 in zip(('r','x','y'),physical,velocity))+')'
  result=xor(result,ctx.set('{ [r,x,y] : '+formula+' }'))
  records.append(dict(base=physical,period=velocity))
 return result,dict(status='extracted',univariate_denominator=None if uni is None else str(uni.as_expr()),
  multiplicative_order=order,rays=records,relation=str(result))

def main():
 start=time.monotonic();ctx=Context(max_operations=30000000);records=[];literal_checks=0;seed_results=[]
 for name,images in [('identity',['R','L']*4),('five',['RRRRR','LLLLL']*4),('nine',['RLLLLRRRR','LRRRRLLLL']*4)]:
  shift,rat=extract_rationals(images);Q={};states=[]
  for s,(P,H,p,h) in enumerate(rat):
   q,cert=parity_relation(ctx,p,h,shift)
   signed_filter=denominator_test(P/H,V)
   states.append(dict(state=s,integer_numerator=str(P),integer_denominator=str(H),parity_numerator=str(p.as_expr()),
    parity_denominator=str(h.as_expr()),signed_denominator_filter=signed_filter,parity_certificate=cert))
   if q is not None:Q[s]=q
  if name in ('identity','five'):
   assert len(Q)==8
   for s in range(8):
    for r in range(5):
     word=[s];phi=typed(images)
     for _ in range(r):word=[t for st in word for t,p in phi[st]]
     actual=read_parity(word)[0]
     expected=ctx.set('{ [r,x,y] : r='+str(r)+' and ('+(' or '.join(f'(x={x} and y={y})' for x,y in sorted(actual)) or '0=1')+') }')
     assert Q[s].intersect(ctx.set('{ [r,x,y] : r='+str(r)+' }')).is_equal(expected)
     literal_checks+=1
   for root in (0,1):
    for mass in (0,1):
     ctx.reset_operations();ans=solve(ctx,images,root,Q,mass)
     assert ans['status']=='decided'
     assert ans['possible']==(name=='identity' and (root%2==0 or mass>=1))
     ans['name']=name;ans['root']=root;seed_results.append(ans)
  else:
   assert not Q and all(not s['signed_denominator_filter']['passes'] for s in states)
  records.append(dict(name=name,images=images,linear_shift=shift,states=states))
 # Synthetic controls ensure extraction handles nontrivial univariate factors,
 # polynomial transients, overlap cancellation and unsupported 2D denominators.
 synthetic=[]
 for name,F,shift,expected in [
  ('zero',S.Integer(0),(0,0),True),
  ('order_three',1/(1+Z*X+Z**2*X**2),(0,0),True),
  ('repeated_factor',1/(1+Z*X)**3,(0,0),True),
  ('cancelled_overlap',(1+Z*X)/(1+Z**2*X**2),(0,0),True),
  ('polynomial',1+Z*X*Y+Z**2,(1,1),True),
  ('Pascal',1/(1+Z+Z*X),(0,0),False)]:
  P,H=S.fraction(S.cancel(F));p=S.Poly(P,*V,modulus=2);h=S.Poly(H,*V,modulus=2)
  q,cert=parity_relation(ctx,p,h,shift);assert (q is not None)==expected
  cert['name']=name;synthetic.append(cert)
 out=dict(records=records,synthetic=synthetic,literal_depth_fiber_equalities=literal_checks,
  seed_results=seed_results,accepted_growing_models=sum(r['accepted_growing_model'] for r in seed_results),
  scope='Executed exact image-to-rational-to-Presburger-parity-to-arbitrary-coordinate bounded-seed pipeline for one-ray F2 denominators. Other parity denominators unsupported. No new class exclusion or accepted growing model.',seconds=time.monotonic()-start)
 (HERE/'ray_parity_extractor.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('records','synthetic','seed_results')},indent=2))
 print([(r['name'],r['root'],r['mass_bound'],r['possible']) for r in seed_results])
if __name__=='__main__':main()
