"""Reduce first four-C center contact to D/C -> C and give a real sharp control.

Exact finite geometry and existing age clauses only. No path generation.
"""

from collections import Counter
from fractions import Fraction as F
from math import ceil, floor
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
GP = ROOT / "chronology_dcuv/literal_residual_geometry.json"
CP = ROOT / "chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv"
HP = ROOT / "chronology_dcuv/protected_patch2.tsv"
AP = ROOT / "atomic_common_4C_frozen_20261023_1344/manifest.json"
DATA = json.loads(GP.read_text())
G = DATA["geometry"]
K = set(map(tuple, DATA["core"]))
IDS = (0, 1, 4, 5, 6, 7, 8, 9)
NEW = {a: i for i, a in enumerate(IDS)}
COUNTED = {tuple(map(int, line.split()[:8])) for line in CP.read_text().splitlines()}
HB = {tuple(map(int, line.split()[:7])) for line in HP.read_text().splitlines()}
VECTORS = {"D": (1, 1), "C": (1, 1), "V": (1, 3), "U": (0, 4)}
HEAD_STEPS = ((0, 1), (1, 0), (0, -1), (-1, 0))
C_WORD = G[1]["word"][len(G[0]["word"]):]


def rot(p, h):
    x, y = p
    return ((x, y), (y, -x), (-x, -y), (-y, x))[h % 4]


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def det(p, q):
    return p[0] * q[1] - p[1] * q[0]


def base(a):
    return 0 if G[a]["name"][0] == "D" else 4 if G[a]["name"][0] == "V" else 7


def requirements(raw):
    colors, initial = {}, {}
    p, h = (0, 0), 0
    for tick, turn in enumerate(raw + G[0]["marker"]):
        black = turn == "L"
        if p in colors:
            if colors[p] != black:
                return initial, {"tick": tick, "cell": p, "prescribed": turn, "actual": "L" if colors[p] else "R"}
        else:
            initial[p] = black
        colors[p] = not black
        h = (h + (-1 if black else 1)) % 4
        p = add(p, HEAD_STEPS[h])
    return initial, None


contexts = {name: {tuple(v[:2]): v[2] for v in G[a]["requirements"]} for name, a in (("D", 0), ("V", 4), ("U", 7))}
contexts["C"], conflict = requirements(C_WORD)
assert conflict is None
outputs = {"D": G[0]["outputs"], "V": G[4]["outputs"], "U": G[7]["outputs"], "C": [(1, 2), (2, 0), (2, 1)]}


def closed_contact(source_atom, consumer, p, h):
    u = tuple(2 * v for v in VECTORS[source_atom])
    v = rot(tuple(2 * z for z in VECTORS[G[consumer]["name"][0]]), h)
    c = (-1, -1)
    w = sub(add((2 * p[0], 2 * p[1]), rot(c, h)), c)
    denominator = det(u, v)
    if denominator:
        s, t = F(det(w, v), denominator), F(det(w, u), denominator)
        return 0 <= s <= 1 and 0 <= t <= 1
    if det(w, u):
        return False
    return all(max(min(c[k], c[k] + u[k]), min(c[k] + w[k], c[k] + w[k] + v[k])) <= min(max(c[k], c[k] + u[k]), max(c[k] + w[k], c[k] + w[k] + v[k])) for k in (0, 1))


def zero_reach(p, target, h):
    x, y = rot(sub(target, p), -h)
    return x >= 0 and y >= 0 and any(y - x - 2 * v >= 0 and (y - x - 2 * v) % 4 == 0 for v in range(x + 1))


# Canonical first-contact geometry, relative heading N at entry gap four.
geometries, boxes = [], []
for a, u in VECTORS.items():
    for b, v in VECTORS.items():
        corners = [(s * u[0] - t * v[0], s * u[1] - t * v[1]) for s in (0, 1) for t in (0, 1)]
        bounds = [(ceil(min(p[k] for p in corners)), floor(max(p[k] for p in corners))) for k in (0, 1)]
        boxes.append({"earlier_atom": a, "later_atom": b, "exact_corners": corners, "integer_bounds": bounds})
        for x in range(bounds[0][0], bounds[0][1] + 1):
            for y in range(bounds[1][0], bounds[1][1] + 1):
                if (x + y) % 2:
                    continue
                denominator = det(u, v)
                if denominator:
                    s, t = F(det((x, y), v), denominator), F(det((x, y), u), denominator)
                    if not (0 <= s < 1 and 0 < t <= 1):
                        continue
                    kind = "NONPARALLEL_ENDPOINT_CONTACT"
                else:
                    if det((x, y), u):
                        continue
                    # At onset of collinear contact the old segment is entered at its START.
                    t = F(-x, v[0]) if v[0] else F(-y, v[1])
                    if not (0 < t <= 1 and add((x, y), (t * v[0], t * v[1])) == (0, 0)):
                        continue
                    s = F(0)
                    kind = "COLLINEAR_FIRST_ENTRY"
                geometries.append({"earlier_atom": a, "later_atom": b, "later_pose": [x, y, 0], "earlier_parameter": s, "later_parameter": t, "kind": kind})
assert len(geometries) == 23

roles = []
for a in IDS:
    count = G[a]["name"].count("C")
    roles.append({"atom": G[a]["name"][0], "full_source": a, "atomic_entry": [0, 0, 0], "clock_shift": 0, "remaining_C": count})
    p, h = tuple(G[base(a)]["endpoint"][:2]), 0
    for j in range(count):
        roles.append({"atom": "C", "full_source": a, "atomic_entry": [*p, h], "clock_shift": j, "remaining_C": count - j})
        p, h = add(p, rot((0, 1), h)), (h - 1) % 4
assert len(roles) == 15

# Reconstruct the exact produced age-five guard needed for U upper input (0,2).
upper_queries = []
for a in IDS:
    for output in G[a]["outputs"]:
        for target in (7, 8, 9):
            for n in range(5):
                h = (-n) % 4
                p = sub(output, rot((0, 2), h))
                key = (NEW[a], NEW[target], *p, h, *output, n)
                wrong = (sum(p) + h) % 2
                hb = (a, target, *p, h, *output)
                if n < G[a]["name"].count("C"):
                    reason = "BEFORE_FULL_SOURCE_EXIT"
                elif wrong:
                    reason = "WRONG_SECTOR"
                elif hb in HB:
                    reason = "SIGNED_HB_EXCLUDED"
                else:
                    assert key in COUNTED
                    reason = "SIGNED_COUNT5_EXCLUDED"
                upper_queries.append({"query": key, "HB_query": hb, "reason": reason})

core_cases, retirement_queries, reductions = [], [], []
for index, geometry in enumerate(geometries):
    a, b = geometry["earlier_atom"], geometry["later_atom"]
    p = tuple(geometry["later_pose"][:2])
    assert p[0] <= 0
    local_common = sub((2, 0), p)
    if contexts[b].get(local_common) is False or local_common in K:
        reason = "SIGNED_ATOMIC_FOUR_C_COMMON_OUTPUT_STILL_CURRENT_BUT_TARGET_WHITE_OR_CORE"
    elif b == "U" and p == (0, -2):
        z = (0, 0)
        assert z in K and add(p, (0, 2)) == z
        for role_index, role in enumerate(roles):
            if role["atom"] != a:
                continue
            source = role["full_source"]
            sx, sy, sh = role["atomic_entry"]
            full_cell = add((sx, sy), rot(z, sh))
            same_output = list(full_cell) in G[source]["outputs"]
            maximum_age = 4 + role["clock_shift"] if same_output else 4 - role["remaining_C"]
            assert maximum_age < 5
            for target in (7, 8, 9):
                core_cases.append({"geometry_index": index, "role_index": role_index, "full_source": source, "target": target, "old_core_cell": z, "full_frame_cell": full_cell, "same_full_source_output": same_output, "maximum_possible_produced_age": maximum_age, "minimum_required": 5})
        reason = "OLD_CORE_TO_U_UPPER_INPUT_TOO_YOUNG"
    elif a in ("V", "U"):
        # Five cases remain; each has a single hard fresh slot.
        hard = (0, 1) if a == "U" and p == (-1, 1) else (0, 0)
        local = sub(hard, p)
        assert local in K or contexts[b].get(local) is False
        producers = (4, 5, 6) if a == "V" else (7, 8, 9)
        for source in producers:
            assert list(hard) in G[source]["outputs"]
            for n in range(5):
                h = (-n) % 4
                for consumer in IDS:
                    cc = G[consumer]["name"].count("C")
                    for inp in G[consumer]["inputs"]:
                        cp = sub(hard, rot(inp, h))
                        key = (NEW[source], NEW[consumer], *cp, h, *hard, n)
                        hb = (source, consumer, *cp, h, *hard)
                        row = {"geometry_index": index, "hard_source_output": hard, "full_source": source, "consumer": consumer, "consumer_input": inp, "consumer_pose": [*cp, h], "entry_C_age": n, "counted_query": key, "HB_query": hb}
                        if n < G[source]["name"].count("C"):
                            why = "BEFORE_FULL_SOURCE_EXIT"
                        elif (sum(cp) + h) % 2:
                            why = "WRONG_SECTOR"
                        elif hb in HB:
                            why = "SIGNED_HB_EXCLUDED"
                        elif key in COUNTED:
                            why = "SIGNED_COUNT5_EXCLUDED"
                        elif closed_contact(a, consumer, cp, h):
                            assert n >= 2
                            why = "EARLIER_NONADJACENT_CLOSED_CENTER_CONTACT"
                        elif b != "C" and n + cc > 4:
                            why = "CONSUMING_FULL_PACKET_CANNOT_FINISH_BEFORE_TARGET_BASE"
                        else:
                            end = add(cp, rot(G[consumer]["endpoint"][:2], h))
                            eh = (h + G[consumer]["endpoint"][2]) % 4
                            assert n + cc == 4 and eh == 0 and not zero_reach(end, p, 0), row
                            row["full_consumer_exit"] = [*end, eh]
                            why = "EXACT_FINAL_ZERO_C_SEMIGROUP_CANNOT_REACH_TARGET"
                        row["reason"] = why
                        retirement_queries.append(row)
        reason = "MANDATORY_HARD_COHORT_RETIREMENT_IMPLIES_EARLIER_CONTACT_OR_IMPOSSIBLE_ZERO_CONE"
        geometry["hard_source_output"] = hard
    else:
        assert a in ("D", "C") and b == "C" and p == (-1, -1)
        reason = "OPEN_D_OR_C_TO_C_GATE"
    reductions.append({"geometry_index": index, "reason": reason})

reason_counts = Counter(row["reason"] for row in reductions)
assert reason_counts == {
    "SIGNED_ATOMIC_FOUR_C_COMMON_OUTPUT_STILL_CURRENT_BUT_TARGET_WHITE_OR_CORE": 12,
    "OLD_CORE_TO_U_UPPER_INPUT_TOO_YOUNG": 4,
    "MANDATORY_HARD_COHORT_RETIREMENT_IMPLIES_EARLIER_CONTACT_OR_IMPOSSIBLE_ZERO_CONE": 5,
    "OPEN_D_OR_C_TO_C_GATE": 2,
}
assert len(core_cases) == 45 and len(retirement_queries) == 1725

# Explicit sharp control: no discovery loop is used here.
word = (1, 0, 5, 5, 6)
seed = {(-5, 2), (-4, 1), (-3, -1), (-3, 3), (-2, 0), (-2, 4), (-1, -1), (-1, 0), (0, -1), (0, 0), (0, 1), (0, 2), (1, 0)}
raw = "".join(G[a]["word"] for a in word)
initial, conflict = requirements(raw)
assert conflict is None and {p for p, black in initial.items() if black} == seed
assert len(raw) == 149
board, p, h = set(seed), (0, 0), 0
for tick, turn in enumerate(raw + G[0]["marker"]):
    black = p in board
    assert black == (turn == "L")
    board.symmetric_difference_update({p})
    h = (h + (-1 if black else 1)) % 4
    p = add(p, HEAD_STEPS[h])
    if tick + 1 == len(raw):
        raw_pose = [*p, h]
assert raw_pose == [-1, 0, 3]

edges, p, h, clock = [], (0, 0), 0, 0
for packet_index, source in enumerate(word):
    for atom in [G[source]["name"][0]] + ["C"] * G[source]["name"].count("C"):
        start = add((2 * p[0], 2 * p[1]), rot((-1, -1), h))
        old_clock = clock
        old_pose = [*p, h]
        head_step = (0, 1) if atom == "C" else VECTORS[atom]
        p = add(p, rot(head_step, h))
        h = (h - int(atom == "C")) % 4
        clock += int(atom == "C")
        end = add((2 * p[0], 2 * p[1]), rot((-1, -1), h))
        edges.append({"atom": atom, "packet_index": packet_index, "entry_pose": old_pose, "entry_C_clock": old_clock, "start_twice": start, "end_twice": end})
assert len(edges) == 10 and clock == 5
contacts = []
for bi, later in enumerate(edges):
    for ai in range(bi - 1):
        earlier = edges[ai]
        u, v = sub(earlier["end_twice"], earlier["start_twice"]), sub(later["end_twice"], later["start_twice"])
        w = sub(later["start_twice"], earlier["start_twice"])
        denominator = det(u, v)
        if denominator:
            s, t = F(det(w, v), denominator), F(det(w, u), denominator)
            if not (0 <= s <= 1 and 0 <= t <= 1):
                continue
        else:
            if det(w, u):
                continue
            k = 0 if v[0] else 1
            t0 = F(-w[k], v[k])
            t1 = F(u[k] - w[k], v[k])
            low, high = max(F(0), min(t0, t1)), min(F(1), max(t0, t1))
            if low > high:
                continue
            t = low
            point = add(later["start_twice"], (t * v[0], t * v[1]))
            k = 0 if u[0] else 1
            s = F(point[k] - earlier["start_twice"][k], u[k])
        contacts.append({"earlier_edge": ai, "later_edge": bi, "earlier_parameter": s, "later_parameter": t})
assert contacts == [{"earlier_edge": 0, "later_edge": 9, "earlier_parameter": F(0), "later_parameter": F(1)}]
assert edges[9]["atom"] == "C" and edges[9]["entry_pose"] == [-1, -1, 0] and edges[9]["entry_C_clock"] == 4
_, repeated_conflict = requirements(raw * 2)
assert repeated_conflict == {"tick": 160, "cell": (-2, 0), "prescribed": "L", "actual": "R"}


def rational_json(value):
    if isinstance(value, F):
        return int(value) if value.denominator == 1 else str(value)
    if isinstance(value, dict):
        return {k: rational_json(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [rational_json(v) for v in value]
    return value


result = {
    "status": "AUTHOR_FOUR_C_FIRST_CENTER_CONTACT_REDUCES_TO_D_OR_C_TO_C_GATE_WITH_ACTUAL_CONTROL",
    "scope": "At first center self-contact with atomic ENTRY gap four, the earlier atom is D/C and later atom is C at (-1,-1,N). A real 13-cell factor realizes D-to-second-C contact. This is not a full-pose return, renewable control, higher-C exclusion, or global theorem.",
    "all_16_exact_geometric_boxes": boxes,
    "all_23_canonical_geometries": geometries,
    "all_15_actual_atomic_roles": roles,
    "all_geometry_reductions": reductions,
    "geometry_reduction_counts": dict(reason_counts),
    "U_upper_input_0_2_minimum_five_queries": upper_queries,
    "all_45_core_age_cases": core_cases,
    "all_1725_hard_retirement_options": retirement_queries,
    "actual_control": {"word": word, "names": [G[a]["name"] for a in word], "seed": sorted(seed), "raw_length": len(raw), "raw_plus_marker_length": len(raw) + len(G[0]["marker"]), "raw_exit_pose": raw_pose, "total_C_count": clock, "all_ten_atomic_chords": edges, "all_nonadjacent_contacts": contacts, "repeat_block_first_conflict": repeated_conflict},
    "dependency_hashes": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (GP, CP, HP, AP, Path(__file__).resolve())},
}
(ROOT / "chronology_dcuv/four_C_center_contact_gate.json").write_text(json.dumps(rational_json(result), indent=2) + "\n")
print(json.dumps({"canonical_geometries": len(geometries), "reductions": dict(reason_counts), "core_age_cases": len(core_cases), "hard_retirement_options": len(retirement_queries), "actual_control_mass": len(seed), "actual_control_raw_length": len(raw)}))
