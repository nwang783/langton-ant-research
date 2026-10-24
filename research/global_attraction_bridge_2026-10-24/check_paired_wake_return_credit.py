"""Pair the defect with its correctly filled guard, retaining lifetime fates."""
import json
from pathlib import Path
P=Path(__file__).parent
j=json.loads((P/'MINIMAL_COHORT_RESTART_CHECKED.json').read_text())
seed={tuple(q) for q in j['initial_seed']}|{(-3,-2)}
word=j['terminal_word'];D=((0,1),(1,0),(0,-1),(-1,0))
def multiple(v):
    if v[0]%2:return None
    k=v[0]//2
    return k if v[1]==-2*k else None
Q=[];p=(0,0);h=1
for w in word:
    Q.append(p);h=(h+(1 if w=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
assert p==(2,-2) and h==1
parity=[]
for i,q in enumerate(Q):
    thresholds=[];hits=[];critical={0}
    for z,r in enumerate(Q):
        m=multiple((r[0]-q[0],r[1]-q[1]))
        if m is not None and (m>0 or (m==0 and z<i)):thresholds.append(m);critical.add(m)
    for r in seed:
        k=multiple((r[0]-q[0],r[1]-q[1]))
        if k is not None and k>=0:hits.append(k);critical|={k,k+1}
    for k in critical:
        assert (sum(k==a for a in hits)+sum(k>=a for a in thresholds))%2==(word[i]=='L')
    parity.append(dict(phase=i,initial_hits=hits,earlier_thresholds=thresholds,tested_periods=sorted(critical)))
B={q:('I',i) for i,q in enumerate(sorted(seed))};p=(0,0);h=1;births={};deaths={};events=[]
for t,w in enumerate(word):
    q=p;l=B.pop(q,None)
    if l is None:
        B[q]=('R',t);births[t]=q;h=(h+1)%4;actual='R'
    else:deaths[l]=t;h=(h-1)%4;actual='L'
    assert actual==w
    events.append(dict(time=t,cell=q,turn=actual,consumed=l))
    p=(q[0]+D[h][0],q[1]+D[h][1])
assert p==(2,-2) and h==1 and len(B)==27
terminal=[]
for q,l in B.items():
    visits=[]
    for i,r0 in enumerate(Q):
        r=(r0[0]+2,r0[1]-2);k=multiple((q[0]-r[0],q[1]-r[1]))
        if k is not None and k>=0:visits.append(104+104*k+i)
    death=min(visits) if visits else None
    if death is not None:deaths[l]=death
    terminal.append(dict(cell=q,lifetime=l,death=death))
base_permanent={t:q for t,q in births.items() if ('R',t) not in deaths}
actual_deaths={tuple(e['consumed']):e['time'] for e in j['events'] if e['consumed'] is not None}
actual_deaths.update({tuple(b['lifetime']):b['first_future_read'] for b in j['terminal_cohort_first_reads'] if b['first_future_read'] is not None})
actual_births={e['time']:tuple(e['cell']) for e in j['events'][:104] if e['turn']=='R'}
actual_permanent={t:q for t,q in actual_births.items() if ('R',t) not in actual_deaths}
common_early=[]
for t,q in sorted(base_permanent.items()):
    if t<71 and actual_births.get(t)==q and ('R',t) in actual_deaths:
        common_early.append(dict(birth=t,cell=q,baseline_death=None,defect_death=actual_deaths['R',t]))
assert common_early==[dict(birth=44,cell=(2,2),baseline_death=None,defect_death=168),dict(birth=46,cell=(1,1),baseline_death=None,defect_death=166),dict(birth=52,cell=(-2,2),baseline_death=None,defect_death=200),dict(birth=58,cell=(-3,1),baseline_death=None,defect_death=210)]
assert len(births)==len(actual_births)==58 and word.count('L')==46
assert len(base_permanent)==12 and len(actual_permanent)==3
assert 14+(58-3)-46==23 and 15+(58-12)-46==15
report=dict(status='AUTHOR paired finite/infinite lifetime control; independent audit pending',baseline_seed=sorted(seed),baseline_pose=[[0,0],1],baseline_word=word,baseline_ray_parity=parity,baseline_events=events,baseline_full_state104=terminal,baseline_permanent_births=[dict(birth=t,cell=q) for t,q in sorted(base_permanent.items())],defect_permanent_births=[dict(birth=t,cell=q) for t,q in sorted(actual_permanent.items())],common_prefix_births_with_different_fates=common_early,balance=dict(R=58,L=46,baseline_returned_R=46,baseline_permanent_R=12,baseline_relevant_change=0,defect_returned_R=55,defect_permanent_R=3,defect_relevant_change=9),scope='Different initial fields, same four actual birth events before first divergence; no lifetime that is permanently unread in one actual trajectory later reactivates in that trajectory.')
(P/'PAIRED_WAKE_RETURN_CREDIT_CHECKED.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(balance=report['balance'],common_prefix_births_with_different_fates=common_early,baseline_parity_tests=sum(len(x['tested_periods']) for x in parity))))
