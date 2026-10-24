"""Exact two-generation residual shadow, with U-entry simplicity.

No age clause, word search, spatial box, or claimed incidence embedding.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,hashlib
ROOT=Path(__file__).resolve().parent
GP=ROOT/'chronology_dcuv/literal_residual_geometry.json';SP=ROOT/'U_entry_simplicity_frozen_20261023_1616/manifest.json';IP=ROOT/'chronology_dcuv/u_middle_input_origin_order.json'
G=json.load(open(GP))['geometry'];IDS=(0,1,4,5,6,7,8,9)
P={(-1,1),(-1,2),(0,2),(0,3)};R=(1,1);S=(1,2);F={(-1,1),(-1,2),(-1,4),(0,2),(0,3)}
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def chord(a,p,h):
 b=0 if a in(0,1)else 4 if a in(4,5,6)else 7
 c=add((2*p[0],2*p[1]),rot((-1,-1),h));return(c,add(c,rot((2,2)if b==0 else(2,6)if b==4 else(0,8),h)))
def intersection(X,Y):
 a,b=X;c,d=Y;u=sub(b,a);v=sub(d,c);w=sub(c,a);D=det(u,v)
 if D:
  s,t=Q(det(w,v),D),Q(det(w,u),D)
  assert 0<=s<=1 and 0<=t<=1
  point=add(a,(s*u[0],s*u[1]));return dict(kind='single_closed_contact',source_parameter=s,clearer_parameter=t,twice_contact_point=point)
 assert det(w,u)==0;k=0 if u[0]else 1
 a0,a1=Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k]);lo,hi=max(Q(0),min(a0,a1)),min(Q(1),max(a0,a1))
 assert lo<=hi
 return dict(kind='closed_collinear_overlap'if lo<hi else'collinear_point',source_parameter_interval=(lo,hi))
def align(cell):
 rows=[];stats=Counter();surv=[]
 for a in IDS:
  for inp in G[a]['inputs']:
   for h in range(4):
    p=sub(cell,rot(inp,h));sector=(sum(p)+h)%2
    hits=P&{add(p,rot(z[:2],h))for z in G[a]['requirements']}
    reason='wrong_sector'if sector else'protected_input_context'if hits else'candidate'
    stats[reason]+=1
    row=dict(packet=a,name=G[a]['name'],input=inp,entry_pose=(*p,h),protected_hits=sorted(hits),reason=reason)
    rows.append(row)
    if reason=='candidate':surv.append(row)
 return rows,stats,surv
first,counts1,helpers=align(R);second,counts2,clearers=align(S)
assert len(first)==len(second)==92
assert counts1==Counter(wrong_sector=46,protected_input_context=43,candidate=3)
assert counts2==Counter(wrong_sector=46,protected_input_context=37,candidate=9)
assert {(r['packet'],r['entry_pose'],tuple(r['input']))for r in helpers}=={(a,(2,0,0),(-1,1))for a in(7,8,9)}
expected={(0,(1,1,0),(0,1)),(1,(1,1,0),(0,1)),(4,(1,-1,0),(0,3)),(5,(1,-1,0),(0,3)),(7,(2,0,0),(-1,2)),(8,(2,0,0),(-1,2)),(9,(2,0,0),(-1,2)),(7,(2,-2,0),(-1,4)),(8,(2,-2,0),(-1,4))}
assert {(r['packet'],r['entry_pose'],tuple(r['input']))for r in clearers}==expected
contacts=[]
for h in helpers:
 a=h['packet'];p=tuple(h['entry_pose'][:2]);H=h['entry_pose'][2]
 assert S in {add(p,rot(o,H))for o in G[a]['outputs']}
 assert S in {add(p,rot(i,H))for i in G[a]['inputs']}  # Fresh recycled identity.
 full_exit=(*add(p,rot(G[a]['endpoint'][:2],H)),(H+G[a]['endpoint'][2])%4)
 hc=chord(a,p,H)
 assert hc==((3,-1),(3,7))
 for b in clearers:
  assert full_exit!=b['entry_pose']
  bc=chord(b['packet'],tuple(b['entry_pose'][:2]),b['entry_pose'][2]);hit=intersection(hc,bc)
  contacts.append(dict(helper=a,helper_full_exit=full_exit,clearer=b['packet'],clearer_entry=b['entry_pose'],source_base_chord_twice=hc,clearer_base_chord_twice=bc,adjacent_full_pose_exception=False,contact=hit))
assert len(contacts)==27
for goal in(7,8,9):
 req={tuple(q[:2]):q[2]for q in G[goal]['requirements']}
 assert req[R]is False and req[S]is False
 assert P<=set(map(tuple,G[goal]['inputs']))
source_cuts=[]
old=json.load(open(IP))['four_cohort_templates']
for a in(7,8,9):
 p=(-1,1);O={add(p,tuple(o))for o in G[a]['outputs']};I={add(p,tuple(i))for i in G[a]['inputs']}
 assert O&F==P and R in O and (-1,4)in I and (-1,4)not in O
 matches=[j for j,t in enumerate(old)if t['source_packet']==a and t['consumer_pose']==[1,-1,0]];assert len(matches)==1
 source_cuts.append(dict(source=a,name=G[a]['name'],source_pose=(-1,1,0),source_fresh_shadow=R,protected_goal_inputs=sorted(P),retired_missing_goal_input=(-1,4),old_inventory_row=matches[0]))
O=dict(status='AUTHOR_EXACT_TWO_GENERATION_U_WHITE_SHADOW',scope='Actual complete-eight chronology, arbitrary ages and earlier history. Suffix beginning forced U helper is simple by signed theorem. Ordered residual identities, including recycled fresh s. No incidence merger/U-count/capture claim.',first_shadow=R,second_shadow=S,protected_goal_inputs=sorted(P),first_consumer_counts=dict(counts1),second_consumer_counts=dict(counts2),all_184_consumer_alignments=dict(first=first,second=second),all_27_source_clearer_contacts=contacts,three_remaining_four_cohort_cuts=source_cuts,dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(GP,SP,IP,Path(__file__).resolve())})
def enc(x):
 if isinstance(x,Q):return int(x)if x.denominator==1 else str(x)
 if isinstance(x,(tuple,list)):return[enc(z)for z in x]
 if isinstance(x,dict):return{k:enc(v)for k,v in x.items()}
 return x
(ROOT/'chronology_dcuv/U_second_generation_white_shadow.json').write_text(json.dumps(enc(O),indent=2)+'\n')
print(json.dumps(dict(first=dict(counts1),second=dict(counts2),contacts=len(contacts),new_source_cuts=source_cuts),indent=2))
