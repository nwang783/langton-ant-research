"""Old U source, arbitrary-tail S-facing V first-contact guard.
Physical final-R origins include CORE writes. No post-foreign age is assigned
to an old identity. New foreign tags are labeled separately.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def contact(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=F(det(q,v),den),F(det(q,u),den)
  return dict(old_s=str(s),new_t=str(t))if 0<=s<=1 and 0<=t<=1 else None
 if det(q,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((F(c[k]-a[k],u[k]),F(d[k]-a[k],u[k])))
 return dict(collinear_old_interval=[str(max(F(0),lo)),str(min(F(1),hi))])if max(0,lo)<=min(1,hi)else None

def rel(q,p):return l.rot(sub(q,p[:2]),-p[2])
def conflict(a,p,black=(),white=()):
 tr=l.trace(W[a]+l.M);bad=[]
 for q in sorted(black):
  x=rel(q,p);f=tr['first'].get(x)
  if x in l.K or f and f[0]=='R':bad.append(dict(SAME_CURRENT_BLACK=q,local=x,role='ENTRY_CORE'if x in l.K else'first_WHITE',actual_first=f,owner=o.describe(a,f[1])if f else None))
 for q in sorted(white):
  x=rel(q,p);f=tr['first'].get(x)
  if x in l.K or f and f[0]=='L':bad.append(dict(physical_WHITE=q,local=x,role='ENTRY_CORE_requires_BLACK'if x in l.K else'first_BLACK',actual_first=f,owner=o.describe(a,f[1])if f else None))
 return bad
STAR={(0,0),(0,1),(1,0),(1,1)};t=(1,2);s=(1,3);r=(0,4);q=(-1,2);G=(-1,4);target=(0,4,2)
# Creator/nextRAW funnel is pure geometry plus a NEW creator's sameLEFT,
# independent of the number of returned atoms or fixed foreign masks.
zT=z(target);assert zT==(1,9);C1=chord('C',(0,4,0));assert C1[1]==zT;Dnext=chord('D',(0,4,0));assert Dnext[1]==zT
newU=(0,4,0);newLEFT={add(newU[:2],p)for p in[(0,0),(0,1)]};assert all(l.rot(sub(p,target[:2]),-2)in l.K for p in newLEFT)
funnel=dict(actual_UC_UCC_C1_RAW_chord=C1,actual_target_ENTRY_center=zT,actual_next_D_BASE_chord=Dnext,UC_UCC_or_next_D_prior_nonadjacent_ENTRY_vertex_return=True,actual_next_U_family_genuinely_NEW_LEFT_cells=sorted(newLEFT),next_U_foreign_true_age_le4='newU entryClock0 same as oldU; use its own earlySTAR completeMISS and bf1018 up toGLOBALfirstENTRY, not noFORE star permanence.',all_NEW_LEFT_in_actual_target_ENTRY_K=True,remaining_actual_creator='plainU',remaining_actual_immediate_next_FULL_family='V/VC/VCC at0,4,N, ENTRY C clock0')
# r is genuine first-V RAW R4, preserved by ownC tails and freshRAWr min5
# strictly beforeFORE. Align every actual FOREIGN input, retaining plain
# creator/firstV coordinates and originalU STAR+bud BEFORE-state only.
fr=[];fg=[]
for n in range(5):
 h=(-n)%4
 for A in'FQB':
  ctx=l.trace(W[A]+l.M)
  for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
   p=(*sub(r,l.rot(slot,h)),h);rec=dict(FOREIGN=A,true_old_U_and_first_V_ENTRY_to_FOREIGN_ENTRY_C_clock=n,ENTRY=p,old_first_V_r_TRUE_input=slot,actual_owner=o.describe(A,ctx['first'][slot][1]))
   if(sum(p[:2])+h)%2:why='sector'
   elif any((loc:=l.rot(sub(tag,p[:2]),-h))in ctx['first']or loc in l.K for tag in STAR):why='forbidden_complete_initial_U_STAR_context_hit_at_age_le4'
   else:
    bad=conflict(A,p,{s})
    if bad:rec['original_U_pre_FOREIGN_bud_CORE_or_FIRST_WHITE']=bad;why='pre_FOREIGN_original_U_bud_BLACK_CORE_or_WHITE_contradiction'
    else:
     fg.append(rec)
     if n==0:
      assert A=='F'and p in[(4,4,0),(3,5,0)]and p[1]<7;why='N0_FOREIGN_head_below_genuine_firstV_RAW_EXIT_y7'
     elif n==1:
      if p==(-3,6,3):assert A=='B';why='W1_FOREIGN_y6_below_actual_firstV_C_W_start_y8'
      else:assert p in[(2,9,3),(3,8,3)]and p[1]-p[0]<=7;why='W1_FOREIGN_H_le7_below_firstV_firstW_H7_plus_required_nonempty_W_BASE_increment2'
     elif n==2:
      assert p in[(-5,5,2),(-3,7,2),(-2,6,2),(0,6,2)]
      why={(-5,5,2):'FOREIGN_erases_selected_q_then_genuine_NEW_lower_min3_excludes_rebirth_at_age_le2',(-3,7,2):'fresh_FOREIGN_R36_tag1,5_current_by_N_W_S_endpoint_guard_inside_targetCORE',(-2,6,2):'spent_creating_U_marker_upper_Gminus1,4_is_WHITE_at_FOREIGN_n2_ENTRY', (0,6,2):'fresh_FOREIGN_R25_tagminus1,4_CURRENT_by_signed_NE3_reserve_inside_targetCORE'}[p]
     elif n==3:
      ep=after(W[A],p);assert ep[2]==3 and ep[0]<=0;rec['actual_FOREIGN_W_RAW_EXIT']=ep;why='remaining_W_to_S_C_puts_x_le_minus1_then_zeroS_cannot_reach_target_x0'
     else:
      assert n==4 and A=='F'and p in[(4,4,0),(3,5,0)];ep=after(W[A],p);assert ep[2]==2 and ep[1]<4;rec['actual_FOREIGN_S_RAW_EXIT']=ep;why='no_C_left_S_foreign_EXIT_below_target_y4'
   rec['route']=why;fr.append(rec)
assert len(fr)==235 and len(fg)==33 and Counter(x['true_old_U_and_first_V_ENTRY_to_FOREIGN_ENTRY_C_clock']for x in fg)=={0:2,1:7,2:12,3:10,4:2}
# Spent source-U upper G is actual nextV firstL1 at overall source tick29,
# and no later R within that V. Begin earliest BLACK-cut descent at this
# actual V RAW EXIT, not at oldU RAWexit whereG was still aliveCORE.
vr=l.trace(W['V']);assert vr['last'][(-1,0)]==('L',1);assert add((0,4),(-1,0))==G
HOLD=STAR|{t,s};RR={A:[dict(slot=p,last_R_tick0=k,first=l.trace(W[A])['first'][p],EXIT_CORE=l.rot(sub(p,after(W[A])[:2]),-after(W[A])[2])in l.K)for p,(c,k)in l.trace(W[A])['last'].items()if c=='R']for A in'DCVU'}
GR=[];GK=[]
for n in range(3):
 h=(-n)%4
 for A in'DCVU':
  raw=l.trace(W[A]);ctx=l.trace(W[A]+l.M)
  for rr in RR[A]:
   slot=tuple(rr['slot']);p=(*sub(G,l.rot(slot,h)),h);ep=after(W[A],p);rec=dict(earlier_RAW=A,ENTRY=p,actual_clock=n,physical_final_R=rr,RAW_EXIT=ep)
   if(sum(p[:2])+h)%2:why='sector'
   elif raw['first'][slot][0]=='L':why='firstL_requires_an_earlier_BLACK_cut_after_actual_G_deletion'
   elif any((loc:=l.rot(sub(tag,p[:2]),-h))in ctx['first']or loc in l.K for tag in HOLD):why='old8_earlier_writer_hits_independently_CURRENT_initial_STAR_arm_or_bud'
   else:
    GK.append(rec)
    if n==0:assert p[1]<7;why='N0_head_below_actual_firstV_RAW_EXIT_y7'
    elif n==1:assert p[1]<8;why='W1_head_below_actual_firstV_first_C_W_start_y8'
    elif A=='C':why='S2_C_writer_completes3_after_FOREIGN_n2'
    else:assert ep[1]<=4<6;why='S2_writer_RAW_EXIT_y_le4_cannot_reach_FOREIGN_y6_by_zeroS'
   rec['route']=why;GR.append(rec)
assert len(GR)==108
Gcuts=[]
for A in'FQB':
 p=(-2,6,2);loc=l.rot(sub(G,p[:2]),-2);f=l.trace(W[A]+l.M)['first'][loc];assert loc==(-1,2)and f==('L',13);Gcuts.append(dict(FOREIGN=A,ENTRY=p,source_spent_G=G,local=loc,actual_FIRST_BLACK=f,owner=o.describe(A,13),physical_WHITE_at_FOREIGN_ENTRY_by_108_CORE_inclusive_origins=True))
# Age2 n2 first family: q is physically L-erased by thisFOREIGN. Leading
# zero/one C cannot repairy2 from the actual N exit heights7/9/10. Two
# leadingCs followedBASE is impossible in actual U-entry FIRSTFOREIGN.
# Target selected lower slot is min3, NOT upper min2. The postFOREIGN
# BASE-to-BASE factor has no initial q and every producer starts>=clock2.
qr=[];ages=json.loads((R/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json').read_text());assert[4,1,2,3]in ages and[4,0,3,2]in ages
for A in'FQB':
 p=(-5,5,2);raw=l.trace(W[A]);loc=l.rot(sub(q,p[:2]),-2);assert raw['last'][loc]==('L',35);ep=after(W[A],p);assert ep[2]==0 and ep[1]>=7
 states=[]
 for lead in['','C']:
  cp=after(''.join(W[a]for a in lead),ep);assert l.rot(sub(q,cp[:2]),-cp[2])not in l.K
  if lead:
   for slot,rr in l.trace(W['C'])['last'].items():
    if rr[0]=='R':assert add(ep[:2],slot)[1]>q[1]
  states.append(dict(actual_leading_ordinary_prefix=lead,actual_first_BASE_ENTRY=cp,q_physical_WHITE_and_not_CORE_at_first_BASE_ENTRY=True))
 assert l.rot(sub(q,target[:2]),-2)==(1,2)
 qr.append(dict(FOREIGN=A,ENTRY=p,physically_erased_q=q,actual_last_L_own_tick0=35,actual_N_RAW_EXIT=ep,zero_or_one_leading_C_cut_states=states,no_two_leading_C_then_BASE='signed594a actualleadingCC terminal grammar, not a completed-nextword assumption',actual_target_selected_lower_input=(1,2),actual_target_owner=o.describe('V',13),exact_actual_lower_age_minimum=3,upper_age2_is_NOT_used=True,post_FOREIGN_producer_entry_clock_ge2_and_target_clock4_gives_age_le2=True,actual_BASE_ending_G8_factor='Choose FIRST actual postFOREIGN D/V/U to targetV. Its real predecessor isFOREIGN orC; actual base-cut grammar applies. The initial q is WHITE, so cannot be an untouched residual root. Any FINAL external target input must be a genuine full-producer O born within this actual factor, even if its physical R occurred in an internal CORE. All have age<=2<selected3. No age is assigned toFOREIGN.',no_source_q_identity_survival_assumed=True))
# n2 third family: genuine sourceFOREIGN NE R25 atlocal1,2 survives the
# complete remaining2C ordinary interval in both branches of signedf24.
ne=json.loads((R/'foreign_three_C_NE_reserve_2026-10-24/three_C_NE_reserve.json').read_text());assert[1,2]in ne['transfer_dichotomy']['nine_retained_originals'];necuts=[]
for A in'FQB':
 p=(0,6,2);slot=(1,2);tag=add(p[:2],l.rot(slot,2));assert tag==(-1,4)and l.trace(W[A])['last'][slot]==('R',25)and list(slot)in l.literal_geometry(W[A])['outputs'];local=l.rot(sub(tag,target[:2]),-2);assert local in l.K
 necuts.append(dict(FOREIGN=A,ENTRY=p,genuine_NEW_FOREIGN_R25=tag,own_R_tick0=25,source_ENTRY_chart_cell=slot,exact_remaining_ordinary_C_count=2,signed_NE3_nine_retained_originals_contains_this_same_cell=True,target_ENTRY_CORE_local=local,no_old_SOURCE_bud_or_foreign_word_after_this_source=True))
# n2 second family: sourceFOREIGN R36 at(-4,2) becomes newtagT=(1,5).
# It is below all subsequent N/W input heads; S input-loss exits cannot
# reach target0,4 by any zero-C S word. Marker CORE loss included.
def Scounts(ep,tar):
 dx=ep[0]-tar[0];drop=ep[1]-tar[1];out=[]
 if dx<0 or drop<0:return out
 for nv in range(dx+1):
  nd=dx-nv;rem=drop-nd-3*nv
  if rem>=0 and rem%4==0:out.append(dict(D=nd,V=nv,U=rem//4))
 return out
T=(1,5);tg=[];Srows=[]
for A in'FQB':
 p=(-3,7,2);tag=add(p[:2],l.rot((-4,2),2));assert tag==T and l.trace(W[A])['last'][(-4,2)]==('R',36)and[-4,2]in l.literal_geometry(W[A])['outputs'];ep=after(W[A],p);assert ep[2]==0 and ep[1]>=9
 tg.append(dict(FOREIGN=A,ENTRY=p,genuine_NEW_R36_tag=T,actual_N_FOREIGN_RAW_EXIT=ep,N_inputs_need_head_y_le4_but_actual_heads_y_ge9=True,W_inputs_need_head_y_le6_but_actual_W_heads_y_ge10=True,target_ENTRY_CORE_local=l.rot(sub(T,target[:2]),-2)))
for A in'DVU':
 for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
  p=(*sub(T,l.rot(slot,2)),2);ep=after(W[A],p);mods=Scounts(ep,target);assert not mods
  Srows.append(dict(S_loss_RAW=A,ENTRY=p,true_input=slot,actual_owner=o.describe(A,l.trace(W[A]+l.M)['first'][slot][1]),RAW_EXIT=ep,all_zeroC_S_endpoint_models_to_target=mods))
assert len(Srows)==8 and all(x['target_ENTRY_CORE_local']in l.K for x in tg)
# All33 necessary FOREIGN rLOSS rows now have exact externally scoped
# guards. rENTRYCORE/firstWHITE would already contradict original r, so
# completed actual contexts really MISS it on every target-compatible
# history. Then use only signed PORTABLE r clock, not its fixed45 masks.
clock=json.loads((R/'V_r_postforeign_contact_clock_2026-10-24/r_contact_clock.json').read_text());rr=clock['all9_actual_source_tail_and_plain_ordinary_r_first_loss_interfaces'];assert len(rr)==9
# Fields of the9 interfaces are retained verbatim; actual three consumer
# exits are established by literal endpoint reconstruction in each chart.
rports=[]
for A,p in[('D',(1,0,3)),('V',(3,0,3)),('U',(4,1,3))]:
 ep=after(W[A],p);assert ep==(0,1,3);globalep=(0,5,3);rports.append(dict(actual_plain_consumer=A,source_V_chart_ENTRY=p,source_V_chart_RAW_EXIT=ep,old_U_chart_RAW_EXIT=globalep,TOTAL_source_U_and_V_clock=3,one_remaining_W_to_S_C_decreases_x_to_le_minus1_then_S_cannot_reach_target_x0=True))
D=[R/'V_r_postforeign_contact_clock_2026-10-24/manifest.json',R/'audits/check_V_r_postforeign_clock_independent.json',R/'fresh_RAW_V_U_early_donor_guards_2026-10-24/manifest.json',R/'audits/check_fresh_RAW_donors_independent.json',R/'foreign_three_C_NE_reserve_2026-10-24/manifest.json',R/'audits/check_foreign_three_C_NE_reserve_independent.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/manifest.json',R/'audits/check_RAW_G8_base_cut_bridge_independent.json',R/'leading_C_ordinary_owner_2026-10-24/manifest.json',R/'audits/check_leading_C_ordinary_owner_independent.json',R/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json',R/'old_V_third_age2_genuine_field_2026-10-24/manifest.json',R/'audits/check_old_V_third_age2_independent.json',R/'U_LEFT_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_LEFT_contact_or_persistence_independent.json',R/'foreign_U_star_age2_2026-10-23/manifest.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',R/'audits/check_foreign_U_raw_ages34_independent.json',R/'foreign_U_marker_clocks_2026-10-23/manifest.json',R/'audits/check_foreign_U_age2_and_marker_independent.json',R/'U_arm_W_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_U_arm_W_guard_independent.json',R/'word_stabilization/U_foreign_prefix_bud_cuts_frozen_20261023_2201/manifest.json',R/'audits/check_U_foreign_prefix_buds_independent.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'audits/check_complete8_foreign_adjacency_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py'];assert all(p.exists()for p in D),[str(p)for p in D if not p.exists()]
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual preFOREIGN genuineU-family source in U-entryG8, FIRSTF/Q/B then arbitrary ordinary-only RAW tail plus actualfinalM11. At GLOBAL first proxy contact outgoing-old-owned by thatU-base, actor cannot be V0,4S atTOTAL C4. This closes only the S-facing V pose, not D0,2S or arbitrarytail simplicity.',actual_creator_and_first_next_BASE_all_length_funnel=funnel,all235_actual_FOREIGN_first_V_r_TRUE_input_roles=fr,all33_foreign_r_RETIREMENT_candidates_and_exact_routes=fg,source_spent_upper_G_WHITE_initial_cut='Actual firstV at0,4N consumes oldU marker-only upperGminus1,4 at ownL1/read2, overall source tick29. Its RAWlast at this cell isL1, soG isWHITE at actual firstV_RAW_EXIT1,7N. Do not claim it wasWHITE at oldU_RAW_EXIT where it was aliveCORE.',all108_pre_FOREIGN_physical_CORE_inclusive_G_first_BLACK_cut_origins=GR,all13_G_origins_and_exact_height_or_clock_cuts=GK,all3_FOREIGN_minus2_6_S_actual_G_FIRST_BLACK_contradictions=Gcuts,all3_FOREIGN_minus5_5_S_selected_q_NEW_age3_guards=qr,all3_FOREIGN_0_6_S_genuinely_NEW_R25_current_tag_guards=necuts,all3_FOREIGN_minus3_7_S_genuinely_NEW_R36_current_tag_interfaces=tg,all8_R36_S_CURRENT_loss_endpoint_exclusions=Srows,portable_original_first_V_r_CLOCK3_scope=clock['portable_lemma_scope'],all3_actual_r_loss_exit_ports_and_future_W_S_cut=rports,SAME_r_FOREIGN_MISS_conclusion='Originalr isCURRENT beforeFORE by freshRAWV min5 strictly in the oldordinary interval. Actual ENTRYCORE/firstWHITE already impossible; all235 TRUEinput roles now excluded for a target-compatible history. Thus COMPLETEFOREIGN RAW+actualM11 MISSES SAMEr. This is proved, not assumed from fixed45 THIRD masks.',after_FOREIGN_clock_use='Apply signed277 portable first-loss clock only once completeFOREIGN MISS is established. A strictly earlier r loss hasTOTALK3 and RAWEXIT0,5,W; one remainingC4 after any zeroW givesSheadx<=-1 and zeroS cannot reach targetx0. If r has not lost, SAMECURRENT r0,4 lies in actual target ENTRYCORE. No persistence through targetRAW.',strict_limits=['no old bud or altered firstV cohort assumed current afterFOREIGN','freshFOREIGN R25 andR36 are NEW identities, not recolored originals','selectedV lower(1,2) minimum3 only inside a real postFOREIGN BASE-ending G8 factor; no upper-min2 substitution','actual spentG erasure is nextRAW read2, not oldU ownRAW or invented first-read ownership','FIRST FOREIGN only and GLOBAL-first stopping; no secondFOREIGN or full-tail simplicity','no fixed ordinary index or zero-rail length cap'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'S_V.json').write_text(json.dumps(out,indent=2)+'\n');print('OldU all-tail S4 V:portable creatorfunnel,235 FORE r roles→33 necessary,all cut by endpoints/4n2port guards; SOURCEr FOREMISS then K3 exit cannotreachS4 target. D0,2S staysseparate.')
