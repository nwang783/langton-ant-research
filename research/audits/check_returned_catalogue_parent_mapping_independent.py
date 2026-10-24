from pathlib import Path
from collections import Counter
from fractions import Fraction
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'seven_word_spatial_return_2026-10-23';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
man=D/'first_returned_catalogue_parent_mapping_manifest.json';assert sha(man)=='d284a4af95c88572bbd11cc0779d148cae5234fbaeeeb25f801eb2030bae5065';m=json.loads(man.read_text())
for p,h in m['files'].items():assert sha(D/p)==h
for p,h in m['dependencies'].items():assert sha(R/p)==h
ns={'__file__':str(S.with_name('check_foreign_kinked_barrier_turn_independent.py'))};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns);W=ns['W']
def end(word,p=0j,h=0):
 for ch in word:h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 return [int(p.real),int(p.imag),h]
a=json.loads((D/'first_returned_catalogue_parent_mapping.json').read_text());cat=json.loads((D/'first_returned_atom_contact.json').read_text());labels=cat['old_source_contact_cases'];roles={q['case']:q['roles']for q in cat['actual_old_fullproducer_clock_annotations']}
for ix,tar,fp,rp,st in [(15,'C',[2,-5,1],[0,-1,3],(0,1)),(30,'V',[3,-4,1],[1,0,3],(Fraction(1,2),Fraction(1,2)))]:
 z=labels[ix];assert(z['source_atom'],z['foreign'],z['returned_atom'],z['foreign_pose'],z['returned_pose'],z['source_to_foreign_C_age'])==('D','F',tar,fp,rp,3)
 assert tuple(Fraction(z['contact'][k])for k in ['s','t'])==st and {v['full_packet']for v in roles[ix]}=={'D','DC'}
keys=[]
for z in a['all14_direct_catalogue_parent_pose_clock_mappings']:
 ix=z['frozen_catalogue_ID'];p=z['actual_older_parent_fullpacket'];word=z['exact_intervening_plain_N_word'];ep=z['actual_older_parent_entry'];w=W[p[0]]+W['C'];pe=end(w,complex(*ep[:2]),ep[2]);ce=end(W[p[0]],complex(*ep[:2]),ep[2]);assert pe==z['actual_older_parent_exit'] and ce==z['actual_older_parent_C1_entry'];assert end(''.join(W[t]for t in word),complex(*pe[:2]),pe[2])==[0,0,0]
 assert[z['parent_full_entry_clock'],z['parent_C1_entry_clock'],z['outgoing_D_entry_clock'],z['foreign_entry_clock']]==[0,0,1,4]
 assert z['foreign_pose_from_same_frozen_case']==labels[ix]['foreign_pose'] and z['contact_parameters_from_same_frozen_case']==labels[ix]['contact'];keys.append((ix,p,word))
assert len(set(keys))==14 and Counter(q[0]for q in keys)=={15:10,30:4}
assert {tuple(z)for z in a['all28_typed_role_keys']}=={(*k,s)for k in keys for s in ['D','DC']}
for z in a['all6_distinct_C75_contact_source_and_earlier_parent_mappings']:
 assert z['frozen_catalogue_ID']==75 and z['actual_contact_containing_source']=='DC' and z['actual_old_contact_atom']=='C1'
 p=z['actual_earlier_last_C_parent'];ep=z['actual_earlier_parent_entry'];k=z['intervening_plain_D_count'];pe=end(W[p[0]]+W['C'],complex(*ep[:2]),ep[2]);assert pe==[-k,-k,0] and end(W['D']*k,complex(*pe[:2]),0)==[0,0,0]
 assert end(W['D'])==z['actual_contact_C1_entry']==[1,1,0]
out={'status':'PASS mandatory explicit catalogue IDs versus parent/source-row counts','author_manifest':sha(man),'actual_coarse_catalogue_ids':[15,30],'parent_row_counts':{'15':10,'30':4,'total':14},'typed_D_DC_row_counts':{'15':20,'30':8,'total':28},'C75_actual_contact_owner':'C1 inside the selected DC, not its earlier last-positive-C parent','C75_older_parent_rows':6,'literal_pose_compositions_checked':20,'clocks':'older parent full entry0/C1 entry0; selected outgoingD entry1; foreign4, equivalent source-to-foreign age3','scope':'No catalogue relabeling. D14/D28 was only ambiguous shorthand for fourteen parent/run rows and twenty-eight source-typed rows; use explicit words. One immediate ordinary RAW atom only.'}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
