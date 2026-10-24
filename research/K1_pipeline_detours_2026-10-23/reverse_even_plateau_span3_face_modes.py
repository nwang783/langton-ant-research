from pathlib import Path
from collections import Counter
import json,ast
r=Path('/workspace/shared/langton/K1_pipeline_detours_2026-10-23');v=json.loads((r/'canonical_max_face_child_ports.json').read_text())['rows'];s=(r/'canonical_max_face_child_ports.py').read_text();tree=ast.parse(s);H='NESW'
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name=='out'],type_ignores=[]),'h','exec'))
f=next(x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name=='feasible');ss=ast.get_source_segment(s,f).replace('def feasible(h):','def feasible(h,exit):')
ss=ss.replace('d={x:0 for x in ns}',"es += [((('A',1)),(exit,0),1),((exit,0),('A',2),1),(('A',2),(exit,1),1)]\n d={x:0 for x in ns}")
exec(ss)
pos={'A':'S','Z':'W','Y':'N','B':'E'};rows=[]
for x in v:
 hs=x['headings']
 if any(len(h)%2 for h in hs.values()):continue
 mins={k:-h[::2].count(pos[k])-max(Counter(h[1::2]).values())for k,h in hs.items()}
 if min(mins.values()) < -3:continue
 for exit in x['potential_children']:
  ts=feasible(hs,exit)
  if ts is None:continue
  ia=1 if hs['A'][3]==hs['A'][1] else 0;ib=1 if hs[exit][3]==hs[exit][1] else 0
  rows.append(dict(headings=hs,exit=exit,bits=(ia,ib),minL=mins,times=ts))
print('rows',len(rows));print(Counter((x['exit'],x['bits'])for x in rows))
for x in rows:print(x['headings'],x['exit'],x['bits'])
# Frozen local certificate retains complete face profiles and exact inequality witnesses.
for x in rows:
 x['profile']=next(q for q in v if q['headings']==x['headings'])
assert len(rows)==20 and all(x['bits'][0]==x['bits'][1]for x in rows)
p=r/'reverse_even_plateau_span3_face_modes.json'
p.write_text(json.dumps(dict(scope='All even WHITE corners of one locally maximum plateau face, L floor lambda-3, full K1 entry/exit order; necessary local modes only.',count=len(rows),rows=rows),indent=2)+'\n')
