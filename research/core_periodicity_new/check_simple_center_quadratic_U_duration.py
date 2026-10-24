"""Finite arithmetic/dependency controls for the analytic quadratic-U corollary.

This checker does not replace the analytic use of the two signed theorems.
It reconstructs atom lengths, marker prefixes, the exact ceiling identity,
center-count arithmetic and the fixed-m recurrence inversion.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
TOP = ROOT.parent
GP = ROOT / 'chronology_dcuv/literal_residual_geometry.json'
HP = TOP / 'word_stabilization/dcuv_epoch_reset_bound_manifest.json'
SP = ROOT / 'U_entry_simplicity_frozen_20261023_1616/manifest.json'
G = json.loads(GP.read_text())['geometry']
IDS = (0, 1, 4, 5, 6, 7, 8, 9)
HS = json.loads(HP.read_text())
assert HS['status'] == 'SIGNED'
assert hashlib.sha256(SP.read_bytes()).hexdigest() == '127a00884b4a06af35a807ab76f6f6499b9427d56350a931c03cc0e8de65524d'
marker = G[0]['marker']
assert len(marker) == 11
assert all(G[a]['word'].startswith(marker) for a in IDS if a != 0)  # D is a 10-step marker prefix.
assert (G[0]['word'] + marker).startswith(marker)
D, V, U = (G[a]['word'] for a in (0, 4, 7))
C = G[1]['word'][len(D):]
assert all(G[a]['word'] == G[b]['word'] + C * c
           for a, b, c in ((0,0,0),(1,0,1),(4,4,0),(5,4,1),(6,4,2),(7,7,0),(8,7,1),(9,7,2)))
lengths = {'D': len(D), 'V': len(V), 'U': len(U), 'C': len(C)}
assert lengths == {'D': 10, 'V': 18, 'U': 28, 'C': 15}

def radius(m, u):
    B = 57 + 38 * (m - 5) + 60 * u
    return (2 * B + 4) // 5

def duration(m, u):
    R = radius(m, u)
    t = (2 * R + 1) ** 2 // 3
    return 20 * R * (t + 1) + 28 * t

controls = []
for m in range(5, 101):
    R0, F0 = radius(m, 0), duration(m, 0)
    for u in range(101):
        R = radius(m, u)
        assert R == R0 + 24 * u
        assert 28 * (2 * R + 2) ** 2 == 112 * (R0 + 24 * u + 1) ** 2
    if m in (5, 10, 20, 50, 100):
        controls.append({'m': m, 'R0': R0, 'F0': F0,
                         'quadratic_bound_coefficients_in_u': [112 * 24 ** 2, 224 * 24 * (R0 + 1), F0 + 112 * (R0 + 1) ** 2]})
# Half-integer centers represented by odd doubled coordinates; four heading
# shifts cannot leave the counted square for any admissible integer head.
for R in range(10):
    centers = {(2*x+dx, 2*y+dy) for x in range(-R, R+1)
               for y in range(-R, R+1) for dx, dy in ((-1,-1),(-1,1),(1,1),(1,-1))}
    assert len(centers) == (2 * R + 2) ** 2

result = {
    'status': 'AUTHOR_ANALYTIC_COROLLARY_WITH_ARITHMETIC_CONTROLS',
    'scope': 'Complete recurrent-eight factors, entry mass m >= 5, u U-family packets. Raw duration only; actual M11 adds 11.',
    'bound': 'L <= F(m,0) + 112 (R(m,0) + 24u + 1)^2; if u=0 use F(m,0).',
    'not_claimed': 'No U upper bound, component budget, record closure, unrestricted ant parsing or capture.',
    'atomic_lengths': lengths, 'arithmetic_tests': 96 * 101,
    'center_square_controls': 10, 'examples': controls,
    'dependencies': {str(p.relative_to(TOP)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (GP, HP, SP, Path(__file__).resolve())}}
(ROOT / 'chronology_dcuv/simple_center_quadratic_U_duration.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
