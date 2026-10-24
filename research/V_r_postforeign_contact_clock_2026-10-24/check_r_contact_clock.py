"""One-foreign r-loss clock, and a THIRD old-U/S-facing-V funnel.
Only physical held-edge geometry after A; no postforeign input-age law.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def raw(tokens):return ''.join(W[a]for a in tokens)
def after(word,p=(0,0,0)):
 pos,h=p[:2],p[2]
 for c in word:h=(h+(1 if c=='R'else-1))%4;pos=add(pos,l.DIRS[h])
 return*pos,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
# Reuse signed finite ordinary r-first-loss geometry, not a postA age law.
SP=R/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/V_parallel_reproductive_supply.json';sj=json.loads(SP.read_text());gates=sj['r_retirement_cases'];assert len(gates)==9
G=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];byid={0:'D',4:'V',7:'U'};clock_rows=[]
# In units pi/4 and beta=atan(1/3), aV=beta, aD=1, aU=0.
# T_open=(K+2)pi/2+aV-aH; closure=aH-aV-pi/2.
for g in gates:
 source=G[g['source']]['name'];consumer=byid[g['consumer']];pose=tuple(g['head']);assert pose in((1,0,3),(3,0,3),(4,1,3))and after(W[consumer],pose)==(0,1,3)
 local=l.rot(sub((0,0),pose[:2]),-pose[2]);tr=l.trace(W[consumer]+l.M);assert tr['first'][local][0]=='L';assert tr['first'][local][1]>=len(W[consumer])
 # Each actual consuming RAW misses r physically; ordered loss is exitCORE.
 assert local not in l.trace(W[consumer])['first']; assert (0,0) in {add((0,1),l.rot(q,3))for q in l.K}
 aa={'D':(1,0),'V':(0,1),'U':(0,0)}[consumer];open_offset=(4-aa[0],1-aa[1]);closing=(aa[0]-2,aa[1]-1);assert tuple(open_offset[k]+closing[k]for k in(0,1))==(2,0)
 clock_rows.append(dict(actual_old_source_full=source,first_loss_ordinary_RAW=consumer,ordinary_pose_relative_source=pose,consumer_actual_RAW_exit=(0,1,3),same_r_local=local,actual_first_r_physical_read=o.describe(consumer,tr['first'][local][1]),same_original_alive_CORE_at_consumer_RAW_exit=True,open_turn_pi_over4_beta_coefficients={'K_coefficient':[2,0],'constant':open_offset},held_r_bridge_closing_turn_coefficients=closing,total_closed_turn_coefficients={'K_coefficient':[2,0],'constant':[2,0]},Jordan_total_K_equation='K+1=4 or -4',only_nonnegative_K_solution=3))
assert len(clock_rows)==9
# Source-creator/actual-next-base funnel at old U contactV(0,4,S).
target=(0,4,2);targetK={add(target[:2],l.rot(q,target[2]))for q in l.K};targetZ=z(target);assert targetZ==(1,9)
funnel=[]
for full in('UC','UCC'):
 C1exit=after(raw('UC'));assert z(C1exit)==targetZ
 funnel.append(dict(actual_creating_full=full,classification='candidate_ENTRY_repeats_actual_creator_C1_EXIT',genuine_actual_C1_exit=C1exit,corrected_repeated_vertex=targetZ))
next_rows=[]
for full in('D','DC','V','VC','VCC','U','UC','UCC'):
 base=full[0];entry=(0,4,0);entryclock=0
 if base=='D':
  ep=after(W['D'],entry);assert z(ep)==targetZ;why='candidate_ENTRY_repeats_actual_next_D_BASE_EXIT';tags=[]
 elif base=='U':
  tags=[add(entry[:2],q)for q in((0,0),(0,1))];assert set(tags)<=targetK;why='actual_next_U_SAME_LEFT_CURRENT_in_candidate_ENTRY_core'
 else:tags=[(0,4)];why='necessary_genuine_first_V_family_source'
 next_rows.append(dict(actual_next_full_after_plain_creator_U=full,actual_entry=entry,actual_ENTRY_clock=entryclock,completion_clock=full.count('C'),classification=why,guarding_SAME_original_tags=tags))
assert[rr['actual_next_full_after_plain_creator_U']for rr in next_rows if rr['classification']=='necessary_genuine_first_V_family_source']==['V','VC','VCC']
# All possible true-n3/4 inverse interfaces for targetV0,4S.
interfaces=[];phase=[]
for b1,b2 in product('DCVU',repeat=2):
 post=int(b1=='C')+int(b2=='C');n=4-post
 if n not in(3,4):continue
 for A in'FQB':
  hA=(-n)%4;delta=after(raw(A+b1+b2),(0,0,hA));pa=(target[0]-delta[0],target[1]-delta[1],hA);tr=l.trace(W[A]+l.M);loc=l.rot(sub((0,4),pa[:2]),-pa[2]);assert loc not in tr['first']
  row=dict(foreign=A,first=b1,second=b2,third='V',third_pose=target,true_creator_and_first_V_ENTRY_to_FOREIGN_C_age=n,total_C_before_third_ENTRY=4,foreign_pose=pa,genuine_first_V_r_cell=(0,4),r_foreign_local=loc,FOREIGN_complete_RAW_plus_actual_M11_MISSES_r=True)
  if n==4:row['r_loss_obstruction']='Any postA first CURRENT loss has K3, but source-toA clock4 already exceeds3.'
  elif b1=='C':row['r_loss_obstruction']='First postA atomC has no inputs and preserves r; every later ordinary entry has K4, not required3.'
  else:
   assert b2=='C';endA=after(W[A],pa);Hend=after(W[b1],endA);assert Hend==(1,4,3)
   row.update(r_loss_obstruction='Only b1 is before the sole postA C at K3; all possible r loss consumers exit(0,5,W), but actual b1 exit is(1,4,W).',actual_b1_exit=Hend,all_possible_r_loss_exit=(0,5,3))
  suffix=l.trace(raw(A+b1+b2+'V')+l.M);row['complete_local_suffix_feasible']=suffix['feasible'];row['local_conflict']=None if suffix['feasible']else suffix;interfaces.append(row)
assert len(interfaces)==45
assert sum(r['true_creator_and_first_V_ENTRY_to_FOREIGN_C_age']==3 for r in interfaces)==18
assert sum(r['true_creator_and_first_V_ENTRY_to_FOREIGN_C_age']==4 for r in interfaces)==27
assert sum(r['complete_local_suffix_feasible']for r in interfaces)==42
# Every remaining firstV source r is current at preA age3/4 by OLD law5;
# afterA currentness is deduced only via held-edge clock and exact exits.
source_first_V=[]
for full in('V','VC','VCC'):
 tr=l.trace(raw(full));assert tr['last'][(0,0)]==('R',4)
 source_first_V.append(dict(actual_first_V_full=full,entry=(0,4,0),ENTRY_clock=0,source_local_r=(0,0),SAME_r_global=(0,4),birth_tick0_within_source_full=4,birth_read_number1=5,own_C_tails_preserve_same_r=True,preFOREIGN_OLD_minimum_first_loss=5,preFOREIGN_age_only=[3,4],no_postFOREIGN_minimum5_claim=True))
paths=[SP,R/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',R/'audits/check_V_parallel_reproductive_supply_independent.json',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json',R/'U_LEFT_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_LEFT_contact_or_persistence_independent.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',R/'foreign_U_star_age2_2026-10-23/manifest.json',R/'foreign_U_marker_clocks_2026-10-23/manifest.json',R/'audits/check_foreign_U_age2_and_marker_independent.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'audits/check_U_left_star_permanence_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_ONE_FOREIGN_V_R_CLOCK_AND_OLD_U_THIRD_S_V_FUNNEL_PENDING_REVIEW',portable_lemma_scope='A genuine PREforeign V/VC/VCC original r is SAME CURRENT at entry of FIRSTforeign and the complete foreign context MISSES r. Along a subsequent ordinary tail that is simple through the first r CURRENT-loss atom, that loss has exact TOTAL source-V-entry-inclusive/consumer-entry-exclusive C count K3. This is a geometric conditional clock, not an input-age theorem after foreign.',all9_actual_source_tail_and_plain_ordinary_r_first_loss_interfaces=clock_rows,held_bridge_geometry='Normalize oldV0N: SAME physical r edge joins sourceV entryE0(-1,-1) to consumer RAW exitL0(1,1). Actual source V/C tails meet it only atE0; actual consuming D/V/U chord only atL0. Earlier ordinary and repaired foreign pieces avoid it while original r is held current. Simple proxy subarc plus that same edge is Jordan; no historical wire.',turn_lift='Signed old2036 closure is aH-aV-pi/2. Signed94 one-first-foreign open lift is(K+2)pi/2+aV-aH. Sum(K+1)pi/2, so Jordan givesK3 or-5; only3 is nonnegative. The actual preFOREIGN complete8->A predecessor is non-C, retaining the signed wrap exclusion.',portable_contact_or_persistence_corollary='If true source-toFOREIGN age>=4, the SAME r is CURRENT before A and A MISSES it, then any first later r CURRENT loss forces an earlier/new proxy contact by completion of its loss atom. At ENTRY of a global first-contact atom r is still CURRENT; nothing asserted through that contact.',third_old_U_V_S_application_scope='Only THIRD ordinary targetV(0,4,S), global FIRST new contact owned by an old creatingU0N chord, true preFOREIGN n3/4 and totalC beforethird4. No other old-U target or full third simplicity.',creator_own_tail_funnel=funnel,all8_actual_next_full_base_funnel_cases=next_rows,all3_genuine_remaining_first_V_full_sources=source_first_V,all45_actual_FOREIGN_b1_b2_inverse_interfaces=interfaces,conclusion='All45 old-U n3/4 thirdV0,4S interfaces are excluded:3 localCU conflicts and42 genuine firstV-r guards. Creator UC/UCC and nextD repeat an old vertex before candidate; nextU SAME LEFT hits candidateK; only actual nextV remains. Each foreign MISSES its original r. At n4 the portable K3 loss is already too early; at n3 the only possible preC ordinary has a wrong EXIT. Therefore SAME r remains current at third entry, but r=(0,4) is in the actual thirdV entryK.',no_altered_first_V_cohort_or_q_shadow_persistence_assumed_after_FOREIGN=True,no_arbitrary_tail_simplicity_or_other_third_U_source_pose_closure=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'r_contact_clock.json').write_text(json.dumps(out,indent=2)+'\n');print('Portable one-FOREIGN V-r first-loss clockK3, not maturity;45 inverse thirdV0,4S cases allFOREIGN-r-MISS, with full creator/next-base funnel and exact wrongEXIT atn3.')
