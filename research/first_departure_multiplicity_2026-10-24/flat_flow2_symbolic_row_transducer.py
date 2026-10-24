"""All-length local row transducer for constant flow2 staircase departure segments.
Five consecutive main corners plus forced D cells and one E cell.
No period, drift, width, front, or bounded-length search.
"""
from itertools import product
from pathlib import Path
from collections import Counter
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
A={'X':'NNSS','Y':'NSSN'};B={'U':'WEEW','V':'WWEE'};D={'U':'NNSS','V':'SSNN'};Ec=['EEW','WEE','EEWW','EWWE','WEEW','WWEE']
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def check(hs):
 ns=[(p,r)for p,h in hs.items()for r in range(len(h))];es=[];succ={}
 for p,h in hs.items():
  for r in range(len(h)-1):es.append(((p,r),(p,r+1),4))
  for dr in H:
   q=(p[0]+V[dr][0],p[1]+V[dr][1]);sr=[r for r in range(len(h))if out(h,r)==dr]
   if q not in hs:continue
   tr=[r for r,x in enumerate(hs[q])if x==dr]
   if len(sr)!=len(tr):return 'port',None
   for x,y in zip(sr,tr):
    a,b=(p,x),(q,y);succ[a]=b;es.extend([(a,b,1),(b,a,-1)])
 # Literal forced successor paths cannot skip the next read at a physical cell.
 for a in ns:
  cur=a;seen={a}
  for _ in range(len(ns)+1):
   if cur not in succ:break
   cur=succ[cur]
   if cur[0]==a[0]:
    if cur[1]!=a[1]+1:return 'skipped_rank',None
    break
   if cur in seen:return 'event_cycle',None
   seen.add(cur)
 d={a:0 for a in ns}
 for _ in ns:
  change=False
  for a,b,k in es:
   if d[b]<d[a]+k:d[b]=d[a]+k;change=True
  if not change:return 'open',d
 return 'clock_cycle',None
rows=[]
for bp,a,b,ap,bn in product('UV','XY','UV','XY','UV'):
 hs={(0,-1):B[bp],(0,0):A[a],(1,0):B[b],(1,1):A[ap],(2,1):B[bn],(1,-1):D[b],(2,0):D[bn]}
 good=[];bad=Counter()
 for eh in Ec:
  ans,cl=check(hs|{(2,-1):eh});bad[ans]+=1
  if ans=='open':good.append(eh)
 rows.append(dict(Bprev=bp,A=a,B=b,Anext=ap,Bnext=bn,E_modes=good,rejections=dict(bad)))
obj=dict(scope=__doc__,A_modes=A,B_modes=B,forced_D_modes=D,E_candidates=Ec,rows=rows,admissible_count=sum(bool(r['E_modes'])for r in rows),warning='A compositional necessary local language only. Surviving modes may fail outside this row or under global clock/board constraints. No whole-cycle or front existence is inferred.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('admissible',obj['admissible_count'],'of',len(rows))
for r in rows:
 if r['E_modes']:print(r)
