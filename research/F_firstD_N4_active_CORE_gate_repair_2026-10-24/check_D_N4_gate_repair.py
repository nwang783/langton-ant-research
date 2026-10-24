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
# Do not restore original143d's unconditional pair claim. Restore these
# source-history-sensitive two N4 labels by new guards on all3 actual gates.
G=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9)
JO=dict((tuple(r[:3]),r[3])for r in json.loads((R/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json').read_text()));assert JO[4,1,2]>=3 and JO[7,0,3]>=4
M=(2,0);FT={(-3,-1),(-2,-1)};F47=(-2,-1);R30=(-3,-3);hole=(-1,-2);FV=[(-7,-3),(-1,-1)]
epF=after(W['F']);rf=add(epF[:2],l.rot(R30,2));hh=add(epF[:2],l.rot(hole,2));ft=l.trace(W['F']);assert ft['last'][rf]==('R',30)and ft['last'][hh]==('L',49)
assert list(rf)in l.literal_geometry(W['F'])['outputs']and hole not in l.K and hole not in l.trace(W['D']+l.M)['first']
# Hole(-1,-2) may be repaired, but no early actual full producer can
# furnish an age-eligible external input at either true readerclock4.
zero=[]
for i in IDS:
 O=[tuple(p)for p in G[i]['outputs']];assert min(p[1]for p in O)>=0 and min(p[0]for p in O)>=-2
 zero.append(dict(actual_full_packet=G[i]['name'],all_outputs=O,minimum_N_output_y=min(p[1]for p in O),minimum_W_output_y_offset=min(p[0]for p in O)))
assert all(hole not in map(tuple,G[i]['outputs'])for i in(0,1))
readers=[]
for a,p,slot,typ in [('V',(-2,-4,0),(1,2),4),('U',(-1,-5,0),(0,3),7)]:
 assert rel(hole,p)==slot and slot not in l.K
 f=l.trace(W[a]+l.M)['first'][slot];assert f[0]=='L';mn=JO[typ,*slot];assert 2<mn
 readers.append(dict(loss_RAW=a,pose=p,ENTRY_C_clock=4,hole=hole,true_input_local=slot,actual_first=f,owner=o.describe(a,f[1]),actual_produced_input_minimum=mn,earliest_possible_actual_full_producer_ENTRY_clock=2,maximum_produced_age=2,scope='Actual selectedD→this BASE factor parsesG8 with real precedingF and SAME actual nextM11 supplied by finalactorV/U. Forehole was physicalWHITE at selectedfactorENTRY, not entryresidual. SourceownD/DC O missesit; laterN0 fullheads y>=1 and Olocaly>=0; W1 fullheads y>=2 and Orotatedy>=-2, so neither clock0 nor1 can supplyy=-2. Every replacement birth is allowed but too young for this actual true input.'))
# R30 at the loss-D entry: first CURRENT loss must be a plain true input,
# including marker-only absorption. No FOREIGN age/minimum is applied.
Dloss=(-2,-2,0);assert rel(R30,Dloss)in l.K
rrows=[]
for K in range(5):
 h=(-K)%4
 for a in'DVU':
  tr=l.trace(W[a]+l.M)
  for slot,(c,t)in tr['first'].items():
   if c!='L'or slot in l.K:continue
   p=(*sub(R30,l.rot(slot,h)),h);ep=after(W[a],p);r=dict(consumer=a,ENTRY_C_clock=K,pose=p,input=slot,owner=o.describe(a,t),RAW_EXIT=ep)
   if(sum(p[:2])+h)%2:why='sector'
   elif K==0:
    assert p[1]<1;why='initial_N0_head_below_sourceD_EXIT_y1'
   elif K==1:
    assert p[1]<2;why='initial_W1_head_below_y2'
   elif K==2:
    co=contact(*FV,*chord(a,p));assert co;r['actual_earlier_FOREIGN_proxy_contact']=co;why='S2_already_contacts_actual_F_piece_or_entry'
   elif K==3:
    if ep[0]+1>Dloss[0]:why='remaining_E_to_N_C_then_nonnegative_x_cannot_reach_lossD'
    else:
     assert ep==(-3,-4,1)and ep[0]+1==Dloss[0]
     # Any E base or N D/V would add positive x. Only N U adds x0,y4.
     assert Dloss[1]-ep[1]==2 and (Dloss[1]-ep[1])%4!=0
     why='exact_remaining_x_forces_empty_E_and_only_N_U_but_needed_y2_not_multiple4'
   else:
    assert K==4 and ep[1]>Dloss[1];why='N4_RAW_exit_y_above_lossD_and_N_cannot_descend'
   r['route']=why;rrows.append(r)
assert len(rrows)==40
rguard=dict(SAME_FOREIGN_output=R30,actual_F_cell=rf,last_R_tick0=30,last_R_read1=31,actual_lossD_pose=Dloss,current_tag_local_at_lossD=rel(R30,Dloss),all40_first_loss_clock_input_roles=rrows,statement='Before N4 D(-2,-2,N), SAME F30 remainsCURRENT if executed F+ordinary proxy prefix is SIMPLE through that entry. EarlyN/W consumers unreachable. EveryS2 sector-valid loss contacts realF already. E3 lossRAW exits at(-3,-4,E),(-2,-3,E) or(-1,-4,E): after remainingC eitherxalreadytoo large, or exactxforces zeroE and onlyN-U4vertical while neededy2. N4losses exit above target. MarkerCORE absorption counted, no old8 maturity applied toR30. It therefore cannot occupy lossD ENTRYCORE.')
# Reconstruct the sourceD slice of the rejected pair-first-loss table. At
# these final N4 target heads the3 equal-exit roles are honestly retained,
# not wrongly cut by y. They must occur immediately before finalactor.
old=json.loads((R/'original_F_piece_firstpost_DC_2026-10-24/F_piece_DC.json').read_text());pair=[r for r in old['all128_coupled_F46_F47_source_current_first_loss_rows']if r['source']=='D'];assert len(pair)==64
openloss=[r for r in pair if r['route'].startswith('N0_unreachable_or_N4')];assert len(openloss)==3
assert{(r['consumer'],tuple(r['pose']))for r in openloss}=={('D',(-2,-2,0)),('V',(-2,-4,0)),('U',(-1,-5,0))}
for r in openloss:assert tuple(r['RAW_EXIT'])==(-1,-1,0)and tuple(r['F_tag'])==F47
origopen=json.loads((R/'original_F_piece_firstpost_DC_2026-10-24/partial_scope_qualification.json').read_text())['all3_OPEN_N4_restoration_residues'];twos=[r for r in origopen if r['original_row']['first_post_RAW']=='D'];assert len(twos)==2
joins=[]
for row in twos:
 target=tuple(row['original_row']['pose']);a=row['original_row']['actor'];assert target==(-1,-1,0)and a in'VU'
 assert rel(F47,target)in l.K
 for loss in openloss:
  x=loss['consumer'];p=tuple(loss['pose']);assert after(W[x],p)==target
  # All local interfaces remain real positives. Their missing oldF/source
  # boundary, not the immediate pair, causes the newly proved contradiction.
  assert l.trace(W[x]+W[a]+l.M)['feasible']
  guard=rguard if x=='D'else next(z for z in readers if z['loss_RAW']==x)
  joins.append(dict(original_OPEN_label=row,actual_immediate_loss_RAW=x,loss_pose=p,loss_RAW_EXIT_equals_final_actor_ENTRY=True,zeroC_N_continuation_must_be_empty='D/V/U each strictly raisesy, so same N head admits no intervening ordinary RAW',local_pair_colour_feasible=True,new_actual_ancestry_guard=guard))
assert len(joins)==6
D=[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json',R/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/manifest.json',R/'audits/check_RAW_G8_base_cut_bridge_independent.json',R/'original_F_piece_firstpost_DC_2026-10-24/manifest.json',R/'original_F_piece_firstpost_DC_2026-10-24/partial_scope_qualification_manifest.json',R/'audits/check_F_DC_partial_qualification_independent.json'];assert all(p.exists()for p in D)
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Separate repair of ONLY sourceD→V/U(-1,-1,N) at postFIRSTF C4 under GLOBAL-first-contact simple-prefix hypothesis and actual ordinary suffix/finalM11. Actual lossRAW D/V/U activeCORE interfaces are retained and individually blocked by source-history guards. No original143d universal pair claim or arbitrary-tail simplicity.',FOREIGN_hole=dict(post_EXIT_cell=hole,actual_F_cell=hh,last_L_tick0=49,last_L_read1=50,physical_WHITE_at_sourceD_ENTRY=True,outside_ENTRY_CORE=True),all8_actual_full_output_N_W_lower_bounds=zero,all2_true_reader_hole_produced_age_guards=readers,F30_CURRENT_endpoint_guard=rguard,all64_original_sourceD_pair_first_loss_rows=pair,all3_active_CORE_equal_exit_gates=openloss,all6_typed_gate_by_final_actor_closures=joins,CORE_safeguard='The original F47 lifetime MAY be aliveCORE after the hypothetical lossRAW and physically deleted at finalactor read2; this local mechanism is not denied. Instead lossD cannot start with SAME CURRENTF30 in its CORE, and lossV/U cannot supply their OTHER external true input from oldFWHITEhole with a sufficiently old actualG8 output. Every physical CORE Rrepair is retained: at those trueinputs the cell lies outside ENTRYCORE and must have a genuine fullO owner. No FOREIGN-output age is used.',original_full143d_universal_pair_claim_still_NOT_PASSED=True,no_blanket_PAIR_CURRENT_at_equal_EXIT_head_asserted=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'D_N4_gate_repair.json').write_text(json.dumps(out,indent=2)+'\n');print('Separate firstD N4 repair:40 SAMEF30 loss roles+2 physicalWHITEhole age guards close6 actual gate/actor combinations; local positives retained.')
