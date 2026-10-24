#!/usr/bin/env python3
"""Freeze one geometric cone violation for every algebraic survivor."""
import json,math,collections,hashlib
from fractions import Fraction as Q
from pathlib import Path
root=Path(__file__).parent
domains=json.loads((root/'inventory.json').read_text())['domains']
source=json.loads((root/'cone_candidates.records.json').read_text())
D=((0,1),(1,0),(0,-1),(-1,0));digits=[]
for t in range(3000):
 ds=[0]*4;z=t
 for j in range(3,-1,-1):ds[j]=z%13;z//=13
 digits.append(ds)
out=[];hist=collections.Counter()
for r in source:
 images=[domains[d][r['indices'][d]]['word'] for d in range(4)]
 ex,ey=map(Q,r['ell']);den=math.lcm(ex.denominator,ey.denominator);ex=int(ex*den);ey=int(ey*den)
 x=y=0
 for t,ds in enumerate(digits):
  if ex*x+ey*y<2*den*max(abs(x),abs(y)):
   out.append(dict(indices=r['indices'],last_map=r['last_map'],ell=r['ell'],read=t,cell=[x,y]));hist[t]+=1;break
  d=0
  for j in ds:d=images[d][j]
  x+=D[d][0];y+=D[d][1]
 else:raise AssertionError(('unresolved cone',r))
raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode()+b'\n';(root/'cone_only.records.json').write_bytes(raw)
summary=dict(status='ALL ALGEBRAIC SURVIVORS HAVE A GEOMETRIC CONE VIOLATION',
 cases=len(out),latest=max(hist),histogram=dict(hist),
 records_sha256=hashlib.sha256(raw).hexdigest())
(root/'cone_only.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
