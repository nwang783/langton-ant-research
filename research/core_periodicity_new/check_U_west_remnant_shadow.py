"""A protected three-output remnant keeps source w current after cycle break.
No age, intact-cycle, first-break, head-box or word-search premise.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];IDS=[0,1,4,5,6,7,8,9]
P={(1,0),(1,1),(0,0)};w=(0,1);source_base_A=(-1,-1);source_base_B=(-1,7);hitpoint=(-1,3)
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
   p=sub(w,rot(i,h));r=dict(packet=a,pose=[*p,h],input_slot=si)
   if(sum(p)+h)%2:r['reason']='wrong_sector'
   else:
    C={add(p,rot(z[:2],h))for z in G[a]['requirements']};hits=sorted(C&P)
    if hits:r.update(reason='protected_west_pair_or_r_complete_context',hits=hits)
    else:
     A,B=base(a,p,h);assert B==hitpoint
     assert tuple(Fraction(source_base_A[k])+Fraction(1,2)*(source_base_B[k]-source_base_A[k])for k in range(2))==hitpoint
     r.update(reason='base_exit_in_strict_interior_of_creating_U_base',base_start=A,base_end=B,contact_doubled=hitpoint,source_U_parameter='1/2',consumer_base_parameter='1')
   rows.append(r)
counts=dict(Counter(r['reason']for r in rows));assert counts==dict(wrong_sector=46,protected_west_pair_or_r_complete_context=40,base_exit_in_strict_interior_of_creating_U_base=6)
remaining=[r for r in rows if r['reason']=='base_exit_in_strict_interior_of_creating_U_base'];assert[(r['packet'],r['pose'])for r in remaining]==[(0,[0,2,2]),(1,[0,2,2]),(4,[0,4,2]),(5,[0,4,2]),(7,[-1,5,2]),(8,[-1,5,2])]
source_rows=[]
for a in[7,8,9]:
 assert P|{w}<=set(map(tuple,G[a]['outputs']))
 source_rows.append(dict(source=a,pose=[0,0,0],protected_three_outputs=sorted(P),forced_surviving_w=w))
goal_rows=[]
for a in[7,8,9]:
 p=(0,2);h=2;I={add(p,rot(i,h))for i in G[a]['inputs']};assert P<=I
 rq=rot(sub(w,p),-h);assert rq==(0,1);assert next(z for z in G[a]['requirements']if tuple(z[:2])==rq)[2]is False
 goal_rows.append(dict(goal=a,pose=[0,2,2],source_triple_in_goal_coordinates=sorted(rot(sub(q,p),-h)for q in P),w_goal_local=rq,entry_requirement=False))
D=[GP,W/'U_entry_simplicity_frozen_20261023_1616/manifest.json',Path(__file__).resolve()]
R=dict(status='AUTHOR_WEST_REMNANT_SHADOW_PENDING_INDEPENDENT_AUDIT',scope='Any actual complete-eight creating U-family0,N: while its original west output pair(1,0),(1,1) and r=(0,0) survive, its original w=(0,1) cannot retire. No intact-cycle assumption; an earlier right cycle breaker is allowed. Thus no later U-family(0,2,S) can consume exactly those retained three source IDs. Universal via source-U suffix simplicity; no age or historical-component bound.',counts=counts,all_92_w_consumers=rows,sources=source_rows,goals=goal_rows,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_west_remnant_shadow.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(counts,indent=2))
