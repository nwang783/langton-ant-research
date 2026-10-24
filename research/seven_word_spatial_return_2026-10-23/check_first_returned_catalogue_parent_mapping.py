"""Explicit frozen catalogue IDs versus parent-row / typed-row COUNTS.

D14 andD28 never mean catalogue IDs14 or28. Actual source events, older
parents, poses, source clocks and outgoing contact owners remain distinct.
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
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
G=json.loads(GP.read_text())['geometry'];FULL={q['name']:q['word']for q in G}
cat=json.loads((H/'first_returned_atom_contact.json').read_text())
labels=cat['old_source_contact_cases'];roles={q['case']:q['roles']for q in cat['actual_old_fullproducer_clock_annotations']}
D=json.loads((R/'returned_D_final_parent_exhaustion_2026-10-24/D_final_parent_exhaustion.json').read_text())
prior=json.loads((R/'returned_D_last_C_parent_reduction_2026-10-24/D_last_C_parent_reduction.json').read_text())
three=json.loads((H/'first_returned_three_F_frontier.json').read_text())

def add(p,q):return p[0]+q[0],p[1]+q[1]
def pose_after(word,pose):
    p=pose[:2];h=pose[2]
    for c in word:
        h=(h+(1 if c=='R'else-1))%4;p=add(p,lit.DIRS[h])
    return(*p,h)

case_rows=[]
for cid,returned,fp,rp,s,t in((15,'C',(2,-5,1),(0,-1,3),Q(0),Q(1)),(30,'V',(3,-4,1),(1,0,3),Q(1,2),Q(1,2))):
    q=labels[cid]
    assert q['source_atom']=='D'and q['returned_atom']==returned and q['foreign']=='F'
    assert tuple(q['foreign_pose'])==fp and tuple(q['returned_pose'])==rp
    assert q['source_to_foreign_C_age']==3
    assert Q(str(q['contact']['s']))==s and Q(str(q['contact']['t']))==t
    assert {x['full_packet']for x in roles[cid]}=={'D','DC'}
    assert all(x['full_source_C_age']==3 and x['full_source_completed']for x in roles[cid])
    case_rows.append(dict(frozen_catalogue_ID=cid,actual_frozen_geometry=q,
        actual_contact_source_full_roles=roles[cid]))

necessary={(q['catalogue_id'],q['last_positive_C_full_packet'],q['actual_pre_D_zero_C_word']):q for q in prior['fourteen_remaining_genuine_DC_VC_interfaces']}
actual={(q['catalogue_id'],q['last_positive_C_parent'],q['actual_pre_selectedD_N_word']):q for q in D['all14_excluded_parent_run_rows']}
assert necessary.keys()==actual.keys()and len(actual)==14
mapped=[]
for key,q in actual.items():
    cid,parent,word=key;assert cid in(15,30)and parent in('DC','VC')
    n=necessary[key];entry=tuple(q['actual_parent_entry'])
    assert list(entry)==n['packet_entry']
    ep=pose_after(FULL[parent],entry)
    assert list(ep)==n['packet_exit']
    assert pose_after(''.join(FULL[a]for a in word),ep)==(0,0,0)
    actual_lastC=pose_after(FULL[parent][:-15],entry)
    assert list(actual_lastC)==q['actual_final_C_entry']==n['last_actual_C_entry']
    assert actual_lastC[2]==1 and ep[2]==0
    assert parent.count('C')==1 # actual firstC, not an invented source label
    assert ep!=(0,0,0)or word==''
    mapped.append(dict(frozen_catalogue_ID=cid,
        actual_older_parent_fullpacket=parent,actual_older_parent_entry=entry,
        actual_older_parent_C1_entry=actual_lastC,actual_older_parent_exit=ep,
        exact_intervening_plain_N_word=word,
        actual_outgoing_contact_D_entry=(0,0,0),
        foreign_pose_from_same_frozen_case=labels[cid]['foreign_pose'],
        contact_parameters_from_same_frozen_case=labels[cid]['contact'],
        parent_full_entry_clock=0,parent_C1_entry_clock=0,
        outgoing_D_entry_clock=1,foreign_entry_clock=4,
        actual_outgoing_owner_unchanged=q['actual_outgoing_contact_owner']))
assert Counter(q['frozen_catalogue_ID']for q in mapped)=={15:10,30:4}

typed={}
for q in D['all28_actual_selected_source_D_DC_roles']:
    key=(q['catalogue_id'],q['last_positive_C_parent'],q['actual_pre_selectedD_N_word'],q['actual_selected_full_packet'])
    assert key not in typed
    parentkey=key[:3];assert parentkey in actual
    assert q['actual_selected_full_packet']in {a['full_packet']for a in roles[q['catalogue_id']]}
    assert q['exclusion']==actual[parentkey]['exclusion']
    assert q['guard_applies_before_F_and_preserves_actual_own_tail']==(q['actual_selected_full_packet']=='DC')
    typed[key]=q
expected={(*key,source)for key in actual for source in('D','DC')}
assert set(typed)==expected and len(typed)==28
assert Counter(k[0]for k in typed)=={15:20,30:8}

# C75 has a DIFFERENT contact source. Its earlier DC/VC parent is not that
# containing source event even if the packet names happen to agree.
c75=labels[75]
assert c75['source_atom']=='C'and c75['returned_atom']=='C'and c75['foreign']=='F'
assert tuple(c75['foreign_pose'])==(2,-5,1)and tuple(c75['returned_pose'])==(0,-1,3)
assert Q(str(c75['contact']['s']))==0 and Q(str(c75['contact']['t']))==1
reduced=next(q for q in three['three_necessary_labels_with_actual_containing_roles']if q['catalogue_case']==75)
assert [q['full_packet']for q in reduced['remaining_actual_containing_fullsource_roles']]==['DC']
assert pose_after(FULL['D'],(0,0,0))==(1,1,0)
assert (2+1,-5+1,1)==(3,-4,1)
crows=[]
for q in three['signed_C75_last_positive_C_parent_interfaces']:
    parent=q['last_positive_C_fullpacket'];k=q['intervening_plain_D_count']
    entry=tuple(q['actual_predecessor_packet_entry_in_selected_D_frame'])
    ep=pose_after(FULL[parent],entry)
    assert ep==(-k,-k,0)and pose_after(FULL['D']*k,ep)==(0,0,0)
    crows.append(dict(frozen_catalogue_ID=75,actual_old_contact_atom='C1',
        actual_contact_containing_source='DC',actual_contact_containing_D_entry=(0,0,0),
        actual_contact_C1_entry=(1,1,0),actual_earlier_last_C_parent=parent,
        actual_earlier_parent_entry=entry,intervening_plain_D_count=k,
        foreign_in_C_frame=(2,-5,1),foreign_in_containing_D_frame=(3,-4,1)))
assert len(crows)==6

paths=[GP,H/'first_returned_atom_contact_manifest.json',
       R/'returned_D_final_parent_exhaustion_2026-10-24/manifest.json',
       R/'audits/check_D_final_parent_exhaustion_independent.json',
       H/'first_returned_three_F_frontier_manifest.json',H/'three_F_parent_assembly_signoff_manifest.json',
       H/'first_foreign_first_returned_atom_simplicity_manifest.json',
       R/'audits/check_first_foreign_returned_simplicity_independent.json']
assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_FROZEN_EXPLICIT_CATALOGUE_PARENT_TYPED_MAPPING_PENDING_REVIEW',
    purpose='Mandatory explicit reconciliation for final9aa9751b assembly. D14 means14 parent/run rows associated ONLY with actual frozen catalogue IDs15/30;D28 means their28 sourceD/DC choices, NOT catalogue IDs14/28.',
    two_actual_frozen_D_catalogue_rows=case_rows,
    all14_direct_catalogue_parent_pose_clock_mappings=mapped,
    all28_typed_role_keys=[list(k)for k in sorted(typed)],
    typed_count_by_actual_catalogue_ID={15:20,30:8},
    all6_distinct_C75_contact_source_and_earlier_parent_mappings=crows,
    temporal_source_events_not_merged_by_equal_packet_names=True,
    exactly_one_immediate_RAW_atom_scope_unchanged=True,
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'first_returned_catalogue_parent_mapping.json').write_text(json.dumps(out,indent=2)+'\n')
print('Actual catalogue15/30 ->14 exact parent/run mappings ->28 D/DC typed roles(20/8).')
print('C75 oldcontactC1/DC event kept distinct from its6 earlierDC/VC parent/run events.')
