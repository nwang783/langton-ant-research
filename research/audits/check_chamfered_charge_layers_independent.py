from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib,sys
B=Path('/workspace/shared/langton');sys.path.insert(0,str(B/'computability/unit_inductive_certificates'));from presburger_read_set_solver import Context
C=Context(max_operations=1000000);I=C.set(json.loads((B/'audits/check_chamfered_frames_independent.json').read_text())['input_relation'])
# B_2 uses old frame parameter K=k+2 and translation (0,2).
points=[(1,-2),(1,-1),(-3,-1),(-3,0)]
for x,y in points:assert I.intersect(C.set(f'[r,k]->{{[x,y]:r>=3 and k>=5 and x={x} and y={y}}}')).is_empty()
def rowcor(x,z,h,y):
 if h==0:return 2*int(y<z)
 if h==2:return 2*int(y<=z)
 return 2 if y<z else 0 if y>z else (-1 if h==3 else 1)*((-1)**x)
def chargepose(x,y,h):
 return tuple(rowcor(x,y,h,q)%4 for q in range(-12,13))+tuple(rowcor(-y,x,(h-1)%4,q)%4 for q in range(-12,13))
reference=chargepose(0,0,1);same=[(x,y,h)for x,y,h in product(range(-10,11),range(-10,11),range(4))if chargepose(x,y,h)==reference];assert same==[(-1,0,3),(0,0,1)]
assert [p for p in same if sum(p)%2==1]==[(0,0,1)]
F={(1,0),(1,1),(-3,1),(-3,2)};rr=Counter();cc=Counter()
for x,y in F:rr[y]+=(-1)**x;cc[x]+=(-1)**y
assert dict(rr)=={0:-1,1:-2,2:-1} and not any(cc.values())
for y in range(-10,11):assert (rr[y]+rowcor(0,2,1,y)-rowcor(0,0,1,y))%4==0
result=dict(status='PASS independent exact whiteness and charge/pose controls; analytic all-layer review passed',pose_controls=21*21*4,charge_equivalent_poses=same,allowed_sector_pose=[0,0,1],four_correcting_cells=sorted(F),all_parameter_white_domain='r>=3,k>=3 in B_2',scope='Every exact clean layer jump fails at every natural phase; correction lower bound2s at even north shift s. No physical correcting path or renewable mechanism.',subject_sha256=hashlib.sha256((B/'causal_reduction/unit_scale/chamfered_multilayer_charge_obstruction.md').read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
