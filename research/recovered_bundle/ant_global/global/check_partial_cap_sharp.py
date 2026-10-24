"""Exact 12-step sharp witness for the partial-cap endpoint constant 14."""
import json
from pathlib import Path
from record_birth import replay,W
seed={(1,-3),(0,-2)}
black,position,heading,events=replay(seed,(0,-4),W,12)
counts={t:sum(sum(e['cell'])==t for e in events) for t in (0,-1,-2,-3)}
deltas={t:sum((-1 if e['black'] else 1) for e in events if sum(e['cell'])==t) for t in (0,-1,-2,-3)}
H=sum(sum(e['cell'])==-1 and e['black'] and e['incoming']==2 and e['outgoing']==1 for e in events)
EB=sum(sum(e['cell'])==-2 and not e['black'] and e['incoming']==3 and e['outgoing']==0 for e in events)
Q=sum(sum(e['cell'])==-1 and e['black'] and e['incoming']==0 and e['outgoing']==3 for e in events)
KC=sum(sum(e['cell'])==-3 and e['black'] and e['incoming']==2 and e['outgoing']==1 for e in events)
M=counts[0];D=EB-M+2*H;Z=KC+2*D+H-Q
base=12*M-8*deltas[-1]+4*deltas[-2]-deltas[-3]
assert position==(2,-2) and heading==1 and position in black
assert all(sum(e['cell'])<=0 for e in events)
assert all(not e['black'] for e in events if sum(e['cell'])==0)
assert counts=={0:1,-1:4,-2:4,-3:2}
assert deltas=={0:1,-1:2,-2:-2,-3:0}
assert H==D==Z==0 and Q==KC==1 and counts[-3]-base==14
result={'seed':sorted(seed),'start':[0,-4,W],'updates':12,'endpoint':[position,heading],
        'events':events,'counts':counts,'deltas':deltas,'M':M,'H':H,'D':D,'Z':Z,
        'Q':Q,'KC':KC,'gap':counts[-3]-base}
Path(__file__).with_name('partial_cap_sharp_witness.json').write_text(json.dumps(result,indent=2)+'\n')
print('Exact fresh-cap endpoint witness passed: +14 is attained.')
