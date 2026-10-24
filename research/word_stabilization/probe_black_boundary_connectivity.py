from verify_macro_word import D
from dual_components import edge
from collections import defaultdict
import json

def components(edges):
 adj=defaultdict(set)
 for e in edges:
  a,b=e;adj[a].add(b);adj[b].add(a)
 comp={}
 for a in adj:
  if a in comp:continue
  todo=[a];root=a
  while todo:
   a=todo.pop()
   if a in comp:continue
   comp[a]=root;todo.extend(adj[a]-comp.keys())
 return comp
out={}
for k in D:
 first={};last={}
 for z in D[k]['trace']:
  p=tuple(z['p']);first.setdefault(p,z['c']);last[p]=z['c']
 read={frozenset(edge(p)) for p in first};before={frozenset(edge(p)) for p,c in first.items() if c=='L'};after={frozenset(edge(p)) for p,c in last.items() if c=='R'}
 deg=defaultdict(int)
 for a,b in read:deg[a]+=1;deg[b]+=1
 boundary={p for p,n in deg.items() if n<4}
 cb=components(before);ca=components(after)
 lost=[(a,b) for a in boundary for b in boundary if a<b and cb.get(a,a)==cb.get(b,b) and ca.get(a,a)!=ca.get(b,b)]
 lastR=[]
 for p,c in last.items():
  if c!='R':continue
  e=frozenset(edge(p));a,b=e;cc=components(after-{e});lastR.append((p,cc.get(a,a)==cc.get(b,b)))
 print(k,'boundary',len(boundary),'lost boundary pairs',len(lost),'cyclic last-R',sum(v for p,v in lastR),'/',len(lastR));print('lost',lost[:15]);print('noncyclic R',[p for p,v in lastR if not v])
 out[k]={'boundary':sorted(boundary),'lost_pairs':lost,'cyclic_lastR':lastR}
open('/workspace/shared/langton/word_stabilization/black_boundary_connectivity.json','w').write(json.dumps(out,indent=2))
