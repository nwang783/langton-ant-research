"""Exact cyclotomic occupation transfer for unit-scale, heading-preserving turn morphisms.
This is a necessary ant-realizability test, not a complete validator.
"""
from fractions import Fraction as Q
import sympy as S

X=S.Symbol('X')
DIR=((0,1),(1,0),(0,-1),(-1,0))

def rotate(p,a):
 x,y=p
 for _ in range(a%4):x,y=-y,x
 return x,y

def image_data(word):
 p=(0,0);h=0;out=[]
 for ch in word:
  s=1 if ch=='R' else -1
  out.append((p,h,0 if s==1 else 1))
  h=(h+s)%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
 return out,p,h

def validate(images,a):
 k=max(map(len,images));assert k>1 and min(map(len,images))>=1
 for j,w in enumerate(images):
  assert set(w)<=set('RL')
  data,p,h=image_data(w);sgn=1 if j==0 else -1
  assert h==sgn%4 and p==rotate((sgn,0),a)
  assert w.count('R')-w.count('L')==sgn
 return k

def cyclotomic_ring(q):
 P=S.Poly(S.cyclotomic_poly(q,X),X);d=P.degree()
 # z^n reduced to an integral coefficient vector, 0<=n<q.
 powers=[]
 for n in range(q):
  v=S.Poly(X**n,X).rem(P)
  powers.append(tuple(int(v.nth(j)) for j in range(d)))
 return d,powers

def phase_matrices(images,a,q,u,v):
 """A clockwise heading index h rotates the north-base image by -h quarter turns.
 a is the counterclockwise Gaussian-unit exponent. Rows are parent states;
 columns are refined child states. The coefficient basis is 1,z,...,z^(phi(q)-1).
 """
 validate(images,a);d,powers=cyclotomic_ring(q);D=8*d
 order=next(r for r in range(1,5) if a*r%4==0)
 mats=[]
 for phase in range(order):
  M=[[0]*D for _ in range(D)]
  for h in range(4):
   for j in range(2):
    row=2*h+j
    for p,hj,sj in image_data(images[j])[0]:
     p=rotate(p,a*phase-h);child=2*((h+hj)%4)+sj
     exponent=(u*p[0]+v*p[1])%q
     for b in range(d):
      prod=powers[(exponent+b)%q]
      for c,z in enumerate(prod):M[row*d+c][child*d+b]+=z
  mats.append(M)
 initial=[0]*D
 for h in range(4):initial[(2*h)*d]=1;initial[(2*h+1)*d]=-1
 return d,mats,initial

def mv(M,v):return [sum(a*b for a,b in zip(row,v)) for row in M]

def block_step(mats,v):
 for M in mats:v=mv(M,v)
 return v

def bm(seq):
 C=[Q(1)];B=[Q(1)];L=0;m=1;b=Q(1)
 for n,z in enumerate(seq):
  delta=Q(z)+sum(C[i]*seq[n-i] for i in range(1,L+1))
  if not delta:m+=1;continue
  T=C[:];fac=delta/b
  if len(C)<len(B)+m:C += [Q(0)]*(len(B)+m-len(C))
  for i in range(len(B)):C[i+m]-=fac*B[i]
  if 2*L<=n:L=n+1-L;B=T;b=delta;m=1
  else:m+=1
 return C[:L+1]

def recurrence_certificate(seq,D):
 C=bm(seq[:2*D+1]);L=len(C)-1
 assert all(Q(seq[n])+sum(C[i]*seq[n-i] for i in range(1,L+1))==0 for n in range(L,len(seq)))
 poly=S.Poly(sum(S.Rational(z.numerator,z.denominator)*X**(L-i) for i,z in enumerate(C)),X)
 hankel_det=S.Matrix([[seq[i+j] for j in range(L)] for i in range(L)]).det() if L else S.Integer(1)
 assert hankel_det!=0
 fac=S.factor_list(poly)[1]
 bounded=all(p==S.Poly(X,X) or (e==1 and p.is_cyclotomic) for p,e in fac)
 return dict(recurrence=[str(z) for z in C],polynomial=str(poly.as_expr()),hankel_determinant=str(hankel_det),bounded=bounded,
             factors=[dict(polynomial=str(p.as_expr()),multiplicity=e,cyclotomic=bool(p.is_cyclotomic)) for p,e in fac])

def test_character(images,a,q,u,v,root='R',all_states=False):
 d,mats,z=phase_matrices(images,a,q,u,v);D=len(z)
 roots=range(8) if all_states else [0 if root=='R' else 1]
 seq={(ph,st,b):[] for ph in range(len(mats)) for st in roots for b in range(d)}
 for r in range(3*D+3):
  cur=z
  for ph in range(len(mats)):
   for st in roots:
    for b in range(d):seq[ph,st,b].append(cur[st*d+b])
   cur=mv(mats[ph],cur)
  z=cur
 cert=[]
 for (ph,st,b),values in seq.items():
  c=recurrence_certificate(values,D);c.update(phase=ph,state=st,basis=b)
  cert.append(c)
 return dict(modulus=q,character=[u,v],dimension=D,rotation_period=len(mats),
             bounded=all(c['bounded'] for c in cert),certificates=cert)

def literal_occupation(images,root,depth):
 word=root
 for _ in range(depth):word=''.join(images[0 if c=='R' else 1] for c in word)
 result={};p=(0,0);h=0
 for c in word:
  s=1 if c=='R' else -1;result[p]=result.get(p,0)+s
  h=(h+s)%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
 return {p:c for p,c in result.items() if c},p,h

def eval_occupation(occ,q,u,v):
 d,pow=cyclotomic_ring(q);out=[0]*d
 for (x,y),z in occ.items():
  for b,c in enumerate(pow[(u*x+v*y)%q]):out[b]+=z*c
 return out
