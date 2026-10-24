"""Complete phase check for ONE-literal-turn orthogonal104 corner.
This is a fixed tiny interface architecture, not a longer connector search.
Incoming two mature periods suffice for every retained literal obstruction.
Every outgoing canonical phase with the compatible incoming head is tested.
"""
from pathlib import Path
import json,hashlib
from certify_highway_wake_reflector import trace
from probe_perpendicular_highway_wake import H
P=Path(__file__).resolve().parent
phases,_,_=trace(H,(0,0),2)
records=[];survivors=[]
for a,(_,ha,_)in enumerate(phases):
 incoming=H[a:]+H[:a]
 pre,p,h=trace(incoming*3,(0,0),ha)
 last={}
 for t,(q,hh,c)in enumerate(pre):
  assert q not in last or last[q][1]!=c
  last[q]=(t,c)
 for turn in 'RL':
  cap,p1,h1=trace(turn,p,h)
  # Both perpendicular highway directions, with all compatible phase heads.
  for target_head in(1,3):
   outphases,_,_=trace(H,(0,0),target_head)
   for b,(_,hb,_)in enumerate(outphases):
    if hb!=h1:continue
    outword=H[b:]+H[:b]
    rr,_,_=trace(turn+outword*10,p,h);seen=dict(last);failure=None
    for t,(q,hh,c)in enumerate(rr):
     if q in seen and seen[q][1]==c:
      failure=dict(time_after_cap_start=t,point=q,earlier=seen[q][0],turn=c);break
     seen[q]=(312+t,c)
    case=dict(in_phase=a,cap=turn,out_rotation_head=target_head,out_phase=b)
    if failure:records.append(dict(**case,**failure))
    else:survivors.append(case)
res=dict(scope=__doc__,cases=len(records)+len(survivors),conflicts=len(records),survivors=survivors,latest_conflict=max(x['time_after_cap_start']for x in records),records=records,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'single_turn_highway_corner.json').write_text(json.dumps(res,indent=2)+'\n');print({k:v for k,v in res.items()if k!='records'})
