"""Exact passive VV LL predecessor junction; all displayed readers retained.
This probes a typed junction, not a period/radius scan or attained factor.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,time
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
V,dom,plainprop,check=[L[k]for k in ['V','dom','propagate','check']]
raw=(base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0].split(' d={a:0 for a in ns}')[0]+" return'open'\n";Q={};exec(raw,Q);rankcheck=Q['check']
def prop(ds):
 z=plainprop(ds)
 return z if z is not None and rankcheck({p:a[0]for p,a in z.items()if len(a)==1})=='open'else None
fixed={(0,0):'NNSS',(0,1):'EEWW',(1,0):'EWWE',(1,1):'SNNS'};ct=Counter();rows=[];ds=prop({p:([fixed[p]]if p in fixed else dom(p))for p in product(range(3),repeat=2)})
def rec(ds):
 if all(len(a)==1 for a in ds.values()):
  hs={p:a[0]for p,a in ds.items()};a=check(hs);ct[a]+=1
  if a=='open':rows.append({str(p):h for p,h in sorted(hs.items())})
  return
 p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
 for h in ds[p]:
  z=prop(ds|{p:[h]})
  if z is not None:rec(z)
rec(ds)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,counts=dict(ct),open=rows),indent=2)+'\n')
print('COUNTS',dict(ct),'OPEN',len(rows))
for r in rows:print('C U T R D',*[r[str(p)]for p in[(0,2),(1,2),(2,2),(2,0),(2,1)]])
