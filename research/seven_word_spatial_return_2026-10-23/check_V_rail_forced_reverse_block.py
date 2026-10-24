"""All-length literal last-L rail guards, not a bounded prefix search.

For V^r VCC V^j with 0<=j<=r+1, next old-eight D/U is impossible.
A finite affine-line/RAW-footprint calculation proves every integer r,j.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',R/'word_stabilization/check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
so=importlib.util.spec_from_file_location('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner=importlib.util.module_from_spec(so);so.loader.exec_module(owner)
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
G=json.loads(GP.read_text())['geometry']

def reads(w):
    p=(0,0);h=0;out=[]
    for tick,c in enumerate(w):
        out.append((p,c,tick));h=(h+(1 if c=='R'else-1))%4
        d=lit.DIRS[h];p=(p[0]+d[0],p[1]+d[1])
    return out
V=reads(G[4]['word']);VCC=reads(G[6]['word'])
def line_hits(seq,c,reverse=False):
    # x=d, so the ACTUAL finite footprint supplies the exact integer bounds.
    lo=min(p[0]for p,_,_ in seq);hi=max(p[0]for p,_,_ in seq)
    out=[]
    for d in range(lo,hi+1):
        if reverse and d<1:continue
        q=(d,3*d+4-c)if reverse else(d,3*d+c)
        hit=[(turn,tick)for p,turn,tick in seq if p==q]
        if hit:out.append(dict(d=d,cell=q,actual_reads=hit))
    return out

interfaces=[]
for switch,c,read_tick in(('D',3,11),('U',2,12)):
    fwd=line_hits(V,c);tail=line_hits(VCC,c);back=line_hits(V,c,True)
    if switch=='D':
        assert fwd==[dict(d=-1,cell=(-1,0),actual_reads=[('L',1)])]
        assert next(q for q in tail if q['d']==0)['actual_reads']==[('L',19)]
    else:
        assert fwd==[dict(d=-1,cell=(-1,-1),actual_reads=[('L',2)]),
                     dict(d=0,cell=(0,2),actual_reads=[('R',12)])]
        assert next(q for q in tail if q['d']==0)['actual_reads']==[('R',12),('L',20)]
    assert back==[]
    assert next(q for q in tail if q['d']==-1)['actual_reads']==[('L',1 if switch=='D' else 2)]
    # VCC relative d=-j; only d<=0 can occur for j>=0. d=-1,0 are
    # exhausted above; any listed positive-d tail contact is irrelevant.
    assert {q['d']for q in tail if q['d']<=0}=={-1,0}
    goal=(0,1)if switch=='D' else (0,2)
    tr=lit.trace(owner.WORDS[switch]+lit.M)
    assert tr['first'][goal]==('L',read_tick)
    o=owner.describe(switch,read_tick)
    interfaces.append(dict(next_old_E_base=switch,c=c,
        proposed_first_L=read_tick,canonical_actual_owner=o,
        victim_in_initial_V_frame='(r-j,3*(r-j)+c)',
        all_forward_plain_V_line_contacts=fwd,
        all_VCC_line_contacts=tail,
        all_past_reverse_V_d_ge1_line_contacts=back,
        last_actual_deletion_tick0=f'18*(r-j)+{19 if switch=="D" else 20}',
        no_intermediate_R='Forward affine-line contacts end at L; VCC d=-j and all earlier reverse V contacts give no later read.',
        validity='Every integer r>=0 and 0<=j<=r+1.'))

# Explicit finite controls are only regression checks. The universal proof is
# the footprint/affine interface above, whose bounds come from actual RAW cells.
regressions=[]
for r in(0,1,2,10):
    for j in(0,r+1):
        for switch,c,tick in(('D',3,11),('U',2,12)):
            prefix=G[4]['word']*r+G[6]['word']+G[4]['word']*j
            tr=lit.trace(prefix+owner.WORDS[switch]+lit.M)
            assert not tr['feasible']
            assert tr['conflict_read']==len(prefix)+tick
            assert tr['previous_read']==18*(r-j)+(19 if switch=='D' else 20)
            assert tr['cell']==[r-j,3*(r-j)+c]
            regressions.append(dict(r=r,j=j,next_base=switch,immutable_conflict=tr))

controls=json.loads((H/'ordered_W_seal_withdrawal_controls.json').read_text())['controls']
for q in controls:
    word=''.join(owner.WORDS[a]for packet in q['full_packet_sequence']for a in packet)+lit.M
    assert lit.trace(word)['feasible']
    B={tuple(p)for p in q['complete_finite_seed']};p=(0,0);h=0
    for c in word:
        assert(p in B)==(c=='L');B.symmetric_difference_update({p})
        h=(h+(1 if c=='R'else-1))%4;d=lit.DIRS[h];p=(p[0]+d[0],p[1]+d[1])

# A genuine continuation with the next forced V, not a prepared source-free
# rail. One previously unread entry root extends the 16-black U-entry control.
continued_tokens=['U','V','VCC','V','V','V']
continued_raw=''.join(''.join(owner.WORDS[a]for a in packet)for packet in continued_tokens)
continued_word=continued_raw+lit.M
continued=lit.trace(continued_word);assert continued['feasible']
continued_seed=sorted(q for q,(turn,_)in continued['first'].items()if turn=='L')
assert len(continued_seed)==17 and len(continued_raw)==148
old_seed={tuple(p)for p in controls[0]['complete_finite_seed']}
assert set(continued_seed)-old_seed=={(-2,3)} and not(old_seed-set(continued_seed))
assert continued['first'][(-2,3)]==('L',143)
B=set(continued_seed);p=(0,0);h=0;original_U_q_reads=[]
for tick,c in enumerate(continued_word):
    assert(p in B)==(c=='L')
    if p==(-1,2):original_U_q_reads.append((c,tick))
    B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4
    d=lit.DIRS[h];p=(p[0]+d[0],p[1]+d[1])
assert original_U_q_reads==[('L',13),('R',21),('L',149)]
continued_control=dict(full_packet_sequence=continued_tokens,RAW_length=148,
    actual_physical_read_count=len(continued_word),complete_finite_seed=continued_seed,
    added_entry_root_relative_to_genuine16black_control=(-2,3),
    added_root_first_read_tick0=143,added_root_actual_owner=owner.describe('V',13),
    genuine_original_U_q_reads=original_U_q_reads,
    q_physical_L_owner=owner.describe('V',19),
    meaning='The third reverse V is genuinely attained on a 17-black complete U-entry board. The preceding 16-black control plus actual M11 is unchanged; only a previously unread root was added.')

# C3 endpoint identities for W=D^a,V^r,VCC. W has both remaining Cs in
# VCC, hence S is empty and E starts(-a-3r-4,1+a+r) in old-C frame.
endpoint=[]
for foreign,X,Y,offset,required_last in(('F',2,-5,0,('V','U')),('Q',4,-5,1,('V','U')),('B',5,-4,2,('U',))):
    # v+2u = r+offset; d+v = a+r+1-Y. A first D/U is necessary:
    # d >= a+1-Y-offset >0 for every a>=1.
    min_d_constant=1-Y-offset
    assert min_d_constant>=3
    if foreign in('F','Q'):
        assert offset<2
        contradiction='First D/U needs at least r+2 earlier Vs, exceeding total E weight r+offset.'
    else:
        assert offset==2 and required_last==('U',)
        contradiction='At least r+2 earlier Vs use the entire E weight; required final U would add2, impossible.'
    endpoint.append(dict(foreign=foreign,target_old_C_frame=(X,Y,1),
        assumed_W_fullpacket_word='D^a,V^r,VCC with a>=1,r>=0',
        actual_S_stage='empty: VCC supplies the two actual remaining C tails',
        actual_E_start='(-a-3r-4,1+a+r,E)',
        exact_E_D_plus_V=f'a+r+{1-Y}',exact_E_V_plus_2U=f'r+{offset}',
        positive_E_D_count_lower_bound=f'a+{min_d_constant}',
        required_last_old_E_packet=required_last,
        all_length_contradiction=contradiction))

deps=[GP,H/'first_returned_five_label_frontier_manifest.json',
      H/'complete8_foreign_adjacency_manifest.json',
      H/'ordered_W_seal_withdrawal_controls_manifest.json',
      R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_ALL_LENGTH_LITERAL_V_RAIL_GUARD_PENDING_REVIEW',
    scope='Literal V^r,VCC,V^j rail with 0<=j<=r+1 forces the next old-eight zero-C base to be V. Its endpoint corollary excludes only C3 W=D^a,V^r,VCC with empty S. Arbitrary mixed W, S nonempty, D-separated V blocks, and the five general first-contact targets remain open.',
    two_all_integer_forward_last_L_and_reverse_nonreading_interfaces=interfaces,
    sixteen_prescribed_literal_regression_checks=regressions,
    both_genuine_U_entry_controls_physically_replayed=True,
    genuine_next_forced_V_17black_continuation=continued_control,
    rejected_seal6ea48d5_not_used=True,
    three_all_length_C3_endpoint_corollaries=endpoint,
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(H/'V_rail_forced_reverse_block.json').write_text(json.dumps(out,indent=2)+'\n')
print('Two exact affine last-L interfaces for every r,j;16 regressions;both genuine controls pass.')
print('Narrow all-length C3 W=D^a V^r VCC / empty-S subfamily excluded for F,Q,B.')
