#!/usr/bin/env python3
"""Independent-coordinate author controls for first-cell monitor only.
Histories need not be port-balanced, so these are not claimed ant fronts.
The full prefix cell graph is rebuilt rather than updating producer state.
"""
from random import Random
from collections import defaultdict
from pathlib import Path
import json
from first_read_backbone_frontier import transition
from frontier_drift_geometry import Geometry
D=((0,1),(1,0),(0,-1),(-1,0));rng=Random(2061023)
def row(hs):
 return [dict(h=h,ins=[h.count(d)for d in range(4)],outs=[sum((x+(1 if j%2==0 else-1))%4==d for j,x in enumerate(h))for d in range(4)])for h in hs]
def physical(hs,a,z,S):
 nodes={(x,y)for y in range(z+1)for x in range(a)};f={};adj={v:[]for v in nodes}
 for v in nodes:
  x,y=v;h=hs[y][x][0];dx,dy=D[h];X=x-dx;Y=y-dy;u=(X%a,Y);seam=X//a
  if u not in nodes:continue
  H=hs[Y][X%a];j=next(j for j,t in enumerate(H)if(t+(1 if j%2==0 else-1))%4==h);w=1+4*j
  f[v]=(u,seam,w);adj[v].append(u);adj[u].append(v)
 seen=set();out=[];C=0
 for start in sorted(nodes):
  if start in seen:continue
  comp={start};stack=[start];seen.add(start)
  while stack:
   for v in adj[stack.pop()]:
    if v not in seen:seen.add(v);comp.add(v);stack.append(v)
  roots=[v for v in comp if v not in f];front=sorted(v for v in comp if v[1]==z)
  if roots:
   assert len(roots)==1;rt=roots[0];assert rt in front
   entries=[]
   for v in front:
    u=v;cost=wind=0
    while u!=rt:u,k,w=f[u];cost+=w;wind+=k
    entries.append((v[0],(-wind)%3,min(S,cost)))
   out.append((rt[0],tuple(entries)))
  else:
   u=start;path=[];index={}
   while u not in index:index[u]=len(path);path.append(u);u=f[u][0]
   cyc=path[index[u]:];wind=sum(f[v][1]for v in cyc);debt=sum(f[v][2]for v in cyc)
   if wind!=-1:return None,0
   C=max(C,min(S,debt))
   if front:out.append((-1,tuple((v[0],0,0)for v in front)))
 return tuple(sorted(out,key=lambda c:c[1][0][0])),C
checks=accepted=reject=cyclic_fronts=0
for trial in range(5000):
 a=rng.choice((2,4,6));H=rng.randrange(2,9);S=rng.choice((4,12,24,64,120));hs=[]
 for y in range(H):
  rr=[]
  for x in range(a):
   axis=1-(x+y)%2
   h=rng.choice((axis,axis+2)) if axis else(2 if y==0 else 0 if y==H-1 else rng.choice((0,2)))
   rr.append((h,)*rng.choice((2,4)))
  hs.append(rr)
 state=();C=0;old=row([()]*a);g=Geometry(a,0)
 for z in range(H):
  new=row(hs[z]);ns,badC,bad=transition(state,old,new,(z-1)%2,g,S);ref,RC=physical(hs,a,z,S);checks+=1
  assert (bad is None)==(ref is not None),(trial,a,H,S,z,bad)
  if bad:reject+=1;break
  accepted+=1;C=max(C,badC);assert C==RC,(trial,z,C,RC)
  # Potentials in already cyclic components are irrelevant spanning-tree choices.
  normalized=tuple((rt,tuple((c,0,0)if rt<0 else(c,w,d)for c,w,d in es))for rt,es in ns)
  assert normalized==ref,(trial,z,normalized,ref)
  cyclic_fronts+=any(rt<0 for rt,es in ns);state=ns;old=new
result=dict(scope=__doc__,random_complete_cell_graphs=5000,prefixes=checks,accepted_prefixes=accepted,rejected_prefixes=reject,cyclic_components_retained_on_frontier=cyclic_fronts,status='AUTHOR_FRESH_COORDINATE_CELL_MONITOR_COMPARISON_PASS')
Path(__file__).with_name('first_read_backbone_random_graphs.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
