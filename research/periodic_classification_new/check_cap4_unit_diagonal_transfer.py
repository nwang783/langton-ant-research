#!/usr/bin/env python3
"""Finite certificate, no width or path-voltage bound."""
from itertools import product
from collections import deque
from pathlib import Path
import json

def histories(parity):
 a=1-parity
 return [()]+[h for m in range(1,5) for h in product((a,a+2),repeat=m)]
def record(p,i,h):
 ins=[sum(x==d for x in h) for d in range(4)]
 outs=[sum((x+(1 if j%2==0 else -1))%4==d for j,x in enumerate(h)) for d in range(4)]
 return dict(parity=p,index=i,headings=list(h),incoming=ins,outgoing=outs,voltage=outs[1]-outs[3] if p else 0)
def run():
 states={(p,i):record(p,i,h) for p in (0,1) for i,h in enumerate(histories(p))};adj={u:[] for u in states}
 for (p,i),a in states.items():
  for (q,j),b in states.items():
   if p==q:continue
   if p==0:ok=a['outgoing'][0]==b['incoming'][0] and a['incoming'][1]==b['outgoing'][1]
   else:ok=a['outgoing'][3]==b['incoming'][3] and a['incoming'][2]==b['outgoing'][2]
   if ok:adj[p,i].append((q,j))
 potential={(0,0):0,(1,0):0};q=deque(potential)
 while q:
  u=q.popleft()
  for v in adj[u]:
   x=(potential[u]+states[v]['voltage'])%2
   if v in potential:assert potential[v]==x,(u,v,potential[u],potential[v])
   else:potential[v]=x;q.append(v)
 assert potential[0,0]==potential[1,0]==0
 for u in potential:
  for v in adj[u]:assert v in potential and (potential[v]-potential[u]-states[v]['voltage'])%2==0
 result=dict(status='EXACT_FINITE_GRAPH_PARITY_CERTIFICATE',states=len(states),edges=sum(map(len,adj.values())),reachable_states=len(potential),reachable_edges=sum(len(adj[u]) for u in potential),empty_potentials=[potential[0,0],potential[1,0]],records=[dict(**states[u],reachable=u in potential,potential=potential.get(u),successors=[list(v) for v in adj[u]]) for u in sorted(states)])
 Path(__file__).with_name('cap4_unit_diagonal_transfer_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='records'}))
if __name__=='__main__':run()
