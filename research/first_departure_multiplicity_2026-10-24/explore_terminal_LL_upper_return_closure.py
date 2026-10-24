"""Discovery: top-side closure only at the fixed terminal LL portal."""
from pathlib import Path
from itertools import product
from collections import Counter
import json,ast,time
b=Path(__file__).parent
Q={'__file__':str(b/'explore_two_flat_pair_reader_closure.py')};exec((b/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],Q)
V,dom,propagate,check=Q['V'],Q['dom'],Q['propagate'],Q['check']
core=json.loads((b/'check_terminal_LL_even_portal_suppliers.json').read_text())
TOP={rr:[(a,z) for a,z in product(dom((0,0)),dom((1,0))) if check({(0,-1):'WWEE',(1,-1):rr,(0,0):a,(1,0):z})=='open'] for rr in ['SNN','SNNS']}
ct=Counter();ans=[];prim=Counter();t=time.time()
for row in core['rows']:
 if row['result']!='open':continue
 hs0={ast.literal_eval(p):h for p,h in row['histories'].items()}
 for a,z in TOP[hs0[(2,2)]]:
  fixed=hs0|{(1,3):a,(2,3):z};prim['rows']+=1
  pts=set(fixed)|{(0,3),(-1,3)}
  ds=propagate({p:[fixed[p]] if p in fixed else dom(p) for p in pts})
  if ds is None:ct['empty_closure']+=1;continue
  def visit(ds):
   if all(len(h)==1 for h in ds.values()):
    hs={p:h[0] for p,h in ds.items()};r=check(hs);ct[r]+=1
    if r=='open':ans.append({str(p):h for p,h in sorted(hs.items())})
    return
   p=min((p for p,h in ds.items() if len(h)>1),key=lambda p:len(ds[p]))
   for h in ds[p]:
    nd=propagate(ds|{p:[h]})
    if nd is not None:visit(nd)
  visit(ds)
print(dict(prim),dict(ct),len(ans),time.time()-t)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,primary=dict(prim),counts=dict(ct),open=ans),indent=2)+'\n')
