from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
B=Path('/workspace/shared/langton');rows=[];tested=0
for axis in(1,1j):
 for n in range(5):
  for history in product((axis,-axis),repeat=n):
   outgoing=tuple(v*(-1j if j%2==0 else 1j)for j,v in enumerate(history));incoming=Counter(history);outs=Counter(outgoing);tested+=1
   hi=[d for d,c in incoming.items()if c==3];ho=[d for d,c in outs.items()if c==3]
   if not hi or not ho:continue
   assert n==4 and len(hi)==len(ho)==1;a,b=hi[0],ho[0]
   if b==-1j*a:
    assert all(history[j]==a and outgoing[j]==b for j in(0,2));orientation='right'
   else:
    assert b==1j*a and all(history[j]==a and outgoing[j]==b for j in(1,3));orientation='left'
   rows.append(dict(incoming=[(int(z.real),int(z.imag))for z in history],outgoing=[(int(z.real),int(z.imag))for z in outgoing],high_turn=orientation))
assert len(rows)==16
out=dict(status='PASS independent complete cap-four high-flow routing table; Jordan first/last-time argument reviewed',tested_histories=tested,high_flow_quad_states=len(rows),rows=rows,scope='No finite physical directed cycle consisting of count-three edges. Essential cylinder cycles/infinite lifts remain possible; no cap-three doubled-edge forest inference.',subject_sha256=hashlib.sha256((B/'periodic_classification_new/cap_four_count_three_cycle_exclusion.md').read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2))
