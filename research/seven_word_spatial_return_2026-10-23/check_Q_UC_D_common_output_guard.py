"""No N-run cutoff: the retained Q/UC+D branch loses its old-C common ID.

All ages and source roles are preforeign. The final contradiction is inside
actual Q RAW, not an appended marker or a postforeign maturation assertion.
"""
from pathlib import Path
from collections import Counter
import hashlib
import importlib.util
import json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',R/'word_stabilization/check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
so=importlib.util.spec_from_file_location('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner=importlib.util.module_from_spec(so);so.loader.exec_module(owner)
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
CP=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
G=json.loads(GP.read_text())['geometry'];KEEP=(0,1,4,5,6,7,8,9)
COUNT={tuple(map(int,line.split()[:8]))for line in CP.read_text().splitlines()}

def add(p,q):return p[0]+q[0],p[1]+q[1]
def pose_after(word,pose=(0,0,0)):
    p=pose[:2];h=pose[2]
    for turn in word:
        h=(h+(1 if turn=='R'else-1))%4;p=add(p,lit.DIRS[h])
    return(*p,h)

# Full UC entry is the clock-zero source frame, with its genuine own C.
UC=(0,0,0)
firstD=pose_after(G[8]['word']);assert firstD==(0,5,3)
selectedD=pose_after(G[0]['word'],firstD);assert selectedD==(-1,6,3)
oldC=pose_after(G[0]['word'],selectedD);assert oldC==(-2,7,3)
selectedExit=pose_after(G[1]['word'],selectedD);assert selectedExit==(-3,7,2)
common=add(oldC[:2],lit.rot((2,0),oldC[2]));assert common==(-2,9)
full_output=(3,1);assert list(full_output)in G[1]['outputs']
assert add(selectedD[:2],lit.rot(full_output,selectedD[2]))==common
raw=lit.trace(G[1]['word']);assert raw['last'][full_output]==('R',18)
assert raw['last'][full_output][1]-len(G[0]['word'])==8

# Every actual full consumer before original-clock4 has source-entry age<3.
young=[]
for age in range(3):
    h=(-age)%4
    for cid in KEEP:
        for inp in map(tuple,G[cid]['inputs']):
            z=lit.rot(inp,h);p=(full_output[0]-z[0],full_output[1]-z[1])
            key=(KEEP.index(1),KEEP.index(cid),*p,h,*full_output,age)
            reason='sector'if(sum(p)+h)%2 else'signed_COUNT5'
            if reason=='signed_COUNT5':assert key in COUNT
            young.append(dict(source='DC',actual_source_output=full_output,
                consumer=G[cid]['name'],actual_input=inp,consumer_pose=(*p,h),
                full_source_entry_C_age=age,exclusion=reason,exact_COUNT5_key=key))
assert len(young)==69 and Counter(q['exclusion']for q in young)=={'sector':40,'signed_COUNT5':29}

# The independently signed support lemma forces this exact first breaker and
# total three-U zero-C suffix. The source UC's own C and selected DC C1 have
# distinct actual clocks0 and1; selected full DC entry is original clock1.
breaker=(3,-1,0);Q=(3,11,0)
forcedU=[(3,-1,0),(3,3,0),(3,7,0)]
p=breaker
for expected in forcedU:
    assert p==expected;p=pose_after(G[7]['word'],p)
assert p==Q

# Before the first breaker, an arbitrary N-oriented zero-C run ends there.
# Each entry has y<=-1, so its input-site y<=3, far below common_y9.
pre=[]
for cid in(0,4,7):
    assert G[cid]['endpoint'][1]>0 and G[cid]['endpoint'][2]==0
    for inp in map(tuple,G[cid]['inputs']):
        required_y=common[1]-inp[1]
        assert required_y>=5 and required_y>breaker[1]
        pre.append(dict(plain_N_consumer=G[cid]['name'],input=inp,
            required_consumer_entry_y=required_y,
            actual_prebreaker_entry_y_upper_bound=-1,
            exclusion='N endpoint cone, valid for every run length and every D/V/U order.'))
assert len(pre)==8
post=[]
for p in forcedU:
    inputs=[add(p[:2],q)for q in map(tuple,G[7]['inputs'])]
    assert common not in inputs and all(q[0]in(2,3)for q in inputs)
    post.append(dict(actual_U_entry=p,all_actual_input_sites=inputs,
                     common_output_x=-2,all_input_x_values=(2,3)))

# Actual Q RAW first requires WHITE at this still-current original identity.
local=(common[0]-Q[0],common[1]-Q[1]);assert local==(-5,-2)
qraw=lit.trace(owner.WORDS['Q']);assert qraw['first'][local]==('R',53)
canonical=owner.describe('Q',53)
assert canonical['owner']=='own Q-base RAW'and canonical['owner_tick0']==53
assert canonical['owner_read_number1']==54

deps=[GP,CP,CP.parent/'manifest.json',H/'DC_C1_UC_support_separator_manifest.json',
      H/'DC_C1_prefix_height_horizon_manifest.json',
      R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',
      R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_ALL_LENGTH_Q_UC_D_COMMON_OUTPUT_GUARD_PENDING_REVIEW',
    scope='Only the remaining actual Q/UC+D parent branch forced by the signed C3 FIRST-contact support lemma. Arbitrary prebreaker N runs retained. A genuine old DC/C1 common output stays current until Q; actual Q RAW requires WHITE. No generic Q adjacency, returned-simplicity or secondforeign theorem.',
    actual_source_UC_entry=UC,selected_creating_D_entry=selectedD,
    selected_old_C1_entry=oldC,selected_DC_full_exit=selectedExit,
    genuine_common_output_in_UC_frame=common,genuine_common_output_full_DC_slot=full_output,
    physical_common_birth_DC_tick0=18,physical_common_birth_C1_tick0=8,
    actual_selected_DC_entry_clock_from_UC=1,actual_Q_entry_clock_from_UC=4,
    atomic_C1_and_full_DC_source_entry_clocks_identical=True,
    all69_minimum_age_three_input_queries=young,
    all8_arbitrary_prebreaker_N_input_height_exclusions=pre,
    all3_forced_U_packet_input_x_exclusions=post,
    current_identity_exhaustive_cases=['A first consumer before clock4 is excluded by the69 age0..2 queries.',
        'At clock4 before first breaker, every possible N consumer head has y<=-1; no input reaches y9.',
        'At/after breaker the exact three U entries have all input x2/3, never x=-2.',
        'No C occurs at clock4 before Q, so there is no further consumer orientation or unfinished full-tail exception.'],
    actual_Q_entry=Q,actual_Q_local_common_cell=local,
    first_actual_Q_read=('R',53),canonical_actual_read_owner=canonical,
    final_contradiction='Original genuine DC/C1 output remains BLACK at Q entry, but Q first reads it R/WHITE at RAW tick53.',
    all_C_side_UC_parent_rows_now_excluded=True,
    remaining_C_last_positive_C_parent_counts=dict(F=6,Q=6,B=4),
    remaining_parent_types=('DC','VC'),
    rejected_seal_or_postforeign_lifetime_not_used=True,
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(H/'Q_UC_D_common_output_guard.json').write_text(json.dumps(out,indent=2)+'\n')
print('69 exact young-input exclusions;8 all-length N height guards;3 forced-U x guards;Q RAW53 contradiction.')
print('All C-side UC parents excluded conditionally on signed support branch;only DC/VC parents remain.')
