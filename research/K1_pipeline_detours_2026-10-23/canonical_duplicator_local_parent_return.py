"""Necessary local canonical D->J->P0->I return with all known cells four-read.
This is NOT an exterior realization or a complete WHITE positive front.
"""
from pathlib import Path
import ast,json
from itertools import product
base=json.loads(Path(__file__).with_name('canonical_max_face_child_ports.json').read_text())['rows']
s=Path(__file__).with_name('canonical_three_child_square_closure.py').read_text();tree=ast.parse(s)
H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0));cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1));op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name in ['rot','pose','outs']],type_ignores=[]),'poses','exec'))
f=next(x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name=='check');ss=ast.get_source_segment(s,f)
ss=ss.replace('def check(packages):','def check(packages,fh):')
ss=ss.replace('ns=[(p,r)for p,h in hh.items()for r in range(len(h))];es=[]',"hh[(-2,2)]=fh\n ns=[(p,r)for p,h in hh.items()for r in range(len(h))];es=[]")
exec(ss)
def find(h):return next(r for r in base if r['headings']==h)
F=find(dict(A='NNSN',Z='WWEW',Y='NSSS',B='EEWE'))
I=find(dict(A='NNSN',Z='WWWE',Y='NSNN',B='WEEE'))
parents=[r for r in base if r['headings']['A']=='NNSN'and r['headings']['B']=='EEWE'and all(len(x)==4 for x in r['headings'].values())]
Gs=[r for r in base if r['headings']['A']=='NNSN'and r['headings']['Z']=='WWWE'and all(len(x)==4 for x in r['headings'].values())]
rows=[];candidates=0
for j,p,g in product(parents,parents,Gs):
 qother=p['other']['Y']
 for fh in (['EEWE','WEEE']if qother=='M-2'else['EWEE','EEEW']):
  candidates+=1
  c=check([(F,(0,0),0),(j,(-1,-1),1),(p,(-2,0),0),(I,(-1,1),3),(g,(1,1),3)],fh)
  if c is not None:rows.append(dict(J=j['headings'],P0=p['headings'],G=g['headings'],f=fh,**c))
r=dict(scope=__doc__,candidates=candidates,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items()if k!='rows'},indent=2));print(json.dumps([dict(J=x['J'],P0=x['P0'],G=x['G'],f=x['f'])for x in rows],indent=2))
