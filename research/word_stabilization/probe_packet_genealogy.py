"""Exploratory L-node ancestry graph using an existing forbidden-pose certificate.
The edge relation is an overapproximation, not a proof of every edge's realizability.
"""
import json,sys
from collections import defaultdict
from pathlib import Path
p,cert,out=sys.argv[1:4];Q=json.load(open(p+'_port_quotient.json'));M=Q['macro_words'];forbid={tuple(map(int,l.split()[:5])) for l in open(cert)}
D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 for _ in range(h%4):p=(p[1],-p[0])
 return p
def sub(p,q):return(p[0]-q[0],p[1]-q[1])
def trace(w):
 p=(0,0);h=0;reads=[];first={};last={};prod={};parent={};node=None
 for t,c in enumerate(w):
  assert last.get(p,(-1,None))[1]!=c
  if c=='L':
   node=t
   if p in prod:parent[t]=prod[p]
   prod.pop(p,None)
  else:assert node is not None;prod[p]=node
  first.setdefault(p,(t,c));last[p]=(t,c);reads.append((p,c,node));h=(h+(1 if c=='R'else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return reads,first,last,prod,parent
T=[trace(a['word']) for a in M];edges=defaultdict(list);nodes=[];outcounts={}
for a,(reads,first,last,prod,parent) in enumerate(T):
 for t,(q,c,n) in enumerate(reads):
  if c=='L':nodes.append((a,t));outcounts[a,t]=0
  else:outcounts[a,n]+=1
 for t,s in parent.items():edges[((a,s),(a,t))].append({'kind':'internal'})
for a,(_,_,last,prod,_) in enumerate(T):
 for q,s in prod.items():
  assert last[q][1]=='R'
  for b,(_,first,_,_,_) in enumerate(T):
   for z,(t,c) in first.items():
    if c!='L':continue
    for h in range(4):
     x,y=sub(q,rot(z,h))
     if (x+y-h)%2:continue
     if (a,b,x,y,h) not in forbid:edges[((a,s),(b,t))].append({'kind':'cross','source_cell':q,'target_pose':[x,y,h]})
A=defaultdict(list);R=defaultdict(list)
for s,t in edges:A[s].append(t);R[t].append(s)
seen=set();order=[]
def dfs(v):
 seen.add(v)
 for u in A[v]:
  if u not in seen:dfs(u)
 order.append(v)
for v in nodes:
 if v not in seen:dfs(v)
seen=set();scc=[]
for v in reversed(order):
 if v in seen:continue
 todo=[v];seen.add(v);S=[]
 while todo:
  u=todo.pop();S.append(u)
  for z in R[u]:
   if z not in seen:seen.add(z);todo.append(z)
 if len(S)>1 or v in A[v]:scc.append(sorted(S))
names=[a.get('name',str(i))for i,a in enumerate(M)]
J={'source':p,'certificate':cert,'nodes':len(nodes),'edges':len(edges),'cyclic_sccs':scc,'cyclic_nodes':[[[names[a],t,outcounts[a,t]]for a,t in s]for s in scc],'edge_details':[{'source':s,'target':t,'options':r}for(s,t),r in edges.items()]}
Path(out+'.json').write_text(json.dumps(J,indent=2));print({k:v for k,v in J.items()if k!='edge_details'})
