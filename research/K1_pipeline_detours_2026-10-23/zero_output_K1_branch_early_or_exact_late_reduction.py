"""Zero-output physical branch reduction; existing complete local inventories only.
No front, period, drift, radius or multiplicity scan.
"""
from pathlib import Path
import ast, json
root=Path(__file__).parent
H='NESW'; V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0))
cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1)); op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
t=ast.parse((root/'canonical_three_child_square_closure.py').read_text())
exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))
prior=json.loads((root/'bit11_new_first_branch_full_ports.json').read_text())['rows']
even=[r for r in prior if all(len(h)%2==0 for h in r['headings'].values())]
assert len(even)==6
modes=sorted(set(tuple(r['headings'][k]for k in('e','r','q','u','t','a'))for r in even))
assert modes==[('NNSN','WWWE','SSSN','EEWE','NNNS','EWEE'),('SNNN','WEWW','SSSN','EEWE','NNNS','EWEE')]
base=json.loads((root/'canonical_max_face_child_ports.json').read_text())['rows']
ce=[r for r in base if all(len(h)%2==0 for h in r['headings'].values())]
late=[]
for row in ce:
 for q in range(4):
  hh,fs,en,bd=pose(row,(-2,0),q)
  if hh.get((-1,0))!='NNSN' or hh.get((-1,1))!='EEWE':continue
  assert en==(-1,0)
  late.append(dict(x=hh[(-2,0)],g=hh[(-2,1)],Q1=fs[(-3,1)],entry=list(en),rotation=q,profile=row['headings']))
assert len(late)==4
out=dict(scope=__doc__,prior_rows=len(prior),even_rows=len(even),modes=[dict(zip(('e','r','q','u','t','a'),x))for x in modes],even_canonical_profiles=len(ce),late_completion_count=len(late),late_completions=late)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
