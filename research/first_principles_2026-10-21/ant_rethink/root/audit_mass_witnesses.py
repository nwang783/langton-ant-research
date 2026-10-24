"""Independent literal replay of all retained exact mass-ceiling witnesses.

This verifies lower witnesses and compares the two independently implemented
complete searches where both are available. It does not replace inspection
of the exhaustive-search coverage arguments.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def replay(seed, length):
    black = {tuple(q) for q in seed}
    x = y = heading = 0
    masses = [len(black)]
    word = []
    for _ in range(length):
        p = x, y
        if p in black:
            word.append("L")
            black.remove(p)
            heading = (heading - 1) % 4
        else:
            word.append("R")
            black.add(p)
            heading = (heading + 1) % 4
        dx, dy = DIRECTIONS[heading]
        x, y = x + dx, y + dy
        masses.append(len(black))
    return "".join(word), masses


def main():
    records = []
    for k in range(16):
        data = json.loads((HERE / f"mass_bound_{k}.json").read_text())
        assert data["complete"] is True
        t = data["forced_exceedance_by"]
        assert t == data["max_surviving_updates"] + 1
        word, masses = replay(data["seed"], t)
        assert word[:-1] == data["word"]
        assert max(masses[:-1]) <= k
        assert masses[-1] == k + 1
        other = HERE.parent / "switching_geometry" / f"mass_ceiling_{k}.json"
        compared = False
        if other.exists():
            independent = json.loads(other.read_text())
            assert independent["T"] == t
            w = independent["witness"]
            assert w["unassigned_initial_black"] == 0
            word2, masses2 = replay(w["visible_initial_black"], t)
            assert word2 == w["word"]
            assert max(masses2[:-1]) <= k and masses2[-1] == k + 1
            compared = True
        records.append({"K": k, "T": t, "literal_witness_passed": True,
                        "independent_full_search_agrees": compared})
    output = {"all_passed": True, "records": records}
    (HERE / "mass_witness_audit.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
