"""Physical first-R predecessor exhaustion for the even-reader whole staircase.
Index controls corroborate algebraic formulas; they do not construct a front.
"""
from pathlib import Path
import json
H = 'NESW'
V = {'N':(0,1), 'E':(1,0), 'S':(0,-1), 'W':(-1,0)}
WORDS = {'A':'WWEW', 'R':'N', 'D':'SSSN', 'E':'EWW'}

def point(family, i):
    return {'A':(i+1,i), 'R':(i+1,i+1), 'D':(i+2,i), 'E':(i+2,i-1)}[family]

def identify(p):
    x, y = p
    family = {0:'R', 1:'A', 2:'D', 3:'E'}.get(x-y)
    if family is None:
        return None
    i = y-1 if family == 'R' else y+1 if family == 'E' else y
    assert point(family, i) == p
    return family, i

def first_destination(family, i):
    p = point(family, i)
    heading = WORDS[family][0]
    direction = H[(H.index(heading)+1) % 4]
    vector = V[direction]
    return p[0]+vector[0], p[1]+vector[1]

rows = []
for family in ['A','R','D']:
    target = point(family, 0)
    predecessors = []
    for direction in H:
        arrivals = [r for r, h in enumerate(WORDS[family]) if h == direction]
        if not arrivals:
            continue
        vector = V[direction]
        source = target[0]-vector[0], target[1]-vector[1]
        source_id = identify(source)
        assert source_id is not None
        hits = first_destination(*source_id) == target
        if hits:
            predecessors.append(source_id)
        rows.append(dict(target_family=family, input_direction=direction,
                         complete_arrival_ranks=arrivals, physical_source=source,
                         source_family_index=source_id, first_destination=first_destination(*source_id),
                         is_first_R_predecessor=hits))
    expected = {'A':[('R',-1),('D',0)], 'R':[('A',0)], 'D':[]}[family]
    assert sorted(predecessors) == sorted(expected)
for n in range(1,9):
    classes = [(family, i) for family in WORDS for i in range(n)]
    assert len(classes) == 4*n
    # Full drift is (-n,-n); transverse offsets prove no cross-family alias.
    assert len({point(f,i)[0]-point(f,i)[1] for f in WORDS for i in [0]}) == 4
    for i in range(n):
        assert identify(first_destination('D',i)) == ('A',i)
        assert identify(first_destination('A',i)) == ('R',i)
        assert identify(first_destination('R',i)) == ('A',i+1)
        assert identify(first_destination('E',i)) is None
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,physical_predecessor_rows=rows,
    all_index_formulas=dict(predecessors_A=['R_(i-1)','D_i'], predecessors_R=['A_i'], predecessors_D=[],
                            basin='Gamma union D', outside_E='not in basin, on geometric RIGHT'),
    full_quotient_controls=list(range(1,9)),
    warning='No exterior successor completion or controller is supplied. The second-cycle conclusion uses a genuine finite full quotient and complete WHITE b-map.'),indent=2)+'\n')
print('PASS all physical input ports and predecessor directions; full-index basin closure, short-quotient roles')
