#!/usr/bin/env python3
"""Complete literal factor proof, no search cutoff or solver verdict.
A four-step physical return is a unit-face loop. Its three noncentral
turns have one common orientation. Four consecutive loops therefore have
only32 possibilities after fixing the initial heading by a genuine rotation.
"""
from itertools import product
from pathlib import Path
import json
D=((0,1),(1,0),(0,-1),(-1,0))
def trace(s,qs):
 p=(0,0);h=3;last={};events=[];failure=None
 for i,q in enumerate(qs):
  for turn in((s if i%2==0 else -s),q,q,q):
   e=dict(time=len(events),cell=p,turn='R' if turn==1 else 'L',heading=h)
   if p in last and last[p]['turn']==e['turn'] and failure is None:failure=dict(first=last[p],second=e)
   last[p]=e;events.append(e);h=(h+turn)%4;p=(p[0]+D[h][0],p[1]+D[h][1])
  assert p==(0,0)
 return events,failure
cases=[]
for s in(1,-1):
 for qs in product((1,-1),repeat=4):
  es,fail=trace(s,qs);assert fail is not None
  cases.append(dict(initial_turn=s,loop_orientations=qs,events=es,failure=fail))
positives=[]
for s in(1,-1):
 for qs in product((1,-1),repeat=3):
  es,fail=trace(s,qs)
  if fail is None:
   first={}
   for e in es:first.setdefault(tuple(e['cell']),e['turn'])
   positives.append(dict(initial_turn=s,loop_orientations=qs,word=''.join(e['turn'] for e in es),input_black=[p for p,t in first.items() if t=='L']))
assert len(positives)==4
r=dict(status='AUTHOR_COMPLETE_FACTOR_CERTIFICATE_PASS',scope='NO_FOUR_CONSECUTIVE_FOUR_STEP_PHYSICAL_RETURNS_ON_ANY_BOARD',cases=cases,three_loop_positive_controls=positives)
root=Path(__file__).parent;root.joinpath('four_unit_returns.certificate.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(dict(status=r['status'],cases=len(cases),three_loop_positives=positives)))
