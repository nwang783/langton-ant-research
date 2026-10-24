"""A physical prepared returned-C loop and exact eight-predecessor isolation.

This is NOT a U-entry control. It protects that indispensable hypothesis in the
new first-foreign and returned-contact interfaces.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util
import json
import hashlib

ROOT = Path('/workspace/shared/langton')
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('lit', ROOT/'word_stabilization/check_foreign_return_interfaces.py')
lit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lit)
GP = ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
WP = ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G = json.loads(GP.read_text())['geometry']
words = {a:r['word'] for a,r in zip('DCVUFQB',json.loads(WP.read_text())['macro_words'])}
full_words = {r['name']:r['word'] for r in G}
sequence = ['DC','DC','D','VC','V','V','F','C']
raw = ''.join(full_words.get(a,words.get(a)) for a in sequence)
actual_word = raw+lit.M
assert len(raw) == 200 and len(actual_word) == 211
literal = lit.trace(actual_word)
assert literal['feasible']
seed = {p for p,(letter,tick) in literal['first'].items() if letter == 'L'}
assert len(seed) == 27


def add(p,q):
    return p[0]+q[0],p[1]+q[1]


def sub(p,q):
    return p[0]-q[0],p[1]-q[1]


def det(p,q):
    return p[0]*q[1]-p[1]*q[0]


def hit(a,b,c,d):
    u,v,z=sub(b,a),sub(d,c),sub(c,a)
    denominator=det(u,v)
    if denominator:
        s,t=Q(det(z,v),denominator),Q(det(z,u),denominator)
        return dict(kind='point',s=s,t=t,point=(a[0]+s*u[0],a[1]+s*u[1])) if 0<=s<=1 and 0<=t<=1 else None
    if det(z,u):
        return None
    k=0 if u[0] else 1
    x,y=Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])
    lo,hi=max(Q(0),min(x,y)),min(Q(1),max(x,y))
    return dict(kind='collinear',s_interval=(lo,hi)) if lo<=hi else None


# Literal fine replay on this COMPLETE finite black board, all unlisted white.
board=set(seed)
p,h=(0,0),0
fine=[]
raw_exit=None
for tick,letter in enumerate(actual_word):
    assert (p in board)==(letter=='L')
    fine.append(dict(tick=tick,cell=p,heading=h,turn=letter))
    board.symmetric_difference_update({p})
    h=(h+(-1 if letter=='L' else 1))%4
    p=add(p,lit.DIRS[h])
    if tick+1==len(raw):
        raw_exit=dict(pose=(*p,h),mass=len(board),black=sorted(board))
assert raw_exit['pose']==(0,0,2) and raw_exit['mass']==53
assert len(board)==52
fine_marker_exit=(*p,h)
assert fine_marker_exit==literal['pose']

# True marked/atomic cuts, not the fine ant path. The final raw C is not
# recoded as an old complete-eight tail after the foreign.
atoms=['D','C','D','C','D','V','C','V','V','F','C']
assert ''.join(words[a] for a in atoms)==raw
p,h=(0,0),0
tick=0
segments=[]
atomic_cuts=[]
for atom in atoms:
    tr=lit.trace(words[atom]);assert tr['feasible']
    start=add((2*p[0],2*p[1]),lit.rot((-1,-1),h))
    ep=add(p,lit.rot(tr['pose'][:2],h))
    eh=(h+tr['pose'][2])%4
    end=add((2*ep[0],2*ep[1]),lit.rot((-1,-1),eh))
    atomic_cuts.append(dict(atom=atom,entry_tick=tick,entry_pose=(*p,h),
                            exit_tick=tick+len(words[atom]),exit_pose=(*ep,eh),
                            doubled_center_segment=(start,end)))
    segments.append((start,end))
    p,h=ep,eh
    tick+=len(words[atom])
assert atomic_cuts[1]['entry_tick']==10 and atomic_cuts[1]['entry_pose']==(1,1,0)
assert atomic_cuts[9]['entry_tick']==129 and atomic_cuts[9]['entry_pose']==(3,-4,1)
assert atomic_cuts[10]['entry_tick']==185 and atomic_cuts[10]['entry_pose']==(1,0,3)
assert segments[-1][1]==segments[1][0]==(1,1)

# Every nonadjacent old/foreign segment pair is disjoint. Adjacent collinear
# continuations are checked too; they share only the actual common endpoint.
old_pair_queries=[]
for i in range(10):
    for j in range(i+1,10):
        contact=hit(*segments[i],*segments[j])
        if j==i+1:
            assert segments[i][1]==segments[j][0]
            assert contact is not None
            if contact['kind']=='point':
                assert contact['s']==1 and contact['t']==0
            else:
                assert contact['s_interval']==(Q(1),Q(1))
        else:
            assert contact is None
        old_pair_queries.append(dict(earlier=i,later=j,contact=contact))

returned_queries=[]
new_contacts=[]
for i in range(10):
    contact=hit(*segments[i],*segments[10])
    if i==9:
        assert contact['kind']=='point' and contact['s']==1 and contact['t']==0
    elif contact is not None:
        assert contact['kind']=='point' and contact['t']==1 and contact['point']==(Q(1),Q(1))
        assert (i,contact['s']) in ((0,Q(1)),(1,Q(0)))
        new_contacts.append(dict(earlier=i,contact=contact))
    returned_queries.append(dict(earlier=i,contact=contact))
assert len(new_contacts)==2

# Both earlier segment descriptions name ONE old vertex. Its outgoing source
# is the first C, not its incoming factor-first D.
ownership=dict(point=(1,1),returned_atom_index=10,returned_parameter=1,
               earlier_unique_vertex=1,outgoing_old_atom_index=1,
               outgoing_old_atom='C',old_parameter=0,
               incoming_old_atom_index=0,incoming_old_parameter=1,
               source_to_foreign_C_age=3,
               foreign_pose_in_old_C_chart=(2,-5,1),
               returned_pose_in_old_C_chart=(0,-1,3),
               physical_source_pose=(1,1,0),physical_returned_exit_pose=(0,0,2),
               physical_pose_return=False)

# Exact left-isolation, not a bounded lookback absence claim. If this whole
# fixed history occurred after ANY earlier full-eight packet, that immediately
# preceding packet would be one of these eight and would give its raw conflict.
predecessors=[]
for source_id in (0,1,4,5,6,7,8,9):
    result=lit.trace(G[source_id]['word']+actual_word)
    assert not result['feasible']
    predecessors.append(dict(full_predecessor=G[source_id]['name'],conflict=result))


def encode(x):
    if isinstance(x,Q):
        return int(x) if x.denominator==1 else str(x)
    if isinstance(x,dict):
        return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):
        return [encode(v) for v in x]
    return x


dependencies=[GP,WP,ROOT/'word_stabilization/check_foreign_return_interfaces.py',
              HERE/'first_returned_atom_contact_manifest.json']
out=dict(status='AUTHOR_FROZEN_PREPARED_POSITIVE_CONTROL_PENDING_REVIEW',
    scope='A complete27-black finite board realizes DC,DC,D,VC,V,V,F,rawC+actualM11. Its first returned proxy contact is old first-C START. It is NOT U-entry: all eight possible immediate full-eight predecessors are literal conflicts. No physical pose/field return, period or capture claim.',
    full_packet_and_raw_foreign_sequence=sequence,
    raw_word=raw,actual_terminal_marker=lit.M,raw_length=len(raw),
    initial_pose=(0,0,0),initial_black=sorted(seed),initial_black_mass=27,
    all_unlisted_cells_white=True,fine_replay=fine,RAW_exit=raw_exit,
    after_actual_marker_pose=fine_marker_exit,after_actual_marker_black=sorted(board),
    after_actual_marker_mass=len(board),actual_atomic_cuts=atomic_cuts,
    old_and_foreign_all_pair_queries=old_pair_queries,
    returned_atom_all_contact_queries=returned_queries,
    first_new_contact_ownership=ownership,
    all_eight_immediate_predecessor_conflicts=predecessors,
    dependencies={str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest()
                  for path in dependencies})
(HERE/'returned_C_prepared_loop_control.json').write_text(json.dumps(encode(out),indent=2)+'\n')
print('Physical211-read replay PASS; mass27->53RAW->52marker.')
print('Old+foreign proxy simple; returned raw C first contact is old C START.')
print('All8 immediate full-eight predecessors impossible: no U-entry lift.')
