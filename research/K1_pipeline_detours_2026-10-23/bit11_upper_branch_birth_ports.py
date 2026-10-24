"""Complete secondary square for the upper maximum branch.
One-step physical birth classification only; no exterior realization.
"""
from pathlib import Path
from itertools import product
import json
H='NESW'
def out(s):return[H[(H.index(v)+(1 if r%2==0 else-1))%4]for r,v in enumerate(s)]
def ts():
 for n in range(1,5):
  for ls in product('NS',repeat=n//2):yield ''.join('N'if r%2==0 else ls[r//2]for r in range(n)),'strict'
 for first in 'NS':
  for n in (3,4):
   for ls in product('NS',repeat=n//2):yield first+ls[0]+('S'if first=='N'else'N')+(''if n==3 else ls[1]),'equal'
def feasible(h,kind,birth):
 ns=[(v,r)for v in h for r in range(len(h[v]))];es=[]
 def eq(a,b):es.extend([(a,b,1),(b,a,-1)])
 for v in h:
  for r in range(len(h[v])-1):es.append(((v,r),(v,r+1),4))
 oh={v:out(x)for v,x in h.items()}
 ports=[('A','W','Z','W'),('Z','N','Y','N'),('Y','E','B','E'),('B','S','A','S'),('B','N','v','N'),('v','W','a','W'),('a','S','Y','S'),('Y','W','u','W'),('u','N','t','N'),('t','E','a','E')]
 ports+= [('v','E','D','E')]if kind=='S'else [('v','E','w','E'),('w','S','D','S'),('D','W','B','W')]
 for x,o,y,i in ports:
  src=[(x,r)for r,z in enumerate(oh[x])if z==o];tar=[(y,r)for r,z in enumerate(h[y])if z==i]
  if len(src)!=len(tar):return
  for x1,y1 in zip(src,tar):eq(x1,y1)
 order=[('A',1),('B',0),('A',2),('B',1),('D',0),('B',2),('D',1)]
 for x,y in zip(order,order[1:]):es.append((x,y,1))
 first=[next((v,r)for r,x in enumerate(oh[v])if x==o)for v,o in [('u','N'),('t','E'),('a','S'),('Y','W')]]
 b=(birth,1)
 if b not in first:return
 for x in first:
  if x!=b:es.append((b,x,1))
 d={x:0 for x in ns}
 for _ in ns:
  change=False
  for x,y,k in es:
   if d[y]<d[x]+k:d[y]=d[x]+k;change=True
  if not change:break
 else:return
 off=d['B',1];return{v:[d[v,r]-off for r in range(len(h[v]))]for v in h}
rows=[];count=0
source=json.loads(Path(__file__).with_name('bit11_max_RIGHT_outward_parent_ports.json').read_text())
for prior in source['rows']:
 for uh,(th,other),birth in product(['W','WE','WEE','WEEE','EEW','EEWE'],ts(),['u','t']):
  if birth=='u' and uh not in ['EEW','EEWE']:continue
  if birth=='t' and not th.startswith('SSN'):continue
  hs=dict(prior['headings'],u=uh,t=th);count+=1;t=feasible(hs,prior['kind'],birth)
  if t is not None:rows.append(dict(kind=prior['kind'],lower_other='M-1'if uh in ['W','WE']else'M',upper_other=('M'if other=='equal'else'M-'+str((len(th)+1)//2)),birth=birth,headings=hs,minimum_clocks=t))
r=dict(scope=__doc__,candidates=count,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(dict(scope=r['scope'],candidates=count,count=len(rows),profiles=sorted(set((x['birth'],x['lower_other'],x['upper_other'],x['headings']['u'],x['headings']['t'],x['headings']['a'])for x in rows))),indent=2))
