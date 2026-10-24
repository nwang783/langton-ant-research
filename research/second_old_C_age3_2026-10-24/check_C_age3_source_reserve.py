"""Eighteen real source-output reserves close the old-C true-age3 slice.

Use only existing signed sector/HB/COUNT5 clauses plus three exact proper
crossings of the actual past D/C source chords. All full and atomic clocks,
consumer completion deadlines and marker/core input owners are explicit.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as Q
import importlib.util
import hashlib
import json

ROOT=Path('/workspace/shared/langton')
HERE=Path(__file__).resolve().parent
P=ROOT/'core_periodicity_new/chronology_dcuv'
GEOMETRY=P/'literal_residual_geometry.json'
HB_PATH=P/'protected_patch2.tsv'
COUNT_PATH=P/'critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
G=json.loads(GEOMETRY.read_text())['geometry']
HB={tuple(map(int,line.split()[:7])) for line in HB_PATH.read_text().splitlines()}
COUNT={tuple(map(int,line.split()[:8])) for line in COUNT_PATH.read_text().splitlines()}
keep=[0,1,4,5,6,7,8,9]
mp={a:i for i,a in enumerate(keep)}
spec=importlib.util.spec_from_file_location('lit',ROOT/'word_stabilization/check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(spec)
spec.loader.exec_module(lit)
spec=importlib.util.spec_from_file_location('owner',ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner=importlib.util.module_from_spec(spec)
spec.loader.exec_module(owner)
WORDS=owner.WORDS


def add(p,q): return p[0]+q[0],p[1]+q[1]
def sub(p,q): return p[0]-q[0],p[1]-q[1]
def det(p,q): return p[0]*q[1]-p[1]*q[0]
def raw(tokens): return ''.join(WORDS[a] for a in tokens)


def after(word,pose=(0,0,0)):
    p,h=pose[:2],pose[2]
    for turn in word:
        h=(h+(1 if turn=='R' else -1))%4
        p=add(p,lit.DIRS[h])
    return *p,h


def z2(pose): return add((2*pose[0],2*pose[1]),lit.rot((-1,-1),pose[2]))
def chord(atom,pose): return z2(pose),z2(after(WORDS[atom],pose))


def proper_intersection(a,b,c,d):
    u,v,z=sub(b,a),sub(d,c),sub(c,a)
    den=det(u,v)
    assert den
    s,t=Q(det(z,v),den),Q(det(z,u),den)
    assert 0<s<1 and 0<t<1
    point=tuple(Q(a[k])+s*u[k] for k in(0,1))
    return dict(old_s=[s.numerator,s.denominator],new_t=[t.numerator,t.denominator],
                point=[[v.numerator,v.denominator] for v in point])


def physical_owner(tokens,tick):
    lo=0
    for index,atom in enumerate(tokens):
        if tick<lo+len(WORDS[atom]):
            return dict(actual_atom_index0=index,actual_atom=atom,
                atom_start_tick0=lo,canonical=owner.describe(atom,tick-lo))
        lo+=len(WORDS[atom])
    j=tick-lo
    assert 0<=j<len(lit.M)
    return dict(actual_atom='next actual word',next_word_tick0=j,
                next_word_read_number1=j+1,turn=lit.M[j])


# These selected roles are a small exact certificate, not a claim that
# every unlisted source output remains current. The prior broader table
# and all its unresolved physical-CORE obligations stay unchanged.
selection=[
    ('DC',1,[(2,0),(2,3),(3,1),(3,2)]),
    ('VC',1,[(2,1),(3,4)]),
    ('VCC',1,[(2,1),(3,4)]),
    ('VCC',2,[(2,5),(-1,5),(1,6)]),
    ('UC',1,[(1,2),(2,5)]),
    ('UCC',1,[(1,2),(2,5)]),
    ('UCC',2,[(1,6),(-2,6),(0,7)])]
assert sum(len(slots) for full,index,slots in selection)==18
source_roles=[]
queries=[]
three_crossings=[]
for full,selected,slots in selection:
    producer=next(a for a in keep if G[a]['name']==full)
    assert G[producer]['word']==raw(full)
    actual_geometry=lit.literal_geometry(raw(full))
    assert {tuple(q) for q in actual_geometry['outputs']}=={tuple(q) for q in G[producer]['outputs']}
    before=full[0]+'C'*(selected-1)
    old_entry=after(raw(before))
    tau=-(selected-1)
    N=3-tau
    source_Cs=full.count('C')
    actual_trace=lit.trace(raw(full))
    role=dict(actual_full=full,selected_C_index1=selected,
        actual_prefix_before_selected_C=before,
        selected_C_pose_in_full_frame=old_entry,
        true_selected_C_ENTRY_clock=0,FOREIGN_ENTRY_clock=3,
        actual_full_ENTRY_clock=tau,actual_full_ENTRY_age_at_FOREIGN=N,
        actual_full_completion_clock=tau+source_Cs,selected_reserves=[])
    for output in slots:
        assert list(output) in actual_geometry['outputs']
        turn,birth_tick=actual_trace['last'][output]
        assert turn=='R'
        normalized=lit.rot(sub(output,old_entry[:2]),-old_entry[2])
        reserve=dict(full_output_slot=output,actual_last_R_tick0=birth_tick,
            normalized_selected_C_cell=normalized,all_query_indices=[])
        for age in range(N+1):
            h=(-age)%4
            for consumer in keep:
                consumer_name=G[consumer]['name']
                consumer_Cs=consumer_name.count('C')
                for slot0 in G[consumer]['inputs']:
                    slot=tuple(slot0)
                    pose=sub(output,lit.rot(slot,h))
                    hb=(producer,consumer,*pose,h,*output)
                    ck=(mp[producer],mp[consumer],*pose,h,*output,age)
                    record=dict(full_source=full,output=output,
                        actual_full_source_age=age,
                        consumer_full=consumer_name,consumer_input_slot=slot,
                        consumer_full_pose=(*pose,h),HB_key=hb,count5_key=ck,
                        FOREIGN_full_source_age_deadline=N,
                        consumer_full_completion_age=age+consumer_Cs)
                    if age<source_Cs:
                        reason='source_full_not_yet_completed; remaining source atoms are input-free C'
                    elif age+consumer_Cs>N:
                        reason='consumer_full_cannot_complete_before_actual_FOREIGN_entry'
                    elif (sum(pose)+h)%2:
                        reason='signed_conserved_sector'
                    elif hb in HB:
                        reason='signed_HB_clause'
                    elif ck in COUNT:
                        reason='signed_COUNT5_clause'
                    else:
                        # All and only the three rows below need the actual
                        # simple preforeign atomic path, not a new clause.
                        assert full=='DC' and age==3 and consumer_name=='V' and h==1
                        assert (output,pose,slot) in {
                            ((2,0),(-1,0),(0,3)),
                            ((2,0),(0,1),(1,2)),
                            ((3,1),(0,1),(0,3))}
                        source_atom='D' if pose==(-1,0) else 'C'
                        source_pose=(0,0,0) if source_atom=='D' else after(WORDS['D'])
                        old_chord=chord(source_atom,source_pose)
                        consumer_chord=chord('V',(*pose,h))
                        crossing=proper_intersection(*old_chord,*consumer_chord)
                        expected=(0,0) if source_atom=='D' else (2,2)
                        assert crossing['point']==[[expected[0],1],[expected[1],1]]
                        reason='proper_crossing_of_actual_past_source_atomic_chord'
                        record.update(actual_past_source_atom=source_atom,
                            actual_past_source_pose=source_pose,
                            actual_past_source_chord=old_chord,
                            candidate_consumer_V_chord=consumer_chord,
                            strict_crossing=crossing,
                            consumer_input_actual_first_owner=None)
                        # Derive the true input first-read tick without an
                        # informal phase label or marker-ownership guess.
                        inp_first=lit.trace(WORDS['V']+lit.M)['first'][slot]
                        record['consumer_input_actual_first_owner']=owner.describe('V',inp_first[1])
                        three_crossings.append(record)
                    record['exclusion']=reason
                    reserve['all_query_indices'].append(len(queries))
                    queries.append(record)
        role['selected_reserves'].append(reserve)
    source_roles.append(role)
assert len(source_roles)==7 and len(queries)==1794 and len(three_crossings)==3
assert Counter(q['exclusion'] for q in queries)['proper_crossing_of_actual_past_source_atomic_chord']==3

# Geometry is re-read from the independently signed obligation table and
# checked directly against actual current-mask transforms, with real role
# clock records above. Its mandatory physical-CORE qualifier is retained.
prior=json.loads((ROOT/'second_contact_signed_obligations_2026-10-24/signed_current_obligations.json').read_text())
base=[r for r in prior['all267_foreign_typed_base_rows'] if r['old']=='C' and r['n']==3]
assert len(base)==54 and all(r['reason']=='keep' for r in base)
all_mask_rows=[]
for role in source_roles:
    for base_row in base:
        pa=tuple(base_row['pa'])
        tokens=base_row['A']+base_row['b1']+base_row['b2']
        trace=lit.trace(raw(tokens)+lit.M)
        assert trace['feasible']
        witnesses=[]
        for reserve in role['selected_reserves']:
            cell=tuple(reserve['normalized_selected_C_cell'])
            local=lit.rot(sub(cell,pa[:2]),-pa[2])
            first=trace['first'].get(local)
            if local in lit.K:
                witnesses.append(dict(reserve=cell,contradiction='SAME CURRENT external residual in FOREIGN entryK'))
            elif first and first[0]=='R':
                witnesses.append(dict(reserve=cell,contradiction='SAME CURRENT BLACK identity required WHITE at actual combined first read',
                    combined_tick0=first[1],actual_read_owner=physical_owner(tokens,first[1])))
        assert witnesses
        all_mask_rows.append(dict(actual_full_source=role['actual_full'],
            selected_C_index1=role['selected_C_index1'],foreign=base_row['A'],
            first=base_row['b1'],second=base_row['b2'],FOREIGN_pose=pa,
            second_pose=base_row['p2'],true_atomic_preFOREIGN_age=3,
            actual_full_ENTRY_age_at_FOREIGN=role['actual_full_ENTRY_age_at_FOREIGN'],
            all_guaranteed_same_CURRENT_witnesses=witnesses))
assert len(all_mask_rows)==378

paths=[GEOMETRY,HB_PATH,COUNT_PATH,
    ROOT/'second_contact_signed_obligations_2026-10-24/manifest.json',
    ROOT/'second_contact_signed_obligations_2026-10-24/core_status_qualification_manifest.json',
    ROOT/'audits/check_second_contact_current_obligations_independent.json',
    ROOT/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',
    ROOT/'audits/check_first_foreign_returned_simplicity_independent.json',
    ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in paths)
out=dict(status='AUTHOR_FROZEN_OLD_C_AGE3_SOURCE_RESERVE_CLOSURE_PENDING_REVIEW',
    scope='Only outgoing genuine old C at atomic source-entry-to-FIRSTforeign age3, chronological FIRST new SECOND ordinary RAW contact after original U-entry complete-eight prefix, actual firstforeign and first ordinary RAW, with one actual finalM11. All seven real containing roles, no general second simplicity.',
    all7_genuine_C_roles_and18_same_identity_source_reserves=source_roles,
    all1794_exact_source_output_consumer_queries=queries,
    exact_query_classification=dict(Counter(q['exclusion'] for q in queries)),
    exactly3_actual_DC_past_atomic_chord_crossings=three_crossings,
    all378_role_specific_actual_before_mask_conflicts=all_mask_rows,
    CURRENT_reason='Every possible preFOREIGN first input consumer is excluded by existing signed source/consumer completion, sector,HB,COUNT5 clauses, or one of three strict actual past-source chord crossings. C tails consume no older residual. Thus the selected SAME source IDs are current at FOREIGN entry. No physical retirement is inferred from a mere CORE ledger loss.',
    deadline_warning='Positive-C consumer full packets must complete their actual RAW before the FIRSTforeign full boundary. A consumer beginning at the deadline with a C tail cannot retire a source tag before that foreign. Marker-only inputs of allowable consumers are retained with canonical physical ownership.',
    conclusion='Every one of54 positional placements is blocked in every one of7 actual C1/C2 roles. Hence old C at true preFOREIGN age3 cannot own the stipulated FIRST SECOND-RAW contact. No long prefix enumeration, larger closure or postFOREIGN maturity is used.',
    no_generic_WHITE_or_currentness_for_unselected_outputs=True,
    no_SECOND_simplicity_or_future_atom_or_foreign_extension=True,
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(HERE/'C_age3_source_reserve.json').write_text(json.dumps(out,indent=2)+'\n')
print('Seven actual C1/C2 roles;18 selected source-output reserves;1,794 exact signed low-age queries.')
print(dict(Counter(q['exclusion'] for q in queries)))
print('Only3 query survivors: proper oldD/ownC crossings for genuine DC. All378 role-specific masks have a SAME CURRENT contradiction.')
