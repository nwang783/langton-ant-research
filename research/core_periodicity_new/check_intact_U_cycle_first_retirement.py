"""Author-only handoff lead: first retirement of a current unit cycle.
No word search, age threshold or historical component inference.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path(__file__).resolve().parent
GP=R/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry']
IDS=(0,1,4,5,6,7,8,9);K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
Z={(1,0),(1,1),(2,0),(2,1)}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def place(q,p,h):
 x,y=rot(q,h);return p[0]+x,p[1]+y
rows=[];stats=Counter();surv={}
for a in IDS:
 for q in sorted(Z):
  for i in G[a]['inputs']:
   for h in range(4):
    ri=rot(i,h);p=q[0]-ri[0],q[1]-ri[1]
    I={place(z,p,h)for z in G[a]['inputs']}
    C={place(z,p,h)for z in K}
    W={place(z[:2],p,h)for z in G[a]['requirements']if not z[2]}
    why='wrong_sector'if(sum(p)+h)%2 else'old_cycle_core'if Z&C else'old_cycle_white'if Z&W else'candidate'
    stats[why]+=1
    rec=dict(packet=a,name=G[a]['name'],source_cycle_cell=q,input_slot=i,consumer_pose=(*p,h),reason=why,cycle_inputs=sorted(Z&I),core_hits=sorted(Z&C),white_hits=sorted(Z&W))
    rows.append(rec)
    if why=='candidate':surv[a,*p,h]=rec
expected_poses={(0,-1,1),(0,2,2),(3,-1,0),(3,2,3)}
assert set(surv)=={(a,*p)for a in(7,8,9)for p in expected_poses}
for a,x,y,h in surv:
 row=surv[a,x,y,h];p=x,y
 assert set(map(tuple,row['cycle_inputs']))=={place((-1,1),p,h),place((-1,2),p,h)}
O=dict(status='AUTHOR_ONLY_EXACT_FIRST_RETIREMENT_LEAD',scope='All four unit-cycle residual identities must be CURRENT until this first retiring packet. No permanent-cycle, historical-component or U-budget theorem.',cycle_cells=sorted(Z),all_alignments=rows,reason_counts=dict(stats),distinct_remaining_placements=list(surv.values()),conclusion='Only U/UC/UCC can first retire such an intact residual cycle, and every surviving placement consumes exactly its two lower inputs from that cycle.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(GP,Path(__file__).resolve())})
(R/'chronology_dcuv/intact_U_cycle_first_retirement.json').write_text(json.dumps(O,indent=2)+'\n')
print(json.dumps(dict(alignments=len(rows),counts=dict(stats),distinct_survivors=len(surv)),indent=2))
