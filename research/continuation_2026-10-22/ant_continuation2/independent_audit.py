"""Independent complex-coordinate audit of the analytic clock and mass lemmas.

This file imports none of the other ant simulators. The finite checks are an
implementation audit, not a replacement for the general proofs.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
DIRECTIONS = (1j, 1, -1j, -1)


def coords(p):
    return int(p.real), int(p.imag)


def parity(p):
    x, y = coords(p)
    return 1 if (x + y) % 2 == 0 else -1


def sector(p, d):
    return parity(p) * (1 if d.imag else -1)


def update(B, p, d):
    old_black = p in B
    d *= 1j if old_black else -1j
    if old_black:
        B.remove(p)
    else:
        B.add(p)
    return p + d, d


def values(B, p, d):
    sigma = sector(p, d)
    answer = []
    for transverse in (False, True):
        normal = (lambda q: int(q.real - q.imag)) if transverse else (lambda q: int(q.real + q.imag))
        e = normal(d)
        coefficient = sigma if transverse else -sigma
        for orientation in (1, -1):
            field = sum(coefficient * parity(q) * Q(3) ** (orientation * normal(q)) for q in B)
            head = Q(1 if orientation * e == 1 else -3, 2) * Q(3) ** (orientation * normal(p))
            answer.append(field + head)
    return answer


def firing(d, new_d):
    for k, normal in enumerate((lambda q: int(q.real + q.imag), lambda q: int(q.real - q.imag))):
        if normal(d) != normal(new_d):
            return 2 * k + (0 if normal(new_d) == 1 else 1)
    raise AssertionError("No clock type fired")


def audit():
    local = 0
    for x, y, d, bit in product((0, 1), (0, 1), DIRECTIONS, (False, True)):
        p = complex(x, y)
        B = {p} if bit else set()
        before = values(B, p, d)
        q, new_d = update(B, p, d)
        after = values(B, q, new_d)
        active = firing(d, new_d)
        normal = x + y if active < 2 else x - y
        expected = 4 * Q(3) ** ((1 if active % 2 == 0 else -1) * normal)
        assert [b - a for a, b in zip(before, after)] == [expected if j == active else 0 for j in range(4)]
        local += 1

    cells = [complex(x, y) for x in range(-1, 2) for y in range(-1, 2)]
    intervals = 0
    first_events = 0
    full_clock_comparisons = 0
    for mask in range(1 << len(cells)):
        initial = {q for j, q in enumerate(cells) if (mask >> j) & 1}
        for d0 in DIRECTIONS:
            B = set(initial)
            p, d = 0j, d0
            midpoint0 = -d0 / 2
            clocks = values(B, p, d)
            first = [None] * 4
            snapshots = [(set(B), p, d)]
            for t in range(1, 33):
                old_p, old_d = p, d
                p, d = update(B, p, d)
                active = firing(old_d, d)
                if first[active] is None:
                    first[active] = t
                x, y = coords(old_p)
                normal = x + y if active < 2 else x - y
                clocks[active] += 4 * Q(3) ** ((1 if active % 2 == 0 else -1) * normal)
                if t in (1, 4, 8, 16, 32):
                    assert values(B, p, d) == clocks
                    full_clock_comparisons += 4
                displacement = p - d / 2 - midpoint0
                assert len(B ^ initial) >= 2 * max(abs(displacement.real), abs(displacement.imag))
                intervals += 1
                if t in (3, 7, 15, 31):
                    for C, q, e in snapshots:
                        displacement = p - d / 2 - q + e / 2
                        assert len(B ^ C) >= 2 * max(abs(displacement.real), abs(displacement.imag))
                        intervals += 1
                    snapshots.append((set(B), p, d))
            assert all(t is not None and t <= 2 * len(initial) + 4 for t in first)
            first_events += 4

    tight = 0
    for K in range(101):
        B = {complex(j + 1, j) for j in range(K)}
        p, d = 0j, 1j
        first = None
        for t in range(1, 2 * K + 5):
            old = d
            p, d = update(B, p, d)
            if firing(old, d) == 0:
                first = t
                break
        assert first == 2 * K + 4
        tight += 1

    endpoint_checks = 0
    previous = None
    for n in range(1, 31):
        B = {complex(x, y) for x in (-2*n, 2*n+1) for y in (-2*n+1, 2*n+2)}
        current = values(B, 0j, 1j)
        if previous is not None:
            assert all(a < b for a, b in zip(previous, current))
        assert all(v > 0 for v in current)
        for row in {-2*n+1, 2*n+2}:
            assert sum((-1) ** int(q.real) for q in B if int(q.imag) == row) == 0
        for col in {-2*n, 2*n+1}:
            assert sum((-1) ** int(q.imag) for q in B if int(q.real) == col) == 0
        previous = current
        endpoint_checks += 1
    return {
        "status": "PASS",
        "independence": "Complex-coordinate stepper; imports no other project simulator",
        "local_cases": local,
        "complete_initial_fields": 512,
        "poses_per_field": 4,
        "literal_updates": 512 * 4 * 32,
        "support_change_intervals": intervals,
        "exact_full_clock_comparisons": full_clock_comparisons,
        "first_event_checks": first_events,
        "sharp_family_K_range": [0, tight - 1],
        "four_cell_endpoint_checks": endpoint_checks,
        "scope": "Finite audit of analytic lemmas; no general highway decision",
    }


if __name__ == "__main__":
    result = audit()
    (HERE / "independent_audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
