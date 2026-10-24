"""Necessary all-count circulation for H/LR/Q, with fixed inherited literal reads.
Output bits are free. This is only incidence, not chronology.
"""
import json,collections
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
import certify_short_refinement_rup as core
P=Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
j=json.loads((P/'forward108_domino_repair.json').read_text())
def rep(p):return(p[0]%2,p[1]-2*(p[0]//2))
def run(nlo=-17,nhi=3):
 ps=[(x,x-a) for a in range(nlo,nhi+1) for x in (0,1)];ix={p:i for i,p in enumerate(ps)}
 keys=[(i,h,s) for i,p in enumerate(ps) for h in range(4) if (sum(p)+h)%2==1 for s in(1,-1)];ki={k:i for i,k in enumerate(keys)};n=len(keys);N=n+len(ps)
 lo=[0]*N
 for w,(x,y,h) in zip(j['words'],j['starts']):
  rr,_,_=core.trace(w,(x,y),h)
  for p,g,c in rr:lo[ki[(ix[rep(p)],g,1 if c=='R' else -1)]]+=1
 A=[];b=[]
 for i,p in enumerate(ps):
  row=[0]*N
  for v,(ii,h,s) in enumerate(keys):
   if ii==i:row[v]=s
  row[n+i]=-1;A.append(row);b.append(0)
  for h in range(4):
   if (sum(p)+h)%2!=1:continue
   vx,vy=D[h];prev=ix.get(rep((p[0]-vx,p[1]-vy)));row=[0]*N
   for v,(ii,g,s) in enumerate(keys):row[v]=int(ii==i and g==h)-int(ii==prev and(g+s)%4==h)
   A.append(row);b.append(0)
  for h in range(4):
   if (sum(p)+h)%2==1:continue
   vx,vy=D[h]
   if rep((p[0]+vx,p[1]+vy)) not in ix:
    A.append([int(ii==i and(g+s)%4==h)for ii,g,s in keys]+[0]*len(ps));b.append(0)
 for ax in range(2):A.append([D[(h+s)%4][ax]for i,h,s in keys]+[0]*len(ps));b.append(2)
 obj=np.array([1]*n+[0]*len(ps));bounds=[(v,None) for v in lo[:n]]+[(0,1)]*len(ps)
 out={}
 for sense in (1,-1):
  ans=linprog(sense*obj,A_eq=A,b_eq=b,bounds=bounds,method='highs');out[str(sense)]=dict(status=ans.message,period=(round(sum(ans.x[:n]),8) if ans.success else None))
  if ans.success:out[str(sense)]['extra']=[(ps[i],h,s,round(ans.x[v]-lo[v],6)) for v,(i,h,s) in enumerate(keys) if ans.x[v]-lo[v]>1e-7]
 print(out)
 (P/'pipeline_incidence_probe.json').write_text(json.dumps(dict(scope=__doc__,range=[nlo,nhi],results=out),indent=2)+'\n')
 return ps,keys,A,b,bounds,lo
if __name__=='__main__':run()
