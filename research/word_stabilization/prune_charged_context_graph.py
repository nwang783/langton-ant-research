import json,sys
from collections import defaultdict
from pathlib import Path
p=sys.argv[1];q=json.load(open(p+'_port_quotient.json'));g=json.load(open(p+'_grammar.json'));M=q['macro_words'];charged=set()
for l in open(p+'_patch2_kernel.fresh.tsv'):
 a,x,y,t=map(int,l.split())
 if t<len(M[a]['word']):charged.add(a)
V=set(range(len(M)))-charged;E=[(a,b)for a,b in g['pairs']if a in V and b in V];A=defaultdict(list);R=defaultdict(list)
for a,b in E:A[a].append(b);R[b].append(a)
seen=set();order=[]
def dfs(a):
 seen.add(a)
 for b in A[a]:
  if b not in seen:dfs(b)
 order.append(a)
for a in V:
 if a not in seen:dfs(a)
seen=set();S=[]
for a in reversed(order):
 if a in seen:continue
 todo=[a];seen.add(a);part=[]
 while todo:
  u=todo.pop();part.append(u)
  for v in R[u]:
   if v not in seen:seen.add(v);todo.append(v)
 if len(part)>1 or a in A[a]:S.append(sorted(part))
print(p,'charged',len(charged),'cyclic',S)
for s in S:
 print('CONTEXTS',[(a,M[a]['context'])for a in s]);print('edges',[(a,b)for a,b in E if a in s and b in s])
Path(p+'_patch2_pruned_graph.json').write_text(json.dumps({'charged':sorted(charged),'recurrent_components':S,'remaining_edges':E},indent=2))
