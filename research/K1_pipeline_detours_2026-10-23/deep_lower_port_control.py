"""Exact short deep-port controls, not a global/front exclusion.
Root qR(S),qL(N),qR(N); negative contact indices are old one-use L3(N)
ports, positive indices are forbidden future ports. Other deep colors
arbitrary, with complete-white cap4 locally completable histories.
"""
from pathlib import Path
import json
D=((0,1),(1,0),(0,-1),(-1,0));root=(0,0)
reports=[]
for n in(8,12,16,20):
 nodes=[0];sol=[]
 def dfs(p,h,t,last,counts,first,trace):
  nodes[0]+=1
  nr=counts.get(root,0)
  if p==root and t:
   if nr==2:
    if t==n and h==0:sol.append(trace)
    return
   if nr!=1 or h!=0:return
  if t==n:return
  if abs(p[0])+abs(p[1])>n-t:return
  if p[0]+p[1]>0:return
  if p==root:opts=(1 if nr==0 else-1,)
  elif p[0]+p[1]==0:
   # Old ports have positive x; future ports negative x are unvisited/forbidden.
   if p[0]<=0 or h!=0 or counts.get(p,0):return
   opts=(-1,)
  elif p in last:
   if counts[p]>= (4 if first[p]==1 else 3):return
   opts=(-last[p],)
  else:opts=(1,-1)
  for c in opts:
   hh=(h+c)%4;dx,dy=D[hh];q=(p[0]+dx,p[1]+dy)
   ll=last.copy();ll[p]=c;cc=counts.copy();cc[p]=cc.get(p,0)+1;ff=first.copy();ff.setdefault(p,c)
   dfs(q,hh,t+1,ll,cc,ff,trace+[(list(p),h,'R'if c==1 else'L')])
 dfs(root,2,0,{}, {},{},[])
 reports.append(dict(span=n,nodes=nodes[0],count=len(sol),samples=[dict(word=''.join(z[2]for z in x),trace=x)for x in sol[:3]]))
 print(n,nodes[0],len(sol),flush=True)
 if sol:break
res=dict(status='EXACT bounded deep-port factor control, NOT an unbounded exclusion',scope=__doc__,reports=reports)
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(res,indent=2)+'\n')
