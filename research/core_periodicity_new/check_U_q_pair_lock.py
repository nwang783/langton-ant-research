"""All-input-q consumer contexts have exact target-upper cover {b,c}.
No center geometry, age, head-box, reachability search or arbitrary truncation.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];IDS=[0,1,4,5,6,7,8,9]
q=(-1,2);b=(-1,4);c=(0,2);d=(0,3);upper={b,c,d};rows=[];hits=[]
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,z):return p[0]+z[0],p[1]+z[1]
def sub(p,z):return p[0]-z[0],p[1]-z[1]
for a in IDS:
 for h in range(4):
  for si,i in enumerate(G[a]['inputs']):
   p=sub(q,rot(i,h));r=dict(packet=a,pose=[*p,h],input_slot=si)
   if(sum(p)+h)%2:r['reason']='wrong_sector'
   else:
    ctx={add(p,rot(z[:2],h))for z in G[a]['requirements']};hit=ctx&upper;assert hit&{b,c};hits.append(hit)
    r.update(reason='protected_b_or_c_complete_context',upper_hits=sorted(hit),b_c_hits=sorted(hit&{b,c}))
   rows.append(r)
assert len(rows)==92 and len(hits)==46
minimal=[]
for n in range(1,4):
 for z in combinations(sorted(upper),n):
  s=set(z)
  if all(s&h for h in hits)and not any(set(t)<=s for t in minimal):minimal.append(z)
assert minimal==[(b,c)]
applications=[]
for a in[7,8,9]:
 p=(-1,4);h=1;O={add(p,rot(o,h))for o in G[a]['outputs']};assert {q,b,c,d}<=O
 applications.append(dict(source=a,pose=[*p,h],protected_goal_upper_triple=sorted(upper),fresh_extra_q=q,derived='q survives with b,c; all four would be same-producer final inputs, excluded by max-three'))
D=[GP,W/'U_max_three_cohort_frozen_20261023_1805/manifest.json']
R=dict(status='AUTHOR_Q_PAIR_LOCK_PENDING_INDEPENDENT_AUDIT',scope='Actual complete recurrent-eight histories: a current residual q=(-1,2) cannot retire while current identities b=(-1,4),c=(0,2) survive. Thus with b,c held to a future U, q cannot be replaced before that goal. No age, simplicity, a/d existence or common-origin premise. Source U-family(-1,4,E) cannot supply all three final upper identities, since it also births and locks q.',counts=dict(Counter(r['reason']for r in rows)),all_92_q_consumer_alignments=rows,unique_minimal_cover_within_upper_triple=minimal,source_applications=applications,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_q_pair_lock.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(dict(counts=R['counts'],minimal_cover=minimal),indent=2))
