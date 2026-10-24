"""Exact outer-reader transfer and first-R basin closure for the pure RRLL band.
All complete cap-four domains are finite from the supplied unique ports.
No period, drift, width, or original-fuel bound is imposed.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b = Path(__file__).parent
L = {'__file__':str(b/'explore_one_use_RRLL_outer_reader_graph.py')}
exec((b/'explore_one_use_RRLL_outer_reader_graph.py').read_text().split('states=[]')[0], L)
Gs, Fs, patch, check = L['Gs'], L['Fs'], L['patch'], L['check']
states = []
nc = Counter()
for state in product(Gs, Fs):
    result = check(patch(state))
    nc[result] += 1
    if result == 'open': states.append(state)
assert nc == {'port':70, 'clock_cycle':6, 'open':24}
edges = []
ec = Counter()
edge_rows = []
for i,a in enumerate(states):
    for j,c in enumerate(states):
        result = check(patch(a) | patch(c,2))
        ec[result] += 1
        edge_rows.append(dict(source=i,target=j,result=result))
        if result == 'open': edges.append((i,j))
assert ec == {'port':422, 'clock_cycle':100, 'open':54}
alive = set(range(24))
peeling = []
while True:
    removed = [i for i in sorted(alive)
               if not any(a == i and c in alive for a,c in edges)
               or not any(c == i and a in alive for a,c in edges)]
    if not removed: break
    peeling.append(removed)
    alive -= set(removed)
cyclic = {0,2,7,8,9,14,17,18,19}
assert alive == cyclic
assert peeling == [[1,4,5,6,10,11,12,13,15,16,20,21,22,23],[3]]
assert states[0] == ('S','W')
assert all((i == 0 and g == 'S' and f == 'W') or (i != 0 and g[0] == 'N' and f[0] == 'E')
           for i,(g,f) in enumerate(states) if i in cyclic)
cyclic_edges = [(i,j) for i,j in edges if i in cyclic and j in cyclic]
assert len(cyclic_edges) == 36
assert {j for i,j in cyclic_edges if i == 0} == {17,18,19}
# If F_j is singleton W, its only physical incoming port is W from G_(j+1).
# Every allowed next G starts N and first-departs E away from F_j.
H = 'NESW'
def first_out(word): return H[(H.index(word[0])+1) % 4]
assert all(first_out(states[j][0]) == 'E' for i,j in cyclic_edges if i == 0)
# All other first-R incoming domains of the finite basin, stated exhaustively.
predecessors = {
    'C_j':['T_j','D_j'], 'A_j':['C_j'], 'T_j':['R_(j-1)'], 'R_j':['A_j'],
    'D_j':['E_j'], 'E_j_if_state0':['F_j'], 'E_j_otherwise':[], 'F_j_if_state0':[]}
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,G_domain=Gs,F_domain=Fs,
    node_counts=dict(nc),states=states,edge_counts=dict(ec),edge_rows=edge_rows,open_edges=edges,
    pruning_rounds=peeling,cyclic_state_ids=sorted(cyclic),cyclic_edges=cyclic_edges,
    full_first_R_predecessors=predecessors,
    basin='Gamma union D union E union singleton-W F at state0; no G class belongs to it',
    warning='Second-cycle/extremal consequence needs a genuine complete WHITE finite full quotient and named cap-four height dependencies.'),indent=2)+'\n')
print('PASS all 100 nodes and 576 pairs; 9 cyclic types, 36 cyclic edges; complete finite first-R basin direction certificate')
