"""Exact forced Gamma contact after genuine XY cap, with all complete
WHITE next helper/target histories. No assumed even continuation mode.
Finite typed-junction cover; no period, width or radius scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import ast,json,time
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
prop,check,dom=L['propagate'],L['check'],L['dom'];j=json.loads((base/'check_LL_cyclic_supplier_reactivation_modes.json').read_text());rows=[];tot=Counter();tm=time.time()
for rs in j['roots']:
 for a in rs['cyclic_necessary_profiles']:
  for c in ['WEE','WEEW']:
   fixed={ast.literal_eval(p):h for p,h in a['histories'].items()}|{(1,-1):'SNNS',(2,-1):c,(0,-1):'EEWW'}
   pts=set(fixed)|{(0,-2),(1,-2),(2,-2)}
   ds=prop({p:([fixed[p]]if p in fixed else ['SSNN','SNNS','SNS']if p==(0,-2)else dom(p))for p in sorted(pts)});ct=Counter();op=[]
   def rec(ds):
    if all(len(z)==1 for z in ds.values()):
     hs={p:z[0]for p,z in ds.items()};v=check(hs);ct[v]+=1
     if v=='open':op.append({str(p):h for p,h in sorted(hs.items())})
     return
    p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
    for h in ds[p]:
     z=prop(ds|{p:[h]})
     if z is not None:rec(z)
   if ds is not None:rec(ds)
   rows.append(dict(root=rs['root'],reaction=a['kind'],C=c,counts=dict(ct),open=op));tot.update(ct);print(rs['root'],a['kind'],c,dict(ct),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(tot),rows=rows,warning='Depends on exact next Gamma RIGHT reduction; no force on still-unfilled later Gamma/exterior beyond that.'),indent=2)+'\n');print('TOTAL',dict(tot),time.time()-tm)
