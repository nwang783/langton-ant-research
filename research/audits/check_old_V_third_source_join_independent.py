from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'old_V_third_source_join_2026-10-24';Y=R/'old_V_third_young_complete_ancestry_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='9c33cd29e1f923d6aaf37b80dcaaa81eabb248651fd8fd729d6aff6203cefb9b'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'V_third_join.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
q=Y/'mandatory_qualifications_manifest.json';assert sha(q)=='b5f5db6052810a5c943f67aa1ac9af2f454dd918ad25da7c139ee99072bc3800'
for f,h in json.loads(q.read_text())['files'].items():assert sha(Y/f)==h
for f,h in json.loads((Y/'collinear_metadata_qualification_manifest.json').read_text())['files'].items():assert sha(Y/f)==h
qual=json.loads((Y/'collinear_metadata_qualification.json').read_text());own=json.loads((R/'audits/check_old_V_third_young_contact_qualification_independent.json').read_text());assert{(r['tokens'],r['old_piece'],r['new_piece'])for r in qual['all_corrected_legitimate_collinear_joins']}==set(map(tuple,own['corrections']))and len(own['corrections'])==180
allangles=json.loads((R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json').read_text())['all831_conditional_preFOREIGN_old_source_angle_interfaces'];angles=[a for a in allangles if a['old_source']=='V'];parts={
'young':[r['angle']for r in json.loads((Y/'young_ancestry.json').read_text())['all101_signed_angle_boxes']],
'age2':[r['angle']for r in json.loads((R/'old_V_third_age2_genuine_field_2026-10-24/age2_field.json').read_text())['all62_signed_angle_contact_boxes']],
'older':json.loads((R/'V_postforeign_pair_rail_reserve_2026-10-24/pair_rail_reserve.json').read_text())['all66_signed_angle_cases']}
canon=lambda a:json.dumps(a,sort_keys=True);assert len(angles)==len(set(map(canon,angles)))==229;assert Counter(map(canon,angles))==Counter(map(canon,sum(parts.values(),[])))
assert Counter(a['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age']for a in angles)=={0:37,1:64,2:62,3:48,4:18}
for idx,row in enumerate(J['all229_exact_V_angle_routes']):
 a=angles[idx];n=a['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];part='young'if n<=1 else'age2'if n==2 else'older';assert row['angle']==a and row['proof_package']==part and row['actual_full_sources']==(['V']if n==0 else['V','VC']if n==1 else['V','VC','VCC'])
reports=['check_old_V_third_young_independent.json','check_old_V_third_young_contact_qualification_independent.json','check_old_V_third_age2_independent.json','check_V_pair_rail_independent.json','check_V_pair_simultaneous_qualification_independent.json']
out=dict(status='PASS exact229 oldV THIRD source composition WITH mandatory metadata/prose and simultaneous-input qualifiers',manifest=sha(MF),mandatory_young_qualifiers=sha(q),all229_disjoint_age_counts=[37,64,62,48,18],independent_reports={f:sha(R/'audits'/f)for f in reports},analytic_review=[
'All229 oldV angles equal the disjoint union101young+62age2+66older by exact full records, not just cardinalities. Sourcefull completion isVonly0,V/VC1,V/VC/VCColder. TruepreFOREIGNage is not totalangleage with returnedC additions.',
'Young source endpoint/ancestry proof requires NO prepared-simple-history assertion. Mandatory authorb5f5db60 and independentd38184a5 correct180 false nonparallel-only adjacency flags and withdraw the erroneous earlier-contact prose; one copied sentence in mainb13 report is explicitly superseded. All endpoint/color/identity/predecessor data remain unchanged.',
'Age2 keeps both genuine currentA/helper fields and possible originalA aliveCORE. Older pair reserve binds b84be11b:24WHITE+3CORE+9 actual source contacts, not36 literal conflicts. UpperU retained, no postforeign age.',
'The result excludes only an outgoing preforeign oldV owner of the chronological GLOBAL FIRST contact in THIRD ordinaryRAW afterFIRSTforeign, under genuineU-entry complete8 prefix and actualfinalM. Overall finite-to-geometric THIRD assembly is separate; no fourth atom, laterforeign, arbitrary-tail seal or capture.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
