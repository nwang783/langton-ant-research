"""Exact early-parent LEFT-L3 cleanup and actual next-gate deadline.
No exterior translator or paid fuel is asserted.
"""
from pathlib import Path
import json
s=Path(__file__).with_name('bit11_early_parent_left_square_ports.py').read_text()
exec(s[:s.index('rows=[];candidates=0')])
ss=ss.replace("('g','E','u','E')]", "('g','E','u','E'),('t','W','f','W'),('f','S','g','S')]")
ss=ss.replace('d={x:0 for x in ns}', "es.append((('B',3),('D',1),1))\n d={x:0 for x in ns}")
exec(ss)
SCOPE='Exact early-parent LEFT-L3 cleanup and actual next-gate deadline; necessary local histories only.'
rows=[];candidates=0
source=json.loads(Path(__file__).with_name('bit11_early_parent_left_square_ports.json').read_text())
for prior in source['rows']:
 if prior['headings']['g']!='SSNS':continue
 for fh in ['EWE','EWEE','EEEW']:
  hs=dict(prior['headings'],f=fh);candidates+=1
  t=feasible(hs,prior['kind'],'u','g')
  if t is not None:rows.append(dict(kind=prior['kind'],headings=hs,minimum_clocks=t))
r=dict(scope=SCOPE,candidates=candidates,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(dict(scope=r['scope'],candidates=candidates,count=len(rows),profiles=sorted(set((x['kind'],x['headings']['v'],x['headings'].get('w',''),x['headings']['D'],x['headings']['a'],x['headings']['f'])for x in rows))),indent=2))
