import sys,json
from collections import defaultdict,deque
from verify_macro_word import D,check,rot
from dual_components import edge

def core(B):
 adj=defaultdict(set)
 for p in B:
  a,b=edge(p);adj[a].add(b);adj[b].add(a)
 todo=deque(v for v in adj if len(adj[v])<2)
 while todo:
  a=todo.popleft()
  for b in list(adj[a]):
   adj[b].remove(a)
   if len(adj[b])==1:todo.append(b)
  adj[a].clear()
 return {p for p in B if edge(p)[1]in adj[edge(p)[0]]}

def bridges(B):
 adj=defaultdict(list)
 for p in B:
  a,b=edge(p);adj[a].append((b,p));adj[b].append((a,p))
 tin={};low={};ans=set();i=0
 def dfs(v,ep=None):
  nonlocal i
  i+=1;tin[v]=low[v]=i
  for w,p in adj[v]:
   if p==ep:continue
   if w in tin:low[v]=min(low[v],tin[w])
   else:
    dfs(w,p);low[v]=min(low[v],low[w])
    if low[w]>tin[v]:ans.add(p)
 for v in list(adj):
  if v not in tin:dfs(v)
 return ans
if __name__=='__main__':
 for w in sys.argv[1:]:
  r=check(w);B=set(map(tuple,r['seed']));c=core(B);br=bridges(B);j=0
  print(w,'initial','B',len(B),'core',len(c),'bridges',len(br))
  for i,k in enumerate(w):
   oldB=B.copy();oc=c;ob=br
   block=r['blocks'][i];px,py,h=block['pose'];tx,ty=rot(D[k]['trace'][-1]['p'],h);exitq=(px+tx,py+ty)
   for t,x,y,*rest in r['trace'][j:j+len(D[k]['word'])]:B.symmetric_difference_update([(x,y)])
   j+=len(D[k]['word']);c=core(B);br=bridges(B)
   print(i,k,'core',len(c),'lostcore',len(oc-c),'newcore',len(c-oc),'bridges',len(br),'newbridges',len(br-ob),'exitoldcore',exitq in oc,'exitoldbridge',exitq in ob,'exitnewcore',exitq in c)
