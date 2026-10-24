"""Literal local even-dual topology only, not an incidence embedding.

Every physical cell is one diagonal edge on the active-center checkerboard.
This finite table is derived directly from the signed literal I/O masks.
"""
from pathlib import Path
from collections import Counter
import json, hashlib

ROOT = Path(__file__).resolve().parent
GP = ROOT / 'chronology_dcuv/literal_residual_geometry.json'
AP = ROOT / 'active_center_edge_walk_frozen_20261023_1739/manifest.json'
J = json.loads(GP.read_text())
G = J['geometry']
IDS = (0, 1, 4, 5, 6, 7, 8, 9)
K = set(map(tuple, J['core']))

def rot(q, h):
    x, y = q
    return ((x, y), (y, -x), (-x, -y), (-y, x))[h % 4]

def edge(q):
    x, y = q
    a, b = (1, 1) if (x + y) % 2 == 0 else (1, -1)
    return ((2*x-a, 2*y-b), (2*x+a, 2*y+b))

def graph(cells):
    cells = set(map(tuple, cells))
    E = {q: edge(q) for q in cells}
    V = {v for e in E.values() for v in e}
    seen, components = set(), []
    for v in sorted(V):
        if v in seen:
            continue
        seen.add(v)
        todo, component = [v], {v}
        while todo:
            v = todo.pop()
            for a, b in E.values():
                if a == v and b not in seen:
                    seen.add(b); component.add(b); todo.append(b)
                if b == v and a not in seen:
                    seen.add(a); component.add(a); todo.append(a)
        components.append(sorted(component))
    # The leaf-pruned edge core is empty for a tree and is the unique cycle
    # for the unicyclic output graphs occurring in this exact table.
    core = set(cells)
    while True:
        degrees = Counter(v for q in core for v in E[q])
        leaves = {q for q in core if any(degrees[v] == 1 for v in E[q])}
        if not leaves:
            break
        core -= leaves
    return dict(cells=sorted(cells), edges_twice=[dict(cell=q, endpoints=E[q]) for q in sorted(E)],
                vertices=len(V), edges=len(E), components=components,
                component_count=len(components), cycle_rank=len(E)-len(V)+len(components),
                leaf_pruned_cycle_cells=sorted(core))

rows = []
for a in IDS:
    g = G[a]
    I, O = graph(g['inputs']), graph(g['outputs'])
    assert I['component_count'] == O['component_count'] == 1
    assert I['cycle_rank'] == 0
    u = a in (7, 8, 9)
    assert O['cycle_rank'] == int(u)
    assert O['leaf_pruned_cycle_cells'] == ([(1,0),(1,1),(2,0),(2,1)] if u else [])
    px, py, h = g['endpoint']
    exit_core = {(px+rot(q,h)[0], py+rot(q,h)[1]) for q in K}
    before, after = graph(K | set(map(tuple, g['inputs']))), graph(exit_core | set(map(tuple, g['outputs'])))
    rows.append(dict(packet=a, name=g['name'], inputs=I, outputs=O,
                     local_core_and_inputs=before, local_exit_core_and_outputs=after))

out = dict(status='AUTHOR_EXACT_LOCAL_EVEN_DUAL_TOPOLOGY',
           scope='Literal finite packet input/output edge graphs only. No historical incidence connectivity, maintained tangle, cycle budget, or U-merger claim.',
           coordinate_scale=2, sector=0,
           theorem='Every full-packet input mask is a tree. Every output mask is connected; D/DC/V/VC/VCC outputs are trees, and U/UC/UCC outputs are unicyclic with the same four-edge cycle.',
           rows=rows,
           dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (GP, AP, Path(__file__).resolve())})
(ROOT/'chronology_dcuv/even_dual_packet_topology.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps([dict(name=r['name'], input_vertices=r['inputs']['vertices'], input_edges=r['inputs']['edges'], output_vertices=r['outputs']['vertices'], output_edges=r['outputs']['edges'], output_cycle_rank=r['outputs']['cycle_rank']) for r in rows], indent=2))
