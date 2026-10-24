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
# Incoming beta is actual previous-FOREIGN output, never assigned JO age.
beta=(1,-1);M=(2,0);target=(0,1,1);birth=[]
for A in'FQB':
 ep=after(W[A]);cell=add(ep[:2],l.rot(beta,ep[2]));tr=l.trace(W[A]);assert tr['last'][cell]==('R',len(W[A])-2)and list(cell)in l.literal_geometry(W[A])['outputs']
 birth.append(dict(actual_foreign=A,actual_FOREIGN_EXIT=ep,SAME_beta_actual_cell=cell,post_EXIT_beta=beta,last_R_tick0=len(W[A])-2,last_R_read1=len(W[A])-1,genuine_external_output=True))
assert beta not in l.trace(W['D']+l.M)['first']
roles=[]
for K in range(4):
 h=(-K)%4
 for a in'DVU':
  tr=l.trace(W[a]+l.M)
  for slot,(c,t)in tr['first'].items():
   if c!='L'or slot in l.K:continue
   p=(*sub(beta,l.rot(slot,h)),h);ep=after(W[a],p);r=dict(consumer=a,sourceD_ENTRY_to_consumer_ENTRY_C_clock=K,pose=p,true_input_local=slot,actual_input=tr['first'][slot],owner=o.describe(a,t),RAW_EXIT=ep)
   if(sum(p[:2])+h)%2:why='sector'
   elif K==0:
    assert p[1]<1;why='N0_head_below_actual_firstD_RAW_EXIT_y1'
   elif K==1:
    assert p[1]<2;why='W1_head_below_actual_first_W_stage_y2'
   elif K==2:
    co=contact(*chord('D',(0,0,0)),*chord(a,p))
    if co:assert a=='U'and p==(0,0,2)and z(p)==z(after(W['D']));r['actual_source_D_contact']=co;why='nonadjacent_actual_source_D_EXIT_ENTRY_repeat'
    else:
     assert a=='U'and p==(1,1,2)and rel(M,p)in[tuple(q)for q in l.literal_geometry(W[a])['inputs']]
     why='SOURCE_D_fresh_common_consumed_at2_below_signed_atomic_min3_in_actual_BASE_cut_G8_factor'
   else:
    assert K==3
    co=contact(*chord('D',(0,0,0)),*chord(a,p))
    if co:r['actual_source_D_contact']=co;why='earlier_actual_source_D_chord_contact'
    else:
     assert ep[0]>=1>target[0];why='same_E3_zeroC_continuation_cannot_move_left_from_RAW_EXIT_x_ge1_to0'
   r['route']=why;roles.append(r)
assert len(roles)==32
readers=[]
for a in'DV':
 q=rel(beta,target);f=l.trace(W[a]+l.M)['first'][q];assert q==(2,1)and q not in l.K and f==('R',7)
 readers.append(dict(actual_target_RAW=a,ENTRY=target,sourceD_ENTRY_to_target_ENTRY_C_clock=3,SAME_beta=beta,local=q,actual_first=f,owner=o.describe(a,7),initial_BLACK_SAME_R_born_identity_contradicts_own_FIRST_WHITE=True))
bguard=dict(statement='Actual first postFOREIGN D0N, ordinary-only suffix and GLOBAL-first-contact simple-prefix stopping. SAME incoming FORE beta is CURRENT at any completed D/V target0,1,E atC3. This is a coordinate/actualG8 source-common guard; no age attached toFORE output. Hypothetical earlier BASE consumer factors are actualG8 by signed base-cut grammar with real precedingF/Q/B and real nextM11. Atomic source-D common minimum3 applies only inside such factors. CURRENT loss includes marker-only CORE capture, not only physical L. C hasI0.',all3_actual_FOREIGN_beta_births=birth,all32_beta_first_loss_clock_input_roles=roles,both_actual_D_V_first_WHITE_readers=readers)
# Exact source-position synthesis from signed129 + signed1607. Arbitrary
# complete entry field allowed. Each SOURCE position is actual, not a new
# history quotient or a shifted fictitious containing packet.
old=json.loads((R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/02_U_entry_center_simplicity.json').read_text())['all129_canonical_first_contact_cases'];assert len(old)==129
boundary=json.loads((R/'core_periodicity_new/atomic_three_C_pose_boundary_frozen_20261023_1607/02_atomic_three_C_pose_boundary.json').read_text());assert boundary['A_pose']==[0,0,0]and boundary['B_pose']==[-1,0,1]
rows=[];branches=[]
for r in old:
 q=dict(signed129_case=r)
 if not r['surviving_allowed_first_full_packet_ids']:
  q['route']='already_signed_complete_G8_first_contact_exclusion';rows.append(q);continue
 n,a,b=r['entry_C_gap'],r['earlier_atom'],r['later_atom'];p=tuple(r['later_pose']);case=[]
 if n==3:
  assert p==(-1,0,1)and(a,b)in{('D','V'),('C','V'),('V','D')}
  if a in'DV':
   x=dict(earlier_atom=a,later_atom=b,actual_old_source_position='factor_first_BASE_entry',actual_source_pose=(0,0,0),actual_later_pose=p,actual_global_C_clock=3,route='separately_signed_FIRST_post_FOREIGN_D_or_V_source_closure',source_first_RAW=a);case.append(x)
   y=dict(earlier_atom=a,later_atom=b,actual_old_source_position='second_complete_entry_after_factor_FIRST_plain_D',actual_first_RAW='D',actual_source_pose=(1,1,0),actual_later_pose=(0,1,1),actual_global_C_clock=3,route='new_genuine_FOREIGN_beta_own_R7_WHITE_guard');case.append(y)
  else:
   assert a=='C'and b=='V';case.append(dict(earlier_atom=a,later_atom=b,actual_old_source_position='actual_C1_inside_factor_FIRST_DC',actual_first_RAW='D',actual_source_pose=(1,1,0),actual_later_pose=(0,1,1),actual_global_C_clock=3,actual_C1_ENTRY_clock=0,no_second_C_or_fictitious_full_source_shift=True,route='new_genuine_FOREIGN_beta_own_R7_WHITE_guard'))
 else:
  assert a=='D'and b=='C'and(n,p)in{(4,(-1,-1,0)),(5,(0,-1,3))};case.append(dict(earlier_atom='D',later_atom='C',actual_old_source_position='factor_FIRST_D_base_in_D_or_DC',actual_source_pose=(0,0,0),actual_later_pose=p,actual_global_C_clock=n,route='separately_signed_FIRST_post_FOREIGN_D_source_closure',source_first_RAW='D'))
 for c in case:
  if c['route'].startswith('new_'):
   s=tuple(c['actual_source_pose']);pp=(*add(s[:2],p[:2]),p[2]);assert pp==(0,1,1)and c['actual_global_C_clock']==3 and c['actual_first_RAW']=='D'
   assert any(x['actual_target_RAW']==b for x in readers)
 q.update(route='signed_boundary_exception_with_actual_position_split',actual_position_branches=case);rows.append(q);branches+=case
assert len(rows)==129 and len(branches)==7
assert Counter(x['route']for x in branches)=={'separately_signed_FIRST_post_FOREIGN_D_or_V_source_closure':2,'new_genuine_FOREIGN_beta_own_R7_WHITE_guard':3,'separately_signed_FIRST_post_FOREIGN_D_source_closure':2}
# Grammar at the selected actual first-contact RAW cut. A completed
# terminal DCC is NOT forbidden and NOT silently called G8.
bridge=json.loads((R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/RAW_G8_bridge.json').read_text());assert len(bridge['all5_fixed_literal_conflicts'])==5 and len(bridge['all7_actual_predecessor_DCCC_EXIT_bud_conflicts'])==7
reg=[]
for word in['UDCC','UQUDCC']:
 t=l.trace(''.join(W[a]for a in word)+l.M);assert t['feasible'];reg.append(dict(actual_prepared_word=word,RAW_plus_actual_M11_complete=True,seed=sorted(q for q,(c,k)in t['first'].items()if c=='L'),terminal_DCC_is_real_and_unparsed=True,not_a_claim_of_proxy_contact_at_its_terminal_C=True))
grammar=dict(selected_factor_starts_actual_first_post_FOREIGN_BASE='D/V/U only',selected_factor_ends_at_first_contact_RAW='D/C/V/U with SAME actualM11',BASE_actor_case='Actual signed BASE-cut bridge gives G8. FirstD has actual precedingFOREIGN; no shared-core reset assumed.',C_actor_case='Maximal V/U C-runs have<=2 by signedVCCC/UCCC conflicts. DCCC forbidden by SAME real precedingRAW EXIT-bud identity; everyD has an actual predecessor. Any internal DCC followedBASE is literal-conflicting. Therefore the selected factor endingC either really parsesG8 or its final maximalrun is exactly terminalDCC.',genuine_exception='If chosen prefix ends terminalDCC, this theorem DOES NOT parse it or exclude a contact in its SECOND C. A first contact in the first C would instead give a prefix endingDC, already covered. The two actual positive controls are retained.',leading_C_exception='If the first postFOREIGN RAW isC, do not apply this ordinary BASE-start factor reduction. Choosing a later firstBASE leaves earlier C-source owners outside; no leading-C closure is inferred here.',terminal_positive_controls=reg)
D=[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/manifest.json',R/'audits/check_RAW_G8_base_cut_bridge_independent.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',R/'audits/check_U_entry_simplicity_independent.json',R/'core_periodicity_new/atomic_three_C_pose_boundary_frozen_20261023_1607/manifest.json',R/'audits/check_atomic_three_C_pose_boundary_independent.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'audits/check_atomic_common_four_C_independent.json',R/'first_postforeign_V_first_contact_2026-10-24/manifest.json',R/'audits/check_first_postforeign_V_contact_independent.json',R/'first_post_Q_B_DC_source_closure_2026-10-24/manifest.json',R/'audits/check_first_Q_B_DC_source_independent.json',R/'first_post_F_DC_source_closure_2026-10-24/manifest.json',R/'first_post_F_DC_source_closure_2026-10-24/terminal_C_maturity_premise_qualifier_manifest.json',R/'audits/check_first_F_DC_source_independent.json',R/'audits/check_first_F_DC_terminal_C_qualification_independent.json'];assert all(p.exists()for p in D)
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual U-entry completeG8 prefix,FIRSTF/Q/B,ordinary-only suffix startingD/V/U,actualfinalM11,GLOBAL-first-new-contact stopping. If selected ordinary prefix through actor really parsesG8 (in particular any BASE actor), outgoing old owner cannot be an ordinary postFOREIGN atom. LeadingC and genuine terminalDCC remain explicit exceptions. This is not arbitrary-tail simplicity.',genuine_beta_C3_boundary_guard=bguard,all129_signed_case_source_position_ledger=rows,all7_possible_boundary_position_branches=branches,actual_RAW_G8_or_terminal_DCC_grammar=grammar,exact_new_non_b1_owner_closure='The old source immediately after initialplainD, or actualC1 of initialDC, lies at1,1,N with ENTRYCclock0. Signed1607 maps its D/V first-contact target to global0,1,E atclock3, cut by SAME foreignbeta atownR7. No longer zero-C rail, larger source position, fake C birth or repaired beta is introduced.',terminal_DCC_not_excluded=True,leading_C_not_covered=True,no_original_FOREIGN_or_preFOREIGN_source_closure=True,no_arbitrary_tail_simplicity_or_later_FOREIGN_or_capture=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'boundary_beta.json').write_text(json.dumps(out,indent=2)+'\n');print('All-length ordinary BASE-start owner reduction:beta32+2readers, signed129→7actualboundarybranches,3new non-b1 branches closed. LeadingC/terminalDCC retained.')
