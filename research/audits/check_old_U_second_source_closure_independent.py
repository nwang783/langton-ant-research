from pathlib import Path
from collections import Counter
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'second_ordinary_after_first_foreign_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();read=lambda p:json.loads(p.read_text());man=D/'old_U_second_source_closure_manifest.json';assert sha(man)=='0473649e19c63aaec1f5003bc3644786f7047eb76cfee2c5ad0713ef9ef660a1'
m=read(man)
for p,h in m['files'].items():assert sha(D/p)==h
for p,h in m['dependencies'].items():assert sha(R/p)==h
ref=read(D/'old_U_second_source_closure.json');base=read(S.with_name('check_old_U_second_LEFT_frontier_independent.json'))['remaining'];bud=read(S.with_name('check_U_second_creator_bud_guards_independent.json'));qr=read(S.with_name('check_U_second_V_original_q_independent.json'));tr=read(S.with_name('check_U_second_V_clock3_reflex_independent.json'));hr=read(S.with_name('check_second_V_first_helper_closure_independent.json'))
def key(r):return(r['foreign'],tuple(r['foreign_pose']),r['first'],r.get('second','V'),tuple(r.get('second_pose',[0,4,2])),r.get('true_preforeign_age',r.get('true_age')))
B={key(r):r for r in base};assert len(base)==len(B)==60
assigned={}
for row in bud['all60_rows']:
 if row['classification']=='necessary_only_not_excluded_here':continue
 ks=[k for k in B if k[:5]==(row['foreign'],tuple(row['foreign_pose']),row['first'],row['second'],tuple(row['second_pose']))];assert len(ks)==1;assigned[ks[0]]=row['classification']
assert len(assigned)==48
for row in qr['all12_rows']:
 if row['east_core_cut']:
  k=key(row);assert k in B and k not in assigned;assigned[k]='original_east_pair_FOREIGN_entry_core'
for row in tr['cases']:
 A=row['foreign'];pose={'Q':(5,0,1),'B':(6,1,1)}[A];k=(A,pose,'C','V',(0,4,2),3);assert k in B and k not in assigned;assigned[k]='clock3_reflex_Jordan_support'
for row in hr['nine_fresh_combined_before_masks']:
 k=(row['foreign'],tuple(row['actual_foreign_pose']),row['first'],'V',(0,4,2),4);assert k in B and k not in assigned and row['combined_r_initial_required_BLACK']is False;assigned[k]='genuine_first_helper_cohort_clock4'
assert set(assigned)==set(B);cnt=Counter(assigned.values());assert cnt==ref['exact_disjoint_remaining_frontier_cuts']
for row in ref['all60_canonical_state_keys_with_disjoint_closure']:
 a,p,b,c,q,n=row['key'];assert assigned[(a,tuple(p),b,c,tuple(q),n)]==row['exclusion']
# Bind actual independent C-branch and one-return simplicity reports as distinct premises.
cr=S.with_name('check_old_U_second_C_left_guard_independent.json');assert sha(cr)=='8722904ed45b9c6a35e808c97dd35479b899157052d44daadb1d13f43df42432'
out=dict(status='PASS old-U outgoing-source branch of chronological first SECOND-RAW contact excluded',manifest=sha(man),independent_cuts=dict(cnt),all60=[dict(key=k,cut=assigned[k])for k in B],analytic_review=[
'The signed ONE-return simple OPEN proxy is the base, not second simplicity. A chronological first contact by the second ordinary chord has exact outgoing ownership at old vertices, strict interior ownership, or the included same-direction collinear onset; the earlier small geometry lemma removes contact with the foreign, first returned atom and immediate preforeign source. Every remaining old-U source is covered by the signed C-target branch or D/V/U frontier.',
'The signed C branch is independent of the sixty-state projection. For D/V/U, the exact pose/clock frontier was independently rederived including two collinear onsets, two already-contacted starts, true n versus effective N, actual full-source tail clocks, LEFT currentness and RIGHT physical BLACK even when in CORE. No current-core identity is silently treated as residual.',
'This checker uses prior INDEPENDENT reports to reconstruct all60 keys and their disjoint36+12+1+2+9 exclusion, then compares every author key. It does not merely rerun author counting. Foreign pose, both letters, second pose and true clock are all retained.',
'All age/first-retirement predicates occur before the first foreign; combined contexts retain actual later toggles. The final nine helper theorem uses genuine source clocks and exact whole-word completion, not postforeign maturation.',
'Only outgoing OLD U source is excluded. Old D/C/V branches, second simplicity, arbitrary ordinary tails, second foreign, language coverage and global capture remain open.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],cnt)
