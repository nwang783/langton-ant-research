"""All-tail S4 D guard by a three-tag coupled first-CURRENT-loss reserve.
This is not a continuation scan. Every origin includes physical CORE R slots.
No maturity law is transported through the first foreign.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
def ld(n,p):
 s=importlib.util.spec_from_file_location(n,R/p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=ld('literal','word_stabilization/check_foreign_return_interfaces.py');o=ld('owner','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h
def rel(q,p):return l.rot(sub(q,p[:2]),-p[2])
def hit(ctx,q,p):return rel(q,p)in ctx['first']or rel(q,p)in l.K
def bad_black(ctx,q,p):
 v=rel(q,p);f=ctx['first'].get(v)
 return dict(tag=q,local=v,ENTRY_CORE=v in l.K,first=f)if v in l.K or f and f[0]=='R'else None
STAR={(0,0),(0,1),(1,0),(1,1)};LEFT={(0,0),(0,1)};d=(1,1);arm=(1,2);bud=(1,3);RES={d,arm,bud};target=(0,2,2)
# Source-tail births are SAME actual U-base R events.
births=[]
for word in ['U','UC','UCC']:
 raw=l.trace(''.join(W[a]for a in word));base=l.trace(W['U']);g=l.literal_geometry(''.join(W[a]for a in word))
 for tag in RES:
  assert raw['last'][tag]==base['last'][tag]and base['last'][tag][0]=='R'and list(tag)in g['outputs']
 births.append(dict(actual_full_creator=word,SAME_U_base_births=[dict(tag=t,actual_last_R=base['last'][t])for t in sorted(RES)]))
# Before FOREIGN, actual fresh U STAR is current at every ordinary RAW cut.
# Bud is independently current through full entry age4. All32 arm-loss
# roles are sector or CURRENT-star contact or literal budCORE/WHITE.
prearm=[]
for A in'DVU':
 ctx=l.trace(W[A]+l.M)
 for h in range(4):
  for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
   p=(*sub(arm,l.rot(slot,h)),h);r=dict(consumer=A,ENTRY=p,true_arm_input=slot,owner=o.describe(A,ctx['first'][slot][1]))
   if(sum(p[:2])+h)%2:why='sector'
   elif any(hit(ctx,t,p)for t in STAR):why='independently_CURRENT_SAME_U_STAR_touched_before_FIRST_FOREIGN'
   else:
    b=bad_black(ctx,bud,p);assert b;r['actual_CURRENT_bud_CORE_or_first_WHITE']=b;why='actual_pre_FOREIGN_source_bud_CURRENT_through4'
   r['route']=why;prearm.append(r)
assert len(prearm)==32 and Counter(x['route']for x in prearm)=={'sector':16,'independently_CURRENT_SAME_U_STAR_touched_before_FIRST_FOREIGN':12,'actual_pre_FOREIGN_source_bud_CURRENT_through4':4}
# Exact terminal support: from W exit(1,4) or(-1,4), one C plus any
# zero-W/S rails cannot reach target0,2S. x equation forces all W counts
# and S D/V counts zero for exitx1; y gap2 is not a multiple4. exitx-1
# is already too far left. No ordering/count cap is used.
def WCS_guard(ep):
 assert ep[2]==3 and ep[1]==4 and ep[0]in[-1,1]
 return dict(actual_W_RAW_EXIT=ep,remaining_C_count=1,target=target,x_equation='0=exitX-dW-3vW-4uW-1-dS-vS',exit_minus1_has_no_nonnegative_x_solution=ep[0]==-1,exit_plus1_forces_all_W_counts_and_S_D_V_zero=ep[0]==1,remaining_y_equation_if_exit_plus1='2=4-4uS',no_nonnegative_integer_solution=True)
# Complete arm MISS through true preFOREIGN age4, with exactly one
# target-specific immediate-return route at age4.
fa=[];ak=[]
for n in range(5):
 h=(-n)%4
 for A in'FQB':
  ctx=l.trace(W[A]+l.M)
  for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
   p=(*sub(arm,l.rot(slot,h)),h);r=dict(FOREIGN=A,true_old_U_ENTRY_to_FOREIGN_ENTRY_C_clock=n,ENTRY=p,true_arm_input=slot,owner=o.describe(A,ctx['first'][slot][1]))
   if(sum(p[:2])+h)%2:why='sector'
   elif any(hit(ctx,t,p)for t in STAR):why='forbidden_COMPLETE_original_U_STAR_context_hit_at_age_le4'
   else:
    ak.append(r)
    if n==0:
     if A in'FQ':assert p in[(4,4,0),(4,6,0)]and p[1]-p[0]<4;why='zeroN_after_U_has_y_minus_x_ge4'
     else:
      assert p==(3,7,0);pair=l.trace(W['D']+W['B']+l.M);assert not pair['feasible'];r['actual_DB_literal_conflict']=pair;why='zeroN_equations_force_DDD_then_forbidden_actual_D_to_FOREIGN_pair'
    elif n==1:assert p==(2,7,3);why='first_W_H_ge5_plus_required_nonempty_W_BASE_H_increment_ge2'
    elif n==2 or n==3 or n==4 and A in'QB':
     b=bad_black(ctx,bud,p);assert b and b['first'][0]=='R';r['genuine_pre_FOREIGN_bud_FIRST_WHITE']=b;why='original_bud_CURRENT_before_FOREIGN_through4'
    else:
     assert n==4 and A=='F'and p==(4,4,0);ep=after(W[A],p);assert ep==target
     r['actual_FOREIGN_RAW_EXIT_equals_target_ENTRY']=ep;why='no_C_left_zeroS_requires_immediate_first_returned_D_already_signed_simple'
   r['route']=why;fa.append(r)
assert len(fa)==235 and len(ak)==16
# Actual spent upper and CORE hole cuts. Creating U h=(0,3) is R27
# ALIVECORE, not WHITE at its RAW exit. Its actual next ordinary RAW has
# own L3, while G=(-1,4) is erased own L1. Neither is rewritten there.
G=(-1,4);h0=(0,3);resets=[]
assert l.trace(W['U'])['last'][h0]==('R',27)
for A in'DCVU':
 raw=l.trace(W[A]);assert raw['last'][(-1,0)]==('L',1)and raw['last'][(0,-1)]==('L',3)
 resets.append(dict(actual_first_next_ordinary_RAW=A,ENTRY=(0,4,0),spent_upper_G=G,actual_G_death_global_tick0=29,actual_G_own_tick0=1,actual_G_read1=2,source_U_R27_CORE_h=h0,actual_h_death_global_tick0=31,actual_h_own_tick0=3,actual_h_read1=4,actual_exit=after(W[A],(0,4,0)),both_holes_physically_WHITE_at_this_executed_RAW_exit=True))
for word in ['UC','UCC']:
 tr=l.trace(''.join(W[a]for a in word));assert tr['last'][G]==('L',29)and tr['last'][h0]==('L',31)
HOLD=STAR|{arm,bud};holes=[];hk=[]
for tag in[G,h0]:
 for n in range(3):
  heading=(-n)%4
  for A in'DCVU':
   raw=l.trace(W[A]);ctx=l.trace(W[A]+l.M)
   for slot,(c,tick)in raw['last'].items():
    if c!='R':continue
    p=(*sub(tag,l.rot(slot,heading)),heading);ep=after(W[A],p);r=dict(hole=tag,writer=A,ENTRY=p,actual_ENTRY_clock=n,physical_final_R_slot=slot,own_R_tick0=tick,first=raw['first'][slot],RAW_EXIT=ep,physical_R_is_EXIT_CORE=rel(tag,ep)in l.K)
    if(sum(p[:2])+heading)%2:why='sector'
    elif raw['first'][slot][0]=='L':why='first_L_needs_an_earlier_BLACK_cut_after_actual_reset'
    elif any(hit(ctx,t,p)for t in HOLD):why='writer_touches_independently_CURRENT_pre_FOREIGN_STAR_arm_or_bud'
    else:
     hk.append(r)
     if n==0:assert p[1]<5;why='after_executed_reset_any_remaining_N0_head_y_ge5_or_already_C1_leaves_no_N0'
     elif n==1:assert p[1]-p[0]<5;why='first_and_later_W1_heads_have_H_y_minus_x_ge5'
     elif A=='C':why='S2_C_writer_completes3_after_FOREIGN_ENTRY2'
     else:assert tag==G and ep[1]<=4<6;why='zeroS_from_writer_exit_y_le4_cannot_reach_FOREIGNminus2_6S'
    r['route']=why;holes.append(r)
assert len(holes)==216 and len(hk)==16
# Align every actual FOREIGN bud input, retaining complete STAR+armMISS.
fb=[];bk=[];newtag=[]
ne=json.loads((R/'foreign_three_C_NE_reserve_2026-10-24/three_C_NE_reserve.json').read_text());assert[1,2]in ne['transfer_dichotomy']['nine_retained_originals']
for n in range(5):
 heading=(-n)%4
 for A in'FQB':
  ctx=l.trace(W[A]+l.M)
  for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
   p=(*sub(bud,l.rot(slot,heading)),heading);ep=after(W[A],p);r=dict(FOREIGN=A,ENTRY=p,true_preFOREIGN_C_clock=n,true_bud_input=slot,owner=o.describe(A,ctx['first'][slot][1]),actual_RAW_EXIT=ep)
   if(sum(p[:2])+heading)%2:why='sector'
   elif any(hit(ctx,t,p)for t in STAR|{arm}):why='forbidden_COMPLETE_original_STAR_or_newly_proved_arm_FOREIGN_context_hit'
   else:
    bk.append(r)
    if n==1:assert p in[(3,8,3),(4,7,3)]and p[1]-p[0]<=5;why='W1_FOREIGN_H_le5_below_first_W_H5_plus_required_nonempty_BASE_increment2'
    elif n==2:
     assert p in[(-2,6,2),(-1,5,2),(1,5,2)]
     if p==(-2,6,2):tag=G;why='genuinely_spent_upper_G_is_WHITE_at_foreign_actual_L13'
     elif p==(-1,5,2):tag=h0;why='actual_next_RAW_L3_deleted_h_is_WHITE_at_foreign_actual_L13'
     else:
      tag=add(p[:2],l.rot((1,2),2));assert tag==h0 and l.trace(W[A])['last'][(1,2)]==('R',25)and [1,2]in l.literal_geometry(W[A])['outputs']and rel(tag,target)in l.K
      r['NEW_foreign_R25_CURRENT_target_CORE']=dict(new_tag=tag,source_foreign_ENTRY_slot=(1,2),R_tick0=25,remaining_ordinary_C=2,target_CORE_local=rel(tag,target),same_cell_is_in_signed_NE3_nine_retained_originals=True);newtag.append(r);why='NEW_FOREIGN_R25_guard_CURRENT_through_remaining2Cs_inside_actual_target_CORE'
     if p!=(1,5,2):
      loc=rel(tag,p);assert ctx['first'][loc]==('L',13);r['physical_WHITE_hole_true_BLACK_read']=dict(hole=tag,local=loc,first=ctx['first'][loc],owner=o.describe(A,13))
    else:
     assert n==3 and ep in[(1,4,3),(-1,4,3)];r['all_length_W_C_S_endpoint_guard']=WCS_guard(ep);why='one_remaining_C_and_exact_zero_W_S_semigroup_cannot_reach_target'
   r['route']=why;fb.append(r)
assert len(fb)==235 and len(bk)==19 and len(newtag)==3
# First ordinary loss of the THREE-tag reserve. Other reserved TRUE
# inputs are retained simultaneously: only CORE/firstWHITE is a color
# conflict. LEFT touches are independent since its SAME IDs remain
# CURRENT at both earlier cuts by the global-first stopping theorem.
joint=[];jk=[]
for A in'DVU':
 ctx=l.trace(W[A]+l.M)
 for tag in sorted(RES):
  for heading in range(4):
   for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
    p=(*sub(tag,l.rot(slot,heading)),heading);ep=after(W[A],p);r=dict(first_lost_reserve_tag=tag,consumer=A,ENTRY=p,input=slot,owner=o.describe(A,ctx['first'][slot][1]),actual_RAW_EXIT=ep)
    if(sum(p[:2])+heading)%2:why='sector'
    elif any(hit(ctx,t,p)for t in LEFT):why='touches_independently_CURRENT_SAME_LEFT_before_and_after_earlier_loss_RAW'
    else:
     bad=[b for t in RES-{tag}if(b:=bad_black(ctx,t,p))]
     if bad:r['other_reserved_CURRENT_CORE_or_first_WHITE']=bad;why='independent_other_reserve_entry_CORE_or_first_WHITE'
     else:
      jk.append(r);assert tag==bud and heading==3 and ep in[(1,4,3),(-1,4,3)]
      r['all_other_RESERVED_true_inputs_retained_not_rejected_as_color']=[t for t in sorted(RES-{tag})if rel(t,p)in list(map(tuple,l.literal_geometry(W[A])['inputs']))]
      r['TOTAL_ordinary_clock_after_one_FOREIGN']=3;r['all_length_W_C_S_endpoint_guard']=WCS_guard(ep);why='only_W3_bud_loss_exit_cannot_reach_total4_target'
    r['route']=why;joint.append(r)
assert len(joint)==96 and len(jk)==4
assert all(rel(t,target)in l.K for t in[arm,bud]);target_guard=dict(SAME_arm=arm,target_arm_CORE_local=rel(arm,target),SAME_bud=bud,target_bud_CORE_local=rel(bud,target),both_CURRENT_at_target_ENTRY_by_coupled_firstloss=True)
D=[R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/U_star_RAW_lift_manifest.json',R/'audits/check_fresh_U_star_RAW_lift_independent.json',R/'U_LEFT_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_LEFT_contact_or_persistence_independent.json',R/'foreign_U_star_age2_2026-10-23/manifest.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',R/'audits/check_foreign_U_raw_ages34_independent.json',R/'foreign_U_marker_clocks_2026-10-23/manifest.json',R/'audits/check_foreign_U_age2_and_marker_independent.json',R/'word_stabilization/U_foreign_prefix_bud_cuts_frozen_20261023_2201/manifest.json',R/'audits/check_U_foreign_prefix_buds_independent.json',R/'foreign_three_C_NE_reserve_2026-10-24/manifest.json',R/'audits/check_foreign_three_C_NE_reserve_independent.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'audits/check_complete8_foreign_adjacency_independent.json',R/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',R/'audits/check_first_foreign_returned_simplicity_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py'];assert all(p.exists()for p in D),[str(p)for p in D if not p.exists()]
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual old U/UC/UCC in U-entry G8 before its FIRSTF/Q/B, arbitrary ordinary-only RAW tail plus actualfinalM11. GLOBAL first proxy contact with outgoing oldU cannot be D0,2S at TOTAL ordinaryC4. No secondFOREIGN or full-tail simplicity claim.',all3_actual_source_tail_SAME_three_tag_births=births,all32_pre_FOREIGN_arm_CURRENT_loss_roles=prearm,pre_FOREIGN_arm_CURRENT_through4='Only beforeFORE: sourceSTAR CURRENT by freshRAWstar lift; sourcebud CURRENT by oldG8 min5. All32 actual arm roles close; C I0 and physical CORE completeness exclude silent capture. This extends the beforeFORE age3 arm guard to4 without carrying it throughFORE.',all235_FOREIGN_arm_TRUE_input_roles=fa,all16_arm_foreign_necessary_rows_and_exact_cuts=ak,all4_actual_first_next_ordinary_hole_reset_cuts=resets,actual_source_h_R27_is_aliveCORE_not_WHITE_at_U_RAW_EXIT=True,all216_CORE_inclusive_physical_G_h_first_BLACK_origins=holes,all16_hole_origin_endpoint_or_clock_cuts=hk,all235_FOREIGN_bud_TRUE_input_roles=fb,all19_foreign_bud_necessary_rows_and_exact_cuts=bk,all3_genuinely_NEW_FOREIGN_R25_target_CORE_guards=newtag,all96_coupled_d_arm_bud_first_CURRENT_loss_roles=joint,all4_only_remaining_W3_bud_loss_ports_and_no_count_cap=jk,actual_target_entry_guard=target_guard,complete_FOREIGN_MISS_scope='d is originalSTAR completeMISS through4. Arm isCURRENT beforeFORE and every trueFOREinput is cut, including the n4 immediate F-return via separately signed one-return simplicity. Bud isCURRENT beforeFORE and every trueFOREinput is cut by cones, actual physical reset holes, NEW foreignR25 or exact future endpoint. Thus all3 same RES are completeFOREIGN contextMISS on a target-compatible history. No source identity is declared CURRENT after a consumingFORE.',CORE_and_simultaneous_input_convention='Earliest CURRENTloss is at actual RAWcut, not physicalL time. Other reserved TRUEinputs remain possible simultaneously; they are never discarded as an intrinsic color failure. Only independent LEFT hits, other ENTRYCORE/firstWHITE, sector and actual endpoint constraints close96. Ordinary C has I0; its five exitCORE writes each require WHITE at entry, so no silent CURRENT absorption.',no_old_age_or_original_bud_permanence_after_FOREIGN=True,no_coupled_cycle_Jordan_or_90_dependency_needed=True,no_prefix_word_enumeration_or_fixed_atom_index=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'S_D.json').write_text(json.dumps(out,indent=2)+'\n');print('OldU S4D author check: prearm32;FOREarm235->16;physical holes216->16;FOREbud235->19;coupled96->4 W3 endpoint failures. SAMEarm+bud in targetCORE.')
