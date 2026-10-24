"""Exact rational dual certificates for cap-free prepared wake incidence bounds.
Floating LP proposes a dual; Fraction arithmetic verifies every inequality.
Chronology is still separate. Bounds apply to the specified finite read strip.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent
W=set(map(tuple,json.loads((P/'shifted_reverse104_bulk.json').read_text())['wake_black_classes']))
D=((0,1),(1,0),(0,-1),(-1,0))
def model(height,offset,sector=1):
 ps=[(x,x+y+offset)for y in range(height)for x in range(2)];ix={p:i for i,p in enumerate(ps)};axis=lambda p:(sector-sum(p))%2
 keys=[(i,h,s)for i,p in enumerate(ps)for h in range(4)if h%2==axis(p)for s in(1,-1)];n=len(keys);N=n+len(ps);A=[];b=[];names=[]
 def eq(row,rhs,name):A.append(row);b.append(rhs);names.append(name)
 for i,p in enumerate(ps):
  row=[0]*N
  for j,(ii,h,s)in enumerate(keys):
   if ii==i:row[j]=s
  row[n+i]=-1;eq(row,-int((p[0]-p[1],p[0]%2)in W),f'color{i}')
  for h in range(4):
   if h%2!=axis(p):continue
   vx,vy=D[h];a=(p[0]-vx,p[1]-vy);q=(a[0]%2,a[1]-2*(a[0]//2));ii=ix.get(q);row=[0]*N
   for j,(k,hh,s)in enumerate(keys):
    row[j]=int(k==i and hh==h)-int(k==ii and(hh+s)%4==h)
   eq(row,0,f'edge{i}_{h}')
  for h in range(4):
   if h%2==axis(p):continue
   vx,vy=D[h];a=(p[0]+vx,p[1]+vy);q=(a[0]%2,a[1]-2*(a[0]//2))
   if q not in ix:
    row=[int(k==i and(hh+s)%4==h)for k,hh,s in keys]+[0]*len(ps);eq(row,0,f'exit{i}_{h}')
 for ax in range(2):eq([D[(h+s)%4][ax]for i,h,s in keys]+[0]*len(ps),-2,f'displacement{ax}')
 return ps,keys,A,b,names

def run(height=4,offset=-2):
 ps,keys,A,b,names=model(height,offset);n=len(keys);N=n+len(ps);bounds=[(0,None)]*n+[(0,1)]*len(ps);res=[]
 for target in[-1]+list(range(len(ps))):
  objective=[int(target<0 or i==target)for i,h,s in keys]+[0]*len(ps)
  lp=linprog(-np.array(objective),A_eq=A,b_eq=b,bounds=bounds,method='highs')
  if not lp.success:raise RuntimeError(lp.message)
  # SciPy minimizes negative objective. Negate equality and upper marginals.
  y=[-F(float(v)).limit_denominator(1000000)for v in lp.eqlin.marginals]
  z=[-F(float(v)).limit_denominator(1000000)for v in lp.upper.marginals]
  assert all(v>=0 for v in z)
  assert all(z[j]==0 for j in range(n))
  assert all(sum(y[i]*A[i][j]for i in range(len(A)))+z[j]>=objective[j]for j in range(N))
  upper=sum(yy*bb for yy,bb in zip(y,b))+sum(z[n:])
  assert abs(float(upper)+lp.fun)<1e-7
  row=dict(target='total'if target<0 else ps[target],upper=str(upper),integer_upper=upper.numerator//upper.denominator,dual_equalities=[str(v)for v in y],dual_upper=[str(v)for v in z[n:]])
  res.append(row)
 out=dict(scope=__doc__,height=height,offset=offset,sector=1,positions=ps,equality_names=names,bounds=res)
 (P/f'wake_return_flow_bounds_h{height}_off{offset}.json').write_text(json.dumps(out,indent=2)+'\n');print([(r['target'],r['upper'])for r in res]);return out
if __name__=='__main__':run()
