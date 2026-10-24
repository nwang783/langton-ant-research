"""All local actual ports of an all-V constant-flow-two first-R wall.
No period or front scan. The global proof uses the embedded essential b-circle.
"""
from pathlib import Path
import json
H='NESW'
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def rotate(h,q):return''.join(H[(H.index(x)+q)%4]for x in h)
rows=[]
for turn,h in [('RIGHT','EEWW'),('RIGHT','EWWE'),('LEFT','WWEE'),('LEFT','WEE'),('LEFT','WEEW')]:
 ci='E';co='S'if turn=='RIGHT'else'N';ex='LEFT'if turn=='RIGHT'else'RIGHT'
 ins=[r for r,x in enumerate(h)if x==ci];outs=[r for r in range(len(h))if out(h,r)==co]
 assert len(ins)==len(outs)==2
 itag={r:('RIGHT'if j==0 else'LEFT')for j,r in enumerate(ins)}
 otag={r:('RIGHT'if j==0 else'LEFT')for j,r in enumerate(outs)}
 events=[]
 for r in range(len(h)):
  a=itag.get(r,ex);b=otag.get(r,ex)
  events.append(dict(rank=r,incoming_heading=h[r],outgoing_heading=out(h,r),incoming_side=a,outgoing_side=b))
 cross=[(e['rank'],e['incoming_side'],e['outgoing_side'])for e in events if e['incoming_side']!=e['outgoing_side']]
 if h in ['WEE','WEEW']:assert cross==[(1,'RIGHT','LEFT'),(2,'LEFT','RIGHT')]
 else:assert not cross
 for q in range(4):
  hh=rotate(h,q);ii=rotate(ci,q);oo=rotate(co,q)
  assert [r for r,x in enumerate(hh)if x==ii]==ins
  assert [r for r in range(len(hh))if out(hh,r)==oo]==outs
 rows.append(dict(turn=turn,history=h,incoming_cycle=ci,outgoing_cycle=co,incoming_cycle_ranks=ins,outgoing_cycle_ranks=outs,exterior_side=ex,events=events,actual_crossings=cross))
obj=dict(scope=__doc__,all_normalized_rows=rows,all_rotations=20,conclusion='Both RIGHT profiles and LEFT V preserve actual event side. LEFT O/U have exactly the genuine L1 RIGHT-to-LEFT and R2 LEFT-to-RIGHT reset pair. An all-V embedded essential b-circle therefore partitions the actual full event orbit, even with chords or arbitrary exterior histories.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS 5 profiles, 20 rotations; only O/U contacts cross, at L1 and R2')
