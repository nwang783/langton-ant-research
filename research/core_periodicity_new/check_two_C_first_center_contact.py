"""Exclude all eight two-C canonical first-contact geometries by a core-age cut.

Exact geometric bounds come from contact parallelograms. No path search.
"""

from fractions import Fraction
from math import ceil, floor
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
GP = ROOT / "chronology_dcuv/literal_residual_geometry.json"
JP = ROOT / "chronology_dcuv/counted_input_age_rules_complete.json"
HP = ROOT / "first_center_contact_frozen_20261023_1412/manifest.json"
AP = ROOT / "atomic_common_4C_frozen_20261023_1344/manifest.json"
DATA = json.loads(GP.read_text())
G = DATA["geometry"]
K = set(map(tuple, DATA["core"]))
MINIMUM = {(a, x, y): age for a, x, y, age in json.loads(JP.read_text())}
IDS = (0, 1, 4, 5, 6, 7, 8, 9)
STEPS = {"D": (1, 1), "C": (1, 1), "V": (1, 3), "U": (0, 4)}
RANK = {"D": 2, "C": 2, "V": 1, "U": 0}
CENTER = (Fraction(-1, 2), Fraction(-1, 2))


def rot(p, h):
    x, y = p
    return ((x, y), (y, -x), (-x, -y), (-y, x))[h % 4]


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def cross(p, q):
    return p[0] * q[1] - p[1] * q[0]


def base(a):
    return 0 if G[a]["name"][0] == "D" else 4 if G[a]["name"][0] == "V" else 7


geometries = []
bounding_boxes = []
heading = 2
for a, va in STEPS.items():
    for b, vb0 in STEPS.items():
        if RANK[a] <= RANK[b]:
            continue  # The signed first-contact n=2 angle refinement is strict.
        vb = rot(vb0, heading)
        correction = sub(CENTER, rot(CENTER, heading))
        corners = [add(correction, (s * va[0] - t * vb[0], s * va[1] - t * vb[1])) for s in (0, 1) for t in (0, 1)]
        bounds = [(ceil(min(p[k] for p in corners)), floor(max(p[k] for p in corners))) for k in (0, 1)]
        bounding_boxes.append({"earlier_atom": a, "later_atom": b, "integer_bounds": bounds, "exact_parallelogram_corners": corners})
        determinant = cross(va, vb)
        assert determinant != 0  # Unequal alpha means these S-heading chords are not parallel.
        for x in range(bounds[0][0], bounds[0][1] + 1):
            for y in range(bounds[1][0], bounds[1][1] + 1):
                if (x + y + heading) % 2:
                    continue
                later_center = add((x, y), rot(CENTER, heading))
                displacement = sub(later_center, CENTER)
                s = Fraction(cross(displacement, vb), determinant)
                t = Fraction(cross(displacement, va), determinant)
                # Outgoing earlier atom, incoming later atom: canonical first-contact convention.
                if 0 <= s < 1 and 0 < t <= 1:
                    assert s == 0
                    if b == "V":
                        assert (x, y) == (0, 2)
                        chosen_input = (1, 2)
                    else:
                        assert b == "U" and (x, y) in ((-1, 1), (-1, 3))
                        chosen_input = (0, 2) if y == 1 else (-1, 4)
                    required_cell = add((x, y), rot(chosen_input, heading))
                    assert required_cell in K
                    geometries.append({
                        "earlier_atom": a,
                        "later_atom": b,
                        "later_pose": [x, y, heading],
                        "earlier_chord_parameter": s,
                        "later_chord_parameter": t,
                        "chosen_later_input": chosen_input,
                        "input_cell_in_earlier_atomic_core": required_cell,
                    })
assert len(geometries) == 8

roles = []
for a in IDS:
    roles.append({"atom": G[a]["name"][0], "full_source": a, "atomic_entry_in_full_source_frame": [0, 0, 0], "atomic_entry_clock_shift": 0, "remaining_source_C": G[a]["name"].count("C")})
    p = tuple(G[base(a)]["endpoint"][:2])
    h = 0
    for j in range(G[a]["name"].count("C")):
        roles.append({"atom": "C", "full_source": a, "atomic_entry_in_full_source_frame": [*p, h], "atomic_entry_clock_shift": j, "remaining_source_C": G[a]["name"].count("C") - j})
        p = add(p, rot((0, 1), h))
        h = (h - 1) % 4
assert len(roles) == 15

cases = []
for geometry_index, geometry in enumerate(geometries):
    for role_index, role in enumerate(roles):
        if geometry["earlier_atom"] != role["atom"]:
            continue
        a = role["full_source"]
        px, py, h = role["atomic_entry_in_full_source_frame"]
        z = geometry["input_cell_in_earlier_atomic_core"]
        in_full_frame = add((px, py), rot(z, h))
        assert list(in_full_frame) not in G[a]["outputs"]
        targets = (4, 5, 6) if geometry["later_atom"] == "V" else (7, 8, 9)
        for target in targets:
            slot = geometry["chosen_later_input"]
            assert list(slot) in G[target]["inputs"]
            minimum = MINIMUM[target, *slot]
            assert minimum > 2
            # Any identity born after the full source exits has age at most this.
            maximum_age = 2 - role["remaining_source_C"]
            assert maximum_age <= 2 < minimum
            cases.append({
                "geometry_index": geometry_index,
                "actual_source_role_index": role_index,
                "full_source": a,
                "full_source_name": G[a]["name"],
                "earlier_atomic_core_cell": z,
                "same_cell_in_full_source_frame": in_full_frame,
                "not_in_full_source_outputs": True,
                "target_full_packet": target,
                "target_full_name": G[target]["name"],
                "target_input_slot": slot,
                "signed_produced_age_minimum": minimum,
                "remaining_source_C_at_earlier_atomic_cut": role["remaining_source_C"],
                "later_producer_age_upper_bound": maximum_age,
                "reason": "CORE_CELL_NOT_RESIDUAL_AT_SOURCE_AND_NOT_RELEASED_BY_SAME_FULL_PRODUCER; ANY_LATER_FRESH_IDENTITY_TOO_YOUNG",
            })
assert len(cases) == 99


def rational_json(value):
    if isinstance(value, Fraction):
        return int(value) if value.denominator == 1 else str(value)
    if isinstance(value, dict):
        return {key: rational_json(v) for key, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [rational_json(v) for v in value]
    return value


result = {
    "status": "AUTHOR_TWO_C_FIRST_CENTER_CONTACT_CORE_AGE_EXCLUSION_PASS",
    "scope": "Actual atomic cuts in a complete recurrent-eight factor. Every canonical first-contact geometry with entry C gap two is impossible by a required old-core cell that is absent from its same full source output mask and therefore too young at the later true input. No initial identity exception survives the core-to-residual transition. No higher-C or global no-contact claim.",
    "all_five_exact_geometric_bounding_boxes": bounding_boxes,
    "all_eight_canonical_two_C_contact_geometries": geometries,
    "all_15_actual_atomic_source_roles": roles,
    "all_99_source_role_target_tail_core_age_cases": cases,
    "dependency_hashes": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (GP, JP, HP, AP, Path(__file__).resolve())},
}
(ROOT / "chronology_dcuv/two_C_first_center_contact.json").write_text(json.dumps(rational_json(result), indent=2) + "\n")
print(json.dumps({"exact_boxes": len(bounding_boxes), "canonical_geometries": len(geometries), "actual_source_roles": len(roles), "core_age_cases": len(cases)}))
