"""All 21 cap-four first-R b-circle corner profiles, with first-track side labels.
Complete WHITE histories and constant selected C height; arbitrary cycle flow.
No period, drift, support or width scan.
"""
from pathlib import Path
from itertools import product
import json
H='NESW'
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
right=['E'+''.join(x)for n in range(1,5)for x in product('EW',repeat=n-1)]
left=['W'+''.join(x)for n in[3,4]for x in product('EW',repeat=n-1)if x[1]=='E']
assert len(right)==15 and len(left)==6
rows=[]
for turn,words in [('RIGHT',right),('LEFT',left)]:
 ci='E';co='S'if turn=='RIGHT'else'N';ex='LEFT'if turn=='RIGHT'else'RIGHT'
 for h in words:
  ins=[r for r,x in enumerate(h)if x==ci];outs=[r for r in range(len(h))if out(h,r)==co]
  itag={r:('RIGHT'if j==0 else'LEFT')for j,r in enumerate(ins)};otag={r:('RIGHT'if j==0 else'LEFT')for j,r in enumerate(outs)}
  events=[dict(rank=r,incoming=h[r],outgoing=out(h,r),input_side=itag.get(r,ex),output_side=otag.get(r,ex))for r in range(len(h))]
  crossings=[(e['rank'],e['input_side'],e['output_side'])for e in events if e['input_side']!=e['output_side']]
  expected=[(1,'RIGHT','LEFT'),(2,'LEFT','RIGHT')]if turn=='LEFT'and h in['WEE','WEEW','WEEE']else[]
  assert crossings==expected,(turn,h,crossings)
  if turn=='RIGHT':assert [e['input_side']for e in events]==[e['output_side']for e in events]==['RIGHT']+['LEFT']*(len(h)-1)
  if turn=='LEFT':assert len(ins)==len(outs)
  for q in range(4):
   rot=lambda z:''.join(H[(H.index(x)+q)%4]for x in z)
   hh=rot(h);cc=rot(ci);oo=rot(co)
   assert[i for i,x in enumerate(hh)if x==cc]==ins
   assert[i for i in range(len(hh))if out(hh,i)==oo]==outs
  rows.append(dict(turn=turn,history=h,cycle_incoming=ci,cycle_outgoing=co,incoming_cycle_ranks=ins,outgoing_cycle_ranks=outs,exterior_side=ex,physical_flows=[len(ins),len(outs)],actual_event_sides=events,crossings=crossings))
assert{r['history']:r['physical_flows'][0]for r in rows if r['turn']=='LEFT'}=={'WWE':1,'WEE':2,'WWEW':1,'WWEE':2,'WEEW':2,'WEEE':3}
obj=dict(scope=__doc__,profiles=rows,normal_profile_count=21,rotated_profile_count=84,conclusion='The only crossing contacts are LEFT WEE/WEEW/WEEE, all at L1 RIGHT-to-LEFT and R2 LEFT-to-RIGHT. Mixed flow2/3/4 RIGHT gates preserve first-track sides; optional L3 is retained with its actual side.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS all21 profiles/all84 rotations; exactly3 LEFT crossing types')
