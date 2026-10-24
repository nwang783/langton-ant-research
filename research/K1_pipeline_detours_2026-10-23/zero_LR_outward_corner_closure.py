"""Exact outward supplier closure at a zero-state LEFT/RIGHT pair.
Signed local inventories only; no exterior or period search.
"""
from pathlib import Path
from itertools import product
from collections import Counter
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
 for a,out,b,inc in [('q',1,'C',1),('C',0,'A',0),('A',3,'Z',3),('Z',0,'Y',0),('Y',1,'B',1),('B',2,'A',2),('Z',2,'q',2),('q',3,'u',3),('u',0,'e',0),('e',1,'Z',1)]:
  src=[(a,r)for r,x in enumerate(oh[a])if x==out];tar=[(b,r)for r,x in enumerate(hs[b])if x==inc]
  if len(src)!=len(tar):return None
  for x,y in zip(src,tar):eql(x,y)
 order=[('C',1),('A',0),('C',2),('A',1),('B',0),('A',2),('B',1)]
 for a,b in zip(order,order[1:]):es.append((a,b,1))
 dist={n:0 for n in ns}
 for it in range(len(ns)):
  change=False
  for a,b,k in es:
   if dist[b]<dist[a]+k:dist[b]=dist[a]+k;change=True
  if not change:break
 else:return None
 off=dist['C',1]
 return{v:[dist[v,r]-off for r in range(len(h))]for v,h in hs.items()}
base=json.loads(Path(__file__).with_name('left_right_zero_launch_local_ports.json').read_text())['reports'][-1]['rows']
rows=[]
for old,pu,qe in product(base,('strict','equal'),('strict','equal')):
 hh={('q'if k=='Q'else k):v for k,v in old['headings'].items()}
 if hh['Z']==[1,1,3,3]:continue # canonical F first-boundary gate
 if len(hh['B'])==4 and hh['B'][3]==1:continue # retain state0 through B
 for u,e in product(strict(3)if pu=='strict'else flat(3),strict(0)if qe=='strict'else flat(0)):
  hs=dict(hh,u=u,e=e);t=feasible(hs)
  if t is not None:rows.append(dict(u_other=pu,e_other=qe,headings={k:''.join(H[i]for i in v)for k,v in hs.items()},minimum_clocks=t))
c=Counter((x['headings']['Z'],x['headings']['q'],x['headings']['u'],x['headings']['e'])for x in rows)
r=dict(scope=__doc__,count=len(rows),corner_patterns=[dict(Z=k[0],q=k[1],u=k[2],e=k[3],count=v)for k,v in sorted(c.items())],rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k!='rows'},indent=2))
