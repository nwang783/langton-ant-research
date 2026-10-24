"""Explicit physical direction replay for every cyclic outer-reader pair.
Additive certificate to b4a5265e; no frozen source is changed.
"""
from pathlib import Path
import json
b = Path(__file__).parent
j = json.loads((b/'check_RRLL_outer_reader_basin.json').read_text())
H = 'NESW'
VEC = {'N':(0,1), 'E':(1,0), 'S':(0,-1), 'W':(-1,0)}
rows = []

def family(p):
    x,y = p
    return {1:('T','R'),0:('C','A'),-1:('D','E'),-2:('G','F')}[y][x%2], x//2

for source_id, next_id in j['cyclic_edges']:
    state, nxt = j['states'][source_id], j['states'][next_id]
    def word(p):
        x,y = p
        if y in [-1,0,1]:
            return {1:('E','N'),0:('NNSN','WWEW'),-1:('WWWE','SSSN')}[y][x%2]
        assert y == -2 and x//2 in [0,1]
        return (state if x//2 == 0 else nxt)[x%2]
    targets = [(0,1),(1,1),(0,0),(1,0),(0,-1),(1,-1)]
    if source_id == 0: targets.append((1,-2))
    for target in targets:
        tf, _ = family(target)
        actual = []
        for direction, vec in VEC.items():
            ranks = [r for r,z in enumerate(word(target)) if z == direction]
            rec = dict(current_state=source_id,next_state=next_id,target=target,target_family=tf,
                       input_direction=direction,complete_arrival_ranks=ranks)
            if ranks:
                p = target[0]-vec[0], target[1]-vec[1]
                h = word(p)
                out = H[(H.index(h[0])+1)%4]
                v = VEC[out]
                dest = p[0]+v[0],p[1]+v[1]
                hits = dest == target
                rec |= dict(physical_source=p,source_word=h,first_R_destination=dest,hits=hits)
                if hits: actual.append(family(p))
            rows.append(rec)
        expect = {'C':[('T',0),('D',0)],'A':[('C',0)],'T':[('R',-1)],'R':[('A',0)],
                  'D':[('E',0)],'E':[('F',0)] if source_id == 0 else [],'F':[]}[tf]
        assert sorted(actual) == sorted(expect), (source_id,next_id,target,actual,expect)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,cyclic_pair_count=36,
    physical_direction_rows=rows,warning='Exact local predecessor closure only; the global consequence still requires a genuine finite WHITE quotient and critical cap-four cycle-height theorem.'),indent=2)+'\n')
print('PASS all 36 cyclic pairs and',len(rows),'complete physical direction domains, including zero ports')
