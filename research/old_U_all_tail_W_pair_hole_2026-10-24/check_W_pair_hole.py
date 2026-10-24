"""Fresh C coupled reserve; outgoing first post-Q/B D/C first-contact closure.
No terminal DCC parsing assumption. Every clock below is actual ordinary C.
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
STAR={(0,0),(0,1),(1,0),(1,1)};LEFT={(0,0),(0,1)};d=(1,1);t=(1,2);s=(1,3);PAIR={d,t};g=(0,2)
# Portable source-arm COMPLETE firstFOREIGN-MISS through true age3.
# Signed276 gives actual armCURRENT at FOREENTRY. Complete STAR-MISS
# follows signed first-effect>=5. Every actual armTRUEinput is aligned.
forearm=[];armkeep=[]
for n in range(4):
 h=(-n)%4
 for A in'FQB':
  ctx=l.trace(W[A]+l.M)
  for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
   p=(*sub(t,l.rot(slot,h)),h);r=dict(FOREIGN=A,true_preFOREIGN_source_ENTRY_C_age=n,ENTRY=p,arm_true_input=slot,owner=o.describe(A,ctx['first'][slot][1]))
   if(sum(p[:2])+h)%2:why='sector'
   elif any((loc:=l.rot(sub(q,p[:2]),-h))in ctx['first']or loc in l.K for q in STAR):why='forbidden_complete_original_STAR_context_hit_at_age_le3'
   else:
    armkeep.append(r)
    if n==0:
     assert(A,p)in[('F',(4,4,0)),('Q',(4,6,0)),('B',(3,7,0))]
     if A in'FQ':assert p[1]-p[0]<4;why='zeroN_after_creatorU_has_y_minus_x_ge4'
     else:why='zeroN_equations_force_only_DDD_beforeB_forbidden_actual_D_to_FOREIGN_pair'
    elif n==1:
     assert p==(2,7,3)and p[1]-p[0]==5;why='first_W_y_minus_x_ge5_then_nonempty_W_base_run_adds_at_least2'
    else:
     assert(n==2 and p in[(-3,5,2),(0,4,2)])or(n==3 and A=='B'and p==(3,0,1))
     loc=l.rot(sub(s,p[:2]),-h);f=ctx['first'][loc];assert f[0]=='R'and f[1]<len(W[A]);r['genuine_preFOREIGN_bud_WHITE_contradiction']=dict(cell=s,local=loc,first=f,owner=o.describe(A,f[1]));why='genuine_source_bud_CURRENT_through3_conflicts_with_FOREIGN_own_first_WHITE'
   r['route']=why;forearm.append(r)
assert len(forearm)==188 and len(armkeep)==13
assert Counter(r['true_preFOREIGN_source_ENTRY_C_age']for r in armkeep)=={0:3,1:3,2:6,3:1}
# Rational outgoing-old-owned W geometry. TotalK3 forced by all-tail angle.
from math import ceil,floor
angles=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows'];geo=[]
a,b=chord('U',(0,0,0));u=sub(b,a)
for A in'DCVU':
 ar=next(r for r in angles if r['source_class']=='preFOREIGN_ordinary'and r['source_atom']=='U'and r['contact_atom']==A);assert[k for k in ar['allowed_C_counts_before_contact_ENTRY']if(2-k)%4==3]==[3]
 c,e=chord(A,(0,0,3));v=sub(e,c);de=det(u,v);assert de
 corners=[tuple(F(a[k]+ss*u[k]-c[k]-tt*v[k],2)for k in(0,1))for ss in(0,1)for tt in(0,1)]
 for x in range(ceil(min(p[0]for p in corners)),floor(max(p[0]for p in corners))+1):
  for y in range(ceil(min(p[1]for p in corners)),floor(max(p[1]for p in corners))+1):
   if(x+y+3)%2:continue
   q=sub(add(c,(2*x,2*y)),a);ss,tt=F(det(q,v),de),F(det(q,u),de)
   if not(0<=ss<1 and 0<tt<=1):continue
   p=(x,y,3);bad=conflict(A,p,LEFT);geo.append(dict(actor=A,ENTRY=p,total_source_C_clock=3,old_source_parameter=str(ss),new_positive_parameter=str(tt),SAME_LEFT_contradictions=bad))
assert len(geo)==18;leftkeep=[r for r in geo if not r['SAME_LEFT_contradictions']];assert len(leftkeep)==6 and all(r['ENTRY'][1]<=3 for r in leftkeep)
# Earliest CURRENT-loss of original d/arm pair before W3 entry. LEFT is
# independent at EVERY earlier cut; TRUE anchor inputs are not intrinsic
# colour conflicts but cause CURRENT loss by actual writerEXIT.
loss=[];pending=[]
for tag in sorted(PAIR):
 other=next(iter(PAIR-{tag}))
 for h in range(4):
  for A in'DVU':
   ctx=l.trace(W[A]+l.M)
   for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
    p=(*sub(tag,l.rot(slot,h)),h);ep=after(W[A],p);r=dict(SAME_first_lost_pair_tag=tag,other_pair_tag=other,consumer=A,ENTRY=p,input=slot,actual_input_owner=o.describe(A,ctx['first'][slot][1]),RAW_EXIT=ep)
    if(sum(p[:2])+h)%2:why='sector'
    elif(co:=contact(*chord('U',(0,0,0)),*chord(A,p))):r['actual_earlier_old_U_contact']=co;why='earlier_actual_creator_chord_contact_before_global_target'
    elif any((loc:=l.rot(sub(q,p[:2]),-h))in ctx['first']or loc in l.K for q in LEFT):why='earlier_consumer_touches_independently_CURRENT_LEFT_at_ENTRY_and_RAW_EXIT'
    else:
     bad=conflict(A,p,{other})
     if bad:r['other_pair_still_CURRENT_entry_colour_guard']=bad;why='other_held_pair_tag_ENTRY_CORE_or_first_WHITE'
     else:
      pending.append(r)
      if h==0:
       assert A=='U'and p==(2,0,0)and ep==(2,4,0)and{tuple(q)for q in PAIR}<={add(p[:2],q)for q in map(tuple,l.literal_geometry(W[A])['inputs'])};why='simultaneous_pair_loss_N2_RAW_exit_y4_then_required_C_W_y_ge5_above_target_y_le3'
      else:
       assert h==2 and tag==t and(A,p)in[('D',(1,3,2)),('V',(1,5,2)),('U',(0,6,2))]and ep==(0,2,2);why='S_heading_forces_totalK0_but_exact_current_edge_Jordan_loop_has_turn0'
    r['route']=why;loss.append(r)
assert len(loss)==64 and len(pending)==5
# The S first-arm-loss closing bridge uses SAME genuine cells w,d,t.
# Their permanence starts only after sourceU RAW. Clip its geometric chord
# at W=(-1,3); direct source-partial and consuming-RAW intersections are
# independently literal, not a backdated current-edge barrier.
bridge=[(1,5),(3,3),(1,1),(-1,3)];bridgecells=[t,d,(0,1)];sourcepart=((-1,3),(-1,7));bridgecheck=[]
for i,(v0,v1)in enumerate(zip(bridge,bridge[1:])):
 co=contact(v0,v1,*sourcepart)
 assert co=={'old_s':'1','new_t':'0'}if i==2 else co is None
 bridgecheck.append(dict(actual_SAME_cell=bridgecells[i],current_edge=(v0,v1),source_partial_contact=co))
jordan=[];alpha={'D':(1,0),'V':(0,1),'U':(2,0)}
for r in pending:
 if r['ENTRY'][2]!=2:continue
 A=r['consumer'];p=tuple(r['ENTRY']);ep=tuple(r['RAW_EXIT']);ctx=l.trace(W[A]+l.M);loc=l.rot(sub(t,p[:2]),-2);assert ctx['first'][loc][1]==len(W[A])+1 and loc not in l.trace(W[A])['first'];assert l.rot(sub(t,ep[:2]),-2)in l.K
 allco=[]
 for i,(v0,v1)in enumerate(zip(bridge,bridge[1:])):
  co=contact(v0,v1,*chord(A,p));assert co=={'old_s':'0','new_t':'1'}if i==0 else co is None;allco.append(co)
 ac,at=alpha[A];open0=(2+ac,at);close=(3-ac-2-2-1,-at);assert(open0[0]+close[0],open0[1]+close[1])==(0,0)
 jordan.append(dict(actual_consumer=r,SAME_arm_unread_through_its_RAW_then_alive_CORE_at_EXIT=True,all3_bridge_consumer_chord_contacts=allco,source_half_chord_start=(-1,3),actual_loss_RAW_EXIT_center=z(ep),bridge=bridge,symbolic_angle_unit='coefficient_pair(pi/4,atan3)',one_FOREIGN_open_turn_at_totalK0=open0,actual_principal_bridge_join_sum=close,closed_total_turn=(0,0),Jordan_requires_plus_or_minus2pi=True,pre_FOREIGN_C_wrap_impossible_since_totalK0=True,independent_current_d_lock_during_S='S d loss has only sector/LEFT conflicts in all64 table, so d staysCURRENT before firstarmS loss; w is independentLEFT. Source t/d/w completeFOREIGN MISS is exact.',current_edge_barrier_scope='Ordinary current-edge barrier and actual kinkedFOREIGN survivor barrier apply after creatingU RAW. Source clipped leg and final consumer RAW are checked directly; no edge was assumed CURRENT before its real R birth.'))
assert len(jordan)==3
# Current d/t at W3 ENTRY cuts five; the sixth TRUE arm input is retained
# as a genuine possible contact role until the independent hole guard.
paircuts=[];live=[]
for r in leftkeep:
 bad=conflict(r['actor'],tuple(r['ENTRY']),PAIR)
 if bad:paircuts.append(dict(geometry=r,pair_CURRENT_at_ENTRY_contradictions=bad))
 else:live.append(r)
assert len(paircuts)==5 and len(live)==1 and live[0]['actor']=='U'and live[0]['ENTRY']==(2,3,3)
# Final lower-q source hole. Earliest RAW-END BLACK cut, CORE included.
# g=(0,2) was genuinely erased by source U ownL20; target ownL13 requires
# BLACK already atENTRY. Pair/LEFT anchors are independent untilENTRY.
assert l.trace(W['U'])['last'][g]==('L',20);assert l.rot(sub(g,(2,3)),-3)==(-1,2);assert l.trace(W['U']+l.M)['first'][(-1,2)]==('L',13)
HOLD=LEFT|PAIR;RR={A:[dict(slot=q,last_R_tick0=tm,last_R_read1=tm+1,first= l.trace(W[A])['first'][q],EXIT_CORE=l.rot(sub(q,after(W[A])[:2]),-after(W[A])[2])in l.K)for q,(c,tm)in l.trace(W[A])['last'].items()if c=='R']for A in'DCVUFQB'}
reb=[];rk={h:[]for h in range(4)}
for h in range(4):
 for A in'DCVU':
  raw=l.trace(W[A]);ctx=l.trace(W[A]+l.M)
  for rr in RR[A]:
   q=tuple(rr['slot']);p=(*sub(g,l.rot(q,h)),h);ep=after(W[A],p);r=dict(earlier_writer=A,ENTRY=p,physical_final_R=rr,RAW_EXIT=ep)
   if(sum(p[:2])+h)%2:why='sector'
   elif raw['first'][q][0]=='L':why='first_hole_L_requires_earlier_BLACK_cut'
   elif any((loc:=l.rot(sub(q0,p[:2]),-h))in ctx['first']or loc in l.K for q0 in HOLD):why='earlier_writer_hits_independently_CURRENT_LEFT_or_pair'
   else:why='necessary_physical_first_BLACK_origin';rk[h].append(r)
   r['route']=why;reb.append(r)
assert len(reb)==144 and not rk[2]and not rk[3]and len(rk[0])==4 and len(rk[1])==3
pre=[];post=[]
for h in range(4):
 for r in rk[h]:
  A=r['earlier_writer'];p=tuple(r['ENTRY']);ep=tuple(r['RAW_EXIT']);x=dict(necessary_origin=r)
  if h==0:assert p==(-2,2,0);x['pre_FOREIGN_route']='N0_head_y2_below_source_U_EXIT_y4'
  else:
   assert h==1
   if A=='C':x['pre_FOREIGN_route']='E3_C_completes4_after_FOREIGN_clock_le3'
   else:
    assert A=='U'and p==(-1,4,1);loc=l.rot(sub(s,p[:2]),-1);f=l.trace(W[A]+l.M)['first'][loc];assert f==('R',17);x.update(pre_FOREIGN_route='old_source_bud_CURRENT_through3_conflicts_with_pre_FOREIGN_U_own_R17',actual_old_bud_WHITE=dict(cell=s,local=loc,first=f))
  pre.append(x)
  y=dict(necessary_origin=r)
  if h==0:
   if A=='C':assert ep==(-2,3,3);y['post_FOREIGN_route']='N2_C_completesW3_left_of_target_x2_and_zeroW_cannot_move_right'
   else:assert ep[1]>=3;y['post_FOREIGN_route']='N2_BASE_RAW_exit_y_ge3_then_required_C_W_y_ge4_above_target3'
  elif A=='C':assert ep[2]==0 and ep[1]>=3;y['post_FOREIGN_route']='E1_C_entersN2_y_ge3_then_required_C_W_y_ge4_above_target3'
  else:
   assert A=='U'and p==(-1,4,1)
   newstar={add(p[:2],l.rot(q,1))for q in STAR};cuts=[];tar=(2,3,3);ct=l.trace(W['U']+l.M)
   for q in sorted(newstar):
    loc=l.rot(sub(q,tar[:2]),-3)
    if list(loc)in l.literal_geometry(W['U'])['inputs']:cuts.append(dict(genuine_new_U_star=q,target_TRUE_input=loc,actual_target_owner=o.describe('U',ct['first'][loc][1])))
   assert{tuple(r['genuine_new_U_star'])for r in cuts}=={(0,3),(-1,3)}
   y.update(post_FOREIGN_route='genuine_fresh_E_U_donor_creates_permanent_ordinary_RAW_star_consumed_by_target_TRUE_inputs',all4_genuinely_new_R_born_star_cells=sorted(newstar),actual_target_input_conflicts=cuts,no_original_bud_persistence_after_FOREIGN_used=True)
  post.append(y)
# Physical final-R FOREIGN origins for g under already proved complete
# STAR+arm MISS; bud is current only atFOREENTRY and is filtered solely by
# ENTRYCORE/firstWHITE, not by its permitted true BLACK input.
frr=[];fkeep=[]
for n in range(4):
 h=(-n)%4
 for A in'FQB':
  raw=l.trace(W[A]);ctx=l.trace(W[A]+l.M)
  for rr in RR[A]:
   q=tuple(rr['slot']);p=(*sub(g,l.rot(q,h)),h);ep=after(W[A],p);r=dict(FOREIGN=A,true_pre_FOREIGN_n=n,ENTRY=p,physical_final_R=rr,RAW_EXIT=ep)
   if(sum(p[:2])+h)%2:why='sector'
   elif raw['first'][q][0]=='L':why='first_hole_L_requires_pre_FOREIGN_BLACK_cut_already_excluded'
   elif any((loc:=l.rot(sub(q0,p[:2]),-h))in ctx['first']or loc in l.K for q0 in STAR|{t}):why='forbidden_complete_STAR_or_arm_context_hit'
   else:
    loc=l.rot(sub(s,p[:2]),-h);f=ctx['first'].get(loc)
    if loc in l.K or f and f[0]=='R':why='genuine_pre_FOREIGN_bud_ENTRY_CORE_or_first_WHITE'
    else:
     fkeep.append(r)
     if n==0:assert p==(-2,2,0);why='N0_foreign_head_y2_below_source_U_EXIT_y4'
     else:assert n==3 and p==(-2,3,1)and ep[2]==3 and ep[0]<2 and ep[1]>3;why='W3_FOREIGN_EXIT_left_and_above_target2,3_no_zeroW_return'
   r['route']=why;frr.append(r)
assert len(frr)==292 and len(fkeep)==6
D=[R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'U_LEFT_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_LEFT_contact_or_persistence_independent.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',R/'audits/check_foreign_U_raw_ages34_independent.json',R/'foreign_U_star_age2_2026-10-23/manifest.json',R/'foreign_U_marker_clocks_2026-10-23/manifest.json',R/'audits/check_foreign_U_age2_and_marker_independent.json',R/'U_arm_W_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_U_arm_W_guard_independent.json',R/'word_stabilization/U_foreign_prefix_bud_cuts_frozen_20261023_2201/manifest.json',R/'audits/check_U_foreign_prefix_buds_independent.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/U_star_RAW_lift_manifest.json',R/'audits/check_fresh_U_star_RAW_lift_independent.json',R/'core_periodicity_new/current_residual_barrier_frozen_20261023_1822/manifest.json',R/'audits/check_current_residual_barrier_independent.json',R/'seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json',R/'audits/check_foreign_kinked_barrier_turn_independent.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'audits/check_complete8_foreign_adjacency_independent.json',R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in D)
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual preFOREIGN genuineU/UC/UCC creator in U-entryG8, FIRSTF/Q/B, arbitrary ordinary-only RAW suffix plus actualfinalM11. At GLOBAL first contact old-owned by creatingU outgoing chord, no W-facing actor is possible. TotalordinaryC3 only; otherheadings/sourcefamilies/arbitrarytail simplicity remain separate.',source_tags=dict(SAME_original_LEFT=sorted(LEFT),SAME_original_topright_d=d,SAME_original_arm_t=t,genuine_pre_FOREIGN_bud=s,source_L20_deleted_physical_hole=g),all188_FOREIGN_arm_input_roles=forearm,all13_arm_foreign_RETIREMENT_candidates_and_exact_endpoint_or_bud_cuts=armkeep,portable_foreign_arm_MISS='At every actual true sourceENTRY-age<=3 complete8-toFIRSTFOREIGN boundary, original arm isCURRENT by signed276. CompleteSTAR MISS at<=3 plus all188 actual arm TRUEinputs eliminate any FORE context hit. ENTRYCORE/firstWHITE are already incompatible with armCURRENT. Thus COMPLETE FORE RAW+M11 MISSES SAME arm, not merely RAW.',all18_exact_outgoing_owned_W_geometries=geo,all64_earlier_first_PAIR_CURRENT_loss_roles=loss,all3_actual_current_edge_S_arm_loss_Jordan_interfaces=jordan,current_bridge_SOURCE_partial_checks=bridgecheck,PAIR_entry_guard='For each of six LEFT-compatible W3 heads y<=3, SAME d andarm remainCURRENT atENTRY. Any earlier firstpair loss has exact64-role cover. S arm-loss requiresK0 but the actual simple current-edge loop turns0; E none; N only simultaneousU2,0 exitsy4 then requiredC producesW>=5; W earlierloss alreadycontacts oldU or requiresotherheldtagWHITE. LEFT inputs treated only via independent CURRENT at earlierCUT, not intrinsic color.',all5_PAIR_CURRENT_direct_W_target_cuts=paircuts,sole_PAIR_compatible_target_before_hole_guard=live[0],all144_CORE_inclusive_ordinary_first_BLACK_cut_hole_origins=reb,all7_pre_FOREIGN_hole_origin_cuts=pre,all7_post_FOREIGN_hole_origin_cuts=post,all292_CORE_inclusive_FOREIGN_hole_R_origins=frr,all6_surviving_FOREIGN_hole_origins_and_endpoint_cuts=fkeep,earliest_BLACK_cut_scope='SourceU actualL20 leavesgWHITE atRAWexit. Choose earliest subsequent actual RAW-END BLACK cut includingCORE. Unread or firstL requires an earlierBLACKcut. Earlierwriters hitting independent CURRENT LEFT+pair are excluded by literal color/entryCORE or actual CURRENTloss atRAWEXIT; marker-onlyaliveCORE capture is not physical death. All remaining funders have exact endpoint cuts or genuine NEW U-star future TRUEinput contradiction. No physical intermediate WHITE seal is claimed.',Jordan_scope='Bridge contains SAME genuine w,d,arm current edges. Their pre-source birth time is NOT backdated: source clipped geometric leg is checked directly; only after sourceRAW does the signed ordinary/current-survivor foreign barrier apply. Direct lossBASE chord intersections show only final endpoint. FirstFORE has repaired actualQ/B fine kink; totalK0 has no C-toFORE wrap. Global-first stopping supplies simple source-to-loss path, so turn0 contradicts Jordan.',no_old_bud_or_age_law_transported_across_FOREIGN=True,no_fixed_atom_index_or_zero_rail_cap=True,conclusion='All-tail oldU W3 source family closes:18 geometry=12LEFT+5pairedreserve+1 physicalhole/freshdonor ancestry. Other sourceheadings remain separate.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'W_pair_hole.json').write_text(json.dumps(out,indent=2)+'\n');print('OldU all-tail W3:188FORE-arm MISS,64pair losses with3current-edge Jordan loops,18geometry→12LEFT+5pair+1physicalhole. Hole144ordinary+292FORE origins; freshUdonor star blocks finalcase.')
