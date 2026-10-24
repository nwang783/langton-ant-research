"""58 of 60 D-source returned-first-contact labels: genuine cut/bud ancestry.
No returned simplicity, postforeign age law, or generic prefix enumeration.
"""
from pathlib import Path
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
# First ACTUAL post-D atom, internal C1 of DC or next full old base, at(1,1,N).
# Complete D-to-foreign is impossible, so such an old atom exists in every case.
first=[]
for i in range(4):
 _,_,_,_,rd=derive(W[i]['word']);assert rd[(-1,-1)]==[[2,'L']]and rd[(-1,0)]==[[1,'L']]and rd[(2,0)][-1]==[8,'R'];first.append(dict(atom='DCVU'[i],actual_entry=[1,1,0],C_clock=0,g00_deletion=[2,'L'],g01_deletion=[1,'L'],fresh_common_bud=bp,bud_birth=[8,'R']))
# Previous REAL atomic exit at oldD entry: all four literal atom types yield
# exactly beta=(1,-1). C is a containing-full-source tail, never a ghost packet.
prev=[]
for a in AT:
 h=(-a['turn'])%4;p=tuple(-z for z in rot(a['endpoint'],h));local=(1,2)if a['name']=='C'else{'D':(2,0),'V':(2,2),'U':(1,3)}[a['name']];assert at(local,p,h)==previous_bud
 prev.append(dict(previous_actual_atom=a['name'],entry=[*p,h],exit=[0,0,0],exit_C_clock=0,fresh_exit_bud=previous_bud,fullproducer_tail_clock_rule='signed1325 actual atomic exit, all15 containing source roles'))
# g00/g01 absence at clocks0/1. Heads N0 x>=1,y>=1; W1 H>=1.
assert g[1]<1 and g[1]-g[0]<1
# For g01 at clock0: only possible y1 head is(1,1), and every y0 output hasx>=0.
for a in AT:assert all(q[0]>=0 for q in a['outputs']if q[1]==0)
# Later gm=(-1,-1) rebirth while source b stays current:38 S/E roles.
# Source D or DC genuinely deleted gm and (0,-1), at ticks2/read3 and3/read4.
for gi in (0,1):
 _,_,_,_,rd=derive(G[gi]['word'])
 assert rd[gm]==[[2,'L']] and rd[young_deleted]==[[3,'L']]
MIN=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text())['slots']
assert MIN['4:(1, 2)']['certified_minimum_C_age']==3
assert MIN['7:(0, 3)']['certified_minimum_C_age']==5
rebirth=[];Eorig=[]
for h in (2,1):
 for a in AT:
  for slot in sorted(a['outputs']):
   p=sub(gm,rot(slot,h));ep=at(a['endpoint'],p,h);hits=sorted({b}&{at(z,p,h) for z in a['context']});detail=None
   if (sum(p)+h)%2:why='wrong_active_sector'
   elif hits:why='current_original_D_common_bud_in_complete_context'
   elif h==1 and a['name']=='C':why='E_C4_completion_after_foreign_clock3'
   elif h==2:
    if p==(-1,-1):
     assert a['name'] in ('V','U') and slot==(0,0) and center(p,h)==(-1,-1);why='S2_origin_entry_repeats_old_D_start'
    elif p==(0,0):
     assert a['name']=='U' and slot==(1,1) and center(p,h)==(1,1);why='S2_origin_entry_repeats_old_D_exit'
    elif a['name']=='V':
     assert p==(1,1) and slot==(2,2) and at((1,2),p,h)==young_deleted
     why='S2_origin_selected_input_was_deleted_and_minimum3'
     detail=dict(input_slot=[1,2],deleted_cell=young_deleted,certified_minimum=3,maximum_post_deletion_age=2)
    else:
     assert a['name']=='U' and p==(0,2) and slot==(1,3) and at((0,3),p,h)==young_deleted
     why='S2_origin_upper_input_was_deleted_and_minimum5'
     detail=dict(input_slot=[0,3],deleted_cell=young_deleted,certified_minimum=5,maximum_post_deletion_age=2)
   elif a['name']=='V' and slot==(0,1):
    assert p==(-2,-1) and ep==(1,-2);why='only_E3_gm_origin_endpoint';Eorig.append((a['name'],slot,p,ep))
   elif a['name']=='U' and slot==(-1,2):
    assert p==(-3,-2) and at((-1,2),p,h)==gm
    _,_,_,_,rd=derive(W[3]['word']);assert rd[(-1,2)]==[[13,'L'],[21,'R']]
    why='cannot_be_earliest_rebirth_same_true_input_requires_earlier_residual'
    detail=dict(input_slot=[-1,2],input_tick0=13,input_read_number1=14,output_tick0=21,output_read_number1=22)
   else:
    assert (a['name'],slot,p,ep) in (('V',(2,1),(-2,1),(1,0)),('U',(1,2),(-3,0),(1,0)))
    assert center(ep,h)==(1,1);why='E3_origin_exit_repeats_old_D_exit'
   rebirth.append(dict(heading=h,atom=a['name'],output=slot,pose=[*p,h],endpoint=ep,current_source_bud_hits=hits,reason=why,detail=detail))
assert len(rebirth)==38 and len(Eorig)==1
# Exact E3 first-clearer endpoint lemma, any common/exit bud origin.
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
# Exact clock1 connector exhaustion for the three BLACK common-bud returnedV
# ports; finite head equations, no guessed prefix length or search radius.
shortset={z['short_raw_word']for z in X['six_actual_controls']};portal=[]
for name,target in(('F',(-3,4)),('Q',(-5,4)),('B',(-6,3))):
 reached=[];rejected=[]
 for nD in range(target[1]-1):
  total=target[1]-2-nD
  for v in range(total+1):
   d=total-v;rem=1+nD-d-3*v-target[0]
   if rem<0 or rem%4:continue
   u=rem//4
   # These lengths come from the exact portal displacement, not a depth cap.
   for pword in sorted(set(''.join(z)for z in permutations('D'*d+'V'*v+'U'*u))):
    if not pword:continue
    if pword[-1]not in(('V','U')if name!='B'else('U',)):continue
    if pword[0]=='U':rejected.append(dict(nN_D=nD,W_word=pword,reason='actual_C15_to_U28_literal_conflict'));continue
    ns='D'*(1+nD)+'C'+pword+name+'V';assert ns in shortset;reached.append(ns)
 portal.append(dict(foreign=name,entry=[*target,3],exact_short_connector_words=reached,other_count_words_rejected_by_C_U=rejected))
assert{z for x in portal for z in x['exact_short_connector_words']}==shortset
rows=[];ep_rows=[];zero_head=[]
for ix,row in enumerate(C['old_source_contact_cases']):
 if row['source_atom']!='D':continue
 n=row['source_to_foreign_C_age'];j=mp[row['foreign']];i=mp[row['returned_atom']];ap=tuple(row['foreign_pose'][:2]);ah=row['foreign_pose'][2];br,_,_,_,rd=derive(W[j]['word']+W[i]['word']+M)
 def val(q):return br.get(rot(sub(q,ap),-ah))
 guard=None;read=None
 if n==2:
  assert val(previous_bud)is False;guard=previous_bud;why='actual_previous_atomic_exit_bud_age2_before_WHITE'
 elif n<=1:
  if val(g)is True:
   assert rot(sub(g,ap),-ah)not in K;guard=g;why='first_post_D_deleted_00_has_no_N0_or_W1_rebirth'
  elif val(b)is False:
   assert n==1;guard=b;why='genuine_D_R8_common_bud_current_age1_before_WHITE'
  elif n==0 and val(g1)is True:
   guard=g1;why='first_post_D_deleted_01_has_no_clock0_N_rebirth'
  elif n==0:
   assert row['returned_atom']=='V';assert ap in((4,4),(4,6),(3,7));dx=ap[0]-1;dy=ap[1]-1;sol=[]
   for d in range(dx+1):
    v=dx-d;rem=dy-d-3*v
    if rem<0 or rem%4:continue
    u=rem//4;last=[a for a,c in(('D',d),('V',v),('U',u))if c and(a in('V','U')if row['foreign']!='B'else a=='U')];sol.append(dict(d=d,v=v,u=u,allowed_last=last))
   if ap in ((4,6),(3,7)):
    if ap==(4,6):
     assert sol==[dict(d=2,v=1,u=0,allowed_last=['V'])];forced='DDDVQV';badtick=113
    else:
     assert sol==[dict(d=0,v=2,u=0,allowed_last=[]),dict(d=2,v=0,u=1,allowed_last=['U'])];forced='DDDUBV';badtick=133
    bad=derive(''.join(W[mp[z]]['word'] for z in forced)+M,True)
    assert bad['tick']==badtick and bad['cell']==(1,2)
    why='clock0_forced_word_actual_deleted_core_conflict'
   else:
    assert all(not z['allowed_last'] for z in sol),(ix,ap,sol);bad=None
    why='clock0_head_count_has_no_actual_allowed_last_foreign_packet'
   zero_head.append(dict(case=ix,all_N_run_counts=sol,actual_forced_word_conflict=bad))
  else:
   assert row['returned_atom']=='V'and row['returned_pose']==[-1,0,1];assert(row['foreign'],ap)in(('F',(-3,4)),('Q',(-5,4)),('B',(-6,3)));why='six_attained_D_entry_connectors_have_complete_finite_no_U_entry_predecessor_closure'
 else:
  assert n==3 and ah==1
  if val(bp)is False:
   guard=bp;ep_rows.extend(endpoints(bp,ap,row['foreign'],ix));why='first_actual_post_D_common_R8_bud_E3_endpoint_guard'
  elif val(b)is False:
   guard=b;ep_rows.extend(endpoints(b,ap,row['foreign'],ix));why='original_D_R8_common_bud_E3_endpoint_guard'
  elif ix in (6,54):
   assert val(gm) is True and row['foreign']=='F' and ap in ((2,-5),(3,-4));guard=gm
   # These endpoint obligations prove b cannot retire ANYWHERE on the old
   # route to this target, even though the future before-mask does not need it white.
   ep_rows.extend(endpoints(b,ap,row['foreign'],ix))
   assert Eorig[0][-1]==(1,-2)
   # From this sole possible E3 origin, exact E-run displacement cannot have
   # a V/U last base as required before F. No length/radius truncation.
   ex,ey=Eorig[0][-1];dx=ap[0]-ex;down=ey-ap[1];solutions=[]
   for v in range(max(down+1,0)):
    d=down-v;rem=dx-d-3*v
    if rem<0 or rem%4:continue
    u=rem//4;last=[a for a,c in (('D',d),('V',v),('U',u)) if c and a in ('V','U')]
    solutions.append(dict(d=d,v=v,u=u,allowed_last=last))
   assert all(not z['allowed_last'] for z in solutions)
   zero_head.append(dict(case=ix,sole_gm_origin=Eorig[0],all_E_run_counts=solutions))
   why='spatially_unretirable_D_bud_plus_deleted_minus11_rebirth_guard'
  else:
   assert ix in (15,30);why='OPEN_necessary_clock3_geometry_not_attained'
 if guard is not None:
  local=rot(sub(guard,ap),-ah);read=rd[local][0];assert local not in K
 rows.append(dict(case=ix,foreign=row['foreign'],foreign_pose=row['foreign_pose'],returned_atom=row['returned_atom'],returned_pose=row['returned_pose'],source_to_foreign_C_clock=n,contact=row['contact'],exclusion=why,chosen_genuine_guard=guard,actual_combined_first_read=read))
counts=Counter(x['exclusion'] for x in rows);assert len(rows)==60
assert counts=={'actual_previous_atomic_exit_bud_age2_before_WHITE':15,'first_post_D_deleted_00_has_no_N0_or_W1_rebirth':15,'genuine_D_R8_common_bud_current_age1_before_WHITE':3,'first_post_D_deleted_01_has_no_clock0_N_rebirth':3,'clock0_forced_word_actual_deleted_core_conflict':2,'clock0_head_count_has_no_actual_allowed_last_foreign_packet':1,'six_attained_D_entry_connectors_have_complete_finite_no_U_entry_predecessor_closure':3,'first_actual_post_D_common_R8_bud_E3_endpoint_guard':9,'original_D_R8_common_bud_E3_endpoint_guard':5,'spatially_unretirable_D_bud_plus_deleted_minus11_rebirth_guard':2,'OPEN_necessary_clock3_geometry_not_attained':2}
assert len(ep_rows)==128
D=[GP,QP,CP,XP,R/'returned_D_entry_controls_2026-10-24/manifest.json',R/'returned_D_entry_controls_2026-10-24/read_index_convention_erratum_manifest.json',R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact_manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',R/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'audits/dcuv_count5_replay/queries.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='58 of60 D-source immediate returned-atom chronological-first-contact labels excluded under actual U-entry complete-eight then firstforeign. Two clock3 geometries remain necessary-only and unattained. Uses genuine previous-exit bud and source/first-successor last-R tags, actual source deletions, exact head equations and finite reverse ancestry closure of attained D-entry controls. No returned simplicity, later-contact, secondforeign or universal seven-word extension.',read_index_convention='All literal ticks are zero-based, physical read numbers are one-based. A context read beyond RAW belongs to the actual following word, not an executed extra marker.',all60_D_source_rows=rows,classification_counts=dict(counts),four_actual_first_post_D_atom_interfaces=first,four_literal_previous_atomic_exit_bud_frames=prev,all38_late_deleted_minus11_output_alignments=rebirth,all128_E3_clearer_endpoint_obligations=ep_rows,exact_clock0_and_gm_origin_head_obligations=zero_head,three_exact_clock1_returnV_portal_exhaustions=portal,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in D})
(H/'D_source_join.json').write_text(json.dumps(o,indent=2)+'\n');print('58 excluded, two necessary-only D-source labels:',dict(counts))
