"""Unbounded S/E/N two-C second-F gate: actual firstforeign R8 output.
No imported preforeign age law, proxy simplicity premise or rail bound.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def spell(s):return ''.join(W[a]for a in s)
def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def meet(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);de=det(u,v)
 if de:
  ss,tt=Q(det(q,v),de),Q(det(q,u),de)
  return dict(old_s=str(ss),new_lo=str(tt),new_hi=str(tt))if 0<=ss<=1 and 0<=tt<=1 else None
 if det(q,u):return None
 k=0 if v[0]else 1;lo,hi=sorted((Q(a[k]-c[k],v[k]),Q(b[k]-c[k],v[k])));lo,hi=max(Q(0),lo),min(Q(1),hi)
 if lo>hi:return None
 point=add(c,(lo*v[0],lo*v[1]));j=0 if u[0]else 1;ss=Q(point[j]-a[j],u[j]);return dict(old_s=str(ss),new_lo=str(lo),new_hi=str(hi))
# Initial plain U, immediately firstA. Both actual identities are checked
# physically; firstA's R8 is a NEW output, not an old producer relabel.
b=(2,4);s=(1,3);target=(3,3,0);births=[]
ut=l.trace(W['U']);assert ut['last'][s]==('R',26)and list(s)in l.literal_geometry(W['U'])['outputs']
for A in'FQB':
 ar=l.trace(W[A]);ag=l.literal_geometry(W[A]);ep=after(W[A],(0,4,0));assert ar['last'][(2,0)]==('R',8)and[2,0]in ag['outputs']and ep[0]<=-3 and ep[1]<=2 and ep[2]==2
 assert(1,-1)not in l.trace(W[A]+l.M)['first'];Kout={add(ep[:2],l.rot(q,ep[2]))for q in l.K};assert b not in Kout and s not in Kout
 births.append(dict(first_foreign=A,actual_entry=(0,4,0),actual_EXIT=ep,new_common_b=dict(cell=b,own_foreign_R_tick0=8,global_R_tick0=36,CURRENT_at_first_EXIT=True),old_U_bud_s=dict(cell=s,own_U_R_tick0=26,first_foreign_complete_context_MISS=True,CURRENT_at_first_EXIT=True)))
# Every possible first CURRENT loss by an actual ordinary RAW is a true
# input, including marker-owned EXIT CORE absorption. Rebuild that local
# completeness, rather than omitting CORE writes or recycled identities.
ports=[];capture=[]
for a in'DCVU':
 geo=l.literal_geometry(W[a]);rt=l.trace(W[a]);tt=l.trace(W[a]+l.M);ep=after(W[a]);Kout={add(ep[:2],l.rot(q,ep[2]))for q in l.K}
 for q in sorted(Kout):
  if q not in l.K and q not in rt['last']:assert q in tt['first']and tt['first'][q][0]=='L'and list(q)in geo['inputs']
  capture.append(dict(atom=a,actual_EXIT_CORE_cell=q,in_ENTRY_CORE=q in l.K,actual_RAW_last_read=rt['last'].get(q),actual_first_requirement=tt['first'].get(q)))
 for slot in map(tuple,geo['inputs']):
  # All headings below are relative to ORIGINAL initial U, not the first
  # foreign EXIT chart: S0,E1,N2 after that first half-turn.
  row=dict(atom=a,input_slot=slot,first_L_owner=o.describe(a,tt['first'][slot][1]),S_input_x_minus_head_x=-slot[0],E_input_y_minus_head_y=-slot[0],N_loss_EXIT_minus_tag=(ep[0]-slot[0],ep[1]-slot[1]))
  assert row['S_input_x_minus_head_x']<=1 and row['E_input_y_minus_head_y']<=1 and row['N_loss_EXIT_minus_tag'][1]>=0
  if row['N_loss_EXIT_minus_tag'][1]==0:assert row['N_loss_EXIT_minus_tag'][0]==1
  ports.append(row)
assert len(ports)==8 and l.literal_geometry(W['C'])['inputs']==[] and len(capture)==20
assert after(W['C'],(0,0,2))==(0,-1,1)and after(W['C'],(0,0,1))==(1,0,0)
zero=[]
for a in'DVU':
 n=after(W[a]);sd=after(W[a],(0,0,2));e=after(W[a],(0,0,1));assert sd[0]<=0 and sd[1]<0 and e[1]<=0 and n[0]>=0 and n[1]>0;zero.append(dict(atom=a,S_increment=sd,E_increment=e,N_increment=n))
ft=l.trace(W['F']+l.M);lb=sub(b,target[:2]);ls=sub(s,target[:2]);assert lb==(-1,1)and ls==(-2,0)and ft['first'][lb]==('R',14)and ft['first'][ls]==('R',44)
# A real genuine-U history reaches the gate with arbitrary-field validity,
# and its open repaired proxy is directly simple. It does not completeF.
prefix='UFCDDVCDU';raw=spell(prefix);tr=l.trace(raw+l.M);assert tr['feasible']and after(raw)==target;seed32={q for q,(c,k)in tr['first'].items()if c=='L'};assert len(seed32)==32
ready=l.trace(raw+W['F'][:14]);assert ready['feasible'];seed33={q for q,(c,k)in ready['first'].items()if c=='L'};assert len(seed33)==33 and seed33-seed32=={(3,5)}and(3,5)not in tr['first']
# Attempt both fixed complete boards. The 32-board genuinely failsL12;
# the minimally enriched 33-board genuinely reaches the protected b R14.
controls=[]
for label,seed,expected in [('32_cell_prefix_board',seed32,(12,(3,5),'L')),('33_cell_unread_extension',seed33,(14,b,'R'))]:
 B={q:('initial',q)for q in seed};p=(0,0,0);tick=0;reads={q:[]for q in[(0,0),(0,1),(1,0),(1,1),(2,0),(2,1),b,s]};cuts=[];fail=None
 for i,a in enumerate(prefix):
  for k,c in enumerate(W[a]):
   q=p[:2];assert(q in B)==(c=='L')
   if q in reads:reads[q].append(dict(global_tick0=tick,atom_index0=i,atom=a,own_tick0=k,turn=c,SAME_R_birth_before=B.get(q)))
   if c=='L':del B[q]
   else:B[q]=tick
   p=after(c,p);tick+=1
  if i>=1:
   K={add(p[:2],l.rot(q,p[2]))for q in l.K};assert B.get(b)==36 and b not in K and B.get(s)==26 and s not in K; assert all(B.get(g)==ut['last'][g][1] and g not in K for g in[(0,0),(0,1),(1,0),(1,1)]); cuts.append(dict(after_atom_index0=i,atom=a,RAW_cut_tick0=tick,head=p,b_SAME_CURRENT=True,s_SAME_CURRENT=True,all4_original_U_STAR_CURRENT=True,original_east_pair_states=[dict(cell=g,original_birth_tick0=ut['last'][g][1],same_original_physically_BLACK=B.get(g)==ut['last'][g][1],actual_present_R_identity=B.get(g))for g in[(2,0),(2,1)]]))
 assert p==target and tick==190
 for k,c in enumerate(W['F']):
  q=p[:2]
  if(q in B)!=(c=='L'):
   fail=dict(candidate_F_own_tick0=k,candidate_F_own_read_number1=k+1,global_tick0=tick,cell=q,required_turn=c,actual_turn='L'if q in B else'R',SAME_R_identity_before=B.get(q),canonical_candidate_owner=o.describe('F',k));break
  if c=='L':del B[q]
  else:B[q]=tick
  p=after(c,p);tick+=1
 assert(fail['candidate_F_own_tick0'],tuple(fail['cell']),fail['required_turn'])==expected
 # The suppliedM11 consists of real first11 fine reads, all before either
 # failure. Thus both prefix fields are complete ordinary contexts.
 controls.append(dict(label=label,complete_seed=sorted(seed),seed_mass=len(seed),prefix_word=prefix,prefix_RAW_length=190,actual_prefix_final_M11_feasible=True,first_unmatched_second_F_request=fail,all_b_s_CURRENT_marked_cut_states=cuts,selected_source_and_cycle_physical_reads=[dict(cell=q,reads=rs)for q,rs in sorted(reads.items())]))
# Earliest original east-pair deletions occur at the final actual U; its
# rebirth of2,1 is a DIFFERENT R. This illustrates real firstforeign mixing.
cr={tuple(q['cell']):q['reads']for q in controls[1]['selected_source_and_cycle_physical_reads']}
assert[(q['global_tick0'],q['turn'])for q in cr[(2,0)]]==[(8,'R'),(176,'L')]
assert[(q['global_tick0'],q['turn'])for q in cr[(2,1)]]==[(7,'R'),(175,'L'),(183,'R')]
# Exact finite geometry of reached prefix, not a general induction.
p=(0,0,0);pieces=[]
for i,a in enumerate(prefix):
 if a in'FQB':
  mid=after(W['F'],p);pieces.append(dict(atom_index0=i,atom=a,piece='Fprefix',start=z(p),end=z(mid)));end=after(W[a],p)
  if a!='F':pieces.append(dict(atom_index0=i,atom=a,piece=a+'tail',start=z(mid),end=z(end)))
 else:
  end=after(W[a],p);pieces.append(dict(atom_index0=i,atom=a,piece='ordinary',start=z(p),end=z(end)))
 p=end
pairs=[]
for i,A in enumerate(pieces):
 for j in range(i+1,len(pieces)):
  B=pieces[j];m=meet(A['start'],A['end'],B['start'],B['end'])
  if j==i+1:assert m==dict(old_s='1',new_lo='0',new_hi='0')
  else:assert m is None
  pairs.append(dict(earlier_piece=i,later_piece=j,intersection=m))
D=[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Initial actual plainU, immediate firstA inF/Q/B, arbitrary ordinary RAW S/E/N section with EXACTLY TWO Cs, target secondFOREIGN F at initial-U frame(3,3,N), with actual marker contexts. This target cannot complete: SAME firstA commonR8 output b2,4 is CURRENT at ENTRY but requiredWHITE by F ownR14. No global-simple, rail-depth, sourceU-star permanence acrossfirstA, or old8 maturity premise.',all3_actual_first_FOREIGN_b_and_s_birth_interfaces=births,all8_plain_true_input_loss_supports=ports,all20_plain_RAW_EXIT_CORE_capture_checks=capture,all3_ordinary_zero_C_drifts=zero,unbounded_first_loss_proof='Choose first CURRENT loss of b. S0 ordinary headsx<=-3; every S inputx<=headx+1<=-2<b_x2. After first actualC S->E, heady<=1; E zeroC cannotraiseY and every E inputy<=heady+1<=2<b_y4. C hasI0. A remaining firstloss is N2; every lossRAW EXIT hasY>=b_y4. With no Csleft, every later N atom strictlyraisesY, so it cannot reach target headY3. This handles SAME-ID rebirths and unreadCORE capture by choosing first loss; it imposes no bound on S/E/N lengths.',old_U_bud_independent_secondary_guard='For s1,3 the same S/E bounds hold. N2 lossEXIT Y>=3, and equality only D/V-upper/U-upperb at EXIT(2,3,N). No subsequent N atom haszeroY increment, so cannot reach target(3,3,N). Thus s alsoCURRENTatENTRY, incompatible with targetownR44. No physical execution past the earlierR14 failure is claimed.',target_white_obligations=[dict(ID='firstA_common_b',cell=b,local=lb,owner=o.describe('F',14)),dict(ID='old_U_exitbud_s',cell=s,local=ls,owner=o.describe('F',44))],all2_complete_pre_entry_fields=controls,genuine_cycle_transfer='In the33-cell completefield, originalU east2,1 R7 dies at finalU ownL13/global175 and2,0 R8 dies at ownL14/global176. Global183 rebirth at2,1 is a NEW finalU R21 identity. OrdinaryC count is2 after one foreign; no prefirstforeign exact-four age theorem is transported.',finite_reached_prefix_proxy=pieces,all_closed_proxy_pair_checks=pairs,finite_reached_prefix_OPEN_simple=True,unread_extension_qualification='32-cell board reaches target and realM11, but first fails proposedF atL12 due unread3,5. Adding exactly that previouslyunreadBLACK yields33-cell board reachingR14. These are DISTINCT completefields; no retcon to a fixed32-cell trajectory. Neither completes secondF.',not_claimed=['No completed secondforeign erosion-positive here.','No other secondF/Q/B gate or alltwoC classification.','No arbitrary firstU-family tails/longer prefirstA prefix extension.','No global proxy simplicity theorem or foreign-count fuel.','No physical ant termination after candidate-word failure.'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'second_F_N2_gate.json').write_text(json.dumps(out,indent=2)+'\n');print('Unbounded2C secondF3,3 gate: genuine firstforeign commonR8 b2,4 CURRENT by S/E/N support; targetR14WHITE conflict. Real32/33 completefields reachgate; firstphysicalfail12/14 distinguished. Sourceeastpair real L175/176, rebirthR183.')
