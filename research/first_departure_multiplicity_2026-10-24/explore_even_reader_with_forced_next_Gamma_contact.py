"""Complete the forced post-XY Gamma V contact and its next RIGHT before
promoting the 14-cell even reader controls. Finite count-forced corner
closure, not a radius/period/front scan. OPEN still not a physical factor.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,ast,time
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
plainprop,check,dom,V=[L[k]for k in ['propagate','check','dom','V']]
raw=(base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0].split(' d={a:0 for a in ns}')[0]+" return'open'\n";Q={};exec(raw,Q);rankcheck=Q['check']
part=Counter()
def prop(ds):
 z=plainprop(ds)
 if z is None:return None
 a=rankcheck({p:v[0]for p,v in z.items()if len(v)==1})
 if a!='open':part[a]+=1;return None
 return z
j=json.loads((base/'check_LL_cyclic_supplier_reactivation_modes.json').read_text());a=next(a for r in j['roots']if r['root']=='EWWE'for a in r['cyclic_necessary_profiles']if a['kind']=='P');fixed0={ast.literal_eval(p):h for p,h in a['histories'].items()}|{(1,-1):'SNNS',(2,-1):'WEEW',(0,-1):'EEWW'};rows=[];tm=time.time()
for mode,F,G,H in [('expanding','NNSS','NNSS','WEEW'),('merge','SSNN','SNNS','WEEW'),('corner_swap','NNSS','SNNS','EWWE')]:
 fixed=fixed0|{(2,-2):F,(3,-1):G,(3,-2):H};pts=set(fixed)
 while True:
  can={(p[0]+v[0],p[1]+v[1])for p in pts for v in V.values()}-pts
  add={q for q in can if sum((q[0]+v[0],q[1]+v[1])in pts for v in V.values())>=2}
  if not add:break
  pts|=add
 ds=prop({p:([fixed[p]]if p in fixed else ['SSNN','SNNS','SNS']if p==(0,-2)else dom(p))for p in sorted(pts)});ct=Counter();opens=[]
 def rec(ds):
  if all(len(v)==1 for v in ds.values()):
   hs={p:v[0]for p,v in ds.items()};a=check(hs);ct[a]+=1
   if a=='open':opens.append({str(p):h for p,h in sorted(hs.items())})
   return
  p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
  for h in ds[p]:
   z=prop(ds|{p:[h]})
   if z is not None:rec(z)
 if ds is not None:rec(ds)
 rows.append(dict(mode=mode,closure_cells=sorted(pts),counts=dict(ct),open=opens));print(mode,'cells',len(pts),dict(ct),'partial',dict(part),'elapsed',time.time()-tm,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,partial_rejections=dict(part),rows=rows,warning='Only three specified source/reader modes tested; no all-even mode exhaustion. OPEN does not fill farther Gamma or physical exterior.'),indent=2)+'\n')
