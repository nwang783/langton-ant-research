#!/usr/bin/env python3
"""Finite conditional g8 single-used F-circle geometry, no exterior cap."""
from itertools import combinations
from collections import Counter
import json
D=((0,1),(1,0),(0,-1),(-1,0))
def geom(dirs):
 p=(0,0);points=[]
 for h in dirs:points.append(p);p=(p[0]+D[h][0],p[1]+D[h][1])
 assert p==(-3,-1)
 T=[3*y-x for x,y in points]
 if len(set(T))!=len(T):return None
 turns=[(h-dirs[j-1])%4 for j,h in enumerate(dirs)];assert all(x in(1,3)for x in turns)
 assert turns.count(1)==turns.count(3)==len(dirs)//2
 return points,T,turns
shapes={};raw=Counter()
for m in(3,5,7):
 for axis in(0,1):
  xs=[i for i in range(2*m)if i%2==axis];ys=[i for i in range(2*m)if i not in xs]
  for E in combinations(xs,(m-3)//2):
   for N in combinations(ys,(m-1)//2):
    E=set(E);N=set(N);dirs=tuple((1 if i in E else 3)if i in xs else(0 if i in N else 2)for i in range(2*m));raw[m]+=1
    z=geom(dirs)
    if z is None:continue
    key=min(dirs[i:]+dirs[:i]for i in range(2*m));shapes[key]=geom(key)
print('raw',dict(raw),'unique shapes',Counter(map(len,shapes)))
for dirs,(pts,T,turns)in shapes.items():
 lo=min(range(len(T)),key=lambda i:T[i]);hi=max(range(len(T)),key=lambda i:T[i]);assert turns[lo]==1 and dirs[lo]==3 and dirs[lo-1]==2,(dirs,T,turns,'MIN');assert turns[hi]==3 and dirs[hi]==2 and dirs[hi-1]==3,(dirs,T,turns,'MAX')
print('minimum R, maximum L on all shapes')
json.dump({'raw':dict(raw),'shapes':[{'directions':d,'points':p,'levels':t,'turns':r}for d,(p,t,r)in shapes.items()]},open('drift31_single_used_shapes_discovery.json','w'),indent=2)
