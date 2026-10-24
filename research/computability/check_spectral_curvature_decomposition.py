#!/usr/bin/env python3
"""Exact algebra controls; these are geometric words, NOT ant models."""
from fractions import Fraction as Q
from pathlib import Path
import random,json
D=((0,1),(1,0),(0,-1),(-1,0))
I=((Q(1),Q(0)),(Q(0),Q(1)))
def mm(a,b):return tuple(tuple(sum(a[i][h]*b[h][j] for h in range(2)) for j in range(2)) for i in range(2))
def mv(a,x):return tuple(sum(a[i][j]*x[j] for j in range(2)) for i in range(2))
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def scale(c,x):return tuple(c*a for a in x)
def inv(a):
 det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
 return ((a[1][1]/det,-a[0][1]/det),(-a[1][0]/det,a[0][0]/det))
def mpow(a,n):
 out=I
 for _ in range(n):out=mm(out,a)
 return out
def coeff(b):return Q(sum(b),4),Q(b[1]+b[3]-b[0]-b[2],4),(Q(b[1]-b[3],2),Q(b[0]-b[2],2))
def curvature(w):return sum(1 if (v-u)%4==1 else -1 for u,v in zip(w,w[1:]))
def forcing(images):
 f=[w[0] for w in images];g=[w[-1] for w in images]
 fp=tuple(range(4));gp=fp;seen={};bs=[]
 while (fp,gp) not in seen:
  seen[fp,gp]=len(bs)
  b=[]
  for w in images:
   pairs=[(gp[u],fp[v]) for u,v in zip(w,w[1:])]
   assert all((u-v)%2 for u,v in pairs)
   b.append(sum(1 if (v-u)%4==1 else -1 for u,v in pairs))
  bs.append(b);fp=tuple(f[x] for x in fp);gp=tuple(g[x] for x in gp)
 return bs,seen[fp,gp],len(bs)-seen[fp,gp]
def constants(A,k,bs,t,q):
 B=inv(tuple(tuple(Q(A[j][i]) for j in range(2)) for i in range(2)))
 C=sum(coeff(bs[j-1])[0]/k**j for j in range(1,t+1))
 C+=Q(1,k**t)*sum(coeff(bs[t+j-1])[0]/k**j for j in range(1,q+1))/(1-Q(1,k**q))
 ell=(Q(0),Q(0))
 for j in range(1,t+1):ell=add(ell,mv(mpow(B,j),coeff(bs[j-1])[2]))
 tail=(Q(0),Q(0))
 for j in range(1,q+1):tail=add(tail,mv(mpow(B,j),coeff(bs[t+j-1])[2]))
 Bq=mpow(B,q);one_minus=tuple(tuple(I[i][j]-Bq[i][j] for j in range(2)) for i in range(2))
 ell=add(ell,mv(mm(mpow(B,t),inv(one_minus)),tail))
 return C,ell
def random_images(A,k,mode,rng):
 out=[]
 for d,(x,y) in enumerate(D):
  tx,ty=mv(A,(x,y))
  first=(d%2 if mode=='preserve' else 1-d%2) if k%2 else 1
  H=(k+int(first==1))//2;V=k-H
  assert (H+tx)%2==0 and (V+ty)%2==0 and abs(tx)<=H and abs(ty)<=V
  hh=[1]*((H+tx)//2)+[3]*((H-tx)//2);vv=[0]*((V+ty)//2)+[2]*((V-ty)//2)
  rng.shuffle(hh);rng.shuffle(vv);hi=vi=0;w=[]
  for j in range(k):
   if (first+j)%2==1:w.append(hh[hi]);hi+=1
   else:w.append(vv[vi]);vi+=1
  assert tuple(sum(D[z][i] for z in w) for i in range(2))==(tx,ty)
  out.append(tuple(w))
 return out
def check(A,k,mode,images):
 M=[[w.count(d) for d in range(4)] for w in images]
 chi=(-1,1,-1,1);epsilon=0 if k%2==0 else (1 if mode=='preserve' else -1)
 for d in range(4):
  assert sum(M[d])==k
  assert sum(M[d][e]*chi[e] for e in range(4))==epsilon*chi[d]
  assert tuple(sum(M[d][e]*D[e][i] for e in range(4)) for i in range(2))==mv(A,D[d])
 bs,t,q=forcing(images);C,ell=constants(A,k,bs,t,q)
 words=[(d,) for d in range(4)];prev=[0]*4;checks=[]
 for r in range(1,4):
  words=[tuple(z for d in w for z in images[d]) for w in words]
  now=[curvature(w) for w in words]
  b=bs[r-1 if r-1<len(bs) else t+(r-1-t)%q]
  assert now==[sum(M[d][e]*prev[e] for e in range(4))+b[d] for d in range(4)]
  checks.append(now);prev=now
 return dict(matrix=A,k=k,axis_mode=mode,images=images,forcing_preperiod=t,forcing_period=q,
  C=str(C),ell=list(map(str,ell)),literal_curvatures=checks,
  halfturn=all(images[(d+2)%4]==tuple((z+2)%4 for z in images[d]) for d in range(4)))
cases=[(((1,-2),(2,1)),9,'preserve'),(((-3,0),(0,5)),17,'preserve'),
 (((-3,2),(0,-3)),13,'preserve'),(((3,0),(0,-3)),13,'preserve'),
 (((2,-2),(2,2)),12,'common'),(((0,-3),(3,0)),13,'swap')]
rng=random.Random(739153);records=[];trials=[]
for A,k,mode in cases:
 zero=[];nonzero=[]
 for attempt in range(1,2001):
  imgs=random_images(A,k,mode,rng);bs,t,q=forcing(imgs);C,ell=constants(A,k,bs,t,q)
  if C==0 and len(zero)<3:zero.append(check(A,k,mode,imgs))
  elif C!=0 and not nonzero:nonzero.append(check(A,k,mode,imgs))
  if len(zero)==3 and nonzero:break
 records+=zero+nonzero;trials.append(dict(matrix=A,k=k,attempts=attempt,zero_mode_controls=len(zero)))
assert all(not r['halfturn'] for r in records)
out=dict(status='EXACT INCIDENCE AND LITERAL CURVATURE CONTROLS PASS',
 note='Geometric substitutions only; no ant legality or finite-support model claimed.',
 trials=trials,controls=records)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='controls'}));print('controls',len(records))
