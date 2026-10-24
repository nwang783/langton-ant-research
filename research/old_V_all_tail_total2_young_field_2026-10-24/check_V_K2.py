"""Old V TOTAL2 source slice: genuine funding MISS and a stopped young field.
The literal firstloss table is reused, not its TOTAL3 future conclusion.
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
RES={(0,0),(1,0),(2,1),(2,2)};angles=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows'];a,b=chord('V',(0,0,0));u=sub(b,a);geo=[];boxes=[]
for A in'DCVU':
 ar=next(r for r in angles if r['source_class']=='preFOREIGN_ordinary'and r['source_atom']=='V'and r['contact_atom']==A);assert 2 in ar['allowed_C_counts_before_contact_ENTRY']
 c,d=chord(A,(0,0,0));v=sub(d,c);de=det(u,v);cs=[tuple(F(a[k]+ss*u[k]-c[k]-tt*v[k],2)for k in(0,1))for ss in(0,1)for tt in(0,1)];bd=[(floor(min(q[k]for q in cs)),ceil(max(q[k]for q in cs)))for k in(0,1)];boxes.append(dict(actor=A,rational_corners=[[[q.numerator,q.denominator]for q in p]for p in cs],integer_bounds=bd,parallel=not bool(de)))
 for x in range(bd[0][0],bd[0][1]+1):
  for y in range(bd[1][0],bd[1][1]+1):
   if(x+y)%2:continue
   q=sub(add(c,(2*x,2*y)),a)
   if de:
    ss,tt=F(det(q,v),de),F(det(q,u),de)
    if not(0<=ss<1 and 0<tt<=1):continue
   else:
    if det(q,u):continue
    kk=0 if v[0]else 1;ss=F(0);tt=F(-q[kk],v[kk])
    if not(0<tt<=1 and add(q,(tt*v[0],tt*v[1]))==(0,0)):continue
   p=(x,y,0);cuts=curcuts(A,p,RES);assert cuts and y<=-1;geo.append(dict(actor=A,ENTRY=p,TOTAL_C=2,old_outgoing_s=str(ss),new_positive_t=str(tt),same_original_fourtag_ENTRY_cuts=cuts))
assert len(geo)==5 and len(boxes)==4
# At trueFOREage2, any actual FOREIGN S input at tagy exits N with
# y>=tagy>=0. The target N heads all lie y<=-1; zeroN strictly raisesy.
fore=[]
for tag in sorted(RES):
 for A in'FQB':
  ctx=l.trace(W[A]+l.M)
  for sl in map(tuple,l.literal_geometry(W[A])['inputs']):
   p=(*add(tag,sl),2);ex=after(W[A],p);assert ex[2]==0 and ex[1]>=tag[1]>=0
   fore.append(dict(SAME_source_tag=tag,FOREIGN=A,ENTRY=p,true_input=sl,actual_owner=o.describe(A,ctx['first'][sl][1]),actual_N_RAW_EXIT=ex,exit_y_ge_tag_y_ge0=True,all5_target_head_y_le_minus1=True,no_zeroN_motion_can_reach_any_target=True))
assert len(fore)==188
Y=json.loads((R/'old_V_young_FOREIGN_ports_total3_transfer_2026-10-24/young_ports.json').read_text());keep=Y['all8_firstloss_ports_set_equal_signed0af'];assert len(keep)==8;loss=[]
for k in keep:
 p=tuple(k['ENTRY']);ex=tuple(k['RAW_EXIT'])
 if p[2]==3:why='W_firstloss_requires_TOTAL3_strictly_after_target_TOTAL2'
 else:assert p[2]==0 and ex[1]>=0;why='N2_firstloss_RAW_EXIT_y_ge0_then_zeroN_cannot_descend_to_target_y_le_minus1'
 loss.append(dict(actual_firstloss=k,route=why))
D=[R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'old_V_young_FOREIGN_ports_total3_transfer_2026-10-24/manifest.json',R/'audits/check_old_V_young_ports_independent.json',R/'V_postforeign_pair_rail_reserve_2026-10-24/manifest.json',R/'audits/check_V_pair_rail_independent.json',R/'fresh_RAW_V_U_early_donor_guards_2026-10-24/manifest.json',R/'audits/check_fresh_RAW_donors_independent.json',R/'full_packet_CURRENT_internal_RAW_lift_2026-10-24/manifest.json',R/'old_U_all_tail_S_D_coupled_reserve_2026-10-24/C_CORE_wording_manifest.json',R/'audits/check_old_U_S4_D_coupled_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py'];assert all(p.exists()for p in D),[str(p)for p in D if not p.exists()]
out=dict(status='AUTHOR_FROZEN_PENDING_REVIEW',scope='Only old preFOREIGN outgoing V-source V/VC/VCC, GLOBALfirst ordinary contact TOTAL C2 after FIRSTF/Q/B and arbitrary ordinary-only suffix plusactualfinalM11. TrueFOREage n0/1/2; no other totalclock or full-tail simplicity.',all4_exact_rational_source_target_boxes=boxes,all5_outgoing_owned_TOTAL2_N_geometries_and_CURRENT_field_cuts=geo,all188_true_FOREIGN_age2_marker_inclusive_input_to_N_EXIT_y_bounds=fore,trueFOREIGN_age0_or1_MISS='Use only the signed literal youngport part ofadc468: same4 source tags CURRENT beforeFOREIGN by genuine preFOREIGN r5/B4/Cbud-through3 and actual own-tail preservation; TRUEinput at those coordinates impossible in actual zero/oneC sourceV-toFOREIGN word. CURRENT also forbids ENTRYCORE/firstWHITE, hence completeMISS. No TOTAL3 transfer conclusion is imported.',trueFOREIGN_age2_MISS='Same4 CURRENT beforeFOREIGN2. ENTRYCORE/firstWHITE impossible; every actualTRUEinput yields N_RAW_EXIT_y>=tagY>=0. No C remains before TOTAL2 actor, every N base strictly raisesy, while all5 targetHEAD y<=-1. Thus completeFOREIGN MISS4 on target-compatible histories.',all128_signed_generic_fourheading_firstloss_rows_copied_without_TOTAL3_conclusion=Y['all128_full_four_heading_first_CURRENT_loss_roles'],all8_possible_firstloss_ports_and_TOTAL2_normal_cuts=loss,CURRENT_field_at_target='After actual completeFOREIGNMISS4, the source field starts current atFOREIGNEXIT. Fresh signed128 table is intrinsic sector/other-held-tag/source-chord logic, no assumption of a TOTAL3 target or FOREage2. W ports would be after TOTAL2; N ports have already exited above every negative-y target. C cannot silently absorb currenttags by I0 and3external/2entryCORE distinction. Thus SAME4 CURRENT at targetENTRY and all5 literal masks contradict.',CORE_scope='Marker capture is CURRENTloss at its actual RAWexit, not necessarily physicaldeath. No tag from an alteredFOREIGN or recoloredR is substituted for the original. Actual own V/VC/VCC tails and true completion clocks remain as in signed source funding facts.',no_fixed_suffix_index_or_foreign_maturity_or_terminal_DCC_parse=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'V_K2.json').write_text(json.dumps(out,indent=2)+'\n');print('OldV TOTAL2 author:5 N targets all y<0; young portMISS at n0/1;188 n2FOREtag exits y>=0;generic8 firstloss ports cannot reach targets;CURRENT field cuts5.')
