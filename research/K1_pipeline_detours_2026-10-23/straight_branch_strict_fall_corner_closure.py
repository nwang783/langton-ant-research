"""Strict-fall entrance plus signed straight-branch successor: local closure only."""
import json
from itertools import product
from pathlib import Path
H='NESW'
def outs(h):return[(x+(1 if i%2==0 else -1))%4 for i,x in enumerate(h)]
def strict(h):
 for n in range(1,5):
  for ls in product((h,(h+2)%4),repeat=n//2):yield[h if r%2==0 else ls[r//2]for r in range(n)]
def flat(h):
 for first in (h,(h+2)%4):
  for n in (3,4):
   for ls in product((h,(h+2)%4),repeat=n//2):yield[first,ls[0],(first+2)%4]+([]if n==3 else[ls[1]])
def feasible(hs):
 ns=[(v,r)for v,h in hs.items()for r in range(len(h))];es=[]
 def eql(a,b):es.extend([(a,b,1),(b,a,-1)])
 for v,h in hs.items():
  for r in range(len(h)-1):es.append(((v,r),(v,r+1),4))
 oh={v:outs(h)for v,h in hs.items()}
 for a,out,b,inc in [('A',3,'Z',3),('Z',0,'Y',0),('Y',1,'B',1),('B',2,'A',2),('e',1,'z',1),('Z',2,'e',2),('z',0,'A',0),('U',3,'z',3),('z',2,'q',2),('q',3,'u',3),('u',0,'e',0)]:
  src=[(a,r)for r,x in enumerate(oh[a])if x==out];tar=[(b,r)for r,x in enumerate(hs[b])if x==inc]
  if len(src)!=len(tar):return None
  for x,y in zip(src,tar):eql(x,y)
 es.append((('A',2),('B',1),1))
 dist={n:0 for n in ns}
 for it in range(len(ns)):
  change=False
  for a,b,k in es:
   if dist[b]<dist[a]+k:dist[b]=dist[a]+k;change=True
  if not change:break
 else:return None
 off=dist['A',1]
 return{v:[dist[v,r]-off for r in range(len(h))]for v,h in hs.items()}
D=json.loads(Path(__file__).with_name('straight_branch_right_corner_extension.json').read_text())
rows=[]
for row in D['rows']:
 for U,q,u,uc in product(([0,0,2],[0,0,2,2]),([2,0,2],[2,0,2,0]),list(strict(3))+list(flat(3)),('dummy',)):
  hh={k:[H.index(c)for c in v]for k,v in row['headings'].items()};hh.update(U=U,q=q,u=u)
  t=feasible(hh)
  if t is not None:rows.append(dict(headings={k:''.join(H[i]for i in v)for k,v in hh.items()},minimum_clocks=t))
r=dict(scope=__doc__,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'count':len(rows),'u':sorted(set(x['headings']['u']for x in rows)),'q':sorted(set(x['headings']['q']for x in rows)),'e':sorted(set(x['headings']['e']for x in rows)),'rows':[x['headings']for x in rows]},indent=2))
