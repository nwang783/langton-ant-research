"""Independent exact normalization audit for the clean transverse model.

No simulation bound supplies the all-separation quantifier. Each possible
read/rail intersection is solved as a pair of integer linear equations.
"""
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path('/workspace/shared/langton')
DATA = json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())
WORD = DATA['word']
assert len(WORD) == 104 and set(WORD) <= {'R', 'L'}
D = tuple(DATA['drift'])
H = DATA['heading']
assert D == (-2, -2) and H == 3
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

def add(p, q): return (p[0]+q[0], p[1]+q[1])
def sub(p, q): return (p[0]-q[0], p[1]-q[1])
def mul(k, p): return (k*p[0], k*p[1])
def det(p, q): return p[0]*q[1]-p[1]*q[0]
def rot(p, r):
    for _ in range(r): p = (p[1], -p[0])
    return p

q = (0, 0)
h = H
reads = []
for letter in WORD:
    reads.append(q)
    h = (h + (1 if letter == 'R' else -1)) % 4
    q = add(q, DIR[h])
assert (q, h) == (D, H)

def line_key(q, d):
    assert abs(d[0]) == abs(d[1]) == 2
    k = (q[0] - q[0] % 2) // d[0]
    return sub(q, mul(k, d))

def lines(r, offset):
    d = rot(D, r)
    odd = set()
    for q in reads:
        odd.symmetric_difference_update({line_key(add(rot(q, r), offset), d)})
    return odd, d

# Exact XOR-event normal form for the incoming rays, directed by E=-D.
E = mul(-1, D)
def incoming_events(shift=(0, 0), add_period=False):
    events = defaultdict(set)
    def boundary(q):
        key = line_key(q, E)
        k = (q[0]-key[0]) // E[0]
        events[key].symmetric_difference_update({k})
    for q in reads:
        boundary(add(sub(q, D), shift))
        if add_period:
            # A singleton at q is a ray starting at q XOR one at q+E.
            boundary(q)
            boundary(add(q, E))
    return {k: sorted(v) for k, v in events.items() if v}

assert incoming_events(add_period=True) == incoming_events(shift=D)

rows = json.loads((ROOT/'scattering/transverse/crossings_discovery.json').read_text())
assert len(rows) == 16
row_map = {(r['rotation'], r['a'], r['s']): r for r in rows}
assert len(row_map) == 16
result = []
for r in (1, 3):
    v = rot(D, r)
    assert abs(det(D, v)) == 8
    for a in (0, 1):
        for s in range(4):
            rails, _ = lines(r, (a, s-a))
            shifted, _ = lines(r, add((a, s-a), D))
            next_n, _ = lines(r, (a, s-a-4))
            assert shifted == next_n
            intersections = []
            for i, q in enumerate(reads):
                phase_epochs = set()
                for b in rails:
                    delta = sub(b, q)
                    denominator = det(D, v)
                    nk, nj = det(delta, v), det(delta, D)
                    if nk % denominator or nj % denominator:
                        continue
                    k, j = nk//denominator, nj//denominator
                    assert add(q, mul(k, D)) == add(b, mul(j, v))
                    # Distinct orbit representatives cannot double-count a cell.
                    assert k not in phase_epochs
                    phase_epochs.add(k)
                    intersections.append((104*k+i, k, i))
            intersections.sort()
            assert intersections
            constant, epoch, phase = intersections[0]
            assert epoch == min(t[1] for t in intersections)
            n_min = max(0, -epoch)
            assert n_min <= 5
            row = row_map[r, a, s]
            assert row['t0'] == 104*20 + constant
            assert row['capture'] == row['t0'] + row['recovery']
            result.append(dict(rotation=r, a=a, s=s,
                               first_contact_constant=constant,
                               first_contact_phase=phase,
                               minimum_separation=n_min,
                               intersection_count=len(intersections),
                               capture_constant=row['capture']-104*20,
                               sector='same' if s % 2 else 'opposite'))

out = dict(status='PASS: exact all-separation normalization for n>=5',
           incoming_period_field_translation=True,
           offset_lattice_index=8,
           scope='Canonical infinite incoming past XOR one bilateral settled perpendicular wake',
           records=result)
(ROOT/'audits/crossing_normalization_audit.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
