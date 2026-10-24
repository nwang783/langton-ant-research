"""Exact audits of four critical clocks and the sharp 2K+4 forcing lemma.

The finite audits supplement the analytic proof in low_mass_recurrence.md.
They make no claim to decide eventual highway formation.
"""
from pathlib import Path
from fractions import Fraction
import json
import random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'ant_continuation'))
from ant_exact import step, DIRS
from axial_separator import sector, sign


def ez(h):
    return 1 if h in (0, 1) else -1


def eu(h):
    return 1 if h in (1, 2) else -1


def event(h, g):
    """Exactly one of z+, z-, u+, u- fires on each ant update."""
    if ez(h) != ez(g):
        return 0 if ez(g) == 1 else 1
    assert eu(h) != eu(g)
    return 2 if eu(g) == 1 else 3


def coefficient(e):
    return Fraction(1 if e == 1 else -3, 2)


def clocks(B, p, h):
    sigma = sector(p, h)
    values = []
    for normal, orientation in ((0, 1), (0, -1), (1, 1), (1, -1)):
        z = p[0] + p[1] if normal == 0 else p[0] - p[1]
        direction = ez(h) if normal == 0 else eu(h)
        factor = -sigma if normal == 0 else sigma
        field = sum(
            factor * sign(x + y)
            * Fraction(3) ** (orientation * (x + y if normal == 0 else x - y))
            for x, y in B
        )
        values.append(field + coefficient(orientation * direction)
                      * Fraction(3) ** (orientation * z))
    return values


def audit_local_clocks():
    count = 0
    for x in (0, 1):
        for y in (0, 1):
            for h in range(4):
                for color in (0, 1):
                    p = (x, y)
                    B = {p} if color else set()
                    before = clocks(B, p, h)
                    q, g, _ = step(B, p, h)
                    after = clocks(B, q, g)
                    active = event(h, g)
                    normal = x + y if active < 2 else x - y
                    direction = 1 if active % 2 == 0 else -1
                    expected = 4 * Fraction(3) ** (direction * normal)
                    for j in range(4):
                        assert after[j] - before[j] == (expected if j == active else 0)
                    count += 1
    return count


def longest_avoiding_prefix(K, h0, forbidden):
    """Exhaust all feasible prefixes with <=K initially black read cells.

    A new read prescribes its initial bit. A repeated read must respect every
    earlier flip. Cells outside the read set cannot reduce the required mass.
    There are only linearly many candidate turn plans when one event is absent.
    """
    longest = 0
    nodes = 0
    max_length = 2 * K + 4
    stack = [((0, 0), h0, {}, frozenset(), 0)]
    while stack:
        p, h, current_bits, initially_black, length = stack.pop()
        nodes += 1
        longest = max(longest, length)
        assert length < max_length, (K, h0, forbidden, length)
        for bit in (0, 1):
            g = (h + (1 if bit == 0 else -1)) % 4
            if event(h, g) == forbidden:
                continue
            if p in current_bits and current_bits[p] != bit:
                continue
            initial = initially_black
            if p not in current_bits and bit == 1:
                initial = initial | {p}
            if len(initial) > K:
                continue
            updated = dict(current_bits)
            updated[p] = 1 - bit
            dx, dy = DIRS[g]
            stack.append(((p[0] + dx, p[1] + dy), g, updated, initial, length + 1))
    return longest, nodes


def audit_all_small_avoiding_plans():
    total_nodes = 0
    records = []
    for K in range(17):
        maxima = []
        for h in range(4):
            for forbidden in range(4):
                longest, nodes = longest_avoiding_prefix(K, h, forbidden)
                assert longest <= 2 * K + 3
                maxima.append(longest)
                total_nodes += nodes
        assert max(maxima) == 2 * K + 3
        records.append({'K': K, 'maximum_avoiding_length': max(maxima)})
    return records, total_nodes


def audit_tight_family():
    records = []
    for K in range(65):
        B = {(j + 1, j) for j in range(K)}
        p, h = (0, 0), 0
        observed = []
        for j in range(2 * K + 4):
            old_h = h
            p, h, letter = step(B, p, h)
            observed.append(letter)
            assert (event(old_h, h) == 0) == (j == 2 * K + 3)
        assert ''.join(observed[:-1]) == 'RL' * K + 'RRR'
        records.append({'K': K, 'first_z_plus_update_index': 2 * K + 3})
    return records


def audit_literal_intervals():
    rng = random.Random(20261022)
    starts = 0
    event_checks = 0
    max_wait = 0
    for seed in range(100):
        B = {(rng.randrange(-6, 7), rng.randrange(-6, 7))
             for _ in range(rng.randrange(40))}
        if seed % 3 == 0:
            B |= {(10**6 + seed, -10**6), (-10**6, 10**6 + seed)}
        p = (rng.randrange(-3, 4), rng.randrange(-3, 4))
        h = rng.randrange(4)
        masses, events = [], []
        for _ in range(1000):
            masses.append(len(B))
            old_h = h
            p, h, _ = step(B, p, h)
            events.append(event(old_h, h))
        next_event = [None] * 4
        next_at = [None] * len(events)
        for t in range(len(events) - 1, -1, -1):
            next_event[events[t]] = t
            next_at[t] = tuple(next_event)
        for t in range(0, 301, 3):
            for target in range(4):
                occurrence = next_at[t][target]
                assert occurrence is not None
                wait = occurrence - t
                assert wait <= 2 * masses[t] + 3
                max_wait = max(max_wait, wait)
                event_checks += 1
            starts += 1
    return starts, event_checks, max_wait


def main():
    local = audit_local_clocks()
    exhaustive, nodes = audit_all_small_avoiding_plans()
    tight = audit_tight_family()
    starts, event_checks, max_wait = audit_literal_intervals()
    result = {
        'status': 'PASS',
        'local_clock_cases': local,
        'exhaustive_plan_mass_range': [0, 16],
        'exhaustive_heading_event_cases': 17 * 4 * 4,
        'exhaustive_symbolic_nodes': nodes,
        'exhaustive_maxima': exhaustive,
        'tight_family_mass_range': [0, 64],
        'tight_family': tight,
        'literal_interval_starts': starts,
        'literal_first_event_checks': event_checks,
        'largest_observed_wait_index': max_wait,
        'proof_scope': 'Every block of 2K+4 updates starting with mass <=K has all four increment types.',
    }
    Path(__file__).with_name('forcing_and_small_mass_audit.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ('exhaustive_maxima', 'tight_family')}, indent=2))


if __name__ == '__main__':
    main()
