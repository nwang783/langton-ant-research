"""Discovery exact LRRL one-use ending into the fixed even-root portal."""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b=Path(__file__).parent;Q={'__file__':str(b/'explore_two_flat_pair_reader_closure.py')};exec((b/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],Q)
ct=Counter();ans=[]
for tail in ['EEW','EEWE']:
 fixed={(0,1):'WE',(0,2):'SNNS',(-1,2):'EEWW',(-1,1):'SS',(1,1):'SSN',(1,2):'WWEE',(1,0):'W',(2,0):'S',(2,1):tail}
 pts=set(fixed)
 while True:
  cand={(p[0]+v[0],p[1]+v[1]) for p in pts for v in Q['V'].values()}-pts;add={p for p in cand if sum((p[0]+v[0],p[1]+v[1]) in pts for v in Q['V'].values())>=2}
  if not add:break
  pts|=add
 ds=Q['propagate']({p:[fixed[p]] if p in fixed else Q['dom'](p) for p in pts})
 if ds is None:ct['empty']+=1;continue
 def visit(ds):
  if all(len(h)==1 for h in ds.values()):
   hs={p:h[0] for p,h in ds.items()};r=Q['check'](hs);ct[r]+=1
   if r=='open':ans.append({str(p):h for p,h in sorted(hs.items())})
   return
  p=min((p for p,h in ds.items() if len(h)>1),key=lambda p:len(ds[p]))
  for h in ds[p]:
   nd=Q['propagate'](ds|{p:[h]})
   if nd is not None:visit(nd)
 visit(ds)
print(dict(ct),len(ans));print(ans)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,counts=dict(ct),open=ans),indent=2)+'\n')
