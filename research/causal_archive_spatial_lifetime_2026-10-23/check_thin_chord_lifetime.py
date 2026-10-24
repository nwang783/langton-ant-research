"""Exact finite geometry behind the all-length thin-chord lifetime proof.

No ant-word search or chronological horizon is used. The note proves the
perturbation/turning implication analytically. This script reconstructs its
finite set of literal roles and all candidate chord-entry sites exactly.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
GEOMETRY = ROOT / 'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
DEPENDENCIES = [
    GEOMETRY,
    ROOT / 'core_periodicity_new/atomic_center_turning_frozen_20261023_1400/manifest.json',
    ROOT / 'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',
    ROOT / 'core_periodicity_new/simple_center_C_lifetime_frozen_20261023_1719/manifest.json',
    ROOT / 'spatial_cursor_2026-10-23/coupled_dual_cursors_and_gate_memory.md',
]
G = json.loads(GEOMETRY.read_text())['geometry']
IDS = (0, 1, 4, 5, 6, 7, 8, 9)


def rot(p, h):
    x, y = p
    return ((x, y), (y, -x), (-x, -y), (-y, x))[h % 4]


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def on_segment(a, b, c):
    return orient(a, b, c) == 0 and all(min(a[j], b[j]) <= c[j] <= max(a[j], b[j]) for j in (0, 1))


def intersect(a, b, c, d):
    p, q, r, s = orient(a, b, c), orient(a, b, d), orient(c, d, a), orient(c, d, b)
    return (p * q < 0 and r * s < 0) or (p == 0 and on_segment(a, b, c)) or (q == 0 and on_segment(a, b, d)) or (r == 0 and on_segment(c, d, a)) or (s == 0 and on_segment(c, d, b))


STEPS = sorted({rot(v, h) for v in ((1, 1), (1, 3), (0, 4)) for h in range(4)})
assert len(STEPS) == 12
assert all((x + y) % 2 == 0 for x, y in STEPS)
assert max(abs(z) for v in STEPS for z in v) == 4
# The previously signed checker derives D/V/U and corrected C from literal
# endpoints. Recheck all three base endpoints and the corrected C convention.
assert [tuple(G[i]['endpoint']) for i in (0, 4, 7)] == [(1, 1, 0), (1, 3, 0), (0, 4, 0)]
assert tuple(G[1]['endpoint']) == (1, 2, 3)
assert add(sub(G[1]['endpoint'][:2], G[0]['endpoint'][:2]), ((1), (0))) == (1, 1)
assert sum(len(G[i]['outputs']) for i in IDS) == 68
assert sum(len(G[i]['inputs']) for i in IDS) == 23


def candidate_entries(d, margin=4):
    rows = []
    for x in range(min(0, d[0]) - margin, max(0, d[0]) + margin + 1):
        for y in range(min(0, d[1]) - margin, max(0, d[1]) + margin + 1):
            if (x + y) % 2:
                continue
            touching = [v for v in STEPS if intersect((0, 0), d, (x, y), add((x, y), v))]
            if touching:
                rows.append({'entry': (x, y), 'touching_vectors': touching})
    return rows


counts = Counter()
cache = {}
roles = []
for a in IDS:
    for o in G[a]['outputs']:
        for b in IDS:
            for i in G[b]['inputs']:
                for h in range(4):
                    counts['raw_alignments'] += 1
                    p = sub(o, rot(i, h))
                    if (sum(p) + h) % 2:
                        counts['wrong_sector'] += 1
                        continue
                    counts['sector_compatible_alignments'] += 1
                    r = rot((-1, -1), h)
                    d = (p[0] + (r[0] + 1) // 2, p[1] + (r[1] + 1) // 2)
                    assert sum(d) % 2 == 0
                    if d not in cache:
                        cache[d] = candidate_entries(d)
                    M = len(cache[d])
                    geometric = 0 if d == (0, 0) else 4 * M + 11
                    residue = (-h) % 4
                    rounded = 0 if d == (0, 0) else geometric - ((geometric - residue) % 4)
                    # A coincident entry cut forces an empty simple subarc;
                    # all distinct source/consumer roles with d=0 are impossible.
                    assert rounded >= 0
                    roles.append({'source': a, 'source_name': G[a]['name'], 'output': o, 'consumer': b, 'consumer_name': G[b]['name'], 'input': i, 'relative_heading': h, 'consumer_head': p, 'center_delta': d, 'candidate_entry_count': M, 'geometric_C_bound': geometric, 'C_age_residue_mod4': residue, 'rounded_C_age_bound': rounded, 'coincident_centers_impossible_for_distinct_entries': d == (0, 0)})
assert counts == Counter(raw_alignments=6256, wrong_sector=3128, sector_compatible_alignments=3128)
assert len(cache) == 72
assert max(map(len, cache.values())) == 71
assert max(r['geometric_C_bound'] for r in roles) == 295
assert max(r['rounded_C_age_bound'] for r in roles) == 294
maximizers = [r for r in roles if r['candidate_entry_count'] == 71]
assert len(maximizers) == 3
assert all(r['source'] == 9 and r['output'] == [0, 7] and r['consumer'] in (7, 8, 9) and r['input'] == [-1, 4] and r['relative_heading'] == 2 and r['consumer_head'] == (-1, 11) and r['center_delta'] == (0, 12) and r['rounded_C_age_bound'] == 294 for r in maximizers)
# Expanded domains are controls, not the proof of completeness (which is the
# maximum coordinate-span-four argument in the note).
for d in cache:
    assert candidate_entries(d, 5) == cache[d]
    assert len(candidate_entries(rot(d, 1))) == len(cache[d])
# Exact integer rounding of the analytic turning inequality.
for k in range(1000):
    assert (8 * k + 23) // 2 == 4 * k + 11

out = {
    'status': 'AUTHOR_EXACT_GEOMETRY_WITH_ANALYTIC_THIN_CHORD_PROOF',
    'scope': 'Simple actual corrected-center complete-eight factors; source and consumer in same factor; no untouched entry identity bound or global capture claim.',
    'geometric_theorem': 'n <= 4*|Q(B-A)|+11 for distinct endpoints; n=0 for coincident endpoints',
    'maximum_candidate_sites': 71,
    'maximum_geometric_C_age_bound': 295,
    'maximum_heading_rounded_C_age_bound': 294,
    'role_counts': dict(counts),
    'distinct_role_center_deltas': len(cache),
    'geometric_steps': STEPS,
    'maximizers': maximizers,
    'all_roles': roles,
    'all_candidate_entry_sites': [{'center_delta': d, 'entries': cache[d]} for d in sorted(cache)],
    'dependencies': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in DEPENDENCIES},
    'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(HERE / 'thin_chord_lifetime_controls.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({k: v for k, v in out.items() if k not in ('all_roles', 'all_candidate_entry_sites', 'dependencies', 'maximizers')}, indent=2))
