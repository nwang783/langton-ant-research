#!/usr/bin/env python3
"""Finite search of physical cycles in the no-adjacent-J10 macro graph."""
from pathlib import Path
from collections import defaultdict, Counter
import json
import math
import sys

BASE = Path(__file__).resolve().parent
OTHER = BASE.parent / "factor_language"
DATA = json.loads((OTHER / "no_pair_port_words.json").read_text())
WORDS = DATA["words"]
NAMES = dict(zip(WORDS, "CVUQB"))
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
ADJ = defaultdict(list)
for u, v, w in DATA["edges"]:
    ADJ[u].append((v, w))


def egcd(a, b):
    if b == 0:
        return (abs(a), 1 if a >= 0 else -1, 0)
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def periodic_check(word):
    p = (0, 0)
    h = 0
    phases = []
    for i, c in enumerate(word):
        phases.append((p[0], p[1], i, c))
        h = (h + (1 if c == "R" else -1)) % 4
        dx, dy = DIRS[h]
        p = p[0] + dx, p[1] + dy
    if h:
        return {"reason": "nonrestored heading"}
    if p == (0, 0):
        return {"reason": "zero drift"}
    dx, dy = p
    g, a, b = egcd(dx, dy)
    groups = defaultdict(list)
    for x, y, i, c in phases:
        longitudinal = a * x + b * y
        residue = longitudinal % g
        key = ((x * dy - y * dx) // g, residue)
        epoch = (longitudinal - residue) // g
        groups[key].append((epoch, i, c))
    rays = 0
    for visits in groups.values():
        visits.sort(key=lambda item: (-item[0], item[1]))
        if any(visits[j][2] == visits[j + 1][2] for j in range(len(visits) - 1)):
            return {"reason": "inconsistent recurring reads"}
        rays += visits[0][2] == "L"
    return {"period": len(word), "drift": [dx, dy], "required_black_rays": rays}


def main(depth):
    stats = Counter()
    results = {}
    last_read = {}
    current_letters = []
    path = []

    def visit(start, port, p, h):
        stats["nodes"] += 1
        if path and port == start:
            # The shortest cyclic rotation is a canonical alphabet word.
            seq = "".join(path)
            canon = min(seq[j:] + seq[:j] for j in range(len(seq)))
            if canon not in results:
                result = periodic_check("".join(current_letters))
                results[canon] = result
                stats[result.get("reason", "consistent periodic word")] += 1
                if result.get("required_black_rays") == 0:
                    print("ZERO RAY CANDIDATE", seq, result, flush=True)
        if len(path) == depth:
            return
        for nxt, w in ADJ[port]:
            if nxt < start:
                continue
            q, hh = p, h
            changes = []
            valid = True
            for c in w:
                old = last_read.get(q)
                if old == c:
                    valid = False
                    break
                changes.append((q, old))
                last_read[q] = c
                hh = (hh + (1 if c == "R" else -1)) % 4
                dx, dy = DIRS[hh]
                q = q[0] + dx, q[1] + dy
            if valid:
                path.append(NAMES[w])
                current_letters.append(w)
                visit(start, nxt, q, hh)
                current_letters.pop()
                path.pop()
            else:
                stats["infeasible extensions"] += 1
            for q, old in reversed(changes):
                if old is None:
                    del last_read[q]
                else:
                    last_read[q] = old

    for start in sorted(ADJ):
        visit(start, start, (0, 0), 0)
    consistent = [dict(macros=k, **v) for k, v in results.items() if "required_black_rays" in v]
    consistent.sort(key=lambda x: (x["required_black_rays"], x["period"], x["macros"]))
    output = {
        "macro_depth_limit": depth,
        "statistics": dict(stats),
        "consistent_cycles": consistent,
        "scope": "Finite macro-depth search, not an all-period exclusion",
    }
    (BASE / f"macro_cycles_{depth}.json").write_text(json.dumps(output, indent=2))
    print(json.dumps({**output, "consistent_cycles": consistent[:30]}, indent=2))


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 12)
