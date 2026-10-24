"""Three causally launched two-tip-cap families, all wake lengths K>=0."""
import json
from pathlib import Path
from blank_collision_operator import cross,multiple
from check_fresh_record_trap_bridge import geometry,replay,verify_tail
P=Path(__file__).parent
base=json.loads((P/'TANGENTIAL_CAP_CAPTURE_CERTIFICATE.json').read_text())
cert=json.loads((P/'TWO_TIP_CAP_CAPTURE_CERTIFICATE.json').read_text())
S=set(map(tuple,base['seed_six']));W=base['launch_word'];H=base['wake_word'];a0=(5,-4);d=(2,-2)
E,p0,h0,ev=replay(S,(1,1),2,W);Q,_,_=geometry(p0,h0,H)
M=set()
for q in Q:M^={q}
results=[];max_delay=0
for block in cert['variants']:
 off=tuple(block['offset']);assert off in((1,0),(0,-1),(1,1));b0=(5+off[0],-4+off[1])
 # Exact all-K first contact with the second cap in the UNPERTURBED wake.
 for _,q,_,_ in ev:
  k=multiple((q[0]-b0[0],q[1]-b0[1]),d)
  assert k is None or k<0
 hits=[]
 for i,q in enumerate(Q):
  e=multiple((b0[0]-q[0],b0[1]-q[1]),d)
  if e is not None:
   assert e>=0 and 104*e+i>45
   hits.append(104*e+i)
 first_unperturbed=min(hits);assert first_unperturbed=={(1,0):60,(0,-1):46,(1,1):75}[off]
 finite=[]
 for row in block['finite_controls']:
  K=row['K'];a=(5+2*K,-4-2*K);b=(a[0]+off[0],a[1]+off[1]);seed=S|{a,b};assert len(seed)==8
  F=row['post_contact_word'];V=row['tail_word'];word=W+H*K+H[:45]+F;T=279+104*K
  B,p,h,events=replay(seed,(1,1),2,word)
  assert events[T][1]==list(a) and events[T][3]=='L'
  assert all(tuple(z[1])not in(a,b)for z in events[:T])
  assert B==set(map(tuple,row['full_final_black']))and[list(p),h]==row['final_pose']
  tq,td,tests=verify_tail(B,p,h,V);assert td==tuple(row['tail_drift'])
  finite.append(dict(K=K,certificate_time=len(word),delay=len(F),tail_drift=td,full_mass=len(B),ray_tests=tests))
  max_delay=max(max_delay,len(F))
  if K!=11:continue
  CF,end,hh=geometry((0,0),1,F);TF,te,th=geometry(end,hh,V);v=(te[0]-end[0],te[1]-end[1]);assert v==(2,2)
  # Same complete difference-ray cover as one-cap family; fixed off cancels.
  checked=[];u=(-2,2)
  for name,A,lo in [('source',E,11),('wake',M,12)]:
   for q in sorted(A):
    origin=(q[0]-5,q[1]+4)
    for x in CF:
     k=multiple((x[0]-origin[0],x[1]-origin[1]),u)
     assert k is None or k<lo
    for i,x in enumerate(TF):
     z=(x[0]-origin[0],x[1]-origin[1]);det=cross(u,v);kn=cross(z,v);jn=cross(z,u)
     if kn%det or jn%det:continue
     k,j=kn//det,jn//det
     assert k<lo or j<0
    checked.append([name,origin,lo])
  assert len(checked)==82
  cap_reads=[i for i,x in enumerate(CF)if x==off]
  for i,x in enumerate(TF):
   k=multiple((off[0]-x[0],off[1]-x[1]),v)
   if k is not None and k>=0:cap_reads.append(len(F)+104*k+i)
  first_actual=min(cap_reads,default=None)
  assert first_actual=={(1,0):None,(0,-1):1857,(1,1):86}[off]
  assert len(F)=={(1,0):2184,(0,-1):2184,(1,1):2392}[off]
  launch,_,_=geometry((1,1),2,W)
  assert min([sum(q)for q in launch]+[sum(q)for q in Q]+[1+sum(q)for q in CF]+[1+sum(q)for q in TF])==-19
  common=dict(delay=len(F),normalized_final_pose=[end,hh],tail_drift=v,
              second_initial_cap_first_read_offset=first_actual,all_parameter_unread_rays=checked,
              min_xy_sum=-19,SW_pristine_record_cuts=19 if off==(0,-1)else 20)
 results.append(dict(offset=off,first_unperturbed_second_cap_phase=first_unperturbed,finite_controls=finite,all_K11plus=common))
assert len(results)==3 and max_delay==13104
report=dict(status='AUTHOR all-parameter scoped result; independent audit pending',variants=results,
            uniform_guard_avoiding_pristine_time_cut_bound=234+13104+2*375,
            uniform_direction_marked_bound=8*(234+13104+2*375),
            maximum_finite_certificate_delay=13104,no_minimal_onset_claim=True,
            scope='Only the three stated causally launched eight-cell families, every integer K>=0.')
(P/'TWO_TIP_CAP_CAPTURE_CHECKED.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(variants=3,literal_controls=36,all_parameter_ray_checks=246,bad_pristine_bound=14088)))
