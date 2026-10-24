"""C75 k0 ancestor-bud guard with real positive clearing countercontrols.

No source-color claim is stronger than actual U-entry old-center simplicity.
First retirement, including core absorption and deferred L ownership, is kept.
"""
from pathlib import Path
from fractions import Fraction as Q
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
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def chord(pose,atom):
    start=add((2*pose[0],2*pose[1]),lit.rot((-1,-1),pose[2]))
    D={'D':(2,2),'C':(2,2),'V':(2,6),'U':(0,8)}[atom]
    return start,add(start,lit.rot(D,pose[2]))
def hit(a,b,c,d):
    u,v,z=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
    assert den
    s,t=Q(det(z,v),den),Q(det(z,u),den)
    return dict(s=[s.numerator,s.denominator],t=[t.numerator,t.denominator],
        point=[str(a[0]+s*u[0]),str(a[1]+s*u[1])])
def pose_after(word,pose=(0,0,0)):
    p=pose[:2];h=pose[2]
    for turn in word:
        h=(h+(1 if turn=='R'else-1))%4;p=add(p,lit.DIRS[h])
    return(*p,h)

g=(-2,-1);priorC=(-1,0,1);selectedD=(0,0,0);F=(3,-4,1)
queries=[];survive=[];births=[]
for sid,out,P in((1,(2,0),(-2,1,1)),(5,(2,2),(-4,1,1))):
    raw=lit.trace(G[sid]['word']);base=lit.trace(owner.WORDS[G[sid]['name'][0]])
    assert raw['last'][out]==base['last'][out]and raw['last'][out][0]=='R'
    assert list(out)in G[sid]['outputs']
    assert add(P[:2],lit.rot(out,P[2]))==g
    assert pose_after(G[sid]['word'],P)==selectedD
    births.append(dict(actual_immediate_parent=G[sid]['name'],parent_entry=P,
        genuine_atomic_exit_bud_full_slot=out,physical_bud_in_selected_D_frame=g,
        last_R_tick0=raw['last'][out][1],own_C_tail_preserves_original_identity=True,
        parent_entry_clock=0,own_C_exit_selected_D_entry_clock=1,foreign_entry_clock=4))
    for age in range(5):
        h=(-age)%4
        for cid in KEEP:
            for inp in map(tuple,G[cid]['inputs']):
                z=lit.rot(inp,h);p=(out[0]-z[0],out[1]-z[1])
                key=(KEEP.index(sid),KEEP.index(cid),*p,h,*out,age)
                reason='sector'if(sum(p)+h)%2 else None
                if reason is None and age<G[sid]['name'].count('C'):
                    reason='source_full_packet_not_yet_completed'
                if reason is None and age+G[cid]['name'].count('C')>4:
                    reason='consumer_full_packet_cannot_complete_before_foreign'
                if reason is None and key in COUNT:reason='signed_COUNT5'
                if reason is None:reason='SURVIVING_ACTUAL_INPUT_ALIGNMENT'
                pg=add(P[:2],lit.rot(p,P[2]));hg=(h+P[2])%4
                row=dict(actual_parent=G[sid]['name'],source_bud_slot=out,consumer=G[cid]['name'],
                    actual_input=inp,full_source_entry_C_age=age,
                    consumer_pose_in_parent_frame=(*p,h),
                    consumer_pose_in_selected_D_frame=(*pg,hg),
                    exact_COUNT5_key=key,disposition=reason)
                queries.append(row)
                if reason=='SURVIVING_ACTUAL_INPUT_ALIGNMENT':survive.append(row)
assert len(queries)==230 and len(survive)==4
assert {(q['actual_parent'],q['consumer'],tuple(q['consumer_pose_in_selected_D_frame']))for q in survive}=={('DC',c,p)for c in('V','VC')for p in((-2,2,2),(-1,1,2))}

# All source ages are before F; the actual helper BASE chord belongs to the
# full V or VC consumer in either ownership mode.
parentD=chord((-2,1,1),'D');parentC=chord(priorC,'C')
assert parentD==((-5,3),(-3,1))and parentC==((-3,1),(-1,-1))
contacts=[]
for P,old,name in(((-2,2,2),parentD,'actual older parent D-base'),((-1,1,2),parentC,'actual older parent C1')):
    helper=chord(P,'V');contact=hit(*old,*helper)
    assert contact['s']==[1,2]and contact['t']==[1,2]
    contacts.append(dict(helper_V_or_VC_entry=P,actual_old_atom=name,
        actual_old_chord=old,actual_helper_V_base_chord=helper,
        exact_strict_midpoint_intersection=contact,
        clock_gap=3,nonadjacent_preforeign_U_entry_simple_path_forbids=True))

fcontext=lit.trace(owner.WORDS['F']+owner.WORDS['C']+lit.M)
local=lit.rot(sub(g,F[:2]),-F[2]);assert local==(-3,-5)
assert local not in lit.trace(owner.WORDS['F'])['first']
assert fcontext['first'][local]==('R',78)
physical_owner=owner.describe('FC',78)
assert physical_owner['owner']=='next actual word RAW'and physical_owner['owner_tick0']==7
assert physical_owner['owner_read_number1']==8

# Honest positive controls: the g identity really is born and cleared. They
# fail the U-entry hypothesis because the helper crosses the older parent D.
controls=[]
for tokens in([
    'DC','DC','DC','D','VC','D','D','U','F','C'],[
    'DC','DC','DC','D','V','DC','V','U','F','C']):
    raw=''.join(''.join(owner.WORDS[a]for a in packet)for packet in tokens)
    actual=raw+lit.M;tr=lit.trace(actual);assert tr['feasible']
    seed=sorted(q for q,(turn,_)in tr['first'].items()if turn=='L')
    B=set(seed);p=(0,0);h=0;greads=[]
    for tick,turn in enumerate(actual):
        assert(p in B)==(turn=='L')
        if p==(2,0):greads.append((turn,tick))
        B.symmetric_difference_update({p});h=(h+(1 if turn=='R'else-1))%4;p=add(p,lit.DIRS[h])
    assert greads[:2]==[('R',8),('L',104)]
    # Verify the final target in the ACTUAL selected-old-C frame. The old
    # path is nonsimple, so this is not a U-entry catalogue attainment.
    old_C_pose=pose_after(G[1]['word']+G[0]['word'])
    assert old_C_pose==(0,3,3)
    Fprefix=''.join(''.join(owner.WORDS[a]for a in packet)for packet in tokens[:-2])
    actualF=pose_after(Fprefix);assert actualF==(5,5,0)
    actualReturn=pose_after(owner.WORDS['F'],actualF);assert actualReturn==(1,3,2)
    normalizedF=(*lit.rot(sub(actualF[:2],old_C_pose[:2]),-old_C_pose[2]),(actualF[2]-old_C_pose[2])%4)
    normalizedReturn=(*lit.rot(sub(actualReturn[:2],old_C_pose[:2]),-old_C_pose[2]),(actualReturn[2]-old_C_pose[2])%4)
    assert normalizedF==(2,-5,1)and normalizedReturn==(0,-1,3)
    endpoint=pose_after(owner.WORDS['C'],actualReturn)
    zold=add((2*old_C_pose[0],2*old_C_pose[1]),lit.rot((-1,-1),old_C_pose[2]))
    zend=add((2*endpoint[0],2*endpoint[1]),lit.rot((-1,-1),endpoint[2]))
    assert zold==zend
    assert greads[2]==('R',len(raw)+7)
    assert len(seed)==(29 if tokens[4]=='VC' else 30)
    # In these replay frames source parent DC is at0N, so the older parentD
    # chord is(-1,-1)->(1,1); helper V entry is(-1,0,E).
    cross=hit(*chord((0,0,0),'D'),*chord((-1,0,1),'V'))
    assert cross['s']==cross['t']==[1,2]
    common_prefix=G[1]['word']*3+owner.WORDS['D']
    helper_tick=len(common_prefix);assert helper_tick==85
    owner_at_death=owner.describe(tokens[4],104-helper_tick)
    assert owner_at_death['owner_tick0']==1 and owner_at_death['owner_read_number1']==2
    controls.append(dict(tokens=tokens,complete_finite_seed=seed,RAW_length=len(raw),
        actual_physical_read_count=len(actual),full_physical_read_consistency=True,
        genuine_first_parent_DC_bud_physical_site=(2,0),all_actual_bud_reads=greads,
        original_bud_R_birth_tick0=8,original_bud_first_L_tick0=104,
        helper_entry_tick0=helper_tick,canonical_clearing_L_owner=owner_at_death,
        original_bud_consumer_age=3,
        genuine_preforeign_parent_D_helper_V_midpoint_crossing=cross,
        no_earlier_uninterrupted_eight_U_entry_lift='Both crossing old chords would lie after any such U entry, violating signed old simplicity.',
        actual_selected_old_C1_pose=old_C_pose,actual_F_pose=actualF,actual_returned_C_pose=actualReturn,
        normalized_F_pose=normalizedF,normalized_returned_C_pose=normalizedReturn,
        returned_C_end_equals_selected_old_C_start=True,
        target_scope='Prepared actual same final C75 geometry and genuine bud clearing, NOT a U-entry catalogue attainment.'))
assert len(controls)==2

deps=[GP,CP,CP.parent/'manifest.json',H/'first_returned_three_F_frontier_manifest.json',
      H/'three_F_parent_assembly_signoff_manifest.json',
      R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',
      R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_C75_K0_ANCESTOR_BUD_GUARD_WITH_POSITIVE_CONTROLS_PENDING_REVIEW',
    scope='Only C75 immediate DC or VC last-positive-C parent, zero intervening D (k0), in actual U-entry old8 history before firstF. Original genuine older exit-bud first retirement, all full-source/consumer completion and marker ownership retained. k1/k2 untouched.',
    two_actual_parent_birth_and_clock_roles=births,
    all230_source_age0_to4_actual_input_queries=queries,
    disposition_counts=dict(Counter(q['disposition']for q in queries)),
    four_surviving_DC_V_VC_inputs=survive,
    two_actual_old_chord_strict_midpoint_obstructions=contacts,
    required_before_WHITE=dict(physical_cell=g,F_local_cell=local,foreign_RAW_misses=True,
        combined_F_RAW_C_M_first_R_tick0=78,canonical_actual_owner=physical_owner),
    identity_core_completeness='The original BLACK residual can first retire only at a true full input, including marker-only absorption before its physical L. No arbitrary later core R rewrite can precede that first retirement. Therefore no first-R repair inventory is omitted.',
    two_real_finite_board_genuine_bud_clearing_controls=controls,
    conclusion='The older bud cannot retire in the actual U-entry factor, remains BLACK at F, and contradicts actual next-word R7/read8 before-WHITE. Both C75 k0 parents are excluded.',
    remaining_C75_last_positive_C_parents=['DC,D','DC,DD','VC,D','VC,DD'],
    no_generic_bud_permanence_or_source_free_clearing_impossibility_claimed=True,
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(H/'C75_immediate_DC_VC_ancestor_bud.json').write_text(json.dumps(out,indent=2)+'\n')
print('230 actual age0..4 input rows ->4V/VC cases, all forbidden by genuine older D/C midpoint crossings.')
print('Two complete29/30-black clearing controls replay248/256 reads but have the exact forbidden old crossing.')
