"""Complete RIGHT to bit11 maximum-branched RIGHT local port closure.
Necessary histories only, not a continuous exterior translator.
"""
from pathlib import Path
import ast,json
tree=ast.parse(Path(__file__).with_name('locked_RIGHT_to_branched_RIGHT_ports.py').read_text())
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),'<saved local functions>','exec'))
H='NESW'
source=json.loads(Path(__file__).with_name('right_turn_equal_branch_ports.json').read_text())
rows=[]
for report in source['reports']:
 for row in report['rows']:
  hh0={k:''.join(H[x] for x in a) for k,a in row['headings'].items()}
  if hh0['B']!='EEWE':continue
  ms=['WWW','WWWE','WEWW'] if report['Y_other']=='strict' else ['WWEW','EWWW']
  for nn,pp in [('NNSN','EWWW'),('SNNN','WWEW')]:
   for mm in ms:
    hh=dict(hh0,n=nn,p=pp,C='SSNS',m=mm)
    t=feasible({k:[H.index(x)for x in s]for k,s in hh.items()})
    if t is not None:rows.append(dict(prior_other=(report['Z_other'],report['Y_other']),headings=hh,minimum_clocks=t))
r=dict(scope=__doc__,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
