"""Discovery LP/MILP minimization; verify any integral primal exactly.
Floating optimizer status alone is NOT a proof of a lower bound.
"""
import json,pathlib
import numpy as np
from scipy.optimize import milp,linprog,Bounds,LinearConstraint
H=5;P=8;D=((0,1),(1,0),(0,-1),(-1,0))
ans=[]
for sigma in(0,1):
 states=[(x,y,h)for x in range(P)for y in range(H)for h in range(4)if(x+y+h)%2==sigma]
 edges=[]
 for a in states:
  for c in(1,-1):
   x,y,h=a;hh=(h+c)%4;dx,dy=D[hh];b=((x+dx)%P,y+dy,hh)
   if 0<=b[1]<H:edges.append((a,b,c,dx))
 rows=[];rhs=[]
 for a in states:rows.append([int(e[1]==a)-int(e[0]==a)for e in edges]);rhs.append(0)
 for x in range(P):
  for y in range(H):
   rows.append([e[2]if e[0][:2]==(x,y)else 0 for e in edges]);rhs.append(int(y in(0,2)or(y==3 and x%2))-int(y==1 and x%2))
 rows.append([e[3]for e in edges]);rhs.append(P)
 A=np.array(rows);b=np.array(rhs);c=np.ones(len(edges));lp=linprog(c,A_eq=A,b_eq=b,bounds=(0,None),method='highs');mp=milp(c,integrality=np.ones(len(edges)),bounds=Bounds(0,np.inf),constraints=LinearConstraint(A,b,b),options={'time_limit':20})
 d=dict(sector=sigma,lp_status=lp.message,lp_value=lp.fun,milp_status=mp.message,milp_value=mp.fun)
 if mp.x is not None:
  v=np.rint(mp.x).astype(int);assert np.all(A@v==b)and np.all(v>=0);d['exact_integral_primal_sum']=int(v.sum());d['flow']=[[list(edges[i][0]),edges[i][2],int(n)]for i,n in enumerate(v)if n]
 if lp.success:d['lp_dual']=lp.eqlin.marginals.tolist()
 ans.append(d)
p=pathlib.Path(__file__).with_suffix('.json');p.write_text(json.dumps(ans,indent=2)+'\n');print(json.dumps([{k:v for k,v in d.items()if k not in('flow','lp_dual')}for d in ans],indent=2))
