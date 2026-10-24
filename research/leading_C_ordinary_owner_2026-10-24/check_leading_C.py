"""Actual leading-C ordinary-owner reduction; no completed next G7 assumption.
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
# Exact grammar around the FIRST foreign. The known final M11 is not
# silently promoted to an extra completed G7 word.
def wordtrace(word):return l.trace(''.join(W[a]for a in word)+l.M)
def wordowner(word,t):
 off=0
 for i,a in enumerate(word):
  if t<off+len(W[a]):return dict(actual_atom_index0=i,actual_RAW=a,RAW_tick0=t-off,RAW_read_number1=t-off+1,canonical=o.describe(a,t-off))
  off+=len(W[a])
 return dict(actual_final_M11_tick0=t-off,actual_final_M11_read_number1=t-off+1,completed_next_G7_NOT_assumed=True)
def failed(word):
 t=wordtrace(word);assert not t['feasible'];return dict(word=word,conflict=t,previous_actual_owner=wordowner(word,t['previous_read']),conflicting_actual_owner=wordowner(word,t['conflict_read']))
initial=[]
for A in'FQB':initial.append(failed(A+'CCC'))
# Every actual completed RAW has its SAME M11 supplied by the next actual
# ordinary RAW (D uses its own10 + next firstL), or by final givenM11.
first_after_CC=[failed('CCD'),failed('CCU')]
ccv=[]
for A in'FQ':ccv.append(failed(A+'CCV'))
# BCCV prepared is genuine; actual FIRST B after G8 has plainU predecessor.
assert wordtrace('BCCV')['feasible'];ccv.append(failed('UBCCV'))
forepairs=json.loads((R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency.json').read_text())
legal=[(r['source'],r['foreign'])for r in forepairs['rows']if r['status']!='IMPOSSIBLE_LITERAL_PAIR'];assert set(legal)=={('V','F'),('V','Q'),('U','F'),('U','Q'),('U','B')}
# No third leadingC; if two, any following ordinary must be D/V/U and the
# above complete true contexts all fail. Two Cs may genuinely be terminal.
CU=failed('CU')
terminal_positive=[]
for word in['UQCC','UBCC']:
 raw=''.join(W[a]for a in word);t=wordtrace(word);assert t['feasible'];seed={q for q,(c,k)in t['first'].items()if c=='L'};B=set(seed);p=(0,0,0);reads=[]
 for k,c in enumerate(raw+l.M):
  assert(p[:2]in B)==(c=='L');reads.append(dict(tick0=k,read_number1=k+1,cell=p[:2],turn=c,owner=wordowner(word,k)))
  if c=='L':B.remove(p[:2])
  else:B.add(p[:2])
  p=after(c,p)
 terminal_positive.append(dict(word=word,actual_finite_black_seed=sorted(seed),all_actual_RAW_and_given_M11_reads=reads,terminal_CC_genuinely_legal=True,no_actual_next_completed_G7_assumed=True))
grammar=dict(all3_FOREIGN_CCC_actual_marker_conflicts=initial,both_universal_CC_to_D_or_U_conflicts=first_after_CC,all3_foreign_CC_to_V_exclusions=ccv,sole_prepared_BCCV_positive_is_retained=True,all5_genuine_G8_to_FIRST_FOREIGN_legal_pairs=legal,universal_C_to_U_conflict=CU,conclusion='An ordinary suffix after the firstFOREIGN either ends at C orCC before any BASE, or has EXACTLY one leadingC followed by firstBASE D/V. There is no later ordinary after the two-leading-C case, but the actual given terminalCC+M is not excluded.',all2_genuine_U_entry_terminal_CC_positive_controls=terminal_positive)
# Fresh incoming C creates beta=(1,-1) in first-D chart, genuinely outside
# its own EXIT core. This is a RAW birth identity, not any preFOREIGN tag.
beta=(1,-1);M=(2,0);CO={(2,0),(2,1),(1,2)};pC=after(W['C']);bC=add(pC[:2],l.rot(beta,pC[2]));assert bC==(1,2)
f=l.trace(W['C'])['last'][bC];assert f==('R',13)and list(bC)in l.literal_geometry(W['C'])['outputs'];assert beta not in l.trace(W['D']+l.M)['first']
birth=dict(actual_previous_RAW='C',previous_C_ENTRY=(0,0,0),previous_C_RAW_EXIT=pC,first_D_ENTRY=pC,previous_C_ENTRY_to_first_D_ENTRY_clock=1,SAME_beta_in_D_chart=beta,SAME_beta_in_previous_C_chart=bC,actual_last_R_tick0=13,actual_last_R_read1=14,external_CURRENT_at_previous_C_EXIT=True,first_D_misses_beta=True)
# Only the late first-D -> C clock5 boundary remains after the previous
# C's portable output reserve. Prove SAME beta CURRENT at that actual
# terminal-C ENTRY using genuine first-CURRENT-loss BASE inputs.
target=(0,-1,3);betaW=[]
for n in range(6):
 h=(-n)%4
 for a in'DVU':
  tr=l.trace(W[a]+l.M)
  for slot,(c,t)in tr['first'].items():
   if c!='L'or slot in l.K:continue
   p=(*sub(beta,l.rot(slot,h)),h);ep=after(W[a],p);r=dict(actual_consumer=a,source_D_ENTRY_to_consumer_ENTRY_C_clock=n,pose=p,actual_input=slot,actual_input_owner=o.describe(a,t),RAW_EXIT=ep)
   if(sum(p[:2])+h)%2:why='sector'
   elif n==0:
    assert p[1]<1;why='N0_below_actual_source_D_EXIT_y1'
   elif n==1:
    assert p[1]<2;why='W1_below_actual_source_D_first_W_head_y2'
   elif n==2:
    co=contact(*chord('D',(0,0,0)),*chord(a,p))
    if co:
     assert a=='U'and p==(0,0,2);r['earlier_actual_contact']=co;why='nonadjacent_source_D_EXIT_repeat'
    else:
     assert a=='U'and p==(1,1,2)and rel(M,p)in[tuple(q)for q in l.literal_geometry(W[a])['inputs']];why='actual_source_D_to_earlier_BASE_G8_factor_common_min3'
   elif n==3:
    co=contact(*chord('D',(0,0,0)),*chord(a,p))
    if co:r['earlier_actual_contact']=co;why='earlier_source_D_contact'
    elif p==(-1,-2,1):
     assert a=='U';g=add(p[:2],l.rot((0,1),h));assert g==(0,-2)and rel(g,target)in l.K;r['fresh_U_same_star_in_final_CORE']=g;why='new_fresh_U_RAW_star_is_CURRENT_in_final_C_ENTRY_CORE'
    else:
     assert(a=='V'and p==(-2,-1,1))or(a=='U'and p==(-3,-2,1));assert z(ep)==z(target);why='earlier_RAW_EXIT_repeats_final_target_ENTRY_vertex'
   elif n==4:
    assert ep[1]>=-1;why='remaining_N_to_W_C_raises_y_to_ge0_then_zeroW_cannot_lower_to_minus1'
   else:
    assert n==5
    if ep[1]>target[1]:why='sameW_RAW_EXIT_y_above_target'
    elif ep[0]<target[0]:why='sameW_RAW_EXIT_left_of_target_then_W_cannot_move_right'
    else:
     assert ep==target and((a=='V'and p==(3,-2,3))or(a=='U'and p==(4,-1,3)));f=tr['first'][rel(M,p)];assert f[0]=='R';r['actual_first_WHITE_on_SAME_source_D_common']=dict(cell=M,local=rel(M,p),first=f,owner=o.describe(a,f[1]));why='independently_CURRENT_source_D_common_at_W5_negative_y_target'
   r['route']=why;betaW.append(r)
assert len(betaW)==48
# The source-D common reserve is a separately independently retained part
# of partial45abc. Do not rehabilitate the rejected original F-pair proof.
oldF=json.loads((R/'original_F_piece_firstpost_DC_2026-10-24/F_piece_DC.json').read_text());common=oldF['fresh_D_common_entry_reserve'];assert len(common['all16_plain_E3_sourceD_DC_common_queries'])==16 and len(common['all16_N4_W5_plain_input_RAW_endpoint_inequalities'])==16
assert 'W5 target y<0'in common['statement']
# Actual required beta is in target ENTRYCORE. C has I0, no hidden
# noninput export or fictitious packet captures a CURRENT identity.
beta_target_conflict=conflict('C',target,{beta});assert any(q['role']=='ENTRY_CORE'for q in beta_target_conflict)
beta_guard=dict(actual_genuine_previous_C_birth=birth,actual_target_RAW='C',actual_target_ENTRY=target,source_D_ENTRY_to_target_ENTRY_C_clock=5,all48_actual_first_CURRENT_beta_loss_roles=betaW,SAME_beta_CURRENT_at_target_ENTRY=True,actual_target_CORE_or_first_WHITE=beta_target_conflict,independently_retained_fresh_D_common_reserve=common,actual_BASE_ending_G8_premise='Whenever a hypothetical earlier D/V/U consumes source-D common, use the actual first-D to that BASE factor with real precedingC and actual nextRAW supplying M11. Never parse the terminalC target or an uncompleted nextG7.',original143d_universal_pair_claim_REMAINS_REJECTED=True,no_foreign_age_or_post_contact_CURRENT_claim=True)
# Seven true boundary branches from signed129/1607 after firstBASE. Work
# in the actual preceding leading-C chart, not in a fake factor reset.
old=json.loads((R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/02_U_entry_center_simplicity.json').read_text())['all129_canonical_first_contact_cases'];bd=json.loads((R/'ordinary_boundary_owner_beta_2026-10-24/boundary_beta.json').read_text())['all7_possible_boundary_position_branches'];assert len(bd)==7
base=(0,1,3);trans=[]
for b in bd:
 q=tuple(b['actual_later_pose']);globalp=(*add(base[:2],l.rot(q[:2],base[2])),(q[2]+base[2])%4);K=1+b['actual_global_C_clock'];r=dict(signed_actual_boundary_branch=b,actual_leading_C_ENTRY=(0,0,0),actual_first_BASE_ENTRY=base,actual_target_in_leading_C_chart=globalp,actual_leading_C_ENTRY_to_target_ENTRY_C_clock=K)
 a=b['later_atom'];assert b['actual_source_position']if'actual_source_position'in b else True
 if K==6:
  assert a=='C'and q==(0,-1,3)and b['actual_old_source_position'].startswith('factor_FIRST_D');r.update(route='new_C_preceded_sourceD_W5_SAME_beta_guard',actual_beta_target_in_leading_C_chart=bC)
 else:
  assert(K==4 and globalp[2]==0 and globalp[1]<=1)or(K==5 and globalp[2]==3 and globalp[1]<=0)
  bad=conflict(a,globalp,CO);assert bad;r.update(route='SAME_three_fresh_leading_C_outputs_CURRENT_by_portable_N4_or_W5_entry_reserve',actual_CURRENT_CORE_or_first_WHITE=bad)
 trans.append(r)
assert Counter(r['route']for r in trans)=={'SAME_three_fresh_leading_C_outputs_CURRENT_by_portable_N4_or_W5_entry_reserve':6,'new_C_preceded_sourceD_W5_SAME_beta_guard':1}
# Exact129 geometry rows: actual grammar at the selected RAW endpoint is
# G8 or real terminalDCC. If G8, only these seven true source positions
# survive before applying the new preceding-C guardians.
ledger=[]
for r in old:
 if not r['surviving_allowed_first_full_packet_ids']:ledger.append(dict(signed129=r,route='already_signed_actual_G8_geometry_exclusion'))
 else:
  rows=[q for q in trans if q['signed_actual_boundary_branch']['earlier_atom']==r['earlier_atom']and q['signed_actual_boundary_branch']['later_atom']==r['later_atom']and q['signed_actual_boundary_branch']['actual_global_C_clock']==r['entry_C_gap']];assert rows;ledger.append(dict(signed129=r,route='actual_source_position_and_preceding_leading_C_guard',all_actual_position_branches=rows))
assert len(ledger)==129
# Genuine source positions BEFORE firstBASE: just the immediate leadingC,
# already signed as outgoing b1C. Two-leading-C case is terminal, so has
# no later actor or source ownership to silently discard.
cp=json.loads((R/'first_post_Q_B_DC_source_closure_2026-10-24/Q_B_DC_closure.json').read_text());assert len(cp['fresh_C_portable_coupled_reserve']['all96_plain_true_input_first_loss_roles'])==96
D=[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'audits/check_complete8_foreign_adjacency_independent.json',R/'third_atom_CCV_adversarial_2026-10-24/manifest.json',R/'audits/third_CCV_independent.json',R/'first_post_Q_B_DC_source_closure_2026-10-24/manifest.json',R/'audits/check_first_Q_B_DC_source_independent.json',R/'first_post_F_DC_source_closure_2026-10-24/manifest.json',R/'first_post_F_DC_source_closure_2026-10-24/terminal_C_maturity_premise_qualifier_manifest.json',R/'audits/check_first_F_DC_source_independent.json',R/'audits/check_first_F_DC_terminal_C_qualification_independent.json',R/'original_F_piece_firstpost_DC_2026-10-24/partial_scope_qualification_manifest.json',R/'audits/check_F_DC_partial_qualification_independent.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/manifest.json',R/'audits/check_RAW_G8_base_cut_bridge_independent.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/U_star_RAW_lift_manifest.json',R/'audits/check_fresh_U_star_RAW_lift_independent.json',R/'ordinary_boundary_owner_beta_2026-10-24/manifest.json',R/'audits/check_ordinary_boundary_beta_independent.json',R/'terminal_DCC_ordinary_owner_2026-10-24/manifest.json',R/'audits/check_terminal_DCC_ordinary_owner_independent.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'audits/check_atomic_common_four_C_independent.json'];assert all(p.exists()for p in D)
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual U-entry completeG8 prefix,FIRST completeF/Q/B,then ordinary-only RAW suffix startingC,with actual finalM11. At GLOBAL first new proxy contact, outgoing old owner cannot be any postFOREIGN ordinary source. LeadingC and terminalDCC are handled as real grammar exceptions; no completed nextG7 assumption. PreFOREIGN/originalFOREIGN owners remain separate.',exact_leading_C_grammar=grammar,new_C_preceded_sourceD_terminal_C5_beta_guard=beta_guard,all7_actual_BASE_boundary_branches_with_genuine_preceding_C_guard=trans,all129_actual_BASE_factor_geometry_source_position_routes=ledger,fresh_C_portable_reserve_scope=cp['fresh_C_portable_coupled_reserve']['statement'],source_before_first_BASE='The single actual leadingC is exactly b1C, whose arbitrary ordinary suffix source-owner exclusion is signed1b595 forQ/B or8b58+mandatory5e243 forF. No second leadingC can have a later ordinary actor, since that branch is terminal.',real_terminal_DCC_actor='Do NOT call terminalDCC a G8 producer. Signed366d ordinary-owner theorem covers its secondC directly, including leadingC old sources. Its firstC endpoint endingDC really is G8. GivenM11 is not a completed nextG7.',no_arbitrary_tail_simplicity_or_FOREIGN_preFOREIGN_source_claim=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'leading_C.json').write_text(json.dumps(out,indent=2)+'\n');print('LeadingC ordinaryowners:terminalCC legal/no ordinary continuation; oneC+firstD/V,129→7actualbranches=6 SAME C outputs+1 betaW5. No nextG7 assumption.')
