"""One further actual square at the early LEFT maximum parent.
Necessary complete ports and canonical birth, not an iterated gate proof.
"""
from pathlib import Path
from itertools import product
import ast,json
H="NESW"
src=Path(__file__).with_name('bit11_new_first_branch_full_ports.py').read_text()
# Reconstruct the inherited finite local feasibility function, then append one square.
ns={};exec(compile(ast.Module(body=[x for x in ast.parse(src).body if isinstance(x,ast.FunctionDef)and x.name=='rs'],type_ignores=[]),'r histories','exec'),globals())
base=Path(__file__).with_name('bit11_upper_branch_birth_ports.py').read_text();tree=ast.parse(base)
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name in ['out','ts']],type_ignores=[]),'helpers','exec'))
f=next(x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name=='feasible');ss=ast.get_source_segment(base,f)
ss=ss.replace("def feasible(h,kind,birth):", "def feasible(h,kind,birth,parent_birth):")
ss=ss.replace("('t','E','a','E')]", "('t','E','a','E'),('Z','S','q','S'),('q','E','h','E'),('h','N','A','N'),('q','W','r','W'),('r','N','e','N'),('e','E','Z','E'),('u','S','e','S'),('e','W','x','W'),('x','N','g','N'),('g','E','u','E')]")
ss=ss.replace("d={x:0 for x in ns}","for vv,oo in [('r','N'),('e','E'),('q','W')]:\n  rr=next(i for i,x in enumerate(oh[vv])if x==oo);es.append((('Z',1),(vv,rr),1))\n ff=[next((vv,rr)for rr,z in enumerate(oh[vv])if z==oo)for vv,oo in [('x','N'),('g','E'),('u','S'),('e','W')]]\n pb=(parent_birth,1)\n if pb not in ff:return\n for z in ff:\n  if z!=pb:es.append((pb,z,1))\n es.append((('e',0),('A',1),4))\n es.append((('A',1),('B',1),15))\n d={x:0 for x in ns}")
exec(ss)
rows=[];candidates=0
source=json.loads(Path(__file__).with_name('bit11_new_first_branch_full_ports.json').read_text())
for prior in source['rows']:
 if not prior['headings']['e'].startswith('S'):continue
 for (xh,xother),(gh,gother),pb in product(rs(),ts(),['x','g']):
  if pb=='x'and not xh.startswith('EEW'):continue
  if pb=='g'and not gh.startswith('SSN'):continue
  hs=dict(prior['headings'],x=xh,g=gh);candidates+=1
  t=feasible(hs,prior['kind'],prior['birth'],pb)
  if t is not None:rows.append(dict(kind=prior['kind'],headings=hs,parent_birth=pb,xother=xother,gother=gother,minimum_clocks=t))
r=dict(scope=__doc__,candidates=candidates,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(dict(scope=r['scope'],candidates=candidates,count=len(rows),profiles=sorted(set((x['headings']['e'],x['headings']['u'],x['headings']['x'],x['headings']['g'],x['parent_birth'])for x in rows))),indent=2))
