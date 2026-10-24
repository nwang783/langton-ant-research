"""Old V source, total ordinary clock4: genuine complete foreign-MISS first.
No fixed-tail-index mask, no source A cleanup, no incoming beta assumption.
"""
from pathlib import Path
from fractions import Fraction as F
from math import floor,ceil
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
def ld(n,p):
 s=importlib.util.spec_from_file_location(n,R/p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=ld('l','word_stabilization/check_foreign_return_interfaces.py');o=ld('o','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h
def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(A,p):return z(p),z(after(W[A],p))
def rel(q,p):return l.rot(sub(q,p[:2]),-p[2])
def bad_current(ctx,tag,p):
 v=rel(tag,p);f=ctx['first'].get(v)
 return dict(SAME_CURRENT_original=tag,local=v,ENTRY_CORE=v in l.K,first=f,owner=o.describe(ctx['atom'],f[1])if f else None)if v in l.K or f and f[0]=='R'else None
angles=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows'];Vangles=[r for r in angles if r['source_class']=='preFOREIGN_ordinary'and r['source_atom']=='V'];assert len(Vangles)==4
K=4;target=(0,0,2);a,b=chord('V',(0,0,0));u=sub(b,a);boxes=[];geo=[]
for ar in Vangles:
 A=ar['contact_atom']
 if4=4 in ar['allowed_C_counts_before_contact_ENTRY']
 if not if4:continue
 c,e=chord(A,(0,0,2));v=sub(e,c);den=det(u,v);assert den
 cs=[tuple(F(a[k]+ss*u[k]-c[k]-tt*v[k],2)for k in(0,1))for ss in(0,1)for tt in(0,1)];bd=[(floor(min(q[k]for q in cs)),ceil(max(q[k]for q in cs)))for k in(0,1)];boxes.append(dict(actor=A,rational_corners=[[[q.numerator,q.denominator]for q in p]for p in cs],integer_bounds=bd))
 for x in range(bd[0][0],bd[0][1]+1):
  for y in range(bd[1][0],bd[1][1]+1):
   if(x+y+2)%2:continue
   q=sub(add(c,(2*x,2*y)),a);ss,tt=F(det(q,v),den),F(det(q,u),den)
   if not(0<=ss<1 and 0<tt<=1):continue
   p=(x,y,2);assert p==target
   geo.append(dict(actor=A,ENTRY=p,total_ordinary_C=4,old_source_outgoing_s=str(ss),new_positive_t=str(tt),SAME_original_r_in_ENTRY_CORE=rel((0,0),p)in l.K))
assert len(boxes)==2 and len(geo)==2 and{r['actor']for r in geo}=={'D','C'}
# Five preFOREIGN source tags at n2. Own full tails preserve all five SAME
# actual V-base births. Exact r5/B4/common3 and C/bud through3 are used
# ONLY in the uninterrupted ordinary prefix before firstFOREIGN.
FIELD={(0,0),(1,0),(2,0),(2,1),(2,2)};birth=[]
for full in['V','VC','VCC']:
 tr=l.trace(''.join(W[a]for a in full));base=l.trace(W['V']);og=l.literal_geometry(''.join(W[a]for a in full))
 for tag in FIELD:assert tr['last'][tag]==base['last'][tag]and base['last'][tag][0]=='R'and list(tag)in og['outputs']
 birth.append(dict(actual_full_source=full,source_full_ENTRY_C_clock=0,actual_full_EXIT_C_clock=full.count('C'),all5_SAME_base_births=[dict(tag=t,actual_R=base['last'][t])for t in sorted(FIELD)]))
# Exact zero-N/C/zero-W equation for the age1 possible foreign heads.
# The y RHS is <=1 for every surviving role, giving a finite arithmetic
# enumeration; uW is solved exactly from x, not capped by a search depth.
def NWmodels(p):
 out=[];Y=p[1]-4
 if Y<0:return out
 for uN in range(Y//4+1):
  for vN in range(Y//3+1):
   for dN in range(Y+1):
    rem=Y-dN-3*vN-4*uN
    if rem<0:continue
    for vW in range(rem+1):
     dW=rem-vW;num=1+dN+vN-dW-3*vW-p[0]
     if num<0 or num%4:continue
     out.append(dict(N_D=dN,N_V=vN,N_U=uN,W_D=dW,W_V=vW,W_U=num//4))
 return out
# All actual foreign true-input alignments to original r, at every true
# source ENTRY to foreign ENTRY age n<=TOTAL4. EntryCORE/firstWHITE is
# already incompatible with rCURRENT there; actual inputs may consume it.
fore=[];n1mods=[];n2keep=[]
for n in range(5):
 h=(-n)%4
 for A in'FQB':
  ctx=l.trace(W[A]+l.M);ctx['atom']=A
  for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
   p=(*sub((0,0),l.rot(slot,h)),h);ex=after(W[A],p);rec=dict(FOREIGN=A,ENTRY=p,true_source_ENTRY_to_FOREIGN_ENTRY_C_age=n,r_true_input=slot,actual_r_read_owner=o.describe(A,ctx['first'][slot][1]),actual_FOREIGN_RAW_EXIT=ex)
   if(sum(p[:2])+h)%2:why='sector'
   elif n==0:
    assert p[1]<=3 and(p[1]<3 or p[0]!=1);why='zeroN_after_sourceV_EXIT1_3_has_strict_positive_y_for_any_BASE;at_y3_head_must_be1_3'
   elif n==1:
    ms=NWmodels(p);rec['all_exact_N_C_W_endpoint_count_models']=ms
    if ms:
     assert len(ms)==1;m=ms[0]
     if p==(2,5,3):
      assert m==dict(N_D=1,N_V=0,N_U=0,W_D=0,W_V=0,W_U=0);tt=l.trace(W['D']+W['C']+W[A]+l.M);assert not tt['feasible'];rec['actual_containing_DC_then_FOREIGN_conflict']=tt;why='exact_counts_force_V_D_C_FOREIGN;actual_DC_to_FOREIGN_literal_conflict_NOT_raw_C_FOREIGN_ban'
     else:
      assert A=='Q'and p==(-3,4,3)and m==dict(N_D=0,N_V=0,N_U=0,W_D=0,W_V=0,W_U=1);tt=l.trace(W['C']+W['U']+W['Q']+l.M);assert not tt['feasible'];rec['actual_C_U_conflict']=tt;why='exact_counts_force_actual_C_U_before_Q_literal_conflict'
     n1mods.append(rec)
    else:why='no_nonnegative_N_C_W_endpoint_count_solution'
   elif n==2:
    bad=[b for tag in FIELD if(b:=bad_current(ctx,tag,p))]
    if bad:rec['genuine_preFOREIGN_current_source_field_contradictions']=bad;why='actual_original_r_B_common_C_bud_CORE_or_firstWHITE_before_FOREIGN'
    else:
     n2keep.append(rec)
     if p==(-5,1,2):why='NEW_FOREIGN_R39_tag_minus1_0_CURRENT_by_N_W_S_endpoint_guard_inside_targetCORE'
     elif p==(-3,3,2):why='NEW_FOREIGN_R36_tag1_1_CURRENT_by_N_W_S_endpoint_guard_inside_targetCORE'
     else:assert A in'QB'and p==(-4,0,2);why='actual_sourceV_L2_hole_minus1_minus1_physical_WHITE_at_foreign_own_L18'
   elif n==3:assert ex[2]==3 and ex[0]<=0;why='remaining_W_to_S_C_makes_x_lt0_then_zeroS_cannot_reach_targetx0'
   else:assert n==4 and ex[2]==2 and ex[1]<0;why='zeroS_foreign_EXIT_y_lt0_cannot_reach_targety0'
   rec['route']=why;fore.append(rec)
assert len(fore)==235 and len(n1mods)==4 and len(n2keep)==8
# The two independent NEW foreign output guards. No source-V siblings
# are kept after the foreign; these tags are genuinely NEW actual R's.
def Scounts(ex,tar):
 dx=ex[0]-tar[0];dy=ex[1]-tar[1];out=[]
 if min(dx,dy)<0:return out
 for nv in range(dx+1):
  nd=dx-nv;rem=dy-nd-3*nv
  if rem>=0 and rem%4==0:out.append(dict(D=nd,V=nv,U=rem//4))
 return out
new=[];Sroles=[]
for p0,slot,tick,tag in[((-5,1,2),(-4,1),39,(-1,0)),((-3,3,2),(-4,2),36,(1,1))]:
 for A in'FQB':
  p=p0;raw=l.trace(W[A]);ex=after(W[A],p);assert add(p[:2],l.rot(slot,2))==tag and raw['last'][slot]==('R',tick)and list(slot)in l.literal_geometry(W[A])['outputs']and ex[2]==0
  # For N inputs local y>=1; for W inputs min local x=-1. Actual N
  # heads start at ex_y, W starts at least ex_y+1. Both exceed tag input
  # head bounds. C has I0 and cannot silently capture CURRENT into CORE.
  assert ex[1]>tag[1]-1 and ex[1]+1>tag[1]+1
  new.append(dict(FOREIGN=A,ENTRY=p,genuine_NEW_R_tag=tag,source_foreign_slot=slot,actual_birth_R_tick0=tick,actual_N_RAW_EXIT=ex,N_input_head_y_at_most=tag[1]-1,W_input_head_y_at_most=tag[1]+1,actual_N_head_y_at_least=ex[1],actual_W_head_y_at_least=ex[1]+1,target_ENTRY_CORE_local=rel(tag,target)))
 assert rel(tag,target)in l.K
 for A in'DVU':
  ctx=l.trace(W[A]+l.M)
  for ins in map(tuple,l.literal_geometry(W[A])['inputs']):
   p=(*add(tag,ins),2);ex=after(W[A],p);ms=Scounts(ex,target);assert not ms
   Sroles.append(dict(SAME_NEW_foreign_tag=tag,first_S_loss_consumer=A,ENTRY=p,true_input=ins,owner=o.describe(A,ctx['first'][ins][1]),actual_RAW_EXIT=ex,all_zeroC_S_count_models_to_target=ms))
assert len(new)==6 and len(Sroles)==16
# Physical source-V hole, not an output/age argument. Source own tails
# preserve actual WHITE. Every finalR origin includes EXIT CORE writes.
g=(-1,-1);resets=[]
for full in['V','VC','VCC']:
 tr=l.trace(''.join(W[a]for a in full));assert tr['last'][g]==('L',2);resets.append(dict(source_full=full,physical_source_last_L_tick0=2,hole=g,WHITE_at_actual_base_and_full_RAW_EXIT=True))
HOLD={(0,0),(1,0),(2,0)};origins=[];ok=[]
for n in range(3):
 heading=(-n)%4
 for A in'DCVU':
  raw=l.trace(W[A]);ctx=l.trace(W[A]+l.M)
  for q,(c,tick)in raw['last'].items():
   if c!='R':continue
   p=(*sub(g,l.rot(q,heading)),heading);ex=after(W[A],p);rec=dict(writer=A,ENTRY=p,preFOREIGN_ENTRY_clock=n,physical_final_R_slot=q,R_tick0=tick,first=raw['first'][q],RAW_EXIT=ex,physical_R_inside_EXIT_CORE=rel(g,ex)in l.K)
   if(sum(p[:2])+heading)%2:why='sector'
   elif raw['first'][q][0]=='L':why='firstL_requires_earlier_BLACK_cut_after_executed_source_L2_reset'
   elif any((v:=rel(tag,p))in ctx['first']or v in l.K for tag in HOLD):why='earlier_writer_touches_independently_CURRENT_preFOREIGN_r_B_common'
   else:
    ok.append(rec)
    if n==0:assert p[1]<3;why='N0_heads_after_sourceV_y_ge3_all_physical_finalR_local_y_ge0'
    elif n==1:assert p[1]<4;why='W1_heads_y_ge4_all_physical_finalR_local_x_ge_minus1'
    elif A=='C':why='S2_C_writer_completes3_after_FOREIGN_ENTRY2'
    else:assert ex[1]<0;why='zeroS_cannot_rise_from_writer_EXIT_y_minus2_to_FOREIGN_y0'
   rec['route']=why;origins.append(rec)
assert len(origins)==108
holecuts=[]
for A in'QB':
 p=(-4,0,2);ctx=l.trace(W[A]+l.M);v=rel(g,p);assert ctx['first'][v]==('L',18);holecuts.append(dict(FOREIGN=A,ENTRY=p,physical_WHITE_hole=g,local=v,actual_FIRST_BLACK=ctx['first'][v],owner=o.describe(A,18)))
# Only now, complete actual FOREIGN MISS of SAME original r is proved.
# Independent source r min5 was used strictly beforeFORE; portable277
# first-loss clock is geometric and CONDITIONAL, not a transported age.
rports=[]
for A,p in[('D',(1,0,3)),('V',(3,0,3)),('U',(4,1,3))]:
 ex=after(W[A],p);assert ex==(0,1,3);rports.append(dict(earlier_original_r_loss_consumer=A,ENTRY=p,actual_RAW_EXIT=ex,TOTAL_ordinary_C=3,remaining_C_to_target=1,zeroW_then_C_W_to_S_x_le_minus1_then_zeroS_cannot_reach_targetx0=True))
reg=[]
for ts in[['V','C','V','C','D','U','Q','D','D','C','D','C','U','U','D'],['U','V','C','V','C','D','U','Q','D','D','C','D','C','U','U','D']]:
 tr=l.trace(''.join(W[a]for a in ts)+l.M);assert not tr['feasible'];reg.append(dict(structurally_endpoint_chosen_whole_word=ts,actual_literal_conflict=tr,reason='The proposed n2Q-hole return is not an attained history; immutable sourceV L2 debt appears at Q ownL18. No depth exploration or U-entry positive is claimed.'))
D=[R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'V_r_postforeign_contact_clock_2026-10-24/manifest.json',R/'audits/check_V_r_postforeign_clock_independent.json',R/'fresh_RAW_V_U_early_donor_guards_2026-10-24/manifest.json',R/'audits/check_fresh_RAW_donors_independent.json',R/'V_postforeign_pair_rail_reserve_2026-10-24/manifest.json',R/'V_postforeign_pair_rail_reserve_2026-10-24/simultaneous_input_qualification_manifest.json',R/'audits/check_V_pair_rail_independent.json',R/'audits/check_V_pair_simultaneous_qualification_independent.json',R/'old_V_third_age2_genuine_field_2026-10-24/manifest.json',R/'audits/check_old_V_third_age2_independent.json',R/'full_packet_CURRENT_internal_RAW_lift_2026-10-24/manifest.json',R/'old_U_all_tail_S_D_coupled_reserve_2026-10-24/C_CORE_wording_manifest.json',R/'audits/check_old_U_S4_D_coupled_independent.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'audits/check_complete8_foreign_adjacency_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py'];assert all(p.exists()for p in D),[str(p)for p in D if not p.exists()]
out=dict(status='AUTHOR_FROZEN_PENDING_REVIEW',scope='Actual preFOREIGN genuine outgoing V-base source of V/VC/VCC in U-entry G8, FIRSTF/Q/B then arbitrary ordinary-only RAW tail plus actualfinalM11. GLOBAL first contact at TOTALordinaryC4 impossible. Only two oldV actorsD/C0,0S; other TOTALclocks/sourceclasses remain separate.',all4_signed_old_V_angle_rows=Vangles,all2_exact_rational_K4_boxes=boxes,all2_outgoing_owned_K4_target_geometries=geo,all3_full_source_SAME_five_output_births=birth,source_preFOREIGN_field_scope='At true age2 only: r5, B4, common3, C/bud through3 signed552; all preserve actual SAME V-base births under own tails. No A-status/helper cleanup or incoming beta is used. FULL currentness is lifted to internal actual C-tail RAW cuts only by explicit8d68 physical identity lemma.',all235_actual_FOREIGN_r_TRUE_input_roles=fore,all4_one_C_N_W_endpoint_count_models_and_real_grammar_cuts=n1mods,all8_n2_source_field_compatible_FOREIGN_r_retirement_rows=n2keep,all6_genuinely_NEW_FOREIGN_output_CURRENT_target_CORE_interfaces=new,all16_NEW_tag_S_loss_exact_endpoint_guards=Sroles,all3_actual_full_source_physical_hole_resets=resets,all108_CORE_inclusive_preFOREIGN_physical_first_BLACK_hole_origins=origins,all_source_hole_origin_survivor_cuts=ok,all2_Q_B_actual_hole_L18_interfaces=holecuts,all3_portable_r_CLOCK3_firstloss_ports_and_final_W_S_guard=rports,all2_structurally_chosen_failed_whole_prefix_return_regressions=reg,complete_FOREIGN_r_MISS_statement='SAME r isCURRENT at each true funding cut n<=4 by its source preFOREIGN min5. EntryCORE/firstWHITE already fail. Every actualTRUEinput row has now been excluded on a target-compatible history, with all5 true n and actualFOREIGNM11. Hence COMPLETEFOREIGN contextMISSr is proved before invoking277. No fixed-third45 mask is reused.',ordinary_C_CORE_scope='C I0 excludes true external inputs; its three external EXITCORE sites are actual first-WHITE, while two are already ENTRYCORE sites unavailable to a CURRENT external tag. No silent capture; no false all5firstWHITE statement.',after_FOREIGN_argument='Portable277 givesTOTALK3 for a strictly earlier first r CURRENTloss and RAWEXIT0,1W, including markerCORE capture. Any zeroW then remaining W-to-S C givesx<=-1; zeroS cannot reach targetx0. Thus SAMEr0,0 isCURRENT at targetENTRY but lies in actual targetCORE. No through-target protection is claimed.',no_postFOREIGN_old_age_law_or_altered_source_cohort_assumption=True,no_fixed_tail_index_or_rail_length_cap=True,no_FULL_packet_completion_bound_used_for_unexecuted_consumer_tails=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'V_K4.json').write_text(json.dumps(out,indent=2)+'\n');print('OldV TOTAL4 author:2 actors;FOREr235 all cut, n2 field leaves8,NEWtags6+hole2; rCLOCK3 finalx guard. Otherclocks separate.')
