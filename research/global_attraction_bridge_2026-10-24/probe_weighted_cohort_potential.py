import json
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from pathlib import Path
from blank_collision_operator import *
P=Path(__file__).parent
rows=[];mask=set();seen=set()
def pow2(a):return Fraction(2)**a
for t,q in enumerate(CP[:500]):
 if q not in seen:
  seen.add(q)
  for h in range(4):
   x=rotate(q,h);incoming=(HEAD[t]+h)%4;hout=(incoming-1)%4;end=(x[0]+D[hout][0],x[1]+D[hout][1]);em=sum((pow2(rotate(z,h)[1])for z in mask),Fraction(0));a=[Fraction(0)for _ in range(4)];a[hout]+=pow2(end[1]);a[h]-=1;b=pow2(x[1])-em
   rows.append(dict(time=t,initial_heading=h,old_cell=x,new_pose=[end,hout],a=a,b=b,emission_weight=em))
 mask^={q}
AA=np.array([[float(a)for a in r['a']]for r in rows]);bb=np.array([float(r['b'])for r in rows]);z=linprog(np.zeros(4),A_ub=AA,b_ub=bb,bounds=[(None,None)]*4,method='highs');print('potentialLP',z.status,z.message)
if z.status==2:
 f=linprog(bb,A_eq=np.vstack([AA.T,np.ones(len(rows))]),b_eq=np.array([0,0,0,0,1]),bounds=(0,None),method='highs');inds=[i for i,x in enumerate(f.x)if x>1e-8];print('witness',f.fun,[(rows[i]['time'],rows[i]['initial_heading'],f.x[i])for i in inds])
 import sympy as sp
 A=sp.Matrix([[sp.Rational(x.numerator,x.denominator)for x in rows[i]['a']]for i in inds]);N=A.T.nullspace();assert len(N)==1
 lam=N[0];lam=lam/sum(lam);assert all(x>=0 for x in lam);rhs=sum(lam[j]*sp.Rational(rows[i]['b'].numerator,rows[i]['b'].denominator)for j,i in enumerate(inds));assert rhs<0
 out=[]
 for j,i in enumerate(inds):
  r=rows[i];out.append({k:([str(x)for x in v]if k=='a'else str(v)if isinstance(v,Fraction)else v)for k,v in r.items()}|dict(multiplier=str(lam[j])))
 print('exact',rhs,out)
 (P/'WEIGHTED_COHORT_POTENTIAL_DISCOVERY.json').write_text(json.dumps(dict(rows=out,total_rhs=str(rhs)),indent=2)+'\n')
