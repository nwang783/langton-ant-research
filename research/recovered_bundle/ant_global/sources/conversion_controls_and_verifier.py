"""Independent physical-position verifier for converter words and controls.

For a representative cell, a one-period event at position q+ell*d occurs at
physical time i-ell*P. Sorting those times checks every visit in the whole
two-sided repeated trajectory, not just a finite repetition window.
"""
import collections
import json
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / 'sources'
DX, DY = (0, 1, 0, -1), (1, 0, -1, 0)

def trace(word, start, h):
    x, y = start
    events = []
    for i, turn in enumerate(word):
        events.append((x, y, h, turn == 'L'))
        h = (h + (3 if turn == 'L' else 1)) % 4
        x, y = x + DX[h], y + DY[h]
    return events, (x, y), h

def verify(word, start, h, U, V):
    U, V = set(map(tuple, U)), set(map(tuple, V))
    events, end, end_h = trace(word, start, h)
    assert end == (start[0] + 2, start[1] + 2)
    assert end_h == h
    assert (h - sum(start)) % 2 == 1
    ranks = collections.defaultdict(list)
    for i, (x, y, _, black) in enumerate(events):
        r = x % 2
        ell = (x - r) // 2
        ranks[x - y, r].append((i - ell * len(word), black))
    final = set(U)
    for key, visits in ranks.items():
        for k, (_, black) in enumerate(sorted(visits)):
            assert black == ((key in U) ^ bool(k % 2)), (key, visits, U)
        if len(visits) % 2:
            final.symmetric_difference_update([key])
    assert final == V
    return {'period': len(word), 'displacement': [2, 2],
            'input_mass': len(U), 'output_mass': len(V),
            'classes_read': len(ranks)}

def control(uid, word, start, h, black_background=False, special_U=None):
    events, _, _ = trace(word, start, h)
    counts = collections.Counter(x - y for x, y, _, _ in events)
    classes = collections.Counter((x - y, x % 2) for x, y, _, _ in events)
    lo, hi = min(counts), max(counts)
    U = ({(s, r) for s in range(lo, hi + 1) for r in range(2)}
         if black_background else set(special_U or []))
    V = U ^ {c for c, n in classes.items() if n % 2}
    verify(word, start, h, U, V)
    return {'id': uid, 'bottom': lo, 'top': hi, 'period': len(word),
            'U': sorted(U), 'V': sorted(V),
            'row_counts': [counts[s] for s in range(lo, hi + 1)]}

data = json.loads((BASE / 'root/standard.json').read_text())
w = data['word']
controls = [
    control(-1, w, (0, 0), (data['heading'] + 2) % 4),
    control(-2, w.translate(str.maketrans('LR', 'RL')), (1, 0), 0, True),
    control(-3, 'RLRL', (1, 0), 0, special_U={(2, 0), (2, 1)}),
]
lines = []
for c in controls:
    U, V = set(map(tuple, c['U'])), set(map(tuple, c['V']))
    lines.append(f"{c['id']} {c['bottom']} {c['top']} {c['period']}")
    for s, n in zip(range(c['bottom'], c['top'] + 1), c['row_counts']):
        lines.append(' '.join(map(str, [int((s, 0) in U), int((s, 1) in U),
                                       int((s, 0) in V), int((s, 1) in V), n])))
(SRC / 'conversion_controls.txt').write_text('\n'.join(lines) + '\n')
(SRC / 'conversion_controls.json').write_text(json.dumps(controls, indent=2) + '\n')
run = subprocess.run([str(SRC / 'conversion_chronology'), str(SRC / 'conversion_controls.txt'),
                      '45', '1'], check=True, capture_output=True, text=True)
(SRC / 'conversion_controls_results.txt').write_text(run.stdout)
by_id = {c['id']: c for c in controls}
report = []
found = set()
for line in run.stdout.splitlines():
    parts = line.split()
    if parts[0] != 'SOLUTION':
        continue
    uid, x, y, h = map(int, parts[1:5])
    c = by_id[uid]
    report.append({'id': uid, **verify(parts[5], (x, y), h, c['U'], c['V'])})
    found.add(uid)
assert found == set(by_id)
(SRC / 'conversion_controls_audit.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report))
