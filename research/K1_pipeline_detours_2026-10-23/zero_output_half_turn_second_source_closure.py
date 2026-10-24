"""Necessary all-even closure of the half-turned supplier's parent.
Retains actual canonical child identities; does not assume a repeated route.
"""
from pathlib import Path
from itertools import product
import ast,json,collections
root=Path(__file__).parent
H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0))
cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1));op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
t=ast.parse((root/'canonical_three_child_square_closure.py').read_text())
exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))
base=json.loads((root/'canonical_max_face_child_ports.json').read_text())['rows']
def find(h):return next(r for r in base if r['headings']==h)
F=find(dict(A='NNSN',Z='WWEW',Y='NSSS',B='EEWE'))
I=find(dict(A='NNSN',Z='WWWE',Y='NSNN',B='WEEE'))
R=find(dict(A='NNSN',Z='WWWE',Y='NSNN',B='WEEE')) # overwritten by physical matching below.
U=find(dict(A='NNSN',Z='WWWE',Y='NNNS',B='EEWE'))
even=[r for r in base if r['headings']['A']=='NNSN'and all(len(h)%2==0 for h in r['headings'].values())]
prior=json.loads((root/'late_D4_outward_Q1_canonical_birth.json').read_text())['rows']
prior=[z for z in prior if z['prior_P0']['Y']=='NSSS'and z['Q1_rotation']==3]
rr=[r for r in even if pose(r,(-3,-1),1)[0].get((-3,-1))=='WEWW'and pose(r,(-3,-1),1)[0].get((-3,0))=='SNNN']
assert len(rr)==1
rows=[];candidates=0
for z in prior:
 packs=[(F,(0,0),0),(find(z['prior_J']),(-1,-1),1),(find(z['prior_P0']),(-2,0),0),(I,(-1,1),3),(find(z['prior_G']),(1,1),3),(find(z['Q1_profile']),(-3,1),3),(rr[0],(-3,-1),1),(F,(-4,0),2),(U,(-5,1),3)]
 for r2,d3,q in product(even,even,(0,2,3)):
  rh,rf,re,rb=pose(r2,(-5,-1),1)
  if rh.get((-4,0))!='WWEW':continue
  if outs(rh[(-4,-1)]).count('E')!=1 or rh[(-5,0)].count('S')!=1:continue
  dh,df,de,db=pose(d3,(-6,0),q)
  if dh.get((-5,1))!='EEWE'or dh.get((-5,0))!=rh[(-5,0)]:continue
  candidates+=1
  c=check(packs+[(r2,(-5,-1),1),(d3,(-6,0),q)])
  if c is not None:rows.append(dict(Rprime_profile=r2['headings'],D3_profile=d3['headings'],D3_rotation=q,**c))
profiles=collections.Counter((r['headings']['(-5, -1)'],r['headings']['(-5, 0)'],r['D3_rotation'],tuple(r['D3_profile'].items()))for r in rows)
out=dict(scope=__doc__,prior_count=len(prior),candidates=candidates,count=len(rows),profiles=[dict(s=k[0],m=k[1],D3_rotation=k[2],D3=dict(k[3]),count=v)for k,v in profiles.items()],rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2))
