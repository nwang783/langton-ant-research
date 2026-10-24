"""All-length old V source, true foreign age2 and total contact clock3.
Foreign consumption derives a short endpoint horizon; arbitrary later
ordinary first losses use a genuinely held four-tag cohort and C port.
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
# Geometry depends on TOTAL3 only; do not copy the previous trueage3.
G=json.loads((R/'old_V_all_tail_foreign_age3_pair_horizon_2026-10-24/V_n3.json').read_text());geo=[dict(actor=g['actor'],ENTRY=tuple(g['ENTRY']),TOTAL_ordinary_C=3,true_preFOREIGN_age=2,old_outgoing_s=g['old_outgoing_s'],new_positive_t=g['new_positive_t'])for g in G['all15_outgoing_owned_W3_geometries_and_guard_routes']];assert len(geo)==15 and max(g['ENTRY'][1]for g in geo)==2 and min(g['ENTRY'][0]for g in geo)==0
r=(0,0);B=(1,0);C=(2,1);bud=(2,2);RES={r,B,C,bud};birth=[]
for full in['V','VC','VCC']:
 tr=l.trace(''.join(W[a]for a in full));ba=l.trace(W['V']);og=l.literal_geometry(''.join(W[a]for a in full))
 for tag in RES:assert tr['last'][tag]==ba['last'][tag]and list(tag)in og['outputs']
 birth.append(dict(actual_full_source=full,actual_entry_clock=0,actual_completion_clock=full.count('C'),all4_SAME_base_births=[dict(tag=t,actual_last_R=ba['last'][t])for t in sorted(RES)],all4_CURRENT_before_FOREIGN2_by_signed_r5_B4_C_bud_through3=True))
# Exact arbitrary zero-N/C/zero-W semigroup from a given N RAW exit to
# a W target. Y bounds cap N/W positive-y counts; W-U is solved exactly
# from x and is never truncated by depth or a preset run length.
def NCW(ex,tar):
 assert ex[2]==0 and tar[2]==3;Y=tar[1]-ex[1]-1;out=[]
 if Y<0:return out
 for un in range(Y//4+1):
  for vn in range(Y//3+1):
   for dn in range(Y+1):
    rem=Y-dn-3*vn-4*un
    if rem<0:continue
    for vw in range(rem+1):
     dw=rem-vw;num=ex[0]+dn+vn-dw-3*vw-tar[0]
     if num<0 or num%4:continue
     out.append(dict(N_D=dn,N_V=vn,N_U=un,W_D=dw,W_V=vw,W_U=num//4))
 return out
# FORETRUEinput tag q has exitY>=qY at headingS. Exact slot/parity and
# finite target y<=2 make any actual compatible loss target RAW2/3.
# Use TWO/THREE only with their actual respective supplied RAWs+M11.
fore=[];short=[]
for tag in sorted(RES):
 for A in'FQB':
  ctx=l.trace(W[A]+l.M)
  for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
   p=(*add(tag,slot),2);ex=after(W[A],p);assert ex[2]==0 and ex[1]>=tag[1]
   rec=dict(SAME_original_source_tag=tag,FOREIGN=A,ENTRY=p,true_input=slot,actual_owner=o.describe(A,ctx['first'][slot][1]),actual_N_RAW_EXIT=ex,exit_y_minus_tag_y=ex[1]-tag[1],all15_target_endpoint_cases=[])
   if(sum(p[:2])+2)%2:rec['route']='sector'
   else:
    for g in geo:
     tar=g['ENTRY'];models=NCW(ex,tar);cases=[]
     for m in models:
      bases=sum(m.values());assert bases<=1;idx=2+bases;assert idx in[2,3]
      rr=dict(exact_count_model=m,actual_contact_RAW_index_derived_not_assumed=idx,actual_short_simplicity='signed3420_TWO_RAW_with_actual_finalM'if idx==2 else'signed2e5_THREE_RAW_with_actual_finalM',body_shape='C'if bases==0 else'D,C'if m['N_D']==1 else'C,D'if m['W_D']==1 else'UNEXPECTED')
      assert rr['body_shape']!='UNEXPECTED';cases.append(rr);short.append(dict(source_tag=tag,FOREIGN=A,ENTRY=p,target_actor=g['actor'],target_ENTRY=tar,**rr))
     rec['all15_target_endpoint_cases'].append(dict(actor=g['actor'],ENTRY=tar,all_exact_count_models=cases,route='actual_target_derived_RAW2_or_RAW3_contact_contradicts_respective_signed_theorem'if cases else'no_nonnegative_N_C_W_endpoint_solution'))
    rec['route']='target_normal_horizon_no_arbitrary_suffix_index_assumption'
   fore.append(rec)
assert len(fore)==188 and all(x['actual_contact_RAW_index_derived_not_assumed']in[2,3]for x in short)
# Closed source V intersections are earlier GLOBAL contacts even at its
# terminal vertex: source and loss actor are separated by theFOREIGN,
# so no legitimate actual source adjacency exception can apply.
def contact(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);de=det(u,v)
 if de:
  ss,tt=F(det(q,v),de),F(det(q,u),de)
  return dict(old_s=str(ss),new_t=str(tt))if 0<=ss<=1 and 0<=tt<=1 else None
 if det(q,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((F(c[k]-a[k],u[k]),F(d[k]-a[k],u[k])))
 return dict(collinear_old_interval=[str(max(F(0),lo)),str(min(F(1),hi))])if max(0,lo)<=min(1,hi)else None
joint=[];keep=[]
for tag in sorted(RES):
 for A in'DVU':
  ctx=l.trace(W[A]+l.M)
  for hd in range(4):
   for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
    p=(*sub(tag,l.rot(slot,hd)),hd);ex=after(W[A],p);rec=dict(first_lost_SOURCE_reserve_tag=tag,consumer=A,ENTRY=p,true_input=slot,actual_owner=o.describe(A,ctx['first'][slot][1]),actual_RAW_EXIT=ex)
    if hd not in[0,3]:why='not_in_actual_postFOREIGN_N2_or_W3_stages'
    elif(sum(p[:2])+hd)%2:why='sector'
    else:
     bad=curcuts(A,p,RES-{tag})
     if bad:rec['other_SOURCE_reserve_CORE_or_firstWHITE']=bad;why='other_CURRENT_reserve_actual_ENTRY_CORE_or_firstWHITE'
     else:
      cc=contact(*chord('V',(0,0,0)),*chord(A,p))
      if cc:rec['actual_earlier_source_chord_contact']=cc;why='earlier_GLOBAL_proxy_contact_with_genuine_old_V_source_not_legitimate_adjacency'
      else:
       keep.append(rec)
       if tag==B:assert hd==0 and ex==(2,0,0);why='first_B_loss_exact_N2_exit2_0'
       elif tag==C:assert hd==0 and ex==(3,1,0);why='first_C_loss_exact_N2_exit3_1'
       else:assert tag==bud and hd==3 and ex==(2,3,3);why='first_bud_loss_W3_exit_y3_above_every_target_y_le2'
    rec['route']=why;joint.append(rec)
assert len(joint)==128 and len(keep)==8 and Counter(tuple(k['first_lost_SOURCE_reserve_tag'])for k in keep)=={B:3,C:2,bud:3}
# Exact future endpoint obligations after the allowed first LOSS. The
# firstB actors all physically/context-MISS original C and leave it
# outside actual exitCORE; no through-loss-pair assumption is used.
future=[];Cwhite=[]
for k in keep:
 tag=tuple(k['first_lost_SOURCE_reserve_tag']);ex=tuple(k['actual_RAW_EXIT']);A=k['consumer'];p=tuple(k['ENTRY'])
 if tag==bud:
  assert ex[1]==3>max(g['ENTRY'][1]for g in geo);future.append(dict(firstloss=k,all_later_W_heads_y_ge3=True,target_all_y_le2=True,route='unreachable_by_zero_W'))
  continue
 if tag==B:
  assert rel(C,p)not in l.trace(W[A]+l.M)['first']and rel(C,p)not in l.K and rel(C,ex)not in l.K
  cp=(2,0,0);loc=rel(C,cp);first=l.trace(W['C'])['first'][loc];assert loc==(0,1)and first==('R',11)
  Cwhite.append(dict(first_B_loss=k,SAME_original_C_still_CURRENT_at_loss_RAW_EXIT=True,actual_immediately_next_C_ENTRY=cp,source_C_local=loc,actual_first_WHITE=first,owner=o.describe('C',11),contradiction='SAME original C is BLACK at its actual firstWHITE, not a postFOREIGN age rule'))
 for g in geo:
  models=NCW(ex,g['ENTRY'])
  for m in models:
   if tag==C:
    assert m==dict(N_D=0,N_V=0,N_U=0,W_D=0,W_V=0,W_U=0)and g['actor']=='U'and g['ENTRY']==(3,2,3);route='actual_C_then_U_literal_conflict'
   else:
    assert tag==B
    if m['N_D']==1:
     assert m==dict(N_D=1,N_V=0,N_U=0,W_D=0,W_V=0,W_U=0)and g['actor']=='U'and g['ENTRY']==(3,2,3);route='actual_D_C_then_U_literal_conflict'
    else:
     assert m['N_V']==m['N_U']==m['N_D']==m['W_V']==m['W_U']==0 and m['W_D']in[0,1];route='forced_immediate_C2_0N_requires_held_original_C_WHITE_at_own_R11'
   if 'literal' in route:tt=l.trace(W['C']+W['U']+l.M);assert not tt['feasible']
   else:tt=None
   future.append(dict(firstloss=k,target_actor=g['actor'],target_ENTRY=g['ENTRY'],exact_remaining_N_C_W_model=m,route=route,actual_C_U_literal_failure=tt))
assert len(Cwhite)==3 and len(future)==20 # 15 B futures,2 C futures,3 bud universal cuts
# If no firstloss occurs, all four SAME tags remain CURRENT; every target
# has a genuine ENTRYCORE or actual beforeWHITE contradiction.
final=[]
for g in geo:
 cuts=curcuts(g['actor'],g['ENTRY'],RES);assert cuts;final.append(dict(actor=g['actor'],ENTRY=g['ENTRY'],SAME_original_reserve_ENTRY_contradictions=cuts))
D=[R/'old_V_all_tail_foreign_age3_pair_horizon_2026-10-24/manifest.json',R/'audits/check_old_V_age3_horizon_independent.json',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'V_postforeign_pair_rail_reserve_2026-10-24/manifest.json',R/'audits/check_V_pair_rail_independent.json',R/'fresh_RAW_V_U_early_donor_guards_2026-10-24/manifest.json',R/'audits/check_fresh_RAW_donors_independent.json',R/'full_packet_CURRENT_internal_RAW_lift_2026-10-24/manifest.json',R/'old_U_all_tail_S_D_coupled_reserve_2026-10-24/C_CORE_wording_manifest.json',R/'audits/check_old_U_S4_D_coupled_independent.json',R/'first_foreign_two_ordinary_simplicity_2026-10-24/manifest.json',R/'audits/two_RAW_simplicity_independent.json',R/'first_foreign_three_ordinary_simplicity_2026-10-24/manifest.json',R/'audits/check_three_RAW_simplicity_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py'];assert all(p.exists()for p in D),[str(p)for p in D if not p.exists()]
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Only old outgoing V-source V/VC/VCC, true sourceENTRY-to-FIRSTFOREIGN_ENTRY age2 and TOTALordinaryC3, arbitrary ordinary-only suffix plusactualM11 at GLOBALfirstcontact. Other ages/clocks/classes remain separate.',all15_exact_total3_geometries_with_TRUE_age2_not_copied_age3=geo,all3_actual_source_tail_original_birth_and_funding_interfaces=birth,all188_actual_FOREIGN_four_tag_input_exit_roles_and_all15_future_endpoint_cases=fore,all_derived_FOREIGN_consumption_RAW2_RAW3_horizons=short,complete_FOREIGN_four_tag_MISS_statement='All four SAME tags CURRENT beforeFOREIGN2. ENTRYCORE/firstWHITE already impossible. Any TRUEFOREIGN consumption has an actual N exit and exact unrestricted N/C/W endpoint models; every compatible one forces actual oldV GLOBAL contact as RAW2/3, excluded by the respective independently signed actual TWO/THREE theorem. No fixed index, no ungiven fourthRAW, no generic postFOREIGN maturity. Therefore COMPLETEFOREIGN contextMISS all4 holds at each candidate-compatible state.',all128_ordinary_joint_first_CURRENT_loss_roles=joint,all8_only_ordinary_firstloss_ports=keep,all3_firstB_loss_genuine_CURRENT_C_immediate_C_white_guards=Cwhite,all20_exact_post_firstloss_future_obligations=future,all15_no_loss_CURRENT_reserve_target_ENTRY_cuts=final,simultaneous_TRUE_inputs='Retained, never excluded as intrinsic color. Other-held tag cuts use only ENTRYCORE/actual firstWHITE. All surviving firstB ports actually MISSC, so C remains SAME CURRENT at their actual RAW exits. The later forced C2,0N ownR11 is a real executed demand, not an unexecuted tail exclusion.',CORE_scope='CURRENTloss at RAWEXIT can precede physicaldeath in actual next read2; tag labels are not recolored replacements. C I0 and3external firstWHITE/2alreadyENTRYCORE sites exclude silent capture. PreFOREIGN full-cut source facts use only explicit8d68 physical internal-RAW lift.',no_post_FOREIGN_r_B_pair_K2_impossibility_claim=True,no_G8_parsing_or_produced_age_rule_after_FOREIGN=True,no_TRAJECTORY_prefix_enumeration_or_rail_length_cap=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'V_n2.json').write_text(json.dumps(out,indent=2)+'\n');print('OldV n2/TOTAL3 author:15 heads;188 FORE input roles=>actual RAW2/3 horizons;128 joint losses->8;15 B+2 C+3 bud futures all cut by real C port/CU/endpoints.')
