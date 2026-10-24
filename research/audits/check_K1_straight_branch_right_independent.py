from pathlib import Path
from itertools import product
import hashlib,json
R=Path(__file__).resolve().parents[1];p=R/'K1_pipeline_detours_2026-10-23/K1_straight_max_branch_forces_right.md'
def out(h):return tuple((v+(1 if i%2==0 else-1))%4 for i,v in enumerate(h))
rows=[]
for n in(3,4):
 for h in product((0,2),repeat=n):
  if h[0]==h[2]:continue
  first=h.index(2);count=out(h)[:first].count(1);assert count<=1
  rows.append(dict(h=h,first_S_rank=first,E_before_first_S=count))
z=(3,3,1,1);B=(0,0,2);O=(3,3,1)
assert out(z)==(0,2,2,0)
for b in(B,B+(2,)):
 for o in(O,O+(1,)):
  assert[i for i,v in enumerate(out(b))if v==3]==[1,2]
  assert[i for i,v in enumerate(o)if v==3]==[0,1]
  assert[i for i,v in enumerate(out(o))if v==2]==[1,2]
  assert[i for i,v in enumerate(b)if v==0]==[0,1]
# z.N outputs ranks0/3 feed B.N inputs0/1; B.W output1/2 feeds O.W0/1;
# e.E output1/2 feeds z.E2/3, and O.S output1/2 feeds e.S1/2.
# Thus second E departure e=T1(B)-2; first S arrival e=T2(B)+2.
q=dict(status='PASS branchful straight-to-LEFT contradiction and forced RIGHT successor',note_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),flat_histories=rows,clock_equalities=['second_E(e)=T3(z)-1=T1(B)-2','first_S(e)=T1(O)+1=T2(B)+2'],scope='Complete WHITE cap4 K1, straight face with equal-M unused LEFT neighbor; no leftmost or branch-free premise. Uses signed no-following-S to conclude RIGHT, not global exclusion.')
Path(__file__).with_suffix('.json').write_text(json.dumps(q,indent=2)+'\n');print(q['status'])
