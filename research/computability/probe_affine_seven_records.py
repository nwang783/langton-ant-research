#!/usr/bin/env python3
"""Small complete local abstraction, NOT an infinite inflation search.
Allows arbitrary initial colors except the fresh record row in the local
seven-letter image inventory. Refinement tests retain literal alternation.
"""
from itertools import product
from pathlib import Path
import json

NODES = ['RRLRLLRL', 'RRLLRRLL']

def trace(w, p=0j, h=1j):
    out = []
    for c in w:
        out.append((p, c))
        h *= -1j if c == 'R' else 1j
        p += h
    return out, p, h

def append(events, last, pristine=False):
    new = last.copy()
    for p, c in events:
        if new.get(p) == c:
            return None
        if pristine and p not in new and p.imag >= 0 and c == 'L':
            return None
        new[p] = c
    return new

words = []
for w in map(''.join, product('RL', repeat=7)):
    if append(trace(w)[0], {}) is not None:
        words.append(w)
local = []
for w in words:
    ev, end, h = trace(w, h=1)
    if end == 3 and append(ev, {-1: 'R'}, pristine=True) is not None:
        local.append(w)
assert sorted('R' + w for w in local) == sorted(NODES)

edges = []
for u in NODES:
    ev, end, _ = trace(u)
    coarse = [p for p, c in ev] + [end]
    for v in NODES:
        level = [(1, {0j: 'R'})]
        counts = [1]
        conflicts = 0
        for n in range(len(u)):
            nxt = []
            for h, last in level:
                for w in ([v[1:]] if n == 0 else words):
                    events, p, hh = trace(w, 1 + 3 * coarse[n], h)
                    if p != 1 + 3 * coarse[n + 1]:
                        continue
                    new = append(events, last)
                    if new is None:
                        conflicts += 1
                    else:
                        nxt.append((hh, new))
            level = nxt
            counts.append(len(level))
        edges.append(dict(coarse=u, fine_record=v, levels=counts,
                          conflicts=conflicts, survivors=len(level)))

out = dict(status='Complete finite overapproximation; all edges survive, no exclusion',
           feasible_seven_words=len(words), local_east_images=local,
           preceding_record_read='R', fine_aligned_origin=[1, 0],
           fine_aligned_heading='E', coarse_heading='N',
           fine_read_length=1 + 7 * len(NODES[0]), edges=edges)
assert all(e['survivors'] for e in edges)
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
