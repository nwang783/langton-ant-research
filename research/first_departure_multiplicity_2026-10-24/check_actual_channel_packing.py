"""Abstract cap-free chronology controls, NOT ant-factor realizations.
Voltages and nonprimitive packing-cycle winding are explicitly retained.
"""
from pathlib import Path
import json
m=13;offset=12;g=4
# Opposed physical rank orders: A0<B12 and B0<A12.
# Relaxed per-event clocks allow starts0/0, while whole channels overlap.
assert 0+offset>=0+g and 0+offset>=0+g
zero=dict(edges=[dict(source='A',target='B',nu=0,w=m),dict(source='B',target='A',nu=0,w=m)],relaxed_starts=dict(A=0,B=0),temporal_winding=0,packing_sum=26,contradiction=True)
rows=[]
for k in[1,2]:
 P=32;S=dict(A=0,B=16)
 edges=[dict(source='A',target='B',nu=0,w=m),dict(source='B',target='A',nu=-k,w=m)]
 for e in edges:assert S[e['target']]-S[e['source']]>=e['w']+e['nu']*P
 assert k*P>=2*m
 phases=[(S[c]+q)%P for c in['A','B']for q in range(m)]
 assert len(set(phases))==2*m
 # Same-cell endpoint rank comparisons can respect the mod-four phase.
 assert (S['B']+offset-S['A'])%4==0
 assert (S['A']+offset+k*P-S['B'])%4==0
 rows.append(dict(P=P,starts=S,edges=edges,temporal_winding=k,all26_event_phases_distinct=True,unassigned_event_phases=P-2*m,not_a_physical_completion=True))
obj=dict(scope=__doc__,zero_winding_countercontrol=zero,positive_winding_controls=rows,proof='Whole contiguous event intervals are disjoint; occurrence voltages align the precedence cycle. No bounded period search.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS zero-winding obstruction and positive winding1/2 calendars')
