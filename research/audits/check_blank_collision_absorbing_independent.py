from pathlib import Path
from collections import Counter
import json,hashlib,sys,random
S=Path(__file__).resolve();R=S.parents[1];P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();manifest=json.loads((P/'BLANK_COLLISION_ABSORBING_MANIFEST.json').read_text())
for f,h in manifest.items():assert sha(P/f)==h
sys.path.insert(0,str(P));import blank_collision_operator as op;import blank_collision_absorber as ab
base=json.loads((P/'PRISTINE_COHORT_ADVANCE_CHECKED.json').read_text());rr=json.loads((P/'BLANK_COLLISION_OPERATOR_CHECKED.json').read_text());ar=json.loads((P/'BLANK_COLLISION_ABSORBER_CHECKED.json').read_text());assert sha(S.with_name('check_pristine_cohort_advance_independent.json'))=='745ea7e2359ca6c33e56307a2b18594e22bfd607c785c6eb9a4e34b99f55afe4'
V=((0,1),(1,0),(0,-1),(-1,0));add=lambda a,b:(a[0]+b[0],a[1]+b[1]);sub=lambda a,b:(a[0]-b[0],a[1]-b[1]);scale=lambda n,v:(n*v[0],n*v[1]);cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
def rotate(p,h):
 for _ in range(h%4):p=(p[1],-p[0])
 return p
def mult(p,d):
 i=next(j for j in(0,1)if d[j]);q,r=divmod(p[i],d[i]);return q if r==0 and scale(q,d)==p else None
def geom(w,p=(0,0),h=0):
 pp=[];hh=[]
 for c in w:pp.append(p);hh.append(h);h=(h+(1 if c=='R'else-1))%4;p=add(p,V[h])
 return pp,hh,p,h
C=base['blank_prefix'];H=base['blank_tail_word'];CP,CH,ep,eh=geom(C);HP,HH,end,hend=geom(H,ep,eh);d=sub(end,ep);assert d==(-2,-2)and eh==hend;first={}
for i,p in enumerate(CP):first.setdefault(p,i)
assert len(first)==1376
TB={tuple(p)for p in base['blank_tail_state']['black']};mask=set()
for p in HP:mask.symmetric_difference_update({p})
assert len(mask)==32
# Independent exact line/segment intersection, returning inclusive nonnegative ray-index intervals.
def intervals(terms,q,d):
 out=[]
 for b,v,L in terms:
  assert L>=1 and(v!=(0,0)or L==1);z=sub(b,q)
  if v==(0,0):
   k=mult(z,d)
   if k is not None and k>=0:out.append((k,k))
   continue
  det=cross(d,v)
  if det:
   nk,nj=cross(z,v),cross(z,d)
   if nk%det==0 and nj%det==0:
    k,j=nk//det,nj//det
    if k>=0 and 0<=j<L:out.append((k,k))
  else:
   off=mult(z,d)
   if off is None:continue
   sign=mult(v,d);assert sign in(-1,1);a,b=sorted((off,off+sign*(L-1)));a=max(a,0)
   if a<=b:out.append((a,b))
 return out

def first_ray(terms,q,d):
 iv=intervals(terms,q,d);changes={0}
 for a,b in iv:changes.update((a,b+1))
 return next((n for n in sorted(changes)if sum(a<=n<=b for a,b in iv)%2),None)
def expand(terms):
 B=set()
 for p,v,L in terms:
  for j in range(L):B.symmetric_difference_update({add(p,scale(j,v))})
 return B
# Exhaust all orientations, antiparallel/domain/parity cases on small exact segments.
DS=((0,0),(2,2),(2,-2),(-2,2),(-2,-2));nray=0
for v in DS:
 for dv in DS[1:]:
  for x in range(-3,4):
   for y in range(-3,4):
    for L in((1,)if v==(0,0)else(1,2,4)):
     seg=[((x,y),v,L)];B=expand(seg);q=(1,-1);ks=[mult(sub(z,q),dv)for z in B];want=min((k for k in ks if k is not None and k>=0),default=None);assert first_ray(seg,q,dv)==want==op.first_on_ray(seg,q,dv);nray+=1
rng=random.Random(874031)
for _ in range(400):
 terms=[]
 for j in range(rng.randrange(1,9)):
  v=rng.choice(DS);terms.append(((rng.randrange(-9,10),rng.randrange(-9,10)),v,1 if v==(0,0)else rng.randrange(1,8)))
 if rng.randrange(2):terms.append(terms[0])
 q=(rng.randrange(-7,8),rng.randrange(-7,8));dv=rng.choice(DS[1:]);B=expand(terms);ks=[mult(sub(z,q),dv)for z in B];want=min((k for k in ks if k is not None and k>=0),default=None);assert first_ray(terms,q,dv)==want==op.first_on_ray(terms,q,dv);nray+=1
 # Compare the complete field parity sweep, including the final zero interval.
 changes=ab.field_ray_changes(terms,q,dv);tests=set(changes)|{0};parity=0
 for k in sorted(tests):parity^=changes.get(k,0);assert parity==(add(q,scale(k,dv))in B)

def explicit_hit(B,p,h):
 best=None
 for b in B:
  local=rotate(sub(b,p),-h)
  if local in first:t=first[local];cand=(t,b,(CH[t]+h)%4)
  else:
   cs=[]
   for i,q in enumerate(HP):
    k=mult(sub(local,q),d)
    if k is not None and k>=0:cs.append((9977+104*k+i,b,(HH[i]+h)%4))
   if not cs:continue
   cand=min(cs)
  if best is None or cand[0]<best[0]:best=cand
 return best
controls=[];totalreads=0;birthchecks=0
for control in rr['finite_histories']:
 B={tuple(p)for p in control['seed']};p=(0,0);h=control['start_heading'];terms=[(z,(0,0),1)for z in sorted(B)];birth={z:('initial',z)for z in B};clock=0;rows=[]
 for record in control['macros']:
  hit=explicit_hit(B,p,h);z=op.next_collision(terms,p,h)
  if hit is None:assert z['kind']!='collision'and record['kind']=='certified no hit';break
  t,x,hin=hit;assert(z['blank_duration'],z['consumed_cell'],z['incoming_heading'])==hit;old=set(B);origin=p;oh=h;parent=birth[x]
  for j in range(t+1):
   c='L'if p in B else'R'
   if j<t:assert p not in old
   else:assert p==x and c=='L'and birth[p]==parent
   if c=='L':B.remove(p);del birth[p]
   else:B.add(p);birth[p]=('R',clock+j)
   h=(h+(1 if c=='R'else-1))%4;p=add(p,V[h]);totalreads+=1
  E=expand(z['emitted_terms']);assert E.isdisjoint(old)and expand(z['new_terms'])==B and(p,h)==z['new_pose']and len(B)==len(old)-1+len(E)
  for child in E:
   local=rotate(sub(child,origin),-oh);assert birth[child]==('R',clock+op.blank_birth(local,t));assert clock<=birth[child][1]<clock+t;birthchecks+=1
  assert record['blank_duration']==t and record['emitted_mass']==len(E)and record['final_mass']==len(B);rows.append((clock,t,len(E),len(B)));clock+=t+1;terms=z['new_terms']
 assert clock==control['final_clock']and B=={tuple(z)for z in control['full_final_black']};controls.append(dict(seed=control['seed'],macros=rows,final_clock=clock,final_mass=len(B)))
# Symbolic enormous emission: exact term construction, no materialization.
K=10**9;x=add(HP[0],scale(K,d));z=op.next_collision([(x,(0,0),1)]);candidates=[9977+104*k+i for i,q in enumerate(HP)if(k:=mult(sub(x,q),d))is not None and k>=0];t=min(candidates);assert t==104000009905==z['blank_duration'];kk,r=divmod(t-9977,104);prefixmask=set()
for q in HP[:r]:prefixmask.symmetric_difference_update({q})
expected=[(q,(0,0),1)for q in sorted(TB)]+[(q,d,kk)for q in sorted(mask)]+[(add(q,scale(kk,d)),(0,0),1)for q in sorted(prefixmask)];assert z['emitted_terms']==expected and len(expected)==757
z2=op.next_collision(z['new_terms'],*z['new_pose']);assert z2['blank_duration']==0 and first_ray(z['new_terms'],z['new_pose'][0],d)==0
# Independent necessary-and-sufficient tail check on exact full XOR field.
def verify(terms,p,h,w):
 Q,heads,end,eh=geom(w,p,h);dv=sub(end,p)
 if eh!=h or dv==(0,0):return False
 for i,q in enumerate(Q):
  iv=intervals(terms,q,dv);steps=[];const=0;tests={0}
  for a,b in iv:tests.update((a,b+1))
  for j,y in enumerate(Q):
   k=mult(sub(y,q),dv)
   if k is not None and k>0:steps.append(k);tests.add(k)
   elif k==0 and j<i:const^=1
  for n in tests:
   color=(sum(a<=n<=b for a,b in iv)+const+sum(n>=s for s in steps))%2
   if color!=(w[i]=='L'):return False
 return True
positive=0
for row in ar['all104_standard_phase_controls']:
 B={tuple(q)for q in row['full_black']};p=tuple(row['pose'][0]);h=row['pose'][1];terms=[(q,(0,0),1)for q in B];w=row['certificate']['period'];assert verify(terms,p,h,w);actual=ab.standard_certificate(terms,p,h);assert actual is not None and actual['period']==w;positive+=1
negative=[]
for row in ar['defect_prefix_controls']:
 B={tuple(q)for q in row['full_black']};p=tuple(row['pose'][0]);h=row['pose'][1];terms=[(q,(0,0),1)for q in B];passing=[i for i in range(104)if verify(terms,p,h,H[i:]+H[:i])];assert bool(passing)==(row['time']in(262,308));negative.append((row['time'],passing))
assert not any(verify(z['new_terms'],*z['new_pose'],H[i:]+H[:i])for i in range(104))
# Fresh direct physical reconstruction at all90 model boundaries, not just supplied endpoints.
seed={tuple(q)for q in ar['defect_prefix_controls'][0]['full_black']};B=set(seed);p=(0,0);h=1;terms=[(q,(0,0),1)for q in B];clock=0;events=[]
while True:
 step=ab.absorbing_step(terms,p,h)
 if step['kind']!='collision':assert step['kind']=='ABSORBED exact full-board standard104'and verify(terms,p,h,step['certificate']['period']);break
 hit=explicit_hit(B,p,h);assert hit[0]==step['blank_duration'];old=set(B)
 for j in range(step['total_duration']):
  if j<step['blank_duration']:assert p not in old
  else:assert p in old and p==step['consumed_cell']
  c='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=add(p,V[h])
 clock+=step['total_duration'];terms=step['new_terms'];assert expand(terms)==B and(p,h)==step['new_pose'];events.append((clock,step['total_duration']));assert clock<=264
assert clock==264 and len(events)==90 and B=={tuple(q)for q in ar['defect_absorbing_event_run']['absorption']['full_black']}
assert ab.absorbing_step([])['kind']=='ABSORBED exact no-old-contact blank capture'
std=[]
for i in range(104):
 w=H[i:]+H[:i];j=next(j for j,c in enumerate(C)if c!=w[j%104]);assert(C[j],w[j%104])==('R','L');std.append(j)
assert std==rr['standard_phase_blank_agreement_lengths']and max(std)==10
out=dict(status='PASS total exact full-board XOR-segment collision operator and sound/complete standard-tail absorbing predicate, NOT universal absorption',bindings=manifest,independent_reference_report=sha(S.with_name('check_pristine_cohort_advance_independent.json')),independent_ray_controls=nray,finite_macro_controls=controls,all_fine_reads_checked=totalreads,emitted_last_R_births_checked=birthchecks,huge_control=dict(K=K,first_collision=t,emission_terms=757,next_collision=0,materialized=False),all104_standard_phase_predicates=positive,defect_predicate_checks=negative,defect_exact_absorption_clock=264,defect_collision_events=90,raw_standard_agreement_lengths=std,analytic_review=[
'Before first old-at-cut cell read, the full actual field differs from blank exactly by untouched B. First contact is therefore an actual L against blank firstR. Complete emission E_t is disjoint from B and excludes selectedx; successor is B-minusx union E_t with the literal L heading. This holds even at t0 and for initially BLACK head. No active-component or historical archive is discarded.',
'Allowed finite XOR diagonal segments are closed under complete emission: E715 points XOR32 finite full-period translates XOR partial104 mask, then old terms and consumed point toggle. The exact supplied715 field is independently signed. All geometry uses integers; arbitrary finite segment lengths need no expansion.',
'Point, parallel/antiparallel and nonparallel determinant intersections exhaust segment/ray contact. Nonparallel solution k=cross(z,v)/det and j=cross(z,d)/det is correctly signed and clipped; parallel lattice offset and direction sign produce an interval. XOR endpoint sweep returns exact first support index, including cancellations. Finite-prefix FIRST positions plus all104 rays therefore give a total next-event map.',
'Full current emitted lifetimes are identified by their actual lastR in the blank prefix/tail. Their births lie from macroentry through strictly before parent consumption, and surviving old siblings persist. Mass is m_next=m-1+|E|. Finite-root, finitely branching interleaving genealogy is exact but may be infinite; raw standard itself has a new collision within11 moves at every phase.',
'The absorbing predicate tests complete-board initial color plus all previous proposed-word visits at every integer interval/threshold change and the final constant region. This is necessary and sufficient for the proposed cyclic104 future, not a repeat-count test. Only known104 cyclic words are in API theorem scope; arbitrary-period certify_word uses are not asserted.',
'Every successful predicate or no-old-contact branch certifies actual standard capture. Conversely any actual standard tail eventually reaches a macro boundary at or after its onset unless a no-contact branch already certified capture: finite positive macro durations preclude Zeno behavior. At that boundary one of104 cyclic tests must pass. Thus event-model absorption is EQUIVALENT to actual capture, not proof of universal absorption or an attraction invariant.',
'Fresh controls cover all104 standard full phases; complete defect0/104/261 fail and262/308 pass. Ninety exact collision macros on the full defect board absorb at264, or266 with its two-move preparation. Earliest word onset262/264 and selected recordguard308/310 remain distinct. Huge104-billion-move control is symbolic, not simulated.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('rays',nray,'fine reads',totalreads,'births',birthchecks,'absorb',clock)
