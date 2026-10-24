"""Literal finite/full-future countercontrol to decreasing relevant-cohort size."""
import json, hashlib
from pathlib import Path

P=Path(__file__).parent
SEED={(-4,1),(-4,2),(-3,-1),(-3,0),(-3,3),(-2,-1),(-2,1),(-2,2),(-2,3),(-1,1),(-1,2),(0,1),(0,2),(1,2)}
DIR=((0,1),(1,0),(0,-1),(-1,0))
NORMALS=((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1))
dot=lambda n,p:n[0]*p[0]+n[1]*p[1]
def rot(p,k):
    x,y=p
    for _ in range(k):x,y=y,-x
    return x,y
def step(B,p,h,t,deaths):
    old=B.pop(p,None)
    if old is None:
        B[p]=('R',t);h=(h+1)%4;turn='R'
    else:
        deaths[old]=t;h=(h-1)%4;turn='L'
    return (p[0]+DIR[h][0],p[1]+DIR[h][1]),h,turn,old

# A real two-step entrance, not a fictitious supporting line.
prep=SEED-{(-1,1)}|{(-1,0)}
B={p:('original',i) for i,p in enumerate(sorted(prep))}
p=(-1,1);h=1;dead={};prep_poses=[];prep_events=[]
for t in (-2,-1):
    prep_poses.append(p);q=p;ih=h;p,h,w,old=step(B,p,h,t,dead)
    prep_events.append(dict(time=t,cell=q,heading=ih,turn=w,consumed=old))
assert set(B)==SEED and p==(0,0) and h==1

# Relabel the chosen-cut cohort, including the R-born preparation lifetime.
B={q:('C0',i) for i,q in enumerate(sorted(B))};dead={}
states=[];poses=[];heads=[];events=[];maxima=[];records=[]
oldmax={n:max(map(lambda p:dot(n,p),prep_poses)) for n in NORMALS}
for t in range(309):
    states.append(dict(B));poses.append(p);heads.append(h);maxima.append(dict(oldmax))
    ns=[n for n in NORMALS if dot(n,p)>oldmax[n] and all(dot(n,q)<dot(n,p) for q in B)]
    if ns:records.append(dict(time=t,mass=len(B),pose=p,heading=h,normals=ns))
    for n in NORMALS:oldmax[n]=max(oldmax[n],dot(n,p))
    if t==308:break
    q=p;ih=h;p,h,w,old=step(B,p,h,t,dead)
    events.append(dict(time=t,cell=q,heading=ih,turn=w,consumed=old))

old=json.loads((P/'SUCCESSIVE_RECORD_DEFECT_SPLIT_CHECKED.json').read_text())
assert ''.join(e['turn'] for e in events)==old['word_to_capture']
assert p==(4,-4) and h==1 and len(B)==54
word=old['period'];assert len(word)==104
Q=[];x,y=p;hh=h
for w in word:
    Q.append((x,y));hh=(hh+(1 if w=='R' else -1))%4
    x+=DIR[hh][0];y+=DIR[hh][1]
d=(x-p[0],y-p[1]);assert d==(2,-2) and hh==h
def ray_multiple(v):
    if v[0]%2:return None
    k=v[0]//2
    return k if v[1]==-2*k else None

# The required bit is a piecewise-constant parity function of k>=0.
# Test every change point, rather than a finite number of guessed periods.
tail_checks=[]
for i,q in enumerate(Q):
    thresholds=[];initial_hits=[];critical={0}
    for j,r in enumerate(Q):
        m=ray_multiple((r[0]-q[0],r[1]-q[1]))
        if m is not None and (m>0 or (m==0 and j<i)):
            thresholds.append(m);critical.add(m)
    for r in B:
        k=ray_multiple((r[0]-q[0],r[1]-q[1]))
        if k is not None and k>=0:initial_hits.append(k);critical|={k,k+1}
    tests=[]
    for k in sorted(critical):
        bit=(sum(k==a for a in initial_hits)+sum(k>=a for a in thresholds))%2
        assert bit==(word[i]=='L')
        tests.append([k,bit])
    tail_checks.append(dict(phase=i,point=q,earlier_read_thresholds=thresholds,initial_black_ray_hits=initial_hits,tests=tests))

# Exact remaining lifetime deaths, including never-read terminal archive.
tail_deaths=[]
for q,lifetime in B.items():
    visits=[]
    for i,r in enumerate(Q):
        k=ray_multiple((q[0]-r[0],q[1]-r[1]))
        if k is not None and k>=0:visits.append(308+104*k+i)
    if visits:dead[lifetime]=min(visits)
    tail_deaths.append(dict(cell=q,lifetime=lifetime,first_future_read=min(visits) if visits else None))
relevant=[{q:l for q,l in s.items() if l in dead and dead[l]>=t} for t,s in enumerate(states)]

catalog=json.loads((P/'OUTWARD_RECORD_GUARDS_CHECKED.json').read_text())
guards=[]
for c in catalog['normal_catalog']:
    for r in c['records']:
        for k in range(4):
            guards.append(dict(phase=r['phase'],rotation=k,heading=(r['normalized_heading']+k)%4,normal=rot(c['outward_normal'],k),black={rot(q,k) for q in r['required_black']},white={rot(q,k) for q in r['required_white']}))
assert len(guards)==32
def guard_matches(field,p,h):
    matches=[]
    for g in guards:
        if h!=g['heading']:continue
        n=g['normal'];bl={(p[0]+q[0],p[1]+q[1]) for q in g['black']};wh={(p[0]+q[0],p[1]+q[1]) for q in g['white']}
        if bl<=set(field) and not wh&set(field) and all(dot(n,q)<dot(n,p) for q in field):
            matches.append([g['phase'],g['rotation'],n])
    return matches
for r in records:
    t=r['time'];r['full_guard_matches']=guard_matches(states[t],poses[t],heads[t])
    r['minimal_guard_matches']=guard_matches(relevant[t],poses[t],heads[t])
    assert bool(r['full_guard_matches'])==(t==308)
    assert bool(r['minimal_guard_matches'])==(t==308)

renewals=[];t=0
while t<308:
    cohort=set(states[t].values());rcohort=set(relevant[t].values())
    consumed=sorted((v,l) for l,v in dead.items() if l in cohort and v>=t)
    assert len(consumed)>=3
    third=consumed[2][0]
    rr=next(r for r in records if r['time']>third);u=rr['time']
    old_live=set(states[u].values())&cohort;new_live=set(states[u].values())-cohort
    old_rel=set(relevant[u].values())&rcohort;new_rel=set(relevant[u].values())-rcohort
    # Prune ALL never-read bits at the entry, retaining the whole later output.
    removed=set(states[t])-set(relevant[t]);pruned_candidates=[]
    for z in range(third+1,309):
        field=set(states[z])-removed
        ns=[n for n in NORMALS if dot(n,poses[z])>maxima[z][n] and all(dot(n,q)<dot(n,poses[z]) for q in field)]
        if ns:pruned_candidates.append((z,ns));break
    renewals.append(dict(start=t,next_record=u,third_consumption=third,full_start=len(cohort),full_end=len(states[u]),full_retired=len(cohort-old_live),full_new_live=len(new_live),relevant_start=len(rcohort),relevant_end=len(relevant[u]),relevant_retired=len(rcohort-old_rel),relevant_new_live=len(new_rel),next_normals=rr['normals'],next_guard_matches=rr['full_guard_matches'],first_record_after_pruning_entry_irrelevant=pruned_candidates[0]))
    t=u
assert [r['start'] for r in renewals]==[0,71,104,169,225]
assert [len(relevant[t]) for t in [0,71,104,169,225,308]]==[14,16,23,25,18,15]
assert all(r['relevant_end']>r['relevant_start'] for r in renewals[:3])
assert [r['third_consumption'] for r in renewals]==[31,93,135,201,256]
assert all(r['first_record_after_pruning_entry_irrelevant'][0]==r['next_record'] for r in renewals)

def fullstate(t):
    return dict(time=t,pose=poses[t],heading=heads[t],black=[dict(cell=q,lifetime=l,death=dead.get(l),relevant=q in relevant[t]) for q,l in sorted(states[t].items())])
def hull(points):
    pts=sorted(set(points))
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[];upper=[]
    for q in pts:
        while len(lower)>=2 and cross(lower[-2],lower[-1],q)<=0:lower.pop()
        lower.append(q)
    for q in reversed(pts):
        while len(upper)>=2 and cross(upper[-2],upper[-1],q)<=0:upper.pop()
        upper.append(q)
    return lower[:-1]+upper[:-1]
def inside(poly,q):
    return all((b[0]-a[0])*(q[1]-a[1])-(b[1]-a[1])*(q[0]-a[0])>=0 for a,b in zip(poly,poly[1:]+poly[:1]))
seed_hull=hull(SEED);geometry=[]
for t in [0,71,104,169,225,308]:
    geometry.append(dict(time=t,relevant_hull=hull(relevant[t]),relevant_outside_original_seed_hull=sorted(q for q in relevant[t] if not inside(seed_hull,q)),normal_supports=[dict(normal=n,seed_max=max(dot(n,q) for q in SEED),head=dot(n,poses[t]),relevant_min=min(dot(n,q) for q in relevant[t]),relevant_max=max(dot(n,q) for q in relevant[t])) for n in NORMALS]))
report=dict(status='AUTHOR full finite/infinite countercontrol; independent audit pending',initial_seed=sorted(SEED),genuine_preparation=dict(initial_seed=sorted(prep),initial_pose=[[-1,1],1],events=prep_events),events=events,all_pristine_records=records,greedy_renewals=renewals,selected_complete_states=[fullstate(t) for t in [0,71,104,169,225,308]],terminal_word=word,terminal_drift=d,terminal_ray_parity=tail_checks,terminal_cohort_first_reads=tail_deaths,geometry=dict(original_seed_hull=seed_hull,cuts=geometry),all_initial_lifetimes_retired_by=max(dead[l] for l in states[0].values()),timing='Local zero is after genuine two-read preparation; 308 is a sufficient guard cut, not earliest standard onset.')
(P/'MINIMAL_COHORT_RESTART_CHECKED.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(records=len(records),tail_parity_tests=sum(len(x['tests']) for x in tail_checks),greedy_renewals=renewals,selected_relevant_sizes=[len(relevant[t]) for t in [0,71,104,169,225,308]])))
