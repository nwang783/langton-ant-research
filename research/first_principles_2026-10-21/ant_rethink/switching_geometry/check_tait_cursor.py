"""Exhaust all local arrival masks for the compressed Tait cursor rule."""
import json
from collections import Counter
from pathlib import Path

from active_loops import step
from component_stats import OFFSETS, edge

CORNERS = ((0, 0), (0, 1), (1, 1), (1, 0))
HEADINGS = (2, 3, 0, 1)  # physical heading at SW,NW,NE,SE port


def plus(a, b):
    return a[0] + b[0], a[1] + b[1]


def cursor(p, h):
    return plus(p, OFFSETS[h])


def other_endpoint(cell, v):
    u, w = edge(cell)
    assert v in (u, w)
    return w if v == u else u


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def minus(a, b):
    return a[0] - b[0], a[1] - b[1]


def main():
    v = (0, -1)
    counts = Counter()
    cases = []
    for port in range(4):
        incoming_port = (port - 1) % 4
        arrival_cell = plus(v, CORNERS[incoming_port])
        previous_vertex = other_endpoint(arrival_cell, v)
        incoming_vector = minus(v, previous_vertex)
        for mask in range(16):
            if mask & (1 << incoming_port):
                continue  # the arrival edge was deleted by the previous macro
            black = {plus(v, CORNERS[j]) for j in range(4) if mask & (1 << j)}
            before = set(black)
            p = plus(v, CORNERS[port])
            h = HEADINGS[port]
            r = 0
            processed = []
            while True:
                was_present = p in black
                old_cursor = cursor(p, h)
                assert old_cursor == v
                old_p = p
                p, h = step(p, h, black, True)
                new_cursor = cursor(p, h)
                processed.append(old_p)
                if was_present:
                    assert new_cursor == other_endpoint(old_p, v)
                    break
                assert new_cursor == v
                r += 1
                assert r <= 4
            assert r in (0, 1, 2, 4)
            assert len(black) - len(before) == r - 1
            assert len(processed) == r + 1
            outgoing_vector = minus(new_cursor, v)
            assert outgoing_vector != (-incoming_vector[0], -incoming_vector[1])
            turn = (cross(incoming_vector, outgoing_vector) > 0) - (
                cross(incoming_vector, outgoing_vector) < 0
            )
            assert turn == {0: 1, 1: 0, 2: -1, 4: 1}[r]
            degree_after = sum(plus(v, c) in black for c in CORNERS)
            assert degree_after <= (3 if r == 4 else 2)
            assert (r == 4) == (not before)
            counts[r] += 1
            cases.append({"port": port, "mask": mask, "r": r,
                          "degree_after": degree_after,
                          "processed_cells": processed})
    output = {"local_cases": len(cases), "r_counts": dict(counts),
              "all_assertions_passed": True, "cases": cases}
    Path(__file__).with_suffix(".json").write_text(json.dumps(output, indent=2))
    print(json.dumps({k: v for k, v in output.items() if k != "cases"}))


if __name__ == "__main__":
    main()
