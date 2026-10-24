"""All-age creator-core funding for original strict U1, using signed pair law.
No enlarged observable, count threshold, word search, or age inventory.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent
GP=W/'chronology_dcuv/literal_residual_geometry.json'
RP=W/'atomic_core_record_interface_frozen_20261023_1359/04_root_out.json'
CY=W/'causal_cycle_renewal_20261023_1841/manifest.json'
G=json.loads(GP.read_text())['geometry'];M=json.loads(RP.read_text());A=M['core_offsets'];assert A==[0,22,20,10]
assert M['target']==7 and M['target_global_phase']==1 and M['record_threshold']==30
I=list(map(tuple,G[7]['inputs']));assert I==[(-1,1),(-1,2),(-1,4),(0,2),(0,3)]
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
rows=[]
for a in[7,8,9]:
 O=set(map(tuple,G[a]['outputs']));assert {(2,0),(2,1)}<=O
 for o in[(2,0),(2,1)]:
  for slot,t in enumerate(I):
   for h in range(4):
    p=sub(t,rot(o,h));r=dict(source=a,source_east_output=o,goal_input_slot=slot,goal_input=t,source_pose=[*p,h])
    if(sum(p)+h)%2:r['reason']='wrong_sector'
    elif h!=0 or p!=(-3,1)or slot!={(2,0):0,(2,1):1}[o]:r['reason']='signed_rigid_pair_consumer_geometry_excluded'
    else:
     # The only legal consuming pose under the signed directed cycle law.
     # Its creator is an earlier full packet, and its ENTERING core was
     # already part of the original historical observable, even if first.
     H=p[1]-p[0];phase=(h+1)%4;value=2*H+A[phase]
     assert value==M['record_threshold']==30
     r.update(reason='creator_entering_core_ties_original_U1_threshold',creator_height=H,creator_global_phase=phase,core_offset=A[phase],creator_entering_core_value=value,original_goal_threshold=M['record_threshold'])
    rows.append(r)
counts=dict(Counter(r['reason']for r in rows));assert counts==dict(wrong_sector=60,signed_rigid_pair_consumer_geometry_excluded=54,creator_entering_core_ties_original_U1_threshold=6)
D=[GP,RP,CY,W/'atomic_core_record_interface_frozen_20261023_1359/manifest.json',Path(__file__).resolve()]
R=dict(status='AUTHOR_ORIGINAL_U1_ALL_AGE_ORIGIN_EXCLUSION_PENDING_INDEPENDENT_AUDIT',scope='Original strict unfunded U1 event, goal U0,N/global phase1/threshold30. None of its five input identities can be an east-column output (2,0) or (2,1) of a genuine earlier U/UC/UCC full producer in the same complete recurrent-eight factor. Any legal such consumer must take both as lower a,q from source(-3,1,N), whose original entering core already ties30. No enlarged atomic history, input-age bound or initial-activation coefficient is needed. Other producer outputs and entry origins are not ruled out by this corollary. Original funding ledger remains11/13; no U1 closure or confinement.',counts=counts,all_120_output_to_goal_alignments=rows,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U1_east_pair_origin.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(counts,indent=2))
