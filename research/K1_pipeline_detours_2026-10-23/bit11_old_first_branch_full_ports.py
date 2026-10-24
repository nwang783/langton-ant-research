"""Necessary old-first-branch closure through both physical maximum squares.
Not a literal exterior translator or original-root charge.
"""
from pathlib import Path
from itertools import product
import ast,json
s=Path(__file__).with_name('bit11_upper_branch_birth_ports.py').read_text();tree=ast.parse(s)
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name in ['out','ts']],type_ignores=[]),'old local helpers','exec'))
f=next(x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name=='feasible');ss=ast.get_source_segment(s,f)
ss=ss.replace("('t','E','a','E')]", "('t','E','a','E'),('Z','S','q','S'),('q','E','h','E'),('h','N','A','N'),('q','W','r','W'),('r','N','e','N'),('e','E','Z','E'),('u','S','e','S')]")
ss=ss.replace("d={x:0 for x in ns}","es.append((('r',1),('Z',1),1))\n d={x:0 for x in ns}")
exec(ss)
H='NESW';rows=[];candidates=0
source=json.loads(Path(__file__).with_name('bit11_upper_branch_birth_ports.json').read_text())
for prior in source['rows']:
 for qh,rh,(eh,other) in product(['SSS','SSSN'],['EEW','EEWE','EEWW'],ts()):
  # At e, SE J=M; its opposite is the P0 fixed by u.
  if prior['lower_other']=='M' and other!='equal':continue
  if prior['lower_other']=='M-1' and (other!='strict' or (len(eh)+1)//2!=1):continue
  hs=dict(prior['headings'],q=qh,r=rh,e=eh,h='WWWE');candidates+=1
  t=feasible(hs,prior['kind'],prior['birth'])
  if t is not None:rows.append(dict(kind=prior['kind'],headings=hs,birth=prior['birth'],minimum_clocks=t))
r=dict(scope=__doc__,candidates=candidates,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(dict(scope=r['scope'],candidates=candidates,count=len(rows),profiles=sorted(set((x['headings']['q'],x['headings']['r'],x['headings']['e'],x['headings']['u'],x['headings']['t'],x['headings']['a'],x['birth'])for x in rows))),indent=2))
