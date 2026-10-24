"""Exact parent-prescribed A,C,C,V geometry and complete-color controls.
No generic prefix search or third-atom simplicity claim.
"""
from pathlib import Path
from fractions import Fraction as Q
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


def raw(tokens): return ''.join(W[a] for a in tokens)
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


def hit(a,b,c,d):
    u,v,z=sub(b,a),sub(d,c),sub(c,a)
    den=det(u,v)
    if den:
        s,t=Q(det(z,v),den),Q(det(z,u),den)
        if not(0<=s<=1 and 0<=t<=1): return None
        point=tuple(Q(a[k])+s*u[k] for k in(0,1))
        return dict(kind='point',old_s=[s.numerator,s.denominator],
                    new_t=[t.numerator,t.denominator],
                    point=[[q.numerator,q.denominator] for q in point])
    if det(z,u): return None
    k=0 if u[0] else 1
    lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
    lo,hi=max(Q(0),lo),min(Q(1),hi)
    return dict(kind='collinear',old_interval=[[lo.numerator,lo.denominator],[hi.numerator,hi.denominator]]) if lo<=hi else None


def physical_owner(tokens,tick):
    lo=0
    for index,atom in enumerate(tokens):
        if tick<lo+len(W[atom]):
            return dict(actual_atom_index0=index,actual_atom=atom,atom_start_tick0=lo,
                        canonical=owner.describe(atom,tick-lo))
        lo+=len(W[atom])
    j=tick-lo
    assert 0<=j<len(lit.M)
    return dict(actual_atom='next actual word',next_word_tick0=j,
                next_word_read_number1=j+1,turn=lit.M[j])


def replay(word,seed,cut):
    black=set(seed)
    p,h=(0,0),0
    atcut=None
    for tick,turn in enumerate(word):
        assert (p in black)==(turn=='L')
        if turn=='L': black.remove(p)
        else: black.add(p)
        h=(h+(1 if turn=='R' else -1))%4
        p=add(p,lit.DIRS[h])
        if tick+1==cut:
            atcut=dict(pose=(*p,h),mass=len(black),complete_BLACK=sorted(black))
    return dict(exit_pose=(*p,h),mass=len(black),complete_BLACK=sorted(black),
                RAW_cut=atcut,physical_reads=len(word))


geometry=[]
for A in 'FQB':
    poses=[(0,0,0)]
    fcut=after(W['F'])
    pA=after(W[A])
    vertices=[z2(poses[0]),z2(fcut)]
    labels=['actual foreign F56 prefix']
    if A!='F':
        vertices.append(z2(pA))
        labels.append('actual foreign remaining tail')
    pose=pA
    for atom in 'CCV':
        pose=after(W[atom],pose)
        vertices.append(z2(pose))
        labels.append(atom)
    segments=list(zip(vertices,vertices[1:]))
    queries=[]
    nonadjacent=[]
    for i,old in enumerate(segments):
        for j in range(i+1,len(segments)):
            contact=hit(*old,*segments[j])
            if j==i+1:
                assert old[1]==segments[j][0]
                assert contact==dict(kind='point',old_s=[1,1],new_t=[0,1],
                                     point=[[old[1][0],1],[old[1][1],1]])
            elif contact is not None:
                nonadjacent.append(dict(old_piece=i,new_piece=j,contact=contact))
            queries.append(dict(old_piece=i,new_piece=j,closed_segment_contact=contact))
    if A=='F':
        assert nonadjacent==[dict(old_piece=0,new_piece=3,contact=dict(
            kind='point',old_s=[3,4],new_t=[3,4],point=[[-11,2],[-5,2]]))]
    else:
        assert not nonadjacent
    geometry.append(dict(foreign=A,actual_piece_labels=labels,
        actual_doubled_vertices=vertices,all_closed_segment_pair_queries=queries,
        nonadjacent_contacts=nonadjacent,
        geometry_only_intended_words_not_assumed_physically_valid=True))

literal=[]
for A in 'FQB':
    tokens=A+'CCV'
    body=raw(tokens)
    word=body+lit.M
    trace=lit.trace(word)
    row=dict(tokens=list(tokens),RAW_length=len(body),actual_final_M_length=len(lit.M),
             complete_context_feasible=trace['feasible'])
    if trace['feasible']:
        seed={p for p,(turn,tick) in trace['first'].items() if turn=='L'}
        assert A=='B' and len(seed)==24 and lit.K<=seed
        actual=replay(word,seed,len(body))
        assert actual['physical_reads']==133
        assert actual['RAW_cut']['pose']==(-1,-3,0)
        assert actual['RAW_cut']['mass']==40 and actual['mass']==39
        row.update(complete_initial_BLACK=sorted(seed),all_unlisted_initial_cells_WHITE=True,
                   initial_mass=len(seed),actual_complete_physical_control=actual,
                   no_proxy_recontact=True,no_U_entry_ancestry_claimed=True)
    else:
        assert (A,trace['conflict_read'],trace['previous_read'],tuple(trace['cell']),trace['turn']) in {
            ('F',101,45,(-1,0),'R'),('Q',118,46,(-1,-1),'R')}
        prefix=word[:trace['conflict_read']]
        before=lit.trace(prefix)
        assert before['feasible']
        seed={p for p,(turn,tick) in before['first'].items() if turn=='L'}
        actual=replay(prefix,seed,len(body) if len(body)<=len(prefix) else -1)
        assert tuple(trace['cell']) in map(tuple,actual['complete_BLACK'])
        row.update(immutable_conflict=trace,
            previous_actual_owner=physical_owner(tokens,trace['previous_read']),
            failing_actual_owner=physical_owner(tokens,trace['conflict_read']),
            complete_initial_BLACK_for_exact_feasible_prefix=sorted(seed),
            all_unlisted_initial_cells_WHITE=True,actual_feasible_prefix=actual,
            actual_next_turn='L',intended_next_turn='R',
            third_RAW_completed_before_failure=(len(prefix)>=len(body)))
    literal.append(row)

# The only complete positive BCCV cannot lift to the stipulated old G8
# history: signed735 forces its immediate previous full packet to be plain U.
forced='UBCCV'
forced_word=raw(forced)+lit.M
bad=lit.trace(forced_word)
assert not bad['feasible']
assert (bad['conflict_read'],bad['previous_read'],bad['cell'],bad['turn'])==(145,1,[-1,0],'L')
assert physical_owner(forced,145)['canonical']['owner_tick0']==13
assert physical_owner(forced,145)['canonical']['owner_read_number1']==14
# Reconstruct all requested reads of the actual source-deleted cell. No
# unseen R repair can occur before the rejecting V tick13/read14.
p,h=(0,0),0
reads=[]
for tick,turn in enumerate(forced_word):
    if p==(-1,0): reads.append((tick,turn))
    h=(h+(1 if turn=='R' else -1))%4
    p=add(p,lit.DIRS[h])
assert reads[:2]==[(1,'L'),(145,'L')]
forced_record=dict(actual_forced_tokens=list(forced),immutable_conflict=bad,
    source_deleting_owner=physical_owner(forced,1),
    third_V_rejecting_owner=physical_owner(forced,145),
    all_prescribed_word_reads_of_source_deleted_cell=reads,
    no_R_rebirth_between_source_U_L1_and_third_V_L13=True,
    complete8_before_FIRST_B_requires_immediate_plain_U=True,
    conclusion='No earlier complete field or longer old G8 prefix can repair this fixed forced-U suffix; it already has an immutable repeated L.',
    no_claim_about_arbitrary_raw_predecessors_or_other_foreign_suffixes=True)

paths=[
    ROOT/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',
    ROOT/'audits/check_complete8_foreign_adjacency_independent.json',
    ROOT/'seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json',
    ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in paths)
out=dict(status='AUTHOR_FROZEN_PRESCRIBED_THIRD_CCV_TARGETS_PENDING_REVIEW',
    scope='Only exact parent-prescribed A,C,C,V plus actual finalM11 for A=F/Q/B, and forced immediate-U lift of the unique prepared B positive. No third-atom simplicity or generic ancestry search.',
    exact_all_pairwise_proxy_geometries=geometry,
    exact_literal_complete_and_partial_controls=literal,
    genuine_old_G8_first_foreign_U_lift_obstruction=forced_record,
    conclusion='FCCV has an intended strict F-piece crossing but fails inside thirdV RAW. QCCV misses foreign and completes RAW but fails actual finalM. BCCV is a genuine complete24-black finite-board control with simple local proxy, but cannot follow any old completeG8 prefix because its mandatory immediate U suffix is immutable-inconsistent.',
    no_attained_U_entry_third_contact_or_general_THIRD_simplicity=True,
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(HERE/'CCV_targets.json').write_text(json.dumps(out,indent=2)+'\n')
print('F: intended proper foreign-prefix crossing at3/4, but immutable RAW-V15/read16 conflict. Q: no contact, RAW succeeds, actual finalM fails.')
print('B: complete24-black/133-read prepared positive, simple proxy; mandatory U predecessor fails at source-L1/thirdV-L13, no U-entry lift in stipulated scope.')
