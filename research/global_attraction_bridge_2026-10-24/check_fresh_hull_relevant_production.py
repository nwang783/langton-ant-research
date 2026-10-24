"""Exact spatial ledger for the frozen literal minimal-cohort control."""
from pathlib import Path
import json,hashlib,collections
P=Path(__file__).parent
j=json.loads((P/'MINIMAL_COHORT_RESTART_CHECKED.json').read_text())
states={s['time']:s for s in j['selected_complete_states']}
S={t:{tuple(b['cell']):b for b in s['black'] if b['relevant']} for t,s in states.items()}
allS={t:{tuple(b['cell']):b for b in s['black']} for t,s in states.items()}
n=(1,-1);dot=lambda q:q[0]-q[1]
t,u=0,104;d=tuple(states[u]['pose'][i]-states[t]['pose'][i] for i in range(2))
assert d==(2,-2) and states[t]['heading']==states[u]['heading']==1
assert max(map(dot,allS[t]))==-1 and all(dot(q)<4 for q in allS[u])
assert len(S[t])==14 and len(S[u])==23
assert all(b['death']<=70 for b in S[t].values())
assert all(b['lifetime'][0]=='R' and 0<=b['lifetime'][1]<u for b in S[u].values())
fresh={q:b for q,b in S[u].items() if dot(q)>=0}
assert len(fresh)==17 and all(dot(q)<=3 for q in fresh)
layers={k:sorted(q for q in fresh if dot(q)==k) for k in range(4)}
assert [len(layers[k]) for k in range(4)]==[5,4,4,4]
normalized={(q[0]-d[0],q[1]-d[1]) for q in S[u]}
added=sorted(normalized-set(S[t]));missing=sorted(set(S[t])-normalized)
assert len(added)==11 and len(missing)==2
first3=sorted(S[u].values(),key=lambda b:b['death'])[:3]
assert [(b['lifetime'],b['death'],dot(b['cell'])) for b in first3]==[(['R',17],109,3),(['R',102],110,2),(['R',27],135,3)]
norm_support=lambda cells:{'normal_min':min(map(dot,cells)),'normal_max':max(map(dot,cells)),'tangent_min':min(x+y for x,y in cells),'tangent_max':max(x+y for x,y in cells)}
report=dict(status='AUTHOR exact spatial countercontrol; independent audit pending',dependency_sha256=hashlib.sha256((P/'MINIMAL_COHORT_RESTART_CHECKED.json').read_bytes()).hexdigest(),normal=n,entry=t,exit=u,displacement=d,normal_advance=dot(d),entry_original_cohort_size=len(S[t]),entry_cohort_latest_death=70,exit_relevant_size=len(S[u]),exit_complete_size=len(allS[u]),fresh_side_relevant_size=len(fresh),fresh_side_layer_counts={k:len(v) for k,v in layers.items()},fresh_side_lifetimes=[b for q,b in sorted(fresh.items())],next_three_inputs=first3,normalized_added=added,normalized_missing=missing,entry_normalized_support=norm_support(S[t]),exit_normalized_support=norm_support(normalized),exact_inequalities={'unit_retirement_charge_fails':'17 > 14','full_relevant_replacement_gain':23-14,'normal_advance':4,'required_linear_displacement_coefficient_for_nonincrease':'alpha >= 9/4'},scope='Finite same-normal pristine-to-pristine production; no repeatability, no all-seed budget exclusion, no claim every newly born bit is at a globally unvisited site.')
(P/'FRESH_HULL_RELEVANT_PRODUCTION_CHECKED.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['fresh_side_lifetimes']}))
