"""Exact necessary local port/clock classification of an equal-M left branch
at a straight K1 birth face. No period/front solver.
"""
from itertools import product
from pathlib import Path
import json
ph={'A':0,'Z':1,'B':2}
def sel():
 for last in(None,0,2):yield[0,0,2]+([]if last is None else[last])
def flat():
 for h in(1,3):
  for length in(3,4):
   for l in product((1,3),repeat=length//2):
    yield[h,l[0],(h+2)%4]+([]if length==3 else[l[1]])
def outs(h):return[(x+(1 if r%2==0 else-1))%4 for r,x in enumerate(h)]
def feas(h):
 ns=[(v,r)for v in h for r in range(len(h[v]))];es=[]
 for v in h:
  for r in range(len(h[v])-1):es.append(((v,r),(v,r+1),1))
 for a,o,b,inc in [('A',3,'Z',3),('Z',0,'B',0)]:
  src=[(a,r)for r,x in enumerate(outs(h[a]))if x==o];tar=[(b,r)for r,x in enumerate(h[b])if x==inc]
  if len(src)!=len(tar):return
  for x,y in zip(src,tar):
   k=(ph[a]+1-ph[b])//4;assert(ph[a]+1-ph[b])%4==0;es.extend([(x,y,k),(y,x,-k)])
 for a,b in [(('A',1),('B',0)),(('B',0),('A',2)),(('A',2),('B',1))]:
  k=-(-(ph[a[0]]+1-ph[b[0]])//4);es.append((a,b,k))
 d={x:0 for x in ns}
 for it in range(len(ns)):
  change=False
  for a,b,k in es:
   if d[b]<d[a]+k:d[b]=d[a]+k;change=True
  if not change:break
 else:return
 off=d['A',1];return{v:[4*(d[v,r]-off)+ph[v]for r in range(len(h[v]))]for v in h}
rows=[]
for a,z,b in product(sel(),flat(),sel()):
 h=dict(A=a,Z=z,B=b);t=feas(h)
 if t is not None:rows.append(dict(headings=h,minimal_clock=t))
r=dict(status='Exact necessary local equal-M branch table; no exterior connector asserted',rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
