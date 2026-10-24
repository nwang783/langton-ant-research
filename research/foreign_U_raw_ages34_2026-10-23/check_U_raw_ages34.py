"""Exact source-deletion and recycled-input descent at RAW erosion ages3/4.
No prefix scan, guessed radius, first-center-contact premise, or age iteration.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)};VEL=((0,1),(1,0),(0,-1),(-1,0))
B=(0,-1);C=(-1,0);GUARDS={B,C}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def derive(w):
 p=(0,0);h=0;par=set();req={};reads={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par);assert p not in req or req[p]==b;req[p]=b;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return req,par,p,h,reads
_,_,_,_,ur=derive(W[3]['word']);deletions=[]
for q in sorted(GUARDS):
 assert ur[q][-1][1]=='L'and q[1]<4 and q[1]-q[0]<5
 deletions.append(dict(cell=q,last_source_U_read=ur[q][-1],N_y_upper_test=q[1],W_H_upper_test=q[1]-q[0]))
# Actual atomic masks, including C15. At clock3, an S C is the C3 producer;
# at clock4 an E C is C4. Their fresh outputs must not be omitted.
AT=[]
for i,gi in((0,0),(2,4),(3,7)):
 rq,_,ep,dh,rd=derive(W[i]['word']+M);_,_,raw_ep,raw_dh,_=derive(W[i]['word'])
 AT.append(dict(name='DCVU'[i],word=W[i]['word'],outputs=set(map(tuple,G[gi]['outputs'])),inputs=set(map(tuple,G[gi]['inputs'])),endpoint=raw_ep,turn=raw_dh))
rq,par,ep,dh,rd=derive(W[1]['word']);cr,_,_,_,_=derive(W[1]['word']+M);assert not({q for q,b in cr.items()if b}-K)
co={at(q,ep,dh)for q in K}^par^K;assert co=={(1,2),(2,0),(2,1)}
AT.append(dict(name='C',word=W[1]['word'],outputs=co,inputs=set(),endpoint=ep,turn=dh))
for a in AT:assert all(q[1]>=0 and sum(q)>=0 for q in a['outputs'])
role_rows=[]
for h in(2,1):
 for q in sorted(GUARDS):
  for a in AT:
   rq,_,_,_,rd=derive(a['word']+M)
   for slot in sorted(a['outputs']):
    p=sub(q,rot(slot,h));hits=sorted({at(z,p,h)for z in rq}&L);out=at(a['endpoint'],p,h)
    if(sum(p)+h)%2:why='wrong_active_sector'
    elif hits:why='held_original_L_in_complete_context'
    elif h==2:
     assert q==C and a['name']=='U'and slot==(-1,2)and p==(-2,2)
     assert slot in a['inputs']and rq[slot]is True and rd[slot][:2]==[(13,'L'),(21,'R')]
     why='recycled_input_requires_strictly_earlier_black_identity_at_same_cell'
    else:
     raise AssertionError(('Unexpected E fresh-output origin',q,a['name'],slot,p))
    role_rows.append(dict(heading=h,guard_cell=q,producer=a['name'],fresh_output_slot=slot,producer_pose=[*p,h],base_endpoint=[*out,(h+a['turn'])%4],held_star_context_hits=hits,reason=why))
assert len(role_rows)==76
assert Counter(r['reason']for r in role_rows if r['heading']==2)=={'wrong_active_sector':18,'held_original_L_in_complete_context':19,'recycled_input_requires_strictly_earlier_black_identity_at_same_cell':1}
assert Counter(r['reason']for r in role_rows if r['heading']==1)=={'wrong_active_sector':20,'held_original_L_in_complete_context':18}
# At clock4 the relevant new N producers are plain D/V/U. A positive C tail
# would complete after the foreign clock; E-C4 outputs are already in the table.
Nrows=[]
for q in(B,C):
 for a in AT:
  if a['name']=='C':continue
  rq,_,_,_,_=derive(a['word']+M)
  for slot in sorted(a['outputs']):
   p=sub(q,slot);hits=sorted({at(z,p,0)for z in rq}&L);out=at(a['endpoint'],p,0)
   if sum(p)%2:why='wrong_active_sector'
   elif hits:why='held_original_L_in_complete_context'
   else:assert out[1]>=2;why='N_birth_completes_at_y_at_least2_above_every_remaining_N_RAW_gate'
   Nrows.append(dict(guard_cell=q,producer=a['name'],fresh_output_slot=slot,producer_pose=[*p,0],base_endpoint=[*out,0],held_star_context_hits=hits,reason=why))
assert len(Nrows)==32 and sum(r['reason'].startswith('N_birth')for r in Nrows)==4
P=R/'foreign_U_star_predecessors_2026-10-23/foreign_U_star_predecessors.json';PD=json.loads(P.read_text());gates={}
for r in PD['rows']:
 if r['reason']=='necessary_interface_not_asserted_attained'and r['raw_retirements']and r['foreign_pose'][2]in(0,1):gates[(r['foreign'],*r['foreign_pose'])]=r
assert len(gates)==24
out=[]
for key,r in gates.items():
 name=r['foreign'];p=tuple(r['foreign_pose'][:2]);h=r['foreign_pose'][2];j='DCVUFQB'.index(name);rq,_,_,_,rd=derive(W[j]['word']+M);core={at(q,p,h)for q in K};I={at(q,p,h)for q,b in rq.items()if b}-core
 if h==1:
  assert p[0]<=0;guards=I&GUARDS;assert guards
  chosen=sorted(guards)[0];why='B_or_C_has_no_first_fresh_residual_identity_through_clock3'
  age=3
 else:
  assert p[1]<0;guards=I&{B,C};assert guards;chosen=sorted(guards)[0];why='no_B_or_C_birth_before_clock4_and_N_birth_ends_above_foreign';age=4
 local=rot(sub(chosen,p),-h);assert rq[local]is True and local not in K
 out.append(dict(foreign=name,pose=[*p,h],C_age=age,chosen_same_source_deleted_guard=chosen,guard_foreign_local=local,guard_first_full_context_read=rd[local][0],reason=why,original_star_RAW_retirements=r['raw_retirements'],marker_spillover=r['marker_spillover']))
assert Counter(r['C_age']for r in out)=={3:15,4:9}
assert all(r['chosen_same_source_deleted_guard']in(B,C)for r in out)
D=[GP,QP,P,R/'foreign_U_star_predecessors_2026-10-23/manifest.json',R/'foreign_U_star_age2_2026-10-23/manifest.json',R/'foreign_U_marker_clocks_2026-10-23/manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='No first foreign RAW retirement of a genuine original U-star identity at source-entry C age3 or4 after an uninterrupted complete-eight interval. Same-source deletion guards and recycled-input earliest-rebirth descent, independent of first-center-contact. Together with signed ages0..2 and marker clocks, any first foreign original-star RAW or marker-only effect requires at least5Cs. Not physical fine-time whiteness, attainment at5, postforeign permanence or all-age exclusion.',same_source_U_deletions=deletions,S_and_E_atomic_fresh_output_rows=role_rows,N_clock4_fresh_output_rows=Nrows,all_remaining_RAW_erosion_gates_at_clocks3_4=out,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'U_raw_ages34.json').write_text(json.dumps(o,indent=2)+'\n');print('76 S/E atomic output roles +32 N roles;15 age3 and9 age4 RAW erosion gates excluded by actual source deletions and recycled-input descent.')
