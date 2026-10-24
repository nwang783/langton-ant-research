#!/usr/bin/env python3
from boundary_probe import *
from collections import defaultdict

def dual(e):
 (x,y),(X,Y)=e
 return ((x,y-1),(x,y)) if x!=X else ((x-1,y),(x,y))
def black_cursor(dart):
 (x,y),d=dart
 return ((x,y-1),(x,y),(x-1,y),(x-1,y-1))[d]
def active(B,dart):
 adj=defaultdict(set)
 for e in B:
  a,b=dual(e);adj[a].add(b);adj[b].add(a)
 v=black_cursor(dart);q=[v];seen={v};i=0;E=0
 while i<len(q):
  v=q[i];i+=1;E+=len(adj[v])
  for w in adj[v]:
   if w not in seen:seen.add(w);q.append(w)
 return dict(vertices=len(q),edges=E//2,cycle_rank=E//2-len(q)+1)
if __name__=='__main__':
 B=set();dart=((0,0),0);best=-1;out=[]
 for t in range(20001):
  if t%10==0:
   C=active(B,dart)
   if C['cycle_rank']>best:out.append(dict(t=t,**C));best=C['cycle_rank']
  E=edge(*dart);nxt=perm(dart,B)
  if E in B:B.remove(E)
  else:B.add(E)
  dart=nxt
 print(json.dumps(out,indent=2))
