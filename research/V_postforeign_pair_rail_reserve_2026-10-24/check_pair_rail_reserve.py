"""Portable original V r/B pair plus C W-rail and bud endpoint reserves. THIRD true ages3/4 only; no age law after first foreign."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('ownership',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(word,p=(0,0,0)):
 pos,h=p[:2],p[2]
 for c in word:h=(h+(1 if c=='R'else-1))%4;pos=add(pos,l.DIRS[h])
 return*pos,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(atom,p):return z(p),z(after(W[atom],p))
from collections import Counter
def raw(tokens):return ''.join(W[a]for a in tokens)
HP=R/'core_periodicity_new/V_C_same_heading_exclusion_frozen_20261023_2043/literal_helpers.py';hn={'__file__':str(HP)};exec(HP.read_text(),hn);G=hn['G'];IDS=hn['IDS'];chords=hn['chords'];contact=hn['contact'];place=hn['place'];edge=hn['edge'];r=(0,0);B=(1,0);C=(2,1);bud=(2,2)
# All old-source B input losses under held r, using PLAIN actual RAW only.
Bqueries=[];Bgates=[]
for src in(4,5,6):
 for co in(0,4,7):
  for h in range(4):
   for slot,q in enumerate(G[co]['inputs']):
    p=sub(B,l.rot(tuple(q),h));ctx={place(z[:2],p,h)for z in G[co]['requirements']};row=dict(actual_old_source_full=G[src]['name'],consumer=G[co]['name'],input_slot0=slot,input_cell=q,pose=(*p,h))
    if(sum(p)+h)%2:row['reason']='wrong_sector'
    elif r in ctx:row['reason']='held_r_complete_context_contact'
    elif any(contact(*old,*new)for old in chords(src)for new in chords(co,p,h)):row['reason']='forbidden_actual_source_chord_contact'
    else:
     assert(co,p,h,slot)in((0,(1,-1),0,0),(4,(1,-3),0,0),(7,(2,-2),0,1),(7,(2,-4),0,2));row['reason']='one_of_four_geometric_B_gates_WITH_upper_U_RETAINED';Z=(3,-1);L0=(1,1);E0=(-1,-1);bridge=[Z,L0,E0];new=chords(co,p,h)[0];prefix=(new[0],Z)
     for i,(u,v)in enumerate(zip(bridge,bridge[1:])):
      expected=[[str(Z[0]),str(Z[1])]]if i==0 else[];assert contact(*prefix,u,v)==expected
      for j,(x,y)in enumerate(chords(src)):
       assert contact(x,y,u,v)==([[str(E0[0]),str(E0[1])]]if i==1 and j==0 else[])
     aa={'D':(1,0),'V':(0,1),'U':(0,0)}[G[co]['name']];openconst=(4-aa[0],1-aa[1]);close=(aa[0],aa[1]-1);assert tuple(openconst[k]+close[k]for k in(0,1))==(4,0)
     row.update(SAME_r_B_bridge=bridge,first_consumer_bridge_contact=Z,consumer_prefix=prefix,actual_first_B_input_read=o.describe(G[co]['name'],l.trace(W[G[co]['name']]+l.M)['first'][tuple(q)][1]),open_turn={'K_coefficient_pi_over4':[2,0],'constant_pi_over4_beta':openconst},closing_turn_pi_over4_beta=close,Jordan_total_clock='K+2=4 or -4; unique nonnegativeK2',upper_U_old_min5_NOT_applied_after_FOREIGN=(co==7 and slot==2));Bgates.append(row)
    Bqueries.append(row)
assert len(Bqueries)==96 and Counter(x['reason']for x in Bqueries)=={'wrong_sector':48,'held_r_complete_context_contact':36,'one_of_four_geometric_B_gates_WITH_upper_U_RETAINED':12}
# No ordinary r loss can happen with B still current at its ENTRY.
RJ=json.loads((R/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/V_parallel_reproductive_supply.json').read_text());rlocks=[]
for gate in RJ['r_retirement_cases']:
 co=gate['consumer'];p=tuple(gate['head'][:2]);h=gate['head'][2];ctx={place(z[:2],p,h):bool(z[2])for z in G[co]['requirements']};ins={place(z,p,h)for z in G[co]['inputs']};core={place(z,p,h)for z in l.K};assert B in ctx and B not in ins and(not ctx[B]or B in core)
 rlocks.append(dict(actual_source=G[gate['source']]['name'],consumer=G[co]['name'],pose=(*p,h),B_is_true_input=False,B_ENTRY_core=B in core,B_required_before_WHITE=not ctx[B],conclusion='r cannot lose CURRENT in this atom if SAME B is CURRENT at atom ENTRY; simultaneous pair loss is excluded too.'))
assert len(rlocks)==9
# Genuine C and bud current before foreign3, all full source tails explicit.
CP=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';COUNT={tuple(map(int,line.split()[:8]))for line in CP.read_text().splitlines()};mp={a:i for i,a in enumerate(IDS)};young=[];sourcefacts=[]
for src in(4,5,6):
 tr=l.trace(G[src]['word']);facts=[]
 for cell,tick in((r,4),(B,9),(C,7),(bud,16)):
  assert list(cell)in G[src]['outputs']and tr['last'][cell]==('R',tick);facts.append(dict(SAME_original_cell=cell,source_actual_final_R_tick0=tick,birth_read_number1=tick+1,own_C_tails_preserve_same_R=True,preFOREIGN_current_proof='signed2036 r first loss5'if cell==r else'signed2043 B first loss4'if cell==B else'new exact age0..3 COUNT5 queries'))
 sourcefacts.append(dict(actual_full_source=G[src]['name'],full_ENTRY_clock=0,full_completion_clock=G[src]['name'].count('C'),facts=facts))
 for cell in(C,bud):
  for n in range(4):
   h=(-n)%4
   for co in IDS:
    for slot,q in enumerate(G[co]['inputs']):
     p=sub(cell,l.rot(tuple(q),h));key=(mp[src],mp[co],*p,h,*cell,n);why='sector'if(sum(p)+h)%2 else'signed_COUNT5'if key in COUNT else'UNEXCLUDED';assert why!='UNEXCLUDED';young.append(dict(source=G[src]['name'],SAME_cell=cell,exact_full_ENTRY_age=n,consumer=G[co]['name'],input_slot0=slot,pose=(*p,h),key=key,reason=why))
assert len(young)==552 and Counter(q['reason']for q in young)=={'sector':276,'signed_COUNT5':276}
# C=(2,1) W first loss with B current: six sectors, one actual old-V
# chord contact, one before-WHITE conflict with SAME B. No age after A.
Cports=[];budports=[]
for co in(0,4,7):
 for slot,q in enumerate(G[co]['inputs']):
  p=sub(C,l.rot(tuple(q),3));new=chords(co,p,3)[0];row=dict(consumer=G[co]['name'],input_slot0=slot,pose=(*p,3),actual_first_input_read=o.describe(G[co]['name'],l.trace(W[G[co]['name']]+l.M)['first'][tuple(q)][1]))
  if(sum(p)+3)%2:row['reason']='sector'
  elif p==(3,2):
   assert co==7;hit=contact(*chords(4)[0],*new);assert hit;row.update(reason='loss_atom_contacts_old_V_chord',actual_consumer_chord=new,exact_source_chord_contact=hit)
  else:
   assert(co,p)==(7,(4,1));local=l.rot(sub(B,p),-3);f=l.trace(W['U']+l.M)['first'][local];assert f[0]=='R';row.update(reason='SAME_current_B_before_WHITE_conflict',B_consumer_local=local,actual_B_first_read=o.describe('U',f[1]))
  Cports.append(row)
  pp=sub(bud,l.rot(tuple(q),3));ep=after(W[G[co]['name']],(*pp,3));assert ep[0]<=2;budports.append(dict(consumer=G[co]['name'],input_slot0=slot,pose=(*pp,3),actual_RAW_exit=ep,actual_first_input_read=o.describe(G[co]['name'],l.trace(W[G[co]['name']]+l.M)['first'][tuple(q)][1]),exit_x_at_most2=True))
assert len(Cports)==8 and Counter(p['reason']for p in Cports)=={'sector':6,'loss_atom_contacts_old_V_chord':1,'SAME_current_B_before_WHITE_conflict':1}and len(budports)==8
# Exact oldV true-preA3/4 FIRST THIRD contact cases, no word tree.
AP=R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json';angles=[x for x in json.loads(AP.read_text())['all831_conditional_preFOREIGN_old_source_angle_interfaces']if x['old_source']=='V'and x['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age']in(3,4)];assert len(angles)==66
old=chord('V',(0,0,0));a,b=old;u=sub(b,a);boxes=[];poses=[];rows=[]
def ctx(cells,tr,p,h,packet):
 out=[]
 for cell in cells:
  loc=l.rot(sub(cell,p),-h);first=tr['first'].get(loc);out.append(dict(SAME_cell=cell,local=loc,status='CORE'if loc in l.K else'MISS'if first is None else first[0],first_read=first,canonical_first_read_owner=None if first is None else o.describe(packet,first[1])))
 return out
for angle in angles:
 b1,b2,b3=angle['first'],angle['second'],angle['third'];n=angle['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];K=angle['total_ordinary_C_before_third'];h=angle['third_heading_relative_old'];hA=angle['true_FOREIGN_heading_relative_old'];c,d=chord(b3,(0,0,h));v=sub(d,c);den=det(u,v);assert den
 corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bounds=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)];boxes.append(dict(angle=angle,rational_corners=[[[q.numerator,q.denominator]for q in p]for p in corners],integer_bounds=bounds))
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y-K)%2:continue
   zz=sub(add(c,(2*x,2*y)),a);s,t=Q(det(zz,v),den),Q(det(zz,u),den)
   if not(0<=s<1 and 0<t<=1):continue
   p3=(x,y,h);poses.append(dict(angle=angle,third_pose=p3,old_s=str(s),new_t=str(t)))
   for A in'FQB':
    de=after(raw(A+b1+b2),(0,0,hA));pa=(x-de[0],y-de[1],hA);body=A+b1+b2+b3;tr=l.trace(raw(body)+l.M);atr=l.trace(W[A]+l.M);ctr=l.trace(W[b3]+l.M);pair=[r]if n==4 else[r,B];fa=ctx(pair,atr,pa[:2],hA,A);fe=ctx(pair,ctr,p3[:2],h,b3);row=dict(foreign=A,first=b1,second=b2,third=b3,true_preFOREIGN_age=n,totalK=K,foreign_pose=pa,third_pose=p3,FOREIGN_r_or_pair_before_facts=fa,third_r_or_pair_before_facts=fe)
    if not tr['feasible']:row.update(classification='immutable_local_literal_conflict',conflict=tr)
    elif any(q['status']in('R','CORE')for q in fa):row['classification']='preFOREIGN_same_r_B_before_state_conflict'
    else:
     assert all(q['status']=='MISS'for q in fa)
     if any(q['status']in('R','CORE')for q in fe):row['classification']='postFOREIGN_r_persistence_candidate_core_or_WHITE'if n==4 else'postFOREIGN_r_B_pair_candidate_core_or_WHITE'
     else:
      assert n==3 and K==3 and b1 in'DVU'and b2 in'DVU';initial=ctx([C,bud],atr,pa[:2],hA,A);row['FOREIGN_C_bud_before_facts']=initial
      if any(q['status']in('R','CORE')for q in initial):row['classification']='preFOREIGN_same_C_bud_before_state_conflict'
      else:
       assert all(q['status']=='MISS'for q in initial);ce=ctx([C],ctr,p3[:2],h,b3)[0]
       if ce['status']in('R','CORE'):row.update(classification='pinned_original_C_W_rail_candidate_conflict',third_C_before_fact=ce)
       else:
        assert b3=='U'and p3==(3,2,3);be=ctx([bud],ctr,p3[:2],h,b3)[0];assert be['status']=='R';row.update(classification='same_bud_W_exit_monotonicity_candidate_WHITE',third_bud_before_fact=be,all_loss_exits_x_at_most2_but_candidate_x3=True)
    rows.append(row)
assert len(rows)==495 and Counter(rw['true_preFOREIGN_age']for rw in rows)=={3:441,4:54}
assert Counter(x['classification']for x in rows)=={'immutable_local_literal_conflict':6,'preFOREIGN_same_r_B_before_state_conflict':18,'postFOREIGN_r_B_pair_candidate_core_or_WHITE':255,'postFOREIGN_r_persistence_candidate_core_or_WHITE':54,'preFOREIGN_same_C_bud_before_state_conflict':6,'pinned_original_C_W_rail_candidate_conflict':129,'same_bud_W_exit_monotonicity_candidate_WHITE':27}
paths=[HP,CP,AP,R/'third_ordinary_local_interface_2026-10-24/manifest.json',R/'audits/third_local_interface_independent.json',R/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',R/'audits/check_V_parallel_reproductive_supply_independent.json',R/'core_periodicity_new/V_C_same_heading_exclusion_frozen_20261023_2043/manifest.json',R/'audits/check_V_C_same_heading_exclusion_independent.json',R/'V_r_postforeign_contact_clock_2026-10-24/manifest.json',R/'audits/check_V_r_postforeign_clock_independent.json',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_PORTABLE_V_PAIR_RAIL_RESERVE_AND_THIRD_N3_N4_CLOSURE_PENDING_REVIEW',portable_pair_lemma='Assume genuine preFOREIGN V original r andB CURRENT before FIRSTforeign and completeFOREIGN context MISSES both. If true source-toFOREIGN age>=3, any first later CURRENT loss of either identity forces a proxy contact by completion of that loss atom. Earliest loss cannot be r with B CURRENT (all9 plain r gates), nor simultaneous; if B first, held r+B bridge gives TOTAL K2, earlier than FOREIGN. Thus both persist to ENTRY of global first-contact atom. No old input-age law afterFOREIGN; upper-U B gate retained.',all96_plain_RAW_B_loss_roles=Bqueries,all12_plain_B_bridge_gates=Bgates,all9_plain_r_gates_require_B_already_absent=rlocks,portable_C_W_rail_lemma='With genuine original C=(2,1) CURRENT at a W zeroC run start and SAME B held through the run, first C loss either contacts old creating-V chord in that atom or conflicts with B BLACK beforeWHITE. Eight plain input roles, no postA age.',all8_plain_C_W_first_loss_roles=Cports,portable_bud_W_endpoint_lemma='With genuine original bud(2,2) CURRENT at start of W zeroC run, no completed loss can precede a later cut whose headx>=3: all eight possible input consumers exitx<=2 and W ordinary x increments are strictly negative. CORE absorption counted at earlier RAW exit.',all8_bud_W_input_exit_bounds=budports,all3_actual_preFOREIGN_source_full_tag_births=sourcefacts,all552_C_and_bud_age0_through3_queries=young,exact_young_query_counts=dict(Counter(q['reason']for q in young)),third_application_scope='Only global FIRST contact by THIRD ordinary RAW with outgoing PREforeign oldV source at true age3 or4. Source fullV/VC/VCC retained. True ages0/1/2 remain outside this theorem; no overall third simplicity.',all66_signed_angle_cases=angles,all66_exact_contact_boxes=boxes,all165_contact_pose_labels=poses,all495_FOREIGN_typed_mask_cases=rows,exact_disjoint_classification=dict(Counter(rw['classification']for rw in rows)),conclusion='All old-V THIRD true-preFOREIGN n3/n4 source cases excluded without endpoint words:54 n4 r-clock/core cuts;441 n3 cases exhaust local/preA conflicts, portable r/B persistence, pinned-C W rail, or bud exact westward exits. Old source ages0/1/2 remain open separately.',no_postFOREIGN_maturity_or_full_cohort_seal_or_unexecuted_consumer_tail=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'pair_rail_reserve.json').write_text(json.dumps(out,indent=2)+'\n');print('Portable r/B first-loss pairK2, upperU retained; C W rail +bud x bound. OldV THIRD n3/n4:495 exact masks, all excluded; no endpoint word enumeration.')
