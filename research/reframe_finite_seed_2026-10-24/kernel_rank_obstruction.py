"""Extract exact resource-relaxed obstruction; never a physical counterexample."""
import json,sys
from pathlib import Path
from fractions import Fraction
from math import lcm,gcd
from functools import reduce
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
OUT=Path(__file__).parent
M=int(sys.argv[1])if len(sys.argv)>1 else 4
j=json.loads((OUT/f'component_kernel_M{M}.json').read_text());T=j['transitions'];n=j['summary']['active_states'];k=j['summary']['passive_types'];e=len(T)
A=lil_matrix((n+1,e));R=lil_matrix((k,e))
for z,t in enumerate(T):
 A[t['source'],z]+=1;A[t['target'],z]-=1;A[n,z]=1
 if t['consume']is not None:R[t['consume'],z]+=1
 if t['emit']is not None:R[t['emit'],z]-=1
r=linprog(np.zeros(e),A_ub=R.tocsr(),b_ub=np.zeros(k),A_eq=A.tocsr(),b_eq=np.array([0]*n+[1]),bounds=(0,None),method='highs')
assert r.success,r.message
f=[Fraction(float(x)).limit_denominator(1000000)for x in r.x];d=lcm(*(x.denominator for x in f));v=[int(x*d)for x in f];g=reduce(gcd,v);v=[x//g for x in v]
flow=[0]*n;fuel=[0]*k
for x,t in zip(v,T):
 flow[t['source']]+=x;flow[t['target']]-=x
 if t['consume']is not None:fuel[t['consume']]-=x
 if t['emit']is not None:fuel[t['emit']]+=x
assert not any(flow)and all(x>=0 for x in fuel)and sum(v)>0
out={'status':'EXACT_RESOURCE_RELAXATION_OBSTRUCTION','active_cap':M,'total_multiplicity':sum(v),'active_flow_balance':flow,'net_passive_emission_minus_consumption':fuel,'used_transitions':[{'multiplicity':x,'index':i,**t}for i,(x,t)in enumerate(zip(v,T))if x], 'scope':'Rules out this nonnegative additive component-weight ranking. Does not supply a chronological spatially composable cycle or actual ant trajectory.'}
(OUT/f'kernel_M{M}_rank_obstruction.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'count':len(out['used_transitions']),'mass':sum(v),'fuel':fuel,'turns':[t['turn']for t in out['used_transitions']]},indent=2))
