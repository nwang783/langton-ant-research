"""Necessary RR stock to strict straight closure, retaining late source L3."""
from pathlib import Path
import json
H='NESW'
def out(h):return[(v+(1 if r%2==0 else-1))%4 for r,v in enumerate(h)]
def feasible(h):
 ns=[(v,r)for v in h for r in range(len(h[v]))];es=[]
 def eq(a,b):es.extend([(a,b,1),(b,a,-1)])
 for v in h:
  for r in range(len(h[v])-1):es.append(((v,r),(v,r+1),4))
 oh={v:out(x)for v,x in h.items()}
 for a,o,b,i in [('A',3,'Z',3),('Z',0,'Y',0),('Y',1,'B',1),('B',2,'A',2),('B',0,'n',0),('n',1,'p',1),('p',2,'C',2),('C',3,'B',3),('n',3,'m',3),('m',2,'Y',2),('C',1,'v',1),('v',2,'D',2),('v',0,'a',0),('a',3,'p',3)]:
  src=[(a,r)for r,x in enumerate(oh[a])if x==o];tar=[(b,r)for r,x in enumerate(h[b])if x==i]
  if len(src)!=len(tar):return
  for x,y in zip(src,tar):eq(x,y)
 for a,b in[(('A',2),('B',1)),(('B',2),('C',1)),(('C',2),('D',1))]:es.append((a,b,1))
 d={x:0 for x in ns}
 for _ in ns:
  change=False
  for a,b,k in es:
   if d[b]<d[a]+k:d[b]=d[a]+k;change=True
  if not change:break
 else:return
 off=d['B',1];return{v:[d[v,r]-off for r in range(len(h[v]))]for v in h}
rows=[]
from itertools import product
for mm,aa,vv,dd in product(['WWW','WWWE'],['SNS','SNSS','SSSN'],['EEE','EEEW'],['SSN','SSNS','SSNN']):
 hh=dict(A='NNSN',Z='WWWE',Y='NNNS',B='EEWE',n='NNSN',p='EWWW',C='SSNS',m=mm,a=aa,v=vv,D=dd);hs={k:[H.index(x)for x in w]for k,w in hh.items()};t=feasible(hs)
 if t is not None:rows.append(dict(headings=hh,minimum_clocks=t))
r=dict(scope=__doc__,count=len(rows),rows=rows);Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
