"""Exact predecessor-RIGHT/straight-max-branch histories, no exterior realization."""
from itertools import product
from pathlib import Path
import json
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
 for a,out,b,inc in [('V',2,'a',2),('a',3,'r',3),('r',0,'U',0),('U',1,'V',1),('U',3,'z',3),('z',2,'q',2),('q',1,'r',1)]:
  src=[(a,r)for r,x in enumerate(oh[a])if x==out];tar=[(b,r)for r,x in enumerate(hs[b])if x==inc]
  if len(src)!=len(tar):return None
  for x,y in zip(src,tar):eql(x,y)
 es.append((('V',2),('U',1),1))
 dist={n:0 for n in ns}
 for it in range(len(ns)):
  change=False
  for a,b,k in es:
   if dist[b]<dist[a]+k:dist[b]=dist[a]+k;change=True
  if not change:break
 else:return None
 off=dist['U',1]
 return{v:[dist[v,r]-off for r in range(len(h))]for v,h in hs.items()}
rows=[]
for za,yr in product(('strict','equal'),repeat=2):
 for v,u,a,r,q in product(([3,3,1],[3,3,1,3],[3,3,1,1]),([0,0,2],[0,0,2,2]),strict(2)if za=='strict'else flat(2),strict(3)if yr=='strict'else flat(3),strict(2)if yr=='strict'else flat(0)):
  if yr=='strict' and (len(r)+1)//2!=(len(q)+1)//2:continue
  hs=dict(V=v,a=a,r=r,U=u,z=[3,3,1,1],q=q);t=feasible(hs)
  if t is not None:rows.append(dict(a_other=za,r_other=yr,headings={k:''.join(H[i]for i in v)for k,v in hs.items()},minimum_clocks=t))
r=dict(scope=__doc__,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
