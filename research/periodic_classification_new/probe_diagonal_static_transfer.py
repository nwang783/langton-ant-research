#!/usr/bin/env python3
from itertools import product
from collections import deque
import json
D=((0,1),(1,0),(0,-1),(-1,0))
def sts(par):
 a=1-par
 return [()]+[h for n in range(1,5) for h in product((a,a+2),repeat=n)]
def counts(h):
 ins=[h.count(d) for d in range(4)];outs=[sum((a+(1 if j%2==0 else -1))%4==d for j,a in enumerate(h)) for d in range(4)]
 return ins,outs
ss=[sts(0),sts(1)];cs=[[counts(h) for h in hs] for hs in ss];adj={}
for p in range(2):
 for i,(ai,ao) in enumerate(cs[p]):
  ns=[]
  for j,(bi,bo) in enumerate(cs[1-p]):
   if p==0:ok=ao[0]==bi[0] and bo[1]==ai[1]
   else:ok=ao[3]==bi[3] and bo[2]==ai[2]
   if ok:ns.append((1-p,j))
  adj[p,i]=ns
start=(0,0,0);q=deque([start]);prev={start:None};end=None
while q:
 p,i,w=q.popleft()
 if i==0 and w==1:end=p,i,w;break
 for a,b in adj[p,i]:
  ww=w+(cs[a][b][1][1]-cs[a][b][1][3] if a else 0)
  k=a,b,ww
  if abs(ww)<=10 and k not in prev:prev[k]=(p,i,w);q.append(k)
path=[]
while end is not None:path.append(end);end=prev[end]
path=path[::-1]
print(json.dumps(dict(states=62,edges=sum(map(len,adj.values())),found=bool(path),path=[dict(parity=p,state=i,voltage=w,headings=ss[p][i]) for p,i,w in path]),indent=2))
