#!/usr/bin/env python3
"""Exact local open-strip clock graph at a fixed literal history assignment."""
from itertools import product
import json,time
D=[(0,1),(1,0),(0,-1),(-1,0)]
def build(n,p,q):
 k=len(p);a=2*k;H={}
 for i in range(k):
  H[2*i,0]=[3];H[2*i+1,0]=[2]
  H[2*i,1]=[0 if j==p[i] else 2 for j in range(n)]
  H[2*i+1,1]=[(1 if j%2 else 3) if j!=q[i] else (3 if j%2 else 1) for j in range(n)]
 inc={};out={};events=[];edges=[]
 for (x,y),hs in H.items():
  for j,h in enumerate(hs):
   e=(x,y,j);events.append(e);inc.setdefault((x,y,h),[]).append(e)
   g=(h+(1 if j%2==0 else -1))%4;out.setdefault((x,y,g),[]).append(e)
   if j:edges.append((e,(x,y,j-1),-1,0,'order'))
 for (x,y,g),es in out.items():
  dx,dy=D[g];xx=x+dx;yy=y+dy;v=-(xx//a);xx%=a
  if yy==2:continue
  ts=inc.get((xx,yy,g),[]);assert len(es)==len(ts)
  for s,t in zip(es,ts):edges.append((s,t,1,-v,'edge'));edges.append((t,s,-1,v,'edge'))
 index={e:i for i,e in enumerate(events)}
 return events,[(index[s],index[t],c,v,label) for s,t,c,v,label in edges]
def check(n,p,q,cycle=False):
 E,G=build(n,p,q);N=len(E);P=4*N;dist=[0]*N;pred=[None]*N
 for j in range(N):
  changed=-1
  for ix,(s,t,c,v,l) in enumerate(G):
   x=dist[s]+c+v*P
   if x<dist[t]:dist[t]=x;pred[t]=ix;changed=t
  if changed<0:return True,None
 if not cycle:return False,None
 cur=changed
 for _ in range(N):cur=G[pred[cur]][0]
 start=cur;cs=[]
 while True:
  ix=pred[cur];s,t,c,v,l=G[ix];cs.append((E[s],E[t],c,v,l));cur=s
  if cur==start:break
 return False,cs
if __name__=='__main__':
 t=time.time()
 for n in range(2,19,2):
  count=0;ok=[]
  for p0,p1,q0,q1 in product(range(1,n,2),repeat=4):
   count+=1;yes,_=check(n,[p0,p1],[q0,q1])
   if yes:ok.append((p0,p1,q0,q1))
  print(json.dumps(dict(n=n,cases=count,feasible=len(ok),examples=ok[:8],seconds=time.time()-t)),flush=True)
