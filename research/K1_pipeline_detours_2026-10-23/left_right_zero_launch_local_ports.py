"""Necessary local port/clock control of adjacent LEFT/RIGHT bends in state0.
Exterior connector histories and whole-front existence are NOT asserted.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,contextlib,io
with contextlib.redirect_stdout(io.StringIO()):
 from right_turn_local_ports import helper,sel
 from right_turn_equal_branch_ports import flat
ph=dict(C=0,A=1,Z=2,Y=3,B=0,Q=3)
def selected0(h):yield[h,h,(h+2)%4];yield[h,h,(h+2)%4,(h+2)%4]
def outs(x):return[(h+(1 if r%2==0 else-1))%4 for r,h in enumerate(x)]
def feasible(h):
 ns=[(v,r)for v in h for r in range(len(h[v]))];es=[]
 for v in h:
  for r in range(len(h[v])-1):es.append(((v,r),(v,r+1),1))
 for a,o,b,inc in [('Q',1,'C',1),('C',0,'A',0),('A',3,'Z',3),('Z',0,'Y',0),('Y',1,'B',1),('B',2,'A',2),('Z',2,'Q',2)]:
  src=[(a,r)for r,x in enumerate(outs(h[a]))if x==o];tar=[(b,r)for r,x in enumerate(h[b])if x==inc]
  if len(src)!=len(tar):return
  for x,y in zip(src,tar):
   assert(ph[a]+1-ph[b])%4==0;k=(ph[a]+1-ph[b])//4;es.extend([(x,y,k),(y,x,-k)])
 order=[('C',1),('A',0),('C',2),('A',1),('B',0),('A',2),('B',1)]
 for a,b in zip(order,order[1:]):
  k=-(-(ph[a[0]]+1-ph[b[0]])//4);es.append((a,b,k))
 d={x:0 for x in ns}
 for it in range(len(ns)):
  ch=False
  for a,b,k in es:
   if d[b]<d[a]+k:d[b]=d[a]+k;ch=True
  if not ch:break
 else:return
 off=d['C',1];return{v:[4*(d[v,r]-off)+ph[v]for r in range(len(h[v]))]for v in h}
reports=[]
for gz,gy in product(('strict','equal'),repeat=2):
 rows=[]
 for c,a,z,y,b,q in product(selected0(1),selected0(0),helper(3)if gz=='strict'else flat(3),helper(0)if gy=='strict'else flat(0),sel(1),helper(0)if gz=='strict'else flat(0)):
  if gz=='strict'and(len(z)+1)//2!=(len(q)+1)//2:continue
  h=dict(C=c,A=a,Z=z,Y=y,B=b,Q=q);t=feasible(h)
  if t is not None:rows.append(dict(headings=h,minimal_clock=t))
 summary=Counter((tuple(x['headings']['Z']),tuple(x['headings']['Y']),tuple(x['headings']['Q']))for x in rows)
 reports.append(dict(GZ=gz,GY=gy,count=len(rows),patterns=[dict(Z=k[0],Y=k[1],Q=k[2],rows=v)for k,v in sorted(summary.items())],rows=rows))
r=dict(scope=__doc__,heading_key=['N','E','S','W'],reports=reports)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({**r,'reports':[{k:v for k,v in x.items()if k!='rows'}for x in reports]},indent=2))
