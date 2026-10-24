"""Canonical first-branch leaves in all three early RIGHT-ancestor modes.
Only complete110 profiles and previously signed ancestor rows.
"""
from pathlib import Path
from collections import Counter
import ast,json
root=Path(__file__).parent
H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0));cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1));op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
t=ast.parse((root/'canonical_three_child_square_closure.py').read_text());exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))
base=json.loads((root/'canonical_max_face_child_ports.json').read_text())['rows']
prior=json.loads((root/'bit11_surviving_cleanup_Q1_parent_ports.json').read_text())['rows']
R=[r for r in prior if r['headings']['j']=='EEWE'];types={}
for r in R:
 hs=r['headings']; typ='R3' if hs['x']=='EWW' else 'R4a'if hs['r']=='WEW'else'R4b'
 physical={(-1,-1):hs['r'],(0,-1):hs['q'],(-1,0):hs['e'],(0,0):hs['Z']}
 types.setdefault(typ,[]).append(physical)
assert set(types)=={'R3','R4a','R4b'}
profiles=[]
for typ,ps in types.items():
 assert all(p==ps[0]for p in ps)
 found=[]
 for row in base:
  for q in range(4):
   hh,fs,en,bd=pose(row,(-1,-1),q)
   if hh!=ps[0]:continue
   assert en==(0,0) and row['potential_children']==[]
   found.append(dict(type=typ,source_rows=len(ps),physical={str(p):h for p,h in hh.items()},entry=list(en),rotation=q,canonical_profile=row['headings'],potential_children=row['potential_children']))
 assert len(found)==1;profiles+=found
out=dict(scope=__doc__,R_rows=len(R),first_branch_leaf_profiles=profiles,capacity='Nodd >= n_Sanc + 3*n_R3 + 4*n_R4a + 2*n_R4b')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
