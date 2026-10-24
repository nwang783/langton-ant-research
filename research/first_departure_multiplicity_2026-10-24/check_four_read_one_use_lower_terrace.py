"""Exact lower-C supplier at a four-read one-use alternating body.
Open component calendars are not physical seed factors or complete fronts.
"""
from pathlib import Path
import json
b = Path(__file__).parent
L = {'__file__': str(b / 'check_even_reader_rail_and_merge_reset.py')}
exec((b / 'check_even_reader_rail_and_merge_reset.py').read_text().split('rows=[]')[0], L)
check, graph = L['check'], L['graph']
A, R, B, S, C, U, V, E = (0,-1), (0,0), (1,0), (1,1), (2,1), (1,-1), (2,0), (2,-1)
fixed = {A:'WWEW', R:'N', B:'WWEW', S:'N', C:'WWEW', U:'SSSN', V:'SSSN'}
rows = []
for word in ['EWW', 'EWWW', 'WWE', 'WWEW']:
    hs = fixed | {E:word}
    result = check(hs)
    row = dict(reader=word, result=result)
    if result == 'open':
        assert word in ['EWW', 'EWWW']
        successor, components, order, times = graph(hs)
        paths = [[(B,2), (U,1), (E,0)], [(E,2), (V,3), (B,3)]]
        assert all(successor[x] == y for p in paths for x,y in zip(p,p[1:]))
        assert times[E,0] == times[B,2] + 2
        assert times[B,3] == times[E,2] + 2
        row |= dict(histories={str(p):h for p,h in hs.items()}, exact_paths=paths,
                    components=components, component_order=order,
                    distinct_mod4_calendar={str(e):t for e,t in times.items()}, events=len(times))
    else:
        assert result == 'clock_cycle'
    rows.append(row)
# Index/occurrence ownership of the circular ten-edge channel, independent
# of a small or nonminimal full quotient. Family offsets x-y are distinct.
channel = [('E',0,2), ('D',0,3), ('A',0,3), ('D',-1,2), ('A',-1,1),
           ('D',-2,0), ('A',-2,0), ('R',-2,0), ('A',-1,2), ('D',-2,1), ('E',-1,0)]
for n in range(1,9):
    uses = []
    for i in range(n):
        uses += [(family, (i+j)%n, rank) for family,j,rank in channel[:-1]]
    assert len(uses) == len(set(uses)) == 10*n
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,rows=rows,
    circular_channel_family_index_rank=channel, circular_occurrence_controls='n=1..8 confirm the stated all-index bijective role formulas only',
    stream_levels=dict(boundary_C='M', lower_C='M-2', lower_N_side_L='M-3', lower_S_side_L='M-4 or M-5'),
    warning='No reader outside these cells is physically connected; the circles and translating fronts are conditional, not attained controls.'),indent=2)+'\n')
print('PASS two25/26-event lower-terrace calendars, two clock failures, exact nested supplier paths and all-index channel roles')
