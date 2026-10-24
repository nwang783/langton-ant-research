"""Fourteen signed necessary D-parent rows are exhausted by signed local guards.
28 actual selected-D/DC typed roles retained. No later-return induction.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
JP=R/'returned_D_last_C_parent_reduction_2026-10-24/D_last_C_parent_reduction.json';EP=R/'F_same_target_C_cohort_lock_2026-10-24/F_C_cohort_lock.json';VP=R/'F_D15_V_rail_C_cohort_lock_2026-10-24/F_D15_V_cohort_lock.json';LP=R/'D15_long_D_run_local_gate_lift_2026-10-24/D15_local_gate_lift.json';BP=R/'seven_word_spatial_return_2026-10-23/D15_empty_D_older_bud_lifts.json'
J=json.loads(JP.read_text());E=json.loads(EP.read_text());V=json.loads(VP.read_text());L=json.loads(LP.read_text());B=json.loads(BP.read_text());rows=[];typed=[]
for f in J['fourteen_remaining_genuine_DC_VC_interfaces']:
 ix=f['catalogue_id'];parent=f['last_positive_C_full_packet'];word=f['actual_pre_D_zero_C_word'];cp=f['last_actual_C_entry']
 if ix==30:
  assert word in('D','DD');k=len(word);z=next(x for x in E['two_exact_older_C_cohort_interfaces']if x['k']==k)
  assert cp==[-k-1,-k,1] and z['foreign']==[3,-4,1]
  pp=next(p for p in z['actual_prior_DC_VC_choices']if p['full_packet']==parent);assert pp['entry']==f['packet_entry']
  why='ed14673e_direct_reader_independent_first_C_cohort_lock'
 elif word in('','D'):
  z=[x for x in B['eight_explicit_actual_typed_premise_lifts']if x['last_positive_C_parent']==parent and x['actual_pre_D_zero_C_word']==word]
  assert len(z)==2 and{x['actual_full_source']for x in z}=={'D','DC'}
  why='aa285e60_genuine_older_bud_WHITE_and_actual_past_chord_lift'
 elif word in('DD','DDD'):
  z=next(x for x in L['four_exact_history_preserving_local_gate_lifts']if x['actual_last_positive_C_parent']==parent and x['old_N_run']==word)
  assert z['literal_word_replacement']is False and z['full_history_changed']is False
  why='372a183d_actual_earlier_plainD_local_gate_lift_no_contact_relabel'
 else:
  assert word=='V';z=V['exact_older_C_V_rail_cohort_interface'][0];assert z['actual_following_N_run']=='V'and z['foreign']==[2,-5,1]
  pp=next(p for p in z['actual_prior_DC_VC_choices']if p['full_packet']==parent);assert pp['entry']==f['packet_entry'] and cp==[-2,-3,1]
  why='d005eb49_genuine_first_C_T_Q_current_lock_after_singleV'
 rows.append(dict(catalogue_id=ix,last_positive_C_parent=parent,actual_pre_selectedD_N_word=word,actual_parent_entry=f['packet_entry'],actual_final_C_entry=cp,exclusion=why,actual_outgoing_contact_owner='original selectedD remains unchanged',scope='this necessary interface is excluded; no word/head/clock/identity history replacement'))
 for full in('D','DC'):typed.append(dict(catalogue_id=ix,last_positive_C_parent=parent,actual_pre_selectedD_N_word=word,actual_selected_full_packet=full,exclusion=why,guard_applies_before_F_and_preserves_actual_own_tail=full=='DC'))
assert len(rows)==14 and len(typed)==28
counts=Counter(x['exclusion']for x in rows);assert sorted(counts.values())==[2,4,4,4]
D=[JP,EP,VP,LP,BP,R/'returned_D_last_C_parent_reduction_2026-10-24/manifest.json',R/'F_same_target_C_cohort_lock_2026-10-24/manifest.json',R/'F_D15_V_rail_C_cohort_lock_2026-10-24/manifest.json',R/'D15_long_D_run_local_gate_lift_2026-10-24/manifest.json',R/'seven_word_spatial_return_2026-10-23/D15_empty_D_older_bud_lifts_manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_FINAL_COMPOSITION_PENDING_INDEPENDENT_REVIEW_ALL_COMPONENTS_SIGNED',scope='All14 genuine necessary last-positive-C parent interfaces of D15/D30 are excluded, including28 actual selectedD/DC roles. Thus neither remaining old outgoing-D first-returned-contact coarse geometry is possible under the stated U-entry old8/firstforeign/immediateordinary premise. No later-return, secondforeign or universal seven-word extension.',all14_excluded_parent_run_rows=rows,all28_actual_selected_source_D_DC_roles=typed,classification_counts=dict(counts),contact_ownership_NOT_changed=True,postforeign_maturity_NOT_used=True,recursive_ancestry_induction_NOT_used=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'D_final_parent_exhaustion.json').write_text(json.dumps(o,indent=2)+'\n');print('All14 genuine D15/D30 parent rows and28 typed sourceD/DC roles exhausted; all component guards signed.')
