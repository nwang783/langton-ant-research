"""Independent strip/bridge reconstruction and literal local face-loop controls.
This is deliberately NOT one live ant trajectory.
"""
from pathlib import Path
from collections import Counter
from itertools import product
import json,hashlib
B=Path('/workspace/shared/langton');tests=steps=reads=0;peak=0
for a,b,w,h,direction in product((-4,0,6),(-6,0,4),(1,3,5,9),(1,3,7,11),range(4)):
 K={(x,y)for x in range(a,a+w)for y in range(b,b+h)};board={complex(x,y)for x,y in((a,b),(a+w,b),(a,b+h),(a+w,b+h))}
 # Use one generic right-growth schedule in a local orthogonal frame.
 if direction==0:origin=complex(a,b);along=1j;normal=1;width=w;height=h
 if direction==1:origin=complex(a+w,b);along=1j;normal=-1;width=w;height=h
 if direction==2:origin=complex(a,b);along=1;normal=1j;width=h;height=w
 if direction==3:origin=complex(a,b+h);along=1;normal=-1j;width=h;height=w
 # Expansion outward from the chosen old boundary, with outer/bridge strips.
 boundary=origin+normal*width
 # For negative direction origin was the opposite endpoint, so this still
 # places boundary at the edge to be expanded.
 order=[(width+1,0)]+[(width+1,jj)for j in range(2,height,2)for jj in(j,j-1)]+[(width,jj)for j in range(1,height-1,2)for jj in(j,j-1)]+[(width,height-1)]
 for u,v in order:
  corners={origin+normal*(u+du)+along*(v+dv)for du,dv in product((0,1),repeat=2)}
  ll=complex(min(z.real for z in corners),min(z.imag for z in corners));q=int(ll.real),int(ll.imag);assert q not in K
  positive=sum(q)%2==0;assert (not(board&corners)) if positive else corners<=board
  # Each elementary operation really is a literal loop in one fixed sector.
  z=ll;head=-1 if positive else -1j;turn='R' if positive else 'L';assert int(z.real+z.imag+(3 if positive else 2))%2==1
  before=board.copy()
  for _ in range(4):
   assert (z in board)==(turn=='L');board.symmetric_difference_update([z]);head*=(-1j if turn=='R' else 1j);z+=head;reads+=1;peak=max(peak,len(board));assert len(board)<=12
  assert z==ll and board==before^corners
  K.add(q);steps+=1
  # Full mixed difference and all marginal charges, not just local toggling.
  delta=Counter()
  for x,y in K:
   for dx,dy,sgn in((0,0,1),(1,0,-1),(0,1,-1),(1,1,1)):delta[x+dx,y+dy]+=sgn
  assert {z:v for z,v in delta.items()if v}=={(int(z.real),int(z.imag)):(-1)**int(z.real+z.imag)for z in board}
  rows=Counter();cols=Counter()
  for z in board:rows[z.imag]+=(-1)**int(z.real);cols[z.real]+=(-1)**int(z.imag)
  assert not any(rows.values()) and not any(cols.values())
 assert len(board)==4 and len(K)==w*h+2*height;tests+=1
out=dict(status='PASS independent all-parity strip/bridge and local face-loop controls',rectangle_expansions=tests,unit_increments=steps,literal_interpolated_reads=reads,maximum_mass=peak,is_one_ant_trajectory=False,proof_scope='Explicit infinite relaxation schedule by odd-rectangle induction; continuous cursor coupling is absent.',subject_sha256=hashlib.sha256((B/'global_capture_bridge_2026-10-23/unit_height_bounded_mass_obstruction.md').read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
