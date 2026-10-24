"""Necessary right-turn local patterns including equal-M LEFT branches.
No exterior connector, period or front sufficiency.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,contextlib,io
with contextlib.redirect_stdout(io.StringIO()):
 from right_turn_local_ports import sel,helper,feasible

def flat(h):
 for first in(h,(h+2)%4):
  for length in(3,4):
   for ls in product((h,(h+2)%4),repeat=length//2):yield[first,ls[0],(first+2)%4]+([]if length==3 else[ls[1]])
reports=[]
for gz,gy in product(('strict','equal'),repeat=2):
 rows=[]
 for a,z,y,b in product(sel(0),helper(3)if gz=='strict'else flat(3),helper(0)if gy=='strict'else flat(0),sel(1)):
  hs=dict(A=a,Z=z,Y=y,B=b);t=feasible(hs)
  if t is not None:rows.append(dict(headings=hs,minimal_clock=t))
 summary=Counter((tuple(x['headings']['Z']),tuple(x['headings']['Y']))for x in rows)
 reports.append(dict(Z_other=gz,Y_other=gy,count=len(rows),helper_pairs=[dict(Z=k[0],Y=k[1],rows=v)for k,v in sorted(summary.items())],rows=rows))
r=dict(scope=__doc__,heading_key=['N','E','S','W'],reports=reports)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({**r,'reports':[{k:v for k,v in x.items()if k!='rows'}for x in reports]},indent=2))
