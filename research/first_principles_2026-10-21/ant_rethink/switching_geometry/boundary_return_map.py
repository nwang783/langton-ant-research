"""Check whether frozen boundary connectivity determines true first exit.

Enumerates all colors in a finite rectangle. The outside is an exit condition,
not an artificial dynamics. Both walks use the standard rule inside the box.
"""
import json
from itertools import product
from pathlib import Path

D = ((1, 0), (0, -1), (-1, 0), (0, 1))


def move(p, h, b):
    nh = (h + (-1 if p in b else 1)) % 4
    return (p[0] + D[nh][0], p[1] + D[nh][1]), nh


def frozen_exit(box, b, state):
    p, h = state
    seen = set()
    while p in box:
        assert (p, h) not in seen
        seen.add((p, h))
        p, h = move(p, h, b)
    return p, h


def true_exit(box, b, state):
    b = set(b)
    p, h = state
    seen = set()
    word = ""
    while p in box:
        key = (frozenset(b), p, h)
        assert key not in seen
        seen.add(key)
        old_p = p
        black = p in b
        p, h = move(p, h, b)
        if black:
            b.remove(old_p)
        else:
            b.add(old_p)
        word += "L" if black else "R"
    return (p, h), b, word


def encode(state):
    return [list(state[0]), state[1]]


def main():
    box = set(product(range(3), repeat=2))
    cells = sorted(box)
    entries = []
    for p in cells:
        for h in range(4):
            if (h % 2 == 1) != ((p[0] + p[1]) % 2 == 0):
                continue
            previous = (p[0] - D[h][0], p[1] - D[h][1])
            if previous not in box:
                entries.append((p, h))
    groups = {}
    first = None
    for mask in range(1 << len(cells)):
        b = {p for j, p in enumerate(cells) if mask & (1 << j)}
        pairing = tuple(frozen_exit(box, b, entry) for entry in entries)
        results = [true_exit(box, b, entry) for entry in entries]
        outputs = tuple(r[0] for r in results)
        for old_b, old_outputs, old_results in groups.get(pairing, []):
            if old_outputs != outputs:
                j = next(j for j in range(len(entries)) if old_outputs[j] != outputs[j])
                first = {
                    "box": [0, 2, 0, 2],
                    "entries": [encode(e) for e in entries],
                    "same_frozen_exits": [encode(e) for e in pairing],
                    "entry": encode(entries[j]),
                    "board_1": sorted(old_b),
                    "board_2": sorted(b),
                    "true_exit_1": encode(old_outputs[j]),
                    "true_exit_2": encode(outputs[j]),
                    "word_1": old_results[j][2],
                    "word_2": results[j][2],
                    "final_black_1": sorted(old_results[j][1]),
                    "final_black_2": sorted(results[j][1]),
                }
                break
        if first:
            break
        groups.setdefault(pairing, []).append((b, outputs, results))
    output = {"counterexample": first, "pairing_groups_seen": len(groups)}
    Path(__file__).with_suffix(".json").write_text(json.dumps(output, indent=2))
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
