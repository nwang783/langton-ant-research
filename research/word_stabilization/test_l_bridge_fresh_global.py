from collections import defaultdict,deque
from dual_components import edge
import random,json
from pathlib import Path
rng=random.Random(37);D=[(0,1),(1,0),(0,-1),(-1,0)];total=0
for trial in range(30):
 B=set() if not trial else {(x,y) for x in range(-5,6) for y in range(-5,6) if rng.random()<.3};seed=set(B)
 adj=defaultdict(set)
 for q in B:
  a,b=edge(q);adj[a].add(b);adj[b].add(a)
 p=(0,0);h=0;read=set()
 for t in range(20000):
  a,b=edge(p);black=p in B
  if black:
   todo=[a];seen={a}
   while todo and b not in seen:
    v=todo.pop()
    for w in adj[v]:
     if (v==a and w==b)or(v==b and w==a):continue
     if w not in seen:seen.add(w);todo.append(w)
   bridge=b not in seen
   if bridge and p in read:
    out={'status':'COUNTEREXAMPLE','trial':trial,'time':t,'cell':p,'heading':h,'seed':sorted(seed),'current_black':sorted(B),'endpoint_degrees':[len(adj[a]),len(adj[b])]}
    print(json.dumps({k:v for k,v in out.items() if k not in ('seed','current_black')}));Path(__file__).with_suffix('.json').write_text(json.dumps(out));raise SystemExit
   B.remove(p);adj[a].remove(b);adj[b].remove(a)
  else:B.add(p);adj[a].add(b);adj[b].add(a)
  read.add(p);h=(h+(-1 if black else 1))%4;v=D[h];p=p[0]+v[0],p[1]+v[1]
 total+=20000;print('PASS',trial,total,flush=True)
