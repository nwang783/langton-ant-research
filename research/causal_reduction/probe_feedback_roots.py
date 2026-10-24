from ancestry import simulate
from collections import Counter
import json
from pathlib import Path
G={(0,-1),(1,1),(1,3),(2,2)}
def rot(q,j):
 x,y=q
 for _ in range(j%4):x,y=y,-x
 return x,y
def ccw(q):return(-q[1],q[0])
def make(n):
 poses=[((0,0),1),((n-1,n),0),((-n,3*n-4),3),((-5*n+5,-n),2),((-3*n,-3*n+8),1)]
 B=set();keys=[]
 for p,h in poses:
  for q in G:
   r=rot(q,h-1);B.add(ccw((p[0]+r[0],p[1]+r[1])))
  r=rot((0,-1),h-1);keys.append(ccw((p[0]+r[0],p[1]+r[1])))
 return B,keys
rows=[]
for n in [20,40,80,160]:
 B,keys=make(n);e=624*n-1516;d=simulate(e+774+3000,B);nodes=d['nodes'];labels=[]
 for a in nodes:
  p=a['parent'];labels.append(0 if p is None else p if p<0 else labels[p])
 keylabels=[-(d['initial'].index(q)+1) for q in keys]
 birth_node=d['reads'][60][2];consumer_node=d['reads'][e][2]+1
 tail=[a for a in nodes if a['time']>=e+774+1000]
 tailroots=Counter(labels[a['id']] for a in tail)
 # Exact last-occurrence of each root in this finite prefix. NOT infinity assertion.
 lastroot={root:max(a['time'] for a,l in zip(nodes,labels) if l==root) for root in set(labels)}
 rows.append(dict(n=n,key_roots=keylabels,birth_root=labels[birth_node],consumption_child_root=labels[consumer_node],tail_root_counts=dict(tailroots),last_root_node_times=lastroot))
 print(rows[-1])
Path(__file__).with_name('feedback_root_probes.json').write_text(json.dumps(rows,indent=2))
