#!/usr/bin/env python3
"""Exact finite calculation for a fixed supplied P104 word.

This verifies the 22 first-read phase claim in the compactness note. It is
not a search over seeds and does not prove the highway conjecture.
"""
import json
from collections import defaultdict
from pathlib import Path

WORD = ("RRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRRLLLLRLR")
SOURCE = ("https://github.com/kehao95/langtons-ant-core/blob/"
          "22e0c9edcc566a4c2f7a9bf92f5cd05c19199617/"
          "wake_synthesis/PROOF.md")
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def main():
    period = len(WORD)
    assert period == 104
    x = y = h = 0
    positions = []
    for letter in WORD:
        positions.append((x, y, h))
        h = (h + (1 if letter == "R" else -1)) % 4
        dx, dy = DIRECTIONS[h]
        x += dx
        y += dy
    assert (x, y, h) == (2, 2, 0)
    drift = (x, y)

    classes = defaultdict(list)
    for i, (x, y, h) in enumerate(positions):
        residue = x % 2
        level = (x - residue) // 2
        key = (x - y, residue)
        classes[key].append((i - period * level, i))

    fresh = []
    odd = 0
    for key, events in classes.items():
        events.sort()
        letters = "".join(WORD[i] for _, i in events)
        assert letters == "".join("R" if r % 2 == 0 else "L"
                                  for r in range(len(events)))
        fresh.append(events[0][1])
        odd += len(events) % 2
    assert len(classes) == 22 and odd == 12

    # Independent literal same-cell test in the two-sided repeated path.
    # For each phase pair, at most one integer epoch can make cells equal.
    literal_fresh = []
    for i, (xi, yi, _) in enumerate(positions):
        earlier = False
        for j, (xj, yj, _) in enumerate(positions):
            dx, dy = xi - xj, yi - yj
            if dx % 2 or dy % 2 or dx != dy:
                continue
            epoch = dx // 2
            if j + period * epoch < i:
                earlier = True
                break
        if not earlier:
            literal_fresh.append(i)
    assert sorted(fresh) == literal_fresh
    assert all(WORD[i] == "R" for i in fresh)

    # Historical marker eligibility and sector are phase dependent.
    phases = [{"phase": i, "position": positions[i][:2],
               "heading": "NESW"[positions[i][2]], "turn": WORD[i],
               "centered_sector": (-1) ** positions[i][2]}
              for i in sorted(fresh)]
    result = {"period": period, "drift": drift, "word": WORD,
              "source": SOURCE, "visited_drift_classes": len(classes),
              "odd_drift_classes": odd, "first_read_phases": phases,
              "literal_same_cell_check": "passed",
              "stable_alternation_check": "passed",
              "status": "fixed_word_check_not_global_proof"}
    out = Path(__file__).with_name("first_divergence_phases.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"period": period, "drift": drift,
                      "first_read_phase_count": len(fresh),
                      "phases": sorted(fresh), "all_first_turns": "R",
                      "status": result["status"]}))


if __name__ == "__main__":
    main()
