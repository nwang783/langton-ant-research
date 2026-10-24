"""Finite exact junction transfer graph for a whole one-use RRLL staircase.
States are complete two-column LL reader interfaces; edges are full adjacent
physical twelve-cell ordinal/clock patches. No period or drift scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b = Path(__file__).parent
L = {'__file__':str(b/'check_even_reader_rail_and_merge_reset.py')}
exec((b/'check_even_reader_rail_and_merge_reset.py').read_text().split('rows=[]')[0], L)
check = L['check']

def words(axis):
    return [''] + [''.join(z) for n in range(1,5) for z in product(axis,repeat=n)]

def patch(state, shift=0):
    s,t,d,e = state
    return {(shift,0):'NNS'+('N' if s else ''), (shift+1,0):'WWE'+('W' if t else ''),
            (shift,1):'E', (shift+1,1):'N', (shift,-1):d, (shift+1,-1):e}

states = []
node_counts = Counter()
for s,t,d,e in product([0,1],[0,1],words('EW'),words('NS')):
    state = (s,t,d,e)
    result = check(patch(state))
    node_counts[result] += 1
    if result == 'open': states.append(state)
print('states',len(states),node_counts,flush=True)
edges = []
edge_counts = Counter()
for i,a in enumerate(states):
    for j,c in enumerate(states):
        if a[1] != c[0]:
            continue
        result = check(patch(a) | patch(c,2))
        edge_counts[result] += 1
        if result == 'open': edges.append((i,j))
adj = {i:[] for i in range(len(states))}
for i,j in edges: adj[i].append(j)
index = {}; low = {}; stack = []; active=set(); scc=[]
def visit(v):
    index[v] = low[v] = len(index)
    stack.append(v);active.add(v)
    for w in adj[v]:
        if w not in index: visit(w);low[v]=min(low[v],low[w])
        elif w in active: low[v]=min(low[v],index[w])
    if low[v] == index[v]:
        part=[]
        while True:
            w=stack.pop();active.remove(w);part.append(w)
            if w==v: break
        scc.append(part)
for i in adj:
    if i not in index:visit(i)
cyclic=[part for part in scc if len(part)>1 or (part[0],part[0])in edges]
print('edges',len(edges),edge_counts,'cyclicSCC',cyclic,flush=True)
for part in cyclic:
    print([(i,states[i])for i in part],flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,node_counts=dict(node_counts),states=states,
    edge_counts=dict(edge_counts),edges=edges,cyclic_components=cyclic,
    warning='Discovery graph only; cyclic adjacency does not certify a whole-period field or chronological orbit.'),indent=2)+'\n')
