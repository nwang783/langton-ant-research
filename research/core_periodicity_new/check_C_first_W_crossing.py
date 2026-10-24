"""A C-first W-oriented proper crossing cannot be the first center contact.

Complete seven-role, shifted-clock existing-KV query inventory. No path search.
"""

from collections import Counter
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
GP = ROOT / "chronology_dcuv/literal_residual_geometry.json"
CP = ROOT / "chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv"
G = json.loads(GP.read_text())["geometry"]
IDS = (0, 1, 4, 5, 6, 7, 8, 9)
NEW = {a: i for i, a in enumerate(IDS)}
COUNTED = {tuple(map(int, line.split()[:8])) for line in CP.read_text().splitlines()}


def rot(p, h):
    x, y = p
    return ((x, y), (y, -x), (-x, -y), (-y, x))[h % 4]


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def cross(p, q):
    return p[0] * q[1] - p[1] * q[0]


def base_id(a):
    return 0 if G[a]["name"][0] == "D" else 4 if G[a]["name"][0] == "V" else 7


def closed_chord_contact(head, heading, base):
    # Twice all centers keeps this exact, including endpoint/collinear contact.
    correction = rot((-1, -1), heading)
    c = (2 * head[0] + correction[0], 2 * head[1] + correction[1])
    step = rot(G[base]["endpoint"][:2], heading)
    d = add(c, (2 * step[0], 2 * step[1]))
    a, b = (-1, -1), (1, 1)
    u, v, w = sub(b, a), sub(d, c), sub(c, a)
    determinant = cross(u, v)
    if determinant:
        s, t = cross(w, v), cross(w, u)
        if determinant < 0:
            determinant, s, t = -determinant, -s, -t
        return 0 <= s <= determinant and 0 <= t <= determinant
    if cross(w, u):
        return False
    return all(max(min(a[k], b[k]), min(c[k], d[k])) <= min(max(a[k], b[k]), max(c[k], d[k])) for k in (0, 1))


# The C atom's fresh q is before-white at later V(1, 0, W), specifically local (2, 0).
q = (1, 2)
target = (1, 0)
assert rot(sub(q, target), -3) == (2, 0)
assert [2, 0, False, 8] in G[4]["requirements"]

roles = []
for a in IDS:
    count = G[a]["name"].count("C")
    position = tuple(G[base_id(a)]["endpoint"][:2])
    heading = 0
    for prefix_index in range(count):
        output = add(position, rot(q, heading))
        assert list(output) in G[a]["outputs"]
        roles.append({
            "full_source": a,
            "full_source_name": G[a]["name"],
            "C_atom_number": prefix_index + 1,
            "atomic_entry_in_full_source_frame": [*position, heading],
            "atomic_birth_clock_shift": prefix_index,
            "full_source_output": output,
            "remaining_source_C_atoms": count - prefix_index,
        })
        position = add(position, rot((0, 1), heading))
        heading = (heading - 1) % 4
assert len(roles) == 7

cases = []
for role_index, role in enumerate(roles):
    a = role["full_source"]
    px, py, original_heading = role["atomic_entry_in_full_source_frame"]
    original_position = (px, py)
    shift = role["atomic_birth_clock_shift"]
    for delta in range(6):
        consumer_heading = (-delta) % 4
        source_age = delta + shift
        for b in IDS:
            consumer_c = G[b]["name"].count("C")
            base = base_id(b)
            for inp in G[b]["inputs"]:
                position = sub(q, rot(inp, consumer_heading))
                full_position = add(original_position, rot(position, original_heading))
                full_heading = (original_heading + consumer_heading) % 4
                key = (NEW[a], NEW[b], *full_position, full_heading, *role["full_source_output"], min(source_age, 5))
                row = {
                    "role_index": role_index,
                    "atomic_entry_C_gap_to_consumer": delta,
                    "full_source_included_C_age": source_age,
                    "counted_cap_value": min(source_age, 5),
                    "consumer": b,
                    "consumer_name": G[b]["name"],
                    "input": inp,
                    "consumer_pose_in_atomic_frame": [*position, consumer_heading],
                    "full_source_counted_query": key,
                }
                if delta < role["remaining_source_C_atoms"]:
                    reason = "CONSUMER_BEFORE_FULL_SOURCE_EXIT"
                elif delta + consumer_c > 5:
                    reason = "CONSUMING_FULL_PACKET_CANNOT_FINISH_BEFORE_TARGET"
                elif (sum(position) + consumer_heading) % 2:
                    reason = "WRONG_SECTOR"
                elif key in COUNTED:
                    reason = "SIGNED_COUNT5_EXCLUDED"
                else:
                    endpoint = add(position, rot(G[base]["endpoint"][:2], consumer_heading))
                    row["consuming_base_endpoint"] = endpoint
                    if closed_chord_contact(position, consumer_heading, base):
                        assert shift == 1 and delta == 4
                        reason = "EARLIER_CLOSED_CENTER_CONTACT"
                    elif delta == 4:
                        assert shift == 1 and consumer_heading == 0 and endpoint[1] >= 2
                        assert 5 - delta == 1
                        # N/W zero-C bases cannot lower y; N-to-W C adds one y.
                        assert endpoint[1] + 1 > target[1]
                        reason = "ONE_REMAINING_C_N_TO_W_STAYS_ABOVE_TARGET"
                    elif delta == 5:
                        assert consumer_heading == 3 and b == 7
                        assert position in ((2, 3), (3, 2))
                        assert endpoint in ((-2, 3), (-1, 2))
                        assert endpoint[0] < target[0] and endpoint[1] > target[1]
                        reason = "FINAL_W_ZERO_CONE_CANNOT_REACH_TARGET"
                    else:
                        raise AssertionError((role, row))
                row["reason"] = reason
                cases.append(row)

assert len(cases) == 7 * 6 * 23 == 966
reasons = Counter(row["reason"] for row in cases)
assert reasons["EARLIER_CLOSED_CENTER_CONTACT"] == 12
assert reasons["ONE_REMAINING_C_N_TO_W_STAYS_ABOVE_TARGET"] == 12
assert reasons["FINAL_W_ZERO_CONE_CANNOT_REACH_TARGET"] == 14
assert sum(reasons.values()) == 966

cone_steps = {str(h): [rot(G[b]["endpoint"][:2], h) for b in (0, 4, 7)] for h in (0, 3)}
assert all(p[1] >= 0 for steps in cone_steps.values() for p in steps)
assert all(p[0] < 0 for p in cone_steps["3"])
assert rot((0, 1), 0) == (0, 1)

result = {
    "status": "AUTHOR_C_FIRST_W_FIVE_C_CANNOT_BE_FIRST_CENTER_CONTACT_PASS",
    "scope": "Actual atomic C inside a complete recurrent-eight factor at (0,0,N), later V base at (1,0,W) with atomic-entry C gap five. If this proper crossing were the first center self-contact, its mandatory fresh q=(1,2) cannot have retired beforehand. Not an unconditional five-C crossing or return exclusion.",
    "source_atomic_fresh_output": q,
    "later_V_pose": [*target, 3],
    "later_white_slot": [2, 0],
    "all_seven_actual_C_roles": roles,
    "all_966_consumer_options": cases,
    "reason_counts": dict(reasons),
    "zero_C_cone_steps": cone_steps,
    "dependency_hashes": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (GP, CP, Path(__file__).resolve())},
}
(ROOT / "chronology_dcuv/C_first_W_crossing.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"roles": len(roles), "options": len(cases), "reasons": dict(reasons)}))
