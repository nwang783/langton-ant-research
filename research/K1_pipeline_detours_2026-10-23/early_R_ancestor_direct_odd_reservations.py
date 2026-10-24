"""Complete lower square and canonical producer at an early RIGHT ancestor.
Saved complete110 inventory, all rotations; no front or period scan.
"""
from pathlib import Path
from collections import Counter
import ast,json
root=Path(__file__).parent
H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0))
cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1));op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
t=ast.parse((root/'canonical_three_child_square_closure.py').read_text());exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))
base=json.loads((root/'canonical_max_face_child_ports.json').read_text())['rows']
prior=json.loads((root/'bit11_surviving_cleanup_Q1_parent_ports.json').read_text())['rows']
R=[r for r in prior if r['headings']['j']=='EEWE'];S=[r for r in prior if r['headings']['j']=='W']
assert len(R)+len(S)==len(prior)
mode_counts=Counter((r['headings']['x'],r['headings']['r'],r['headings']['e'])for r in R)
assert set(mode_counts)=={('EWW','WEEW','SNN'),('EWWW','WEW','SNNN'),('EWWW','WEWW','SNNN')}
F=[];Q=[]
for row in base:
 for q in range(4):
  hh,fs,en,bd=pose(row,(-3,-1),q)
  if hh.get((-2,0))=='EWWW':
   d=hh[(-3,0)];t=hh[(-2,-1)]
   if d.count('S')==1 and outs(d).count('E')==1 and outs(t).count('E')==1:F.append(dict(physical={str(p):h for p,h in hh.items()},entry=list(en),rotation=q,canonical_profile=row['headings'],potential_children=row['potential_children']))
  hh,fs,en,bd=pose(row,(-4,0),q)
  if hh.get((-3,0))=='NNS' and hh.get((-3,1))=='EEWE':
   flags=sum(row['headings'][k]==p for k,p in [('Z','WWEW'),('Y','NNSN'),('B','EEWE')])
   assert en==(-3,0) and len(row['headings']['A'])==3 and flags==1
   Q.append(dict(physical={str(p):h for p,h in hh.items()},entry=list(en),rotation=q,canonical_profile=row['headings'],potential_children=row['potential_children'],flag_one_potential_count=flags))
assert len(F)==1 and F[0]['physical']=={'(-3, -1)':'EEWW','(-3, 0)':'NNS','(-2, 0)':'EWWW','(-2, -1)':'SSS'}
assert len(Q)==4
out=dict(scope=__doc__,ancestor_rows=len(prior),R_rows=len(R),S_rows=len(S),R_modes=[dict(x=x,r=r,e=e,count=n)for(x,r,e),n in sorted(mode_counts.items())],lower_F_completions=F,Q2_completions=Q,capacity='Nodd >= n_Sanc + n_R3 + 2*n_R4 = n_A + n_R4')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
