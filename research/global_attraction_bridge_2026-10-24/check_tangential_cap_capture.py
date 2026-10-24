"""All-K causal seven-cell wake/cap family: literal finite controls + exact unread rays."""
import json
from pathlib import Path
from blank_collision_operator import cross,multiple,D
from check_fresh_record_trap_bridge import geometry,replay,verify_tail
P=Path(__file__).parent
cert=json.loads((P/'TANGENTIAL_CAP_CAPTURE_CERTIFICATE.json').read_text())
S=set(map(tuple,cert['seed_six']));a0=tuple(cert['cap_base']);d=tuple(cert['wake_drift'])
W=cert['launch_word'];H=cert['wake_word'];F=cert['common_post_contact_word'];V=cert['common_tail_word']
assert len(S)==6 and len(W)==234 and len(H)==104 and len(F)==2184 and len(V)==104
E,p0,h0,ev=replay(S,(1,1),2,W);Q,d0,_=verify_tail(E,p0,h0,H);assert d0==d==(2,-2) and len(E)==50
assert min(sum(q)for q in S)==1 and sum(a0)==1
M=set()
for q in Q:M^={q}
assert len(M)==32
A45=set()
for q in Q[:45]:A45^={q}
assert len(E)+(2*H[:45].count('R')-45)+1==58
assert H.count('R')-H.count('L')==12
assert Q[45]==a0 and H[45]=='R'
# All-K unread first cap. Prefix occurrences lie at strictly negative ray indices;
# all H-phase visits have relative time >=45.
prefix_indices=[]
for _,q,_,_ in ev:
 k=multiple((q[0]-a0[0],q[1]-a0[1]),d)
 if k is not None:assert k<0;prefix_indices.append(k)
phase_hits=[]
for i,q in enumerate(Q):
 off=multiple((a0[0]-q[0],a0[1]-q[1]),d)
 if off is not None:
  assert off>=0 and 104*off+i>=45
  phase_hits.append([i,off,104*off+i])
assert min(z[2]for z in phase_hits)==45
# Literal controls K0..11 retain complete fields and prove all infinite tails.
small=[];base_B=None;base_birth=None;base_records=None
for K in range(12):
 row=cert['finite_controls'][K];assert row['K']==K
 a=(a0[0]+K*d[0],a0[1]+K*d[1]);B=S|{a};p=(1,1);h=2
 birth={q:['initial',q]for q in B};T=279+104*K
 continuation=row['post_contact_word'];whole=W+H*K+H[:45]+continuation
 assert len(whole)==row['certificate_time']
 records=[];best=2;cohort=None;consumed=[]
 for t,turn in enumerate(whole):
  if sum(p)<best:
   best=sum(p)
   if all(sum(q)>best for q in B):records.append([t,p,h,best])
  if t==T:
   assert p==a and p in B;cohort=dict(birth)
   assert len(B)==58+12*K
  assert(p in B)==(turn=='L')
  if turn=='L':
   old=birth.pop(p);B.remove(p)
   if cohort is not None and cohort.get(p)==old:consumed.append([t-T,(p[0]-a[0],p[1]-a[1]),old])
   h=(h-1)%4
  else:B.add(p);birth[p]=['R',t];h=(h+1)%4
  p=(p[0]+D[h][0],p[1]+D[h][1])
 assert B==set(map(tuple,row['full_final_black'])) and [list(p),h]==row['final_pose']
 tq,td,tests=verify_tail(B,p,h,row['tail_word']);assert td==tuple(row['tail_drift'])
 small.append(dict(K=K,certificate_time=len(whole),post_contact_duration=len(continuation),
                   full_final_mass=len(B),tail_drift=td,infinite_tail_change_tests=tests))
 if K==11:
  assert continuation==F and row['tail_word']==V and len(B)==356
  assert len(consumed)==113 and sum(z[2][0]=='R'for z in consumed)==112
  assert consumed[0][1]==(0,0) and consumed[0][2][0]=='initial'
  assert min(z[2][1]-T for z in consumed if z[2][0]=='R')==-910
  assert max(z[0]for z in consumed)==1872
  remaining={q for q,b in cohort.items()if birth.get(q)==b}
  assert len(remaining)==77
  for q in remaining:
   assert all((k:=multiple((q[0]-r[0],q[1]-r[1]),td)) is None or k<0 for r in tq)
  assert [z[3]for z in records]==list(range(0,-20,-1))
  base_B=B;base_birth=consumed;base_records=records
# Build normalized common future from the cap, including its first actual L.
_,_,entry_h=geometry(p0,h0,H[:45]);CF,end,hh=geometry((0,0),entry_h,F)
TF,te,th=geometry(end,hh,V);tail_d=(te[0]-end[0],te[1]-end[1]);assert tail_d==(2,2)
assert end==(6,14) and hh==3 and th==hh
# All differing cells between normalized B_K and B_11 lie in these rays.
# Each ray is proven disjoint from the ENTIRE common future read footprint.
def ray_intersections(b,lo):
 hits=[];u=(-d[0],-d[1])
 for t,q in enumerate(CF):
  k=multiple((q[0]-b[0],q[1]-b[1]),u)
  if k is not None and k>=lo:hits.append(['prefix',t,k])
 for i,q in enumerate(TF):
  z=(q[0]-b[0],q[1]-b[1]);det=cross(u,tail_d)
  kn=cross(z,tail_d);jn=cross(z,u)
  if kn%det or jn%det:continue
  k,j=kn//det,jn//det
  if k>=lo and j>=0:hits.append(['tail',i,k,j])
 return hits
ray_checks=[]
for name,A,lo in [('source',E,11),('wake',M,12)]:
 for q in sorted(A):
  b=(q[0]-a0[0],q[1]-a0[1]);assert not ray_intersections(b,lo)
  ray_checks.append(dict(cohort=name,base=b,backward_parameter_min=lo))
assert len(ray_checks)==82
# Source-shift + extra wake XOR formula for normalized contact fields, checked
# literally on K11 as an anchor. Its all-K derivation is in the proof.
normalized={}
for K in (11,12,32):
 field={(0,0)}
 for q in E:field^={(q[0]-a0[0]-K*d[0],q[1]-a0[1]-K*d[1])}
 for q in A45:field^={(q[0]-a0[0],q[1]-a0[1])}
 for l in range(1,K+1):
  for q in M:field^={(q[0]-a0[0]-l*d[0],q[1]-a0[1]-l*d[1])}
 normalized[K]=field
assert len(normalized[11])==190
for K in (12,32):
 for q in set(CF):assert(q in normalized[K])==(q in normalized[11])
# Every consumed wave lifetime has an all-K last-R formula, not a cell-only tag.
for offset,z,birth in base_birth:
 if birth[0]!='R':continue
 candidates=[]
 for i,q in enumerate(Q):
  s=multiple((a0[0]+z[0]-q[0],a0[1]+z[1]-q[1]),d)
  if s is not None and (s<0 or s==0 and i<45):candidates.append((104*s+i-45,i,s))
 rel,i,s=max(candidates)
 assert 11+s>=0 and H[i]=='R' and rel==birth[1]-(279+104*11)
# Whole-path SW maximum is a path calculation. Tail (2,2) moves inward for SW.
launch_positions,_,_=geometry((1,1),2,W)
minsum=min([sum(q)for q in launch_positions]+[sum(q)for q in Q]+[1+sum(q)for q in CF]+[1+sum(q)for q in TF])
assert minsum==-19
# The latest SW record precedes any cyclic standard tail, so no outward guard
# could have captured there. Exact first words rule out all 104 cyclic phases.
full11=W+H*11+H[:45]+F+V*3
for t,_,_,_ in base_records:
 for phase in range(104):
  candidate=V[phase:]+V[:phase]
  assert any(full11[t+j]!=candidate[j%104]for j in range(min(312,len(full11)-t)))
report=dict(status='AUTHOR all-K proof; independent audit pending',finite_controls=small,
 all_K11plus=dict(common_post_contact_duration=2184,normalized_final_pose=[end,hh],tail_drift=tail_d,
                 complete_parameter_difference_rays=ray_checks,selected_initial_cohort_consumptions=base_birth,
                 consumed_entry_cohort=113,consumed_wave_born=112,remaining_entry_cohort='12K - 55, all unread forever',
                 final_black_mass='12K + 224',SW_pristine_records=20,min_xy_sum=-19),
 all_parameter_uniform_bad_pristine_record_time_cuts=3168,
 bound_decomposition=dict(arbitrary_length=234+2184,standard_pieces=2,fringe_allowance=375),
 prefix_cap_ray_indices=sorted(set(prefix_indices)),cap_phase_hits=phase_hits,
 no_minimal_capture_time_claim=True)
(P/'TANGENTIAL_CAP_CAPTURE_CHECKED.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(finite_controls=len(small),all_parameter_rays=len(ray_checks),post_contact=2184,bad_pristine_bound=3168)))
