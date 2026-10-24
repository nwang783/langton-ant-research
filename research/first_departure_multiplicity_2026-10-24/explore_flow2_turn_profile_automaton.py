"""Finite necessary-state automaton, not a search over word periods.
Combines signed global-M staircase windows with the local RR and LL corner covers.
"""
from itertools import product
from collections import Counter
from collections import defaultdict
R=set('XY');L=set('OUV');S='XYOUV'
stair={tuple(s.split())for s in ['U X O X V','U X O Y V','U X U X O','U X U X U','V Y O X V','V Y O Y V','V Y U X O','V Y U X U']}
def t(x):return'R'if x in R else'L'
def valid(w):
 for i in range(len(w)-2):
  if len({t(x)for x in w[i:i+3]})==1:return False
 for i in range(len(w)-3):
  v=w[i:i+4];tt=''.join(map(t,v))
  if tt=='LRRL'and(v[0]!='V'or v[3]!='V'):return False
  if tt=='RLLR':
   if not(v[0]=='Y'and v[2]=='V'and ((v[1]=='V'and v[3]=='Y')or(v[1]in'OU'and v[3]=='X'))):return False
 for i in range(len(w)-4):
  v=w[i:i+5]
  if ''.join(map(t,v))=='LRLRL'and tuple(v)not in stair:return False
 return True
G=defaultdict(dict)
for w in product(S,repeat=5):
 if valid(w):
  G[w[:4]][w[1:]]=1 if w[-1]in R else-1
  G[w[1:]]
stack=[];ix={};low={};on=set();scc=[]
def dfs(u):
 ix[u]=low[u]=len(ix);stack.append(u);on.add(u)
 for v in G[u]:
  if v not in ix:dfs(v);low[u]=min(low[u],low[v])
  elif v in on:low[u]=min(low[u],ix[v])
 if low[u]==ix[u]:
  cc=set()
  while True:
   v=stack.pop();on.remove(v);cc.add(v)
   if v==u:break
  if len(cc)>1 or u in G[u]:scc.append(cc)
for u in list(G):
 if u not in ix:dfs(u)
print('nodes',len(G),'edges',sum(map(len,G.values())),'cyclic SCC',[(len(c),sum(v in c for u in c for v in G[u]))for c in scc])
for c in scc:
 es=[(u,v,w)for u in c for v,w in G[u].items()if v in c]
 print('SCC symbols',set(x for w in c for x in w))
 for sign in[1,-1]:
  dd={u:0 for u in c};cycle=False
  for _ in c:
   ch=False
   for u,v,w in es:
    if dd[v]>dd[u]+sign*w:dd[v]=dd[u]+sign*w;ch=True
   if not ch:break
  else:cycle=True
  print('negative cycle for sign',sign,cycle)
 print('states', [''.join(w)for w in sorted(c)])
