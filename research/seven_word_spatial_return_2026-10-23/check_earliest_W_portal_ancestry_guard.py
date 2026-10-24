"""Endpoint-driven actual candidate families and an all-length earliest guard.

No larger generic prefix scan. False6ea48d5 remains withdrawn; both genuine
plain-source regression controls are physically replayed below.
"""
from pathlib import Path
import importlib.util
import json
import hashlib
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',ROOT/'word_stabilization/check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
GP=ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
WP=ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry']
WORDS={a:r['word']for a,r in zip('DCVUFQB',json.loads(WP.read_text())['macro_words'])}
FULL={r['name']:r['word']for r in G}
def word(tokens):return ''.join(FULL.get(t,WORDS.get(t))for t in tokens)
def pose_only(w):
    p=(0,0);h=0
    for c in w:
        h=(h+(1 if c=='R'else-1))%4;d=lit.DIRS[h];p=(p[0]+d[0],p[1]+d[1])
    return(*p,h)
def normalize(p,source):
    q=(p[0]-source[0],p[1]-source[1]);z=lit.rot(q,-source[2])
    return(*z,(p[2]-source[2])%4)

triple_guards=[]
for tokens,expected in((('D','V','Q'),93),(('D','U','B'),113)):
    tr=lit.trace(word(tokens)+WORDS['C']+lit.M);assert not tr['feasible']
    assert tr['conflict_read']==expected and tr['previous_read']==1 and tr['cell']==[-1,0]
    assert tr['turn']=='L' and expected-len(word(tokens))+1==2
    assert expected<len(word(tokens))+len(WORDS['C'])
    triple_guards.append(dict(tokens=tokens,literal_conflict=tr,
        previous_actual_owner='D RAW phase2 L deletion',
        required_actual_continuation='returned RAW C',
        conflicting_actual_owner='returned RAW C phase2, not foreign RAW',
        immutable_without_any_seed_choice=True))

# At T=2 the signed complementary-index law gives remaining E weight1 for Q
# or2 for B. Actual last-packet rules force a unique non-D final packet.
T2=[]
for source_base,weight in(('V',1),('U',2)):
    for foreign,remaining,final in(('Q',1,'V'),('B',2,'U')):
        Dconstant = 4 if source_base == 'V' else 3
        # B>=1 after first-W-D, so there is certainly an immediately
        # preceding D before the single final V/U, for any dormant D length.
        assert Dconstant+1>=4
        T2.append(dict(source_base=source_base,source_weighted_index=2,
            foreign=foreign,remaining_E_weight=remaining,
            actual_S_runs_before_portal_consumer='arbitrary; not omitted',
            forced_remaining_E_fullword=f'D^(B+{Dconstant}),{final},{foreign},returned_RAW_C',
            actual_W_head_parameter='B>=1',remaining_D_count_formula=f'B+{Dconstant}',
            immutable_forbidden_suffix=['D',final,foreign,'returned_RAW_C']))

containing_role_guards=[]
for source in(6,9):
    tr=lit.trace(G[source]['word']+G[0]['word']+lit.M)
    assert not tr['feasible']
    before_next=len(G[source]['word'])+len(G[0]['word'])
    assert tr['conflict_read']-before_next+1==2
    containing_role_guards.append(dict(old_full_source=G[source]['name'],old_C_index=2,
        forced_first_W_fullpacket='D',complete_pair_conflict=tr,
        contradiction_read_owner='next actual word RAW phase2, supplied by actual M11',
        conflict_inside_D_RAW=False,source_full_completion_retained=True))

# Structurally prescribed attempts, not an endpoint word tree or depth ladder.
# T2 immediate boundary module or actual plain-U regression module, then the
# forced Q/B E tail. A single T3 F module tests the next earliest weighted level.
attempts=[]
for source in(1,5,8,6,9):
    oldC_prefix=G[source]['word'][:-15]
    oldC_pose=pose_only(oldC_prefix)
    for family,mid in(('T2_boundary_UCC',['D','UCC','V']),
                       ('T2_plain_U_regression_module',['D','U','VCC','V','V'])):
        for foreign,last in(('Q','V'),('B','U')):
            tokens=[G[source]['name']]+mid+['D']*4+[last,foreign,'C']
            prefix=word(tokens[:-2]);foreign_pose=normalize(pose_only(prefix),oldC_pose)
            assert foreign_pose==({'Q':(4,-5,1),'B':(5,-4,1)}[foreign])
            returned_pose=normalize(pose_only(word(tokens[:-1])),oldC_pose);assert returned_pose==(0,-1,3)
            tr=lit.trace(word(tokens)+lit.M);assert not tr['feasible']
            attempts.append(dict(family=family,old_full_source=G[source]['name'],
                old_C_index=1 if source in(1,5,8)else 2,tokens=tokens,
                normalized_foreign_pose=foreign_pose,normalized_returned_RAW_C_pose=returned_pose,
                full_board_first_read_consistency=False,literal_conflict=tr,
                scope='Only this endpoint/portal-selected physical word; not arbitrary W exhaustion.'))
    tokens=[G[source]['name'],'D','V','U','VCC','V','V']+['D']*5+['V','F','C']
    assert normalize(pose_only(word(tokens[:-2])),oldC_pose)==(2,-5,1)
    assert normalize(pose_only(word(tokens[:-1])),oldC_pose)==(0,-1,3)
    tr=lit.trace(word(tokens)+lit.M);assert not tr['feasible']
    attempts.append(dict(family='T3_F_plain_U_regression_module',old_full_source=G[source]['name'],
        old_C_index=1 if source in(1,5,8)else 2,tokens=tokens,
        normalized_foreign_pose=(2,-5,1),normalized_returned_RAW_C_pose=(0,-1,3),
        full_board_first_read_consistency=False,literal_conflict=tr,
        scope='One prescribed next-weight F module, not all T3 candidates.'))
assert len(attempts)==25

controls=json.loads((HERE/'ordered_W_seal_withdrawal_controls.json').read_text())['controls']
for c in controls:
    w=word(c['full_packet_sequence'])+lit.M;assert lit.trace(w)['feasible']
    B={tuple(q)for q in c['complete_finite_seed']};p=(0,0);h=0;reads=[];tag=tuple(c['source_tag_physical_site'])
    for tick,z in enumerate(w):
        assert(p in B)==(z=='L')
        if p==tag:reads.append((z,tick))
        B.symmetric_difference_update({p});h=(h+(1 if z=='R'else-1))%4;d=lit.DIRS[h];p=(p[0]+d[0],p[1]+d[1])
    assert reads==[tuple(q)for q in c['source_tag_all_actual_reads']]

deps=[GP,WP,ROOT/'word_stabilization/check_foreign_return_interfaces.py',
      HERE/'ordered_W_portal_submatching_manifest.json',HERE/'W_portal_complementary_indices_manifest.json',
      HERE/'ordered_W_marker_ownership_erratum_manifest.json',HERE/'returned_C_double_tail_source_manifest.json',
      HERE/'ordered_W_seal_withdrawal_controls_manifest.json']
out=dict(status='AUTHOR_FROZEN_EARLIEST_PORTAL_GUARD_AND_ENDPOINT_SELECTED_ATTEMPTS_PENDING_REVIEW',
    scope='Exactly three actual C3 residues. Universal T<=2 portal nonspending, arbitrary D lengths and arbitrary N/W/S before the pop. Two old C2 fullsource-role exclusions.25 prescribed positive-realization attempts all fail; no arbitrary-W or all-T3 exclusion.',
    both_immutable_DVQ_DUB_complete_prefix_returned_C_guards=triple_guards,
    four_unbounded_T2_endpoint_tail_obligations=T2,
    both_old_C2_containing_fullsource_complete_pair_guards=containing_role_guards,
    all25_endpoint_and_actual_portal_selected_candidate_histories=attempts,
    both_genuine_U_entry_regression_controls_replayed=controls,
    conclusions=['Every actual spent W portal in any of the three residues must have source weighted index T>=3.',
        'The earliest W portal is unspent, whether its producer is V(T1)or U(T2); its identity remains current through the first return.',
        'Old C2 of VCC/UCC is impossible by first-W-D and actual next-word phase2 contradiction; together with signed C1 double-tail closure, only C1 of DC/VC/UC remains.',
        'No actual U-entry realization was attained by the25 specifically selected whole histories; no broader negative-search claim is made.'],
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(HERE/'earliest_W_portal_ancestry_guard.json').write_text(json.dumps(out,indent=2)+'\n')
print('Universal T<=2 portal guard;two old-C2 complete-pair cuts;25 endpoint-selected histories fail;two genuine regressions pass.')
