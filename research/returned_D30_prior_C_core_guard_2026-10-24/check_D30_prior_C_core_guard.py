"""Any actual C immediately before selected D is incompatible with D30.
No returned simplicity, postforeign age law, or generic prefix enumeration.
"""
from pathlib import Path
from fractions import Fraction as F
cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
def point_meet(a,b,c,d):
 u=sub(b,a);v=sub(d,c);w=sub(c,a);den=cross(u,v);assert den
 return F(cross(w,v),den),F(cross(w,u),den)
from collections import Counter
from itertools import permutations
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';CP=R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json';XP=R/'returned_D_entry_controls_2026-10-24/D_entry_controls.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];C=json.loads(CP.read_text());X=json.loads(XP.read_text());M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};VEL=((0,1),(1,0),(0,-1),(-1,0));mp={a:i for i,a in enumerate('DCVUFQB')};b=(2,0);bp=(3,1);g=(0,0);g1=(0,1);gm=(-1,-1);young_deleted=(0,-1);previous_bud=(1,-1)
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def derive(w,stop=False):
 p=(0,0);h=0;par=set();rq={};rd={};first={}
 for t,ch in enumerate(w):
  initial=(ch=='L')^(p in par)
  if p in rq and rq[p]!=initial:
   if stop:return dict(tick=t,cell=p,first=first[p],required_initial=initial)
   raise AssertionError((t,p))
  if p not in rq:rq[p]=initial;first[p]=[t,ch]
  rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return rq,par,p,h,rd
AT=[]
for i in range(4):
 rq,par,ep,dh,rd=derive(W[i]['word']);ctx,_,_,_,_=derive(W[i]['word']+M);outs={q for q in rq if rq[q]^(q in par)}-{at(z,ep,dh)for z in K};assert all(q[1]>=0 and sum(q)>=0 for q in outs);AT.append(dict(name='DCVU'[i],endpoint=ep,turn=dh,outputs=outs,context=ctx))
def endpoints(identity,target,foreign,case):
 out=[]
 for gi in(0,4,7):
  for slot in map(tuple,G[gi]['inputs']):
   p=sub(identity,rot(slot,1));ep=at(tuple(G[gi]['endpoint'][:2]),p,1);dx=target[0]-ep[0];down=ep[1]-target[1];sol=[];allowed=('V','U')if foreign in('F','Q')else('U',)
   for v in range(max(down+1,0)):
    d=down-v;rem=dx-d-3*v
    if rem<0 or rem%4:continue
    u=rem//4;last=[a for a,c in(('D',d),('V',v),('U',u))if c and a in allowed];sol.append(dict(d=d,v=v,u=u,allowed_last=last))
   assert ep!=target and all(not z['allowed_last']for z in sol),(identity,target,gi,slot,sol)
   out.append(dict(case=case,identity=identity,clearer=G[gi]['name'],input_slot=slot,entry=[*p,1],endpoint=ep,foreign_entry=target,all_E_run_counts=sol))
 return out

import importlib.util
OP=R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py';spc=importlib.util.spec_from_file_location('own',OP);own=importlib.util.module_from_spec(spc);spc.loader.exec_module(own)
prior_C=(-1,0);prior_h=1;hole=(-1,1);foreign=(3,-4);q01=(0,1)
cr,_,ce,ch,creads=derive(W[1]['word']);assert at(ce,prior_C,prior_h)==(0,0) and(prior_h+ch)%4==0
assert creads[(-1,0)]==[[1,'L']] and at((-1,0),prior_C,prior_h)==hole
old_C_start=center(prior_C,prior_h);old_C_end=center((0,0),0);old_D_end=center((1,1),0)
assert(old_C_start,old_C_end,old_D_end)==((-3,1),(-1,-1),(1,1))
fr=derive(W[4]['word'])[0];rq,_,_,_,rd=derive(W[4]['word']+W[2]['word']+M);loc=rot(sub(hole,foreign),-1)
assert loc not in fr and loc not in K and rq[loc]is True and rd[loc][0]==[69,'L']
endrows=[]
for tag in(previous_bud,b,bp):endrows.extend(endpoints(tag,foreign,'F',30))
# True source-D input is first physically deleted by the actual post-D atom.
post=[]
for i in range(4):
 rr=derive(W[i]['word'])[4];assert rr[(-1,0)]==[[1,'L']]
 post.append(dict(actual_post_D_atom='DCVU'[i],entry=[1,1,0],deleted_global_input=q01,delete_tick0=1,delete_read_number1=2,C_entry_clock=0))
# No FULL source born clock0/N can output q01. Source D/DC also do not output it.
full=[]
for gi in (0,1,4,5,6,7,8,9):
 outs=set(map(tuple,G[gi]['outputs']));assert all(q[1]>=0 for q in outs) and all(q[0]>=0 for q in outs if q[1]==0)
 assert q01 not in outs if gi in(0,1)else True
 full.append(dict(packet=G[gi]['name'],all_outputs_have_nonnegative_y=True,height0_outputs_have_nonnegative_x=True,N0_heads_after_selected_D_have_x_y_at_least1=True))
MIN=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text())['slots']
prec=[]
for gi,p,slot,minimum in((0,(0,2),(0,1),3),(4,(0,4),(0,3),2),(7,(-1,5),(-1,4),5)):
 assert at(tuple(G[gi]['endpoint'][:2]),p,2)==(-1,1) and at(slot,p,2)==q01
 assert MIN[f'{gi}:{slot}']['certified_minimum_C_age']==minimum
 assert MIN[f'{gi+1}:{slot}']['certified_minimum_C_age']==minimum
 prec.append(dict(preceding_actual_base=G[gi]['name'],containing_full_packet_choices=[G[gi]['name'],G[gi+1]['name']],pose=[*p,2],true_input_slot=slot,deleted_global_input=q01,full_entry_clock=2,certified_minimum=minimum,latest_possible_producer_full_entry_clock=2-minimum,exclusion='postdeletion producer cannot be older; all full birthclock0 origins absent'))
# Only remaining actual predecessor of S-entry(-1,1) would be C_W(0,1),
# below W1 head y>=2. This also treats internal tail ownership literally.
assert at((0,1),(0,1),3)==(-1,1) # actual C_W headstep(-1,0)
raw=[];roles=[]
for i in range(4):
 qr,pa,en,dh,rr=derive(W[i]['word']);ctx=derive(W[i]['word']+M)[0];fresh={q for q,z in rr.items()if z[-1][1]=='R'};ek={at(q,en,dh)for q in K};raw.append(dict(name='DCVU'[i],endpoint=en,turn=dh,context=ctx,fresh=fresh,exitK=ek,reads=rr))
 for slot in fresh:
  p=sub(hole,slot);assert not(p[0]>=0 and p[1]>=0)
  wp=sub(hole,rot(slot,3))
  if wp[1]>=2:assert i==3 and(slot,wp)in(((-1,2),(1,2)),((-1,3),(2,2)))
cu=derive(W[1]['word']+W[3]['word']+M,True);assert isinstance(cu,dict)
for h in(2,1):
 held={previous_bud,b,bp}
 for a in raw:
  for slot in sorted(a['fresh']):
   p=sub(hole,rot(slot,h));en=at(a['endpoint'],p,h);hits=sorted(held&{at(z,p,h)for z in a['context']});core=slot in a['exitK']
   if(sum(p)+h)%2:why='wrong_active_sector'
   elif hits:why='current_three_D_buds_complete_context'
   elif h==1 and a['name']=='C':why='E_C4_completion_after_foreign3'
   elif h==1:
    assert(a['name'],slot,p)in(('D',(2,1),(-2,3)),('V',(2,3),(-4,3)),('U',(1,4),(-5,2)))and en==(-1,2)and core;why='E_base3_CORE_to_three_bud_trap'
   elif(a['name'],slot,p)in(('D',(2,0),(1,1)),('V',(2,2),(1,3)),('U',(1,3),(0,4))):
    assert center(en,2)==old_D_end;why='old_D_exit_corrected_center_repeated'
   elif(a['name'],slot,p)in(('D',(0,0),(-1,1)),('C',(0,0),(-1,1)),('V',(0,2),(-1,3)),('U',(-1,3),(-2,4))):
    assert center(en,(h+a['turn'])%4)==old_C_start;why='actual_prior_C_entry_corrected_center_repeated'
   elif(a['name'],slot,p)in(('D',(1,1),(0,2)),('V',(1,3),(0,4)),('U',(0,4),(-1,5))):why='direct_source_D_input_01_rebirth_deadline_lock'
   elif a['name']=='V' and slot==(0,0) and p==(-1,1):
    assert center(p,h)==(-1,3) and center(en,h)==(-3,-3);why='strict_midpoint_crossing_of_actual_prior_C_chord'
   elif a['name']=='U' and slot==(0,0) and p==(-1,1):
    assert center(p,h)==(-1,3) and center(en,h)==(-1,-5);why='crosses_old_D_start_at_later_chord_strict_midpoint'
   else:
    assert a['name']=='C'and slot==(0,2)and p==(-1,3)and en==(-1,2)and core;why='S_C3_CORE_to_three_bud_trap'
   roles.append(dict(heading=h,atom=a['name'],last_R_slot=slot,last_R_tick0=a['reads'][slot][-1][0],is_exit_core=core,pose=[*p,h],endpoint=en,held_tag_contacts=hits,reason=why))
assert len(roles)==72
trap=[]
for i,tag in((0,previous_bud),(2,b),(3,bp)):
 p=(-1,2);loc=rot(sub(tag,p),-1);qr,_,_,_,rr=derive(W[i]['word']+M);assert qr[loc]is False
 trap.append(dict(next_old_atom='DCVU'[i],genuine_current_tag=tag,first_owner=own.describe('DCVU'[i],rr[loc][0][0])))
from collections import Counter
D=[GP,QP,OP,R/'audits/dcuv_count5_replay/queries.json',R/'returned_D_Jordan_ancestry_horizon_2026-10-24/manifest.json',R/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',Path(__file__).resolve()]
assert point_meet(old_C_start,old_C_end,(-1,3),(-3,-3))==(F(1,2),F(1,2))
assert point_meet(old_C_end,old_D_end,(-1,3),(-1,-5))==(F(0),F(1,2))
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='D30 with ANY actual E-to-N C immediately before selectedD, arbitrary containing DC/VC/UC/VCC/UCC role and earlier history/connector. Actual C core deletion, true D-input rebirth deadline lock with correct Vupper2 and DC/VC/UC roles,72 core-inclusive repairs, exact old C/D chord contacts and triple-bud trap. No old V or U cohort permanence beyond ordinary buds, no postforeign age law.',actual_prior_C=dict(entry=[*prior_C,prior_h],exit=[0,0,0],source_fullpacket_tail_role='actual first or second final C; no standalone fullpacket or invented K'),source_core_deletion=dict(local_cell=[-1,0],global_cell=hole,own_C_tick0=1,own_C_read_number1=2),actual_past_chords=dict(C=[old_C_start,old_C_end],D=[old_C_end,old_D_end]),future_required_BLACK=dict(combined_tick0=69,canonical_owner=own.describe('V',13),outside_foreign_entry_K=True,foreign_RAW_misses=True),four_actual_first_post_D_01_deletions=post,all8_full_birthclock0_no_01_output_cones=full,all3_possible_S_predecessor_input_deadlines=prec,all24_held_bud_endpoint_obligations=endrows,all72_S_E_final_R_CORE_and_residual_roles=roles,role_counts=dict(Counter(x['reason']for x in roles)),three_bud_trap=trap,first_W_C_to_U_literal_conflict=cu,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'D30_prior_C_core_guard.json').write_text(json.dumps(o,indent=2)+'\n');print('Any actual prior C D30:72 core-safe repair origins blocked by source01 lock, exact old C/D contacts and three-bud trap.')
