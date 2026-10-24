"""Immediate UC creator cannot repair its retired upper slot for D30.
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
OP=R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'
spec=importlib.util.spec_from_file_location('ownership',OP);own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
up=(-5,0);uh=1;hole=(-1,1);foreign=(3,-4)
assert at(tuple(G[8]['endpoint'][:2]),up,uh)==(0,0) and (uh+G[8]['endpoint'][2])%4==0
uq=at((-1,2),up,uh);ubud=at((1,3),up,uh)
assert uq==(-3,1) and ubud==(-2,-1)
sourceword=W[3]['word']+W[1]['word'];sr,sp,se,sh,sreads=derive(sourceword)
assert sreads[(-1,4)]==[[29,'L']] and at((-1,4),up,uh)==hole
assert (-1,4) not in {at(q,se,sh) for q in K} and (-1,4) not in set(map(tuple,G[8]['outputs']))
FREQ,_,_,_,FREAD=derive(W[4]['word']);CREQ,_,_,_,CREAD=derive(W[4]['word']+W[2]['word']+M);local=rot(sub(hole,foreign),-1)
assert local not in FREQ and local not in K and CREQ[local] is True and CREAD[local][0]==[69,'L']
assert own.describe('VC',13)['owner_read_number1']==14
L={at(q,up,uh)for q in((0,0),(0,1),(1,0),(1,1))};held=L|{uq,ubud,previous_bud,b,bp};assert len(held)==9
endrows=[]
for tag in(previous_bud,b,bp):endrows.extend(endpoints(tag,foreign,'F',30))
assert len(endrows)==24
# Every actual final-R BLACK atomic-cut role, including exit core.
raw=[];roles=[]
for i in range(4):
 rq,par,en,turn,rr=derive(W[i]['word']);ctx=derive(W[i]['word']+M)[0];fresh={q for q,z in rr.items() if z[-1][1]=='R'};ek={at(q,en,turn) for q in K}
 assert all(q[0]>=0 or (i==3 and q in{(-1,2),(-1,3)}) for q in fresh)
 raw.append(dict(name='DCVU'[i],endpoint=en,turn=turn,context=ctx,fresh=fresh,exitK=ek,reads=rr))
# N0 heads have x,y>=0. Negative-x slots need y<0 to hit hole.
for a in raw:
 for slot in a['fresh']:
  p=sub(hole,slot)
  if p[0]>=0 and p[1]>=0:raise AssertionError(('possible_N0',a['name'],slot,p))
# W1 heads have y>=2; only U negative-x slots can reach holey1.
# q slot(-1,2) needs FIRST W head(1,2), immediately after C; C->U fails.
# core slot(-1,3) needs(2,2), impossible since at y2 W starts(1,2) and x never rises.
for a in raw:
 for slot in a['fresh']:
  p=sub(hole,rot(slot,3))
  if p[1]<2:continue
  assert a['name']=='U' and (slot,p) in (((-1,2),(1,2)),((-1,3),(2,2)))
cu=derive(W[1]['word']+W[3]['word']+M,True);assert isinstance(cu,dict)
for h in(2,1):
 for a in raw:
  for slot in sorted(a['fresh']):
   p=sub(hole,rot(slot,h));en=at(a['endpoint'],p,h);hits=sorted(held&{at(q,p,h)for q in a['context']});core=slot in a['exitK']
   if(sum(p)+h)%2:why='wrong_active_sector'
   elif hits:why='genuine_held_UC_star_q_bud_or_three_D_buds_context'
   elif a['name']=='C' and h==1:why='E_C4_completes_after_clock3_foreign'
   elif a['name']=='C':
    assert slot==(0,2) and p==(-1,3) and en==(-1,2) and core;why='S_C3_CORE_repair_forces_E_endpoint_minus1_plus2'
   else:
    assert a['name']=='D' and h==1 and slot==(2,1) and p==(-2,3) and en==(-1,2) and core
    why='E_D3_CORE_repair_forces_E_endpoint_minus1_plus2'
   roles.append(dict(heading=h,atom=a['name'],last_R_slot=slot,last_R_tick0=a['reads'][slot][-1][0],last_R_read_number1=a['reads'][slot][-1][0]+1,is_exit_core=core,pose=[*p,h],endpoint=en,held_contacts=hits,reason=why))
assert len(roles)==72
# ANY next E base from that core endpoint hits a different genuine held bud.
trap=[]
for i,tag in((0,previous_bud),(2,b),(3,bp)):
 p=(-1,2);loc=rot(sub(tag,p),-1);rq,_,_,_,rd=derive(W[i]['word']+M)
 assert rq[loc] is False
 owner=own.describe('DCVU'[i],rd[loc][0][0]);trap.append(dict(next_atom='DCVU'[i],entry=[*p,1],genuine_held_tag=tag,local_cell=loc,first_requirement='WHITE',physical_owner=owner))
# Preserve prescribed constructive near-control, not as a universal exclusion.
m=3;k=4*m-3;ns='UC'+'DC'+'D'*k+'CD'+'U'*m+'CD'+'U'*m+'FV';word=''.join(W[mp[a]]['word']for a in ns)+M;bad=derive(word,True)
assert isinstance(bad,dict) and bad['tick']==445 and bad['cell']==(-1,4)
# First445 reads are actually feasible on a COMPLETE finite board, rest WHITE.
rq,par,en,dh,rd=derive(word[:445]);board={q for q,black in rq.items()if black};initial=sorted(board);p=(0,0);h=0;log=[]
for t,ch in enumerate(word[:445]):
 turn='L' if p in board else'R';assert turn==ch;log.append(dict(tick0=t,read_number1=t+1,cell=p,turn=turn));board.symmetric_difference_update({p});h=(h+(-1 if turn=='L'else 1))%4;p=add(p,VEL[h])
assert p==(-1,4) and p not in board and word[445]=='L'
from collections import Counter
D=[GP,QP,OP,R/'returned_D_Jordan_ancestry_horizon_2026-10-24/manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'core_periodicity_new/U_q_source_history_frozen_20261023_2027/manifest.json',R/'word_stabilization/U_foreign_prefix_bud_cuts_frozen_20261023_2201/manifest.json',R/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Only D30 immediate genuine UC predecessor, arbitrary old-eight connector/earlier history. Deleted true source upper slot needs BLACK before F; all72 final-R repairs INCLUDING EXIT CORE are blocked by genuine current source/D buds. No postforeign input minimum, no all-D30 exclusion.',actual_UC_entry=[*up,uh],selected_D_entry=[0,0,0],source_deletion=dict(global_cell=hole,source_local_cell=[-1,4],owner=own.describe('UC',29)),future_required_BLACK=dict(foreign_local_cell=local,foreign_RAW_misses=True,foreign_entry_K_misses=True,combined_tick0=69,returned_owner=own.describe('V',13)),held_tags=sorted(held),all24_target_bud_endpoint_obligations=endrows,all72_S_E_final_R_CORE_and_residual_repair_roles=roles,role_counts=dict(Counter(z['reason']for z in roles)),three_bud_core_endpoint_trap=trap,first_W_C_to_U_conflict=cu,failed_constructive_UC_entry_history=dict(raw_word=ns,RAW_length=len(word)-11,complete_initial_black_board=initial,initial_mass=len(initial),all445_actual_fine_reads=log,first_failed_read_tick0=445,expected='L',actual='R',cell=[-1,4],creator_original_deletion_tick0=29,returned_V_local_tick0=13,scope='Actual genuine UC-entry old-eight and complete firstF+M prefix; the prescribed returned V FAILS, so no completed-return counterexample.'),dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'D30_UC_deleted_core_guard.json').write_text(json.dumps(o,indent=2)+'\n');print('D30 immediateUC guard:72 core-inclusive last-R roles,24 endpoint guards,3-bud trap; genuine445-read near-control preserved.')
