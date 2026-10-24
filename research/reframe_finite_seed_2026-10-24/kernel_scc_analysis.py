"""Exact integer graph certificates and explicit first-return kernel paths.
These are local-kernel paths, NOT chronological full-board trajectories.
"""
import json,sys
from pathlib import Path
from collections import deque
OUT=Path(__file__).parent
sys.setrecursionlimit(50000)

def analyze(M):
 j=json.loads((OUT/f'component_kernel_M{M}.json').read_text());T=j['transitions'];n=j['summary']['active_states'];adj=[[]for _ in range(n)]
 for z,t in enumerate(T):adj[t['source']].append(z)
 # Kahn topological certificate after deleting empty state 0.
 indeg=[0]*n
 for t in T:
  if t['source']!=0 and t['target']!=0:indeg[t['target']]+=1
 q=deque(i for i in range(1,n)if not indeg[i]);order=[]
 while q:
  u=q.popleft();order.append(u)
  for z in adj[u]:
   v=T[z]['target']
   if v!=0:
    indeg[v]-=1
    if not indeg[v]:q.append(v)
 assert len(order)==n-1,(M,n,len(order))
 pos={u:i for i,u in enumerate(order)}
 assert all(pos[t['source']]<pos[t['target']]for t in T if t['source'] and t['target'])
 # Reachability from and to 0 identifies the unique possible cyclic SCC.
 def reach(edges):
  seen={0};todo=[0]
  while todo:
   for v in edges[todo.pop()]:
    if v not in seen:seen.add(v);todo.append(v)
  return seen
 fw=[[]for _ in range(n)];bw=[[]for _ in range(n)]
 for t in T:fw[t['source']].append(t['target']);bw[t['target']].append(t['source'])
 scc=sorted(reach(fw)&reach(bw));ss=set(scc)
 cyc=[z for z,t in enumerate(T)if t['source']in ss and t['target']in ss]
 # Number and all first-return paths through DAG; zero means no selfloop.
 counts=[0]*n
 for u in reversed(order):counts[u]=sum(1 if T[z]['target']==0 else counts[T[z]['target']]for z in adj[u])
 total=sum(1 if T[z]['target']==0 else counts[T[z]['target']]for z in adj[0])
 assert total<1000000,total
 paths=[]
 def dfs(u,path):
  for z in adj[u]:
   v=T[z]['target']
   if v==0:paths.append(path+[z])
   elif counts[v]:dfs(v,path+[z])
 dfs(0,[]);assert len(paths)==total
 paths.sort(key=lambda p:(len(p),p))
 records=[]
 for path in paths:
  ts=[T[z]for z in path];word=''.join(t['turn']for t in ts)
  p=(0,0);h=0
  for c in word:
   h=(h+(1 if c=='R'else-1))%4;d=((0,1),(1,0),(0,-1),(-1,0))[h];p=p[0]+d[0],p[1]+d[1]
  records.append({'indices':path,'word':word,'length':len(path),'displacement':p,'heading':h,'imports':sum(t['consume']is not None for t in ts),'emissions':sum(t['emit']is not None for t in ts),'transitions':ts})
 out={'active_cap':M,'vertices':n,'edges':len(T),'nonempty_topological_order':order,'recurrent_scc':scc,'recurrent_edge_indices':cyc,'first_return_count':total,'first_return_cycles':records,'scope':'Exact local-kernel graph only. Cycles require full chronological spatial compatibility before being physical.'}
 (OUT/f'kernel_M{M}_scc.json').write_text(json.dumps(out,indent=2)+'\n')
 print(M,'scc',len(scc),'cyclic_edges',len(cyc),'first_returns',total,'lengths',sorted(set(len(p)for p in paths)),'import_cycles',sum(r['imports']>0 for r in records),'heading0',sum(r['heading']==0 for r in records))
 if M==5:
  for i,r in enumerate(records):
   if r['imports']:
    (OUT/'kernel_M5_first_import_cycle.json').write_text(json.dumps({'cycle_index':i,**r},indent=2)+'\n');print('FIRST_IMPORT',i,r['word'],r['indices']);break
 return out
if __name__=='__main__':
 for M in [4,5]:analyze(M)
