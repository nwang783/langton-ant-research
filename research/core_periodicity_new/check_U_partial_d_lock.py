"""Exact partial-cohort locking, using future center geometry, not a word cap."""
from pathlib import Path
from fractions import Fraction
import json,collections,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';J=json.loads(GP.read_text());G=J['geometry'];IDS=[0,1,4,5,6,7,8,9]
P={(-1,1),(-1,2),(0,2)};d=(0,3);goal_start=(-1,-1);goal_exit=(-1,7)
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def base(a,p,h):
 A=add((2*p[0],2*p[1]),rot((-1,-1),h));v=(2,2)if a in[0,1]else(2,6)if a in[4,5,6]else(0,8);return A,add(A,rot(v,h))
rows=[]
for a in IDS:
 for h in range(4):
  for si,i in enumerate(G[a]['inputs']):
   p=sub(d,rot(i,h));r=dict(packet=a,pose=[*p,h],input_slot=si)
   if(sum(p)+h)%2:r['reason']='wrong_sector'
   else:
    ctx={add(p,rot(z[:2],h))for z in G[a]['requirements']};hit=sorted(ctx&P)
    if hit:r.update(reason='protected_a_q_c_complete_context',hits=hit)
    else:
     A,B=base(a,p,h);v=sub(B,A);axis=0 if v[0]else 1;t=Fraction(goal_exit[axis]-A[axis],v[axis]);assert 0<=t<=1
     assert tuple(Fraction(A[k])+t*v[k]for k in range(2))==goal_exit
     assert goal_exit!=goal_start
     r.update(reason='base_contains_future_goal_U_exit_vertex',base_start=A,base_end=B,consumer_parameter=str(t),goal_U_parameter='1',contact_doubled=goal_exit)
   rows.append(r)
counts=dict(collections.Counter(r['reason']for r in rows));assert counts==dict(wrong_sector=46,protected_a_q_c_complete_context=40,base_contains_future_goal_U_exit_vertex=6)
remaining=[r for r in rows if r['reason']=='base_contains_future_goal_U_exit_vertex']
assert[(r['packet'],r['pose'])for r in remaining]==[(0,[0,4,2]),(4,[0,6,2]),(7,[-1,7,2]),(7,[1,4,3]),(8,[1,4,3]),(9,[1,4,3])]
applications=[]
for a in[7,8,9]:
 p=(-1,1);h=0;O={add(p,rot(o,h))for o in G[a]['outputs']};assert P|{d}<=O
 applications.append(dict(source=a,pose=[-1,1,0],protected_goal_triple=sorted(P),additional_same_source_goal_d=d,derived='d survives to goal, forcing forbidden four same-producer inputs; U-entry suffix supplies simplicity'))
D=[GP,W/'U_entry_simplicity_frozen_20261023_1616/manifest.json',W/'U_max_three_cohort_frozen_20261023_1805/manifest.json']
R=dict(status='AUTHOR_PARTIAL_D_LOCK_PENDING_INDEPENDENT_AUDIT',scope='On an actual complete recurrent-eight factor with simple corrected atomic-center path, a current residual identity at d=(0,3) cannot retire strictly before a future U/UC/UCC at0,N if the three other current goal identities a,q,c survive to that goal. Entry or produced d allowed; no age, b-existence, birth relation or record premise. The generic lock is conditional on simplicity. Its three source-U-family applications are universal via U-entry suffix simplicity.',protected_goal_inputs=sorted(P),locked_goal_input=d,counts=counts,all_92_consumer_alignments=rows,three_universal_source_applications=applications,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_partial_d_lock.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(counts,indent=2))
