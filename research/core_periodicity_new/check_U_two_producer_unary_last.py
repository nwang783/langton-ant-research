"""Complete finite two-producer U support assembly, unary latest producer.
No actual-prefix search or general producer-triple recurrence is inferred.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];IDS=[0,1,4,5,6,7,8,9];P=set(map(tuple,G[7]['inputs']));a=(-1,1);q=(-1,2);b=(-1,4);c=(0,2);d=(0,3)
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def cross(p,q):return p[0]*q[1]-p[1]*q[0]
def on(p,a,b):return cross(sub(p,a),sub(b,a))==0 and sum((p[i]-a[i])*(p[i]-b[i])for i in range(2))<=0
def contact(A,B):
 p,q=A;r,s=B;x=cross(sub(q,p),sub(r,p));y=cross(sub(q,p),sub(s,p));u=cross(sub(s,r),sub(p,r));v=cross(sub(s,r),sub(q,r))
 return((x>0>y or y>0>x)and(u>0>v or v>0>u))or any(on(z,*e)for z,e in[(p,B),(q,B),(r,A),(s,A)])
def outputs(a,p,h):return{add(p,rot(o,h)):tuple(o)for o in G[a]['outputs']}
def ctx(a,p,h):return{add(p,rot(z[:2],h))for z in G[a]['requirements']}
def endpoint(a,p,h):
 e=G[a]['endpoint'];return(*add(p,rot(e[:2],h)),(h+e[2])%4)
def chords(a,p,h):
 base=0 if a in[0,1]else 4 if a in[4,5,6]else 7
 e=G[base]['endpoint'];A=add((2*p[0],2*p[1]),rot((-1,-1),h));p=add(p,rot(e[:2],h));B=add((2*p[0],2*p[1]),rot((-1,-1),h));out=[(A,B)]
 for _ in range(G[a]['name'].count('C')):
  A=B;p=add(p,rot((0,1),h));h=(h-1)%4;B=add((2*p[0],2*p[1]),rot((-1,-1),h));out.append((A,B))
 return out
T=chords(7,(0,0),0);pairs=[{a,b},{a,d},{q,b},{q,d}];sources=[]
for S in IDS:
 for h in range(4):
  poses={sub(t,rot(o,h))for t in P for o in G[S]['outputs']}
  for p in sorted(poses):
   if(sum(p)+h)%2:continue
   O=outputs(S,p,h)
   for trio in combinations(sorted(set(O)&P),3):sources.append((S,p,h,O,set(trio)))
assert len(sources)==132
rows=[]
for S,p,h,O,got in sources:
 missing=P-got
 for j in range(4):
  poses={sub(t,rot(o,j))for t in missing for o in G[1]['outputs']}
  for r in sorted(poses):
   if(sum(r)+j)%2 or not missing<=set(outputs(1,r,j)):continue
   C=ctx(1,r,j);row=dict(source=S,source_pose=[*p,h],source_goal_triple=sorted(got),DC_pose=[*r,j],DC_goal_pair=sorted(missing))
   if C&got:reason='DC_complete_context_hits_protected_source_triple';row['hits']=sorted(C&got)
   elif any(contact(A,B)for A in chords(S,p,h)for B in chords(1,r,j)):
    # Any permitted adjacent common endpoint requires these exact full poses.
    assert endpoint(S,p,h)!=(*r,j)
    reason='nonadjacent_source_DC_center_contact'
   elif any(contact(A,B)for A in chords(S,p,h)for B in T):reason='nonadjacent_source_goal_center_contact'
   elif any(contact(A,B)for A in chords(1,r,j)for B in T):
    assert endpoint(1,r,j)!=(0,0,0)
    reason='nonadjacent_DC_goal_center_contact'
   elif(-1,3)in O and any(x<=got for x in pairs):reason='signed_first_white_shadow_on_retained_pair'
   elif S in[7,8,9]and(*p,h)==(-1,1,0)and got=={a,q,c}:reason='signed_partial_d_lock_source_application'
   elif S in[7,8,9]and(*p,h)==(-1,4,1)and got=={b,c,d}:reason='signed_q_pair_lock_source_application'
   elif any(O[t]in[(2,0),(2,1)]for t in got&{b,c,d})and S in[7,8,9]:reason='signed_east_ID_cannot_be_upper_U_input'
   elif S in[7,8,9]and(*p,h)==(0,2,2)and got=={a,q,c}:reason='signed_west_remnant_three_shadow'
   else:raise AssertionError(('unblocked_static_configuration',row))
   row['reason']=reason;rows.append(row)
counts=dict(Counter(r['reason']for r in rows));assert counts.get('signed_partial_d_lock_source_application')==4 and counts.get('signed_q_pair_lock_source_application')==3 and counts.get('signed_east_ID_cannot_be_upper_U_input')==3 and counts.get('signed_west_remnant_three_shadow')==6
# If latest DC supplied three goal inputs, all four raw triple alignments
# arise from its four-output mask at(-3,1,N). The remaining older q is in
# that DC's before-white complete context, independently of the other source.
latest3=[]
for S,p,h,O,got in sources:
 if S!=1:continue
 assert(*p,h)==(-3,1,0)and q not in got and q in ctx(1,p,h)
 rr=next(z for z in G[1]['requirements']if tuple(z[:2])==sub(q,p));assert rr[2]is False
 latest3.append(dict(DC_pose=[*p,h],DC_goal_triple=sorted(got),necessarily_older_q=q,q_is_before_white=True))
assert len(latest3)==4
D=[GP]+[W/n/'manifest.json'for n in['U_max_three_cohort_frozen_20261023_1805','U_white_shadow_frozen_20261023_1709','U_partial_d_lock_frozen_20261023_1832','U_q_pair_lock_frozen_20261023_1840','causal_cycle_renewal_20261023_1841','U_west_remnant_shadow_frozen_20261023_1914']]+[Path(__file__).resolve()]
R=dict(status='AUTHOR_TWO_PRODUCER_UNARY_LAST_EXCLUSION_PENDING_INDEPENDENT_AUDIT',scope='Actual complete recurrent-eight factor with simple corrected atomic-center path. If a U-family event has exactly TWO genuine earlier full producers for its five input IDs, the latest producer cannot be D or DC. P3+laterDC2 complete geometry has no survivors; latestDC3 is before-white incompatible with older q; latestD/DC1 forces other-source4, already excluded. No entry origins are grouped, no general3-producer or historical-component conclusion.',earlier_source_triple_placements=132,later_DC_pair_configurations=len(rows),counts=counts,all_later_DC_pair_configurations=rows,latest_DC_three_cases=latest3,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_two_producer_unary_last.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(dict(configurations=len(rows),counts=counts,latest_DC3=len(latest3)),indent=2))
