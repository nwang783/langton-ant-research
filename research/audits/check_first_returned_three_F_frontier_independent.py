from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';manifests=['first_returned_three_F_frontier_manifest.json','three_F_parent_assembly_signoff_manifest.json'];expected=['d77c5e042fe1e73ec40e898025c18ef65e76b4b3c958588c323fd62f02c7fd3a','ca5ba2718ad039c05001e4273083c35feef78c2f3c463a77192d39dbc51748c5'];bindings={}
for f,hh in zip(manifests,expected):
 p=D/f;assert hashlib.sha256(p.read_bytes()).hexdigest()==hh;mf=json.loads(p.read_text());bindings[f]=hh
 for name,h in mf['files'].items():assert hashlib.sha256((D/name).read_bytes()).hexdigest()==h
 for field in ['dependencies','signed_dependencies','separate_D_parent_assembly_dependencies']:
  for name,h in mf.get(field,{}).items():assert hashlib.sha256((R/name).read_bytes()).hexdigest()==h
cat=json.loads((D/'first_returned_atom_contact.json').read_text())['old_source_contact_cases'];old=json.loads((D/'first_returned_five_label_frontier.json').read_text());A=json.loads((D/'first_returned_three_F_frontier.json').read_text());cnt=Counter(z['source_atom']for z in cat);assert cnt=={'D':60,'C':51,'V':112,'U':148}
prior=old['all_five_necessary_labels_with_actual_fullsource_roles'];remain=[z for z in prior if z['catalogue_case']not in[76,77]];assert remain==A['three_necessary_labels_with_actual_containing_roles'];assert[z['catalogue_case']for z in remain]==[15,30,75]
assert[[x['full_packet']for x in z['remaining_actual_containing_fullsource_roles']]for z in remain]==[['D','DC'],['D','DC'],['DC']]
assert all(z['foreign']=='F'and z['source_to_foreign_C_age']==3 for z in remain);assert sum(A['signed_excluded_source_counts'].values())==368
DP=json.loads((R/'returned_D_last_C_parent_reduction_2026-10-24/D_last_C_parent_reduction.json').read_text());drows=DP['fourteen_remaining_genuine_DC_VC_interfaces'];assert drows==A['fourteen_worker_D_last_positive_C_parent_interfaces'];dr={(z['catalogue_id'],z['last_positive_C_full_packet'],z['actual_pre_D_zero_C_word'])for z in drows}
assert dr=={(15,p,w)for p in['DC','VC']for w in['','D','DD','DDD','V']}|{(30,p,w)for p in['DC','VC']for w in['D','DD']}
crows=A['signed_C75_last_positive_C_parent_interfaces'];assert{(z['last_positive_C_fullpacket'],z['intervening_plain_D_count'])for z in crows}=={(p,k)for p in['DC','VC']for k in[0,1,2]};assert len(drows)+len(crows)==20
# Fresh creating-D frame transform and non-lift of the returnedV input guard.
p=SELF.with_name('check_foreign_kinked_barrier_turn_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('geometries=[]')[0],ns);W,M,walk=ns['W'],ns['M'],ns['walk'];d=walk(W['D']);assert(d['p'],d['h'])==(1+1j,0)
assert d['p']+(2-5j)==3-4j and d['p']-1j==1+0j
assert W['V'][13]=='L'and W['C'][13]=='R'
gate=json.loads(SELF.with_name('check_returned_D_forced_core_ports_independent.json').read_text());assert gate['status'].startswith('PASS')and[z['case']for z in gate['two_submitted_and_one_compatible_C75_port_transcript']]==[15,30,75]
out={'status':'PASS joint three-F frontier and signed14+6 parent boundary, necessary only','joint_manifest_hashes':bindings,'source_counts':dict(cnt),'excluded_counts':A['signed_excluded_source_counts'],'remaining_coarse_labels':[15,30,75],'actual_containing_fullsources':[['D','DC'],['D','DC'],['DC']],'D_parent_run_rows':sorted(dr),'C75_parent_run_rows':sorted((z['last_positive_C_fullpacket'],z['intervening_plain_D_count'])for z in crows),'gate_report_hash':hashlib.sha256(SELF.with_name('check_returned_D_forced_core_ports_independent.json').read_bytes()).hexdigest(),'analytic_review':[
'The disjoint371-label catalogue and independently signed source reductions giveD58,C50,V112,U148 exclusions,368 total. The Q/B common-output theorem applies to all genuine containing C roles, so precisely15,30,75 remain, allF and atomic age3. No new geometric completeness assumption is added.',
'D-side40-to14 assembly is now independently PASS; its immutable pending-at-freeze wording is upgraded only by the separately bound status addendum. C75 has6 DC/VC x D^k(k0..2) parent rows from the signed horizon and F-side UC support cuts. Total20 counts TARGET/PARENT/RUN interfaces, while selectedD/DC source choices remain separately retained; it is not a count of attained histories.',
'The creatingD to ownC1 frame is translation(1,1) with unchanged heading and Cclock. Thus C75 oldC F(2,-5),returnedC(0,-1,W) becomes genuine sourceD F(3,-4),returnedC(1,0,W), exactly the reader-independent preforeign bud/currentness premises. The independently signed799c gate report directly replayed that actual C reader.',
'Original bud L51 and new coreR55 are distinct lifetimes. F R55 is EXITCORE, not a residual output; next actualC/V read3 deletes replacementcore. Marker beta belongs to next actualword tick1/read2. No ledger is allowed to carry the original identity through this reset.',
'The D30 immediate-priorC deleted-core guard specifically needs returnedV13L. ReturnedC13R requires the opposite beforecolor, so it does NOT remove C75 k0. The new assembly explicitly respects this non-lift.',
'Necessary parent/run restrictions are not recursively imposed on older epochs. Finite D/DC-entry positive controls and genuine W portal controls remain valid. No U-entry attainment, first-F exclusion, returned simplicity, second-foreign induction, archive contraction or global capture is proved.'
]}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
