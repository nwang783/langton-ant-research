"""Complete necessary closure at the activated left child R and Q2.
Assumes the zero-output all-four NSSS/EWEE late-outward mode.
No repeated late-route premise is imposed on the off-cycle descendant.
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
old=json.loads((root/'late_D4_outward_Q1_canonical_birth.json').read_text())['rows']
def find(h):return next(r for r in base if r['headings']==h)
F=find(dict(A='NNSN',Z='WWEW',Y='NSSS',B='EEWE'))
I=find(dict(A='NNSN',Z='WWWE',Y='NSNN',B='WEEE'))
even=[r for r in base if r['headings']['A']=='NNSN'and all(len(h)%2==0 for h in r['headings'].values())]
prior=[r for r in old if r['prior_P0']['Y']=='NSSS'and r['Q1_rotation']==3]
rows=[];candidates=0
for z in prior:
 packs=[(F,(0,0),0),(find(z['prior_J']),(-1,-1),1),(find(z['prior_P0']),(-2,0),0),(I,(-1,1),3),(find(z['prior_G']),(1,1),3),(find(z['Q1_profile']),(-3,1),3)]
 for r,q2,q in product(even,even,(0,2,3)):
  rh,rf,re,rb=pose(r,(-3,-1),1)
  if rh.get((-2,0))!='WWEW':continue
  if outs(rh[(-2,-1)]).count('E')!=z['headings']['(-1, -1)'].count('E') or rh[(-3,0)].count('S')!=1:continue
  qh,qf,qe,qb=pose(q2,(-4,0),q)
  if qh.get((-3,1))!='EEWE'or qh.get((-3,0))!=rh[(-3,0)]:continue
  candidates+=1
  c=check(packs+[(r,(-3,-1),1),(q2,(-4,0),q)])
  if c is not None:rows.append(dict(R_profile=r['headings'],Q2_profile=q2['headings'],Q2_rotation=q,**c))
profiles=collections.Counter((r['headings']['(-3, -1)'],r['headings']['(-3, 0)'],r['Q2_rotation'],tuple(r['Q2_profile'].items()))for r in rows)
out=dict(scope=__doc__,prior_count=len(prior),candidates=candidates,count=len(rows),profiles=[dict(s=k[0],m=k[1],Q2_rotation=k[2],Q2=dict(k[3]),count=v)for k,v in profiles.items()],rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2))
