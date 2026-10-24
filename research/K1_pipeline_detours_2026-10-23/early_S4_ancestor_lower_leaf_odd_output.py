"""Lower flag-zero leaf forced by S-ancestor interface4.
Saved complete canonical110 inventory and exact physical port counts.
"""
from pathlib import Path
import ast,json
root=Path(__file__).parent
H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0));cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1));op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
t=ast.parse((root/'canonical_three_child_square_closure.py').read_text());exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))
base=json.loads((root/'canonical_max_face_child_ports.json').read_text())['rows'];rows=[]
for row in base:
 for q in range(4):
  hh,fs,en,bd=pose(row,(-3,-1),q)
  if hh.get((-2,0))!='EWWW' or fs.get((-4,0))!=-1:continue
  d=hh[(-3,0)];tt=hh[(-2,-1)]
  if d.count('S') or outs(d).count('E')!=1 or outs(tt).count('E')!=1:continue
  flag=int(row['headings']['A']=='NNSN')
  assert not flag and not row['potential_children']
  rows.append(dict(physical={str(p):h for p,h in hh.items()},entry=list(en),rotation=q,canonical_profile=row['headings'],incoming_flag=flag,potential_children=row['potential_children']))
assert len(rows)==1
assert rows[0]['physical']=={'(-3, -1)':'EEWW','(-3, 0)':'NN','(-2, 0)':'EWWW','(-2, -1)':'SSS'}
out=dict(scope=__doc__,count=len(rows),rows=rows,capacity='Nodd >= 4*nS3 + 4*nS4a + 2*nS4b + 3*nR3 + 4*nR4a + 2*nR4b >= 2*n_A')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
