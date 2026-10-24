from pathlib import Path
import json,hashlib
from collections import Counter
S=Path(__file__).resolve();R=S.parents[1];D=R/'old_U_all_tail_S_D_coupled_reserve_2026-10-24'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'manifest.json')=='b224a727a36249ba2a52d77316613720fc6279ec16b10b82b954928e6d8308b5'
for f,h in json.loads((D/'manifest.json').read_text())['files'].items():assert sha(D/f)==h
ref=json.loads((D/'S_D.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')]
raw={a:tr(W[a])for a in W};ctx={a:tr(W[a]+M)for a in W}
I={a:{q for q,b in ctx[a]['req'].items()if b and q not in K}for a in W}
assert {a:len(I[a])for a in'DCVUFQB'}==dict(D=1,C=0,V=2,U=5,F=14,Q=15,B=18)
STAR={0j,1j,1,1+1j};LEFT={0j,1j};d=1+1j;arm=1+2j;bud=1+3j;RES={d,arm,bud};target=2j;th=2
local=lambda q,p,h:(q-p)/rot(h)
hit=lambda a,q,p,h:local(q,p,h)in K or local(q,p,h)in ctx[a]['req']
bad=lambda a,q,p,h:local(q,p,h)in K or ctx[a]['req'].get(local(q,p,h))is False
exit=lambda a,p,h:(p+rot(h)*raw[a]['p'],(h+raw[a]['h'])%4)
pose=lambda p,h:tuple(xy(p)+[h])
sector=lambda p,h:(int(p.real+p.imag)+h)%2

def compare(rows,key,ours,extra=()):
 got={key(r):r for r in rows};assert set(got)==set(ours),(len(got),len(ours),set(got)^set(ours))
 for k,v in ours.items():assert got[k]['route']==v,(k,got[k]['route'],v)
 return dict(Counter(ours.values()))
# Current external identities cannot disappear except at a true context input.
# Any apparent EXIT-CORE capture must be a required BLACK input or already
# require WHITE. Check every external EXIT-CORE site from literal words.
corechecks=[]
for a in W:
 z=raw[a];ek={z['p']+rot(z['h'])*q for q in K}
 for q in ek-K:
  assert q in ctx[a]['req']
  assert (ctx[a]['req'][q] and q in I[a]) or not ctx[a]['req'][q]
  corechecks.append((a,xy(q),ctx[a]['req'][q]))
for q in {raw['C']['p']+rot(raw['C']['h'])*k for k in K}-K:
 assert ctx['C']['req'].get(q) is False
births=[]
for word in ('U','UC','UCC'):
 z=tr(''.join(W[a]for a in word));ek={z['p']+rot(z['h'])*k for k in K}
 for q in RES:assert z['last'][q]==raw['U']['last'][q] and z['last'][q][0]=='R' and q not in ek
 births.append((word,[(xy(q),z['last'][q])for q in sorted(RES,key=lambda q:(q.real,q.imag))]))
pre={}
for a in'DVU':
 for h in range(4):
  for slot in I[a]:
   p=arm-rot(h)*slot;k=(a,pose(p,h),tuple(xy(slot)))
   if sector(p,h):why='sector'
   elif any(hit(a,q,p,h)for q in STAR):why='independently_CURRENT_SAME_U_STAR_touched_before_FIRST_FOREIGN'
   else:assert bad(a,bud,p,h);why='actual_pre_FOREIGN_source_bud_CURRENT_through4'
   pre[k]=why
pc=compare(ref['all32_pre_FOREIGN_arm_CURRENT_loss_roles'],lambda r:(r['consumer'],tuple(r['ENTRY']),tuple(r['true_arm_input'])),pre)
# Directional endpoint semigroups: west and south increments plus a single C.
assert [exit(a,0j,3)[0] for a in'DVU']==[-1+1j,-3+1j,-4]
assert [exit(a,0j,2)[0] for a in'DVU']==[-1-1j,-1-3j,-4j]
assert exit('C',0j,3)==(-1+0j,2)
def WCS(ep):
 p,h=ep;assert p in(1+4j,-1+4j)and h==3
 # target x0 => 0=exitx-1-dW-3vW-4uW-dS-vS.
 # exitx=-1 impossible; +1 makes all listed counts zero; then 2=4-4uS.
 assert p.real==-1 or (4-2)%4!=0
armrows={};armkeep=[]
for n in range(5):
 h=(-n)%4
 for a in'FQB':
  for slot in I[a]:
   p=arm-rot(h)*slot;k=(n,a,pose(p,h),tuple(xy(slot)))
   if sector(p,h):why='sector'
   elif any(hit(a,q,p,h)for q in STAR):why='forbidden_COMPLETE_original_U_STAR_context_hit_at_age_le4'
   else:
    armkeep.append(k)
    if n==0:
     if a in'FQ':assert p.imag-p.real<4;why='zeroN_after_U_has_y_minus_x_ge4'
     else:assert p==3+7j and tr(W['D']+W['B']+M)['bad'];why='zeroN_equations_force_DDD_then_forbidden_actual_D_to_FOREIGN_pair'
    elif n==1:assert p==2+7j;why='first_W_H_ge5_plus_required_nonempty_W_BASE_H_increment_ge2'
    elif n in(2,3)or n==4 and a in'QB':assert ctx[a]['req'].get(local(bud,p,h))is False;why='original_bud_CURRENT_before_FOREIGN_through4'
    else:assert(n,a,p)==(4,'F',4+4j)and exit(a,p,h)==(target,th);why='no_C_left_zeroS_requires_immediate_first_returned_D_already_signed_simple'
   armrows[k]=why
ac=compare(ref['all235_FOREIGN_arm_TRUE_input_roles'],lambda r:(r['true_old_U_ENTRY_to_FOREIGN_ENTRY_C_clock'],r['FOREIGN'],tuple(r['ENTRY']),tuple(r['true_arm_input'])),armrows)
assert len(armkeep)==16
# Actual reset, retaining the U R27 CORE replacement.
G=-1+4j;hole=3j;assert raw['U']['last'][hole]==('R',27)
assert hole in {raw['U']['p']+rot(raw['U']['h'])*k for k in K}
for a in'DCVU':
 z=tr(W[a],4j,0)
 assert z['last'][G]==('L',1)and z['last'][hole]==('L',3)
for word in('UC','UCC'):
 z=tr(''.join(W[a]for a in word));assert z['last'][G]==('L',29)and z['last'][hole]==('L',31)
HOLD=STAR|{arm,bud};hr={};hk=[]
for q in(G,hole):
 for n in range(3):
  h=(-n)%4
  for a in'DCVU':
   for slot,(c,t)in raw[a]['last'].items():
    if c!='R':continue
    p=q-rot(h)*slot;ep=exit(a,p,h);k=(tuple(xy(q)),n,a,pose(p,h),tuple(xy(slot)),t)
    if sector(p,h):why='sector'
    elif raw[a]['req'][slot]:why='first_L_needs_an_earlier_BLACK_cut_after_actual_reset'
    elif any(hit(a,x,p,h)for x in HOLD):why='writer_touches_independently_CURRENT_pre_FOREIGN_STAR_arm_or_bud'
    else:
     hk.append(k)
     if n==0:assert p.imag<5;why='after_executed_reset_any_remaining_N0_head_y_ge5_or_already_C1_leaves_no_N0'
     elif n==1:assert p.imag-p.real<5;why='first_and_later_W1_heads_have_H_y_minus_x_ge5'
     elif a=='C':why='S2_C_writer_completes3_after_FOREIGN_ENTRY2'
     else:assert q==G and ep[0].imag<=4;why='zeroS_from_writer_exit_y_le4_cannot_reach_FOREIGNminus2_6S'
    hr[k]=why
hc=compare(ref['all216_CORE_inclusive_physical_G_h_first_BLACK_origins'],lambda r:(tuple(r['hole']),r['actual_ENTRY_clock'],r['writer'],tuple(r['ENTRY']),tuple(r['physical_final_R_slot']),r['own_R_tick0']),hr)
assert len(hk)==16
# NEW foreign R25 is a true external output and one of the retained nine.
ne=json.loads((R/'foreign_three_C_NE_reserve_2026-10-24/three_C_NE_reserve.json').read_text());assert[1,2]in ne['transfer_dichotomy']['nine_retained_originals']
br={};bk=[];new=[]
for n in range(5):
 h=(-n)%4
 for a in'FQB':
  for slot in I[a]:
   p=bud-rot(h)*slot;ep=exit(a,p,h);k=(n,a,pose(p,h),tuple(xy(slot)))
   if sector(p,h):why='sector'
   elif any(hit(a,q,p,h)for q in STAR|{arm}):why='forbidden_COMPLETE_original_STAR_or_newly_proved_arm_FOREIGN_context_hit'
   else:
    bk.append(k)
    if n==1:assert p in(3+8j,4+7j)and p.imag-p.real<=5;why='W1_FOREIGN_H_le5_below_first_W_H5_plus_required_nonempty_BASE_increment2'
    elif n==2:
     assert p in(-2+6j,-1+5j,1+5j)
     if p in(-2+6j,-1+5j):
      q=G if p==-2+6j else hole;loc=local(q,p,h)
      assert [(j,c)for j,(x,hh,c)in enumerate(ctx[a]['reads'])if x==loc][0]==(13,'L')
      why='genuinely_spent_upper_G_is_WHITE_at_foreign_actual_L13'if q==G else'actual_next_RAW_L3_deleted_h_is_WHITE_at_foreign_actual_L13'
     else:
      q=p+rot(h)*(1+2j);assert q==hole and raw[a]['last'][1+2j]==('R',25)
      assert local(1+2j,raw[a]['p'],raw[a]['h'])not in K and local(q,target,th)in K
      new.append((a,pose(p,h),xy(q)));why='NEW_FOREIGN_R25_guard_CURRENT_through_remaining2Cs_inside_actual_target_CORE'
    else:assert n==3;WCS(ep);why='one_remaining_C_and_exact_zero_W_S_semigroup_cannot_reach_target'
   br[k]=why
bc=compare(ref['all235_FOREIGN_bud_TRUE_input_roles'],lambda r:(r['true_preFOREIGN_C_clock'],r['FOREIGN'],tuple(r['ENTRY']),tuple(r['true_bud_input'])),br)
assert len(bk)==19 and len(new)==3
jr={};jk=[]
for q in RES:
 for a in'DVU':
  for h in range(4):
   for slot in I[a]:
    p=q-rot(h)*slot;ep=exit(a,p,h);k=(tuple(xy(q)),a,pose(p,h),tuple(xy(slot)))
    if sector(p,h):why='sector'
    elif any(hit(a,x,p,h)for x in LEFT):why='touches_independently_CURRENT_SAME_LEFT_before_and_after_earlier_loss_RAW'
    elif any(bad(a,x,p,h)for x in RES-{q}):why='independent_other_reserve_entry_CORE_or_first_WHITE'
    else:
     assert q==bud and h==3;WCS(ep);jk.append(k);why='only_W3_bud_loss_exit_cannot_reach_total4_target'
    jr[k]=why
jc=compare(ref['all96_coupled_d_arm_bud_first_CURRENT_loss_roles'],lambda r:(tuple(r['first_lost_reserve_tag']),r['consumer'],tuple(r['ENTRY']),tuple(r['input'])),jr)
assert len(jk)==4 and all(local(q,target,th)in K for q in(arm,bud))
LD=R/'full_packet_CURRENT_internal_RAW_lift_2026-10-24'
assert sha(LD/'manifest.json')=='8d68b1f841eaee84d409ea60cd16715c2dff6999531cd049b33a68c2a0a67504'
for f,h in json.loads((LD/'manifest.json').read_text())['files'].items():assert sha(LD/f)==h
lr=json.loads((LD/'CORE_lift.json').read_text());corefirst=[]
for q in sorted(K,key=lambda q:(q.real,q.imag)):
 j,c=next((j,c)for j,(p,h,c)in enumerate(raw['C']['reads'])if p==q)
 assert c=='L' and j<6;corefirst.append((tuple(xy(q)),j))
assert set(corefirst)=={(tuple(r['incoming_CORE_cell']),r['actual_C_first_L_tick0'])for r in lr['all5_actual_next_C_CORE_first_L_reads']}
internal=[(w,w[:j])for w in ('D','DC','V','VC','VCC','U','UC','UCC')for j in range(1,len(w))]
assert len(internal)==7 and set(internal)=={(r['actual_full_packet'],r['internal_RAW_cut_after'])for r in lr['all7_internal_RAW_cut_interfaces']}
analysis=[
'Bound physical bookkeeping supplement8d68: all five incoming C core identities are actually L-deleted within six reads, and all seven internal full-eight cuts have next C. SAME final CURRENT therefore forces SAME internal CURRENT. Every full packet used in the preforeign hole filter is genuinely completed before FOREIGN clock<=4; no future uncompleted packet is used. Only the THREE external C EXIT-CORE capture sites are first-WHITE; its other two EXIT-CORE sites are already ENTRY CORE and cannot contain an external CURRENT tag.',
'All finite domains are reconstructed from literal RAW/context first reads, physical last-R slots including EXIT CORE, and actual sector. No author generator was executed. Complete 32/235/216/235/96 role equalities hold.',
'Preforeign bud age5 is invoked on the real complete-eight consumer ENTRY. If a RAW context captures the bud in marker CORE inside a positive-C packet, it is a true full-packet input at the earlier BASE entry (age at most4), and actual own C deletes it. This is forbidden by the full-packet input theorem even if packet completion clock exceeds4. No blanket full-boundary law is silently imposed on internal cuts. C has zero external input; its EXIT CORE demands WHITE.',
'The U-star RAW lift is independently current at every ordinary RAW cut before FOREIGN. Arm first loss uses that independent star and preforeign bud only. Its FOREIGN alignment proof uses signed complete star MISS, never assumes arm persistence after a consuming foreign.',
'Zero N after U has H>=4; first C adds one. At W a nonempty actual BASE before FOREIGN is mandatory by actual adjacency, increases H by at least2. At n0 B3,7 the nonnegative N equations force exactly DDD. At n4 F4,4 exits exactly target; no C remains and every S base strictly lowers y, so immediate-returned-RAW simplicity applies with actual M, not a hypothetical completed next packet.',
'The h0,3 replacement is physically U R27 alive CORE until the executed next ordinary L3. Earliest BLACK-cut descent begins after that reset. Every possible restoring RAW-END R including CORE is counted. A first-L writer needs a preceding BLACK cut. Current HOLD hits are excluded under independent preforeign source/consumer-entry laws. Source-own C tails are actual reset events.',
'The three S2 foreign R25 guards are genuinely new external identities, all in the signed NE3 retained-nine branch. Remaining two C clocks measured from foreign ENTRY are within that theorem. No U R27 identity is reused.',
'Both all-length W/C/S endpoint arguments use nonnegative x counts to force all W and S D/V counts zero, then y4-4u cannot equal2; no rail cap/order enumeration. After one foreign, W heading at total ordinary clock at most4 is exactly3.',
'Postforeign LEFT currentness is conditional on GLOBAL-first stopping and complete star MISS. It supplies every earlier genuine cut including after a putative first loss actor; therefore any LEFT context input/capture is disallowed. Other reserve TRUE inputs are explicitly retained simultaneously. Only other entry-CORE/first-WHITE constraints eliminate rows.',
'At target ENTRY the SAME arm and bud are external current but both lie in actual D core. Conclusion excludes only old-U D0,2S totalC4 GLOBAL-first contact in the specified one-FOREIGN history. No postforeign age law, cycle/Jordan induction, secondFOREIGN or full-tail simplicity follows.'
]
out=dict(status='PASS scoped old-U all-tail S4 D coupled reserve',manifest_sha256=sha(D/'manifest.json'),independent_core_completeness_checks=len(corechecks),source_same_births=births,counts=dict(prearm=pc,foreign_arm=ac,physical_hole_origins=hc,foreign_bud=bc,joint_first_loss=jc),necessary=dict(arm=armkeep,holes=hk,bud=bk,new_FOREIGN_R25=new,joint=jk),analytic=analysis,dependencies={**ref['dependencies'],str((LD/'manifest.json').relative_to(R)):sha(LD/'manifest.json')},internal_RAW_lift=dict(incoming_CORE_deaths=corefirst,internal_cuts=internal))
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('report',sha(S.with_suffix('.json')))
