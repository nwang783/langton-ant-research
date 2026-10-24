from pathlib import Path
from itertools import product
import json,hashlib,sys,importlib
P=Path(__file__);R=P.parent.parent;S=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();bind={}
for name in('COLLISION_NORMAL_SPAN_MANIFEST.json','AXIS_BLACK_MASS_OBSTRUCTION_MANIFEST.json'):
 m=json.loads((S/name).read_text());bind[name]=sha(S/name)
 for f,h in m['files'].items():assert sha(S/f)==h;bind[f]=h
assert bind['COLLISION_NORMAL_SPAN.md']=='97b29b89f2f85bab2bb76483e94230a79ae6b8600ef5812917eb15e560d92dac'and bind['AXIS_BLACK_MASS_OBSTRUCTION.md']=='cf36fa42eeb2dab93339e8b8379c0aa84cf2a37c35ad5e5dc7587b6a81cb6bc7'
sys.path.insert(0,str(S));op=importlib.import_module('blank_collision_operator');C,H=op.C,op.H;V=(1j,1,-1j,-1);xy=lambda p:(int(p.real),int(p.imag));B=set();p=0j;h=0;reads=[]
for a in C+H:
 assert(p in B)==(a=='L');reads.append(p);B.symmetric_difference_update({p});h=(h+(1 if a=='R'else-1))%4;p+=V[h]
cp=reads[:len(C)];hp=reads[len(C):];assert len(C)==9977 and len(H)==104 and p-hp[0]==-2-2j;dr=-2-2j;norms=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)];dot=lambda n,q:n[0]*q.real+n[1]*q.imag
rows=[]
for n in norms:
 A=max(dot(n,q)for q in cp);hi=max(dot(n,q)for q in hp);lo=min(dot(n,q)for q in hp);delta=dot(n,dr);K=max(0,A,hi if delta<=0 else hi-lo);assert K>=1
 assert all(dot(n,q)<=K for q in cp)
 if delta<=0:assert all(dot(n,q)<=K for q in hp)
 else:assert all(dot(n,q)-dot(n,r)<=K for q,r in product(hp,hp))
 rows.append({'normal':list(n),'prefix_max':A,'tail_max':hi,'tail_min':lo,'tail_drift_projection':delta,'endpoint_span':K})
ref=json.loads((S/'COLLISION_NORMAL_SPAN_CHECKED.json').read_text());assert rows==ref['canonical_rows']and max(r['endpoint_span']for r in rows[:4])==29 and max(r['endpoint_span']for r in rows[4:])==48
controls=[]
for r in ref['huge_and_prefix_controls']:
 rot=r['heading'];t=r['requested_reference_time'];k,j=divmod(t-len(C),104);q=cp[t]if t<len(C)else hp[j]+k*dr;x=q*(-1j)**rot;z=op.next_collision([(xy(x),(0,0),1)],(0,0),rot);assert z['kind']=='collision'and z['blank_duration']==r['actual_collision_time']and list(z['consumed_cell'])==r['consumed_cell']and len(z['emitted_terms'])==r['terms'];c=complex(*z['consumed_cell'])
 for n in norms:
  K=29 if 0 in n else 48;limit=max(0,dot(n,c))+K;assert dot(n,complex(*z['new_pose'][0]))<=limit
  for b,v,L in z['emitted_terms']:assert max(dot(n,complex(*b)),dot(n,complex(*b)+(L-1)*complex(*v)))<=limit
 controls.append({'heading':rot,'requested':t,'actual':z['blank_duration'],'terms':len(z['emitted_terms'])})
# Two complete singleton RRRL controls, direct physical replay and explicit finite rejection of EVERY104 cyclic standard word.
potential=[]
for heading,old,eh,ep,EB in[(1,-1,3,-2,{0,-1j,-1-1j}),(3,1,1,2,{0,1j,1+1j})]:
 B={complex(old)};p=0j;h=heading;states=[(set(B),p,h)];log=[]
 for t,a in enumerate('RRRL'):
  assert(p in B)==(a=='L');log.append([t,*xy(p),h,a]);B.symmetric_difference_update({p});h=(h+(1 if a=='R'else-1))%4;p+=V[h]
 assert(B,p,h)==(EB,ep,eh);states.append((set(B),p,h));z=op.next_collision([(xy(complex(old)),(0,0),1)],(0,0),heading);assert z['blank_duration']==3 and z['total_duration']==4 and {complex(*q)for q in op.materialize(z['new_terms'])}==B
 fails=[]
 for bb,pp,hh in states:
  actual=[]
  for _ in range(208):
   a='L'if pp in bb else'R';actual.append(a);bb.symmetric_difference_update({pp});hh=(hh+(1 if a=='R'else-1))%4;pp+=V[hh]
  witnesses=[]
  for i in range(104):
   ww=H[i:]+H[:i];bad=next(j for j,a in enumerate(actual)if a!=ww[j%104]);witnesses.append(bad)
  fails.append(witnesses)
 before=Counter()if False else None
 potential.append({'heading':heading,'read_log':log,'final_field':sorted(map(xy,B)),'final_pose':[*xy(p),h],'all104_standard_rotations_fail_initial_and_final_at':fails})
out={'status':'PASS completed-macro axis29/diagonal48 span and narrowly specified absolute-axis mass-potential obstruction','bindings':bind,'literal_normal_rows':rows,'huge_controls':controls,'potential_controls':potential,'analytic_review':[
'Complete physical blank C9977+H104 geometry and every finite inequality were reconstructed. For positive normal drift, earlier tail period l<=selected period k gives normal(q_l-x_k)<=B-b; for nonpositive drift the entire tail is <=B. Prefix maxima remain separately retained. Proper rotations permute each normal family. No finite flight-length scan is a premise.',
'Every emitted identity is born at a prior read; actual contact successor is one step from selected old cell and covered since K>=1. Full unchanged old archives are NOT bounded or deleted. The20 exact signed-operator controls include huge10^9-period inputs with every emitted segment endpoint checked, but the all-length conclusion is analytic.',
'Each next entry is one step from the previous selected input, so a FIXED input band yields uniform padding30/49 without cumulative error. At a current pristine record, the selected input is still BLACK and lies behind it, but will be consumed in the FUTURE. This is not an injective backward charge or a budget on regenerated out-of-band inputs.',
'The two independent singleton RRRL histories and their full fields are literal. All104 cyclic standard candidates fail within208 physical reads at BOTH initial and final states, so the absorber exception cannot remove either. In absolute horizontal layers the mass changes are exactly2f(-1),2f(1); headheight remains0 and E/W credits cancel across the two inequalities. If f(-1)+f(1)>0, nonincrease on BOTH is impossible.',
'These are separate histories, not a composable cycle or renewable controller. The no-go applies only to fixed absolute axis-layer positive mass plus tangentially invariant heading/height credit. Diagonal/recentered weights, nonlinear lifetime/archive potentials and unsigned record guards are not addressed. Neither note proves capture or a universal pristine-record bound.'
]};P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(P),sha(P.with_suffix('.json')))
