#!/usr/bin/env python3
import json
from pathlib import Path
here=Path(__file__).resolve().parent
geo=json.loads((here/'../../../core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').resolve().read_text())
def rotate(p,h):
    x,y=p
    for _ in range(h): x,y=y,-x
    return x,y
spares={(2,3),(3,1),(3,2)}; main=(2,0)
rows=[]; candidates=0
for row in geo['geometry']:
    if row['name'] not in ('U','UC','UCC'): continue
    assert {tuple(q) for q in row['inputs']}=={(-1,1),(-1,2),(-1,4),(0,2),(0,3)}
    for h in range(4):
        J={rotate(q,h) for q in row['inputs']}
        poses={(p[0]-q[0],p[1]-q[1]) for p in spares for q in J}
        candidates+=len(poses)
        for p in sorted(poses):
            I={(p[0]+q[0],p[1]+q[1]) for q in J}
            if spares<=I:
                assert h==0 and p==(3,-1) and main in I
                rows.append(dict(packet=row['name'],head=[*p,h],inputs=sorted(map(list,I))))
assert len(rows)==3
result=dict(scope='All placements from exact input masks, no chronology claimed',
            candidate_poses=candidates,unique_geometry_placements=1,rows=rows)
here.joinpath('check_u_bulk_spares.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
