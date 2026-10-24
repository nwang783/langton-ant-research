"""Targeted q-port R(S),L(N),R(N) return control; arbitrary other colors.
No front or period search. Endpoint is the third q arrival, before reading R.
"""
from pathlib import Path
import json
D=((0,1),(1,0),(0,-1),(-1,0));root=(0,0)
reports=[]
for n in(8,12,16,20,24):
 nodes=[0];sol=[]
 def dfs(p,h,t,last,counts,trace):
  nodes[0]+=1
  nr=counts.get(root,0)
  if p==root and t:
   if nr==2:
    if t==n and h==0:sol.append(trace)
    return
   if nr!=1 or h!=0:return
  if t==n:return
  if abs(p[0])+abs(p[1])>n-t:return
  if p==root:
   c=1 if nr==0 else-1
   opts=(c,)
  elif p in last:opts=(-last[p],)
  else:opts=(1,-1)
  for c in opts:
   hh=(h+c)%4;dx,dy=D[hh];q=(p[0]+dx,p[1]+dy)
   ll=last.copy();ll[p]=c;cc=counts.copy();cc[p]=cc.get(p,0)+1
   dfs(q,hh,t+1,ll,cc,trace+[(list(p),h,'R'if c==1 else'L')])
 dfs(root,2,0,{}, {},[])
 reports.append(dict(span=n,nodes=nodes[0],count=len(sol),samples=[dict(word=''.join(z[2]for z in x),trace=x)for x in sol[:3]]))
 if sol:break
res=dict(status='EXACT finite lower-port joint return control',scope='q starts R incomingS, next read L incomingN, next arrival incomingN. All other cells arbitrary initial colors and exact alternating repeated reads. No deep-halfplane or whole-front sufficiency asserted.',reports=reports)
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
