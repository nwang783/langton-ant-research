from itertools import product
from collections import Counter,defaultdict
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];R=ROOT/'K1_pipeline_detours_2026-10-23'
# Four incident edges: south incoming N, north incoming S, east outgoing E, west outgoing W.
# Solve the four directed face differences from actual port multiplicities.
facepairs={('in',0):('SE','SW'),('in',2):('NW','NE'),('out',1):('SE','NE'),('out',3):('NW','SW')}
rows=[]
for n in range(1,5):
 for heads in product((0,2),repeat=n):
  turns=[1 if i%2==0 else -1 for i in range(n)];outs=[(h+t)%4 for h,t in zip(heads,turns)]
  flows={('in',h):heads.count(h)for h in (0,2)}|{('out',h):outs.count(h)for h in(1,3)}
  heights={'NW':0}
  while len(heights)<4:
   before=len(heights)
   for edge,(c,l)in facepairs.items():
    f=flows[edge]
    if c in heights:heights.setdefault(l,heights[c]-f)
    if l in heights:heights.setdefault(c,heights[l]+f)
   assert len(heights)>before
  assert all(heights[c]-heights[l]==flows[e]for e,(c,l)in facepairs.items())
  ordinals=Counter();incoming=[];outgoing=[]
  for h,o in zip(heads,outs):
   for typ,heading,dest in [('in',h,incoming),('out',o,outgoing)]:
    e=typ,heading;ordinals[e]+=1;dest.append(heights[facepairs[e][0]]-ordinals[e]+1)
  repaired=list(range(n))
  if n>=3:repaired[1],repaired[2]=2,1
  assert all(incoming[i]==outgoing[repaired[i]]for i in range(n))
  if n<3:assert incoming==outgoing
  else:
   assert incoming[0]==outgoing[0]
   assert incoming[1]==outgoing[2]and incoming[2]==outgoing[1]and abs(incoming[1]-outgoing[1])==1
   if n==4:assert incoming[3]==outgoing[3]
   high=max(heights['NW'],heights['SE']);want={high,high-1}if heights['NW']==heights['SE']else{high-1,high-2};assert {incoming[1],outgoing[1]}==want
  levels=defaultdict(list)
  for i,j in enumerate(repaired):
   turn=(outs[j]-heads[i])%4;assert turn in(1,3);levels[incoming[i]].append((heads[i],outs[j],turn))
  for lev,arcs in levels.items():
   assert len(arcs)<=2
   if len(arcs)==2:assert {a for a,b,t in arcs}=={0,2}and{b for a,b,t in arcs}=={1,3}and len({t for a,b,t in arcs})==1
   if lev==max(heights['NW'],heights['SE']):assert all(t==1 for a,b,t in arcs)
  rows.append({'headings':heads,'face_heights':heights,'incoming_levels':incoming,'outgoing_levels':outgoing,'repaired_successor_rank':repaired,'levels':dict(levels)})
assert len(rows)==30 and sum(len(x['headings'])>=3 for x in rows)==24
out={'status':'PASS independent face-equation/ordinal reconstruction of all30 local cap-four sheet exchanges and embedded corner pairings','rows':rows,'note_sha256':hashlib.sha256((R/'chronological_stream_sheet_exchange.md').read_bytes()).hexdigest(),'scope':'Local identity and smoothing controls. Connected global exchange graph, parity, clock and bridge conclusions are separately analytic; no actual cap-four front is generated.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
