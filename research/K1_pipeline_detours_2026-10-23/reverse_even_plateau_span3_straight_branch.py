"""Even WHITE-collar plateau: zero-bit straight branch and its exact Q-face square.
Three selected faces plus one forced equal-height branch, not a front scan.
"""
from pathlib import Path
from itertools import product
import ast,json
root=Path('/workspace/shared/langton/K1_pipeline_detours_2026-10-23');rows=json.loads((root/'reverse_even_plateau_span3_face_modes.json').read_text())['rows'];H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0));cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1));op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
s=(root/'canonical_three_child_square_closure.py').read_text();tree=ast.parse(s)
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in['rot','pose','outs']],type_ignores=[]),'poses','exec'))
f=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='check');ss=ast.get_source_segment(s,f).replace('def check(packages):','def check(packages,links):')
ss=ss.replace('d={x:0 for x in ns}',"for entry,exit in links:\n  es.extend([((entry,1),(exit,0),1),((exit,0),(entry,2),1),((entry,2),(exit,1),1)])\n d={x:0 for x in ns}")
exec(ss)
R=[x for x in rows if x['bits']==[0,0]];S=[x for x in R if x['exit']=='Y'];surv=[];attempts=0
qr={'Z':3,'Y':0,'B':1}
def exitpos(part,ll,q):
 return pose(part['profile'],ll,q)[0] # actual marker use cp then cell formula

def cell(p,ll,q):
 a,b=rot((2*p[0]-1,2*p[1]-1),q);return((a+1)//2+ll[0],(b+1)//2+ll[1])
for prev,cur,nxt in product(R,S,R):
 q=qr[prev['exit']];pe=cell(cp['A'],(1,-1),q);nx=cell(cp[nxt['exit']],(-1,1),0);links=[(pe,(1,0)),((1,0),(0,1)),((0,1),nx)];parts=[(prev['profile'],(1,-1),q),(cur['profile'],(0,0),0),(nxt['profile'],(-1,1),0)];attempts+=1;z=check(parts,links)
 if z:surv.append((prev,cur,nxt,parts,links,z))
selected_attempts=attempts; selected_survivors=len(surv)
# Complete the actual equal-height branch J with its true canonical birth,
# but no selected-cycle membership or direction is imposed at J.
base=json.loads((root/'canonical_max_face_child_ports.json').read_text())['rows'];opts=[]
for x in base:
 if any(len(h)%2 for h in x['headings'].values()):continue
 pos={'A':'S','Z':'W','Y':'N','B':'E'}
 if any(-h[::2].count(pos[k])-max(h[1::2].count(a)for a in set(h)) < -3 for k,h in x['headings'].items()):continue
 opts.append(x)
closed=[];att=0
for prev,cur,nxt,parts,links,z in surv:
 for row,q in product(opts,range(4)):
  att+=1;y=check(parts+[(row,(-1,-1),q)],links)
  if y:closed.append(dict(prev=prev,cur=cur,next=nxt,J=row,Jrotation=q,**y))
assert len(closed)==2
assert all(q['prev']['exit']=='B'and q['next']['exit']=='B'and q['Jrotation']==0 for q in closed)
assert all(q['headings']['(0, -1)']=='NNSS'and q['headings']['(-1, -1)']=='EWWE'and q['headings']['(-1, 0)']=='NSSN'and q['headings']['(0, 0)']=='WWEE' for q in closed)
out=dict(scope=__doc__,selected_attempts=selected_attempts,selected_survivors=selected_survivors,branch_attempts=att,count=len(closed),rows=closed)
p=root/'reverse_even_plateau_span3_straight_branch.json';p.write_text(json.dumps(out,indent=2)+'\n');print('PASS',selected_attempts,'selected triples;',att,'branch additions; exactly two retained side-obstructed profiles')
