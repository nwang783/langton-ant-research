"""Exact per-heading/turn incidence bounds for the fixed prepared wake cylinder."""
from bound_wake_return_flow import model,P,F,linprog,np
import json
ps,keys,A,b,names=model(13,-4);n=len(keys);N=n+len(ps);bounds=[(0,None)]*n+[(0,1)]*len(ps);rows=[]
for target,key in enumerate(keys):
 objective=[int(j==target)for j in range(N)]
 lp=linprog(-np.array(objective),A_eq=A,b_eq=b,bounds=bounds,method='highs');assert lp.success
 y=[-F(float(v)).limit_denominator(1000000)for v in lp.eqlin.marginals];z=[-F(float(v)).limit_denominator(1000000)for v in lp.upper.marginals]
 assert all(v>=0 for v in z)and all(z[j]==0 for j in range(n))
 assert all(sum(y[i]*A[i][j]for i in range(len(A)))+z[j]>=objective[j]for j in range(N))
 upper=sum(yy*bb for yy,bb in zip(y,b))+sum(z[n:])
 rows.append(dict(key=key,upper=str(upper),integer_upper=upper.numerator//upper.denominator,dual_equalities=list(map(str,y)),dual_upper=list(map(str,z[n:]))))
out=dict(scope=__doc__,positions=ps,equality_names=names,bounds=rows)
(P/'wake_return_individual_count_bounds.json').write_text(json.dumps(out,indent=2)+'\n');print('Exact bounds',len(rows),'positive',sum(x['integer_upper']>0 for x in rows))
