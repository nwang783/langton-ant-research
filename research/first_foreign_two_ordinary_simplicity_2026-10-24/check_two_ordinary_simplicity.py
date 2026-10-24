"""Dependency-complete finite-to-geometric TWO ordinary RAW assembly.

No new trajectory search. Original217 angle IDs and every final D/C role key
are compared directly. Actual final-M ownership and local closed-segment
interfaces are reconstructed from the literal words.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import hashlib
import importlib.util
import json

ROOT=Path('/workspace/shared/langton')
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('lit',ROOT/'word_stabilization/check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(spec)
spec.loader.exec_module(lit)
spec=importlib.util.spec_from_file_location('owner',ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner=importlib.util.module_from_spec(spec)
spec.loader.exec_module(owner)
W=owner.WORDS
SMALL=ROOT/'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry.json'
CURRENT=ROOT/'second_contact_signed_obligations_2026-10-24/signed_current_obligations.json'
C3=ROOT/'second_old_C_age3_2026-10-24/C_age3_source_reserve.json'
D3=ROOT/'old_D_second_age3_next_base_2026-10-24/next_base_guard.json'
small=json.loads(SMALL.read_text())
current=json.loads(CURRENT.read_text())
c3=json.loads(C3.read_text())
d3=json.loads(D3.read_text())
angles=small['conditional217_old_source_angle_interfaces']


def add(p,q): return p[0]+q[0],p[1]+q[1]
def sub(p,q): return p[0]-q[0],p[1]-q[1]
def det(p,q): return p[0]*q[1]-p[1]*q[0]


def after(word,pose=(0,0,0)):
    p,h=pose[:2],pose[2]
    for turn in word:
        h=(h+(1 if turn=='R' else -1))%4
        p=add(p,lit.DIRS[h])
    return *p,h


def z2(pose): return add((2*pose[0],2*pose[1]),lit.rot((-1,-1),pose[2]))
def chord(atom,pose): return z2(pose),z2(after(W[atom],pose))


def hit(a,b,c,d):
    u,v,z=sub(b,a),sub(d,c),sub(c,a)
    den=det(u,v)
    if den:
        s,t=Q(det(z,v),den),Q(det(z,u),den)
        return dict(kind='point',old_s=s,new_t=t) if 0<=s<=1 and 0<=t<=1 else None
    if det(z,u): return None
    k=0 if u[0] else 1
    lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
    lo,hi=max(Q(0),lo),min(Q(1),hi)
    return dict(kind='collinear',old_s_interval=(lo,hi)) if lo<=hi else None


# Direct literal local proof in all four orientations. The foreign pieces
# use only the actual F56 fine cut, never an internal marked core.
local=[]
for heading in range(4):
    for A in 'FQB':
        entry=(0,0,heading)
        fcut=after(W['F'],entry)
        end=after(W[A],entry)
        vertices=[z2(entry),z2(fcut)]
        if A!='F': vertices.append(z2(end))
        pieces=list(zip(vertices,vertices[1:]))
        for b1 in 'DCVU':
            first=chord(b1,end)
            p2=after(W[b1],end)
            for b2 in 'DCVU':
                second=chord(b2,p2)
                assert all(hit(*p,*second) is None for p in pieces)
                adjacent=hit(*first,*second)
                assert (adjacent==dict(kind='point',old_s=Q(1),new_t=Q(0))
                        or adjacent==dict(kind='collinear',old_s_interval=(Q(1),Q(1))))
                assert first[1]==second[0]
                local.append(dict(foreign=A,first=b1,second=b2,actual_heading=heading,
                    true_foreign_piece_vertices=vertices,first_chord=first,second_chord=second,
                    second_misses_FOREIGN_and_meets_b1_only_at_actual_adjacency=True))
assert len(local)==192

# b2+actual finalM supplies b1's ACTUAL next marker even for D10. No marker
# is inserted into the physical history and M11 is executed only once.
marker_supply=[]
for b1 in 'DCVU':
    for b2 in 'DCVU':
        assert (W[b2]+lit.M)[:len(lit.M)]==lit.M
        assert (W[b1]+W[b2]+lit.M)[:len(lit.M)]==lit.M
        marker_supply.append(dict(first=b1,second=b2,
            b1_context_marker_comes_from_actual_b2_plus_if_needed_actual_next_word=True,
            actual_b2_RAW_reads_used=min(len(W[b2]),len(lit.M)),
            actual_final_M_reads_used=max(0,len(lit.M)-len(W[b2]))))
assert len(marker_supply)==16

# The last preforeign full packet is plain V/U by signed735. The four
# possible closed-segment second contacts with that immediate old base are
# actual immutable contradictions; no such source is omitted from angles.
last=[]
for row in small['four_possible_immediate_old_base_contacts_all_literal_conflicting']:
    tokens=(row['immediate_old_plain_base']+row['foreign']+
            row['first_ordinary']+row['second_ordinary'])
    trace=lit.trace(''.join(W[a] for a in tokens)+lit.M)
    assert not trace['feasible']
    old=row['immutable_whole_context_conflict']
    assert (trace['cell'],trace['conflict_read'],trace['previous_read'])==(
        old['cell'],old['conflict_read'],old['previous_read'])
    last.append(dict(actual_tokens=list(tokens),immutable_conflict=trace))
assert len(last)==4


def angle_key(a):
    return a['old_source'],a['first_ordinary'],a['second_ordinary'],a['actual_old_source_to_FOREIGN_C_age']


def contact_key(r):
    # These are physical poses and literal letters, not implicit row IDs.
    return r['foreign'],r['first'],r['second'],tuple(r['foreign_pose']),tuple(r['second_pose'])


# Every original angle ID is explicit and duplicate-free. U/V/C/D source
# lemmas are assigned by TRUE preforeign age, not returned effectiveN.
source_proofs={
    ('D',0):'zero_preforeign_C_old_DV_slice_manifest.json',
    ('D',1):'second_old_D_age1_2026-10-24/manifest.json',
    ('D',2):'second_old_sources_age2_bud_2026-10-24/manifest.json',
    ('D',3):'old_D_second_age3_next_base_2026-10-24/manifest.json',
    ('C',1):'second_old_C_age1_2026-10-24/manifest.json',
    ('C',2):'second_old_sources_age2_bud_2026-10-24/manifest.json',
    ('C',3):'second_old_C_age3_2026-10-24/manifest.json',
    ('V',0):'zero_preforeign_C_old_DV_slice_manifest.json',
    ('V',1):'old_V_second_contact_age1_2026-10-24/manifest.json + mandatory b664 scope',
    ('V',2):'second_old_sources_age2_bud_2026-10-24/manifest.json + old_V_age2_common_port_guard',
    ('V',3):'old_V_second_age3_2026-10-24/manifest.json',
    ('V',4):'second_contact_signed_obligations_2026-10-24/manifest.json + mandatory389 physical CORE qualification'}
angle_records=[]
assert len({angle_key(a) for a in angles})==217
for index,angle in enumerate(angles):
    old,n=angle['old_source'],angle['actual_old_source_to_FOREIGN_C_age']
    proof=('old_U_second_source_closure_manifest.json' if old=='U' else source_proofs[old,n])
    angle_records.append(dict(original217_angle_index0=index,exact_original_angle=angle,
        source_exclusion=proof,classification='signed_source_slice_excluded'))
assert Counter(r['exact_original_angle']['old_source'] for r in angle_records)=={'D':54,'C':44,'V':59,'U':60}

# Direct final D/C pose-and-role joins: D age3 has54 physical masks per
# ACTUAL D/DC role, not prior first-returned labels15/30 or D14/D28 counts.
dbase=[r for r in current['all267_foreign_typed_base_rows'] if r['old']=='D' and r['n']==3]
cbase=[r for r in current['all267_foreign_typed_base_rows'] if r['old']=='C' and r['n']==3]
assert len(dbase)==len(cbase)==54
Dkeys={(r['A'],r['b1'],r['b2'],tuple(r['pa']),tuple(r['p2'])) for r in dbase}
Ckeys={(r['A'],r['b1'],r['b2'],tuple(r['pa']),tuple(r['p2'])) for r in cbase}
assert len(Dkeys)==len(Ckeys)==54
actualD=d3['all108_actual_source_role_contact_cases']
assert len(actualD)==108
assert {(r['actual_full_source'],contact_key(r)) for r in actualD}=={(full,key) for full in ('D','DC') for key in Dkeys}
assert Counter(r['proof'] for r in actualD)=={
    'excluded_by_same_original_common_CURRENT':72,
    'excluded_by_incoming_beta_min3_and_final_E_endpoint_guard':12,
    'actual next D/V/U-family current reserve; all8 next fulls excluded':12,
    'signed sourceDC C1 common(3,1) current reserve':12}
D_angle_keys={(r['b1'],r['b2']) for r in dbase}
assert D_angle_keys=={(a['first_ordinary'],a['second_ordinary']) for a in angles
                     if a['old_source']=='D' and a['actual_old_source_to_FOREIGN_C_age']==3}
Croles={(r['actual_full'],r['selected_C_index1']) for r in c3['all7_genuine_C_roles_and18_same_identity_source_reserves']}
assert Croles=={('DC',1),('VC',1),('VCC',1),('VCC',2),('UC',1),('UCC',1),('UCC',2)}
actualC=c3['all378_role_specific_actual_before_mask_conflicts']
assert len(actualC)==378
Cactual={(r['actual_full_source'],r['selected_C_index1'],
         (r['foreign'],r['first'],r['second'],tuple(r['FOREIGN_pose']),tuple(r['second_pose']))) for r in actualC}
assert Cactual=={(full,index,key) for full,index in Croles for key in Ckeys}
assert all(r['all_guaranteed_same_CURRENT_witnesses'] for r in actualC)
C_angle_keys={(r['b1'],r['b2']) for r in cbase}
assert C_angle_keys=={(a['first_ordinary'],a['second_ordinary']) for a in angles
                     if a['old_source']=='C' and a['actual_old_source_to_FOREIGN_C_age']==3}

paths=[
    ROOT/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',
    ROOT/'seven_word_spatial_return_2026-10-23/first_returned_catalogue_parent_mapping_manifest.json',
    ROOT/'audits/check_first_foreign_returned_simplicity_independent.json',
    ROOT/'audits/check_returned_catalogue_parent_mapping_independent.json',
    ROOT/'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry_manifest.json',
    ROOT/'audits/check_second_ordinary_small_interface_independent.json',
    ROOT/'second_ordinary_after_first_foreign_2026-10-24/remaining_24_angles_manifest.json',
    ROOT/'audits/remaining24_second_contact_angles_independent.json',
    ROOT/'second_old_C_age3_2026-10-24/manifest.json',
    ROOT/'audits/old_C_age3_reserve_independent.json',
    ROOT/'old_D_second_age3_common_beta_2026-10-24/manifest.json',
    ROOT/'old_D_second_age3_next_base_2026-10-24/manifest.json',
    ROOT/'audits/old_D_age3_next_base_independent.json',
    ROOT/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',
    ROOT/'second_contact_signed_obligations_2026-10-24/manifest.json',
    ROOT/'second_contact_signed_obligations_2026-10-24/core_status_qualification_manifest.json',
    ROOT/'audits/check_second_contact_current_obligations_independent.json',
    ROOT/'second_old_C_age2_2026-10-24/manifest.json',
    ROOT/'audits/check_old_C_second_age2_independent.json',
    ROOT/'old_V_age1_scope_qualification_2026-10-24/manifest.json',
    ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in paths)
out=dict(status='AUTHOR_FROZEN_TWO_ORDINARY_FINITE_TO_GEOMETRIC_ASSEMBLY_PENDING_REVIEW',
    theorem='An actual U-entry complete-eight prefix, its FIRST complete F/Q/B, and exactly TWO immediately following ordinary RAW atoms D/C/V/U with one actual final M11 have a simple OPEN corrected-center proxy through the second RAW exit. The old complete field, fine identities and actual cursor are retained.',
    all192_rotation_checked_FOREIGN_b1_b2_local_closed_segment_interfaces=local,
    all16_actual_terminal_marker_supply_cases=marker_supply,
    exactly4_immediate_old_V_U_contact_candidates_all_actual_literal_conflicts=last,
    all217_original_angle_IDs_with_signed_source_exclusion=angle_records,
    exact_source_angle_counts=dict(Counter(r['exact_original_angle']['old_source'] for r in angle_records)),
    direct54_pose_keys_per_actual_D_DC_source_and108_role_proof_cases=actualD,
    direct7_real_C_containing_roles_and378_pose_role_conflicts=actualC,
    finite_to_geometric_bridge='Signed one-RAW theorem gives the already-simple finite prefix. Local closed-segment checks remove foreign and b1 contacts. Any other first positive b2 contact lies on an outgoing old D/C/V/U atom; the old terminal point belongs to foreign and is already removed. Exact angle/ownership theorem puts it among original217, all now excluded. Therefore no actual first contact exists.',
    physical_CORE_qualification='CURRENT external absence alone does not imply physical death; same original R-born BLACK may be alive in CORE. Only guaranteed CURRENT or actual combined before-WHITE conflicts are used.',
    positive_controls_scope='The signed prepared RAW-C and D/VC-entry positives remain real, without the required genuine source/U ancestry. Later internal U does not retroactively include an earlier selected source. Withdrawn seal6ea48d5 is NOT used.',
    no_third_RAW_or_later_tail_or_second_foreign_extension=True,
    no_fine_walk_self_avoidance_or_global_language_coverage_or_capture=True,
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(HERE/'two_ordinary_simplicity.json').write_text(json.dumps(out,indent=2)+'\n')
print('Direct217 angle IDs all excluded: D54+C44+V59+U60. Final D108 and C378 actual pose/role keys match exactly.')
print('192 rotation-checked local closed-segment cases and16 actual marker-supply cases reconstructed;4 last-old-base controls fail literally.')
print('Geometric conclusion is SIMPLE OPEN proxy through exactly TWO immediate ordinary RAWs after FIRSTforeign, with actual finalM11. No iteration.')
