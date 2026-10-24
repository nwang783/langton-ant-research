"""Discovery upper bound: monotone produced-token closure in finite white patch.
Outside inputs treated freely present, deletion/white reads/head continuity forgotten.
Only strict packet entering/created peak < target threshold is imposed.
"""
import json,sys
from pathlib import Path
from collections import deque,defaultdict
from resource_profile import load_profile
profile,pot=map(Path,sys.argv[1:3]); target,phase,R=map(int,sys.argv[3:6]); out=Path(sys.argv[6])
P,D,M=load_profile(profile);G=D['geometry']['geometry'];v=json.loads(pot.read_text())['values'];keep=P['keep']
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def L(q):return v['ax']*q[0]+v['ay']*q[1]
def A(h):return L(rot((-1,1),h))+v[f'c{h%4}']
def T(a,h):
 h%=4;g=G[a];e=g['endpoint'];return max([2*L(rot(e[:2],h))+A(h+e[2])]+[2*L(rot(q,h))+v[f'w_{a}_{i}_{h}']for i,q in enumerate(g['outputs'])])
S=T(target,phase);points={(x,y)for x in range(-R,R+1)for y in range(-R,R+1)};points|=set(map(tuple,G[target]['inputs']));Q=sorted(points);ix={q:i for i,q in enumerate(Q)};actions=set()
for q in Q:
 for a in keep:
  for h in range(4):
   for oo in G[a]['outputs']:
    z=rot(oo,h);p=q[0]-z[0],q[1]-z[1]
    if (sum(p)+h)%2:continue
    if 2*L(rot(p,phase))+max(A(h+phase),T(a,h+phase))<S:actions.add((*p,h,a))
edges=[];need=[];depend=defaultdict(list);queue=deque();enabled=[]
for x,y,h,a in sorted(actions):
 def absolute(q):z=rot(q,h);return x+z[0],y+z[1]
 ins={ix[q]for q in map(absolute,G[a]['inputs'])if q in ix};outs={ix[q]for q in map(absolute,G[a]['outputs'])if q in ix};k=len(edges);edges.append((sorted(ins),sorted(outs),(x,y,h,a)));need.append(len(ins))
 for i in ins:depend[i].append(k)
 if not ins:queue.append(k)
reached=set();rounds=0
while queue:
 k=queue.popleft();enabled.append(k)
 for i in edges[k][1]:
  if i not in reached:
   reached.add(i)
   for j in depend[i]:
    need[j]-=1
    if need[j]==0:queue.append(j)
empty=[Q[i]for i in range(len(Q))if i not in reached];goal=[q for q in map(tuple,G[target]['inputs'])if ix[q]not in reached];J={'target':target,'phase':phase,'R':R,'threshold':S,'points':len(Q),'actions':len(edges),'reached':len(reached),'empty':empty,'unreachable_goal_inputs':goal,'scope':'Monotone necessary-input upper bound; outside arbitrary, head continuity and deletion forgotten.'};out.write_text(json.dumps(J));print(json.dumps({k:v for k,v in J.items()if k not in('empty','scope')}))
