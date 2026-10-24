"""Full canonical upper/lower half-turn rail profiles and nonpositive odd cover.
No front search: complete110 profiles, four rotations and physical port counts.
"""
from pathlib import Path
import ast,json
root=Path(__file__).parent
H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0));cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1));op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
t=ast.parse((root/'canonical_three_child_square_closure.py').read_text());exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))
base=json.loads((root/'canonical_max_face_child_ports.json').read_text())['rows']
def pos(s):return len(s)==3 and s[0]!=s[1] and s[1]==s[2]
def package(hh,en,row,q,cover):
 odd={p:h for p,h in hh.items()if len(h)%2}
 witness=[p for p in cover if p in odd and not pos(odd[p])]
 assert not odd or witness
 return dict(physical={str(p):h for p,h in hh.items()},entry=list(en),rotation=q,canonical_profile=row['headings'],odd=[list(p)for p in odd],nonpositive_cover=[list(p)for p in witness])
upper=[];lower=[]
for row in base:
 for q in range(4):
  hh,fs,en,bd=pose(row,(-1,1),q)
  if hh.get((0,1))=='SSNS' and fs.get((0,2))==-2:
   upper.append(package(hh,en,row,q,[(-1,1),(-1,2),(0,2)]))
  hh,fs,en,bd=pose(row,(-1,-1),q)
  if hh.get((0,0))=='WWEW' and en==(0,0) and hh[(-1,0)].count('S')==1 and outs(hh[(0,-1)]).count('E')==1:
   lower.append(package(hh,en,row,q,[(0,-1),(-1,-1)]))
assert len(upper)==5 and len(lower)==9
S={(-1,1),(-1,2),(0,2),(0,-1),(-1,-1)};U=set();cur=S
for q in range(4):U|=cur;cur={(1-y,x)for x,y in cur}
assert len(U)==12 and all(sum((x+y)%2==p for x,y in U)==6 for p in (0,1))
out=dict(scope=__doc__,upper_count=len(upper),lower_count=len(lower),upper=upper,lower=lower,normalized_cover=sorted(S),four_rotation_union=sorted(U),union_count=len(U),checker_counts=[6,6],capacity='H <= 6*(Nodd-Npos)+|U| <= 7*(Nodd-Npos)-nSanc')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['upper','lower']},indent=2))
