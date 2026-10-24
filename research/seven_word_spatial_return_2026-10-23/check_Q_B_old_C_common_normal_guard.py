"""Target-level Q/B obstruction, with all seven real C-source roles.

No predecessor classification is needed. Before age3 all actual full consumer
roles are excluded; at age3 exact E exits cannot reach Q/B with legal final type.
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

source_roles=[];young=[]
for sid,j in((1,1),(5,1),(6,1),(6,2),(8,1),(9,1),(9,2)):
    packet=G[sid]['name'];base=packet[0];prefix=owner.WORDS[base]+owner.WORDS['C']*(j-1)
    cp=pose_after(prefix);q=add(cp[:2],lit.rot((2,0),cp[2]))
    raw=lit.trace(G[sid]['word']);assert raw['feasible']
    assert list(q)in G[sid]['outputs']
    assert raw['last'][q]==('R',len(prefix)+8)
    own=owner.describe(packet,len(prefix)+8)
    assert own['owner_tick0']==8 and own['owner_read_number1']==9
    source_roles.append(dict(actual_full_source=packet,actual_C_index=j,
        C_entry_pose_in_actual_full_source=cp,common_output_full_source_slot=q,
        last_actual_R_full_context_tick0=len(prefix)+8,canonical_physical_birth_owner=own,
        full_source_entry_to_atomic_C_entry_C_shift=j-1,
        own_later_C_tails_preserve_original_common_identity=True))
    for atomic_age in range(3):
        full_age=atomic_age+j-1;h=(cp[2]-atomic_age)%4
        for cid in KEEP:
            for inp in map(tuple,G[cid]['inputs']):
                z=lit.rot(inp,h);p=(q[0]-z[0],q[1]-z[1])
                key=(KEEP.index(sid),KEEP.index(cid),*p,h,*q,full_age)
                reason='sector'if(sum(p)+h)%2 else None
                if reason is None and packet.count('C')>full_age:
                    reason='actual_source_full_packet_not_yet_completed'
                if reason is None:
                    assert key in COUNT;reason='signed_COUNT5'
                young.append(dict(actual_full_source=packet,actual_C_index=j,
                    atomic_C_source_included_age=atomic_age,
                    full_source_entry_included_age=full_age,
                    consumer=G[cid]['name'],actual_input=inp,consumer_pose=(*p,h),
                    common_full_source_slot=q,exact_COUNT5_key=key,exclusion=reason))
assert len(source_roles)==7 and len(young)==483

# At age3, any full old consumer finishing before same-clock foreign is plain:
# a real own C tail would advance the clock and cannot be silently dropped.
align=[]
for cid in(0,4,7):
    for inp in map(tuple,G[cid]['inputs']):
        z=lit.rot(inp,1);p=(2-z[0],-z[1])
        end=add(p,lit.rot(G[cid]['endpoint'][:2],1))
        assert sum(end)>=1
        first=lit.trace(G[cid]['word']+lit.M)['first'][inp]
        assert first[0]=='L'
        align.append(dict(actual_plain_E_consumer=G[cid]['name'],actual_input=inp,
            consumer_entry_in_old_C_frame=(*p,1),actual_full_RAW_exit=(*end,1),
            exit_normal_x_plus_y=sum(end),
            canonical_physical_input_owner=owner.describe(G[cid]['name'],first[1])))
assert len(align)==8
minimum=[q for q in align if q['exit_normal_x_plus_y']==1]
assert len(minimum)==3 and all(q['actual_full_RAW_exit']==(2,-1,1)for q in minimum)
steps=[]
for cid in(0,4,7):
    q=lit.rot(G[cid]['endpoint'][:2],1)
    assert sum(q)=={'D':0,'V':2,'U':4}[G[cid]['name']]
    steps.append(dict(actual_plain_E_packet=G[cid]['name'],step=q,normal_increment=sum(q)))

targets=[]
for foreign,pose,tick in(('Q',(4,-5,1),53),('B',(5,-4,1),63)):
    common=(2,0);rel=(common[0]-pose[0],common[1]-pose[1]);local=lit.rot(rel,-pose[2])
    tr=lit.trace(owner.WORDS[foreign]);assert tr['feasible']
    assert tr['first'][local]==('R',tick)
    actual_owner=owner.describe(foreign,tick)
    assert actual_owner['owner_tick0']==tick and actual_owner['owner_read_number1']==tick+1
    normal=sum(pose[:2])
    if foreign=='Q':
        assert normal==-1 and all(q['exit_normal_x_plus_y']>normal for q in align)
        argument='Every possible first-consumer exit has normal>=1; zero-C E steps never decrease normal, so Q target normal=-1 is unreachable.'
    else:
        assert normal==1
        delta=(pose[0]-2,pose[1]+1);assert delta==(3,-3)
        assert delta==tuple(3*x for x in lit.rot(G[0]['endpoint'][:2],1))
        argument='Only normal1 exits survive. All equal(2,-1,E), followed necessarily by exactly three plain Ds; final old packet is D, contradicting actual B predecessor U.'
    targets.append(dict(foreign=foreign,actual_foreign_entry_in_old_C_frame=pose,
        original_common_output=(2,0),actual_foreign_local_cell=local,
        first_actual_RAW_read=('R',tick),canonical_actual_read_owner=actual_owner,
        target_normal_x_plus_y=normal,first_consumer_endpoint_obstruction=argument,
        final_contradiction='Original common identity has no possible first old consumer and remains BLACK, but foreign first reads it R/WHITE.'))

# Positive F context omission is retained. This proof cannot be imported there.
fpose=(2,-5,1);flocal=lit.rot((2-fpose[0],-fpose[1]),-1)
assert flocal not in lit.trace(owner.WORDS['F']+owner.WORDS['C']+lit.M)['first']

deps=[GP,CP,CP.parent/'manifest.json',H/'returned_C_source_reduction_manifest.json',
      H/'first_returned_atom_contact_manifest.json',H/'complete8_foreign_adjacency_manifest.json',
      R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',
      R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_TARGET_LEVEL_Q_B_C_COMMON_NORMAL_GUARD_PENDING_REVIEW',
    scope='Exactly C76/C77 of the actual FIRST-returned-atom catalogue after one first foreign. All seven real old-C full-source roles retained. No predecessor-parent reduction is needed; F/C75 and D15/D30 are untouched.',
    all7_actual_C_source_birth_and_clock_roles=source_roles,
    all483_atomic_age0_to2_real_full_source_input_queries=young,
    young_query_reason_counts=dict(Counter(q['exclusion']for q in young)),
    all8_actual_age3_plain_E_input_alignments=align,
    all3_zero_C_E_normal_steps=steps,
    minimum_normal_exit_roles=minimum,
    two_exact_target_RAW_and_endpoint_contradictions=targets,
    F_common_output_absence_control=True,
    C76_and_C77_excluded_for_all_real_containing_source_roles=True,
    no_postforeign_maturation_or_internal_marker_assumed=True,
    remaining_coarse_catalogue_labels=(15,30,75),
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(H/'Q_B_old_C_common_normal_guard.json').write_text(json.dumps(out,indent=2)+'\n')
print('7 genuine C roles;483 exact young consumer queries:',out['young_query_reason_counts'])
print('8 actual E input exits;Q normal -1 impossible;B normal1 forces finalD, not mandatoryU.')
