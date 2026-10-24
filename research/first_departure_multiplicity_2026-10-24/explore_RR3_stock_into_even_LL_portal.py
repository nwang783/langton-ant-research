"""Exact immediate RR1/3/1 stock gate feeding the fixed even LL portal.
All three signed entry profiles, complete two-neighbor corner closure.
"""
from pathlib import Path
from collections import Counter
import json
b=Path(__file__).parent;L={'__file__':str(b/'explore_two_flat_pair_reader_closure.py')};exec((b/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
V,dom,propagate,check=L['V'],L['dom'],L['propagate'],L['check'];rows=[]
for Y,q,C,z in [('EWW','EEW','SSN','NNS'),('EWW','EEWE','SSNS','NNSN'),('EWWE','EEW','SSNN','NNS')]:
 fixed={(1,1):'SN',(0,1):Y,(0,0):'NNSS',(1,0):'EE',(1,2):q,(0,2):C,(2,2):'SSNS',(2,3):'EWWW',(1,3):z};pts=set(fixed)
 while True:
  cand={(p[0]+v[0],p[1]+v[1])for p in pts for v in V.values()}-pts
  add={r for r in cand if sum((r[0]+v[0],r[1]+v[1])in pts for v in V.values())>=2}
  if not add:break
  pts|=add
 ds=propagate({p:[fixed[p]]if p in fixed else dom(p)for p in sorted(pts)});ct=Counter();op=[]
 if ds is None:ct['primary_PORT']+=1
 else:
  print('domains',Y,q,{p:a for p,a in ds.items()if len(a)>1},flush=True)
  def rec(ds):
   if all(len(v)==1 for v in ds.values()):
    hs={p:v[0]for p,v in ds.items()};a=check(hs);ct[a]+=1
    if a=='open':op.append({str(p):h for p,h in hs.items()})
    return
   p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
   for h in ds[p]:
    nd=propagate(ds|{p:[h]})
    if nd is not None:rec(nd)
  rec(ds)
 print(Y,q,len(pts),ct,'open',len(op),flush=True);rows.append(dict(Y=Y,q=q,C=C,z=z,cells=sorted(pts),counts=dict(ct),open=op))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,rows=rows),indent=2)+'\n')
