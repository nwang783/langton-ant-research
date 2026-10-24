"""Literal two-corner scattering probes with exact half-plane certificates.

No finite range in this script is interpreted as an all-parameter theorem.
Coordinates: north is +y, white turns right, black turns left.
"""
import argparse
import json
from pathlib import Path

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def run(seed, limit=400000):
    black = set(seed)
    visited = set()
    p = (0, 0)
    h = 0
    initial_contacts = []
    period_reads = []
    first_visits = []
    records = []
    for start in range(0, limit, 104):
        old = set(black)
        p0, h0 = p, h
        positions = []
        reads = []
        fresh = []
        for j in range(104):
            t = start + j
            positions.append(p)
            b = p in black
            reads.append(int(b))
            isfresh = p not in visited
            fresh.append(isfresh)
            if isfresh and p in seed:
                initial_contacts.append({"t": t, "p": p, "h": h})
            visited.add(p)
            if b:
                black.remove(p)
            else:
                black.add(p)
            h = (h + (-1 if b else 1)) % 4
            dx, dy = DIRS[h]
            p = p[0] + dx, p[1] + dy
        v = p[0] - p0[0], p[1] - p0[1]
        if abs(v[0]) == abs(v[1]) == 2 and h == h0:
            shifted = {(x + v[0], y + v[1]) for x, y in old}
            diff = black ^ shifted
            dot = lambda q: v[0] * q[0] + v[1] * q[1]
            path_min = min(map(dot, positions + [p]))
            diff_max = max(map(dot, diff), default=path_min - 1 + 8)
            threshold = diff_max - 8
            if threshold < path_min:
                # The standard inward-nested half-plane certificate proves
                # all future position, heading and read-color observations.
                cert = {
                    "start": start, "end": start + 104, "drift": v,
                    "pose": [p0, h0], "threshold": threshold,
                    "path_min": path_min, "difference_max": diff_max,
                    "difference_size": len(diff), "black_mass": len(black),
                    "read_word": "".join("L" if b else "R" for b in reads),
                    "period_positions": positions,
                    "fresh_period_sites": [
                        {"phase": j, "p": q}
                        for j, (q, f) in enumerate(zip(positions, fresh)) if f
                    ],
                    "initial_contacts": initial_contacts,
                }
                return cert
    return {"status": "limit", "limit": limit, "initial_contacts": initial_contacts}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--depths", type=int, nargs="+", default=[40, 80, 120])
    parser.add_argument("--limit", type=int, default=400000)
    parser.add_argument("--output", default="exceptional_corners_probe.json")
    args = parser.parse_args()
    result = {"scope": "finite literal probes, each positive result has an exact half-plane certificate", "cases": []}
    for n in args.depths:
        q = (-33 - 2 * n, -14 - 2 * n)
        a = (q[0], 8 - q[0])
        for seed in [{q}, {q, a}]:
            cert = run(seed, args.limit)
            item = {"depth": n, "seed": sorted(seed), "certificate": cert}
            result["cases"].append(item)
            print(json.dumps({"depth": n, "seed": sorted(seed), "certificate_end": cert.get("end"), "drift": cert.get("drift"), "contacts": cert.get("initial_contacts")}), flush=True)
    path = Path(__file__).with_name(args.output)
    path.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
