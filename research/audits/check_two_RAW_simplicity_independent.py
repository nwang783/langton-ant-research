import json,hashlib,itertools
from pathlib import Path
from collections import Counter
R=Path('/workspace/shared/langton');P=R/'first_foreign_two_ordinary_simplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
man=P/'manifest.json';assert sha(man)=='3420cd04ea53ef20a603672481463f8bf6774595528441e8f9140124d2d84f76';mf=json.loads(man.read_text())
for f,h in mf['files'].items():assert sha(P/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
# Independently authored literal geometry code, rerun without writing its frozen report.
f=R/'audits/check_second_ordinary_small_interface_independent.py';ns={'__file__':str(f)};exec(f.read_text().split("out={'status'")[0],ns)
W,M,pose,chord,pieces,meet,cross,minus=[ns[k]for k in ['W','M','pose','chord','pieces','meet','cross','minus']]
J=json.loads((P/'two_ordinary_simplicity.json').read_text());A=json.loads((R/'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry.json').read_text())
local=[]
for h in range(4):
 for a in'FQB':
  ps,ep,vs=pieces(a,0j,h)
  for b in'DCVU':
   bc=chord(b,*ep);p2=pose(b,*ep)
   for c in'DCVU':
    cc=chord(c,*p2);assert all(meet(*p,*cc)is None for p in ps)
    ht=meet(*bc,*cc)
    if cross(minus(bc[1],bc[0]),minus(cc[1],cc[0])):assert ht[:2]==(1,0)
    else:assert ht==(bc[1],)
    local.append((a,b,c,h,tuple(vs),bc,cc))
assert len(local)==192
canon=lambda v:json.dumps(v,sort_keys=True)
for a,b,c,h,vs,bc,cc in local:
 row=next(r for r in J['all192_rotation_checked_FOREIGN_b1_b2_local_closed_segment_interfaces']if(r['foreign'],r['first'],r['second'],r['actual_heading'])==(a,b,c,h))
 assert canon([vs,bc,cc])==canon([row['true_foreign_piece_vertices'],row['first_chord'],row['second_chord']])
for b,c in itertools.product('DCVU',repeat=2):
 assert (W[c]+M)[:11]==M
 row=next(r for r in J['all16_actual_terminal_marker_supply_cases']if(r['first'],r['second'])==(b,c))
 assert (row['actual_b2_RAW_reads_used'],row['actual_final_M_reads_used'])==(min(len(W[c]),11),max(0,11-len(W[c])))
# Every angle is generated anew with true age n distinguished from effective N.
angles=ns['angles'];ak=lambda r:(r['old_source'],r['first_ordinary'],r['second_ordinary'],r['actual_old_source_to_FOREIGN_C_age'],r['total_ordinary_C_before_second'],r['second_heading_relative_old_source'],r['foreign_heading_relative_old_source'])
assert set(angles)==set(map(ak,A['conditional217_old_source_angle_interfaces']))
rows=J['all217_original_angle_IDs_with_signed_source_exclusion'];assert len(rows)==217
for i,r in enumerate(rows):assert r['original217_angle_index0']==i and r['exact_original_angle']==A['conditional217_old_source_angle_interfaces'][i]
assert Counter(r[0]for r in angles)=={'D':54,'C':44,'V':59,'U':60}
prior=R/'audits/remaining24_second_contact_angles_independent.json';pr=json.loads(prior.read_text());assert sha(prior)=='4fed375c6c9d3ea24e7549c865f331a92e3b48a781b25f1e0b2ff0bd34cdb8fe'
for f,h in pr['dependencies'].items():assert sha(R/f)==h
remaining=set(map(ak,pr['remaining']));assert len(remaining)==24 and remaining<set(angles)
assert remaining=={r for r in angles if r[0]in'DC'and r[3]==3}
# Exact mask/real-containing-role joins, not merely 24 counts.
cur=json.loads((R/'second_contact_signed_obligations_2026-10-24/signed_current_obligations.json').read_text())
key=lambda r:(r['foreign'],r['first'],r['second'],tuple(r['foreign_pose']),tuple(r['second_pose']))
dj=json.loads((R/'old_D_second_age3_next_base_2026-10-24/next_base_guard.json').read_text())
cj=json.loads((R/'second_old_C_age3_2026-10-24/C_age3_source_reserve.json').read_text())
for old in'DC':
 base=[r for r in cur['all267_foreign_typed_base_rows']if r['old']==old and r['n']==3];bk={(r['A'],r['b1'],r['b2'],tuple(r['pa']),tuple(r['p2']))for r in base};assert len(bk)==54
 assert {(r['b1'],r['b2'])for r in base}=={(r[1],r[2])for r in remaining if r[0]==old}
 if old=='D':
  rr=dj['all108_actual_source_role_contact_cases'];assert len(rr)==108
  assert {(r['actual_full_source'],key(r))for r in rr}=={(s,k)for s in('D','DC')for k in bk}
  assert rr==J['direct54_pose_keys_per_actual_D_DC_source_and108_role_proof_cases']
 else:
  roles={('DC',1),('VC',1),('VCC',1),('VCC',2),('UC',1),('UCC',1),('UCC',2)}
  rr=cj['all378_role_specific_actual_before_mask_conflicts'];assert len(rr)==378
  actual={(r['actual_full_source'],r['selected_C_index1'],(r['foreign'],r['first'],r['second'],tuple(r['FOREIGN_pose']),tuple(r['second_pose'])))for r in rr}
  assert actual=={(s,j,k)for s,j in roles for k in bk}and all(r['all_guaranteed_same_CURRENT_witnesses']for r in rr)
  assert rr==J['direct7_real_C_containing_roles_and378_pose_role_conflicts']
report={'status':'PASS actual U-entry G8 prefix + FIRST foreign + exactly TWO immediate ordinary RAW atoms with actual final M11 has simple OPEN corrected-center proxy','manifest_sha256':sha(man),'script_sha256':sha(Path(__file__)),'dependencies':mf['dependencies'],'local_rotated_closed_segment_checks':192,'actual_marker_supply_cases':16,'literal_immediate_old_contacts':ns['contacts'],'original_angles':217,'source_counts':dict(Counter(r[0]for r in angles)),'D_actual_roles':108,'C_actual_roles':378,'analytic_review':['The actual second RAW plus final M supplies the one-RAW theorem recognition prefix, including D10 spilling precisely one actual next-word read. No inserted second M or marked core is assumed.','Closed-segment geometry excludes every true F-prefix/Q-B-tail and b1 except genuine terminal adjacency in all rotations, including singleton collinear adjacency. Thus the start of b2 is disjoint from the old G8 compact arc.','A hypothetical contact has a positive earliest new parameter. At an old vertex the outgoing old atom owns it; old terminal lies on foreign and is already excluded. Same-direction collinear onset occurs at an outgoing start and is retained; an opposite approach would overlap that outgoing chord before the alleged first contact. Old initial vertex remains included.','The old subarc and first new contacting chord form the actual Jordan loop needed by the signed angle formula. Only b1=C increments effective N; source maturity uses true preforeign n. Every genuine internal C keeps its complete containing producer and clock shift.','Signed 193-angle dependency closure plus exact final D108/C378 joins eliminates all217 necessary interfaces, hence an actual earliest contact cannot occur. This is the explicit finite-to-geometric bridge, not an inference from catalogue size alone.','All lifetime laws stop before foreign or use exact complete-context masks. Mandatory389 permits old physical identity alive in CORE when only external CURRENT absence is known. Later-U prepared positives and withdrawn full-output seal remain untouched.'],'not_claimed':['fine-walk selfavoidance','third RAW','later full C tail','second foreign','unrestricted language coverage','global capture']}
p=R/'audits/two_RAW_simplicity_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
