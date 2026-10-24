"""Necessary canonical Q1 closure in the outward-M late D4 route.
Rebuilds complete local canonical profiles and all shared ordinal ports.
No new off-Gamma K1 ordering or exterior realization is assumed.
"""
from pathlib import Path
from itertools import product
import ast,json,collections
root=Path(__file__).parent
base=json.loads((root/'canonical_max_face_child_ports.json').read_text())['rows']
old=json.loads((root/'canonical_duplicator_local_parent_return.json').read_text())['rows']
H='NESW'; V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0))
cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1));op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
tree=ast.parse((root/'canonical_three_child_square_closure.py').read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'closure_helpers','exec'))
def find(h):
 return next(r for r in base if r['headings']==h)
F=find(dict(A='NNSN',Z='WWEW',Y='NSSS',B='EEWE'))
I=find(dict(A='NNSN',Z='WWWE',Y='NSNN',B='WEEE'))
rows=[]; attempts=0
outward=[r for r in old if r['heights'].get('(-3, 1)')==0]
for prior in outward:
 packages=[(F,(0,0),0),(find(prior['J']),(-1,-1),1),(find(prior['P0']),(-2,0),0),(I,(-1,1),3),(find(prior['G']),(1,1),3)]
 for q,r in product((2,3),base):
  hh,fs,entry,bd=pose(r,(-3,1),q)
  if hh.get((-2,1))!=prior['headings']['(-2, 1)'] or hh.get((-2,2))!=prior['f']:continue
  attempts+=1
  z=check(packages+[(r,(-3,1),q)])
  if z is not None:
   rows.append(dict(prior_J=prior['J'],prior_P0=prior['P0'],prior_G=prior['G'],f=prior['f'],Q1_rotation=q,Q1_profile=r['headings'],Q1_other=r['other'],Q1_potential_children=r['potential_children'],**z))
profiles=collections.Counter((r['prior_P0']['Z'],r['prior_P0']['Y'],r['f'],r['Q1_rotation'],tuple(r['Q1_profile'].items()))for r in rows)
out=dict(scope=__doc__,outward_prior_rows=len(outward),attempts=attempts,count=len(rows),profiles=[dict(x=k[0],g=k[1],f=k[2],rotation=k[3],Q1=dict(k[4]),count=v)for k,v in profiles.items()],rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2))
