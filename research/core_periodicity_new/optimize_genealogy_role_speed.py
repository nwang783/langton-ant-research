"""Find and EXACTLY certify the maximum cycle displacement/C ratio.
Floating LP is only a discovery aid. Final integer all-edge potential plus an
attained directed cycle proves the rational optimum without trusting LP.
CLI ROLE_GRAPH.json PREFIX.
"""
from pathlib import Path
from fractions import Fraction
import sys,json,hashlib
import numpy as np
from scipy.sparse import coo_matrix
from scipy.optimize import linprog
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());V=J['roles'];E=J['all_fundamental_edges'];nv=len(V);ne=len(E);rr=[];cc=[];vv=[];b=[]
for i,(u,v,n,d)in enumerate(E):
 rr.extend([i,i,i]);cc.extend([0,u+1,v+1]);vv.extend([-n,-1,1]);b.append(-d)
A=coo_matrix((vv,(rr,cc)),shape=(ne,nv+1)).tocsr();cost=np.zeros(nv+1);cost[0]=1
res=linprog(cost,A_ub=A,b_ub=b,bounds=[(0,1)]+[(None,None)]*nv,method='highs');assert res.success,res.message
r=Fraction(float(res.x[0])).limit_denominator(nv*max(e[2]for e in E));p,q=r.numerator,r.denominator
D=[0]*nv
for k in range(nv):
 change=False
 for u,v,n,d in E:
  x=D[u]+p*n-q*d
  if D[v]>x:D[v]=x;change=True
 if not change:break
else:raise AssertionError(('rational candidate has negative cycle',str(r)))
lo=min(D);D=[x-lo for x in D];margins=[p*n+D[u]-D[v]-q*d for u,v,n,d in E];assert min(margins)>=0
adj=[[]for _ in V];radj=[[]for _ in V];tight=[]
for i,(u,v,n,d)in enumerate(E):
 if margins[i]==0:adj[u].append((v,i));radj[v].append(u);tight.append(i)
seen=set();order=[]
def visit(u):
 seen.add(u)
 for v,i in adj[u]:
  if v not in seen:visit(v)
 order.append(u)
for u in range(nv):
 if u not in seen:visit(u)
cl=[-1]*nv;comps=[]
def back(u,c):
 cl[u]=c;comps[c].append(u)
 for v in radj[u]:
  if cl[v]<0:back(v,c)
for u in reversed(order):
 if cl[u]<0:comps.append([]);back(u,len(comps)-1)
cyclic=[c for c in comps if len(c)>1 or any(v==c[0]for v,i in adj[c[0]])];assert cyclic,'No attaining cycle: rational candidate was only an upper bound.'
# Simple DFS extracts a genuine directed zero-margin cycle.
cycle=None
for comp in cyclic:
 allowed=set(comp);color={};parent={}
 def dfs(u):
  global cycle
  color[u]=1
  for v,ei in adj[u]:
   if v not in allowed:continue
   if color.get(v)==1:
    path=[ei];z=u
    while z!=v:z,ee=parent[z];path.append(ee)
    path.reverse();cycle=path;return True
   if not color.get(v):
    parent[v]=(u,ei)
    if dfs(v):return True
  color[u]=2;return False
 for u in comp:
  if not color.get(u)and dfs(u):break
 if cycle is not None:break
assert cycle is not None
sumC=sum(E[i][2]for i in cycle);sumY=sum(E[i][3]for i in cycle);assert Fraction(sumY,sumC)==r
for i,j in zip(cycle,cycle[1:]+cycle[:1]):assert E[i][1]==E[j][0]
O=dict(status='AUTHOR_EXACT_MAX_CYCLE_RATIO_CERTIFICATE_NOT_INDEPENDENT',scope='Exact optimum only for the supplied signed-relation relaxation graph. All edges remain merely unexcluded, not physically realizable. Larger Cgaps+4 preserve the upper bound.',source_file=str(src.resolve()),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),rho_numerator=p,rho_denominator=q,rho_decimal=float(r),integer_potential=D,potential_range=max(D)-min(D),all_edge_count=ne,minimum_integer_margin=min(margins),tight_edges=tight,critical_SCCs=cyclic,critical_roles=[[V[u]for u in comp]for comp in cyclic],attaining_cycle_edge_ids=cycle,attaining_cycle_edges=[E[i]for i in cycle],attaining_cycle_roles=[V[E[i][0]]for i in cycle],attaining_cycle_total_C=sumC,attaining_cycle_total_dy=sumY,discovery_lp_objective=float(res.x[0]))
out.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print({k:v for k,v in O.items()if k not in ['integer_potential','tight_edges','critical_SCCs','critical_roles']});print('critical_SCC_sizes',[len(c)for c in cyclic])
