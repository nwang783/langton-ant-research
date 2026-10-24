"""Exact all-even passive source advanced to another YY cap then singletonV
and nextRIGHT. Tests a specified possible role reset, not a global scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
prop,check,dom=L['propagate'],L['check'],L['dom'];basefixed={(0,0):'NNSS',(0,1):'EEWW',(0,2):'NNSS',(1,0):'EWWE',(1,1):'SNNS',(1,2):'EWWE',(2,0):'NNSS',(2,1):'WWEE',(2,2):'NSSN',(1,-1):'SNNS',(0,-1):'EEWW'};rows=[]
for c in ['WEE','WEEW']:
 fixed=basefixed|{(2,-1):c};pts=set(fixed)|{(0,-2),(1,-2),(2,-2)};ds=prop({p:([fixed[p]]if p in fixed else ['SS','SSN','SSNN','SNNS','SNS','SNSN']if p==(0,-2)else dom(p))for p in sorted(pts)});ct=Counter();op=[]
 def rec(ds):
  if all(len(z)==1 for z in ds.values()):
   hs={p:z[0]for p,z in ds.items()};v=check(hs);ct[v]+=1
   if v=='open':op.append({str(p):h for p,h in sorted(hs.items())})
   return
  p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
  for h in ds[p]:
   z=prop(ds|{p:[h]})
   if z is not None:rec(z)
 rec(ds);rows.append(dict(C=c,counts=dict(ct),open=op));print(c,dict(ct),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,rows=rows),indent=2)+'\n')
