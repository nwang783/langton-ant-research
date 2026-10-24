"""Complete cap-four local first-R-departure corner multiplicities.
No front, period, drift or support scan.
"""
from pathlib import Path
from itertools import product
import json
H='NESW'
def out(h,i):return H[(H.index(h[i])+(1 if i%2==0 else-1))%4]
right=[];left=[]
for n in range(1,5):
 for tail in product('EW',repeat=n-1):
  h='E'+''.join(tail);fi=h.count('E');fo=sum(out(h,i)=='S'for i in range(n))
  assert fi>=1 and fo>=1
  right.append(dict(headings=h,incoming_cycle='E',outgoing_cycle='S',incoming_first_rank=0,incoming_uses=fi,outgoing_uses=fo))
for n in(3,4):
 for l1 in'EW':
  for l3 in(''if n==3 else'EW'):
   pass
 # Easier retain the exact finite alternating-head choices without special strings.
 for tail in product('EW',repeat=n-1):
  h='W'+''.join(tail)
  if h[2]!='E':continue
  fi=h.count('E');fo=sum(out(h,i)=='N'for i in range(n));assert fi==fo
  left.append(dict(headings=h,incoming_cycle='E',outgoing_cycle='N',incoming_first_rank=h.index('E'),incoming_uses=fi,outgoing_uses=fo))
assert len(right)==15 and len(left)==6
assert {r['headings']for r in left if r['incoming_uses']==1}=={'WWE','WWEW'}
assert {r['headings']for r in left if r['incoming_uses']==2}=={'WEE','WEEW','WWEE'}
assert {r['headings']for r in left if r['incoming_uses']==3}=={'WEEE'}
assert [(r['headings'],r['incoming_uses'],r['outgoing_uses'])for r in right if r['outgoing_uses']==4]==[('EWEW',2,4)]
assert [(r['headings'],r['incoming_uses'],r['outgoing_uses'])for r in right if r['incoming_uses']==4]==[('EEEE',4,2)]
obj=dict(scope=__doc__,RIGHT_rows=right,LEFT_rows=left,counts=dict(RIGHT=15,LEFT=6),warning='LEFT flatness uses constancy of selected clockwise C height around an actual b-cycle. Locally allowed rows are not complete-front realizations or a refutation of a global one-use theorem.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS',len(right),len(left))
