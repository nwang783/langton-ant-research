"""One exact actual-geometry transfer extraction, not a candidate search."""
import pathlib,sys,time,json
import sympy as S
from sympy.polys.matrices import DomainMatrix
HERE=pathlib.Path(__file__).parent
sys.path.insert(0,str(HERE.parent/'unit_inductive_certificates'))
from check_read_sets import typed

def main():
 start=time.monotonic();z,x,y=S.symbols('z x y');images=['RLLLLRRRR','LRRRRLLLL']*4;phi=typed(images)
 C=max(0,-min(p[0] for row in phi for t,p in row));D=max(0,-min(p[1] for row in phi for t,p in row))
 T=S.zeros(8)
 for s,row in enumerate(phi):
  for t,p in row:T[s,t]+=x**(p[0]+C)*y**(p[1]+D)
 M=DomainMatrix.from_Matrix(S.eye(8)-z*T)
 rhs=DomainMatrix.from_Matrix(S.Matrix([1,-1]*4)).convert_to(M.domain)
 print('begin exact transfer solve',flush=True)
 num,den=M.solve_den(rhs);N=num.to_Matrix();den=M.domain.to_sympy(den)
 print('solved',time.monotonic()-start,flush=True)
 records=[]
 for s in range(8):
  P,H=S.fraction(S.cancel(N[s]/den))
  pp=S.Poly(P,z,x,y,modulus=2);hh=S.Poly(H,z,x,y,modulus=2)
  g=S.gcd(pp,hh);pp=pp.exquo(g);hh=hh.exquo(g)
  records.append(dict(state=s,integer_numerator=str(P),integer_denominator=str(H),
   parity_numerator=str(pp.as_expr()),parity_denominator=str(hh.as_expr()),
   integer_denominator_factors=str(S.factor(H)),parity_terms=[len(pp.terms()),len(hh.terms())]))
  print(s,records[-1]['parity_terms'],flush=True)
 out=dict(images=images,linear_shift=[C,D],records=records,seconds=time.monotonic()-start,
  scope='Actual typed geometry rational occupation extraction only; no ant legality or finite seed claimed.')
 (HERE/'rational_occupation_probe.json').write_text(json.dumps(out,indent=2)+'\n')
 print(out['seconds'],flush=True)
if __name__=='__main__':main()
