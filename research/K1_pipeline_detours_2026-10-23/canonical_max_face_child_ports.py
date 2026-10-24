"""Complete necessary maximum-face corner inventory with one canonical birth.
Count possible rank-one canonical child contacts. No K1 ordering is imposed.
"""
from itertools import product
from pathlib import Path
import json
H='NESW'
def out(h):return [H[(H.index(x)+(1 if r%2==0 else-1))%4]for r,x in enumerate(h)]
def histories(pos):
 neg=H[(H.index(pos)+2)%4]
 for n in range(1,5):
  for ls in product((pos,neg),repeat=n//2):yield ''.join(pos if r%2==0 else ls[r//2]for r in range(n)),'M-'+str((n+1)//2)
 for start in(pos,neg):
  for n in(3,4):
   for ls in product((pos,neg),repeat=n//2):yield start+ls[0]+(neg if start==pos else pos)+(''if n==3 else ls[1]),'M'
def feasible(h):
 ns=[(v,r)for v in h for r in range(len(h[v]))];es=[]
 for v in h:
  for r in range(len(h[v])-1):es.append(((v,r),(v,r+1),4))
 oh={v:out(h[v])for v in h}
 for v,o,w,i in [('A','W','Z','W'),('Z','N','Y','N'),('Y','E','B','E'),('B','S','A','S')]:
  a=[(v,r)for r,z in enumerate(oh[v])if z==o];b=[(w,r)for r,z in enumerate(h[w])if z==i]
  if len(a)!=len(b):return
  for x,y in zip(a,b):es.extend([(x,y,1),(y,x,-1)])
 first=[next((v,r)for r,z in enumerate(oh[v])if z==o)for v,o in [('A','W'),('Z','N'),('Y','E'),('B','S')]]
 if ('A',1)not in first:return
 for x in first:
  if x!=('A',1):es.append((('A',1),x,1))
 d={x:0 for x in ns}
 for _ in ns:
  change=False
  for x,y,k in es:
   if d[y]<d[x]+k:d[y]=d[x]+k;change=True
  if not change:break
 else:return
 off=d['A',1];return{v:[d[v,r]-off for r in range(len(h[v]))]for v in h}
rows=[];candidates=0
for ah,(zh,zo),(yh,yo),(bh,bo)in product(['NNS','NNSN','NNSS'],histories('W'),histories('N'),histories('E')):
 candidates+=1;h=dict(A=ah,Z=zh,Y=yh,B=bh)
 if any(out(h[v]).count(o)!=h[w].count(i)for v,o,w,i in [('A','W','Z','W'),('Z','N','Y','N'),('Y','E','B','E'),('B','S','A','S')]):continue
 t=feasible(h)
 if t is None:continue
 child=[v for v,p in [('Z','WWE'),('Y','NNS'),('B','EEW')]if h[v].startswith(p)]
 rows.append(dict(headings=h,other=dict(Z=zo,Y=yo,B=bo),potential_children=child,minimum_clocks=t))
r=dict(scope=__doc__,candidates=candidates,count=len(rows),child_count_histogram={str(i):sum(len(x['potential_children'])==i for x in rows)for i in range(4)},rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items()if k!='rows'}|dict(forks=[x for x in rows if len(x['potential_children'])>=2]),indent=2))
