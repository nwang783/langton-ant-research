"""Sound restricted exact negative-divergence certificates at positive characters.
No certificate is not a boundedness or realizability verdict.
"""
from fourier_transfer import *

def matrices(images,a,x,y):
 validate(images,a);x=Q(x);y=Q(y);assert x>0 and y>0
 order=next(r for r in range(1,5) if a*r%4==0);out=[]
 for phase in range(order):
  M=[[Q(0)]*8 for _ in range(8)]
  for h in range(4):
   for j in range(2):
    for p,hj,sj in image_data(images[j])[0]:
     px,py=rotate(p,a*phase-h)
     M[2*h+j][2*((h+hj)%4)+sj]+=x**px*y**py
  out.append(M)
 return out,[Q(1),Q(-1)]*4

def negative_divergence(seq,D):
 C=bm(seq[:2*D+1]);L=len(C)-1
 assert all(Q(seq[n])+sum(C[i]*seq[n-i] for i in range(1,L+1))==0 for n in range(L,len(seq)))
 det=S.Matrix([[S.Rational(seq[i+j]) for j in range(L)] for i in range(L)]).det() if L else S.Integer(1)
 assert det!=0
 P=S.Poly(sum(S.Rational(c)*X**(L-i) for i,c in enumerate(C)),X)
 fs=S.factor_list(P)[1];roots=[]
 for f,m in fs:
  if f.degree()==1:roots.append((-f.nth(0)/f.nth(1),m))
  elif not f.is_cyclotomic:
   return dict(certified=False,reason='nonlinear noncyclotomic residual',minimal_polynomial=str(P.as_expr()))
 R=max([abs(r) for r,m in roots]+[S.Integer(1)])
 top=[(r,m) for r,m in roots if abs(r)==R]
 if R<=1 or len(top)!=1 or top[0][0]!=R:
  return dict(certified=False,reason='no unique positive rational dominant root above one',minimal_polynomial=str(P.as_expr()))
 m=top[0][1]
 Den=sum(S.Rational(c)*X**i for i,c in enumerate(C))
 Num=sum(sum(S.Rational(C[j])*S.Rational(seq[i-j]) for j in range(i+1))*X**i for i in range(L))
 H=S.cancel(Den/(1-R*X)**m)
 leading=S.cancel(Num.subs(X,1/R)/H.subs(X,1/R)/S.factorial(m-1))
 assert leading!=0
 return dict(certified=bool(leading<0),reason='negative dominant coefficient' if leading<0 else 'positive dominant coefficient',
  minimal_polynomial=str(P.as_expr()),dominant_root=str(R),multiplicity=m,leading_coefficient=str(leading),
  hankel_determinant=str(det))

def test(images,a,x,y,root='R'):
 mats,z=matrices(images,a,x,y);D=8;seq=[[] for _ in mats];idx=0 if root=='R' else 1
 for r in range(6*D+7):
  cur=z
  for ph,M in enumerate(mats):
   seq[ph].append(cur[idx]);cur=mv(M,cur)
  z=cur
 records=[]
 for ph,values in enumerate(seq):
  for parity in range(2):
   c=negative_divergence(values[parity::2],D);c.update(phase=ph,block_parity=parity);records.append(c)
 return dict(x=str(x),y=str(y),negative_divergence=any(r['certified'] for r in records),records=records)

if __name__=='__main__':
 import json
 im=('RLLRRRRLL','RRLLLLRRL')
 print(json.dumps(test(im,0,2,1)))
