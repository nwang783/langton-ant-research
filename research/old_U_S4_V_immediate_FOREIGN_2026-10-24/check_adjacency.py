"""Narrow actual U-F/Q/B adjacency repair for the S4 V guard.
The rejected universal143d pair claim is not used. Only45abc's explicit
strict-lower N4 scope and its independently retained first-loss table apply.
"""
from pathlib import Path
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
def ld(n,p):
 s=importlib.util.spec_from_file_location(n,R/p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=ld('l','word_stabilization/check_foreign_return_interfaces.py');o=ld('o','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def after(w,p):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h
sourceU=(0,0,0);FORE=(0,4,0);target=(0,4,2);futures=[]
for A,hook in [('Q',[(-3,-3),(-2,-3),(-1,-3),(-1,-2)]),('B',[(-2,-4),(-1,-4),(0,-4),(0,-3)])]:
 ex=after(W[A],FORE);cuts=[]
 for cell in hook:
  tag=add(ex[:2],l.rot(cell,ex[2]));loc=l.rot(sub(tag,target[:2]),-target[2]);first=l.trace(W['V']+l.M)['first'].get(loc)
  if loc in l.K or first and first[0]=='R':cuts.append(dict(SAME_CURRENT_hook=tag,post_FOREIGN_EXIT_N_chart=cell,target_local=loc,actual_FIRST_WHITE=first,actual_owner=o.describe('V',first[1])if first else None))
 assert len(cuts)==2 and {tuple(x['SAME_CURRENT_hook'])for x in cuts}=={(-1,3),(-2,3)}
 futures.append(dict(actual_adjacent_words='U'+A,actual_FOREIGN_ENTRY=FORE,actual_FOREIGN_RAW_EXIT=ex,true_preFOREIGN_C_clock=0,total_C_to_actor=4,target=target,guarded_same_hook_FIRST_WHITE=cuts,hook_stopping_scope='Signed715 keeps the same four hook identities CURRENT at every RAW entry before the first ordinary contact with the actual foreign proxy. GLOBAL-first contact with oldU entails that premise through targetENTRY, no through-target claim.'))
ex=after(W['F'],FORE);rel=l.rot(sub(target[:2],ex[:2]),-ex[2]);ft=(*rel,(target[2]-ex[2])%4);assert ft==(-4,-2,0)
pair=[(-3,-1),(-2,-1)];pcuts=[]
for q in pair:
 loc=sub(q,ft[:2]);first=l.trace(W['V']+l.M)['first'][loc];assert first[0]=='R';pcuts.append(dict(SAME_F_tag_post_EXIT_N=q,target_local=loc,actual_first_WHITE=first,actual_owner=o.describe('V',first[1])))
orig=json.loads((R/'original_F_piece_firstpost_DC_2026-10-24/F_piece_DC.json').read_text());qual=json.loads((R/'original_F_piece_firstpost_DC_2026-10-24/partial_scope_qualification.json').read_text());assert 'heady<=-2'in qual['corrected_pair_scope']
rows=orig['all128_coupled_F46_F47_source_current_first_loss_rows'];assert len(rows)==128
from collections import Counter
print('routes',Counter(x['route']for x in rows))
# The independently retained table supplies all roles, not new exclusions.
# Exact remaining-loss exits are reconstructed from all D/V/U input slots.
ports=[]
for A in'DVU':
 for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
  for tag in pair:
   p=(*sub(tag,slot),0)
   if(sum(p[:2]))%2:continue
   ep=after(W[A],p)
   if ep==(-1,-1,0):
    ports.append(dict(actor=A,ENTRY=p,which_original_F_tag=tag,input=slot,actual_owner=o.describe(A,l.trace(W[A]+l.M)['first'][slot][1]),RAW_EXIT=ep,target_y=-2,strictly_lower_target_not_reachable_by_zeroC_N=True))
assert len(ports)==3
# Both source guardians are target-normal: their proof uses no actual F
# proper-contact requirement except the displayed support inequalities.
guards=[]
for b1 in'DCVU':
 if b1=='D':why='Actual firstD common2,0: portable BASE-projection minimum3 and exact N4 input exits x>=2 keep SAME common CURRENT at targetx=-4. The128 pair roles then leave only N4 ports exitingy=-1 above targety=-2.'
 elif b1=='C':why='Actual firstC O3: signed fresh-C target-normal reserve keeps all3 CURRENT at N4 targety=-2<=1. The128 pair roles then leave only N4 ports exitingy=-1 above targety=-2.'
 elif b1=='V':why='Signed15e source-owner-independent portable F46/F47 reserve at GLOBAL-firstcontact ENTRY, using genuine nonterminal firstV pair25a at every earlier completed cut. Actual next ordinary RAW and its marker exist.'
 else:why='Signeda08 exact64-role F-pair first-loss table with independently CURRENT freshU LEFT; strong ordinary RAW U-star lift supplies the same LEFT despite earlierF. All surviving table rows are earlier actualF contacts, forbidden strictly before GLOBALtarget.'
 guards.append(dict(actual_first_post_F_RAW=b1,post_F_EXIT_N_target=ft,total_post_F_C_clock=4,actual_independent_source_reserve_and_F_pair_scope=why))
D=[R/'foreign_Q_B_hook_contact_reserve_2026-10-24/manifest.json',R/'audits/check_foreign_hook_reserve_independent.json',R/'original_F_piece_firstpost_DC_2026-10-24/partial_scope_qualification_manifest.json',R/'audits/check_F_DC_partial_qualification_independent.json',R/'original_F_piece_firstpost_DC_2026-10-24/F_piece_DC.json',R/'first_postforeign_V_first_contact_2026-10-24/portable_F_reserve_scope_lift_manifest.json',R/'audits/check_portable_F_scope_independent.json',R/'firstpostU_F_piece_first_contact_2026-10-24/manifest.json',R/'audits/check_F_piece_firstpostU_independent.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/U_star_RAW_lift_manifest.json',R/'audits/check_fresh_U_star_RAW_lift_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py'];assert all(p.exists()for p in D),[str(p)for p in D if not p.exists()]
out=dict(status='AUTHOR_FROZEN_PENDING_REVIEW',exact_scope='Only the omitted immediate creating-plainU then FIRSTF/Q/B adjacency in oldU actorV0,4S GLOBAL-first-contact at total ordinaryC4, arbitrary ordinary suffix plus actualM11. No oldU S4 D exclusion or arbitrarytail simplicity.',all2_actual_U_Q_B_adjacency_hook_guards=futures,actual_U_F_RAW_EXIT=ex,old_U_chart_actor=target,actual_post_F_EXIT_N_chart_actor=ft,all2_same_F46_F47_target_FIRST_WHITE_reads=pcuts,mandatory_partial45abc_corrected_scope=qual['corrected_pair_scope'],all128_independently_retained_first_D_C_F_pair_roles=rows,all3_N4_pair_loss_actors_per_actual_first_D_or_C=ports,all4_actual_first_post_F_RAW_source_routes=guards,rejected143d_universal_pair_claim_remains_rejected=True,no_reuse_at_y_minus1_active_CORE_target=True,conclusion='ImmediateUF/UQ/UB is impossible for this target. After excluding it,0aad196b creator/nextordinaryBASE funnel is exhaustive. This supplement does not modify the original frozen file or claim the original was complete.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'adjacency.json').write_text(json.dumps(out,indent=2)+'\n');print('Immediate U-FORE S4V adjacency:Q/B hooks;F target-4,-2N with4 genuine first-letter reserves; no rejected y=-1 pair lift.')
