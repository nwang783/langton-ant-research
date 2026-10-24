from pathlib import Path
import importlib.util,json,hashlib,sys,random
from collections import Counter
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'reframe_finite_seed_2026-10-24'
spec=importlib.util.spec_from_file_location('author_active_flight',D/'active_flight.py');A=importlib.util.module_from_spec(spec);sys.modules[spec.name]=A;spec.loader.exec_module(A)
p=SELF.parent/'check_cycle_birth_finite_fuel_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('cells=')[0],ns)
ends,component,step,wvertex=[ns[k]for k in('ends','component','step','wvertex')]
def xy(z):return int(z.real),int(z.imag)
stat=Counter();maxevent=0;maxph=0;witness=[]
def check(B0,p0,h0,M):
 global maxevent,maxph
 B=set(B0);p=p0;h=h0;lattice=int(wvertex(p,h).real+wvertex(p,h).imag)%4
 plan=A.plan(set(map(xy,B)),xy(p),h,M)
 assert plan.status!='translator','Finite test fixture unexpectedly needs infinite-certificate checking'
 for t in range(plan.event+1):
  bb,pp,hh=plan.state_at(t);assert(set(map(lambda q:complex(*q),bb)),complex(*pp),hh)==(B,p,h)
  verts,C=component(B,lattice,wvertex(p,h));kind=None
  if len(C)>M:kind='cap'
  elif p not in B:
   e0,e1=ends(p,lattice);other=e1 if e0==wvertex(p,h)else e0
   oldD=component(B,lattice,other)[1]
   if oldD and oldD!=C:kind='import'
  if kind:
   assert(t,kind)==(plan.event,plan.status)
   if kind=='import':
    updated=set(B);pn,hn,ch=step(updated,p,h);Cnew=component(updated,lattice,wvertex(pn,hn))[1]
    assert Cnew==C|oldD|{p};stat['exact_whole_component_imports']+=1
   break
  assert t<plan.event
  p,h,ch=step(B,p,h);stat['literal_updates']+=1
 stat['cases']+=1;stat[plan.status]+=1;stat['repeated_predictor_cases']+=int(plan.period>0);maxevent=max(maxevent,plan.event);maxph=max(maxph,len(plan.phases));return plan
cells=[complex(x,y)for x in range(-1,2)for y in range(-1,2)]
for mask in range(512):
 B={q for i,q in enumerate(cells)if mask>>i&1}
 for h in range(4):
  for M in(0,1,3,6):check(B,0j,h,M)
rng=random.Random(244052)
for j in range(150):
 shift=complex(rng.randrange(-25,26),rng.randrange(-25,26));B={complex(x,y)+shift for x in range(-6,7)for y in range(-6,7)if rng.random()<.21}
 # Keep a remote complete component, never a cropped field.
 B|={shift+70+70j,shift+71+70j,shift+70+71j,shift+71+71j}
 check(B,shift,rng.randrange(4),rng.choice((2,9,30,70)))
s=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text());B={complex(*q)for q in s['seed']};p=0j;h=s['heading']
for phase in range(104):
 a=check(B,p,h,70)
 if phase in(0,7,38,84):witness.append({'phase':phase,'event':a.event,'period':a.period,'drift':a.drift,'collision':a.witness})
 p,h,ch=step(B,p,h)
a=check(set(),0j,0,10);assert(a.status,a.event,a.period,a.drift)==('import',8,20,(0,0));witness.append({'blank':True,'event':a.event,'period':20,'drift':(0,0),'collision':a.witness})
# Derive first periodic collision independently by brute chronology; author
# ray_epoch is tested, not reused to calculate the expected result.
for trial in range(6000):
 P=rng.randrange(1,10);d=(rng.randrange(-3,4),rng.randrange(-3,4));i=rng.randrange(P);j=rng.randrange(P);q=(rng.randrange(-8,9),rng.randrange(-8,9));v=(rng.randrange(-8,9),rng.randrange(-8,9))
 brute=None
 for k in range(34):
  if any(l*P+j<k*P+i and(q[0]+k*d[0],q[1]+k*d[1])==(v[0]+l*d[0],v[1]+l*d[1])for l in range(k+1)):
   brute=k;break
 if d==(0,0):n=(0 if j<i else 1)if v==q else None
 else:n=A.ray_epoch(v,q,d)
 if n is not None and(n<0 or(n==0 and j>=i)):n=None
 assert n==brute;stat['synthetic_chronology_cases']+=1
N=10**40;assert A.ray_epoch((3*N+1,-2*N+4),(1,4),(3,-2))==N
# Synthetic finite-run representation at a huge index. This tests arithmetic
# only and is NOT represented as a physical ant path.
P0=A.Phase((0,0),0,frozenset({(0,0)}),'L',None,frozenset({(-1,0)}));P1=A.Phase((1,0),1,frozenset({(1,0)}),'L',None,frozenset({(0,-1)}));z=A.Plan('import',2*N+1,3,0,2,(4,2),[P0,P1],frozenset({(-10,-10)}),1)
ph,terms=z.archive_terms(2*N+1);assert ph.p==(4*N+1,2*N)and ph.C==frozenset({(4*N+1,2*N)})
assert terms==[(frozenset({(-10,-10)}),(0,0),1),(frozenset({(-1,0)}),(4,2),N),(frozenset({(0,-1)}),(4,2),N),(frozenset({(4*N-1,2*N)}),(0,0),1)]
mp=D/'manifest.json';mf=json.loads(mp.read_text());mh=hashlib.sha256(mp.read_bytes()).hexdigest()
for f,h in mf['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
clarification=hashlib.sha256((D/'LIFETIME_METADATA_CLARIFICATION.md').read_bytes()).hexdigest();assert clarification=='489ab3483875166fb0a953134771ac5e6332e51960b42b05c497d68c49c85ffd'
out={'status':'PASS total exact first-import/cap active-flight reduction and complete chronological field representation','author_manifest_sha256':mh,'mandatory_metadata_clarification_sha256':clarification,'author_note_sha256':mf['files']['EXACT_ACTIVE_COMPONENT_FLIGHT.md'],'independent_controls':dict(stat),'maximum_event':maxevent,'maximum_predictor_phases':maxph,'examples':witness,'analytic':['For every pre-import state, active and dormant occupied vertex sets are disjoint. L affects only the active component and emits complete disjoint components; R to an active vertex cannot hit a dormant edge. An R to a new endpoint is the sole potential first import. If an emitted fragment could meet an older archive, its immediately preceding active history would already contain the first such R query. Thus query-versus-earlier-emission testing includes emitted/emitted collisions.','The isolated component predictor is not asserted physical after its first collision. Its earliest algebraic collision nevertheless is physical by induction on update time: every referenced emission precedes that query, so no later hypothetical archive can create an earlier spurious deviation. Cap priority is tested at pre-update cuts; an import that would cause a post-R overflow is correctly reported before that overflow.','Active connected mass<=M pins its edges to the head-relative square[-M,M]^2, including empty M0 and every R-only cut. Heading and finite relative edge set therefore give finitely many predictor states. A repeated heading forces even physical displacement parity, preserving the same fixed diagonal lattice. Finite cap failure or finite shape repetition is guaranteed, without a numerical simulation horizon.','For periodic query q_i+kD and emission v+ell D, equality gives v-q_i=(k-ell)D. Chronology forces n>0 or n0,j<i. For nonzero D the integer solution is unique; its earliest realization is k=n,ell0. For zero D equal vertices collide in cycle0 if j<i, otherwise cycle1. Static/preperiod emissions are eligible from cycle0; actual preperiod queries separately use only strictly prior emissions. All cases are finite integer arithmetic.','If no collision candidate exists, the entire predictor is actual. A zero-drift periodic predictor would keep the physical head in a bounded finite region forever, impossible by the retained no-bounded-orbit theorem; therefore the remaining infinite certificate has nonzero drift and restored heading. No supplied control is claimed to realize that branch.','Before the first event, full field is active plus initial archives plus strictly earlier emitted edge sets. Each whole prior period contributes a finite translation run, current period only j<i. All are current edge lifetimes, not XOR-cancelled or silently discarded; identity equality has never been read while dormant. Current implementation records detachment phase, not a separate original R-birth timestamp for each edge. Its promised complete-field and first-event outputs are exact.','The finite quantitative collision estimates follow from query distance<=P+1/2 and emitted vertex distance<=P+M+1/2 from cycle-start head. A nonzero integer drift coordinate bounds static epoch byceil(R)+P+1 and emission gap by2P+M+1. These are per-flight bounds depending on the complete archive position, not mass-only or total-import budgets.'],'scope':'Complete finite input field and integer active cap. Exact first nonempty dormant R import, earlier cap failure, or certified infinite nonzero translating no-import tail. No standard104 classification, universal capture, undecidability or finite closed state for successive imports. Synthetic arithmetic/run tests are not physical examples.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(stat)
