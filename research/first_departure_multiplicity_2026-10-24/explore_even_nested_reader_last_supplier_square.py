"""Exact downstream 2x2 supplier/target square at the EVEN nested reader.
Retains full C.R0/L1/R2/L3 and ALL complete0..4 WHITE histories of its
L3 source, two-S output recipient, and closing corner. Not a radius,
period, drift or strip-length search. OPEN is necessary only.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import ast,json,time
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
prop,check,dom,out,V=[L[k]for k in ['propagate','check','dom','out','V']]
j=json.loads((base/'check_LL_cyclic_supplier_reactivation_modes.json').read_text());rows=[];total=Counter();tm=time.time()
for rr in j['roots']:
 for a in rr['cyclic_necessary_profiles']:
  fixed={ast.literal_eval(p):h for p,h in a['histories'].items()}|{(1,-1):'SNNS',(2,-1):'WEEW'}
  pts=set(fixed)|{(2,-2),(3,-1),(3,-2)}
  ds=prop({p:([fixed[p]]if p in fixed else dom(p))for p in sorted(pts)});ct=Counter();opens=[]
  def rec(ds):
   if all(len(v)==1 for v in ds.values()):
    hs={p:v[0]for p,v in ds.items()};z=check(hs);ct[z]+=1
    if z=='open':opens.append(dict(F=hs[(2,-2)],G=hs[(3,-1)],H=hs[(3,-2)]))
    return
   p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
   for h in ds[p]:
    nd=prop(ds|{p:[h]})
    if nd is not None:rec(nd)
  if ds is not None:rec(ds)
  total.update(ct);rows.append(dict(root=rr['root'],reaction=a['kind'],R=fixed[(2,0)],counts=dict(ct),open=opens))
  print(rr['root'],a['kind'],fixed[(2,0)],dict(ct),'rows',len(opens),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(total),rows=rows,warning='Finite literal supplier-square interface only. No cycle role assigned to G/F/H, no actual phase-distinct calendar/exterior factor or front supplied.'),indent=2)+'\n');print('DONE',dict(total),time.time()-tm,flush=True)
