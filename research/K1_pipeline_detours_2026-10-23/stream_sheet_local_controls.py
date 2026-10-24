"""All complete white cap-four local histories, no front/period search."""
from itertools import product
from collections import Counter
from pathlib import Path
import json
rows=[]
for n in range(1,5):
 for hs in product((0,2),repeat=n):
  turns=['R'if i%2==0 else'L'for i in range(n)]
  outs=[(h+(1 if c=='R'else-1))%4 for h,c in zip(hs,turns)]
  r=Counter(h for h,c in zip(hs,turns)if c=='R')
  hSE=r[0]-r[2];hNW=0;hC={0:hSE,2:hNW,1:hSE,3:hNW}
  ins=Counter();outc=Counter();events=[]
  for i,(h,o,c)in enumerate(zip(hs,outs,turns)):
   ins[h]+=1;outc[o]+=1
   a=hC[h]-ins[h]+1;b=hC[o]-outc[o]+1
   events.append(dict(rank=i,turn=c,incoming=h,outgoing=o,in_ordinal=ins[h],out_ordinal=outc[o],in_level=a,out_level=b))
  # Reconstruct all incident L heights from the exact port counts.
  hSW=hSE-ins[0];hNE=hNW-ins[2]
  assert hSE-outc[1]==hNE and hNW-outc[3]==hSW
  assert events[0]['in_level']==events[0]['out_level']
  if n<3:assert all(e['in_level']==e['out_level']for e in events)
  else:
   a,b=events[1],events[2]
   assert a['in_level']==b['out_level']and a['out_level']==b['in_level']
   assert abs(a['in_level']-a['out_level'])==1
   lam=max(hSE,hNW)
   pair=sorted([a['in_level'],a['out_level']])
   assert pair==([lam-1,lam]if hSE==hNW else[lam-2,lam-1])
   if n==4:assert events[3]['in_level']==events[3]['out_level']
  rows.append(dict(headings=hs,turns=''.join(turns),h_SE=hSE,h_NW=hNW,h_NE_L=hNE,h_SW_L=hSW,events=events))
p=Path(__file__).with_suffix('.json')
p.write_text(json.dumps(dict(scope='30 complete white cap-four local histories in one checker phase. Rotations give the other phase. Exact local sheet exchange only.',count=len(rows),rows=rows),indent=2)+'\n')
print('PASS',len(rows),'local histories,',sum(len(r['events'])>=3 for r in rows),'two-R adjacent exchanges')
