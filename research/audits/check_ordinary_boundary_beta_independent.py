from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'ordinary_boundary_owner_beta_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json'
assert sha(MF)=='268f0f040d6fa870d63b3aa54b369431eedc97ce4c1f42a61fa1385981d95ac3';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'boundary_beta.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,rot,xy,center,meet=[ns[k] for k in ('W','M','K','tr','rot','xy','center','meet')]
def first(a):
 ans={}
 for t,(q,h,c) in enumerate(tr(W[a]+M)['reads']):ans.setdefault(q,(c,t))
 return ans
beta=1-1j;common=2+0j;target=1j;guard=J['genuine_beta_C3_boundary_guard'];births=[]
for a in 'FQB':
 z=tr(W[a]);q=z['p']+rot(z['h'])*beta;assert z['last'][q]==('R',len(W[a])-2) and beta not in K
 r=next(r for r in guard['all3_actual_FOREIGN_beta_births'] if r['actual_foreign']==a)
 assert r['actual_FOREIGN_EXIT']==[*xy(z['p']),z['h']] and r['SAME_beta_actual_cell']==xy(q) and r['last_R_tick0']==len(W[a])-2
 births.append((a,xy(q),len(W[a])-2))
assert beta not in first('D')
assert not [q for q,(c,t) in first('C').items() if c=='L' and q not in K]
oldD=tr(W['D']);oldch=(center(0j,0),center(oldD['p'],oldD['h']));assert oldD['p']==1+1j
rows=[];count=Counter()
for clock in range(4):
 h=(-clock)%4
 for a in 'DVU':
  for slot,(c,t) in first(a).items():
   if c!='L' or slot in K:continue
   p=beta-rot(h)*slot;z=tr(W[a],p,h);ep=z['p'];co=None
   if (int(p.real+p.imag)+h)%2:why='sector'
   elif clock==0:assert p.imag<1;why='N0_head_below_actual_firstD_RAW_EXIT_y1'
   elif clock==1:assert p.imag<2;why='W1_head_below_actual_first_W_stage_y2'
   elif clock==2:
    co=meet(*oldch,center(p,h),center(ep,z['h']))
    if co is not None:
     assert a=='U' and p==0j and center(p,h)==oldch[1];why='nonadjacent_actual_source_D_EXIT_ENTRY_repeat'
    else:
     assert a=='U' and p==1+1j and (common-p)/rot(h) in [q for q,(c,t) in first(a).items() if c=='L' and q not in K]
     why='SOURCE_D_fresh_common_consumed_at2_below_signed_atomic_min3_in_actual_BASE_cut_G8_factor'
   else:
    co=meet(*oldch,center(p,h),center(ep,z['h']))
    if co is not None:why='earlier_actual_source_D_chord_contact'
    else:assert ep.real>=1>target.real;why='same_E3_zeroC_continuation_cannot_move_left_from_RAW_EXIT_x_ge1_to0'
   ar=next(r for r in guard['all32_beta_first_loss_clock_input_roles'] if r['consumer']==a and r['sourceD_ENTRY_to_consumer_ENTRY_C_clock']==clock and r['true_input_local']==xy(slot))
   assert ar['pose']==[*xy(p),h] and ar['RAW_EXIT']==[*xy(ep),z['h']] and ar['actual_input']==['L',t] and ar['route']==why
   o=ar['owner'];assert o['packet']==a and o['context_tick0']==t and o['turn']=='L' and o['RAW_length']==len(W[a])
   assert o['next_word_tick0']==(t-len(W[a]) if t>=len(W[a]) else None)
   rows.append(dict(clock=clock,consumer=a,slot=xy(slot),pose=[*xy(p),h],exit=[*xy(ep),z['h']],read=t,route=why,contact=repr(co)));count[why]+=1
assert len(rows)==32
for a in 'DV':
 loc=(beta-target)/rot(1);assert loc==2+1j and loc not in K and first(a)[loc]==('R',7)
assert [tr(W[a])['p'] for a in 'DVU']==[1+1j,1+3j,4j] and tr(W['C'])['p']==1j
# Exact equality to the separately signed complete129-case ledger, not just aggregate counts.
signed=json.loads((R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/02_U_entry_center_simplicity.json').read_text())['all129_canonical_first_contact_cases']
assert [r['signed129_case'] for r in J['all129_signed_case_source_position_ledger']]==signed and len(signed)==129
boundary=[r for r in signed if r['surviving_allowed_first_full_packet_ids']]
assert {(r['entry_C_gap'],r['earlier_atom'],r['later_atom'],tuple(r['later_pose'])) for r in boundary}=={(3,'D','V',(-1,0,1)),(3,'C','V',(-1,0,1)),(3,'V','D',(-1,0,1)),(4,'D','C',(-1,-1,0)),(5,'D','C',(0,-1,3))}
actual=[]
for r in J['all129_signed_case_source_position_ledger']:
 b=r['signed129_case']
 if not b['surviving_allowed_first_full_packet_ids']:
  assert r['route']=='already_signed_complete_G8_first_contact_exclusion';continue
 branches=r['actual_position_branches'];a=b['earlier_atom'];later=b['later_atom'];clock=b['entry_C_gap']
 assert len(branches)==(2 if clock==3 and a in 'DV' else 1)
 for branch in branches:
  sp=complex(*branch['actual_source_pose'][:2]);assert branch['actual_source_pose'][2]==0
  tp=sp+complex(*b['later_pose'][:2]);assert branch['actual_later_pose']==[*xy(tp),b['later_pose'][2]]
  assert branch['earlier_atom']==a and branch['later_atom']==later and branch['actual_global_C_clock']==clock
  if sp==0j:
   assert a in 'DV' and branch['route'].startswith('separately_signed_FIRST_post_FOREIGN')
  else:
   assert sp==1+1j and clock==3 and branch['actual_first_RAW']=='D' and tp==target and branch['route']=='new_genuine_FOREIGN_beta_own_R7_WHITE_guard'
   if a=='C':assert branch['actual_C1_ENTRY_clock']==0 and branch['actual_old_source_position']=='actual_C1_inside_factor_FIRST_DC'
   else:assert branch['actual_old_source_position']=='second_complete_entry_after_factor_FIRST_plain_D'
  actual.append(branch)
assert actual==J['all7_possible_boundary_position_branches'] and len(actual)==7 and sum(b['route'].startswith('new_') for b in actual)==3
for r in J['actual_RAW_G8_or_terminal_DCC_grammar']['terminal_positive_controls']:
 z=tr(''.join(W[a] for a in r['actual_prepared_word'])+M);assert not z['bad'] and sorted(map(xy,[q for q,b in z['req'].items() if b]))==r['seed']
O=dict(status='PASS ordinary postforeign owner reduction only at actual BASE-start G8 cuts',manifest=sha(MF),script=sha(S),genuine_beta_births=births,first_loss_roles=rows,counts=dict(count),signed_geometry_rows=129,boundary_geometry_rows=5,actual_position_branches=7,new_beta_branches=3,analytic_review=[
'SAME beta is born by each actual FOREIGN penultimate R and lies outside EXIT CORE. Initial sourceD plus its real marker misses it. The first CURRENT loss interface includes all plain true inputs, including D/V/U marker-owned absorption; C has no external inputs and preserves old residual identities. No maturity law is assigned to the FOREIGN source.',
'After sourceD, initial N heads have y>=1; one C raises the initial W stage to y>=2 and W bases cannot lower y. All relevant N0/W1 input poses violate these cones. At S2, one U repeats the actual oldD terminal vertex nonadjacently, already a prior contact at its entry; the other consumes original sourceD common at age2, excluded by signed atomic minimum3 on the actual sourceD-to-earlier-BASE G8 factor with its real next M. Neither a terminalC cut nor an uncompleted source is used for this maturity invocation.',
'At E3 the remaining contact cases already hit the actual oldD chord before the stipulated global-first target. Other first-loss RAW exits have x>=1; with no C remaining every E BASE strictly increases x, so they cannot precede target x0. Thus beta is still CURRENT at target ENTRY. It is a nonCORE first-WHITE ownR7 of both targetD/V; no persistence through the actual contact is assumed.',
'The complete signed129 universe is compared row-for-row. Its five boundary exceptions are used as universal G8 first-contact alternatives, not as an application of only the U-entry corollary. Separately signed actual-atomic1607 locates all E3 source entries: firstBASE, second complete entry after firstplainD, or C1 of firstDC. C1 enters at clock0 and head1,1,N. Exact translations produce seven branches, four firstpostD/V owners already signed and three target0,1,E beta cuts.',
'Each selected factor begins at the actual firstpostforeign BASE with unrestricted entry field. Every internal marker is supplied by the actual next RAW. BASE actors always permit the signed G8 parse; C actors require the explicit real-G8 condition, with genuine terminalDCC left unparsed. Its first C would instead endDC and be covered. LeadingC, preforeign owners, originalforeign pieces and laterforeign behavior remain outside the statement.',
'All original U-entry/FIRSTforeign/global-first-contact hypotheses and the mandatory terminal-C maturity qualifier5e243 are retained. This is an all-length outgoing ordinary-owner reduction at actual grammar cuts, not arbitrary-tail simplicity or universal attraction. Actual UDCC/UQUDCC marked positive exceptions remain feasible.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(count);print(sha(S.with_suffix('.json')))
