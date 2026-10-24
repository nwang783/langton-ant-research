"""All-age two-cohort exclusion from one compulsory spare and simple centers.
Exact92-placement geometry; no HB, age kernel, path depth or node budget.
"""
from pathlib import Path
from fractions import Fraction
import json,hashlib,collections
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';J=json.loads(GP.read_text());G=J['geometry'];K=set(map(tuple,J['core']));IDS=[0,1,4,5,6,7,8,9]
P=set(map(tuple,G[7]['inputs']));w=(0,4)
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def base_chord(a,p,h):
 kind=0 if a in[0,1]else 4 if a in[4,5,6]else 7
 c=add((2*p[0],2*p[1]),rot((-1,-1),h));v=(2,2)if kind==0 else(2,6)if kind==4 else(0,8)
 return c,add(c,rot(v,h))
SA,SB=base_chord(8,(1,5),2);assert SA==(3,11)and SB==(3,3)
rows=[]
for a in IDS:
 for h in range(4):
  for slot in G[a]['inputs']:
   v=rot(slot,h);p=w[0]-v[0],w[1]-v[1];r=dict(packet=a,head=[*p,h],input_slot=slot)
   if(sum(p)+h)%2:r['reason']='wrong_sector'
   else:
    C={add(p,rot(q[:2],h))for q in G[a]['requirements']}|{add(p,rot(q,h))for q in K};hits=sorted(C&P)
    if hits:r.update(reason='protected_final_input_context',hits=hits)
    else:
     A,B=base_chord(a,p,h);u=sub(SB,SA);v=sub(B,A);d=cross(u,v);rel=sub(A,SA)
     assert d
     s=Fraction(cross(rel,v),d);t=Fraction(cross(rel,u),d)
     assert 0<s<1 and 0<=t<=1
     q=(Fraction(SA[0])+s*u[0],Fraction(SA[1])+s*u[1])
     r.update(reason='nonadjacent_source_base_contact',source_parameter=str(s),consumer_parameter=str(t),contact_doubled=[str(x)for x in q],consumer_base_start=A,consumer_base_end=B)
   rows.append(r)
cnt=dict(collections.Counter(r['reason']for r in rows));assert cnt==dict(wrong_sector=46,protected_final_input_context=40,nonadjacent_source_base_contact=6)
cs=[r for r in rows if r['reason']=='nonadjacent_source_base_contact']
assert[(r['packet'],r['head'])for r in cs]==[(0,[1,4,3]),(1,[1,4,3]),(4,[3,4,3]),(5,[3,4,3]),(7,[4,5,3]),(8,[4,5,3])]
source_rows=[]
for a in[8,9]:
 O={add((1,5),rot(o,2))for o in G[a]['outputs']};assert w in O and P- {(-1,2)}<=O and(-1,2)not in O
 assert tuple(rot(sub(w,(1,5)),-2))==(1,1)
 source_rows.append(dict(packet=a,head=[1,5,2],protected_co_born_goal_inputs=sorted(P-{(-1,2)}),older_fifth_input=[-1,2],compulsory_spare=w,source_spare_output_slot=[1,1],source_base_start=SA,source_base_end=SB,C_tails=G[a]['name'].count('C')))
 assert G[a]['name'].count('C')>=1
for a in[7,8,9]:
 assert P==set(map(tuple,G[a]['inputs']))
 assert next(q for q in G[a]['requirements']if tuple(q[:2])==w)[2]is False
 assert all(tuple(q[:2])not in P for q in G[a]['requirements']if q[3]<11)
D=[GP,W/'u_middle_origin_frozen_20261023_1013/manifest.json',W/'U_white_shadow_frozen_20261023_1709/manifest.json',W/'U_entry_simplicity_frozen_20261023_1616/manifest.json',Path(__file__).resolve()]
O=dict(status='AUTHOR_EXACT_TWO_COHORT_EXCLUSION_PENDING_INDEPENDENT_AUDIT',scope='Actual complete recurrent-eight factor with simple corrected atomic center. UC/UCC(1,5,S) cannot supply the four stated final U identities while q predates the source. No age, HB, root-component or record assumption. No U count or capture.',target_inputs=sorted(P),source_rows=source_rows,compulsory_goal_white=w,counts=cnt,all_consumer_alignments=rows,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/UC_older_four_cohort_simple_exclusion.json').write_text(json.dumps(O,indent=2)+'\n');print(json.dumps(cnt,indent=2))
