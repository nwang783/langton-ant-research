"""Reader-independent F3,-4 gate blocked after C1,one/twoD,selectedD.
No returned-word premise, no source-free atomic-C-to-foreign assumption.
"""
from pathlib import Path
from collections import Counter
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};VEL=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def derive(w):
 p=(0,0);h=0;par=set();req={};rd={};first={}
 for t,ch in enumerate(w):
  initial=(ch=='L')^(p in par)
  if p in req and req[p]!=initial:return dict(feasible=False,tick0=t,cell=p,first_read=first[p])
  if p not in req:req[p]=initial;first[p]=[t,ch]
  rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L' else 1))%4;p=add(p,VEL[h])
 return dict(feasible=True,requirements=req,reads=rd,parity=par,endpoint=[*p,h])
MIN=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text())['slots']
allmins=[]
for gi in(0,1,4,5,6,7,8,9):
 for slot in map(tuple,G[gi]['inputs']):
  n=MIN[f'{gi}:{slot}']['certified_minimum_C_age'];assert n>=2
  if n==2:assert gi in(4,5)and slot==(0,3)
  allmins.append(dict(packet=G[gi]['name'],slot=slot,certified_minimum=n))
assert len(allmins)==23
# A final actual C3 is in one of these complete old packet tails.
full_tail_F=[]
for gi in(1,5,6,8,9):
 z=derive(G[gi]['word']+W[4]['word']+M);assert not z['feasible'];full_tail_F.append(dict(full_old_packet=G[gi]['name'],foreign='F',literal_conflict=z))
cu=derive(W[1]['word']+W[3]['word']+M);assert not cu['feasible']
# IMPORTANT regression: raw C alone CAN precede F, so the complete parent
# contexts above cannot be silently replaced by an artificial standalone C.
cf=derive(W[1]['word']+W[4]['word']+M);assert cf['feasible']
rows=[];Eroles=[];Sbound=[];Wqueries=[];lastcore=[]
for k in(1,2):
 cp=(-k-1,-k);T=(-k-1,-k-2);Q=(-k,-k-2);RB=(1-k,-k-1);foreign=(3,-4)
 assert at((2,0),cp,1)==T and at((2,1),cp,1)==Q and at((1,2),cp,1)==RB
 src=derive(W[1]['word']);assert src['endpoint']==[0,1,3]
 for tag,slot in((T,(2,0)),(Q,(2,1)),(RB,(1,2))):assert src['reads'][slot][-1][1]=='R'
 parents=[]
 for gi in(1,5):
  ep=tuple(G[gi]['endpoint'][:2]);dh=G[gi]['endpoint'][2];parent=sub((-k,-k),rot(ep,1));assert(1+dh)%4==0
  full=derive(G[gi]['word']);assert full['feasible']
  for tag in(T,Q,RB):
   slot=rot(sub(tag,parent),-1);assert slot in set(map(tuple,G[gi]['outputs']))and full['reads'][slot][-1][1]=='R'
  # The full source is DC orVC, first tail only; base/C1 starts clock-1.
  parents.append(dict(full_packet=G[gi]['name'],entry=[*parent,1],C1_entry=[*cp,1],C1_exit=[-k,-k,0],full_source_entry_C_clock=-1,C1_entry_C_clock=-1,C1_exit_C_clock=0))
 # Q's only full-age2 consumer is V/VC upper; its W1 head is too low.
 for gi in(4,5):
  p=sub(Q,rot((0,3),3));assert p[1]==Q[1]<2
  Wqueries.append(dict(k=k,tag=Q,consumer=G[gi]['name'],slot=[0,3],pose=[*p,3],source_full_age=2,selected_D_clock=1,why='W1 heads after selectedD have y>=2'))
 # S2 first consumers of T/Q end no higher than tag. Remaining C3 drops1,
 # and real complete-tail/foreign + C/U rules force an E D/V dropping1 more.
 for label,tag in(('T',T),('Q',Q)):
  for gi in(0,4,7):
   for slot in map(tuple,G[gi]['inputs']):
    p=sub(tag,rot(slot,2));ep=at(tuple(G[gi]['endpoint'][:2]),p,2);assert ep[1]<=tag[1]
    assert ep[1]-2<foreign[1]
    Sbound.append(dict(k=k,tag_label=label,tag=tag,consumer_base=G[gi]['name'],input_slot=slot,entry=[*p,2],S_base_exit=ep,maximum_possible_foreign_y=ep[1]-2,required_foreign_y=foreign[1],why='one remaining S-to-E C plus mandatory first E D/V'))
 # Hierarchical CURRENT lock: prove T, thenQ, then k2 exitbudR.
 held=set();labels=[('T',T),('Q',Q)]+([('R_exit',RB)]if k==2 else[])
 for label,tag in labels:
  for gi in(0,4,7):
   ctx=derive(G[gi]['word']+M)['requirements']
   for slot in map(tuple,G[gi]['inputs']):
    p=sub(tag,rot(slot,1));ep=at(tuple(G[gi]['endpoint'][:2]),p,1);hits=sorted(held&{at(z,p,1)for z in ctx});minimum=MIN[f'{gi}:{slot}']['certified_minimum_C_age'];sol=[]
    if(sum(p)+1)%2:why='wrong_active_sector'
    elif minimum>4:why='true_input_full_age4_below_minimum5'
    elif hits:why='would_touch_or_retire_previously_proved_CURRENT_cohort_tag'
    else:
     dx=foreign[0]-ep[0];down=ep[1]-foreign[1]
     if ep==foreign:sol.append(dict(d=0,v=0,u=0,allowed_last=[G[gi]['name']]if gi in(4,7)else[]))
     else:
      for v in range(max(down+1,0)):
       d=down-v;rest=dx-d-3*v
       if rest<0 or rest%4:continue
       u=rest//4;last=[a for a,n in(('D',d),('V',v),('U',u))if n and a in('V','U')];sol.append(dict(d=d,v=v,u=u,allowed_last=last))
     assert all(not z['allowed_last']for z in sol),(k,label,gi,slot,ep,sol)
     why='no_exact_E_zero_run_endpoint_with_actual_last_V_U'
    Eroles.append(dict(k=k,tag_label=label,tag=tag,prior_CURRENT_tags=sorted(held),consumer=G[gi]['name'],input_slot=slot,full_input_minimum=minimum,consumer_entry=[*p,1],endpoint=ep,current_contacts=hits,E_run_solutions=sol,reason=why))
  held.add(tag)
 # Actual last plainV/U before F necessarily has one held tag in its core.
 for gi,tag in((4,Q if k==1 else RB),(7,T if k==1 else Q)):
  p=sub(foreign,rot(tuple(G[gi]['endpoint'][:2]),1));slot=rot(sub(tag,p),-1);before=derive(G[gi]['word']);assert tag in held and slot in K and before['requirements'][slot]is True
  t,ch=before['reads'][slot][0];assert ch=='L'
  lastcore.append(dict(k=k,last_old_packet=G[gi]['name'],entry=[*p,1],same_original_CURRENT_tag_in_entryK=tag,local_core_cell=slot,first_RAW_tick0=t,first_RAW_read_number1=t+1,why='A current ordered residual cannot already be in a later old entry core; any prior marker-only core absorption was a first full consumer already excluded.'))
 rows.append(dict(k=k,actual_prior_DC_VC_choices=parents,actual_following_N_run='D'*k,selected_D_entry=[0,0,0],foreign=[3,-4,1],genuine_first_C_cohort=dict(T=T,Q=Q,exitbud=RB),first_consumer_clock_bounds=dict(T='at least selectedDclock2, atomic ENTRY maturity3',Q='at least selectedDclock1, full-produced minimum2',exitbud='at least selectedDclock3, actual C EXIT maturity3'),proved_CURRENT_at_foreign=sorted(held),returned_reader_NOT_USED=True))
assert len(Eroles)==40 and len(Sbound)==32 and len(Wqueries)==4 and len(lastcore)==4
D=[GP,QP,R/'audits/dcuv_count5_replay/queries.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Reader-independent F(3,-4,E) impossible at selectedDclock3 when actual first C1 of a genuine DC/VC parent is followed by one or two N D packets before selectedD(D/DC). Sequential current T/Q/exitbud cohort locks prevent every actual lastV/U entrycore. Applies to D30 andC75 source frames without changing contact ownership. No postforeign maturity or source-free raw-C/foreign shortcut.',two_exact_older_C_cohort_interfaces=rows,all23_complete8_input_minima=allmins,five_COMPLETE_old_C_tail_to_F_conflicts=full_tail_F,atomic_C_to_U_conflict=cu,standalone_raw_C_to_F_negative_scope_control=dict(literally_feasible=True,warning='RawC+F is feasible; only the five completeG8 parent-tail conflicts justify no immediateF after actual lastC3.'),all32_S2_consumer_vertical_budget_obligations=Sbound,all4_Q_age2_W_consumer_cone_failures=Wqueries,all40_E3_hierarchical_current_cohort_roles=Eroles,all4_LAST_V_U_entry_core_clashes=lastcore,E_role_counts=dict(Counter(z['reason']for z in Eroles)),dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'F_C_cohort_lock.json').write_text(json.dumps(o,indent=2)+'\n');print('F3,-4 k1/k2 cohort lock:40 E roles,32 S budgets,4W cones,4 real last-core clashes; rawCF scope countercontrol retained.')
