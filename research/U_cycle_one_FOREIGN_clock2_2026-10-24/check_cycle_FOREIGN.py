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
Z={(1,0),(1,1),(2,0),(2,1)};STAR={(0,0),(0,1),(1,0),(1,1)};LEFT={(0,0),(0,1)};t=(1,2);s=(1,3);hole=(0,-1)
RR={A:[dict(slot=q,last_R_tick0=k,first=l.trace(W[A])['first'][q],EXIT_CORE=l.rot(sub(q,after(W[A])[:2]),-after(W[A])[2])in l.K)for q,(c,k)in l.trace(W[A])['last'].items()if c=='R']for A in'DCVU'}
# Portable physical deleted-hole no-FIRST-BLACK-cut beforeFOREIGNn<=2.
# All STAR andarm areCURRENT throughout the old8 source interval. Include
# CORE writes; a firstL writer needsBLACK at its previous actualCUT.
assert l.trace(W['U'])['last'][hole]==('L',3);hb=[];hk=[]
for n in range(3):
 h=(-n)%4
 for A in'DCVU':
  raw=l.trace(W[A]);ctx=l.trace(W[A]+l.M)
  for rr in RR[A]:
   q=tuple(rr['slot']);p=(*sub(hole,l.rot(q,h)),h);r=dict(actual_source_C_clock=n,earlier_RAW=A,ENTRY=p,physical_last_R=rr,RAW_EXIT=after(W[A],p))
   if(sum(p[:2])+h)%2:why='sector'
   elif raw['first'][q][0]=='L':why='prior_BLACK_cut_required_before_this_firstL'
   elif any((loc:=l.rot(sub(tag,p[:2]),-h))in ctx['first']or loc in l.K for tag in STAR|{t}):why='earlier_RAW_would_hit_independently_CURRENT_original_STAR_or_arm'
   else:
    hk.append(r)
    if n==0:assert p[1]<4;why='N0_head_below_actual_U_RAW_EXIT_y4'
    else:assert n==1 and p[1]<5;why='W1_head_below_first_W_stage_y5'
   r['route']=why;hb.append(r)
assert len(hb)==108
# Z same IDs CURRENT atFOREENTRY n<=2 by signed old8 directed firstbreak
# clock4. FORE TRUEinput cycle roles, with COMPLETE STAR+armMISS (not
# just TRUE input filtering), intactZ and preFORE budBLACK guards.
frows=[];fg=[]
for n in range(3):
 h=(-n)%4
 for tag in[(2,0),(2,1)]:
  for A in'FQB':
   ctx=l.trace(W[A]+l.M)
   for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
    p=(*sub(tag,l.rot(slot,h)),h);r=dict(true_preFOREIGN_SOURCE_ENTRY_C_age=n,FOREIGN=A,original_east_cycle_tag=tag,ENTRY=p,TRUE_input=slot,actual_input_owner=o.describe(A,ctx['first'][slot][1]))
    if(sum(p[:2])+h)%2:why='sector'
    elif any((loc:=l.rot(sub(q,p[:2]),-h))in ctx['first']or loc in l.K for q in STAR|{t}):why='forbidden_complete_STAR_or_arm_context_hit'
    else:
     bad=conflict(A,p,Z|{s})
     if bad:r['held_intact_Z_or_bud_ENTRY_CORE_FIRST_WHITE']=bad;why='CURRENT_Z_or_preFORE_bud_BLACK_conflict'
     else:
      fg.append(r)
      if n==0:assert p==(7,-1,0);why='FOREIGN_N0_head_y_minus1_below_U_EXIT_y4'
      elif n==1:assert p in[(4,1,3),(5,4,3)]and p[1]-p[0]<5;why='FOREIGN_W1_y_minus_x_below_first_W_bound5'
      else:
       assert n==2 and A=='B'and p==(0,-2,2);loc=l.rot(sub(hole,p[:2]),-2);f=ctx['first'][loc];assert loc==(0,-1)and f==('L',3);r['actual_SOURCE_deleted_WHITE_CORE_hole']=dict(cell=hole,local=loc,first=f,owner=o.describe('B',3));why='SOURCE_L3_deleted_hole_remains_physical_WHITE_at_FOREIGN_ENTRY_but_B_RAW_L3_CORE_needsBLACK'
    r['route']=why;frows.append(r)
assert len(frows)==282 and len(fg)==20 and Counter(r['true_preFOREIGN_SOURCE_ENTRY_C_age']for r in fg)=={0:6,1:12,2:2}
# Every future ordinary CURRENT Z firstloss before GLOBALfirst contact is
# a plainBASE TRUEinput, not an unexecuted full-familyCtail. C I0 has no
# silent outside-CORE capture. SAMELEFT is independent through earliercuts.
plain=[];right=[]
for tag in sorted(Z):
 for h in range(4):
  for A in'DVU':
   ctx=l.trace(W[A]+l.M)
   for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
    p=(*sub(tag,l.rot(slot,h)),h);r=dict(first_lost_original_Z_tag=tag,earlier_ordinary_RAW=A,ENTRY=p,input=slot,input_owner=o.describe(A,ctx['first'][slot][1]),RAW_EXIT=after(W[A],p))
    if(sum(p[:2])+h)%2:why='sector'
    elif bad:=conflict(A,p,Z):r['intact_Z_ENTRY_CORE_or_FIRST_WHITE']=bad;why='held_intact_Z_colour_orCORE_conflict'
    elif co:=contact(*chord('U',(0,0,0)),*chord(A,p)):r['actual_earlier_creator_U_contact']=co;why='earlier_creator_chord_contact_before_GLOBALtarget'
    elif any((loc:=l.rot(sub(q,p[:2]),-h))in ctx['first']or loc in l.K for q in LEFT):why='earlier_BASE_hits_independently_CURRENT_SAME_LEFT'
    else:
     assert A=='U'and p==(3,-1,0)and tuple(slot)in[(-1,1),(-1,2)];right.append(r);why='only_right_U3,minus1N_consumes_original_Epair_together'
    r['route']=why;plain.append(r)
assert len(plain)==128 and len(right)==2
# Literal old1902 protected bridge, valid source ownC-tail interfaces;
# adding one survivor-FOREIGN changes turn but not geometry. The source
# tail checks are fresh, no SOURCE labels are backdated before real birth.
P=(-1,7);E=(5,1);B=(5,-3);bridge=[E,(3,3),(1,1),(-1,3),P];edges=list(zip(bridge,bridge[1:]));assert z((3,-1,0))==B
half=(B,E);last=[]
for i,(u,v)in enumerate(edges):
 co=contact(u,v,*half);assert co=={'old_s':'0','new_t':'1'}if i==0 else co is None;last.append(co)
ct=[];cp=(0,4,0)
for i in range(2):
 aa=chord('C',cp);cases=[]
 for j,(u,v)in enumerate(edges):
  co=contact(u,v,*aa);assert co=={'old_s':'1','new_t':'0'}if i==0 and j==3 else co is None;cases.append(co)
 ct.append(dict(actual_source_C_tail_index1=i+1,ENTRY=cp,chord=aa,all_bridge_contacts=cases));cp=after(W['C'],cp)
oldclock=json.loads((R/'core_periodicity_new/U_renewal_exact_clock_frozen_20261023_1902/02_U_renewal_exact_clock.json').read_text());assert oldclock['bridge_doubled']==[list(p)for p in bridge]and oldclock['bridge_turns_in_pi_over_4']==[1,2,-2,-1]
assert sum(oldclock['bridge_turns_in_pi_over_4'])==0
clock=dict(SAME_current_bridge=bridge,physical_current_cells=[(2,1),(1,1),(0,1)],last_segment_is_actual_past_source_U_chord_not_a_historical_wire=True,actual_breaker_partial_chord=half,all4_partial_breaker_contacts=last,all2_actual_source_C_tail_bridge_interfaces=ct,source_FULL_C_clock_convention='TOTAL Cs count actual sourceU ENTRY inclusive, right consuming U ENTRY exclusive; sourceUC/UCC tails stay at their literal counts. No identity age or support ROOT corollary is lifted.',ordinary_zero_FOREIGN_turn_in_pi_over2='K',exact_ONE_FOREIGN_lift_in_pi_over2='K+2',bridge_join_sum_in_pi_over4=oldclock['bridge_turns_in_pi_over_4'],no_C_to_FOREIGN_wrap='The actual FIRST foreign follows plainV/U by signed complete8 adjacency; its previous atomic letter is notC.',Jordan_equation='(K+2)*pi/2 is plus_or_minus2pi; K>=0 forces K=2.',valid_geometry='GLOBALfirst stopping supplies a simple source-to-breaker-half path. OLD SAME Z and w avoid every earlier ordinary chord via current-edge barrier and actual FOREIGN pieces via survivor kinked barrier after proved completeFORE MISS. Source C tails and final consumer half are checked directly. Thus the old1902 bridge remains genuinely Jordan, not assumed permanently current after any retirement.',NO_upper_input_age_or_older_support_budget_lift=True)
# Target-independent corollary for the critical SOURCE d/arm pair loss.
# U2,0N atTOTAL2 requires old Ebottom2,0 in its actual ENTRYCORE. Thus a
# previous Z loss must already have happened; its RIGHT U3,-1N clock2
# RAW completes at3,3N. Any subsequent ordinary RAW reaching sameclock2
# is zeroN and cannot descend to2,0. No age law is assigned acrossFORE.
crit=(2,0,0);e0=(2,0);assert sub(e0,crit[:2])in l.K
assert tuple(right[0]['RAW_EXIT'])==(3,3,0)
critical=dict(actual_critical_N_RAW='U',ENTRY=crit,TOTAL_C_clock=2,original_Ebottom_required_ENTRY_CORE=dict(cell=e0,local=(0,0)),actual_previous_cycle_breaker='U3,-1,N',actual_previous_breaker_TOTAL_C_clock=2,actual_previous_breaker_RAW_EXIT=(3,3,0),zeroN_raw_endpoint_increments={A:after(W[A])[:2]for A in'DVU'},contradiction='All prior cycle loss before this ENTRY is the rightU atclock2, but after its actualRAWEXIT every zeroN base raisesy and never decreasesx, so cannot reach2,0. If its optionalC tail executes it already passesclock2. Original cycle current in U2,0 ENTRYCORE is impossible; thus this critical pair consumer has no actual prior history under the stated hypotheses.',no_unexecuted_breaker_C_tail_used=True)
# A structurally chosen genuine U-entry regression. Full prefix is legal,
# firstFOREIGN+firstD proxy is simple, and original Epair remains SAME.
word='UCCVDUUFD';raw=''.join(W[A]for A in word);tr=l.trace(raw+l.M);assert tr['feasible'];seed={q for q,(c,k)in tr['first'].items()if c=='L'};assert len(seed)==37
black=set(seed);ids={q:('entry',q)for q in seed};p=(0,0,0);reads=[];atcut=None
for tick,c in enumerate(raw+l.M):
 assert(p[:2]in black)==(c=='L');reads.append(dict(tick0=tick,read_number1=tick+1,cell=p[:2],turn=c,prior_identity=ids.get(p[:2])))
 if c=='L':black.remove(p[:2]);ids.pop(p[:2])
 else:black.add(p[:2]);ids[p[:2]]=('R',tick)
 p=after(c,p)
 if tick+1==len(raw):
  assert ids[(2,0)]==('R',8)and ids[(2,1)]==('R',7)and all(l.rot(sub(q,p[:2]),-p[2])not in l.K for q in[(2,0),(2,1)])
  atcut=dict(actual_RAW_EXIT=p,SAME_original_Epair_CURRENT={str(q):ids[q]for q in[(2,0),(2,1)]})
bad=l.trace(raw+W['U']+l.M);assert not bad['feasible']and bad['conflict_read']==232 and bad['previous_read']==8 and tuple(bad['cell'])==(2,0)
reg=dict(actual_genuine_U_entry_word=word,complete_black_seed=sorted(seed),all219_actual_RAW_plus_M11_fine_reads=reads,cut_before_attempted_next_U=atcut,attempted_next_U_actual_ENTRY=(2,-4,0),immutable_FIRST_WHITE_failure=bad,actual_failed_U_owner=o.describe('U',24),no_genuine_proxy_recontact_or_counterexample_claim=True)
D=[R/'core_periodicity_new/U_renewal_exact_clock_frozen_20261023_1902/manifest.json',R/'audits/check_U_renewal_exact_clock_independent.json',R/'core_periodicity_new/causal_cycle_renewal_20261023_1841/manifest.json',R/'audits/check_directed_U_cycle_renewal_independent.json',R/'old_U_all_tail_W_pair_hole_2026-10-24/manifest.json',R/'audits/check_old_U_all_tail_W_independent.json',R/'U_LEFT_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_LEFT_contact_or_persistence_independent.json',R/'core_periodicity_new/current_residual_barrier_frozen_20261023_1822/manifest.json',R/'audits/check_current_residual_barrier_independent.json',R/'seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json',R/'audits/check_foreign_kinked_barrier_turn_independent.json',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'U_arm_W_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_U_arm_W_guard_independent.json',R/'word_stabilization/U_foreign_prefix_bud_cuts_frozen_20261023_2201/manifest.json',R/'audits/check_U_foreign_prefix_buds_independent.json',R/'foreign_U_star_age2_2026-10-23/manifest.json',R/'audits/check_foreign_U_age2_and_marker_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py'];assert all(p.exists()for p in D),[str(p)for p in D if not p.exists()]
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual genuineU-family in old U-entryG8 before FIRSTFOREIGN at true creator age<=2, then ordinary-only suffix with actualcontexts. Under GLOBALfirst stopping / simple executed prefix and SAME LEFT, original four-edge cycle completely survives thatFOREIGN. Its first subsequent ordinary retirement strictly before the chosen GLOBAL target can ONLY be right plainRAWU3,-1N atTOTAL sourceC clock2. Critical U2,0N pair consumer atTOTAL2 impossible. Not arbitrary-tail simplicity, permanent cycles, birth budget or old upper-age/root corollary.',original_Z_same_IDs=sorted(Z),actual_SOURCE_U_L3_deleted_physical_hole=hole,all108_pre_FOREIGN_physical_CORE_inclusive_first_BLACK_cut_origins=hb,all282_early_FOREIGN_cycle_Einput_roles=frows,all20_surviving_early_FOREIGN_gate_rows_and_endpoint_or_CORE_cuts=fg,complete_early_FOREIGN_cycle_MISS='West cycle IDs are STAR and already completeFORE MISS. If an east ID is touched, CURRENT excludesENTRYCORE/firstWHITE, while all actual TRUEinputs are enumerated282, leaving only N/W unreachable or B0,-2S requiring actual SOURCEdeleted WHITE CORE hole. Includesmarker-only absorption; no fine-time or future-marker execution claim.',all128_plain_ordinary_cycle_first_CURRENT_loss_roles=plain,only2_right_U_INPUT_rows=right,one_FOREIGN_exact_clock2_current_bridge=clock,critical_N2_pair_consumer_exclusion=critical,actual37_cell_genuine_U_entry_cycle_survival_regression=reg,strict_limits=['TRUE preFOREIGN age<=2 only for complete cycleFOREMISS','no old8 firstbreak rule blindly crossesFORE; plainRAW128 rebuilt independently','CURRENT LEFT is independent through strictly earlier loss cuts; allowed consumption during chosen GLOBAL target is not excluded by this lemma','SOURCE ownC tails preserve actual sameZ/w labels, no ghost current edges','FOREIGN itself is not assigned a producer age','no postFOREIGN upper-minimum or older-support/root funding corollary','no permanent-cycle fuel or arbitrary-tail/simple/secondFOREIGN theorem'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'cycle_FOREIGN.json').write_text(json.dumps(out,indent=2)+'\n');print('EarlyFOREcycleMISS:108 physicalhole+282FORE roles. PostFORE128 plain firstloss only rightU3,-1; currentbridge totalturnK+2→K2. U2,0N pair consumer impossible before GLOBALtarget.')
