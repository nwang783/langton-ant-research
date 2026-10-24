"""Exact necessary finite-coefficient-range filter, not a chronology test.
A bounded integer rational array has a reduced denominator which is a
product of cyclotomic polynomials in nonnegative primitive monomials.
"""
import functools,math,json,pathlib,time
import sympy as S
HERE=pathlib.Path(__file__).parent

def denominator_test(expr,variables):
 num,den=S.fraction(S.cancel(expr)); denpoly=S.Poly(den,*variables,domain=S.QQ)
 assert denpoly.coeff_monomial((0,)*len(variables))!=0
 records=[]
 for factor,multiplicity in S.factor_list(denpoly.as_expr(),*variables)[1]:
  P=S.Poly(factor,*variables,domain=S.QQ); exponents=P.monoms()
  nz=[v for v in exponents if any(v)]; reason=None; primitive=None; uni=None
  first=nz[0];g=functools.reduce(math.gcd,first);primitive=tuple(v//g for v in first)
  pivot=next(i for i,v in enumerate(primitive) if v)
  degrees=[]
  for v,c in P.terms():
   n,rem=divmod(v[pivot],primitive[pivot])
   if rem or tuple(n*w for w in primitive)!=v:
    reason='factor support is not on one monomial ray';break
   degrees.append((n,c))
  if reason is None:
   t=S.Symbol('t');uni=S.Poly(sum(c*t**n for n,c in degrees),t,domain=S.QQ).monic()
   if not uni.is_cyclotomic:reason='one-ray factor is not cyclotomic'
  records.append(dict(factor=str(factor),multiplicity=multiplicity,primitive_monomial=primitive,
   univariate=None if uni is None else str(uni.as_expr()),passes=reason is None,reason=reason))
 return dict(passes=all(r['passes'] for r in records),reduced_numerator=str(num),
  reduced_denominator=str(den),factors=records)

def main():
 start=time.monotonic();z,x,y=S.symbols('z x y');v=(z,x,y)
 # R^(5^r), with all four read sites shifted up one in y.
 root= y*(S.Rational(1,4)/(1-5*z)+S.Rational(3,4)/(1-z))
 other=(x*y+x+1)*(S.Rational(1,4)/(1-5*z)-S.Rational(1,4)/(1-z))
 cases=[('single_affine_particle',1/(1-z*x),True),
 ('two_dimensional_fiber',1/((1-z*x)*(1-z*y)),True),
 ('repeated_particle_pole',1/(1-z*x)**2,True),
 ('period_two_particle',1/(1-z**2*x**2),True),
 ('signed_period_three',1/(1+z*x+z*z*x*x),True),
 ('Pascal_coefficients',1/(1-z-z*x),False),
 ('exponential_single_site',1/(1-2*z),False),
 ('cancellation_removed', (1-z-z*x)/((1-z-z*x)*(1-z*x)),True),
 ('literal_right_five',root+other,False)]
 records=[]
 for name,F,expected in cases:
  r=denominator_test(F,v);assert r['passes']==expected;(r.update(name=name));records.append(r)
 # Independent literal R5 occupation at 4 sites, not legal on any board.
 direct_checks=0
 D=((0,1),(1,0),(0,-1),(-1,0))
 for r in range(7):
  p=(0,0);h=0;occ={}
  for _ in range(5**r):
   occ[p]=occ.get(p,0)+1;h=(h+1)%4;p=(p[0]+D[h][0],p[1]+D[h][1])
  expected={(0,0):(5**r+3)//4,(1,0):(5**r-1)//4,(1,-1):(5**r-1)//4,(0,-1):(5**r-1)//4}
  expected={p:c for p,c in expected.items() if c};assert occ==expected;direct_checks+=len(expected)
 out=dict(cases=len(cases),literal_occupation_checks=direct_checks,records=records,
  scope='Necessary reduced-denominator filter only. Passing does not imply bounded coefficients or legality.',seconds=time.monotonic()-start)
 (HERE/'binomial_denominator.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
