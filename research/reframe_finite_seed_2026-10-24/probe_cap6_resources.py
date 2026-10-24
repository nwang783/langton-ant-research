import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
p=Path(__file__).parent
j=json.loads((p/'kernel_M6_scc.json').read_text());R=j['first_return_cycles'];k=134;A=lil_matrix((len(R),k));sizes={}
for i,r in enumerate(R):
 for t in r['transitions']:
  if t['consume']is not None:A[i,t['consume']]-=1;sizes[t['consume']]=len(t['imported_component'])
  if t['emit']is not None:A[i,t['emit']]+=1;sizes[t['emit']]=len(t['emitted_component'])
bounds=[(0,None)]*k;bounds[0]=(1,1)
r=linprog(np.ones(k),A_ub=A.tocsr(),b_ub=np.zeros(len(R)),bounds=bounds,method='highs');print(r.message)
if r.success:
 from fractions import Fraction
 from math import lcm
 f=[Fraction(float(x)).limit_denominator(1000000)for x in r.x];d=lcm(*(x.denominator for x in f));w=[int(x*d)for x in f];delta=[]
 for q in R:
  v=sum(w[t['emit']]for t in q['transitions']if t['emit']is not None)-sum(w[t['consume']]for t in q['transitions']if t['consume']is not None);assert v<=0;delta.append(v)
 out={'weights':w,'scale':d,'component_sizes':sizes,'zero_drop_count':delta.count(0),'strict_drop_count':sum(x<0 for x in delta),'zero_drop_indices':[i for i,x in enumerate(delta)if x==0]};(p/'cap6_resource_probe.json').write_text(json.dumps(out,indent=2)+'\n');print('weights',[(i,x)for i,x in enumerate(w)if x],'zero',out['zero_drop_count'],'strict',out['strict_drop_count'])
else:
 from fractions import Fraction
 from math import lcm,gcd
 from functools import reduce
 b=[0]*k;b[0]=-1
 dual=linprog(np.ones(len(R)),A_ub=-A.transpose().tocsr(),b_ub=b,bounds=(0,None),method='highs');print('dual',dual.message)
 if dual.success:
  f=[Fraction(float(x)).limit_denominator(1000000)for x in dual.x];d=lcm(*(x.denominator for x in f));w=[int(x*d)for x in f];g=reduce(gcd,w);w=[x//g for x in w];net=[0]*k
  for v,q in zip(w,R):
   if not v:continue
   for t in q['transitions']:
    if t['consume']is not None:net[t['consume']]-=v
    if t['emit']is not None:net[t['emit']]+=v
  assert net[0]>0 and all(x>=0 for x in net)
  out={'status':'EXACT_RESOURCE_RELAXATION_OBSTRUCTION_NOT_PHYSICAL_COMPILER','net_emission_minus_consumption':net,'cycles':[{'index':i,'multiplicity':x,**q}for i,(x,q)in enumerate(zip(w,R))if x]};(p/'cap6_resource_obstruction.json').write_text(json.dumps(out,indent=2)+'\n');print('support',[(i,x,R[i]['word'])for i,x in enumerate(w)if x],'net',[(i,x)for i,x in enumerate(net)if x])
