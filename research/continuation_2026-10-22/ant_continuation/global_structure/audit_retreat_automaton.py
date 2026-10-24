#!/usr/bin/env python3
"""Exact controls for retreat_area.md. No finite seed census proves HC."""
from itertools import product
import json

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def window_step(state, rx, ry, signs):
    bits, ix, iy, h = state
    width = rx + 1
    area = width * (ry + 1)
    black = (bits >> (ix + width * iy)) & 1
    bits ^= 1 << (ix + width * iy)
    h = (h + (-1 if black else 1)) % 4
    dx, dy = DIRS[h]
    du, dv = signs[0] * dx, signs[1] * dy
    # Current upper corner is (0,0), current head is (-ix,-iy).
    add_u = max(0, -ix + du)
    add_v = max(0, -iy + dv)
    next_ix, next_iy = ix + add_u - du, iy + add_v - dv
    if next_ix > rx or next_iy > ry:
        return None
    assert min(next_ix, next_iy) >= 0
    if add_u:
        last_col = sum(1 << (rx + width * j) for j in range(ry + 1))
        bits &= ~last_col
    bits <<= add_u + width * add_v
    bits &= (1 << area) - 1
    return (bits, next_ix, next_iy, h), (add_u, add_v)


def literal_step(B, p, h, signs):
    black = p in B
    if black:
        B.remove(p)
    else:
        B.add(p)
    h = (h + (-1 if black else 1)) % 4
    dx, dy = DIRS[h]
    return (p[0] + signs[0] * dx, p[1] + signs[1] * dy), h


def project(B, p, h, M, rx, ry):
    width = rx + 1
    bits = 0
    for u, v in B:
        ix, iy = M[0] - u, M[1] - v
        if 0 <= ix <= rx and 0 <= iy <= ry:
            bits |= 1 << (ix + width * iy)
    return bits, M[0] - p[0], M[1] - p[1], h


def exhaustive_transitions():
    count = 0
    for rx, ry in product(range(3), repeat=2):
        width = rx + 1
        area = width * (ry + 1)
        for bits in range(1 << area):
            inside = {
                (-i, -j)
                for i in range(rx + 1)
                for j in range(ry + 1)
                if (bits >> (i + width * j)) & 1
            }
            for ix, iy, h, ex, ey in product(
                range(rx + 1), range(ry + 1), range(4), (-1, 1), (-1, 1)
            ):
                # These remote bits make both initial maxima exactly zero.
                # They lie below a lower side and are absent from the window.
                B = inside | {(-rx - 2, 0), (0, -ry - 2)}
                signs = ex, ey
                p = -ix, -iy
                planned = window_step((bits, ix, iy, h), rx, ry, signs)
                q, hh = literal_step(B, p, h, signs)
                MM = max(0, q[0]), max(0, q[1])
                projected = project(B, q, hh, MM, rx, ry)
                outside = projected[1] > rx or projected[2] > ry
                assert (planned is None) == outside
                if planned is not None:
                    assert planned[0] == projected
                    assert planned[1] == MM
                count += 1
    return count


def blank_certificate():
    # This is a positive control for the certificate mechanism, not the
    # research target. Bounds are fixed before the simulation starts.
    rx = ry = 100
    signs = -1, -1
    state = (0, 0, 0, 0)
    B = set()
    p = (0, 0)
    h = 0
    M = (0, 0)
    seen = {}
    for t in range(100000):
        if state in seen:
            s, old_M = seen[state]
            drift_uv = M[0] - old_M[0], M[1] - old_M[1]
            assert drift_uv != (0, 0)
            return {
                "first_repeat_from": s,
                "first_repeat_at": t,
                "period": t - s,
                "physical_drift": [signs[i] * drift_uv[i] for i in range(2)],
                "fixed_bounds": [rx, ry],
            }
        seen[state] = t, M
        result = window_step(state, rx, ry, signs)
        assert result is not None
        state, advance = result
        M = M[0] + advance[0], M[1] + advance[1]
        p, h = literal_step(B, p, h, signs)
        if t % 127 == 0:
            assert state == project(B, p, h, M, rx, ry)
    raise AssertionError("No repeat inside positive-control budget")


if __name__ == "__main__":
    result = {
        "exact_small_window_transitions": exhaustive_transitions(),
        "blank_positive_control": blank_certificate(),
        "status": "All exact controls passed; no HC claim",
    }
    print(json.dumps(result, indent=2))
