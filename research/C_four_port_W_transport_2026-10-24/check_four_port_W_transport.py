"""Four current C ports support an arbitrary-length zero-C W transfer.

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
PORTS={'beta':(1,-1),'q':(2,0),'arm':(2,1),'bud':(1,2)}
selection=[]
for full,selected in [('DC',1),('VC',1),('VCC',1),('VCC',2),('UC',1),('UCC',1),('UCC',2)]:
    before=full[0]+'C'*(selected-1)
    old_entry=after(raw(before))
    slots=[add(old_entry[:2],lit.rot(cell,old_entry[2])) for cell in PORTS.values()]
    selection.append((full,selected,slots))
assert sum(len(slots) for full,index,slots in selection)==28
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
assert len(source_roles)==7 and len(queries)==2760 and len(three_crossings)==3
assert Counter(q['exclusion'] for q in queries)['proper_crossing_of_actual_past_source_atomic_chord']==3


# A literal first-touch table is enough. There is no age assignment after
# the foreign. Four SAME CURRENT identities begin outside the actual K.
first_touch=[]
compatible={}
for atom in 'DVU':
    geometry=lit.literal_geometry(WORDS[atom])
    trace=lit.trace(WORDS[atom]+lit.M)
    for port,cell in PORTS.items():
        for slot0 in geometry['inputs']:
            slot=tuple(slot0)
            entry=sub(cell,lit.rot(slot,3))
            requirements=[]
            blocked=[]
            consumed=[]
            for sibling,q in PORTS.items():
                local=lit.rot(sub(q,entry),1)
                first=trace['first'].get(local)
                is_input=list(local) in geometry['inputs']
                if local in lit.K:
                    blocked.append(dict(port=sibling,reason='CURRENT outside K cannot occupy ENTRY core'))
                elif first and first[0]=='R':
                    blocked.append(dict(port=sibling,reason='first actual read requires WHITE'))
                elif is_input:
                    assert first and first[0]=='L'
                    consumed.append(sibling)
                requirements.append(dict(port=sibling,canonical_local_cell=local,
                    in_ENTRY_K=local in lit.K,true_input=is_input,actual_first_read=first,
                    physical_first_owner=owner.describe(atom,first[1]) if first else None))
            endpoint=after(WORDS[atom],(*entry,3))
            row=dict(first_input_packet=atom,alleged_first_touched_port=port,
                actual_true_input_slot=slot,actual_W_entry=(*entry,3),actual_W_RAW_exit=endpoint,
                all_four_tag_requirements=requirements,blocked_by_held_cohort=blocked,
                simultaneous_cohort_inputs=consumed,
                normalized_source_C_sector_compatible=(sum(entry)+3)%2==0)
            first_touch.append(row)
            if not blocked:
                assert not {'beta','q'}&set(consumed)
                assert endpoint[1]>=2
                for lower in ('beta','q'):
                    local=lit.rot(sub(PORTS[lower],entry),1)
                    assert local not in trace['first']
                    exit_core={add(endpoint[:2],lit.rot(k,3)) for k in lit.K}
                    assert PORTS[lower] not in exit_core
                compatible[atom,entry]=dict(packet=atom,entry=(*entry,3),RAW_exit=endpoint,
                    only_upper_inputs=consumed,lower_two_complete_context_MISS=True,
                    normalized_source_C_sector_compatible=(sum(entry)+3)%2==0)
assert len(first_touch)==32 and len(compatible)==9
assert sum(not row['blocked_by_held_cohort'] for row in first_touch)==11
assert sum(row['normalized_source_C_sector_compatible'] for row in compatible.values())==2

# Even without holding the upper two, every possible W input consumer of
# a lower original needs an entry below the first-touch exit height.
lower_poses=[]
for lower in ('beta','q'):
    cell=PORTS[lower]
    for atom in 'DVU':
        geometry=lit.literal_geometry(WORDS[atom])
        for slot0 in geometry['inputs']:
            slot=tuple(slot0)
            entry=sub(cell,lit.rot(slot,3))
            assert entry[1]<= (0 if lower=='beta' else 1)
            lower_poses.append(dict(lower_port=lower,consumer=atom,true_input_slot=slot,
                required_W_entry=(*entry,3),maximum_entry_y=0 if lower=='beta' else 1))
assert len(lower_poses)==16
W_drifts={a:after(WORDS[a],(0,0,3)) for a in 'DVU'}
assert W_drifts=={'D':(-1,1,3),'V':(-3,1,3),'U':(-4,0,3)}

# The old-C global-first-contact K=3 targets are exact and finite, even
# though the preceding plain W rail has arbitrary length.
def floor(q): return q.numerator//q.denominator

def ceil(q): return -((-q.numerator)//q.denominator)

a,b=chord('C',(0,0,0))
u=sub(b,a)
targets=[]
boxes=[]
for atom in 'DCVU':
    c,d=chord(atom,(0,0,3))
    v=sub(d,c)
    den=det(u,v)
    assert den
    corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2) for k in(0,1))
             for s in(0,1) for t in(0,1)]
    bounds=[(floor(min(p[k] for p in corners)),ceil(max(p[k] for p in corners))) for k in(0,1)]
    boxes.append(dict(atom=atom,exact_rational_corners=[[[q.numerator,q.denominator] for q in p] for p in corners],integer_bounds=bounds))
    for x in range(bounds[0][0],bounds[0][1]+1):
        for y in range(bounds[1][0],bounds[1][1]+1):
            if (x+y-3)%2: continue
            z=sub(add(c,(2*x,2*y)),a)
            s,t=Q(det(z,v),den),Q(det(z,u),den)
            if not(0<=s<1 and 0<t<=1): continue
            head=(x,y,3)
            trace=lit.trace(WORDS[atom]+lit.M)
            conflicts=[]
            for lower in ('beta','q'):
                cell=PORTS[lower]
                local=lit.rot(sub(cell,head[:2]),1)
                first=trace['first'].get(local)
                if local in lit.K:
                    conflicts.append(dict(SAME_current_port=lower,canonical_cell=local,reason='ENTRY core'))
                elif first and first[0]=='R':
                    conflicts.append(dict(SAME_current_port=lower,canonical_cell=local,
                        reason='actual first R requires WHITE',physical_owner=owner.describe(atom,first[1])))
            assert conflicts
            targets.append(dict(atom=atom,actual_W_entry=head,
                old_s=[s.numerator,s.denominator],new_t=[t.numerator,t.denominator],
                guaranteed_lower_pair_conflicts=conflicts))
assert len(targets)==6
assert {(r['atom'],tuple(r['actual_W_entry'])) for r in targets}=={
    ('D',(0,-1,3)),('C',(0,-1,3)),('V',(1,0,3)),('V',(2,-1,3)),
    ('U',(1,0,3)),('U',(3,0,3))}

# Complete FOREIGN-context MISS is strong enough to preserve both physical
# fine identity and external CURRENT status at its actual RAW exit.
foreign_miss=[]
for A in 'FQB':
    trace=lit.trace(WORDS[A]+lit.M)
    endpoint=after(WORDS[A])
    sites=set(trace['first'])
    exitK={add(endpoint[:2],lit.rot(k,endpoint[2])) for k in lit.K}
    geometry=lit.literal_geometry(WORDS[A])
    assert lit.K<=sites and exitK<=sites
    assert {tuple(q) for q in geometry['outputs']}<=sites
    foreign_miss.append(dict(foreign=A,canonical_RAW_exit=endpoint,
        ENTRY_K_and_actual_EXIT_K_and_all_fresh_O_are_in_complete_context=True,
        implication='A SAME CURRENT ID outside this complete read context is unread, unchanged and outside the actual exit K, hence remains CURRENT. No R55-core export shortcut is used.'))

# Actual prepared regression: the upper bud can be physically retired.
# The transfer preserves only beta/q, not all four ports or an output seal.
word=WORDS['U']+lit.M
trace=lit.trace(word)
assert trace['feasible']
start=(2,3,3)
seed={add(start[:2],lit.rot(p,3)) for p,(turn,tick) in trace['first'].items() if turn=='L'}
seed.update(PORTS.values())
entryK={add(start[:2],lit.rot(k,3)) for k in lit.K}
assert set(PORTS.values()).isdisjoint(entryK)
black=set(seed)
p,h=start[:2],start[2]
port_reads={name:[] for name in PORTS}
raw_cut=None
for tick,turn in enumerate(word):
    assert (p in black)==(turn=='L')
    for name,cell in PORTS.items():
        if p==cell:
            port_reads[name].append(dict(tick0=tick,turn=turn,
                canonical_owner=owner.describe('U',tick)))
    if turn=='L': black.remove(p)
    else: black.add(p)
    h=(h+(1 if turn=='R' else -1))%4
    p=add(p,lit.DIRS[h])
    if tick+1==len(WORDS['U']):
        actual_exitK={add(p,lit.rot(k,h)) for k in lit.K}
        assert all(PORTS[name] in black and PORTS[name] not in actual_exitK for name in ('beta','q'))
        raw_cut=dict(pose=(*p,h),mass=len(black),complete_BLACK=sorted(black),
                     SAME_beta_q_alive_outside_actual_exitK=True)
assert not port_reads['beta'] and not port_reads['q']
assert port_reads['bud'] and port_reads['bud'][0]['turn']=='L'
assert len(seed)==13 and len(word)==39
regression=dict(initial_head=start,complete_initial_BLACK=sorted(seed),
    all_unlisted_initial_cells_WHITE=True,initial_mass=len(seed),
    actual_tokens=['U','actual next M11 prefix'],physical_reads=len(word),
    all_four_initial_current_BLACK_tag_reads=port_reads,
    RAW_exit=raw_cut,physical_exit_after_actual_prefix=(*p,h),
    complete_physical_BLACK_after_prefix=sorted(black),
    no_genuine_C_creator_or_foreign_ancestry_claimed=True,
    conclusion='A real prepared board retires the old upper bud while leaving SAME beta/q unread and CURRENT at RAW exit. No all-four permanence or one-output seal is asserted.')

# Complete foreign-HIT alternatives are finite. Every allowed hit of a
# CURRENT tag must be a true BLACK input, never ENTRY core or beforeWHITE.
foreign_hit_queries=[]
foreign_hit_poses={}
for A in 'FQB':
    geometry=lit.literal_geometry(WORDS[A])
    trace=lit.trace(WORDS[A]+lit.M)
    for port,cell in PORTS.items():
        for slot0 in geometry['inputs']:
            slot=tuple(slot0)
            head=sub(cell,lit.rot(slot,1))
            blockers=[]
            if (sum(head)+1)%2:
                classification='conserved_source_C_sector'
            else:
                for name,q in PORTS.items():
                    local=lit.rot(sub(q,head),3)
                    first=trace['first'].get(local)
                    if local in lit.K:
                        blockers.append(dict(port=name,reason='CURRENT in ENTRY core'))
                    elif first and first[0]=='R':
                        blockers.append(dict(port=name,reason='CURRENT BLACK before first WHITE requirement'))
                classification='held_four_port_color_conflict' if blockers else 'necessary_FOREIGN_HIT_pose'
            row=dict(foreign=A,aligned_current_port=port,true_FOREIGN_input=slot,
                     actual_E_entry=(*head,1),classification=classification,
                     exact_held_port_conflicts=blockers)
            foreign_hit_queries.append(row)
            if classification=='necessary_FOREIGN_HIT_pose':
                endpoint=after(WORDS[A],(*head,1))
                assert endpoint[2]==3 and endpoint[0]<=0
                record=dict(foreign=A,E_entry=(*head,1),actual_W_RAW_exit=endpoint,
                    source_four_port_HIT_is_only_a_necessary_color_interface=True)
                if endpoint[0]<0:
                    record['all_tail_exclusion']='Every old-C K3 target has headx>=0; every later W step strictly decreases x.'
                else:
                    assert A=='F' and head==(2,-5) and endpoint==(0,-1,3)
                    record['all_tail_exclusion']='Only targetD/C head0,-1W is reachable, with ZERO intervening W steps. The independently signed one-RAW simplicity theorem excludes this immediate contact.'
                foreign_hit_poses[A,head]=record
assert len(foreign_hit_queries)==188
assert Counter(q['classification'] for q in foreign_hit_queries)=={
    'conserved_source_C_sector':94,'held_four_port_color_conflict':71,
    'necessary_FOREIGN_HIT_pose':23}
assert len(foreign_hit_poses)==19
assert sum(r['actual_W_RAW_exit'][0]==0 for r in foreign_hit_poses.values())==1
assert all(r['actual_W_entry'][0]>=0 for r in targets)

paths=[
    ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json',
    ROOT/'core_periodicity_new/chronology_dcuv/protected_patch2.tsv',
    ROOT/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv',
    ROOT/'second_old_C_age3_2026-10-24/manifest.json',
    ROOT/'audits/old_C_age3_reserve_independent.json',
    ROOT/'one_foreign_first_contact_compression_2026-10-24/manifest.json',
    ROOT/'audits/check_one_foreign_contact_C_window_independent.json',
    ROOT/'seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json',
    ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',
    ROOT/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',
    ROOT/'seven_word_spatial_return_2026-10-23/first_returned_catalogue_parent_mapping_manifest.json',
    ROOT/'audits/check_first_foreign_returned_simplicity_independent.json']
assert all(p.exists() for p in paths)
out=dict(status='AUTHOR_FROZEN_ALL_LENGTH_OLD_C_AGE3_FIRST_CONTACT_EXCLUSION_PENDING_REVIEW',
    scope='A genuine old C at true preFIRSTforeign age3 cannot own the GLOBAL FIRST new proxy contact after FIRSTforeign and ANY finite ordinary RAW suffix with actual terminalM11. Four CURRENT ports yield an all-length W transport on FOREIGN-MISS; all19 possible FOREIGN-HIT gates fail by x monotonicity or signed immediate one-RAW simplicity. No other-source or arbitrary-tail simplicity conclusion.',
    normalized_ports=PORTS,
    all7_real_C_roles_with_uniform_four_CURRENT_reserves=source_roles,
    all2760_exact_uniform_reserve_queries=queries,
    uniform_query_classification=dict(Counter(q['exclusion'] for q in queries)),
    exactly3_real_DC_past_source_crossings=three_crossings,
    all32_first_cohort_input_alignments=first_touch,
    all9_distinct_color_compatible_first_touch_poses=list(compatible.values()),
    all16_possible_lower_port_consumer_heads=lower_poses,
    exact_zero_C_W_RAW_drifts=W_drifts,
    all4_exact_old_C_K3_target_boxes=boxes,
    all6_outgoing_owned_old_C_contact_targets=targets,
    all3_complete_foreign_MISS_implications=foreign_miss,
    all188_possible_FOREIGN_input_four_port_HIT_alignments=foreign_hit_queries,
    all19_necessary_FOREIGN_HIT_pose_x_cone_exclusions=list(foreign_hit_poses.values()),
    actual_prepared_upper_loss_regression_not_a_genuine_C_history=regression,
    first_touch_proof='Before the first actual true-input/cohort loss, all4 tags are CURRENT. Every color-compatible first-touch packet consumes only arm/bud, completely misses beta/q and exits at y>=2. Every later plainW head has y>=2, while beta/q input consumers require y<=0/1. Hence no lower original can ever lose CURRENT status. If there is no first touch, all4 survive. Marker-only CORE absorption is included as a true input, not omitted.',
    contact_corollary='Signed arbitrary-tail window gives totalK<=3 for an outgoing oldC (maximal alpha). True preFOREIGN age3 therefore leaves zero returnedC before global first contact, so the arbitrary suffix is exactly a plainW rail plus terminal D/C/V/U target. The six exact targets all contradict the SAME lower pair at their ENTRY.',
    final_HIT_MISS_exhaustion='Every valid FOREIGN either completely misses all4 current ports or reads one as a true input. The former has SAME beta/q W persistence. The latter is among19 poses:18 exitx<0 cannot reach any target; soleF2,-5E exits0,-1W and forces immediate targetD/C with no prior W atom, excluded by signed one-RAW simplicity.',
    no_unconditional_foreign_MISS_assumed=True,
    no_postFOREIGN_maturation_ordinary_atom_count_cap_or_finite_geometry_quotient=True,
    no_old_C_other_age_or_old_D_V_U_or_second_FOREIGN_or_global_capture_conclusion=True,
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(HERE/'four_port_W_transport.json').write_text(json.dumps(out,indent=2)+'\n')
print('Uniform four current ports:7 real C roles/28 outputs/2760 signed queries, only3 oldDC strict crossings.')
print('32 first-touch input alignments ->9 distinct color-compatible poses, none consume beta/q, all exitsy>=2; all16 lower consumers requirey<=0/1.')
print('FOREIGN-HIT exhaustive188 alignments leave19 poses:18 exitx<0; soleF2,-5E forces an already excluded immediateD/C. GlobalFIRST oldC age3 contact is impossible after ANY ordinary suffix.')
