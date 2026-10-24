#!/usr/bin/env python3
"""Independent direct validation of the open-patch state/time certificate."""
import json,re,sys
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
r=int(sys.argv[1]);base=Path(__file__).with_name('one_a_local_r'+str(r));model=base.with_suffix('.model').read_text();val={}
for line in model.splitlines():
 k,v=line.split(' -> ');val[k]= -int(v[3:-1]) if v.startswith('(- ') else int(v)
ps=[(x,y) for x in range(-r,r+1) for y in range(-r,r+2)];ev={};hist={};labels={};edgeout={};edgein={}
for i,p in enumerate(ps):
 k=val['s'+str(i)];axis=1 if sum(p)%2==0 else 0
 if k==0: hist[p]=[];labels[p]='..';continue
 h=(axis+(0 if k<=5 else 2))%4;typ=(k-1)%5
 hs=[[h],[h,h],[h,(h+2)%4],[h,h,(h+2)%4],[h,(h+2)%4,(h+2)%4]][typ]
 labels[p]='RDSAB'[typ]+'NESW'[h];ts=[val[f't{i}_{j}'] for j in range(len(hs))];assert all(a<b for a,b in zip(ts,ts[1:]));hist[p]=list(zip(ts,hs))
 for j,(t,h) in enumerate(hist[p]):
  assert t not in ev;ev[t]=(p,j)
  c=1 if j%2==0 else -1;o=(h+c)%4;dx,dy=D[o];q=p[0]+dx,p[1]+dy;edgeout.setdefault((p,q),[]).append(t)
  dx,dy=D[h];z=p[0]-dx,p[1]-dy;edgein.setdefault((z,p),[]).append(t)
pset=set(ps);checked=0
for e in set(edgeout)|set(edgein):
 if e[0] not in pset or e[1] not in pset:continue
 assert [t+1 for t in edgeout.get(e,[])]==edgein.get(e,[]),(e,edgeout.get(e),edgein.get(e));checked+=1
assert labels[0,0]=='SW' and labels[0,1]=='AN' and labels[-1,1]=='DW'
print('VALID local patch only',r,len(ev),'events',checked,'internal directed edges')
for y in range(r+1,-r-1,-1):print(y,' '.join(labels[x,y] for x in range(-r,r+1)))
print('central',json.dumps({str(p):hist[p] for p in [(0,0),(0,1),(-1,1),(-1,0)]}))
