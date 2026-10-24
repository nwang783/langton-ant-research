"""Three-F source/parent/core-mechanism dependency join.

No frozen older catalogue or source proof is edited. Exact D gate source799c
is cited, not independently re-enumerated; its audit report and reader-independent C75 lift are bound explicitly.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
old=json.loads((H/'first_returned_five_label_frontier.json').read_text())
cat=json.loads((H/'first_returned_atom_contact.json').read_text())
normal=json.loads((H/'Q_B_old_C_common_normal_guard.json').read_text())
rows=old['all_five_necessary_labels_with_actual_fullsource_roles']
assert [q['catalogue_case']for q in rows]==[15,30,75,76,77]
assert normal['C76_and_C77_excluded_for_all_real_containing_source_roles']
remaining=[q for q in rows if q['catalogue_case']not in(76,77)]
assert [q['catalogue_case']for q in remaining]==[15,30,75]
assert all(q['foreign']=='F'and q['source_to_foreign_C_age']==3 for q in remaining)
assert Counter(q['source_atom']for q in cat['old_source_contact_cases'])=={'D':60,'C':51,'V':112,'U':148}
counts=dict(D=58,C=50,V=112,U=148)
assert sum(counts.values())==368 and len(cat['old_source_contact_cases'])==371
assert [q['full_packet']for q in remaining[0]['remaining_actual_containing_fullsource_roles']]==['D','DC']
assert [q['full_packet']for q in remaining[1]['remaining_actual_containing_fullsource_roles']]==['D','DC']
assert [q['full_packet']for q in remaining[2]['remaining_actual_containing_fullsource_roles']]==['DC']

height=json.loads((H/'DC_C1_prefix_height_horizon.json').read_text())
support=json.loads((H/'DC_C1_UC_support_separator.json').read_text())
cparents=[q for q in height['all21_remaining_necessary_last_C_parent_rows']
          if q['foreign']=='F'and q['last_positive_C_fullpacket']in('DC','VC')]
assert len(cparents)==6
assert all(q['intervening_plain_D_count']in(0,1,2)for q in cparents)
assert sum(q['foreign']=='F'for q in support['four_excluded_UC_parent_interfaces'])==2

# Gate values are copied from the worker-owned immutable source and its
# independent C75 lift. No duplicate F mask enumeration is introduced here.
GatePath=R/'returned_D_forced_core_ports_2026-10-24/D_forced_core_ports.json'
GateManifest=GatePath.with_name('manifest.json')
gate=json.loads(GatePath.read_text())
GateAudit=R/'audits/check_returned_D_forced_core_ports_independent.json'
gaudit=json.loads(GateAudit.read_text());assert gaudit['status'].startswith('PASS')
assert [q['case']for q in gaudit['two_submitted_and_one_compatible_C75_port_transcript']]==[15,30,75]
DP=R/'returned_D_last_C_parent_reduction_2026-10-24/D_last_C_parent_reduction.json'
DManifest=DP.with_name('manifest.json');dj=json.loads(DP.read_text())
dparents=dj['fourteen_remaining_genuine_DC_VC_interfaces']
assert len(dj['all40_actual_last_positive_C_interfaces'])==40 and len(dparents)==14
assert Counter(q['catalogue_id']for q in dparents)=={15:10,30:4}
assert {(q['catalogue_id'],q['last_positive_C_full_packet'],q['actual_pre_D_zero_C_word'])for q in dparents}=={(case,parent,word)for case,words in((15,('','D','DD','DDD','V')),(30,('D','DD')))for parent in('DC','VC')for word in words}

g15,g30=gate['two_forced_core_reset_interfaces']
assert (g15['catalogue_id'],g30['catalogue_id'])==(15,30)
assert g30['foreign_pose']==[3,-4,1]and g30['genuine_old_raw_input']==[2,0]
assert g30['core_black_rewrite']['is_F_exit_core']and not g30['core_black_rewrite']['is_fresh_F_residual_output']
c75=dict(catalogue_case=75,old_actual_full_source='DC',
    actual_old_C1_in_creating_D_frame=(1,1,0),
    atomic_C1_and_full_DC_entry_C_clocks_identical=True,
    foreign_in_old_C_frame=(2,-5,1),foreign_in_creating_D_frame=(3,-4,1),
    returned_RAW_C_in_creating_D_frame=(1,0,3),
    old_common_D_birth_site=(2,0),genuine_D_RAW_birth_tick0=8,
    worker_gate_lemma_used='D30 F3,-4E original-D-bud currentness; independent of returned atom/contact owner',
    exact_literal_RAW_core_reset=dict(g30['original_residual_retirement']),
    exact_literal_new_black_core_write=dict(g30['core_black_rewrite']),
    replacement_core_physical_deletion=dict(owner='immediately following actual RAW C',
        owner_tick0=3,owner_read_number1=4,combined_tick0=59),
    no_original_identity_survival_through_F=True,
    mechanism_audit_status='Independent PASS799c0027 explicitly includes this reader-independent C75 lift.')

signed_deps=[H/'first_returned_five_label_frontier_manifest.json',
    H/'Q_B_old_C_common_normal_guard_manifest.json',
    R/'audits/check_Q_B_old_C_common_normal_guard_independent.json',
    H/'DC_C1_prefix_height_horizon_manifest.json',H/'DC_C1_UC_support_separator_manifest.json',
    R/'audits/check_DC_C1_Jordan_ancestry_horizon_independent.json',
    R/'audits/check_DC_C1_UC_support_separator_independent.json',
    GateManifest,GatePath,GateAudit]
assert all(p.exists()for p in signed_deps)
out=dict(status='SIGNED_COARSE_AND_CORE_GATE_JOIN_D_PARENT_ASSEMBLY_REVIEW_PENDING',
    scope='Chronological FIRST returned ordinary-atom contact after one first foreign only. Coarse labels15/30/75, not attainment, exclusion of F, returned simplicity or secondforeign induction.',
    original_disjoint_source_counts=dict(D=60,C=51,V=112,U=148),
    signed_excluded_source_counts=counts,
    remaining_catalogue_IDs=(15,30,75),
    three_necessary_labels_with_actual_containing_roles=remaining,
    signed_C75_last_positive_C_parent_interfaces=cparents,
    D_last_positive_C_parent_assembly_status='All component guards signed; worker40-to14 assembly review pending.',
    fourteen_worker_D_last_positive_C_parent_interfaces=dparents,
    total_parent_run_interfaces=20,
    C75_parent_restriction_limit='Only prior DC/VC then D^k,k0..2. Arbitrary history before that parent and all later stages remain unbounded.',
    worker_owned_two_D_gate_source_status='Independent PASS799c0027 with explicit C75 lift',
    worker_owned_two_D_gate_interfaces=gate['two_forced_core_reset_interfaces'],
    explicit_signed_C75_same_F_gate_premise_lift=c75,
    mechanism_is_not_budget=True,
    original_identity_and_new_core_R_identity_are_distinct=True,
    beta_ancestry_clarification='In actual U-entry history selected D is noninitial: incoming beta is a genuine immediately preceding atomic exit-bud. Only source-free DC-entry controls may treat it as arbitrary initial support.',
    signed_dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in signed_deps},
    separate_D_parent_assembly_dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(DManifest,DP)})
(H/'first_returned_three_F_frontier.json').write_text(json.dumps(out,indent=2)+'\n')
print('371 labels split368 excluded +3 necessaryF cases15/30/75;source roles D/DC,D/DC,DC.')
print('C75 signed6 parent rows;workerD40-to14 assembly review pending;F core mechanism independently PASS799c.')
