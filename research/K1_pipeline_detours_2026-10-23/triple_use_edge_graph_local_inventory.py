"""Exact physical edge-three incidence at all30 white cap-four local histories.
Incoming axis E/W; rotations cover the other axis. No front or period scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
H='NESW'
rows=[]
for n in range(1,5):
 for hs in product('EW',repeat=n):
  h=''.join(hs);rE=sum(s=='E'for s in h[::2]);rW=sum(s=='W'for s in h[::2]);lE=sum(s=='E'for s in h[1::2]);lW=sum(s=='W'for s in h[1::2]);a=-max(rE,rW)
  C=dict(NE=rW+a,SW=rE+a);L=dict(NW=a-lE,SE=a-lW)
  flows=dict(W=h.count('E'),E=h.count('W'),N=rW+lE,S=rE+lW)
  sectors=dict(W=('SW','NW'),E=('NE','SE'),N=('NE','NW'),S=('SW','SE'))
  ports=[p for p,f in flows.items()if f==3]
  inc=sum(p in'WE'for p in ports);out=sum(p in'NS'for p in ports)
  assert all(C[sectors[p][0]]==0 and L[sectors[p][1]]==-3 for p in ports)
  if n==3 and h[0]==h[2]:
   assert len(ports)==1
   typ='sink'if h[0]==h[1]else'source'
   assert (inc,out)==((1,0)if typ=='sink'else(0,1))
  else:
   typ='internal'if ports else'absent'
   assert (n==4 and(inc,out)==(1,1))if ports else True
  if len(ports)==2:
   cs={sectors[p][0]for p in ports};ls={sectors[p][1]for p in ports}
   # If sectors differ, both are at the same level and meet at this corner.
   assert all(C[c]==0 for c in cs)and all(L[l]==-3 for l in ls)
  rows.append(dict(headings=h,length=n,C=C,L=L,port_flows=flows,triple_ports=ports,triple_indegree=inc,triple_outdegree=out,type=typ))
assert len(rows)==30
out=dict(scope=__doc__,count=len(rows),types=dict(Counter(r['type']for r in rows)),degree_histogram=dict(Counter(len(r['triple_ports'])for r in rows)),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2))
