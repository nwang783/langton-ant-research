"""Explicit WHITE-premise lifts of849d; no contact theorem is transplanted.

The older-bud proof needs no selected-D own C or returned-V input. Its actual
parent, clocks, first-consumer tables and old D/C crossing witnesses are fixed.
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
BASE=H/'C75_immediate_DC_VC_ancestor_bud.json'
b=json.loads(BASE.read_text())
assert len(b['all230_source_age0_to4_actual_input_queries'])==230
assert len(b['four_surviving_DC_V_VC_inputs'])==4
assert all(q['exact_strict_midpoint_intersection']['s']==[1,2]and q['exact_strict_midpoint_intersection']['t']==[1,2]for q in b['two_actual_old_chord_strict_midpoint_obstructions'])
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
G=json.loads(GP.read_text())['geometry']

def add(p,q):return p[0]+q[0],p[1]+q[1]
def pose_after(word,pose):
    p=pose[:2];h=pose[2]
    for turn in word:
        h=(h+(1 if turn=='R'else-1))%4;p=add(p,lit.DIRS[h])
    return(*p,h)

rows=[]
for preword,anchor,tag,expected_tick in(('',(0,0,0),(-2,-1),68),('D',(-1,-1,0),(-3,-2),78)):
    assert pose_after(owner.WORDS['D']*len(preword),anchor)==(0,0,0)
    fp=(2,-5,1);relativeF=(fp[0]-anchor[0],fp[1]-anchor[1],fp[2])
    assert relativeF==((2,-5,1)if not preword else(3,-4,1))
    raw=lit.trace(owner.WORDS['F']);allctx=lit.trace(owner.WORDS['F']+owner.WORDS['C']+lit.M)
    local=lit.rot((tag[0]-fp[0],tag[1]-fp[1]),-fp[2])
    assert local not in raw['first']and local not in lit.K
    assert allctx['first'][local]==('R',expected_tick)
    actual_owner=owner.describe('FC',expected_tick)
    assert actual_owner['owner_tick0']==(12 if not preword else 7)
    assert actual_owner['owner_read_number1']==(13 if not preword else 8)
    for source in('D','DC'):
        for P in b['two_actual_parent_birth_and_clock_roles']:
            parent=P['actual_immediate_parent'];sid=1 if parent=='DC' else 5
            entry=(*add(anchor[:2],P['parent_entry'][:2]),P['parent_entry'][2])
            assert pose_after(G[sid]['word'],entry)==anchor
            q=add(entry[:2],lit.rot(P['genuine_atomic_exit_bud_full_slot'],entry[2]));assert q==tag
            old_chords=[]
            for c in b['two_actual_old_chord_strict_midpoint_obstructions']:
                off=(2*anchor[0],2*anchor[1])
                old=tuple(add(tuple(p),off)for p in c['actual_old_chord'])
                helper=tuple(add(tuple(p),off)for p in c['actual_helper_V_base_chord'])
                old_chords.append(dict(old_actual_atom=c['actual_old_atom'],old_chord=old,
                    helper_chord=helper,strict_intersection_parameters=c['exact_strict_midpoint_intersection']))
            rows.append(dict(catalogue_id=15,actual_outgoing_old_source='D',actual_full_source=source,
                last_positive_C_parent=parent,actual_pre_D_zero_C_word=preword,
                source_D_entry=(0,0,0),earlier_actual_D_anchor=anchor,
                anchor_actual_fullpacket='D'if preword else source,
                anchor_following_own_C_NOT_required_by_reused_lemma=True,
                actual_parent_entry=entry,parent_full_entry_clock=0,
                anchor_atomic_D_entry_clock=1,selected_D_entry_clock=1,foreign_entry_clock=4,
                original_parent_exit_bud=tag,relative_F_in_anchor_frame=relativeF,
                raw_F_never_reads_bud=True,first_required_R_tick0=expected_tick,
                canonical_actual_WHITE_read_owner=actual_owner,
                all230_original_first_consumer_queries_unchanged=True,
                four_survivors_same_translated_actual_old_chord_crossings=old_chords,
                no_first_contact_conclusion_is_transferred=True,
                conclusion='Original actual older bud cannot retire and stays BLACK; actual WHITE requirement excludes this parent/run/source combination.'))
assert len(rows)==8

# Only4 target/parent/run rows are removed; selectedD/DC containing choices
# remain a separate type layer rather than extra claimed attained histories.
removed=sorted({(q['last_positive_C_parent'],q['actual_pre_D_zero_C_word'])for q in rows})
assert removed==[('DC',''),('DC','D'),('VC',''),('VC','D')]
deps=[GP,BASE,H/'C75_immediate_DC_VC_ancestor_bud_manifest.json',
      R/'audits/check_C75_immediate_DC_VC_ancestor_bud_independent.json',
      H/'first_returned_three_F_frontier_manifest.json',H/'three_F_parent_assembly_signoff_manifest.json',
      R/'returned_D_last_C_parent_reduction_2026-10-24/manifest.json',
      R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
# The independent report's actual retained filename is resolved explicitly.
if not deps[3].exists():
    cand=list((R/'audits').glob('*C75*ancestor*independent.json'))
    assert len(cand)==1;deps[3]=cand[0]
out=dict(status='AUTHOR_FROZEN_D15_EMPTY_D_OLDER_BUD_PREMISE_LIFTS_PENDING_REVIEW',
    scope='Only D15 last positive-C parentDC/VC, followed by empty or one plainD before its selected sourceD/DC. Reader-independent first-retirement/chord lemma849d is reused after actual WHITE before-masks and source clocks are reconstructed. No oldC ownership relabeling or outgoing-contact theorem is imported.',
    eight_explicit_actual_typed_premise_lifts=rows,
    four_removed_D15_parent_run_rows=removed,
    selected_D_following_C_is_NOT_a_premise_of_original_guard=True,
    retained_positive_controls='The two signed849d clearing controls remain legal but have the forbidden older parentD/helperV crossing; no source-free bud-permanence claim.',
    remaining_D15_parent_run_words=('DD','DDD','V'),remaining_parent_types=('DC','VC'),
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(H/'D15_empty_D_older_bud_lifts.json').write_text(json.dumps(out,indent=2)+'\n')
print('8 exact typed premise lifts remove4 D15 parent/run rows(empty,D)x(DC,VC).')
print('Actual WHITE owners returnedC12/read13 or followingword7/read8;no selectedDC-tail/contact assumption.')
