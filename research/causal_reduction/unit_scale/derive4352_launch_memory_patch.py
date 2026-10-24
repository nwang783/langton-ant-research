"""Unique launch-only memory patch for the prescribed15324 return word.
Stop at its FIRST mismatch outside the original6812 launch READ support.
There is no chosen cap radius, repair count, or word-search horizon.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib
from probe4352_return_end_limit import build,trace,A,L,V
import inverse4352_tail_completion as T
P=Path(__file__).resolve().parent
b=build();p=(117,111);h=0;seen=set();corrections=[];hist=defaultdict(list)
for i,q,hh,c in list(trace(L['forward_prelude_word'],tuple(L['forward_entry_pose'][0]),L['forward_entry_pose'][1]))[:-1]:hist[q].append((i,hh,c))
i=0
while True:
 c=A['word'][i%len(A['word'])]
 if b.color(p)!=(c=='L'):
  assert p not in seen
  row={'offset':i,'cell':p,'heading':h,'required':c,'actual':'L'if b.color(p)else'R','future4352_read':T.future_read(p),'launch_history':hist.get(p)}
  if p not in hist:boundary=row;break
  assert not T.future_read(p)
  corrections.append(row);b.toggle(p)
 seen.add(p);b.toggle(p);h=(h+(1 if c=='R'else-1))%4;p=p[0]+V[h][0],p[1]+V[h][1];i+=1
out={'scope':__doc__,'corrections':corrections,'patch':sorted(x['cell']for x in corrections),'first_nonlaunch_mismatch':boundary,'prescribed_legal_prefix_length':i,'all_patch_cells_future4352_unread':True,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared4352_launch_memory_patch.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
