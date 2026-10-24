"""Algebra-only controls for the degree-minus-one temporal-cover identity.
Not ant fronts, board factors or geometry controls. Physical hypotheses
(distinct selected event phases, critical side partition) require proof.
"""
from itertools import product
from pathlib import Path
import json
rows=[]
for n in range(2,6):
 for kinds in product('XYO',repeat=n):
  jumps=[8 if k=='X'else -12 if k=='Y'else-4 for k in kinds]
  P=-(n+sum(jumps))
  if P<=0:continue
  edge=[];xp=[];yp=[];op=[];cur=0
  for k,d in zip(kinds,jumps):
   nxt=cur+d
   if k=='X':xp.append((cur,nxt))
   elif k=='Y':yp.append((nxt,cur))
   else:op.append((nxt,cur))
   edge.append((nxt,nxt+1));cur=nxt+1
  assert cur==-P
  def covers(a,b,t):
   # count ALL P-translated copies of this oriented positive interval.
   lo=(t-b)//P+1;hi=(t-a)//P
   return max(0,int(hi-lo+1))
  for q in range(P):
   t=q+.5
   c=lambda xs:sum(covers(a,b,t)for a,b in xs)
   B,NX,NY,I2=map(c,[edge,xp,yp,op])
   assert NY-NX==1+B-I2
  rows.append(dict(kinds=''.join(kinds),P=P,selected_event_phases_distinct=len({int(a)%P for a,b in edge})==n))
obj=dict(scope=__doc__,cochain_controls=len(rows),distinct_phase_controls=sum(r['selected_event_phases_distinct']for r in rows),all_regular_time_equalities=True,rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS',len(rows),'algebra controls, all translated copies retained')
