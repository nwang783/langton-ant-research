"""Couple the equal-K RIGHT entrance and signed double-max RIGHT successor.
Finite local ordinal histories only; no exterior or translator search.
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
 for a,out,b,inc in [('V',2,'a',2),('a',3,'r',3),('r',0,'U',0),('U',1,'V',1),('U',3,'z',3),('z',2,'q',2),('q',1,'r',1),('A',3,'w',3),('w',0,'y',0),('y',1,'B',1),('B',2,'A',2),('e',1,'z',1),('w',2,'e',2),('z',0,'A',0),('q',3,'u',3),('u',0,'e',0)]:
  src=[(a,r)for r,x in enumerate(oh[a])if x==out];tar=[(b,r)for r,x in enumerate(hs[b])if x==inc]
  if len(src)!=len(tar):return None
  for x,y in zip(src,tar):eql(x,y)
 for a,b in[(('V',2),('U',1)),(('U',2),('A',1)),(('A',2),('B',1))]:es.append((a,b,1))
 dist={n:0 for n in ns}
 for it in range(len(ns)):
  change=False
  for a,b,k in es:
   if dist[b]<dist[a]+k:dist[b]=dist[a]+k;change=True
  if not change:break
 else:return None
 off=dist['U',1]
 return{v:[dist[v,r]-off for r in range(len(h))]for v,h in hs.items()}
pred=json.loads(Path(__file__).with_name('straight_branch_predecessor_right_ports.json').read_text())['rows']
fut=json.loads(Path(__file__).with_name('straight_branch_right_corner_extension.json').read_text())['rows']
rows=[]
for p,f,u in product(pred,fut,list(strict(3))+list(flat(3))):
 if p['r_other']!='equal':continue
 hh=dict(p['headings']);fh={('w'if k=='Z'else'y'if k=='Y'else k):v for k,v in f['headings'].items()}
 if any(k in hh and hh[k]!=v for k,v in fh.items()):continue
 hh.update(fh);hs={k:[H.index(c)for c in v]for k,v in hh.items()};hs['u']=u
 t=feasible(hs)
 if t is not None:rows.append(dict(a_other=p['a_other'],headings={k:''.join(H[i]for i in v)for k,v in hs.items()},minimum_clocks=t))
c=Counter((x['headings']['q'],x['headings']['u'],x['headings']['e'])for x in rows)
r=dict(scope=__doc__,count=len(rows),corner_patterns=[dict(q=k[0],u=k[1],e=k[2],count=v)for k,v in sorted(c.items())],rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k!='rows'},indent=2))
