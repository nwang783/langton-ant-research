"""Canonical completion obstruction at the zero-output early R ancestor.
No front or period scan: only the complete110 canonical-face inventory.
"""
from pathlib import Path
import ast,json,collections
root=Path(__file__).parent
H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0))
cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1));op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
t=ast.parse((root/'canonical_three_child_square_closure.py').read_text())
exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))
base=json.loads((root/'canonical_max_face_child_ports.json').read_text())['rows']
even=[r for r in base if all(len(h)%2==0 for h in r['headings'].values())]
prior=json.loads((root/'bit11_surviving_cleanup_Q1_parent_ports.json').read_text())['rows']
source=[r for r in prior if all(len(h)%2==0 for h in r['headings'].values())]
assert all(r['headings']['x']=='EWWW'and r['headings']['r']=='WEWW'and r['headings']['j']=='EEWE'for r in source)
rows=[]
for nw in ('NNSN','SNNN'):
 for r in even:
  for q in range(4):
   hh,fs,e,bd=pose(r,(-3,-1),q)
   if hh.get((-3,0))!=nw or hh.get((-2,0))!='EWWW':continue
   rows.append(dict(NW=nw,rotation=q,profile=r['headings'],physical={str(p):h for p,h in hh.items()},SE_E_departures=outs(hh[(-2,-1)]).count('E')))
out=dict(scope=__doc__,even_canonical_profiles=len(even),signed_ancestor_rows=len(prior),all_even_ancestor_rows=len(source),source_pairs=sorted(set((r['headings']['x'],r['headings']['r'],r['headings']['j'])for r in source)),canonical_completions=rows,completions_by_NW={h:sum(r['NW']==h for r in rows)for h in ('NNSN','SNNN')},physical_port_survivors=sum(r['SE_E_departures']==1 for r in rows))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
