from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__).resolve(); R=S.parents[1]; H=R/'returned_D_final_parent_exhaustion_2026-10-24'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(H/'manifest.json')=='bd138da4f01ee9b9935427a8b9d23aab518a6235eb54e749b368257dbe16f072'
for q in json.loads((H/'manifest.json').read_text())['files']:assert sha(H/q['file'])==q['sha256']
a=json.loads((H/'D_final_parent_exhaustion.json').read_text())
for p,h in a['dependencies'].items():assert sha(R/p)==h
j=json.loads((R/'returned_D_last_C_parent_reduction_2026-10-24/D_last_C_parent_reduction.json').read_text())['fourteen_remaining_genuine_DC_VC_interfaces']
expected={(15,p,w)for p in ['DC','VC'] for w in ['','D','DD','DDD','V']}|{(30,p,w)for p in ['DC','VC']for w in ['D','DD']}
assert {(z['catalogue_id'],z['last_positive_C_full_packet'],z['actual_pre_D_zero_C_word'])for z in j}==expected
actual={(z['catalogue_id'],z['last_positive_C_parent'],z['actual_pre_selectedD_N_word'])for z in a['all14_excluded_parent_run_rows']}
assert actual==expected and len(a['all14_excluded_parent_run_rows'])==14
assert {(z['catalogue_id'],z['last_positive_C_parent'],z['actual_pre_selectedD_N_word'],z['actual_selected_full_packet'])for z in a['all28_actual_selected_source_D_DC_roles']}=={(*x,s)for x in expected for s in ['D','DC']}
counts=Counter()
for z in a['all14_excluded_parent_run_rows']:
 i,p,w=z['catalogue_id'],z['last_positive_C_parent'],z['actual_pre_selectedD_N_word']
 dep='ed14673e' if i==30 else 'aa285e60' if w in ['','D'] else '372a183d' if w in ['DD','DDD'] else 'd005eb49'
 assert z['exclusion'].startswith(dep);counts[dep]+=1
 old=next(x for x in j if (x['catalogue_id'],x['last_positive_C_full_packet'],x['actual_pre_D_zero_C_word'])==(i,p,w))
 assert z['actual_parent_entry']==old['packet_entry'] and z['actual_final_C_entry']==old['last_actual_C_entry']
assert counts=={'ed14673e':4,'aa285e60':4,'372a183d':4,'d005eb49':2}
reports={'check_D_last_C_parent_join_independent':'dafea2c3968584c781f549168465056127d3070d846792e7a4c82e1bbf46ec49','check_F_first_C_cohort_lock_independent':'e42f0c0527ca96d96daf2529d44b8024ea7130e71e156c33f33f5fd7dbab585a','check_D15_remaining_cohort_and_bud_lifts_independent':'17dad0d38c39dc7e857156c6f5fc527be67afb03e60906d23a1d407ff1bde2be'}
for p,h in reports.items():assert sha(S.with_name(p+'.json'))==h
out=dict(status='PASS all fourteen D15/D30 necessary parent/run interfaces excluded',author_manifest=sha(H/'manifest.json'),independent_component_reports=reports,rows=sorted(expected),selected_full_sources=['D','DC'],counts=dict(counts),analytic_review=[
'The signed horizon/parent reduction supplies exactly these fourteen rows, not a hypothesis about all older epochs. Its source tail variants are retained separately in twenty-eight typed D/DC roles.',
'D30 uses the reader-independent BEFORE-F first-C cohort lemma. The one-V D15 interface uses its distinct qualified first-C T/Q hierarchy. Neither needs postforeign maturity.',
'D15 long-D runs are reanchored at an actual earlier plain D without changing one letter, identity, clock or the actual later-D outgoing contact owner. The stronger preforeign predicate, not a same-contact induction, licenses this use.',
'The empty/one-D older-bud obstruction uses only the real DC/VC source, exact full/atomic clock, actual old chords and the correct future WHITE mask. It does not require the chosen plain D to own C1. Marker ownership remains following actual word read8 where applicable.',
'This composition removes the two old-D coarse FIRST-returned-contact labels only. A separate whole-catalogue plus local returned/foreign geometry assembly is needed before signing one-returned-atom simplicity. No later packet iteration or global capture follows.' ])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
