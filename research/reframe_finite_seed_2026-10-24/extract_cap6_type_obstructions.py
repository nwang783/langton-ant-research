import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
from fractions import Fraction
from math import lcm,gcd
from functools import reduce
p=Path(__file__).parent;R=json.loads((p/'kernel_M6_scc.json').read_text())['first_return_cycles'];k=134;A=lil_matrix((len(R),k))
for i,r in enumerate(R):
 for t in r['transitions']:
  if t['consume']is not None:A[i,t['consume']]-=1
  if t['emit']is not None:A[i,t['emit']]+=1
for typ in[1,2]:
 b=[0]*k;b[typ]=-1
 dual=linprog(np.ones(len(R)),A_ub=-A.transpose().tocsr(),b_ub=b,bounds=(0,None),method='highs');print(typ,dual.message)
 if not dual.success:continue
 f=[Fraction(float(x)).limit_denominator(1000000)for x in dual.x];d=lcm(*(x.denominator for x in f));w=[int(x*d)for x in f];g=reduce(gcd,w);w=[x//g for x in w];net=[0]*k
 for v,q in zip(w,R):
  if v:
   for t in q['transitions']:
    if t['consume']is not None:net[t['consume']]-=v
    if t['emit']is not None:net[t['emit']]+=v
 assert net[typ]>0 and all(x>=0 for x in net)
 out={'target_type':typ,'status':'EXACT_RESOURCE_RELAXATION_OBSTRUCTION_NOT_PHYSICAL_COMPILER','net_emission_minus_consumption':net,'cycles':[{'index':i,'multiplicity':x,**q}for i,(x,q)in enumerate(zip(w,R))if x]};(p/f'cap6_type{typ}_obstruction.json').write_text(json.dumps(out,indent=2)+'\n');print('support',[(i,x,R[i]['word'])for i,x in enumerate(w)if x],'net',[(i,x)for i,x in enumerate(net)if x])
