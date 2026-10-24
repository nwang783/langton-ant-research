"""Complete local LEFT/RIGHT pair inventories, retaining all selected L3 states.
Finite local port/clock closure, not a period or translator search.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
H='NESW'
def out(h):return[(v+(1 if r%2==0 else-1))%4 for r,v in enumerate(h)]
def strict(h):
 for n in range(1,5):
  for ls in product((h,(h+2)%4),repeat=n//2):yield[h if r%2==0 else ls[r//2]for r in range(n)]
def flat(h):
 for first in(h,(h+2)%4):
  for n in(3,4):
   for ls in product((h,(h+2)%4),repeat=n//2):yield[first,ls[0],(first+2)%4]+([]if n==3 else[ls[1]])
def feasible(h):
 ns=[(v,r)for v in h for r in range(len(h[v]))];es=[]
 def eq(a,b):es.extend([(a,b,1),(b,a,-1)])
 for v in h:
  for r in range(len(h[v])-1):es.append(((v,r),(v,r+1),4))
 oh={v:out(x)for v,x in h.items()}
 for a,o,b,i in [('q',1,'C',1),('C',0,'A',0),('A',3,'Z',3),('Z',0,'Y',0),('Y',1,'B',1),('B',2,'A',2),('Z',2,'q',2)]:
  src=[(a,r)for r,x in enumerate(oh[a])if x==o];tar=[(b,r)for r,x in enumerate(h[b])if x==i]
  if len(src)!=len(tar):return
  for x,y in zip(src,tar):eq(x,y)
 order=[('C',1),('A',0),('C',2),('A',1),('B',0),('A',2),('B',1)]
 for a,b in zip(order,order[1:]):es.append((a,b,1))
 for r,x in enumerate(oh['Z']):
  if x==0:es.append((('A',1),('Z',r),0)) # actual canonical minimum boundary
 d={x:0 for x in ns}
 for _ in ns:
  change=False
  for a,b,k in es:
   if d[b]<d[a]+k:d[b]=d[a]+k;change=True
  if not change:break
 else:return
 off=d['C',1]
 return{v:[d[v,r]-off for r in range(len(h[v]))]for v in h}
source=json.loads(Path(__file__).with_name('right_turn_equal_branch_ports.json').read_text())
rows=[]
for rep in source['reports']:
 for row,c,q in product(rep['rows'],([1,1,3],[1,1,3,1],[1,1,3,3]),strict(0)if rep['Z_other']=='strict'else flat(0)):
  hs=dict(row['headings'],C=c,q=q)
  if rep['Z_other']=='strict'and(len(q)+1)//2!=(len(hs['Z'])+1)//2:continue
  t=feasible(hs)
  if t is not None:rows.append(dict(Z_other=rep['Z_other'],Y_other=rep['Y_other'],headings={k:''.join(H[i]for i in v)for k,v in hs.items()},minimum_clocks=t))
cnt=Counter((int(x['headings']['A']=='NNSN'),int(x['headings']['B']=='EEWE'),x['Z_other'],x['Y_other'],x['headings']['Z'],x['headings']['Y'],x['headings']['q'])for x in rows)
r=dict(scope=__doc__,count=len(rows),patterns=[dict(sA=k[0],sB=k[1],Z_other=k[2],Y_other=k[3],Z=k[4],Y=k[5],q=k[6],count=v)for k,v in sorted(cnt.items())],rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k!='rows'},indent=2))
