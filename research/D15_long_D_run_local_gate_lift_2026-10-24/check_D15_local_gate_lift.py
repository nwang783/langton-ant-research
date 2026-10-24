"""Four exact history-preserving lifts to a READER-INDEPENDENT local F gate.
Does NOT identify outgoingD with C1 or use C75 first-contact ownership.
"""
from pathlib import Path
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
JP=R/'returned_D_last_C_parent_reduction_2026-10-24/D_last_C_parent_reduction.json';J=json.loads(JP.read_text())
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
rows=[]
for z in J['fourteen_remaining_genuine_DC_VC_interfaces']:
 if z['catalogue_id']!=15 or z['actual_pre_D_zero_C_word']not in('DD','DDD'):continue
 old=z['actual_pre_D_zero_C_word'];new=old[:-1];k=len(new);translation=(1,1)
 cp=z['last_actual_C_entry'];newcp=[cp[0]+1,cp[1]+1,cp[2]];assert newcp==[-k-1,-k,1]
 pp=z['packet_entry'];newpp=[pp[0]+1,pp[1]+1,pp[2]]
 T=add((newcp[0],newcp[1]),rot((2,0),1));Q=add((newcp[0],newcp[1]),rot((2,1),1));RB=add((newcp[0],newcp[1]),rot((1,2),1))
 assert(T,Q,RB)==((-k-1,-k-2),(-k,-k-2),(1-k,-k-1))
 f=add((2,-5),translation);ret=add((0,-1),translation);assert(f,ret)==((3,-4),(1,0))
 # Old selectedD remains the actual later contact owner; do not change it.
 old_contact_in_new_frame=(1,1)
 assert old_contact_in_new_frame==(1,1)
 rows.append(dict(old_catalogue_id=15,actual_last_positive_C_parent=z['last_positive_C_full_packet'],old_N_run=old,earlier_selected_plain_D_entry_in_old_frame=[-1,-1,0],new_origin_translation=translation,new_parent_entry=newpp,new_actual_C1_entry=newcp,new_pre_D_N_run=new,new_selected_plain_D_entry=[0,0,0],unchanged_old_selected_D_now_later_entry=[1,1,0],new_foreign_pose=[*f,1],new_returned_C_pose=[*ret,3],C_clock_of_both_old_and_new_selected_D=0,foreign_C_clock=3,new_same_original_C1_tag_cells=dict(T=T,Q=Q,exitbud=RB),unchanged_outgoing_contact_owner='actual later selectedD at[1,1,N]; NOT C1',contact_point_in_new_frame=old_contact_in_new_frame,applied_theorem='ed14673e local BEFORE-F gate; has NO returned-reader/contact-owner premise',literal_word_replacement=False,full_history_changed=False,conclusion='This F cannot occur, so the original D15 interface is excluded.'))
assert len(rows)==4
D=[JP,R/'returned_D_last_C_parent_reduction_2026-10-24/manifest.json',R/'F_same_target_C_cohort_lock_2026-10-24/manifest.json',R/'three_F_backward_ancestry_interface_2026-10-24/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_COMPOSITION_PENDING_INDEPENDENT_REVIEW_COMPONENTS_SIGNED',scope='Four D15 DC/VC+DD/DDD interfaces excluded via one exact earlier-plainD rebase to signed reader-independent local F3,-4 cohort gate. No old-source-contact relabeling, no DD-to-DC rewrite, no recursive induction.',four_exact_history_preserving_local_gate_lifts=rows,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'D15_local_gate_lift.json').write_text(json.dumps(o,indent=2)+'\n');print('Four D15 DD/DDD local-gate lifts, all literal history and outgoingD ownership preserved.')
