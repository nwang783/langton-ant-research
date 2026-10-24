"""All-age global four-input producer structure and record funding corollaries.
Dependency-bound finite assembly, not a language or reachability search.
"""
from pathlib import Path
import json,hashlib,collections
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';SP=W/'U_white_shadow_frozen_20261023_1709/02_U_white_shadow_retirement.json';CP=W/'UC_older_four_simple_frozen_20261023_1733/02_UC_older_four_cohort_simple_exclusion.json';AP=W/'atomic_core_record_interface_frozen_20261023_1359/02_atomic_core_record_interface.json'
G=json.loads(GP.read_text())['geometry'];S=json.loads(SP.read_text());C=json.loads(CP.read_text());A=json.loads(AP.read_text());P={(-1,1),(-1,2),(-1,4),(0,2),(0,3)};b=(-1,4)
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
rows=[]
for t in S['four_cohort_templates']:
 a=t['source_packet'];dx,dy,dh=t['consumer_pose'];h=(-dh)%4;p=rot((-dx,-dy),h)
 O={add(p,rot(o,h))for o in G[a]['outputs']};got=P&O;assert len(got)==4
 if t['previous_outcome']=='excluded_all_ages':out='signed_old_all_age_exclusion'
 elif t['new_retirement_exclusion']:out='signed_white_shadow_exclusion'
 elif(a in[8,9]and(*p,h)==(1,5,2)):
  # The SOURCE itself is U-family, hence its complete source-to-goal suffix is simple.
  assert any(r['packet']==a and r['head']==[1,5,2]for r in C['source_rows'])
  out='signed_source_U_entry_simplicity_exclusion'
 else:
  assert(*p,h)==(-1,1,0)and got==P-{b};out='only_remaining_four_cohort_structure'
 rows.append(dict(source_packet=a,consumer_pose=t['consumer_pose'],source_in_goal_coordinates=[*p,h],co_born_goal_inputs=sorted(got),classification=out))
cnt=dict(collections.Counter(r['classification']for r in rows));assert cnt==dict(signed_old_all_age_exclusion=7,signed_white_shadow_exclusion=12,signed_source_U_entry_simplicity_exclusion=2,only_remaining_four_cohort_structure=3)
remaining=[r for r in rows if r['classification']=='only_remaining_four_cohort_structure']
assert{r['source_packet']for r in remaining}=={7,8,9}
for a in[7,8,9]:
 p=(-1,1);O={add(p,tuple(o))for o in G[a]['outputs']};I={add(p,tuple(o))for o in G[a]['inputs']}
 assert P-{b}<=O and b in I and b not in O
assert G[7]['endpoint']==[0,4,0]
assert all(o[1]>=0 for a in[0,1,4,5,6,7,8,9]for o in G[a]['outputs'])
assert all(G[a]['endpoint'][1]>0 and G[a]['endpoint'][2]==0 for a in[0,4,7])
# For plain U, all same-C-clock future producer starts are N and have y>=5;
# nonnegative literal output y prevents b at y4. C tails only postpone clocks.
record=[]
for a in[7,8,9]:
 row=next(r for r in A['rows']if r['packet']==a and r['global_phase']==1)
 entry=row['entry_core']+4;old=row['old_peak']+4;atomic=row['atomic_exits'][0]['core_value']+4
 assert entry==26 and atomic==34
 record.append(dict(source=a,source_pose=[-1,1,0],original_entry_core=entry,original_created_peak=old,earlier_atomic_U_base_exit=[-1,5,0],earlier_atomic_core=atomic,goal_U1_threshold=30,funded_in_original_history=max(entry,old)>=30,funded_in_enlarged_atomic_history=atomic>=30))
assert[r['original_created_peak']for r in record]==[34,14,26]
assert[r['funded_in_original_history']for r in record]==[True,False,False]
assert all(r['funded_in_enlarged_atomic_history']for r in record)
D=[GP,SP,CP,AP,W/'u_middle_origin_frozen_20261023_1013/manifest.json',W/'U_white_shadow_frozen_20261023_1709/manifest.json',W/'UC_older_four_simple_frozen_20261023_1733/manifest.json',W/'U_entry_simplicity_frozen_20261023_1616/manifest.json',W/'atomic_core_record_interface_frozen_20261023_1359/manifest.json',Path(__file__).resolve()]
O=dict(status='AUTHOR_GLOBAL_FOUR_COHORT_STRUCTURE_PENDING_INDEPENDENT_AUDIT',scope='Actual complete recurrent-eight factors. Any four-input producer cohort is one of three U-family shapes and requires a strictly later-C b birth. Thus q-youngest has no four-cohort. Enlarged strict U1 has no four-cohort by atomic core34. No component, total-U or capture bound.',counts=cnt,all24templates=rows,remaining_structure=remaining,strict_b_birth_clock_proof=dict(plain_U_exit=[-1,5,0],target_b=[-1,4],all_literal_outputs_have_nonnegative_local_y=True,zero_C_N_endpoints_strictly_increase_y=True,C_tails_postpone_future_full_source_births=True),record_funding_rows=record,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_four_cohort_global_structure.json').write_text(json.dumps(O,indent=2)+'\n');print(json.dumps(dict(counts=cnt,record=record),indent=2))
