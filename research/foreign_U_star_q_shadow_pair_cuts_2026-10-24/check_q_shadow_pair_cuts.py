"""Bounded intersection of existing69 gates with all-age genuine reserves."""
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent;BP=R/'U_star_one_foreign_return_transfer_2026-10-24/check_U_star_corner_transfer.py';n={'__file__':str(BP)};exec(BP.read_text().split('# Exactly twelve constant local suffixes.')[0],n)
W=n['W'];mp=n['mp'];M=n['M'];K=n['K'];L=n['L'];rot=n['rot'];sub=n['sub'];literal=n['literal']
GP=R/'foreign_U_port_interfaces_2026-10-23/foreign_U_ports.json';G=json.loads(GP.read_text())['interfaces']['star']['gates'];assert len(G)==69
ports={'original_q':(-1,2),'cleanup_A':(-1,4),'cleanup_r':(-1,5)}
def own(A,t):
 le=len(W[mp[A]]['word']);return dict(owner='own FOREIGN RAW',symbol=A,tick0=t,read_number1=t+1)if t<le else dict(owner='next actual word M11 prefix; not an extra marker word',tick0=t-le,read_number1=t-le+1)
rows=[];typed=[];counts=Counter();forced=Counter();universal=[]
for old in G:
 A=old['foreign'];x,y,h=old['pose'];d=literal(W[mp[A]]['word']+M);pdata={}
 for name,cell in ports.items():
  s=rot(sub(cell,(x,y)),-h);req=d['requirements'].get(s);rr=d['reads'].get(s,[]);core=s in K;good=not core and req is not False
  pdata[name]=dict(global_cell=cell,FOREIGN_local=s,before_BLACK=req,in_actual_FOREIGN_entryK=core,positive_CURRENT_compatible=good,all_physical_reads=[dict(combined_tick0=t,turn=ch,owner=own(A,t))for t,ch in rr],block_reason='CURRENT_cannot_be_ENTRYCORE'if core else'CURRENT_BLACK_vs_before_WHITE'if req is False else None)
 qgood=pdata['original_q']['positive_CURRENT_compatible'];shgood=pdata['cleanup_A']['positive_CURRENT_compatible']and pdata['cleanup_r']['positive_CURRENT_compatible']
 if qgood and shgood:branch='both_genuine_ancestry_branches_necessary_only'
 elif qgood:branch='must_retain_SAME_original_q_before_FOREIGN'
 elif shgood:branch='must_have_had_age2_qcleanup_and_hold_SAME_r_A_shadows'
 else:branch='impossible_for_ALL_source_tail_types';universal.append(old)
 forced[branch]+=1;rows.append(dict(foreign=A,pose=old['pose'],old_star_target_tags=old['target_tags'],ports=pdata,plain_U_necessary_ancestry=branch))
 for src,ok in(('U',qgood or shgood),('UC',qgood),('UCC',shgood)):
  why='necessary_only_not_cut_by_this_reserve'if ok else'all_age_genuine_reserve_conflict'
  counts[src,why]+=1;typed.append(dict(source_full=src,foreign=A,pose=old['pose'],classification=why,ports=pdata))
assert counts==Counter({('U','necessary_only_not_cut_by_this_reserve'):66,('U','all_age_genuine_reserve_conflict'):3,('UC','necessary_only_not_cut_by_this_reserve'):59,('UC','all_age_genuine_reserve_conflict'):10,('UCC','necessary_only_not_cut_by_this_reserve'):56,('UCC','all_age_genuine_reserve_conflict'):13})
assert len(universal)==3 and{(x['foreign'],tuple(x['pose']))for x in universal}=={(A,(-5,3,2))for A in'FQB'}
shared=[]
for A in'FQB':
 d=literal(W[mp[A]]['word']+M);assert d['requirements'][(-4,1)]is False and d['reads'][(-4,1)]==[[39,'R']];assert d['requirements'][(-4,-2)]is False and d['reads'][(-4,-2)][0]==[52,'R']
 assert len(W[mp[A]]['word'])>52
 shared.append(dict(foreign=A,pose=[-5,3,2],q_cell=[-1,2],q_FOREIGN_local=[-4,1],q_first_R_own_RAW_tick0=39,q_first_R_read_number1=40,shadow_r_cell=[-1,5],shadow_r_FOREIGN_local=[-4,-2],shadow_r_first_R_own_RAW_tick0=52,shadow_r_first_R_read_number1=53,both_reads_in_COMMON_F56_RAW_prefix=True,no_future_M11_needed_for_this_corollary=True))
# Forced UCC shadow is not inferred merely from a conditional retirement:
# no direct foreign can follow UCC; any old successor is V/VC.
nexttable=[]
for b in('D','DC','V','VC','VCC','U','UC','UCC','F','Q','B'):
 d=literal(''.join(W[mp[a]]['word']for a in'UCC'+b)+M);nexttable.append(dict(next_word=b,feasible=d['feasible'],conflict=d if not d['feasible']else None))
assert [z['next_word']for z in nexttable if z['feasible']]==['V','VC']
D=[BP,GP,R/'foreign_U_port_interfaces_2026-10-23/manifest.json',R/'U_q_shadow_reserve_budget_2026-10-24/manifest.json',R/'core_periodicity_new/U_q_source_history_frozen_20261023_2027/manifest.json',R/'U_second_V_original_q_frontier_2026-10-24/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Existing69 firstFOREIGN genuine old-U star gates only. All-age reserve beforeFOREIGN rejects26 of207 source-tail typed states:3U/10UC/13UCC. F/Q/B(-5,3,S) impossible for every U-family creator by own commonF56 R39/R52. No age rule or reserve permanence through foreign.',all69_local_gate_reserve_interfaces=rows,all207_source_tail_typed_cases=typed,counts=[dict(source=k[0],classification=k[1],count=v)for k,v in sorted(counts.items())],plain_U_branch_counts=dict(forced),three_all_tail_ALL_AGE_RAW_obstructions=shared,UCC_genuine_shadow_forcing_all8_plus3_foreign_successors=nexttable,source_type_justification=dict(U='Either originalq CURRENT or BOTH genuine qcleanup r/A CURRENT, signed all-age reserve.',UC='Signed2027 originalq is permanentlyCURRENT beforefirstforeign.',UCC='DirectF/Q/B afterUCC is impossible; exactnextoldfullpacketonlyV/VC, forcingqcleanup andpermanentgenuine r/A shadows.'),not_claimed=['Remaining181 typed states are necessary only, not attained.', 'Some26 exclusions may overlap earlier age/geometry laws; no novelty count against all prior results is asserted.', 'A beforeTRUE positive port may be consumed byFOREIGN; no permanence is inferred after it.', 'CORE conflicts refer to SOURCE tag CURRENT atFOREIGN entry, not a claim that a physicallyBLACK CORE tag is already deleted.'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'q_shadow_pair_cuts.json').write_text(json.dumps(o,indent=2)+'\n');print('Existing69 gates: all-age reserve rejects3U/10UC/13UCC; F/Q/B(-5,3,S) impossible incommonF56 R39/R52 forALLtailtypes.')
