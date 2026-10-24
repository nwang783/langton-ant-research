"""Necessary strict S / bit11 branched R / bit11 R local overlap.
No full exterior trace or translating front is asserted.
"""
from pathlib import Path
from itertools import product
import json
H='NESW'
def out(h):return[(v+(1 if r%2==0 else-1))%4 for r,v in enumerate(h)]
def feasible(h):
 ns=[(v,r)for v in h for r in range(len(h[v]))];es=[]
 def eq(a,b):es.extend([(a,b,1),(b,a,-1)])
 for v in h:
  for r in range(len(h[v])-1):es.append(((v,r),(v,r+1),4))
 oh={v:out(x)for v,x in h.items()}
 for a,o,b,i in [('A',3,'Z',3),('Z',0,'B',0),('B',3,'w',3),('w',0,'Y',0),('Y',1,'C',1),('C',2,'B',2),('w',2,'e',2),('e',1,'Z',1),('C',0,'n',0),('n',1,'p',1),('p',2,'D',2),('D',3,'C',3),('n',3,'m',3),('m',2,'Y',2)]:
  src=[(a,r)for r,x in enumerate(oh[a])if x==o];tar=[(b,r)for r,x in enumerate(h[b])if x==i]
  if len(src)!=len(tar):return
  for x,y in zip(src,tar):eq(x,y)
 order=[('A',1),('B',0),('A',2),('B',1),('C',0),('B',2),('C',1),('D',0),('C',2),('D',1)]
 for a,b in zip(order,order[1:]):es.append((a,b,1))
 d={x:0 for x in ns}
 for _ in ns:
  change=False
  for a,b,k in es:
   if d[b]<d[a]+k:d[b]=d[a]+k;change=True
  if not change:break
 else:return
 off=d['C',1];return{v:[d[v,r]-off for r in range(len(h[v]))]for v in h}
rows=[]
for (nn,pp),ee in product([('NNN','EWE'),('NNNS','EEEW'),('NNNS','EWEE'),('NNSN','EWWW'),('SNNN','WWEW')],['SSS','SSSN']):
 for mm in ['EWE','EWEE','EEEW'] if nn in ['NNN','NNNS'] else ['WWEW','EWWW']:
  hh=dict(A='NNSN',Z='WWWE',B='NNSN',w='WWEW',Y='NSSS',C='EEWE',e=ee,n=nn,p=pp,D='SSNS',m=mm)
  hs={k:[H.index(x)for x in s]for k,s in hh.items()};t=feasible(hs)
  if t is not None:rows.append(dict(headings=hh,minimum_clocks=t))
r=dict(scope=__doc__,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(dict(scope=r['scope'],count=r['count'],patterns=sorted(set((a['headings']['n'],a['headings']['p'],a['headings']['m'])for a in rows))),indent=2))
