from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
j=json.load(open(H/'hook_split.json'));flat=[r for c in j['foreign_cases']for r in c['all_colour_compatible_earliest_contact_owners_and_clock_routes']]
loss=[r for r in flat if r['hook_inputs']];assert len(loss)==16
openq=[r for r in loss if r['route']=='OPEN_Q_W5_hook_loss_funding'];assert len(openq)==1
r=openq[0];assert(r['foreign'],r['atom'],tuple(r['head']),r['h'],r['actual_outgoing_owner'])==('Q','U',(0,-1),3,'Qtail')
assert r['after_signed_hook_min4']==[5]and r['hook_inputs']==[[-1,-2]]
assert len([r for r in flat if r['route']=='FOREIGN_EXIT_contact_owned_by_b1_not_discarded'])==20
assert len(j['all5_genuine_FOREIGN_owned_W5_hook_MISS_tail_gates'])==5
routes=Counter(r['route']for r in loss);assert routes=={'excluded_by_piece_window_and_hook_min4':10,'excluded_by_signed_R39_R54_N4_guard':4,'excluded_by_signed_B_W5_hole':1,'OPEN_Q_W5_hook_loss_funding':1}
paths=['Q_B_foreign_first_contact_hook_split_2026-10-24/manifest.json','audits/check_Q_B_hook_owner_split_independent.json','foreign_Q_W5_deleted_core_guard_2026-10-24/manifest.json','audits/check_Q_W5_core_funding_independent.json']
out=dict(status='AUTHOR_DEPENDENCY_EXACT_Q_B_HOOK_LOSS_GLOBAL_FIRST_CONTACT_CLOSED_PENDING_REVIEW',scope='Only GLOBAL FIRST new contact owned by originalQ/B outgoing FORE pieces whose candidateRAW has a TRUE input among protected4SAMEhook IDs. All16 properFORE hookLOSS geometries nowclosed. Five complete-contextMISS tailgates and20 EXIT contacts ownedbyb1 stayoutside.',all16_original_foreign_hook_loss_geometries_and_routes=loss,Q_W5_status_change=dict(exact_old_record=openq[0],new_route='excluded_by_signed_d3f96db6_Q_hole_funding_under_SIMPLE_executed_prefix',no_first_Q_contact_only_weakening=True,no_V_target_C_predecessor_lift=True),still_open_five_hookMISS_tail_gates=j['all5_genuine_FOREIGN_owned_W5_hook_MISS_tail_gates'],still_separate_twenty_foreignEXIT_outgoing_b1_contacts=[r for r in flat if r['route']=='FOREIGN_EXIT_contact_owned_by_b1_not_discarded'],no_rewrite_of_original_ff80_status=True,no_arbitrary_tail_simplicity_or_secondFOREIGN_or_coverage_capture=True,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest()for p in paths})
(H/'hook_loss_closure_addendum.json').write_text(json.dumps(out,indent=2)+'\n');print('All16 proper outgoingQ/B hookLOSS firstcontact cases closed;5 hookMISS and20 b1-terminal contacts explicitlyremain separate.')
