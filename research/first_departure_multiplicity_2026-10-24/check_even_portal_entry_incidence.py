"""Complete six-cell reader-independent entry kernel at the fixed even LL portal.
All 248 complete WHITE cap-four products; literal physical ordinal failures.
No global height, critical-side, period, drift or clock filter is used.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else -1))%4]
def exact(hs):
 su={}
 for p,h in hs.items():
  for d,v in V.items():
   q=p[0]+v[0],p[1]+v[1]
   if q not in hs:continue
   ss=[r for r in range(len(h)) if out(h,r)==d]
   tt=[r for r,z in enumerate(hs[q]) if z==d]
   if len(ss)!=len(tt):return 'port',dict(source=p,direction=d,source_ranks=ss,target=q,target_ranks=tt)
   su.update({(p,r):(q,s) for r,s in zip(ss,tt)})
 for e in sorted(su):
  path=[e];cur=e;seen={e}
  while cur in su:
   cur=su[cur];path.append(cur)
   if cur[0]==e[0]:
    if cur[1]!=e[1]+1:return 'rank',dict(path=path,start_rank=e[1],returned_rank=cur[1])
    break
   if cur in seen:return 'cycle',dict(path=path)
   seen.add(cur)
 return 'open',dict(successor_edges=[[e,f] for e,f in sorted(su.items())])
words=['']+[''.join(z) for n in range(1,5) for z in product('NS',repeat=n)]
rows=[];ct=Counter();open_profiles=[]
for root,q,c in product(['EWW','EWWE'],['E','EE','EEW','EEWE'],words):
 hs={(1,1):'SN',(0,1):root,(0,0):'NNSS',(1,0):'EE',(1,2):q,(0,2):c}
 z,cert=exact(hs);ct[z]+=1
 row=dict(root=root,q=q,C=c,result=z,certificate=cert)
 rows.append(row)
 if z=='open':open_profiles.append((root,q,c))
expected=[('EWW','EE','SSN'),('EWW','EEW','SSN'),('EWW','EEWE','SSNS'),('EWWE','EE','SSNN'),('EWWE','EEW','SSNN')]
assert open_profiles==expected and ct=={'port':225,'rank':18,'open':5}
assert all(out(c,0)=='W' for _,_,c in open_profiles)
# Only LEFT q has a compatible selected incoming b edge. It then has flow one.
LEFT=[z for z in open_profiles if z[1] in ['EEW','EEWE']]
assert LEFT==[('EWW','EEW','SSN'),('EWW','EEWE','SSNS'),('EWWE','EEW','SSNN')]
# Rotation invariant witness classes: O root has opposite L1 heading; q has same.
assert expected[0][0][0]!=expected[0][0][1]
assert all(q[0]==q[1] for root,q,c in LEFT if root=='EWWE')
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(ct),coordinates=dict(B=[1,1],Y=[0,1],Z=[0,0],A=[1,0],q=[1,2],C=[0,2]),open_profiles=open_profiles,cyclic_LEFT_profiles=LEFT,rows=rows,warning='Necessary local entry data only. No actual factor, complete front, renewal or original-fuel charge.'),indent=2)+'\n')
print('PASS248:225 ports+18 literal rank failures+5 open; all5 C.R0 point WEST; three cyclic LEFT profiles')
