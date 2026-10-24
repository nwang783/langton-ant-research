"""Exact local sides and stage support for two conditional first-contact loops.
The global Jordan confinement is proved in the accompanying note, not inferred
from sampled words. Finite run cases follow a derived positive height weight.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';CP=R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];C=json.loads(CP.read_text());VEL=((0,1),(1,0),(0,-1),(-1,0));K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def ctr(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def endpoint(word):
 p=(0,0);h=0
 for ch in word:h=(h+(-1 if ch=='L' else 1))%4;p=add(p,VEL[h])
 return p,h
AT=[]
for n in 'DCVU':
 i='DCVUFQB'.index(n);ep,dh=endpoint(W[i]['word']);AT.append(dict(name=n,endpoint=ep,turn=dh))
# Check exact stage monotonicity from all actual atom endpoints, not a corpus.
stages=[]
for h in (0,3,2,1):
 for a in AT:
  ep=rot(a['endpoint'],h);out=(h+a['turn'])%4
  if a['name']!='C':
   assert out==h
   assert ep[1]>=0 if h in (0,3) else ep[1]<=0
  else:
   assert (h,out,ep) in ((0,3,(0,1)),(3,2,(-1,0)),(2,1,(0,-1)),(1,0,(1,0)))
  stages.append(dict(heading=h,atom=a['name'],head_displacement=ep,exit_heading=out,entry_center_y_offset=rot((-1,-1),h)[1],exit_center_y_offset=rot((-1,-1),out)[1]))
# Principal-angle algebra in quarter-turn units. Symbol a=alpha_V/(pi/2)
# lies STRICTLY between1/2 and1; alpha_D=alpha_C=1/2.
# Open lift =5+alpha_return-alpha_D; closing turn=-1/2-alpha_return.
rows=[];frames=[]
for ix,cap in ((15,3),(30,2)):
 r=C['old_source_contact_cases'][ix];assert r['source_atom']=='D' and r['foreign']=='F' and r['source_to_foreign_C_age']==3
 p=tuple(r['foreign_pose'][:2]);assert r['foreign_pose'][2]==1;Y=p[1];lower=2*Y+1
 fstart=ctr(p,1);fe,fh=endpoint(W[4]['word']);fep=at(fe,p,1);fend=ctr(fep,(1+fh)%4)
 rp=tuple(r['returned_pose'][:2]);rh=r['returned_pose'][2];assert ctr(rp,rh)==fend
 re,rdh=endpoint(W['DCVU'.index(r['returned_atom'])]['word']);rend=ctr(at(re,rp,rh),(rh+rdh)%4)
 q=(-1,-1) if ix==15 else (0,0)
 assert r['contact']['t']==1 if ix==15 else r['contact']['t']=='1/2'
 assert q==rend if ix==15 else q==((fend[0]+rend[0])//2,(fend[1]+rend[1])//2)
 assert fstart[1]==lower and fend[1]==lower+6 and min(fend[1],q[1])>=lower
 ar=(F(1,2),F(0)) if ix==15 else (F(0),F(1))
 opened=(F(5)+ar[0]-F(1,2),ar[1]);closed=(-F(1,2)-ar[0],-ar[1]);assert (opened[0]+closed[0],opened[1]+closed[1])==(F(4),F(0))
 # D15 interior sector in angle-quarter units is(1/2,7/2).
 # Every possible actual pre-D incoming reverse ray is strictly inside it.
 rays={'D':[F(5,2),0],'V':[F(2),1],'U':[F(3),0],'C':[F(3,2),0]}
 for c,a in rays.values():assert F(1,2)<c+a*F(1,2) and c+a*F(1)<F(7,2)
 # D30 source D BEFORE contact has reverse direction5/2, strictly between
 # outgoing1/2 and reversed returnedV ray3+a, a in(1/2,1).
 assert F(1,2)<F(5,2)<F(3)+F(1,2)
 runwords=[]
 for length in range(cap+1):
  for zz in product('DVU',repeat=length):
   word=''.join(zz);height=sum({'D':1,'V':3,'U':4}[x] for x in word)
   if height>cap:continue
   x=sum(c in 'DV' for c in word);center=ctr((-x,-height),0);assert center[1]>lower
   runwords.append(word)
   for gi in (1,5,6,8,9):
    ep=tuple(G[gi]['endpoint'][:2]);dh=G[gi]['endpoint'][2];h=(-dh)%4;head=(-x,-height);base=sub(head,rot(ep,h));lastC=(head[0]-1,head[1],1)
    assert (1+endpoint(W[1]['word'])[1])%4==0
    frames.append(dict(catalogue_id=ix,actual_pre_D_zero_C_word=word,vertical_weight=height,last_positive_C_full_packet=G[gi]['name'],packet_entry=[*base,h],packet_exit=[*head,0],last_actual_C_entry=lastC,earlier_history_remains_unconstrained=True))
 assert sorted(runwords)==sorted(['','D','DD','DDD','V'] if ix==15 else ['','D','DD'])
 # The NEXT positive height would put an actual old start on/below support.
 assert -2*(cap+1)-1<=lower and -2*cap-1>lower
 rows.append(dict(catalogue_id=ix,foreign_pose=r['foreign_pose'],returned_atom=r['returned_atom'],returned_pose=r['returned_pose'],contact=q,foreign_piece=[fstart,fend],returned_closed_piece=[fend,q],doubled_y_lower_bound=lower,open_tangent_quarter_coefficients=[str(x) for x in opened],closing_turn_quarter_coefficients=[str(x) for x in closed],total_turn_quarters=4,CCW_interior_local_rays=rays if ix==15 else {'earlier_D_ray':[F(5,2),0]},maximum_actual_pre_D_N_run_vertical_weight=cap,exhaustive_actual_zero_C_run_words=runwords,source_own_DC_tail_after_D_is_not_in_this_pre_D_run=True))
D=[GP,QP,CP,R/'seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json',R/'seven_word_spatial_return_2026-10-23/first_foreign_all_source_join_manifest.json',R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact_manifest.json',R/'returned_D_source_join_2026-10-24/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Conditional chronological-FIRST-contact Jordan confinement for two remaining D-source geometries. Every strictly earlier old point is inside the simple loop. Only the actual last zero-C N-run before selected D gets the explicit weight bound; arbitrary earlier clocks/prefixes are not bounded.',symbolic_angle='All angle coefficients are in units pi/2, pair[constant,coefficient of a], where1/2<a=atan(3)/(pi/2)<1.',two_exact_local_loops=rows,all16_atomic_stage_displacements=stages,all40_exhaustive_last_positive_C_packet_and_short_run_interfaces=frames,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in D})
(H/'D_Jordan_horizon.json').write_text(json.dumps(o,indent=2,default=str)+'\n');print('Two CCW local loops; support -9/-7; pre-D runs five/three;40 last-positive-C interfaces.')
