"""Nine exact second-V states: genuine first-helper cohort closure."""
from pathlib import Path
from collections import Counter
import hashlib,json,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent;BP=R/'U_star_one_foreign_return_transfer_2026-10-24/check_U_star_corner_transfer.py';n={'__file__':str(BP)};exec(BP.read_text().split('# Exactly twelve constant local suffixes.')[0],n)
W=n['W'];mp=n['mp'];M=n['M'];K=n['K'];L=n['L'];LEFT=n['PORTS']['LEFT'];literal=n['literal'];at=n['at'];rot=n['rot'];sub=n['sub'];center=n['center'];add=n['add'];q=(-1,2)
P=R/'U_second_V_original_q_frontier_2026-10-24/original_q_frontier.json';J=json.loads(P.read_text());rows=[x for x in J['remaining11_necessary_states']if x['true_preforeign_clock']==4];assert len(rows)==9
CP=R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py';sp=importlib.util.spec_from_file_location('owner',CP);co=importlib.util.module_from_spec(sp);sp.loader.exec_module(co)
QMIN=R/'audits/dcuv_count5_replay/queries.json';mins=json.loads(QMIN.read_text());mrows=[]
for key in('0:(0, 1)','1:(0, 1)'):
 s=mins['slots'][key];assert s['certified_minimum_C_age']==3 and s['unexcluded_counts_0_to_4'][:3]==[0,0,0]
 assert all('OPEN'not in x['reasons_0_through_4'][:3]for x in s['rows']);mrows.append(dict(slot=key,certified_minimum=3,all_0_to_2_excluded=True,admitted_rows=len(s['rows'])))
CUT2=center((0,4),2);assert CUT2==(1,9)
creator=[]
for typ in('UC','UCC'):
 aa=n['walk'](typ);C1=aa[1];assert C1['atom']=='C'and C1['end']==CUT2
 creator.append(dict(creating_full_type=typ,own_first_C_tail_actual_end=C1['end'],own_C1_exit_head=literal(''.join(W[mp[z]]['word']for z in'UC'))['endpoint'],later_FIRST_return_endpoint=CUT2,reason='prior nonadjacent corrected vertex before SECOND atom; forbidden by signed one-return simplicity'))
helper=[];hstar={add(z,(0,4))for z in L};hleft={add(z,(0,4))for z in LEFT};K2={at(z,(0,4),2)for z in K};assert hleft<=K2 and hstar<=K2
for typ in('D','DC','V','VC','VCC','U','UC','UCC'):
 if typ[0]=='D':
  aa=n['walk']('U'+typ);aa=aa[1];assert aa['atom']=='D'and aa['end']==CUT2
  why='prior_following_D_base_end_EQUALS_FIRST_return_end'
 elif typ[0]=='U':why='new_genuine_U_LEFT_pair_CURRENT_by_age4_FOREIGN_MISS_transfer_but_inside_CUT2_core'
 else:why='remaining_actual_first_V_family'
 helper.append(dict(first_following_full=typ,entry=[0,4,0],source_C_clock=0,classification=why))
assert sum(x['classification']=='remaining_actual_first_V_family'for x in helper)==3
# All three candidate first-V packets have genuine r/A, and truly delete g.
firstV=[];g=(-1,4);r=(0,4);A=(0,5)
for typ in('V','VC','VCC'):
 d=literal(''.join(W[mp[z]]['word']for z in typ));assert d['reads'][(0,0)][-1]==[4,'R'];assert d['reads'][(0,1)][-1]==[11,'R'];assert d['reads'][(-1,0)]==[[1,'L']]
 firstV.append(dict(first_full=typ,entry=[0,4,0],actual_base_entry_clock=0,genuine_r_cell=r,r_birth_own_V_tick0=4,genuine_A_cell=A,A_birth_own_V_tick0=11,deleted_g_cell=g,g_last_L_own_V_tick0=1,g_last_L_global_tick0=29,own_tail_preserves_A_and_does_not_rebirth_g=True))
# If A retires preforeign, signed2043 gives V/VC(0,8,S)at sourceclock2.
cleanup=[]
for typ in('V','VC'):
 d=literal(''.join(W[mp[z]]['word']for z in typ));entry=(0,8);h=2;end=at(tuple(d['endpoint'][:2]),entry,h);eh=(h+d['endpoint'][2])%4;cl=2+typ.count('C')
 assert(end,eh,cl)==(((-1,5),2,2)if typ=='V'else((-1,4),1,3))
 cleanup.append(dict(full_A_consumer=typ,entry=[0,8,2],entry_C_clock=2,exit=[*end,eh],exit_C_clock=cl,none_of_nine_FOREIGN_entries_has_this_pose_or_clock=True))
# Plain V cleanup: every next actual full packet is either D/DC with a
# genuine replacement too young, or V/U base consuming held originalq.
vnext=[]
for b in('D','DC','V','VC','VCC','U','UC','UCC'):
 d=literal(''.join(W[mp[z]]['word']for z in b)+M);pp=(-1,5);h=2
 if b[0]=='D':
  slot=rot(sub(g,pp),-h);assert slot==(0,1)and d['requirements'][slot]is True and slot not in K
  why='deleted_g_requires_produced_D_input_age3_but_all_after_L29_births_have_age_at_most2';guard=dict(cell=g,input_slot=slot,first_input_L=co.describe(b,d['reads'][slot][0][0]),consumer_entry_clock=2,earliest_possible_new_full_producer_entry_clock=0,maximum_produced_age=2,certified_minimum=3)
 else:
  slot=rot(sub(q,pp),-h);assert slot==(0,3)and d['requirements'][slot]is True
  why='consumes_FORCED_HELD_same_original_q_before_FOREIGN';guard=dict(cell=q,input_slot=slot,first_q_L=co.describe(b,d['reads'][slot][0][0]))
 vnext.append(dict(next_full=b,entry=[*pp,h],classification=why,guard=guard))
# VC cleanup: ALL next full words have the common D-prefix R8 on oldq.
vcnext=[]
for b in('D','DC','V','VC','VCC','U','UC','UCC'):
 d=literal(''.join(W[mp[z]]['word']for z in b)+M);pp=(-1,4);h=1;slot=rot(sub(q,pp),-h);assert slot==(2,0)and d['requirements'][slot]is False and d['reads'][slot][0]==[8,'R']
 vcnext.append(dict(next_full=b,entry=[*pp,h],held_original_q_cell=q,q_local=slot,first_q_read=co.describe(b,8),classification='common_R8_requires_WHITE_but_originalq_stays_BLACK'))
# The exact nine-mask terminal premise is deliberately NOT generalized.
res=[]
for old in rows:
 a,b1,b2=old['foreign'],old['first'],old['second'];p=tuple(old['foreign_pose'][:2]);h=old['foreign_pose'][2];d=literal(''.join(W[mp[z]]['word']for z in(a,b1,b2))+M);slot=rot(sub(r,p),-h)
 assert d['requirements'][slot]is False and d['reads'][slot][0][1]=='R'
 res.append(dict(foreign=a,first=b1,second=b2,foreign_pose=old['foreign_pose'],second_pose=old['second_pose'],true_preforeign_clock=4,first_helper_genuine_r=r,combined_r_before_BLACK=False,all_combined_r_reads=d['reads'][slot],classification='excluded_genuine_first_V_r_locked_BLACK_versus_before_WHITE'))
D=[BP,CP,P,R/'U_second_V_original_q_frontier_2026-10-24/manifest.json',QMIN,R/'U_star_one_foreign_return_transfer_2026-10-24/manifest.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',R/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',R/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',R/'core_periodicity_new/V_C_same_heading_exclusion_frozen_20261023_2043/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Nine exact true-clock4 SECONDV0,4S states excluded, assuming signed prior reductions and originalq guard. Genuine creator plainU and first-nextV funnel, forced A-cleanup continuation obstruction, then preforeign r-lock versus nine exact combined masks. No arbitrary-tail fixed-mask transplantation.',creating_UC_UCC_old_vertex_exclusion=creator,first_following_eight_full_funnel=helper,new_following_U_cohort_guard=dict(new_U_base_entry=[0,4,0],genuine_new_U_star=sorted(hstar),new_LEFT=sorted(hleft),true_FOREIGN_age=4,FOREIGN_must_MISS_by_signed_first_effect_min5=True,same_LEFT_current_at_CUT2_by_signed_transfer=True,actual_second_V_entryK=sorted(K2),contradiction='BOTH newLEFT originals inside CUT2core, impossible CURRENT'),genuine_first_V_fine_history=firstV,only_A_first_consumers=cleanup,plain_V_A_cleanup_all8_continuations=vnext,VC_A_cleanup_all8_continuations=vcnext,produced_D_minima=mrows,A_persistence_argument='If originalA retires, exact V/VC cleanup atclock2 has no permissible next old full word before these FOREIGNNclock4 targets. Thus A stays ORIGINAL CURRENT before FOREGIN. Signed V-r lock then keeps originalr current BLACK. Both age and r-lock authority are used ONLY before FOREIGN.',all9_exact_terminal_before_masks=res,scaling_limit='For longer returned tails the final contact need not require first-Vr WHITE at FOREIGN entry. A foreign may rewrite r/A/B, and later ordinary words can change the parity between FOREIGN funding cut and final read. The nine exact combined masks are essential and are not claimed portable.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'first_helper_cohort_closure.json').write_text(json.dumps(o,indent=2)+'\n');print('Nine exact SECONDV states excluded: creator plainU, first helperV family; originalA cleanup has no full continuation with heldq, so preFOREIGN rBLACK conflicts all9 masks.')
