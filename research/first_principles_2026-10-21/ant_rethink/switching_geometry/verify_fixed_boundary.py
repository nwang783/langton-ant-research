"""Literal verification of the fixed-boundary return-summary counterexample."""
import json
from itertools import product
from pathlib import Path
from boundary_return_map import D, true_exit
from return_summary_audit import admissible, summarize


def main():
    box = set(product(range(5), repeat=2))
    boundary = {p for p in box if p[0] in (0, 4) or p[1] in (0, 4)}
    b1 = {(0, 1), (1, 1)}
    b2 = {(0, 1), (1, 2)}
    assert b1 & boundary == b2 & boundary == {(0, 1)}
    entries = [(p, h) for p in sorted(box) for h in range(4)
               if admissible(p, h)
               and (p[0]-D[h][0], p[1]-D[h][1]) not in box]
    s1 = summarize(box, entries, b1)
    s2 = summarize(box, entries, b2)
    assert s1 == s2
    assert s1[1] == (2, 10, 2, 1, 2, 2, 1, 2, 2, 2)
    assert s1[2] == (4, 4, 4, 4, 4, 4)
    entry = ((0, 1), 0)
    exit1, final1, word1 = true_exit(box, b1, entry)
    exit2, final2, word2 = true_exit(box, b2, entry)
    assert exit1 == ((1, 5), 3)
    assert exit2 == ((-1, 4), 2)
    assert len(word1) == 35 and len(word2) == 18
    assert word1 == "LRRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLR"
    assert word2 == "LRLRRRRLRRRRLLLLRL"
    out = {"verified": True, "identical_boundary": True,
           "identical_frozen_summary": True, "equal_initial_mass": 2,
           "first_exit_steps": [len(word1), len(word2)],
           "first_exits": [exit1, exit2], "final_black": [sorted(final1), sorted(final2)]}
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2))
    print(json.dumps(out))


if __name__ == "__main__":
    main()
