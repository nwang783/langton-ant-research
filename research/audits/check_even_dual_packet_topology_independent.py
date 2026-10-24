"""Literal complete-eight local physical graph topology, no historical labels."""
from pathlib import Path
from collections import defaultdict,deque
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'core_periodicity_new/even_dual_packet_topology_frozen_20261023_1815';M=json.loads((D/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((D/f['frozen']).read_bytes()).hexdigest()==f['sha256']
K={q for q,b in walk(mark)[2].items()if b}
def ends(q):
 x,y=xy(q);return ((2*x-1,2*y-1),(2*x+1,2*y+1))if(x+y)%2==0 else((2*x-1,2*y+1),(2*x+1,2*y-1))
def top(S):
 G=defaultdict(set);E={q:ends(q)for q in S}
 for q,(a,b)in E.items():G[a].add(q);G[b].add(q)
 todo=set(G);cs=0
 while todo:
  w=[todo.pop()];cs+=1
  while w:
   for q in G[w.pop()]:
    for v in E[q]:
     if v in todo:todo.remove(v);w.append(v)
 rank=len(E)-len(G)+cs;alive=set(E);queue=deque(v for v in G if len(G[v])==1)
 while queue:
  v=queue.popleft()
  if len(G[v])!=1:continue
  q=next(iter(G[v]));alive.discard(q)
  for a in E[q]:
   G[a].discard(q)
   if len(G[a])==1:queue.append(a)
 return dict(edges=len(E),vertices=len(G),components=cs,rank=rank,cyclic_core=sorted(map(xy,alive)))
rows=[]
for s in (0,1,4,5,6,7,8,9):
 e,h,_,f=walk(raws[s]);B={q for q,b in walk(raws[s]+mark)[2].items()if b};I=B-K;O=(B^f)-{e+rotation(q,h)for q in K};a=top(I);b=top(O)
 assert a['components']==b['components']==1 and a['rank']==0 and b['rank']==int(s in(7,8,9))
 assert b['cyclic_core']==([(1,0),(1,1),(2,0),(2,1)]if s in(7,8,9)else[])
 rows.append(dict(packet=s,input=a,output=b))
out=dict(status='PASS independent literal all-eight input/output even-dual graph inventory',manifest_sha256=hashlib.sha256((D/'manifest.json').read_bytes()).hexdigest(),rows=rows,scope='Local physical graph only, not historical incidence, merger or global cycle budget.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
