import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
from fractions import Fraction
from math import lcm
p=Path(__file__).parent;R=json.loads((p/'kernel_M6_scc.json').read_text())['first_return_cycles']; allowed=set(json.loads((p/'cap6_profile_budget_filter.json').read_text())['surviving_indices']); R=[r for i,r in enumerate(R)if i in allowed]; print('survivors',len(R)); k=134;A=lil_matrix((len(R),k))
for i,r in enumerate(R):
 for t in r['transitions']:
  if t['consume']is not None:A[i,t['consume']]-=1
  if t['emit']is not None:A[i,t['emit']]+=1
A=A.tocsr();out={}
for typ in [0,1,2]:
 b=[(0,None)]*k;b[typ]=(1,1)
 r=linprog(np.ones(k),A_ub=A,b_ub=np.zeros(len(R)),bounds=b,method='highs');print(typ,r.message)
 if r.success:
  f=[Fraction(float(x)).limit_denominator(1000000)for x in r.x];d=lcm(*(x.denominator for x in f));w=[int(x*d)for x in f];delta=[]
  for q in R:
   v=sum(w[t['emit']]for t in q['transitions']if t['emit']is not None)-sum(w[t['consume']]for t in q['transitions']if t['consume']is not None);assert v<=0;delta.append(v)
  out[typ]={'weights':w,'scale':d,'zero_drop_count':delta.count(0),'strict_drop_count':sum(x<0 for x in delta),'zero_drop_indices':[i for i,x in enumerate(delta)if x==0]};print('nonzero',[(i,x)for i,x in enumerate(w)if x],'zero',out[typ]['zero_drop_count'])
 else:out[typ]={'status':'LP_INFEASIBLE_NO_EXACT_DUAL_YET'}
(p/'cap6_profile_budget_fuel_probe.json').write_text(json.dumps(out,indent=2)+'\n')
