"""All S/R successor output states at a bit11 maximum RIGHT branch.
Necessary port and clock inventory, not a complete exterior cursor.
"""
from pathlib import Path
from itertools import product
import json
H='NESW'
def out(h):return[(v+(1 if r%2==0 else-1))%4 for r,v in enumerate(h)]
def feasible(h,kind):
 ns=[(v,r)for v in h for r in range(len(h[v]))];es=[]
 def eq(a,b):es.extend([(a,b,1),(b,a,-1)])
 for v in h:
  for r in range(len(h[v])-1):es.append(((v,r),(v,r+1),4))
 oh={v:out(x)for v,x in h.items()}
 ports=[('A',3,'Z',3),('Z',0,'Y',0),('Y',1,'B',1),('B',2,'A',2),('B',0,'v',0),('v',3,'a',3),('a',2,'Y',2)]
 ports+= [('v',1,'D',1)] if kind=='S' else [('v',1,'w',1),('w',2,'D',2),('D',3,'B',3)]
 for aa,o,b,i in ports:
  src=[(aa,r)for r,x in enumerate(oh[aa])if x==o];tar=[(b,r)for r,x in enumerate(h[b])if x==i]
  if len(src)!=len(tar):return
  for x,y in zip(src,tar):eq(x,y)
 order=[('A',1),('B',0),('A',2),('B',1),('D',0),('B',2),('D',1)]
 for x,y in zip(order,order[1:]):es.append((x,y,1))
 d={x:0 for x in ns}
 for _ in ns:
  change=False
  for x,y,k in es:
   if d[y]<d[x]+k:d[y]=d[x]+k;change=True
  if not change:break
 else:return
 off=d['B',1];return{v:[d[v,r]-off for r in range(len(h[v]))]for v in h}
rows=[];candidates=0
for vh,dh in [('NNN','EEW'),('NNN','EEWW'),('NNNS','EEWE')]:
 for ah in ['EWE','EWEE','EEEW']:
  hh=dict(A='NNSN',Z='WWEW',Y='NSSS',B='EEWE',v=vh,D=dh,a=ah);candidates+=1
  t=feasible({k:[H.index(x)for x in s]for k,s in hh.items()},'S')
  if t is not None:rows.append(dict(kind='S',first_other='strict',headings=hh,minimum_clocks=t))
source=json.loads(Path(__file__).with_name('right_turn_equal_branch_ports.json').read_text())
for report in source['reports']:
 for rr in report['rows']:
  if rr['headings']['A']!=[0,0,2,0]:continue
  rot={k:''.join(H[(x+1)%4]for x in vs)for k,vs in rr['headings'].items()}
  for ah in ['EWE','EWEE','EEEW'] if report['Z_other']=='strict' else ['WWEW','EWWW']:
   hh=dict(A='NNSN',Z='WWEW',Y='NSSS',B=rot['A'],v=rot['Z'],w=rot['Y'],D=rot['B'],a=ah);candidates+=1
   t=feasible({k:[H.index(x)for x in s]for k,s in hh.items()},'R')
   if t is not None:rows.append(dict(kind='R',first_other=report['Z_other'],headings=hh,minimum_clocks=t))
r=dict(scope=__doc__,candidates=candidates,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(dict(scope=r['scope'],candidates=candidates,count=len(rows),profiles=sorted(set((x['kind'],x['first_other'],x['headings']['v'],x['headings'].get('w',''),x['headings']['a'],x['headings']['D'])for x in rows))),indent=2))
