"""Integer-flow discovery control, not a chronological front certificate."""
import numpy as np,json
from pathlib import Path
from scipy.optimize import milp,Bounds,LinearConstraint
import probe_pipeline_incidence as base
ps,ks,A,b,bd,lo=base.run();n=len(ks);N=len(lo)
r=milp(np.array([1]*n+[0]*(N-n),dtype=float),integrality=np.ones(N),bounds=Bounds([z[0] for z in bd],[np.inf if z[1] is None else z[1] for z in bd]),constraints=LinearConstraint(np.array(A),np.array(b),np.array(b)),options={'time_limit':30.0,'mip_rel_gap':0.0})
out=dict(scope=__doc__,status=r.message,objective=None if r.fun is None else float(r.fun))
if r.x is not None:
 v=[round(x) for x in r.x];assert max(abs(x-y) for x,y in zip(v,r.x))<1e-6
 assert all(sum(a*x for a,x in zip(row,v))==bb for row,bb in zip(A,b))
 out['positive_extra']=[dict(position=ps[i],heading=h,turn='R'if s==1 else'L',count=v[z]-lo[z])for z,(i,h,s)in enumerate(ks)if v[z]>lo[z]]
 out['flows']=[dict(position=ps[i],heading=h,turn='R'if s==1 else'L',count=v[z],base=lo[z])for z,(i,h,s)in enumerate(ks)if v[z]]
 out['output_black']=[ps[i]for i,x in enumerate(v[n:])if x]
Path('pipeline_integer_flow.json').write_text(json.dumps(out,indent=2)+'\n');print('INTEGER',out)
