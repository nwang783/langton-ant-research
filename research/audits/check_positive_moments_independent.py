"""Independent rational occupation transfer and shift-operator pole certificate."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json,hashlib
import sympy as S
ROOT=Path(__file__).resolve().parents[1];F=ROOT/'computability/unit_fourier';X=S.Symbol('X');heads=(1j,1,-1j,-1)
def trace(w,h=1j):
 p=0j;reads=[]
 for c in w:reads.append((p,h,c));h*=(-1j if c=='R'else 1j);p+=h
 return reads
def advance(z,images,a,r,x,y):
 ans=[]
 for h in heads:
  for word in images:
   total=Q(0)
   for p,hh,c in trace(word,h):
    p*=1j**((a*r)%4);total+=x**int(p.real)*y**int(p.imag)*z[2*heads.index(hh)+(c=='L')]
   ans.append(total)
 return ans
controls=json.loads((F/'unit9_fourier.json').read_text())['geometric_controls'];literalchecks=0
for a,images in controls:
 for x,y in [(Q(2),Q(1)),(Q(1,2),Q(2)),(Q(3,2),Q(2,3))]:
  z=[Q(1),Q(-1)]*4;words=['R','L']
  for r in range(4):
   for hi,h in enumerate(heads):
    for i,w in enumerate(words):
     val=sum((1 if c=='R'else -1)*x**int(p.real)*y**int(p.imag)for p,hh,c in trace(w,h))
     assert val==z[2*hi+i];literalchecks+=1
   z=advance(z,images,a,r,x,y);words=[''.join(images[c=='L']for c in w)for w in words]
def check_certificate(seq,cert,D):
 P=S.Poly(cert['minimal_polynomial'],X);L=P.degree();co=[Q(str(z))for z in P.all_coeffs()]
 assert L<=D and len(seq)>=L+D
 assert all(sum(co[j]*seq[n-j]for j in range(L+1))==0 for n in range(L,len(seq)))
 hd=S.Matrix([[seq[i+j]for j in range(L)]for i in range(L)]).det()if L else S.Integer(1)
 assert hd!=0 and str(hd)==cert['hankel_determinant']
 r=S.Rational(cert['dominant_root']);m=cert['multiplicity'];assert r>1
 quotient,remainder=P.div(S.Poly((X-r)**m,X));assert remainder.is_zero and quotient.eval(r)!=0
 for fac,mul in S.factor_list(quotient)[1]:
  if fac.degree()==1:assert abs(-fac.nth(0)/fac.nth(1))<r
  else:assert fac.is_cyclotomic
 # Project away all other modes, then take m-1 exact R-forward differences.
 op=quotient*S.Poly((X-r)**(m-1),X)
 value=sum(op.nth(i)*seq[i]for i in range(op.degree()+1))
 leading=S.cancel(value/(factorial(m-1)*r**(m-1)*quotient.eval(r)))
 assert str(leading)==cert['leading_coefficient']and bool(leading<0)==cert['certified']
 return leading
synthetic=json.loads((F/'check_positive_moments.json').read_text())['synthetic']
for c in synthetic:
 b=Q(c['base']);m=c['multiplicity'];sign=c['sign'];seq=[sign*b**n*(n+1)**(m-1)+(-1)**n for n in range(60)]
 assert check_certificate(seq,c['certificate'],8)==sign
rows=json.loads((F/'positive_controls.records.json').read_text());count=0;pairs=set()
for row in rows:
 for test in row['tests']:
  if not test['negative_divergence']:continue
  x=Q(test['x']);y=Q(test['y']);z=[Q(1),Q(-1)]*4;seq=[]
  for r in range(65):seq.append(z[0]);z=advance(z,[row['R'],row['L']],0,r,x,y)
  for cert in test['records']:
   if cert['certified']:
    assert cert['phase']==0;check_certificate(seq[cert['block_parity']::2],cert,8);count+=1;pairs.add((row['R'],row['L']))
assert len(pairs)==10
out=dict(status='PASS positive-moment lower-bound obstruction and frozen negative certificates',rational_literal_checks=literalchecks,synthetic_leading_cases=len(synthetic),negative_certificates=count,covered_pairs=len(pairs),independent_leading_method='Exact shift-operator projection, not generating-function evaluation',scope='One-sided finite-support obstruction only; positive divergence or no certificate gives no conclusion. Current implementation validates charge-preserving images although the coefficientwise lower-bound theorem itself does not need charge preservation.',sha256={f:hashlib.sha256((F/f).read_bytes()).hexdigest()for f in ['positive_moments.md','positive_moments.py','positive_controls.records.json']})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
