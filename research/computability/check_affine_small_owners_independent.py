#!/usr/bin/env python3
"""No-import replay of the two small ownership inventories used at cone equality."""
from itertools import product
from pathlib import Path
import json

DIR = [1j, 1, -1j, -1]

def path(word, heading):
    p = 0j
    h = DIR[heading]
    events = []
    last = {}
    first = {}
    for c in word:
        if last.get(p) == c:
            return None
        last[p] = c
        first.setdefault(p, c)
        events.append((p, c))
        h *= -1j if c == 'R' else 1j
        p += h
    return p, first, events

def inventory(k, a, theta):
    result = []
    for hc in range(4):
        for c in 'RL':
            target = a * DIR[(hc + (1 if c == 'R' else -1)) % 4]
            for hf in range(4):
                if hf % 2 != ((k % 2) * hc + theta) % 2:
                    continue
                for word in map(''.join, product('RL', repeat=k)):
                    z = path(word, hf)
                    if z is not None and z[0] == target:
                        result.append((hc, c, hf, word, z[1]))
    return result

out = []
for k, a, theta in [(4, 2, 0), (7, 3, 1)]:
    inv = inventory(k, a, theta)
    targets = []
    for hc, c, hf, word, first in inv:
        if hc != 0 or c != 'R':
            continue
        witnesses = []
        for z, read in first.items():
            if read != 'L':
                continue
            owners = set()
            for oc, turn, of, ow, ofirst in inv:
                for v in ofirst:
                    delta = z - v
                    dx, dy = int(delta.real), int(delta.imag)
                    if dx % a or dy % a:
                        continue
                    x, y = dx // a, dy // a
                    if (x + y + oc) % 2:
                        continue
                    owners.add((x, y))
            if owners and all(y >= 0 for x, y in owners):
                witnesses.append(dict(cell=[int(z.real), int(z.imag)],
                                      owners=sorted(owners)))
        assert witnesses, (k, a, theta, hf, word)
        targets.append(dict(word=word, fine_heading=hf,
                            forward_witnesses=witnesses))
    assert targets
    out.append(dict(k=k, scale=a, theta=theta, oriented_records=len(inv),
                    target_count=len(targets), targets=targets,
                    status='PASS all target images have forward first-L witness'))

assert [(r['oriented_records'], r['target_count']) for r in out] == [(32, 4), (96, 12)]
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
