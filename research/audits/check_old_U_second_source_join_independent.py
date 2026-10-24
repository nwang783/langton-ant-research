from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'second_ordinary_after_first_foreign_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'old_U_second_source_progress_manifest.json';assert sha(mf)=='1559601818ab2c60004ff4a8c09c1ca8aa3d0110979db8cd177a4b781ba71083';m=json.loads(mf.read_text())
for k,h in m['files'].items():assert sha(P/k)==h
for k,h in m['dependencies'].items():assert sha(R/k)==h
src=json.loads((P/'old_U_second_contact_LEFT_frontier.json').read_text())['exact60_necessary_only_remaining_states'];g=json.loads((R/'U_second_contact_creator_bud_guards_2026-10-24/creator_bud_guards.json').read_text());z=json.loads((P/'old_U_second_source_progress.json').read_text())
def key(r):return(r['foreign'],tuple(r['foreign_pose']),r['first'],r['second'],tuple(r['second_pose']),r.get('true_preforeign_age',r.get('true_preforeign_clock')))
a={key(x):x for x in src};b={key(x):x for x in g['all60_typed_cases']};assert len(a)==len(b)==len(src)==60 and a.keys()==b.keys();cnt=Counter(x['classification']for x in b.values());remain=[x for k,x in a.items()if b[k]['classification']=='necessary_only_not_excluded_here'];assert cnt=={'genuine_s_BLACK_vs_combined_before_WHITE':36,'source_deleted_g_no_rebirth_through_clock3':12,'necessary_only_not_excluded_here':12}
assert {key(x)for x in remain}=={key(x)for x in g['remaining12_necessary_states']}=={key(x)for x in z['remaining12_necessary_only_states']}
assert all(x['second']=='V'and tuple(x['second_pose'])==(0,4,2)for x in remain);assert Counter((x['foreign'],x['first'],x['true_preforeign_age'])for x in remain)==Counter((f,a,3 if a=='C'else 4)for f in'FQB'for a in'DCVU')
out={'status':'PASS exact60-key integration of previously signed guards, not a new exclusion','manifest':sha(mf),'disjoint_counts':dict(cnt),'remaining12_keys':sorted(map(key,remain)),'scope':'Only chronological FIRST SECOND-ordinary new contact with an old outgoing U source. Twelve necessary V(0,4,S) cases are not actual U-entry attainments. The newer q-frontier is separate and not imported into this join.'};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
