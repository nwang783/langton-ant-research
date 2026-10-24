"""Independent literal controls for author operator; large-distance control is symbolic, not expanded."""
import json,random
from pathlib import Path
from blank_collision_operator import *
from check_fresh_record_trap_bridge import replay,verify_tail
P=Path(__file__).parent
# Exhaust all pairs of allowed line directions on a small interval family, including parity cancellations.
DRS=[(0,0),(2,2),(2,-2),(-2,2),(-2,-2)];rng=random.Random(73419);ray_controls=0
for _ in range(300):
 seg=[]
 for j in range(rng.randrange(1,9)):
  d=rng.choice(DRS);b=(rng.randrange(-10,11),rng.randrange(-10,11));n=1 if d==(0,0)else rng.randrange(1,8);seg.append((b,d,n))
 if rng.randrange(2):seg.append(seg[0])
 field=materialize(seg);d=rng.choice(DRS[1:]);q=(rng.randrange(-6,7),rng.randrange(-6,7));candidates=[multiple((x[0]-q[0],x[1]-q[1]),d)for x in field];want=min((k for k in candidates if k is not None and k>=0),default=None);assert first_on_ray(seg,q,d)==want;ray_controls+=1
# Finite literal histories, preserving every field and true lifetime.
seeds=[set(),{(0,0)},{(0,-1)},{(-2,-2)},{(-1,2),(3,-4),(4,1)}]
rr=json.loads((P/'OUTWARD_RECORD_GUARDS_CHECKED.json').read_text())['normal_catalog'][2]['records'][0]
seeds +=[set(map(tuple,rr['required_black'])),set(map(tuple,rr['required_black']))-{(-3,-2)}]
controls=[]
for ix,seed in enumerate(seeds):
 h=1 if ix>=5 else 0;p=(0,0);B=set(seed);terms=[(x,(0,0),1)for x in sorted(seed)];clock=0;birth={x:['initial',x]for x in B};macros=[];emissions=[]
 for step in range(35):
  z=next_collision(terms,p,h)
  if z['kind']!='collision':
   # Exact no-hit condition is verified independently by all finite-prefix slots and every initial black/ray intersection.
   for x in B:
    local=rotate((x[0]-p[0],x[1]-p[1]),-h);assert local not in set(CP)
    assert all((k:=multiple((local[0]-q[0],local[1]-q[1]),DR))is None or k<0 for q in HP)
   macros.append(dict(kind='certified no hit',time=clock));break
  t=z['blank_duration'];assert t<30000
  parent=birth[z['consumed_cell']];born_this={};old=set(B);originp=p;originh=h
  for s in range(t+1):
   a='L'if p in B else'R'
   if s<t:assert p not in old
   else:assert p==z['consumed_cell']and a=='L'and birth[p]==parent
   if a=='L':B.remove(p);birth.pop(p);h=(h-1)%4
   else:B.add(p);birth[p]=['R',clock+s];born_this[p]=clock+s;h=(h+1)%4
   p=(p[0]+D[h][0],p[1]+D[h][1])
  emitted=materialize(z['emitted_terms']);assert emitted.isdisjoint(old)and materialize(z['new_terms'])==B and (p,h)==z['new_pose']
  for x in emitted:
   local=rotate((x[0]-originp[0],x[1]-originp[1]),-originh);assert birth[x]==['R',clock+blank_birth(local,t)]
  macros.append(dict(start=clock,blank_duration=t,collision=clock+t,consumed_cell=z['consumed_cell'],parent_origin=parent,emitted_mass=len(emitted),final_mass=len(B),pose=[p,h]))
  clock+=t+1;terms=z['new_terms'];assert clock<100000
 controls.append(dict(seed=sorted(seed),start_heading=1 if ix>=5 else 0,macros=macros,final_clock=clock,full_final_black=sorted(B)))
# Huge K is not simulated or materialized: first old input on a far reference ray.
K=10**9;point=(HP[0][0]+K*DR[0],HP[0][1]+K*DR[1]);old=[(point,(0,0),1)];z=next_collision(old);assert z['kind']=='collision'
candidate=[]
for i,q in enumerate(HP):
 k=multiple((point[0]-q[0],point[1]-q[1]),DR)
 if k is not None and k>=0:candidate.append(T+104*k+i)
assert z['blank_duration']==min(candidate)and len(z['emitted_terms'])<1000
# One more exact collision on the complete enormous emitted board uses interval parity, not an expanded seed.
z2=next_collision(z['new_terms'],*z['new_pose']);assert z2['kind']=='collision'and z2['blank_duration']<1000
# Every actual standard phase still has a first old collision, so this operator does not terminate on standard104.
std=[]
for i in range(104):
 w=H[i:]+H[:i];j=next(j for j,a in enumerate(C)if a!=w[j%104]);assert(C[j],w[j%104])==('R','L');std.append(j)
assert max(std)==10
out=dict(status='AUTHOR exact closed XOR-segment collision operator; independent audit pending',ray_intersection_controls=ray_controls,finite_histories=controls,huge_K_control=dict(K=K,old_cell=point,first_collision_blank_duration=z['blank_duration'],emission_term_count=len(z['emitted_terms']),successor_pose=z['new_pose'],next_collision_blank_duration=z2['blank_duration'],next_collision_cell=z2['consumed_cell']),standard_phase_blank_agreement_lengths=std,max_standard_macro_duration=11,canonical_blank_period_odd_mask_size=len(M))
(P/'BLANK_COLLISION_OPERATOR_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n');print(dict(ray_controls=ray_controls,finite_histories=len(controls),large=z['blank_duration'],terms=len(z['emitted_terms']),next=z2['blank_duration'],max_standard_duration=11,mask=len(M)))
