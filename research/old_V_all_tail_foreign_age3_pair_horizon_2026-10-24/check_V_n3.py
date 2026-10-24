"""All-length old V source, true foreign age3 and total contact clock3.
Foreign input-to-exit normal bound derives a real first/two-RAW horizon;
it does not assume the target's ordinary index. No old age crossesFOREIGN.
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
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h
def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(A,p):return z(p),z(after(W[A],p))
def rel(q,p):return l.rot(sub(q,p[:2]),-p[2])
def curcuts(A,p,tags):
 tr=l.trace(W[A]+l.M);out=[]
 for tag in sorted(tags):
  loc=rel(tag,p);f=tr['first'].get(loc)
  if loc in l.K or f and f[0]=='R':out.append(dict(SAME_CURRENT_tag=tag,local=loc,ENTRY_CORE=loc in l.K,actual_first=f,actual_owner=o.describe(A,f[1])if f else None))
 return out
angles=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows'];va=[x for x in angles if x['source_class']=='preFOREIGN_ordinary'and x['source_atom']=='V'];boxes=[];geo=[];a,b=chord('V',(0,0,0));u=sub(b,a);r=(0,0);B=(1,0);C=(2,1);bud=(2,2)
for ar in va:
 A=ar['contact_atom'];assert3=3 in ar['allowed_C_counts_before_contact_ENTRY'];assert assert3
 c,d=chord(A,(0,0,3));v=sub(d,c);de=det(u,v);assert de
 cs=[tuple(F(a[k]+ss*u[k]-c[k]-tt*v[k],2)for k in(0,1))for ss in(0,1)for tt in(0,1)];bd=[(floor(min(q[k]for q in cs)),ceil(max(q[k]for q in cs)))for k in(0,1)];boxes.append(dict(actor=A,rational_corners=[[[q.numerator,q.denominator]for q in p]for p in cs],integer_bounds=bd))
 for x in range(bd[0][0],bd[0][1]+1):
  for y in range(bd[1][0],bd[1][1]+1):
   if(x+y+3)%2:continue
   q=sub(add(c,(2*x,2*y)),a);s,t=F(det(q,v),de),F(det(q,u),de)
   if not(0<=s<1 and 0<t<=1):continue
   p=(x,y,3);pc=curcuts(A,p,{r,B})
   if pc:route='SAME_r_B_pair_CURRENT_at_ENTRY';extra=[]
   else:
    cc=curcuts(A,p,{C})
    if cc:route='SAME_C_FOREIGN_MISS_then_portable_W_rail';extra=cc
    else:assert A=='U'and p==(3,2,3);bc=curcuts(A,p,{bud});assert bc;route='SAME_bud_FOREIGN_MISS_then_W_loss_exit_x_le2_cannot_reach_targetx3';extra=bc
   geo.append(dict(actor=A,ENTRY=p,TOTAL_ordinary_C=3,true_preFOREIGN_source_ENTRY_C_age=3,old_outgoing_s=str(s),new_positive_t=str(t),pair_entry_cuts=pc,additional_current_tag_cuts=extra,route=route))
assert len(geo)==15 and all(g['ENTRY'][0]>=0 for g in geo)and Counter(g['route']for g in geo)=={'SAME_r_B_pair_CURRENT_at_ENTRY':9,'SAME_C_FOREIGN_MISS_then_portable_W_rail':5,'SAME_bud_FOREIGN_MISS_then_W_loss_exit_x_le2_cannot_reach_targetx3':1}
# Generic actual FOREIGN headingE normal: any TRUE input tag at x0 has
# exitX<=x0. Every marker-only input and true CORE capture remains real.
normal=[]
for A in'FQB':
 ctx=l.trace(W[A]+l.M)
 for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
  p=(*sub((0,0),l.rot(slot,1)),1);ex=after(W[A],p);assert ex[2]==3 and ex[0]<=0
  normal.append(dict(FOREIGN=A,true_input=slot,tag_x_normalized=0,actual_FOREIGN_ENTRY=p,actual_W_RAW_EXIT=ex,exit_x_minus_input_tag_x=ex[0],actual_physical_first_L=ctx['first'][slot],actual_owner=o.describe(A,ctx['first'][slot][1]),includes_future_marker_CAPTURE_not_necessarily_executed_physical_L=True))
assert len(normal)==47
# Derive complete MISS at candidate-compatible funding cuts, not a generic
# port seal. If foreign TRUEinput consumed tagged x, a zero-W rail before
# candidate has d+3v+4u <=tag_x-target_x. A bound <=1 means empty orD,
# hence candidate is RAW1/2 afterFORE, contradicted by signed9aa for RAW1 and signed3420 for RAW2.
horizons=[]
for g in geo:
 need=[r,B]
 if g['route']=='SAME_C_FOREIGN_MISS_then_portable_W_rail':need.append(C)
 if g['route']=='SAME_bud_FOREIGN_MISS_then_W_loss_exit_x_le2_cannot_reach_targetx3':need.append(bud)
 for tag in need:
  maxdrop=tag[0]-g['ENTRY'][0]
  if maxdrop<0:route='actual_FOREIGN_exit_x_le_tagx_lt_targetx_zeroW_cannot_reach'
  else:assert maxdrop<=1;route='at_most_one_D_before_target_forces_RAW1_signed9aa_or_RAW2_signed3420_contact'
  horizons.append(dict(actor=g['actor'],target_ENTRY=g['ENTRY'],SAME_original_source_tag=tag,actual_FOREIGN_heading='E',true_FOREIGN_age=3,TOTAL_contact_clock=3,no_C_between_FOREIGN_EXIT_and_contact_ENTRY=True,all_possible_nonnegative_zeroW_counts_satisfy=f'dW+3vW+4uW <= {maxdrop}',maximum_prior_ordinary_RAW_count=None if maxdrop<0 else maxdrop,when_one_prior_atom_it_is_plain_RAW_D=0<=maxdrop<=1,route=route,ENTRYCORE_or_firstWHITE_tag_foreign_hit_already_impossible_by_genuine_funding_CURRENT=True))
assert len(horizons)==36
birth=[]
for full in['V','VC','VCC']:
 tr=l.trace(''.join(W[A]for A in full));ba=l.trace(W['V']);og=l.literal_geometry(''.join(W[A]for A in full))
 for tag in[r,B,C,bud]:assert tr['last'][tag]==ba['last'][tag]and list(tag)in og['outputs']
 birth.append(dict(full_source=full,true_full_ENTRY_C_clock=0,actual_full_completion_clock=full.count('C'),all4_SAME_births=[dict(tag=t,R_tick0=ba['last'][t][1])for t in[r,B,C,bud]],all4_CURRENT_before_FOREIGN3_by_r5_B4_and_C_bud_young552=True))
# Explicit zero-W port inventories for the downstream rails. CURRENT pair
# transfer comes ONLY from signed358+b84 under actual proven MISS; the
#9 TRUE simultaneous rows in b84 are earlier actual source contacts.
Cports=[];budports=[]
for A in'DVU':
 ctx=l.trace(W[A]+l.M)
 for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
  p=(*sub(C,l.rot(slot,3)),3);ex=after(W[A],p);rec=dict(consumer=A,ENTRY=p,C_true_input=slot,owner=o.describe(A,ctx['first'][slot][1]),RAW_EXIT=ex)
  if(sum(p[:2])+3)%2:why='sector'
  elif A=='U'and p==(3,2,3):why='earlier_actual_old_V_chord_contact_unless_it_is_target;entry_CURRENT_still_suffices'
  else:assert A=='U'and p==(4,1,3);cuts=curcuts(A,p,{B});assert cuts;rec['independent_CURRENT_B_first_WHITE']=cuts;why='independent_CURRENT_B_actual_firstWHITE'
  rec['route']=why;Cports.append(rec)
  pb=(*sub(bud,l.rot(slot,3)),3);eb=after(W[A],pb);assert eb[0]<=2;budports.append(dict(consumer=A,ENTRY=pb,bud_true_input=slot,owner=o.describe(A,ctx['first'][slot][1]),RAW_EXIT=eb,exit_x_le2=True,target_U3_2_has_x3_and_zeroW_never_increases_x=True))
assert len(Cports)==8 and len(budports)==8
D=[R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'V_postforeign_pair_rail_reserve_2026-10-24/manifest.json',R/'V_postforeign_pair_rail_reserve_2026-10-24/simultaneous_input_qualification_manifest.json',R/'audits/check_V_pair_rail_independent.json',R/'audits/check_V_pair_simultaneous_qualification_independent.json',R/'V_r_postforeign_contact_clock_2026-10-24/manifest.json',R/'audits/check_V_r_postforeign_clock_independent.json',R/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',R/'audits/check_first_foreign_returned_simplicity_independent.json',R/'first_foreign_two_ordinary_simplicity_2026-10-24/manifest.json',R/'audits/two_RAW_simplicity_independent.json',R/'full_packet_CURRENT_internal_RAW_lift_2026-10-24/manifest.json',R/'old_U_all_tail_S_D_coupled_reserve_2026-10-24/C_CORE_wording_manifest.json',R/'audits/check_old_U_S4_D_coupled_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py'];assert all(p.exists()for p in D),[str(p)for p in D if not p.exists()]
out=dict(status='AUTHOR_FROZEN_PENDING_REVIEW',scope='Only old preFOREIGN outgoing V-source V/VC/VCC, true sourceENTRY-to-FIRSTFOREIGN_ENTRY age n3 and TOTALordinaryC3 at GLOBALfirst ordinary contact; arbitrary zeroC W suffix length plus actualfinalM11. This is not other true ages or full oldV/alltail simplicity.',all4_signed_old_V_angle_rows=va,all4_rational_head_boxes=boxes,all15_outgoing_owned_W3_geometries_and_guard_routes=geo,all3_genuine_source_tail_birth_and_funding_interfaces=birth,all47_actual_FOREIGN_input_to_W_EXIT_normal_bounds=normal,all36_genuine_foreign_MISS_target_horizons=horizons,FOREIGN_MISS_precedes_transfer='Originalr/B CURRENT beforeFOREIGN3 by actual preFOREIGN bounds. FOREIGNENTRYCORE/firstWHITE hit already contradicts that state. Any TRUEFOREIGN consumption has actual exitx<=tagx. Exact zeroW normal forces target within RAW1/2, or makes it unreachable. Signed9aa excludes actual firstRAW contact and signed3420 excludes actual secondRAW contact under their respective real Uentry+FIRSTFOREIGN+actualM11 premises. Do not assume an ungiven secondRAW when the actual target is first. Thus completeFOREIGN r/B MISS is proved, not assumed from fixed-third inverses. C/bud MISS is separately proved only where needed by the same normal bound.',portable_pair_use='Now use only signed358+b84 portable pair lemma: with SAMEr/B CURRENT beforeFOREIGN and actual completeMISS and n>=3, any first ordinary pair loss under a still-simple prefix hasTOTALK2, earlier than actualFOREIGN age3. r-first and simultaneous TRUEinput rows retain their actual-source-contact dependency; not all36 held-r rows are literal color conflicts. Therefore SAMEpair CURRENT at targetENTRY, not through target.',all8_portable_C_W_firstloss_roles=Cports,all8_portable_bud_W_firstloss_endpoint_bounds=budports,source_C_and_bud_transfer_scope='Only zeroC W afterFOREIGN; C firstloss either actual earlier oldV contact or currentB firstWHITE. Bud any firstloss RAWexitx<=2 cannot reach final targetx3 by zeroW. Neither uses postFOREIGN age. C has no external input and the three external/two alreadyENTRYCORE capture distinction prevents silent absorption.',no_fixed_actor_index_assumed_in_horizon=True,no_ordinary_RAW_to_G8_tail_parse_or_terminal_DCC_ban_needed=True,no_old_age_after_FOREIGN_or_original_A_cleanup_assumed=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'V_n3.json').write_text(json.dumps(out,indent=2)+'\n');print('OldV trueFOREIGN3/TOTAL3:15 heads,47 normal ports,36 target-derived RAW<=2 horizons proveactualMISS;9 pair+5 C+1 bud. No fixedindex.')
