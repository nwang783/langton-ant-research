#!/usr/bin/env python3
"""Only the critical k15 images escaping the vertex-only overlap theorem."""
from pathlib import Path
import hashlib,json,sys,time
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE.parent))
from search_axis_swapping_halfturn import replay
j=json.loads((HERE/'inventory.json').read_text());E=j['E'];N=j['N'];indices=j['north_original_indices'];records=[];survivors=[];latest=None;start=time.monotonic()
for ie,u in enumerate(E):
 for jn in indices:
  v=N[jn];im={1:u,0:v,3:[(d+2)%4 for d in u],2:[(d+2)%4 for d in v]}
  def letters(d,depth):
   if not depth:yield d
   else:
    for z in im[d]:yield from letters(z,depth-1)
  for root in [1,0]:
   for h in [(root+3)%4,(root+1)%4]:
    r=replay(letters(root,4),h,10000);record=dict(east=ie,north=jn,root=root,heading=h,**r);records.append(record)
    if r['status']=='UNKNOWN':survivors.append(record)
    elif latest is None or r['time']>latest['time']:latest=record
blob=json.dumps(records,separators=(',',':'));(HERE/'records.json').write_text(blob+'\n')
out=dict(status='COMPLETE RESIDUAL PREFIX TEST',pairs=len(E)*len(indices),cases=len(records),cap=10000,survivors=survivors,latest_conflict=latest,records_sha256=hashlib.sha256(blob.encode()).hexdigest(),seconds=time.monotonic()-start)
(HERE/'result.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='survivors'}));print('survivors',len(survivors))
