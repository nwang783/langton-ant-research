"""Exact four-face LRLR overlap inside an even WHITE-collar local maximum.
Retains all source ports, lambda-3 L floor, true face births and K1 order.
"""
from pathlib import Path
from itertools import product
import json,ast
root=Path(__file__).parent;rows=json.loads((root/'reverse_even_plateau_span3_face_modes.json').read_text())['rows'];H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0));cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1));op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
s=(root/'canonical_three_child_square_closure.py').read_text();tree=ast.parse(s)
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in['rot','pose','outs']],type_ignores=[]),'poses','exec'))
f=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='check');ss=ast.get_source_segment(s,f)
ss=ss.replace('def check(packages):','def check(packages,links,qh):')
ss=ss.replace('ns=[(p,r)for p,h in hh.items()for r in range(len(h))];es=[]',"hh[(0,-1)]=qh\n rs=qh[::2]\n if rs.count('S')-rs.count('N')!=heights[(-1,-1)]:return\n ns=[(p,r)for p,h in hh.items()for r in range(len(h))];es=[]")
ss=ss.replace('d={x:0 for x in ns}',"for entry,exit in links:\n  es.extend([((entry,1),(exit,0),1),((exit,0),(entry,2),1),((entry,2),(exit,1),1)])\n d={x:0 for x in ns}")
exec(ss)
positions=[((1,-1),3),((0,0),0),((1,1),3),((0,2),0)];contacts=[(1,-1),(1,0),(1,1),(1,2),(1,3)];links=list(zip(contacts,contacts[1:]));out=[];counts={}
for bit in(0,1):
 L=[r for r in rows if r['exit']=='Z'and r['bits']==[bit,bit]];R=[r for r in rows if r['exit']=='B'and r['bits']==[bit,bit]];attempts=0;surv=[]
 qoptions=[]
 for n in(2,4):
  for h in product('NS',repeat=n):
   h=''.join(h);rn=h[::2].count('N');rs=h[::2].count('S');lm=max(h[1::2].count(x)for x in'NS')
   if rn>=rs and -rn-lm>=-3:qoptions.append(h)
 for parts,qh in product(product(L,R,L,R),qoptions):
  attempts+=1;packages=[(p['profile'],ll,q)for p,(ll,q)in zip(parts,positions)];z=check(packages,links,qh)
  if z is not None:surv.append(dict(bit=bit,face_headings=[p['headings']for p in parts],**z))
 counts[bit]=dict(attempts=attempts,survivors=len(surv));out.extend(surv)
print('COUNTS',counts)
assert counts[0]['survivors']==0
assert out and all(r['face_headings'][1]==dict(A='NNSN',Z='WWWE',Y='NNNS',B='EEWE')for r in out)
p=root/'reverse_even_plateau_span3_LRLR_overlap.json';p.write_text(json.dumps(dict(scope=__doc__,counts=counts,rows=out),indent=2)+'\n');print('PASS',counts,'all first RIGHT faces locked to strict row4')
