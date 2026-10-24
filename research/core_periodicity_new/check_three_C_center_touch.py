"""All n3 canonical nonproper contacts reduce to a V-family -> plain D gate.

Use exact old-core/retired-input age cuts, existing clauses and two literal controls.
No path generation or higher counted threshold.
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
JP = ROOT / "chronology_dcuv/counted_input_age_rules_complete.json"
DATA = json.loads(GP.read_text())
G = DATA["geometry"]
K = set(map(tuple, DATA["core"]))
IDS = (0, 1, 4, 5, 6, 7, 8, 9)
NEW = {a: i for i, a in enumerate(IDS)}
COUNTED = {tuple(map(int, line.split()[:8])) for line in CP.read_text().splitlines()}
HB = {tuple(map(int, line.split()[:7])) for line in HP.read_text().splitlines()}
VECTORS = {"D": (1, 1), "C": (1, 1), "V": (1, 3), "U": (0, 4)}
CENTER = (F(-1, 2), F(-1, 2))
HEAD_STEPS = ((0, 1), (1, 0), (0, -1), (-1, 0))


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


JO = {tuple(row[:3]): row[3] for row in json.loads(JP.read_text())}
assert all(JO[a, 0, 1] >= 3 for a in (0, 1))
assert all(JO[a, 1, 2] >= 3 for a in (4, 5, 6))

# Reconstruct standalone C guards, including its actual next marker.
cword = G[1]["word"][len(G[0]["word"]):]
p, h, colors, cguards = (0, 0), 0, {}, {}
for turn in cword + G[0]["marker"]:
    black = turn == "L"
    assert p not in colors or colors[p] == black
    cguards.setdefault(p, black)
    colors[p] = not black
    h = (h + (-1 if black else 1)) % 4
    p = add(p, HEAD_STEPS[h])
assert not cguards[(0, 3)] and not cguards[(1, 1)]

assert all(o[1] >= 0 for a in IDS for o in G[a]["outputs"])
assert all(G[a]["endpoint"][1] >= 1 for a in (0, 4, 7))
geometries, boxes = [], []
for a, u in VECTORS.items():
    for b, vb in VECTORS.items():
        v = rot(vb, 1)
        correction = sub(CENTER, rot(CENTER, 1))
        corners = [add(correction, (s * u[0] - t * v[0], s * u[1] - t * v[1])) for s in (0, 1) for t in (0, 1)]
        bounds = [(ceil(min(p[k] for p in corners)), floor(max(p[k] for p in corners))) for k in (0, 1)]
        boxes.append({"earlier_atom": a, "later_atom": b, "exact_corners": corners, "integer_bounds": bounds})
        denominator = det(u, v)
        assert denominator != 0
        for x in range(bounds[0][0], bounds[0][1] + 1):
            for y in range(bounds[1][0], bounds[1][1] + 1):
                if (x + y + 1) % 2:
                    continue
                w = sub(add((x, y), rot(CENTER, 1)), CENTER)
                s, t = F(det(w, v), denominator), F(det(w, u), denominator)
                if 0 <= s < 1 and 0 < t <= 1 and not (0 < s < 1 and 0 < t < 1):
                    geometries.append({"earlier_atom": a, "later_atom": b, "later_pose": [x, y, 1], "earlier_parameter": s, "later_parameter": t})
assert len(geometries) == 24

roles = []
for a in IDS:
    count = G[a]["name"].count("C")
    roles.append({"atom": G[a]["name"][0], "full_source": a, "atomic_entry": [0, 0, 0], "clock_shift": 0, "remaining_C": count})
    p, h = tuple(G[base(a)]["endpoint"][:2]), 0
    for j in range(count):
        roles.append({"atom": "C", "full_source": a, "atomic_entry": [*p, h], "clock_shift": j, "remaining_C": count - j})
        p, h = add(p, rot((0, 1), h)), (h - 1) % 4
assert len(roles) == 15


def no_new_clock_zero_output(role, cell):
    """Return a rigorous upper age for any later identity at an old cell.

    The containing full source does NOT output that cell. If it has no C,
    all later clock-zero entries are N and already strictly above the cell.
    """
    source = role["full_source"]
    x, y, h = role["atomic_entry"]
    full_cell = add((x, y), rot(cell, h))
    assert list(full_cell) not in G[source]["outputs"]
    if role["remaining_C"]:
        return 3 - role["remaining_C"], "LATER_FULL_PRODUCER_STARTS_AT_CLOCK_AT_LEAST_ONE"
    assert role["clock_shift"] == 0 and role["atom"] != "C"
    assert G[source]["name"].count("C") == 0
    assert cell[1] < G[source]["endpoint"][1]
    # Every full-source output y>=0; N zero-C entry heads only move upward.
    return 2, "CLOCK_ZERO_N_PRODUCER_CANNOT_OUTPUT_BEHIND_SOURCE_EXIT"


core_cases, retained_input_cases, lower_cases, reductions = [], [], [], []
for geometry_index, geometry in enumerate(geometries):
    a, b = geometry["earlier_atom"], geometry["later_atom"]
    p = tuple(geometry["later_pose"][:2])
    if b == "C" and p == (-1, 0):
        # Current common(2,0) is target local(0,3), before-white in literal C.
        assert rot(sub((2, 0), p), -1) == (0, 3)
        reason = "CURRENT_COMMON_OUTPUT_IN_TARGET_C_WHITE"
    elif b == "V" and p == (-3, 0):
        cell = add(p, rot((1, 2), 1))
        assert cell == (-1, -1) and cell in K
        for ri, role in enumerate(roles):
            if role["atom"] != a:
                continue
            upper, why = no_new_clock_zero_output(role, cell)
            assert upper < 3
            for target in (4, 5, 6):
                core_cases.append({"geometry_index": geometry_index, "source_role_index": ri, "target": target, "input": [1, 2], "old_core_cell": cell, "produced_age_upper": upper, "required_age_at_least": 3, "reason": why})
        reason = "OLD_CORE_SELECTED_INPUT_CANNOT_HAVE_AGE_THREE"
    elif b == "U" and p == (-4, -1):
        cell = add(p, rot((-1, 4), 1))
        assert cell == (0, 0) and cell in K
        for ri, role in enumerate(roles):
            if role["atom"] != a:
                continue
            assert 3 + role["clock_shift"] <= 4
            for target in (7, 8, 9):
                core_cases.append({"geometry_index": geometry_index, "source_role_index": ri, "target": target, "input": [-1, 4], "old_core_cell": cell, "produced_age_upper": 3 + role["clock_shift"], "required_age_at_least": 5, "reason": "ANY_CORE_TO_RESIDUAL_BIRTH_IS_SAME_FULL_SOURCE_OR_LATER"})
        reason = "OLD_CORE_UPPER_INPUT_TOO_YOUNG_EVEN_WITH_SECOND_C_SHIFT"
    elif b == "U" and p == (-2, -1):
        assert add(p, rot((-1, 4), 1)) == (2, 0)
        # Common output survives at all 3C E heads X<=1; its full-source age<=4.
        reason = "CURRENT_COMMON_OUTPUT_IS_UPPER_INPUT_OF_AGE_AT_MOST_FOUR"
    elif b == "D" and p == (-1, 0):
        cell = add(p, rot((0, 1), 1))
        assert cell == (0, 0) and cell in K
        if a in ("D", "C"):
            for ri, role in enumerate(roles):
                if role["atom"] != a:
                    continue
                upper, why = no_new_clock_zero_output(role, cell)
                assert upper < 3
                for target in (0, 1):
                    core_cases.append({"geometry_index": geometry_index, "source_role_index": ri, "target": target, "input": [0, 1], "old_core_cell": cell, "produced_age_upper": upper, "required_age_at_least": 3, "reason": why})
            reason = "OLD_CORE_D_INPUT_NOT_RELEASED_AT_CLOCK_ZERO"
        else:
            assert a in ("V", "U")
            for source in ((4, 5, 6) if a == "V" else (7, 8, 9)):
                # The old source(0,0) is the ONLY possible age-three identity here.
                assert [0, 0] in G[source]["outputs"]
                assert G[source]["name"].count("C") or G[source]["endpoint"][1] > 0
                for target in (0, 1):
                    key = (NEW[source], NEW[target], -1, 0, 1, 0, 0, 3)
                    excluded = key in COUNTED
                    if not excluded:
                        assert a == "V" and target == 0
                    lower_cases.append({"source": source, "target": target, "query": key, "reason": "SIGNED_COUNT5_EXCLUDED" if excluded else "OPEN_V_FAMILY_OLD_OUTPUT_TO_PLAIN_D"})
            reason = "OPEN_V_FAMILY_TO_PLAIN_D_GATE" if a == "V" else "OLD_U_OUTPUT_TO_D_COUNTED_EXCLUDED"
    elif a == "U" and b == "D" and p == (-1, 2):
        cell = add(p, rot((0, 1), 1))
        assert cell == (0, 2)
        reason = "RETIRED_U_INPUT_CANNOT_BE_REPRODUCED_OLD_ENOUGH_FOR_D"
    elif a == "U" and b == "V" and p == (-3, 2):
        cell = add(p, rot((1, 2), 1))
        assert cell == (-1, 1)
        reason = "RETIRED_U_INPUT_CANNOT_BE_REPRODUCED_OLD_ENOUGH_FOR_SELECTED_V"
    elif a == "U" and b == "U" and p == (-4, 1):
        cell = add(p, rot((-1, 4), 1))
        assert cell == (0, 2)
        reason = "RETIRED_U_INPUT_CANNOT_HAVE_UPPER_AGE_FIVE_AT_CLOCK_THREE"
    elif a == "U" and b == "C" and p == (-1, 2):
        assert rot(sub((0, 1), p), -1) == (1, 1)
        reason = "SOURCE_U_OUTPUT_0_1_CANNOT_RETIRE_BY_CLOCK_THREE_AND_TARGET_C_REQUIRES_WHITE"
    else:
        raise AssertionError(geometry)
    if reason.startswith("RETIRED_U_INPUT"):
        targets = (0, 1) if b == "D" else (4, 5, 6) if b == "V" else (7, 8, 9)
        required = 3 if b in ("D", "V") else 5
        for source in (7, 8, 9):
            assert list(cell) in G[source]["inputs"] and list(cell) not in G[source]["outputs"]
            if required == 3:
                assert cell[1] < G[7]["endpoint"][1]
                maximum = 2  # clock-zero later N production cannot reach behind U's exit.
            else:
                maximum = 3 - G[source]["name"].count("C")
            assert maximum < required
            for target in targets:
                retained_input_cases.append({"geometry_index": geometry_index, "source": source, "target": target, "retired_original_input": cell, "replacement_age_upper": maximum, "required_age_at_least": required})
    reductions.append({"geometry_index": geometry_index, "reason": reason})
assert len(core_cases) == 108 and len(retained_input_cases) == 24 and len(lower_cases) == 12
assert sum(row["reason"] == "OPEN_V_FAMILY_OLD_OUTPUT_TO_PLAIN_D" for row in lower_cases) == 3

# Exact upper-slot age5 premises and source-U output(0,1) age0..3 shadow.
upper_queries, shadow_queries = [], []
for source in IDS:
    for output in G[source]["outputs"]:
        for target in (7, 8, 9):
            for age in range(5):
                h = (-age) % 4
                p = sub(output, rot((-1, 4), h))
                key = (NEW[source], NEW[target], *p, h, *output, age)
                hb = (source, target, *p, h, *output)
                if age < G[source]["name"].count("C"):
                    why = "BEFORE_SOURCE_EXIT"
                elif (sum(p) + h) % 2:
                    why = "WRONG_SECTOR"
                elif hb in HB:
                    why = "SIGNED_HB_EXCLUDED"
                else:
                    assert key in COUNTED
                    why = "SIGNED_COUNT5_EXCLUDED"
                upper_queries.append({"query": key, "reason": why})
for source in (7, 8, 9):
    for age in range(4):
        h = (-age) % 4
        for target in IDS:
            for inp in G[target]["inputs"]:
                p = sub((0, 1), rot(inp, h))
                key = (NEW[source], NEW[target], *p, h, 0, 1, age)
                if age < G[source]["name"].count("C"):
                    why = "BEFORE_SOURCE_EXIT"
                elif (sum(p) + h) % 2:
                    why = "WRONG_SECTOR"
                else:
                    assert key in COUNTED
                    why = "SIGNED_COUNT5_EXCLUDED"
                shadow_queries.append({"query": key, "reason": why})
assert len(upper_queries) == 1020 and len(shadow_queries) == 276


def literal_control(word):
    raw = "".join(G[a]["word"] for a in word)
    colors, initial = {}, {}
    p, h = (0, 0), 0
    for tick, turn in enumerate(raw + G[0]["marker"]):
        black = turn == "L"
        assert p not in colors or colors[p] == black
        if p not in colors:
            initial[p] = black
        colors[p] = not black
        h = (h + (-1 if black else 1)) % 4
        p = add(p, HEAD_STEPS[h])
    seed = {p for p, black in initial.items() if black}
    assert K <= seed
    board, p, h, clock = set(seed), (0, 0), 0, 0
    identities = {q: {"kind": "entry", "cell": q} for q in seed - K}
    boundaries, edges = [], []
    for packet_index, source in enumerate(word):
        old_pose, old_clock = [*p, h], clock
        core = {add(p, rot(q, h)) for q in K}
        assert core <= board and set(identities) == board - core
        consumed = []
        for inp in G[source]["inputs"]:
            cell = add(p, rot(inp, h))
            assert cell in identities
            consumed.append({"cell": cell, "input": inp, "identity": identities.pop(cell)})
        outputs = [add(p, rot(q, h)) for q in G[source]["outputs"]]
        for output, local in zip(outputs, G[source]["outputs"]):
            assert output not in identities
            identities[output] = {"kind": "produced", "packet_index": packet_index, "source": source, "output": local, "birth_C_clock": clock}
        for turn in G[source]["word"]:
            black = p in board
            assert black == (turn == "L")
            board.symmetric_difference_update({p})
            h = (h + (-1 if black else 1)) % 4
            p = add(p, HEAD_STEPS[h])
        expected = add(tuple(old_pose[:2]), rot(tuple(G[source]["endpoint"][:2]), old_pose[2]))
        assert p == expected and h == (old_pose[2] + G[source]["endpoint"][2]) % 4
        clock += G[source]["name"].count("C")
        core = {add(p, rot(q, h)) for q in K}
        assert core <= board and set(identities) == board - core
        boundaries.append({"packet_index": packet_index, "source": source, "entry_pose": old_pose, "entry_C_clock": old_clock, "consumed": consumed, "exit_pose": [*p, h], "exit_C_clock": clock, "live_residual_identities": [{"cell": cell, "identity": identity} for cell, identity in sorted(identities.items())]})
    raw_pose = [*p, h]
    for turn in G[0]["marker"]:
        black = p in board
        assert black == (turn == "L")
        board.symmetric_difference_update({p})
        h = (h + (-1 if black else 1)) % 4
        p = add(p, HEAD_STEPS[h])
    p, h, clock = (0, 0), 0, 0
    for packet_index, source in enumerate(word):
        for atom in [G[source]["name"][0]] + ["C"] * G[source]["name"].count("C"):
            start = add((2 * p[0], 2 * p[1]), rot((-1, -1), h))
            old_pose, old_clock = [*p, h], clock
            step = (0, 1) if atom == "C" else VECTORS[atom]
            p = add(p, rot(step, h))
            h = (h - int(atom == "C")) % 4
            clock += int(atom == "C")
            end = add((2 * p[0], 2 * p[1]), rot((-1, -1), h))
            edges.append({"atom": atom, "packet_index": packet_index, "entry_pose": old_pose, "entry_C_clock": old_clock, "start_twice": start, "end_twice": end})
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
                t0, t1 = F(-w[k], v[k]), F(u[k] - w[k], v[k])
                low, high = max(F(0), min(t0, t1)), min(F(1), max(t0, t1))
                if low > high:
                    continue
                t = low
                point = add(later["start_twice"], (t * v[0], t * v[1]))
                k = 0 if u[0] else 1
                s = F(point[k] - earlier["start_twice"][k], u[k])
            contacts.append({"earlier_edge": ai, "later_edge": bi, "earlier_parameter": s, "later_parameter": t, "earlier_path_parameter": ai + s, "later_path_parameter": bi + t})
    first_time = min(row["later_path_parameter"] for row in contacts)
    first_contacts = [row for row in contacts if row["later_path_parameter"] == first_time]
    canonical = set()
    for row in first_contacts:
        ai, bi, s, t = row["earlier_edge"], row["later_edge"], row["earlier_parameter"], row["later_parameter"]
        if s == 1:
            ai, s = ai + 1, F(0)
        if t == 0:
            bi, t = bi - 1, F(1)
        canonical.add((ai, bi, s, t))
    assert len(canonical) == 1
    ai, bi, s, t = next(iter(canonical))
    assert edges[ai]["atom"] == "V" and edges[bi]["atom"] == "D" and s == 0 and t == 1
    assert edges[bi]["entry_C_clock"] - edges[ai]["entry_C_clock"] == 3
    assert rot(sub(tuple(edges[bi]["entry_pose"][:2]), tuple(edges[ai]["entry_pose"][:2])), -edges[ai]["entry_pose"][2]) == (-1, 0)
    assert (edges[bi]["entry_pose"][2] - edges[ai]["entry_pose"][2]) % 4 == 1
    selected = boundaries[-1]["consumed"]
    assert len(selected) == 1 and selected[0]["identity"]["kind"] == "produced"
    assert selected[0]["identity"]["source"] == 6 and selected[0]["identity"]["output"] == [0, 0]
    return {"word": word, "names": [G[a]["name"] for a in word], "seed": sorted(seed), "entry_mass": len(seed), "raw_length": len(raw), "raw_plus_marker_length": len(raw) + len(G[0]["marker"]), "raw_exit_pose": raw_pose, "all_full_packet_identity_boundaries": boundaries, "atomic_chords": edges, "all_nonadjacent_contacts": contacts, "first_contact_path_time": first_time, "canonical_first_contact": {"earlier_edge": ai, "later_edge": bi, "earlier_parameter": s, "later_parameter": t}}


controls = [literal_control((6, 5, 0)), literal_control((0, 6, 5, 0))]
assert [control["entry_mass"] for control in controls] == [8, 9]


def rational_json(value):
    if isinstance(value, F):
        return int(value) if value.denominator == 1 else str(value)
    if isinstance(value, dict):
        return {k: rational_json(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [rational_json(v) for v in value]
    return value


result = {
    "status": "AUTHOR_THREE_C_NONPROPER_FIRST_CONTACT_REDUCES_TO_V_FAMILY_PLAIN_D_GATE",
    "scope": "All24 canonical n3 nonproper contacts reduce to earlier V base, later plain D(-1,0,E), old source output(0,0). Source full V/VC/VCC remains individually open; VCC sharp controls are literal. No next complete packet, factor-first/second restriction, no-contact or global claim is assumed.",
    "all_16_exact_geometric_boxes": boxes,
    "all_24_canonical_nonproper_geometries": geometries,
    "all_15_actual_source_roles": roles,
    "geometry_reductions": reductions,
    "geometry_reduction_counts": dict(Counter(row["reason"] for row in reductions)),
    "all_108_old_core_age_cases": core_cases,
    "all_24_retired_U_input_age_cases": retained_input_cases,
    "all_12_old_source_0_0_to_D_queries": lower_cases,
    "all_1020_upper_minus1_4_age_five_queries": upper_queries,
    "all_276_U_output_0_1_early_retirement_queries": shadow_queries,
    "two_actual_boundary_controls": controls,
    "dependency_hashes": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (GP, CP, HP, AP, JP, Path(__file__).resolve())},
}
(ROOT / "chronology_dcuv/three_C_center_touch.json").write_text(json.dumps(rational_json(result), indent=2) + "\n")
print(json.dumps({"canonical_nonproper_geometries": len(geometries), "core_age_cases": len(core_cases), "retired_input_cases": len(retained_input_cases), "old_source_queries": len(lower_cases), "upper_age_queries": len(upper_queries), "U_output_shadow_queries": len(shadow_queries), "actual_control_masses": [c["entry_mass"] for c in controls]}))
