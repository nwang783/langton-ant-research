"""Exact certificate extraction after physical and provisional trap filters."""
from pathlib import Path
import json,numpy as np
from scipy.sparse import lil_matrix
from scipy.optimize import linprog
from fractions import Fraction
from math import lcm,gcd
from functools import reduce
p=Path(__file__).parent;K=json.loads((p/'component_kernel_M6.json').read_text())['transitions'];C=json.loads((p/'kernel_M6_compact_returns.json').read_text())['returns'];F=json.loads((p/'cap6_physical_return_filter.json').read_text());ids=F['feasible_indices'];A=lil_matrix((len(ids),134));used=set()
for a,i in enumerate(ids):
 for z in C[i]['indices']:
  t=K[z]
  if t['consume']is not None:A[a,t['consume']]-=1;used.add(t['consume'])
  if t['emit']is not None:A[a,t['emit']]+=1;used.add(t['emit'])
A=A.tocsr();Z=set(json.loads((p/'cap6_zero_weight_closure.json').read_text())['forced_zero_types']);proof=[]
def integerize(xs):
 f=[Fraction(float(x)).limit_denominator(1000000)for x in xs];d=lcm(*(x.denominator for x in f));v=[int(x*d)for x in f];g=reduce(gcd,v);return [x//g for x in v],d//g if d%g==0 else None
while True:
 U=sorted(used-Z);b=[(0,0)]*134
 for x in U:b[x]=(1,None)
 r=linprog(np.ones(134),A_ub=A,b_ub=np.zeros(len(ids)),bounds=b,method='highs');print('remaining',len(U),r.message)
 if r.success:
  w,scale=integerize(r.x);assert all(x>=0 for x in w)and all(w[x]>0 for x in U)
  delta=A@np.array(w,dtype=np.int64);assert max(delta)<=0
  out={'forced_zero_types':sorted(Z),'positive_types':U,'weights':w,'zero_drop_count':int(sum(delta==0)),'strict_drop_count':int(sum(delta<0)),'zero_drop_indices':[ids[i]for i,x in enumerate(delta)if x==0],'new_dual_witnesses':proof};(p/'cap6_resource_cone_closure.json').write_text(json.dumps(out,indent=2)+'\n');print('WEIGHTS',[(i,x)for i,x in enumerate(w)if x],'zero',out['zero_drop_count']);break
 AU=A[:,U].transpose().tocsr();summ=np.asarray(A[:,U].sum(axis=1)).reshape(-1)
 from scipy.sparse import vstack,csr_matrix
 Q=vstack([-AU,csr_matrix(-summ.reshape(1,-1))]);rhs=np.array([0]*len(U)+[-1]);rr=linprog(np.ones(len(ids)),A_ub=Q,b_ub=rhs,bounds=(0,None),method='highs');assert rr.success,rr.message
 v,_=integerize(rr.x);net=np.asarray(A.transpose()@np.array(v,dtype=np.int64)).reshape(-1).astype(int).tolist();assert all(net[i]>=0 for i in U)and sum(net[i]for i in U)>0
 new={i for i in U if net[i]>0};proof.append({'new_forced_zero_types':sorted(new),'net':net,'paths':[{'index':ids[i],'multiplicity':x}for i,x in enumerate(v)if x]});Z|=new;print('NEWZERO',new,'support',proof[-1]['paths'])
