"""The two off-circle unit-face corners at LRL and RLR G3 triples.
Exhaust1..4 WHITE histories and exact face levels; no global scan.
"""
from itertools import product
from pathlib import Path
import json
H='NESW'
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def matches(axis,inc,dep):
 ans=[]
 for n in range(1,5):
  for hh in product(axis,repeat=n):
   h=''.join(hh)
   if h.count(inc)==sum(out(h,r)==dep for r in range(n))==1:ans.append(h)
 return ans
peak=matches('NS','S','W');valley=matches('EW','W','S')
assert set(peak)=={'S','NNNS','NSNN'}and set(valley)=={'EEW','WEE','EEWE','WEEE'}
val=[]
for h in valley:
 rE=sum(s=='E'for s in h[::2]);rW=sum(s=='W'for s in h[::2]);lE=sum(s=='E'for s in h[1::2]);lW=sum(s=='W'for s in h[1::2]);a=-3
 # Inside Q is SE at c-3=-3; lW=0 for every allowed profile.
 assert lW==0 and rE==rW==1
 val.append(dict(headings=h,C=dict(NE=a+rW,SW=a+rE),L=dict(SE=a-lW,NW=a-lE),opposite_L_drop=lE,odd=len(h)%2==1))
assert all(r['opposite_L_drop']in(1,2)for r in val)
obj=dict(scope=__doc__,main_profiles=dict(A=['NNNS','NSNN'],B=['EEWE','WEEE']),LRL_off_corner_profiles=peak,RLR_off_corner_profiles=val,consequences=['At a locally maximal C component, every LRL triple has singleton S; otherwise opposite C rises by2.','At a locally minimal L component, RLR cannot occur; the opposite L drops by1 or2 in every complete WHITE profile.','Essential simple physical circles have no three equal consecutive turns; with no RLR and zero signed turning, every turn run has length2 and the drift is axis.'],warning='Axis restriction concerns a G3 circle touching a locally minimal L plateau, even if the plateau has odd corners. It is not a restriction on arbitrary local minima without such a circle.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
