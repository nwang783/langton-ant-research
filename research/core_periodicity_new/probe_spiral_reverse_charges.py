"""Exact mod-four charge lower bounds for reversed seven-arm interfaces.
Exploratory only; not a feasibility or impossibility theorem beyond each output.
"""
from collections import Counter
import json
from pathlib import Path
CAP={(1,-1),(1,0),(-1,1),(0,1),(-3,0),(-3,1),(-2,-1),(-1,-1),(-2,1)}
def E(n):
 b=set(CAP)
 for j in range(2,n+1):b.update({(j,-j),(j,j-1),(j-1,j),(-j-2,1-j),(-j-2,j),(-j-1,-j),(j-2,-j)})
 return b
def rot(p,k):
 x,y=p
 for _ in range(k):x,y=y,-x
 return x,y
def F(c,x,h,chi):
 a=int(c==x);g=0 if x<c else 1 if x==c else 2
 return chi*[-g,g-a,-g+2*a,g+a][h]
def sums(B,axis):
 d=Counter()
 for x,y in B:d[(x,y)[axis]]+=1 if (x+y)%2==0 else-1
 return d
def score(a,b,p,h,chi):
 lo=min(min(a),min(b),0,p)-2;hi=max(max(a),max(b),0,p)+2
 return sum(min(z,4-z) for c in range(lo,hi+1) for z in [(a[c]+F(c,0,0 if h[1]==0 else 1,1)-b[c]-F(c,p,h[0],chi))%4])
def run(n,m):
 B=E(n); A=[sums(B,i) for i in (0,1)];out=[]
 for k in range(4):
  parity=(k+1)%2;sgn=1 if parity==0 else-1;C={rot(q,k) for q in E(m)};Cs=[sums(C,i) for i in(0,1)];p=rot((0,-1),k);h=(2+k)%4;chi=1 if h%2==0 else-1
  vals=[]
  for axis in(0,1):
   choices={0:[],1:[]}
   for t in range(-2*(n+m)-6,2*(n+m)+7):
    b=Counter({c+t:sgn*v for c,v in Cs[axis].items()});x=p[axis]+t;oldh=axis;newh=(h+axis)%4
    lo=min(min(A[axis]),min(b),0,x)-2;hi=max(max(A[axis]),max(b),0,x)+2
    z=[(A[axis][c]+F(c,0,oldh,1)-b[c]-F(c,x,newh,chi))%4 for c in range(lo,hi+1)]
    sc=sum(min(v,4-v) for v in z)
    choices[t%2].append((sc,t))
   vals.append({q:sorted(v)[:6] for q,v in choices.items()})
  cand=[]
  for q in(0,1):
   for xc,tx in vals[0][q]:
    for yc,ty in vals[1][parity^q]:cand.append((max(xc,yc),xc+yc,tx,ty,xc,yc))
  out.append({'rotation':k,'best':sorted(cand)[:6]})
 return {'n':n,'m':m,'cases':out}
if __name__=='__main__':
 out=[run(n,m) for n in [5,10,20,40,80] for m in[n,n+1]]
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
 for x in out:print(x['n'],x['m'],[(c['rotation'],c['best'][0]) for c in x['cases']],flush=True)
