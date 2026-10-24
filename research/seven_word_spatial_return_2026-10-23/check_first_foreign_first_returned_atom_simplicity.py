"""Complete371-label geometric/source join, with actual-path implication.

The finite catalogue is a necessary interface, not a realized history list.
Its exhaustive signed exclusions imply no chronological first new contact.
Nothing is iterated past this one returned ordinary atom.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
cat=json.loads((H/'first_returned_atom_contact.json').read_text())
three=json.loads((H/'first_returned_three_F_frontier.json').read_text())
D=json.loads((R/'returned_D_final_parent_exhaustion_2026-10-24/D_final_parent_exhaustion.json').read_text())
oldD=json.loads((R/'returned_D_last_C_parent_reduction_2026-10-24/D_last_C_parent_reduction.json').read_text())
normal=json.loads((H/'Q_B_old_C_common_normal_guard.json').read_text())
C0=json.loads((H/'C75_immediate_DC_VC_ancestor_bud.json').read_text())
labels=cat['old_source_contact_cases']
assert len(labels)==371
assert Counter(q['source_atom']for q in labels)=={'D':60,'C':51,'V':112,'U':148}
assert [q['catalogue_case']for q in three['three_necessary_labels_with_actual_containing_roles']]==[15,30,75]
assert all(labels[i]['source_atom']==a for i,a in((15,'D'),(30,'D'),(75,'C'),(76,'C'),(77,'C')))
assert all(labels[i]['foreign']==a for i,a in((15,'F'),(30,'F'),(75,'F'),(76,'Q'),(77,'B')))

# Exact exhausted D boundary, preserving actual outgoing owner and source type.
necessaryD={(q['catalogue_id'],q['last_positive_C_full_packet'],q['actual_pre_D_zero_C_word'])for q in oldD['fourteen_remaining_genuine_DC_VC_interfaces']}
closedD={(q['catalogue_id'],q['last_positive_C_parent'],q['actual_pre_selectedD_N_word'])for q in D['all14_excluded_parent_run_rows']}
assert necessaryD==closedD and len(closedD)==14
assert Counter(q[0]for q in closedD)=={15:10,30:4}
assert len(D['all28_actual_selected_source_D_DC_roles'])==28
assert D['contact_ownership_NOT_changed']and D['postforeign_maturity_NOT_used']
assert Counter(q['exclusion']for q in D['all14_excluded_parent_run_rows'])==D['classification_counts']

# All6 C75 predecessor rows are exhausted; sourceDC/C1 typing is retained.
Cparents=three['signed_C75_last_positive_C_parent_interfaces']
assert {(q['last_positive_C_fullpacket'],q['intervening_plain_D_count'])for q in Cparents}=={(a,k)for a in('DC','VC')for k in range(3)}
closedC=[]
for q in Cparents:
    k=q['intervening_plain_D_count'];parent=q['last_positive_C_fullpacket']
    assert parent in('DC','VC')
    dep='849d3404_actual_older_bud_and_past_chord_guard'if k==0 else'ed14673e_reader_independent_first_C_current_cohort_lock'
    closedC.append(dict(actual_parent=parent,intervening_plain_D_count=k,exclusion=dep))
assert len(closedC)==6 and Counter(q['exclusion']for q in closedC)=={'849d3404_actual_older_bud_and_past_chord_guard':2,'ed14673e_reader_independent_first_C_current_cohort_lock':4}
assert len(C0['four_surviving_DC_V_VC_inputs'])==4
assert normal['C76_and_C77_excluded_for_all_real_containing_source_roles']

closed=[]
for i,q in enumerate(labels):
    a=q['source_atom']
    if i in(15,30):dep='bd138da4_all14_D_parent_rows_and28_D_DC_roles_exhausted'
    elif i==75:dep='all6_real_DC_C1_parent_rows_exhausted_849d_and_ed146'
    elif i in(76,77):dep='fd25e1ae_target_level_old_C_common_normal_guard_all7_source_roles'
    elif a=='D':dep='bdb22f14_original58_D_source_exclusions'
    elif a=='C':dep='c268e9e4_original48_C_source_exclusions'
    elif a=='V':dep='c93013e2_all112_V_source_exclusion_join'
    else:
        assert a=='U';dep='13e9c2ce_all148_U_source_exclusion_join'
    closed.append(dict(catalogue_id=i,source_atom=a,foreign=q['foreign'],returned_atom=q['returned_atom'],exclusion=dep))
assert len(closed)==371
local=cat['local_foreign_returned_atom_cases'];assert len(local)==12
assert all(not q['new_contacts']for q in local)

# Component manifests and independent reports, all immutable. The final
# composition is what this new source/geometric join asks the auditor to check.
paths=[
 H/'first_foreign_all_source_join_manifest.json',R/'audits/check_first_foreign_all_source_join_independent.json',
 H/'first_returned_atom_contact_manifest.json',R/'audits/check_first_returned_atom_contact_independent.json',
 H/'first_returned_three_F_frontier_manifest.json',H/'three_F_parent_assembly_signoff_manifest.json',
 R/'audits/check_first_returned_three_F_frontier_independent.json',
 R/'returned_D_final_parent_exhaustion_2026-10-24/manifest.json',
 R/'audits/check_D15_remaining_cohort_and_bud_lifts_independent.json',
 H/'Q_B_old_C_common_normal_guard_manifest.json',R/'audits/check_Q_B_old_C_common_normal_guard_independent.json',
 H/'C75_immediate_DC_VC_ancestor_bud_manifest.json',R/'audits/check_C75_immediate_ancestor_bud_independent.json',
 R/'F_same_target_C_cohort_lock_2026-10-24/manifest.json',R/'audits/check_F_first_C_cohort_lock_independent.json',
 H/'D15_empty_D_older_bud_lifts_manifest.json',R/'D15_long_D_run_local_gate_lift_2026-10-24/manifest.json',
 R/'F_D15_V_rail_C_cohort_lock_2026-10-24/manifest.json',
 H/'foreign_kinked_barrier_manifest.json',H/'complete8_foreign_adjacency_manifest.json',
 H/'ordered_W_marker_ownership_erratum_manifest.json',H/'ordered_W_U_role_label_erratum_manifest.json',
 H/'ordered_W_seal_withdrawal_controls_manifest.json',H/'ordered_W_portal_submatching_manifest.json',
 H/'V_rail_forced_reverse_block_manifest.json',H/'V_rail_no_further_C_scope_clarification_manifest.json',
 H/'returned_C_prepared_loop_control_manifest.json',
 R/'returned_D_clock3_controls_2026-10-24/manifest.json',
 R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
# Keep exact retained filenames; do not fabricate a report if unavailable.
for i,p in enumerate(paths):
    if not p.exists()and 'check_first_foreign_all_source_join_independent' in p.name:
        cand=list((R/'audits').glob('*first_foreign*all*source*independent.json'));assert len(cand)==1;paths[i]=cand[0]
    if not p.exists()and 'check_first_returned_atom_contact_independent' in p.name:
        cand=list((R/'audits').glob('*first_returned_atom*independent.json'));assert len(cand)==1;paths[i]=cand[0]
assert all(p.exists()for p in paths),[str(p)for p in paths if not p.exists()]
out=dict(status='AUTHOR_FROZEN_ALL371_FIRST_RETURNED_CONTACT_EXCLUSIONS_AND_PROXY_SIMPLICITY_PENDING_FINAL_REVIEW',
    exact_history_scope=dict(old_packets='Finite sequence of complete G8 D/DC/V/VC/VCC/U/UC/UCC packets; first packet U/UC/UCC.',
        first_foreign='One actual complete F/Q/B RAW with genuine actual context.',
        next_atom='Exactly its immediately following actual RAW D/C/V/U plus verified actual nextM11 prefix.',
        full_physical_field_and_cursor_retained=True,internal_C_and_F56_cuts_not_marked_cores=True,
        no_arbitrary_seven_word_coverage_assumed=True),
    original_disjoint_source_counts=dict(D=60,C=51,V=112,U=148),
    all371_necessary_labels_excluded=closed,
    D14_necessary_parent_run_set_equals_excluded_set=True,D28_actual_full_source_roles_retained=True,
    all6_C75_actual_DC_C1_parent_rows_excluded=closedC,
    all12_foreign_returned_local_pairs_have_only_true_terminal_adjacency=True,
    geometric_implication_steps=[
        'The signed U-entry old8 theorem and firstforeign375-label join make the prefix through this firstforeign simple.',
        'The immediate returned ordinary chord is simple itself and meets foreignpieces only at genuine terminal adjacency; harmless Q-to-U collinear continuation is not overlap.',
        'If a new old-prefix contact existed, finiteness and the already-simple prefix give a chronological first positive one.',
        'Outgoing old-vertex ownership, old terminal ownership by the foreign and exact parallel-onset rules put this contact in the signed371-label catalogue with0<=n<=4.',
        'Every one of those371 necessary labels is excluded by genuine original histories, producer clocks, before-color guards and unchanged contact ownership.',
        'Therefore no such first contact exists, and the actual geometric proxy extends injectively through exactly this one returned ordinary atom.'],
    conclusion='The ordinary corrected-center plus true F/Q/B piece proxy is a simple open arc through the first foreign and exactly its immediately following actual ordinary RAW atom.',
    does_NOT_conclude=['Fine ant path is selfavoiding','First returned complete packet including laterCtails is simple','Second ordinary atom is covered','Secondforeign is covered','RepeatedF expenditure is bounded','Every ant enters this packet language','Global stabilization or standard104 capture'],
    controls_and_rejected_claim_record=[
        'Actual prepared D/DC-entry loops remain legal but fail the required U-entry ancestry or old-prefix simplicity.',
        '849d genuine older-bud clearing controls remain legal; both have an explicit earlier parentD/helperV crossing.',
        'Source-free rawCforeign words can be legal;735023be is only an actual complete-packet adjacency theorem.',
        'Full-output seal6ea48d5 stays WITHDRAWN/NOT_PASSED; genuine14/16black U-entry controls and17black forced-V continuation remain positive.',
        'Only corrected23f62a2c matching with mandatory ownership/U-role errata is used. No at-most-one or finite-boundary quotient is imported.'],
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'first_foreign_first_returned_atom_simplicity.json').write_text(json.dumps(out,indent=2)+'\n')
print('371/371 exact necessary old-source labels excluded;D14/C6 parent exhaustion checked.')
print('Together prefix simplicity +12 local foreign pairs ->actual proxy simple through ONE returned atom only.')
