from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'Q_B_hook_two_C_foreign_transfer_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json'
assert sha(MF)=='63c1fb626ac174b4863369e7120dd66af7e267133ffe01fa5aef59d41629d40c';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'QB_two_C_hook_transfer.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in ('W','M','K','tr','rot','xy')]
H=lambda q:int(q.imag-q.real);NE={-1-1j,-1+0j,-1+1j,0j,1j,1+0j,1+1j,1+2j,2+0j,2+1j};HOOK={-1-1j,-2-1j,-3-1j,-3-2j};field=NE|HOOK;assert len(field)==13

def first(a):
 ans={}
 for t,(q,h,c)in enumerate(tr(W[a]+M)['reads']):ans.setdefault(q,(c,t))
 return ans
sources=[]
for a,post in [('Q',{-3-3j,-2-3j,-1-3j,-1-2j}),('B',{-2-4j,-1-4j,-4j,-3j})]:
 z=tr(W[a]);assert z['h']==2;ek={z['p']+rot(z['h'])*q for q in K};O={q for q,(c,t)in z['last'].items()if c=='R' and q not in ek};assert {z['p']-q for q in post}==HOOK and field<=O and z['last'][-1-1j]==('R',46)
 row=next(r for r in J['all2_actual_source_hook_frames']if r['source_foreign']==a);assert row['actual_EXIT']==[*xy(z['p']),2]
 assert [dict(cell=xy(q),own_R_tick0=z['last'][q][1])for q in sorted(HOOK,key=lambda q:(q.real,q.imag))]==row['all4_actual_hook_R_births'];sources.append(dict(source=a,exit=xy(z['p']),births=row['all4_actual_hook_R_births']))
# Every first-L external slot of RAW plus actual M, including unread exit-core capture.
goals=defaultdict(list)
for a in 'FQB':
 for g in sorted(HOOK,key=lambda q:(q.real,q.imag)):
  for slot,(c,t)in first(a).items():
   if c!='L' or slot in K:continue
   p=g-slot
   if int(p.real+p.imag)%2:continue
   goals[a,p].append((g,slot,t))
assert len(goals)==60
rows=[];kept=[];counts=Counter()
for (a,p),wits in sorted(goals.items(),key=lambda x:(x[0][0],x[0][1].real,x[0][1].imag)):
 ar=next(r for r in J['all60_next_foreign_hook_input_geometries_unspent_NE_branch']if r['next_foreign']==a and r['entry']==[*xy(p),0]);aws={(complex(*w['hook_cell']),complex(*w['input_slot']),w['physical_first_L']['context_tick0'])for w in ar['hook_input_witnesses']};assert set(wits)==aws
 bad=[]
 for g in sorted(field,key=lambda q:(q.real,q.imag)):
  loc=g-p;f=first(a).get(loc)
  if loc in K or(f and f[0]=='R'):bad.append(dict(SAME_CURRENT=xy(g),local=xy(loc),role='ENTRY_CORE'if loc in K else'initial_WHITE',actual_first=list(f)if f else None))
 typ='all_NE_unspent_FIELD_CORE_WHITE'if bad else'three_deleted_CORE_hole_route';assert ar['classification']==typ
 if bad:assert bad==ar['conflicts']
 else:kept.append((a,p))
 assert p.real<3 or p.imag<3 or H(p)<0
 br=next(r for r in J['all60_spent_NE_branch_N_cone_routes']if r['next_foreign']==a and r['entry']==[*xy(p),0]);assert br['violations']==dict(X_below3=p.real<3,Y_below3=p.imag<3,H_below0=H(p)<0)
 rows.append(dict(next_foreign=a,entry=[*xy(p),0],true_inputs=len(wits),classification=typ));counts[typ]+=1
assert len(kept)==12 and {p for a,p in kept}=={-2-4j,-4j,1-5j,2-4j}
# Reconstruct EVERY physical R, not only final residual outputs.
coreholes=[-1+0j,-1-1j,-1j];allR=[];negative=[];normal=[]
for a in 'DCVU':
 z=tr(W[a]);assert [z['last'][q]for q in coreholes]==[('L',1),('L',2),('L',3)]
 rr=[]
 for t,(q,h,c)in enumerate(z['reads']):
  if c!='R':continue
  assert q.real>=-1 and q.imag>=0 and q!=-1+0j;rr.append(dict(own_tick0=t,local_cell=xy(q)))
  if q.real==-1:
   assert a=='U';negative.append(dict(atom=a,own_tick0=t,local_cell=xy(q)))
  if a!='C':
   assert H(z['p'])>=H(q);normal.append(dict(producer=a,R_own_tick0=t,R_local_cell=xy(q),N_RAW_EXIT_H_minus_written_cell_H=H(z['p'])-H(q)))
 allR.append(dict(atom=a,all_physical_R_events=rr))
assert allR==J['all4_plain_physical_R_supports'] and negative==J['all_negative_x_R_events_only_U'] and normal==J['all_physical_DVU_R_to_N_RAW_EXIT_normal_bounds']
cu=tr(W['C']+W['U']);assert cu['bad'][:2]==(29,1) and cu['bad'][-1]=='L'
assert (tr(W['C'],0j,2)['p'],tr(W['C'],0j,2)['h'])==(-1j,1)
for a in 'DVU':
 assert tr(W[a],0j,2)['p'].imag<0 and tr(W[a],0j,1)['p'].imag<=0 and H(tr(W[a])['p'])>=0
# All24 last-R funding obstructions, source-specific actual deleted holes.
selected={'Q':{-2-4j:0,-4j:1,1-5j:2,2-4j:1},'B':{-2-4j:2,-4j:0,1-5j:1,2-4j:0}};routes=[]
for source in 'QB':
 ep=tr(W[source])['p'];holes=[ep-q for q in coreholes]
 for a,p in kept:
  i=selected[source][p];g=holes[i];loc=g-p;f=first(a)[loc];assert f[0]=='L'and f[1]<len(W[a])and H(g)>H(p)
  row=next(r for r in J['all24_source_target_deleted_hole_routes']if r['source_foreign']==source and r['next_foreign']==a and r['target_entry']==[*xy(p),0]);assert row['first_ordinary_deleted_core_index0']==i and row['physical_hole']==xy(g) and row['hole_H']==H(g) and row['target_H']==H(p) and row['actual_target_first_BLACK']['context_tick0']==f[1] and row['actual_target_first_BLACK']['next_word_tick0']is None
  routes.append(dict(source=source,target=a,head=xy(p),hole=xy(g),hole_H=H(g),target_H=H(p),own_FIRST_L=f[1]))
assert len(routes)==24
O=dict(status='PASS SAME Q/B hook across one next FOREIGN after exactly two ordinary Cs only',manifest=sha(MF),script=sha(S),actual_source_frames=sources,true_hook_loss_poses=rows,unspent_counts=dict(counts),spent_cone_exclusions=60,physical_R_event_count=sum(len(r['all_physical_R_events'])for r in allR),hole_routes=routes,analytic_review=[
'Both source frames and all four actual last-R hook births reconstruct. The hook and NE sets share SAME R46 at(-1,-1), giving13 distinct current cells. Signed four-C ordinary hook maturity is used only through the two-C ordinary connector. Signed158 supplies either allNE unspent or actual first pair-loss U(3,-1,N) completed at3,3, followed only by N bases with X,Y>=3 and H=y-x>=0.',
'All complete-context external first-L slots are regenerated, including marker-only exitCORE absorption. At nextFOREIGN entry any oldCURRENT tag inside ENTRYCORE or demanding firstWHITE already contradicts actual partition/color. Grouping all hook true-input roles gives exactly60 poses, all outside the spent-pair cone. In the unspent branch48 CORE/WHITE cuts leave twelve genuinely simultaneous-input poses. No static population argument discards them.',
'The first actual ordinary RAW exists because exactlytwo Cs occur and physically L1/L2/L3-deletes the three common CORE holes. Every RAW has those as its last reads at those cells. Complete physical R supports, including CORE writes and intermediate nonfinal writes, show S heads cannot restore the two upper holes or sidehole. For the sidehole in E, the required top row and negative-local-x R force an initial E U immediately after the first C, which is literally impossible by CU29/1. Any earlier S base or E D/V lowers that row; a second C has no negative-x R. Thus all three remain WHITE until N2 for arbitrary rail lengths.',
'For every physical R of a completed N D/V/U producer, H_EXIT>=H_written. Remaining N increments have nonnegative H, and no C remains. A selected hole with H larger than the nextFOREIGN head cannot therefore have any repairing last R before target entry. This includes CORE-to-external funding and all earlier prepared colors because the actual firstordinary L deleted them. Each of24 source/target choices then has an ownRAW FIRST L contradiction, so the target cannot self-repair before reading it.',
'Exhausting every true-input first loss also prevents unread absorption into nextFOREIGN EXITCORE. Hence the same four old identities remain BLACK and CURRENT at that RAWexit and avoid deletion in its real suppliedM. This does not execute any subsequent foreign, assert zero/one-C generic transfer, global simplicity, full-state finite abstraction, decreasing resource, or capture. Earlier history and sourceU assumptions are genuinely absent.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
