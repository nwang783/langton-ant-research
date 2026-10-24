import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
from fractions import Fraction
from math import lcm,gcd
from functools import reduce
p=Path(__file__).parent;K=json.loads((p/'component_kernel_M6.json').read_text())['transitions'];C=json.loads((p/'kernel_M6_compact_returns.json').read_text())['returns'];F=json.loads((p/'cap6_physical_return_filter.json').read_text());ids=F['feasible_indices'];R=[C[i]for i in ids];k=134;A=lil_matrix((len(R),k))
for i,r in enumerate(R):
 for z in r['indices']:
  t=K[z]
  if t['consume']is not None:A[i,t['consume']]-=1
  if t['emit']is not None:A[i,t['emit']]+=1
out=[]
for typ in[0,1,2]:
 b=[0]*k;b[typ]=-1
 dual=linprog(np.ones(len(R)),A_ub=-A.transpose().tocsr(),b_ub=b,bounds=(0,None),method='highs');print(typ,dual.message)
 if not dual.success:continue
 f=[Fraction(float(x)).limit_denominator(1000000)for x in dual.x];d=lcm(*(x.denominator for x in f));w=[int(x*d)for x in f];g=reduce(gcd,w);w=[x//g for x in w];net=[0]*k;cs=[]
 for i,(v,q)in enumerate(zip(w,R)):
  if v:
   for z in q['indices']:
    t=K[z]
    if t['consume']is not None:net[t['consume']]-=v
    if t['emit']is not None:net[t['emit']]+=v
   cs.append({'index':ids[i],'multiplicity':v,'word':q['word'],'indices':q['indices'],'minimal_seed':F['minimal_finite_seeds'][str(ids[i])],'transitions':[K[z]for z in q['indices']]})
 assert net[typ]>0 and all(x>=0 for x in net)
 out.append({'target_type':typ,'net_emission_minus_consumption':net,'cycles':cs});print('support',[(x['index'],x['multiplicity'],x['word'])for x in cs],'net',[(i,x)for i,x in enumerate(net)if x])
(p/'physical_cap6_resource_obstructions.json').write_text(json.dumps({'status':'EXACT_INDIVIDUALLY_PHYSICAL_RESOURCE_RELAXATION_NOT_JOINT_COMPOSABILITY','obstructions':out},indent=2)+'\n')
