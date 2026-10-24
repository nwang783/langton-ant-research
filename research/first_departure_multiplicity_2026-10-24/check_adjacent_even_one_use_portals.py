"""Exact two-portal composition. Counts retain O/U lower roots; the surviving
join has an actual8-step same-event cycle independent of external readers.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
rows=[];ct=Counter()
for u,l in product(['EWW','EWWE'],repeat=2):
 hs={}
 for i,y in enumerate([u,l]):hs.update({(1,1-2*i):'SN',(0,1-2*i):y,(0,-2*i):'NNSS',(1,-2*i):'EE'})
 su={};bad=[]
 for p,h in hs.items():
  for d,v in V.items():
   q=p[0]+v[0],p[1]+v[1]
   if q not in hs:continue
   sr=[r for r in range(len(h))if out(h,r)==d];tr=[r for r,z in enumerate(hs[q])if z==d]
   if len(sr)!=len(tr):bad.append(dict(source=p,target=q,direction=d,sr=sr,tr=tr))
   else:su.update({(p,r):(q,s)for r,s in zip(sr,tr)})
 if bad:
  assert l=='EWW';ans='port';data=bad
 else:
  assert l=='EWWE';path=[((1,-1),0),((0,-1),1),((0,-2),3),((1,-2),1),((1,-1),1),((0,-1),2),((0,0),0),((1,0),0),((1,-1),0)]
  assert all(su[e]==f for e,f in zip(path,path[1:]));ans='actual_event_cycle';data=path
 ct[ans]+=1;rows.append(dict(upper_root=u,lower_root=l,result=ans,certificate=data))
assert ct=={'port':2,'actual_event_cycle':2}
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(ct),rows=rows,warning='Exact adjacent complete interface only. Does not exclude one prepared portal or inserted geometry/changed endpoint roles.'),indent=2)+'\n');print('PASS2 port failures+2 actual8-step cycle failures; no adjacent even portals')
