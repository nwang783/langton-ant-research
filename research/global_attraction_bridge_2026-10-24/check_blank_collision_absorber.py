"""All104 actual standard phases plus complete defect-control and no-contact regressions."""
import json
from pathlib import Path
from blank_collision_absorber import *
P=Path(__file__).parent
source=json.loads((P/'OUTWARD_RECORD_GUARDS_CHECKED.json').read_text())['normal_catalog'][2]['records'][0];J=set(map(tuple,source['required_black']));W=source['cycle_word'];B=set(J);p=(0,0);h=1;controls=[]
for i in range(104):
 terms=[(x,(0,0),1)for x in sorted(B)];c=standard_certificate(terms,p,h);assert c is not None and c['drift']==(2,-2)
 assert c['period']==W[i:]+W[:i]
 controls.append(dict(phase=i,full_black=sorted(B),pose=[p,h],certificate=c))
 a=W[i];assert(p in B)==(a=='L');B^={p};h=(h+(1 if a=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
# Negative fields cannot pass merely because a few periods or a local patch look favorable.
B=J-{(-3,-2)};p=(0,0);h=1;neg=[]
for t in range(309):
 if t in(0,104,261,262,308):
  c=standard_certificate([(x,(0,0),1)for x in sorted(B)],p,h);assert bool(c)==(t>=262)
  neg.append(dict(time=t,full_black=sorted(B),pose=[p,h],certificate=c))
 if t==308:break
 a='L'if p in B else'R';B^={p};h=(h+(1 if a=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
# Follow the absorbing event model on the entire defect field until its real certified boundary.
terms=[(x,(0,0),1)for x in sorted(J-{(-3,-2)})];p=(0,0);h=1;clock=0;events=[]
for j in range(400):
 z=absorbing_step(terms,p,h)
 if z['kind']!='collision':
  assert clock>=262 and z['kind']=='ABSORBED exact full-board standard104';absorbed=dict(time=clock,event=j,pose=[p,h],certificate=z['certificate'],full_black=sorted(materialize(terms)));break
 events.append(dict(time=clock,duration=z['total_duration'],collision=z['consumed_cell']))
 clock+=z['total_duration'];terms=z['new_terms'];p,h=z['new_pose']
else:raise AssertionError('finite positive regression failed to absorb')
assert absorbing_step([])['kind']=='ABSORBED exact no-old-contact blank capture'
# Long segment input to the predicate is tested symbolically without materializing it.
K=10**9;x=(HP[0][0]+K*DR[0],HP[0][1]+K*DR[1]);z=next_collision([(x,(0,0),1)]);large=standard_certificate(z['new_terms'],*z['new_pose']);assert large is None
out=dict(status='AUTHOR exact absorbing collision model controls; independent audit pending',all104_standard_phase_controls=controls,defect_prefix_controls=neg,defect_absorbing_event_run=dict(events=events,absorption=absorbed),empty_board_no_contact_absorbs=True,billion_period_emission_is_not_falsely_certified=True)
(P/'BLANK_COLLISION_ABSORBER_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n');print(dict(standard_phases=104,defect_absorption_time=absorbed['time'],collision_events=len(events),large_terms=len(z['new_terms'])))
