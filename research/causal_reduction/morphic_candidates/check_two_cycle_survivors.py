"""Exact sublattice exclusions for the two bounded-prefix survivors."""
import json,pathlib
HERE=pathlib.Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
rows=[]
summary=json.loads((HERE/'complementary_roots_l17.json').read_text())
for result in summary['results']:
 for r in result['survivors']:
  u,v=r['u'],r['v'];a,b=r['scale'];A=a*a-b*b;B=2*a*b;norm=A*A+B*B
  maps={c:''.join(u if z=='R'else v for z in w)for c,w in [('R',u),('L',v)]}
  assert maps['R'][0]=='R'and maps['L'][0]=='L'
  certificates=[]
  for c,w in maps.items():
   x=y=h=0;bad=[]
   for j,z in enumerate(w):
    if j and(x*A+y*B)%norm==0 and(y*A-x*B)%norm==0:bad.append([j,x,y])
    h=(h+(1 if z=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
   assert not bad
   assert (x,y,h)==((A,B,1)if c=='R'else(-A,-B,3))
   certificates.append(dict(letter=c,length=len(w),internal_phases=len(w)-1,sublattice_hits=bad,endpoint=[x,y,h]))
  # First read is R at origin; second is L at (1,0), a fresh nonzero cell.
  assert maps['R'][:2]=='RL'
  assert maps['L'][:3]=='LRL'
  rows.append(dict(u=u,v=v,scale=[a,b],squared_scale=[A,B],squared_norm=norm,images=certificates,explicit_first_L={'R_root':dict(time=1,cell=[1,0]),'L_root':dict(time=2,cell=[-1,1])},infinite_first_L_family='R root: times289^j, cells A^j; L root: times2*289^j, cells A^j*(-1+i), j>=0'))
assert len(rows)==2
out=dict(claim='Each survivor needs infinitely many initial black cells by exact coarse-vertex first-visit preservation for its squared substitution.',certificates=rows)
(HERE/'two_cycle_survivor_sublattice.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
