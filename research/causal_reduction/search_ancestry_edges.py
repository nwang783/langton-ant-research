import sys,contextlib,json
with contextlib.redirect_stdout(open('/dev/null','w')):from probe_macro_ancestry import trace,scc
from collections import defaultdict
front=[''];graph=defaultdict(set);examples={};best=0
for n in range(1,14):
 front=[w+c for w in front for c in 'CVB' if trace(w+c)]
 for w in front:
  o=trace(w)
  for child,par in enumerate(o['parent']):
   if par<0 or not o['nodes'][child]:continue
   a=o['nodeinfo'][par];b=o['nodeinfo'][child];u=a[1:];v=b[1:];graph[u].add(v);graph[v]|=set();examples.setdefault(str((u,v)),w)
 print(n,len(front),'maxdepth',max(trace(w)['maxdepth'] for w in front),flush=True)
cs=scc(graph)
print('SCC',[(sorted(c),[(u,v) for u in c for v in graph[u] if v in c]) for c in cs if len(c)>1 or next(iter(c)) in graph[next(iter(c))]])
print('Edges',[(u,v,examples[str((u,v))]) for u in graph for v in graph[u]])
open('/workspace/shared/langton/causal_reduction/ancestry_edge_discovery.json','w').write(json.dumps(dict(edges=[dict(source=u,target=v,example=examples[str((u,v))]) for u in graph for v in graph[u]],scc=[list(c) for c in cs]),indent=2))
