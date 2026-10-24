"""All-length24-state exact RRLL one-use transfer; no period or drift cutoff.
Full GLOBAL-M local node/edge domains, then a finite strict-rank certificate.
Surviving lower ports remain open, not a translating front.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b = Path(__file__).parent
L = {'__file__':str(b/'explore_one_use_RRLL_transfer_graph.py')}
exec((b/'explore_one_use_RRLL_transfer_graph.py').read_text().split('states = []')[0], L)
check, words, patch = L['check'], L['words'], L['patch']
X = {}
exec((b/'check_even_portal_entry_incidence.py').read_text().split('words=')[0], X)
exact, out, VEC = X['exact'], X['out'], X['V']
states = []
node_counts = Counter()
node_nonport = []
for s,t,d,e in product([0,1],[0,1],words('EW'),words('NS')):
    state = (s,t,d,e)
    result = check(patch(state))
    node_counts[result] += 1
    if result != 'port':
        node_nonport.append(dict(state=state,result=result))
    if result == 'open':
        states.append(state)
assert len(states) == 24
assert node_counts == {'port':3783,'skipped_rank':26,'clock_cycle':10,'global_C_max':1,'open':24}
edges = []
edge_rows = []
edge_counts = Counter()
for i,a in enumerate(states):
    for j,c in enumerate(states):
        if a[1] != c[0]:
            continue
        hs = patch(a) | patch(c,2)
        result, certificate = exact(hs)
        if result == 'rank':
            result = 'skipped_rank'
        assert result == check(hs)
        edge_counts[result] += 1
        edge_rows.append(dict(source=i,target=j,result=result,certificate=certificate))
        if result == 'open':
            edges.append((i,j))
assert edge_counts == {'port':126,'skipped_rank':150,'open':18}
assert states[23] == (1,1,'WWWE','SSSN')
rank = {i:0 for i in range(24)}
for i in [2,5,12,14,16]:
    rank[i] = 1
assert all((i == j == 23) or rank[i] > rank[j] for i,j in edges)
assert [(i,j) for i,j in edges if i == j] == [(23,23)]
# Exact physical nineteen-edge passage through the surviving homogeneous band.
def band_word(p):
    x,y = p
    return {1:('E','N'),0:('NNSN','WWEW'),-1:('WWWE','SSSN')}[y][x%2]
path = [((1,-1),3)]
while True:
    p,r = path[-1]
    h = band_word(p)
    direction = out(h,r)
    vector = VEC[direction]
    q = p[0]+vector[0],p[1]+vector[1]
    sources = [a for a in range(len(h)) if out(h,a) == direction]
    ordinal = sources.index(r)
    if q[1] not in [-1,0,1]:
        assert direction == 'S' and q == (-2,-2) and ordinal == 0
        exit_cell = q
        break
    targets = [a for a,z in enumerate(band_word(q)) if z == direction]
    assert len(sources) == len(targets)
    path.append((q,targets[ordinal]))
assert len(path) == 18
# An initial edge from F_0=(1,-2) Nout_only enters the displayed E_0.L3.
assert path[0] == ((1,-1),3)
roles = []
for (x,y),r in path:
    family = {1:('T','R'),0:('C','A'),-1:('D','E')}[y][x%2]
    j = x//2
    roles.append((family,j,r))
for n in range(1,9):
    used = [(family,(j+i)%n,r) for i in range(n) for family,j,r in roles]
    assert len(used) == len(set(used)) == 18*n
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,node_counts=dict(node_counts),
    node_nonport_rows=node_nonport,states=states,edge_counts=dict(edge_counts),edge_rows=edge_rows,
    open_edges=edges,strict_rank=rank,only_cyclic_state=23,band_actual18_read_path=path,
    band_channel=dict(source_port='F_j.Nout_only',target_port='G_(j-1).Sin_only',length=19),
    all_index_disjoint_roles=roles,
    warning='Actual outer readers F/G, complete full-period cursor and field are open. A cyclic interface graph is not an attained front.'),indent=2)+'\n')
print('PASS3844 nodes->24 states;294 complete pair patches->18 edges; only cyclic state23; exact19-edge lower-port channel')
