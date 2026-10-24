"""Complete24-row max-three producer-cohort assembly and youngest-clock support.
Only finite literal placements and already signed dependency catalogues.
"""
from pathlib import Path
import json,hashlib,collections
W=Path(__file__).resolve().parent
paths=dict(geometry=W/'chronology_dcuv/literal_residual_geometry.json',shadow=W/'U_white_shadow_frozen_20261023_1709/02_U_white_shadow_retirement.json',older=W/'UC_older_four_simple_frozen_20261023_1733/02_UC_older_four_cohort_simple_exclusion.json',second=W/'U_second_shadow_frozen_20261023_1754/02_U_second_generation_white_shadow.json',minclock=W/'u1_minclock_cohort_frozen_20261023_1118/02_u_minimum_clock_cohort_by_phase.json',qresidue=W/'U_q_youngest_shadow_frozen_20261023_1717/02_U_q_youngest_shadow_corollary.json')
G=json.loads(paths['geometry'].read_text())['geometry'];S=json.loads(paths['shadow'].read_text());O=json.loads(paths['older'].read_text());T=json.loads(paths['second'].read_text());M=json.loads(paths['minclock'].read_text());Q=json.loads(paths['qresidue'].read_text());IDS=[0,1,4,5,6,7,8,9];P=[(-1,1),(-1,2),(-1,4),(0,2),(0,3)]
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
literal=[]
for a in IDS:
 for h in range(4):
  poses={(t[0]-rot(o,h)[0],t[1]-rot(o,h)[1])for t in P for o in G[a]['outputs']}
  for p in sorted(poses):
   if(sum(p)+h)%2:continue
   outputs={add(p,rot(o,h))for o in G[a]['outputs']};got=set(P)&outputs
   if len(got)>=4:literal.append(dict(source_packet=a,source_in_goal=[*p,h],goal_input_cohort=sorted(got)))
assert len(literal)==24 and all(len(r['goal_input_cohort'])==4 for r in literal)
L={(r['source_packet'],tuple(r['source_in_goal'])):r for r in literal};rows=[]
for t in S['four_cohort_templates']:
 a=t['source_packet'];dx,dy,dh=t['consumer_pose'];h=(-dh)%4;p=rot((-dx,-dy),h);key=a,(*p,h);assert key in L
 if t['previous_outcome']=='excluded_all_ages':reason='old_seven_all_age_exclusions'
 elif t['new_retirement_exclusion']:reason='twelve_first_generation_shadow_exclusions'
 elif a in[8,9]and(*p,h)==(1,5,2):
  assert any(z['packet']==a and z['head']==[1,5,2]for z in O['source_rows'])
  reason='two_source_U_entry_simple_suffix_exclusions'
 else:
  assert any(z['source']==a and z['source_pose']==[*p,h]and z['old_inventory_row']==t['signed_inventory_row']for z in T['three_remaining_four_cohort_cuts'])
  reason='three_second_generation_shadow_exclusions'
 rows.append(dict(**L[key],old_inventory_row=t['signed_inventory_row'],consumer_in_source=t['consumer_pose'],exclusion_dependency=reason))
assert len({(r['source_packet'],tuple(r['source_in_goal']))for r in rows})==24
counts=dict(collections.Counter(r['exclusion_dependency']for r in rows));assert counts==dict(old_seven_all_age_exclusions=7,twelve_first_generation_shadow_exclusions=12,two_source_U_entry_simple_suffix_exclusions=2,three_second_generation_shadow_exclusions=3)
# Existing all-age same-clock DAG, not a new age-by-age query.
phase_rows=[];older_masks=[]
for ph in M['phases']:
 h=ph['heading'];kept=[];pruned=[]
 for c in ph['completed_abstract_states']:
  r=c['last_producer'];pc=r['output_mask'].bit_count()
  if pc>=4:reason='max_three_global_producer_law'
  elif h==2:reason='signed_youngest_q_residue_two_law'
  else:reason=None
  q=dict(older_input_mask=c['older_input_mask'],youngest_input_mask=c['minimum_age_input_mask'],birth_packets=c['birth_packets'],last_source=r['packet'],last_pose=r['head'],last_output_mask=r['output_mask'])
  if reason:q['reason']=reason;pruned.append(q)
  else:
   # The surviving complementary masks are precisely STRICTLY older C births.
   assert c['older_input_mask']&16 and(c['older_input_mask']&28).bit_count()>=2
   kept.append(q)
 masks=sorted({c['older_input_mask']for c in kept});older_masks.append(masks);phase_rows.append(dict(heading=h,kept=kept,pruned=pruned,strictly_older_masks=masks))
assert older_masks==[[24,28],[20,28],[],[28]]
D=list(paths.values())+[W/p/'manifest.json'for p in['u_middle_origin_frozen_20261023_1013','U_white_shadow_frozen_20261023_1709','UC_older_four_simple_frozen_20261023_1733','U_second_shadow_frozen_20261023_1754','U_entry_simplicity_frozen_20261023_1616','u1_minclock_cohort_frozen_20261023_1118','U_q_youngest_shadow_frozen_20261023_1717']]+[Path(__file__).resolve()]
result=dict(status='AUTHOR_COMPLETE_DEPENDENCY_ASSEMBLY_PENDING_INDEPENDENT_AUDIT',scope='Actual complete recurrent-eight factors. Any U-family event consumes at most THREE current identities from one genuine full-packet producer. Different producers can share one historical component; entry identities are not one producer. Also youngest produced q has strictly older upper d and another upper support. No U count, record closure or capture.',literal_four_cohort_count=24,literal_five_cohort_count=0,exclusion_counts=counts,all24_exclusion_rows=rows,youngest_clock_support_by_phase=phase_rows,strictly_older_masks_by_phase=older_masks,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_max_three_producer_cohort.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(exclusion_counts=counts,older_masks=older_masks),indent=2))
