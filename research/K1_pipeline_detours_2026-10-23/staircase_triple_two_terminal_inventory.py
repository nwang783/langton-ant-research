"""Direct original-WHITE inward staircase terminal inventory.
No reversal assumption, front search, or period scan.
"""
from itertools import product
from pathlib import Path
import json
H='NESW'
def output(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def count(h,p,kind):return sum((x if kind=='in'else output(h,r))==p for r,x in enumerate(h))
W=[];X=[]
for n in range(1,5):
 for hh in product('EW',repeat=n):
  h=''.join(hh)
  if count(h,'W','in')==count(h,'S','out')==1:
   rE=sum(x=='E'for x in h[::2]);rW=sum(x=='W'for x in h[::2]);lE=sum(x=='E'for x in h[1::2]);lW=sum(x=='W'for x in h[1::2]);a=-3
   W.append(dict(headings=h,C=dict(NE=a+rW,SW=a+rE),L=dict(SE=a-lW,NW=a-lE),odd_terminal=n==3))
 for hh in product('NS',repeat=n):
  h=''.join(hh)
  if count(h,'N','in')==count(h,'E','out')==3:X.append(h)
assert {x['headings']for x in W}=={'EEW','WEE','EEWE','WEEE'}and set(X)=={'NNNS','NSNN'}
assert all(set(r['C'].values())=={-2}and r['L']['SE']==-3 for r in W)
assert all(r['L']['NW']==(-4 if r['odd_terminal']else-5)for r in W)
assert all(count(r['headings'],'E','in')==count(r['headings'],'N','out')==3 for r in W if not r['odd_terminal'])
obj=dict(scope=__doc__,inward_W_profiles=W,inward_X_profiles=X,forced_extension='If all W are four-read, W becomes B of a parallel NE staircase row at c-2; X becomes A from its two triple ports.',terminal='EEW/WEE are opposite-R three-read odd outputs with L1 incoming E; the role and quarter-rotated row frame recover uniquely.',warning='The terminal stops the prescribed straight row continuation, not every possible lower-level physical current or alternate nonstaircase route.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS original-WHITE inward profiles')
