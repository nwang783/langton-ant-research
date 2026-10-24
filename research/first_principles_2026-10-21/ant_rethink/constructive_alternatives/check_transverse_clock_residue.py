"""Exact numerical controls for the transverse-clock residue lemma.

This checks the retained standard seed, literal per-update clock gains,
deposit coefficient, and the explicit odometer's one-bit return times.
It is not an exhaustive search or a global Langton-ant proof.
"""

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parents[1]
REFERENCE = json.loads(
    (WORKSPACE / "ant_global/root/standard.json").read_text()
)
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))


def f(z):
    return 3 ** abs(z) - 1


def chi(q):
    return -1 if (q[0] + q[1]) % 2 else 1


def eta(h):
    return 1 if h in (1, 2) else -1


def sigma(p, h):
    return chi(p) if h in (0, 2) else -chi(p)


def j(z, e):
    return f(z) // 2 if e * z >= 0 else -3 * f(z) // 2


def weight(q, sector=-1, center=2):
    return sector * chi(q) * f(q[0] - q[1] - center)


def clock(board, p, h, center=2):
    sector = sigma(p, h)
    return sum(weight(q, sector, center) for q in board) + j(
        p[0] - p[1] - center, eta(h)
    )


def update(board, p, h):
    black = p in board
    if black:
        board.remove(p)
    else:
        board.add(p)
    h = (h + (-1 if black else 1)) % 4
    return (p[0] + DIR[h][0], p[1] + DIR[h][1]), h, "L" if black else "R"


def main():
    local_cases = 0
    for x in range(-7, 8):
        for y in range(-7, 8):
            for h in range(4):
                for black in (False, True):
                    board = {(x, y)} if black else set()
                    p = (x, y)
                    before = clock(board, p, h)
                    old_sigma = sigma(p, h)
                    old_eta = eta(h)
                    z = x - y - 2
                    p1, h1, _ = update(board, p, h)
                    actual = clock(board, p1, h1) - before
                    expected = 1 + (
                        4 * f(z) if eta(h1) != old_eta and old_eta * z < 0 else 0
                    )
                    assert sigma(p1, h1) == old_sigma
                    assert actual == expected and actual >= 1
                    local_cases += 1

    seed = {tuple(q) for q in REFERENCE["seed"]}
    board = set(seed)
    p = (0, 0)
    h = REFERENCE["heading"]
    before = clock(board, p, h)
    gains = []
    letters = []
    for _ in range(104):
        old = clock(board, p, h)
        p, h, letter = update(board, p, h)
        letters.append(letter)
        gains.append(clock(board, p, h) - old)
    assert "".join(letters) == REFERENCE["word"]
    assert p == tuple(REFERENCE["drift"]) == (-2, -2)
    assert h == REFERENCE["heading"] == 3
    translated = {(q[0] + p[0], q[1] + p[1]) for q in seed}
    assert translated <= board
    deposit = board - translated
    assert len(deposit) == 12
    assert before == -138
    assert sum(weight(q) for q in seed) == -142
    assert sum(weight(q) for q in deposit) == sum(gains) == 856
    assert min(q[0] - q[1] for q in deposit) == -3
    assert max(q[0] - q[1] for q in deposit) == 7

    # Direct board-coordinate replay of the separate compact countermodel.
    a = 0
    bits = set()
    targets = {(2 * 4**r + 1) // 3: 2 * r for r in range(10)}
    counter_returns = []
    for t in range(1, max(targets) + 1):
        old_mass = len(bits)
        if a == 0:
            index = 0
        else:
            k = 0
            while k in bits:
                k += 1
            index = k + 1
        if index in bits:
            bits.remove(index)
        else:
            bits.add(index)
        a ^= 1
        assert abs(len(bits) - old_mass) == 1
        if t in targets:
            assert a == 1 and bits == {targets[t]}
            counter_returns.append({"time": t, "black_index": targets[t]})

    result = {
        "status": "exact_controls_passed",
        "local_clock_cases": local_cases,
        "canonical_period": 104,
        "canonical_drift": p,
        "initial_clock": before,
        "deposit_weight": sum(weight(q) for q in deposit),
        "deposit": sorted(deposit),
        "clock_gain_inventory": {str(v): gains.count(v) for v in sorted(set(gains))},
        "countermodel_single_bit_returns": counter_returns,
        "scope": "Algebraic and literal replay controls, not a global ant proof.",
    }
    (HERE / "transverse_clock_residue_controls.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
