from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'seven_word_spatial_return_2026-10-23';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
man=D/'first_foreign_first_returned_atom_simplicity_manifest.json';assert sha(man)=='9aa9751b11a62f91ef4b9dfe819ffc0f1e255bd2f666df385dbbd97ae9d7ef93';m=json.loads(man.read_text())
for p,h in m['files'].items():assert sha(D/p)==h
for p,h in m['dependencies'].items():assert sha(R/p)==h
# Re-run the independent exact rational catalogue and every local pair calculation,
# stopping before its report write. No frozen author code is executed.
p=S.with_name('check_first_returned_atom_contact_independent.py');ns={'__file__':str(p)};exec(p.read_text().split("man=D/'first_returned_atom_contact_manifest.json'")[0],ns)
assert len(ns['angles'])==56 and len(ns['local'])==12 and len(ns['full'])==24
cat=json.loads((D/'first_returned_atom_contact.json').read_text());a=json.loads((D/'first_foreign_first_returned_atom_simplicity.json').read_text());three=json.loads((D/'first_returned_three_F_frontier.json').read_text());labels=cat['old_source_contact_cases']
assert len(labels)==371 and Counter(q['source_atom']for q in labels)=={'D':60,'C':51,'V':112,'U':148}
assert len(a['all371_necessary_labels_excluded'])==371
cnt=Counter()
for i,(q,z)in enumerate(zip(labels,a['all371_necessary_labels_excluded'])):
 assert z['catalogue_id']==i and all(z[k]==q[k]for k in ['source_atom','foreign','returned_atom']);cnt[z['exclusion']]+=1
assert sorted(cnt.values())==[1,2,2,48,58,112,148]
assert [q['catalogue_case']for q in three['three_necessary_labels_with_actual_containing_roles']]==[15,30,75]
assert all(labels[i]['foreign']=='F'for i in [15,30,75])
# Check ALL six C75 boundary rows against the exact already signed local predicates.
cohort=json.loads((R/'F_same_target_C_cohort_lock_2026-10-24/F_C_cohort_lock.json').read_text())['two_exact_older_C_cohort_interfaces'];cp=three['signed_C75_last_positive_C_parent_interfaces'];assert len(cp)==6
for z in cp:
 k=z['intervening_plain_D_count'];p=z['last_positive_C_fullpacket'];assert z['actual_last_C_index']==1 and z['previous_full_source_entry_to_foreign_C_age']==4 and p in ['DC','VC']
 ep=z['actual_predecessor_packet_entry_in_selected_D_frame'];assert ep==([-2-k,1-k,1]if p=='DC'else[-4-k,1-k,1])
 if k:
  e=next(v for v in cohort if v['k']==k);pp=next(v for v in e['actual_prior_DC_VC_choices']if v['full_packet']==p)
  assert pp['entry']==ep and pp['full_source_entry_C_clock']==-1 and pp['C1_exit_C_clock']==0 and e['foreign']==[3,-4,1] and e['returned_reader_NOT_USED']
 else:assert ep in [[-2,1,1],[-4,1,1]]
# The creatingD frame is genuine translation, not a contact-owner substitution.
walk,W=ns['walk'],ns['W'];tr=walk(W['D']);assert(tr['p'],tr['h'])==(1+1j,0);assert tr['p']+(2-5j)==3-4j
# Bind the independent D composition made after the author assembly froze.
rp=S.with_name('check_D_final_parent_exhaustion_independent.json');assert sha(rp)=='a76cd8803a26230b062fb91381aaaed85ed05ec740c86be491eb3db865908669';dr=json.loads(rp.read_text());assert len(dr['rows'])==14
prior=three['signed_excluded_source_counts'];assert sum(prior.values())==368
out={'status':'PASS actual proxy simplicity through one first complete foreign and exactly one immediate ordinary RAW atom','author_manifest_sha256':sha(man),'source_counts':dict(Counter(q['source_atom']for q in labels)),'exact_exclusion_counts':dict(cnt),'angle_cases':56,'all371_labels_excluded':True,'local_foreign_returned_pairs':ns['local'],'prepared_full_successor_controls':24,'D_final_independent_report':sha(rp),'C75_boundary_rows':6,'analytic_review':[
'The prior signed U-entry complete-eight simple path and first-foreign theorem provide actual injectivity up to the foreign exit. The twelve fresh rational local pairs meet only at the actual terminal adjacency, including the two-piece Q/B foreign. Q-to-U collinear continuation has a singleton endpoint intersection, not overlap or reversal.',
'The returned straight chord is itself injective and its starting point is new relative to the old-eight path. Any old contact therefore has a positive earliest parameter, since the old proxy is finite and compact. A nonparallel contact at an old vertex belongs to its unique outgoing old atom; the sole old terminal vertex lies on the foreign, whose full pair clearance has already excluded it. The original old starting vertex is retained as an outgoing-source endpoint, not discarded.',
'For a parallel first contact, same-direction onset is the old outgoing start, included by source s=0 and new t>0. Opposite-direction approach to that start would already overlap its outgoing segment just before contact, contradicting earliest onset. At an old segment end, the next outgoing atom owns the vertex; only the actual old terminal has no such owner, and it is already foreign-cleared. Thus no endpoint or collinear case is lost.',
'The intervening prefix subarc and the new partial chord form a Jordan loop precisely because all earlier contacts are absent. The signed one-foreign tangent formula, actual preceding-C bit0 and strict closing-angle bounds give56 ranked angle cases with C age0..4. Exact parallelogram boxes, sector parity and already-actual foreign clearance reconstruct all371 possible first-contact interfaces. This is a necessary-interface argument, never an assumption of physical attainment.',
'The signed previous reductions remove368 labels. The two remaining D labels have the independently verified fourteen-row/twenty-eight actualD/DC exhaustion. C75 retains actualDC/C1 source and six priorDC/VC interfaces; the two zero-D ones use the signed genuine older-bud/past-chord theorem, and four k1/2 rows match the exact reader-independent BEFORE-F cohort predicates at fullsource age4 and atomic selectedclock3. No returnedV13BLACK requirement is illicitly transferred to C13WHITE.',
'All sources therefore exclude the earliest hypothetical contact. The actual auxiliary proxy extends as a simple OPEN arc through this one returned RAW atom. This is not fine-walk selfavoidance, a full returned packet with later C tails, a second ordinary atom or foreign, arbitrary seven-word coverage, or global capture.',
'Original tags and all maturity claims stop before foreign entry unless an exact combined before-mask is used. F51L/55R and returned3L are distinct lifetime/core operations. Actual next-word marker read2/read8 ownership remains unchanged. PreparedD-entry loops, actual older-bud clearing histories with earlier forbidden crossings, rawCF positives and the withdrawn full-output seal remain consistent countercontrols.'
]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
