"""Smaller complete certificate for the transport composition obstruction.
This author checker shares the no-import palette/trace implementation in
transport_composition_closure.py. An independent audit must not count this
shared code as a second implementation.
"""
import json,pathlib,hashlib
from transport_composition_closure import palette,trace
p=palette();phases=[(a,b) for a in p['R'] for b in p['L'] if (a,b)!=('R','L')]
records=[]
for i,(a,b) in enumerate(phases):
 for c in 'RL':
  for j,w in enumerate(p[c][1:]):
   out=''.join(a if x=='R' else b for x in w);result=trace(out)
   assert 'conflict' in result,(a,b,w,result)
   records.append(dict(outer=[a,b],inner_root=c,inner_word=w,expanded_length=len(out),**result))
raw=json.dumps(records,sort_keys=True,separators=(',',':')).encode()+b'\n'
base=pathlib.Path(__file__);base.with_suffix('.records.json').write_bytes(raw)
answer=dict(status='COMPLETE',outer_maps=len(phases),inner_words=12,cases=len(records),latest_conflict=max(r['conflict'] for r in records),max_expanded_length=max(r['expanded_length'] for r in records),records_sha256=hashlib.sha256(raw).hexdigest())
base.with_suffix('.json').write_text(json.dumps(answer,indent=2)+'\n');print(json.dumps(answer))
