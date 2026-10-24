"""Exact finite counterchecks of richer frozen boundary summaries."""
import json
from itertools import product
from pathlib import Path
from boundary_return_map import D, move, true_exit, encode


def admissible(p, h):
    return (h % 2 == 1) == ((p[0] + p[1]) % 2 == 0)


def summarize(box, entries, b):
    covered = set()
    exits, lengths = [], []
    for start in entries:
        p, h = start
        n = 0
        while p in box:
            assert (p, h) not in covered
            covered.add((p, h))
            p, h = move(p, h, b)
            n += 1
        exits.append((p, h))
        lengths.append(n)
    remaining = {(p, h) for p in box for h in range(4) if admissible(p, h)} - covered
    cycles = []
    while remaining:
        start = min(remaining)
        p, h = start
        n = 0
        while True:
            assert (p, h) in remaining
            remaining.remove((p, h))
            p, h = move(p, h, b)
            n += 1
            if (p, h) == start:
                break
        cycles.append(n)
    return tuple(exits), tuple(lengths), tuple(sorted(cycles))


def main():
    box = set(product(range(3), repeat=2))
    cells = sorted(box)
    entries = [(p, h) for p in cells for h in range(4) if admissible(p, h)
               and (p[0]-D[h][0], p[1]-D[h][1]) not in box]
    levels = {"pairing_loop_count": {}, "pairing_loop_lengths": {},
              "pairing_loop_lengths_mass": {}, "all_lengths_mass": {}}
    witnesses = {}
    for mask in range(1 << len(cells)):
        b = {p for j, p in enumerate(cells) if mask & (1 << j)}
        pairing, lengths, cycles = summarize(box, entries, b)
        results = [true_exit(box, b, entry) for entry in entries]
        outputs = tuple(r[0] for r in results)
        keys = {"pairing_loop_count": (pairing, len(cycles)),
                "pairing_loop_lengths": (pairing, cycles),
                "pairing_loop_lengths_mass": (pairing, cycles, len(b)),
                "all_lengths_mass": (pairing, lengths, cycles, len(b))}
        for level, key in keys.items():
            previous = levels[level].get(key)
            if previous is None:
                levels[level][key] = (b, outputs, results)
                continue
            old_b, old_outputs, old_results = previous
            if old_outputs != outputs and level not in witnesses:
                j = next(j for j in range(len(entries)) if old_outputs[j] != outputs[j])
                witnesses[level] = {
                    "entry": encode(entries[j]), "board_1": sorted(old_b),
                    "board_2": sorted(b), "true_exit_1": encode(old_outputs[j]),
                    "true_exit_2": encode(outputs[j]), "word_1": old_results[j][2],
                    "word_2": results[j][2],
                    "summary_1": summarize(box, entries, old_b),
                    "summary_2": (pairing, lengths, cycles),
                }
    output = {"box": [0, 2, 0, 2], "all_boards_checked": 1 << len(cells),
              "entries": [encode(e) for e in entries],
              "group_counts": {k: len(v) for k, v in levels.items()},
              "counterexamples": witnesses}
    Path(__file__).with_suffix(".json").write_text(json.dumps(output, indent=2))
    print(json.dumps({k: v for k, v in output.items() if k != "counterexamples"}))
    for k, w in witnesses.items():
        print(json.dumps({"level": k, **{a: b for a, b in w.items() if not a.startswith("summary")}}))


if __name__ == "__main__":
    main()
