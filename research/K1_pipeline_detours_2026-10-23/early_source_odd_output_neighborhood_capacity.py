"""Finite early-source odd-output neighborhood and rotated incidence capacity.
Only saved complete local ancestor inventories and exact affine offsets.
"""
from pathlib import Path
from collections import Counter
import json
root=Path(__file__).parent
rs=json.loads((root/'bit11_surviving_cleanup_Q1_parent_ports.json').read_text())['rows']
hit=('v','D','a','q','j')
oddsets=[{k for k,h in r['headings'].items()if len(h)%2}for r in rs]
assert all(not s or s&set(hit)for s in oddsets)
clean=[r for r,s in zip(rs,oddsets)if not s]
assert len(clean)==2
assert all((r['headings']['x'],r['headings']['r'],r['headings']['j'])==('EWWW','WEWW','EEWE')for r in clean)
coords=dict(v=(1,2),a=(0,2),q=(0,-1),j=(-3,1))
S=set(coords.values())|{(2,2),(2,1),(-3,-1),(-3,0),(-2,-1)}
R=[];U=set();cur=S
for q in range(4):
 R.append(sorted(cur));U|=cur;cur={(1-y,x)for x,y in cur}
assert len(S)==9 and len(U)==28
cnt=Counter((x+y)%2 for x,y in U)
assert cnt=={0:14,1:14}
out=dict(scope=__doc__,ancestor_rows=len(rs),odd_hitting_set=list(hit),all_odd_sets_hit=True,all_even_rows=len(clean),coordinates={k:list(v)for k,v in coords.items()},selected_D_coordinates_by_kind=dict(S=[2,2],R=[2,1]),new_lower_square_corners=[[-3,-1],[-3,0],[-2,-1]],normalized_offsets=sorted(S),four_rotations=R,rotation_union=sorted(U),union_count=len(U),checker_counts=dict(cnt),capacity='n_early <= 14 Nodd')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in ['four_rotations','rotation_union']},indent=2))
