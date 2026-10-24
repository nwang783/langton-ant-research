"""Check all seven actual C roles and three target V-family tails at gap three."""

from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
GP = ROOT / "chronology_dcuv/literal_residual_geometry.json"
CP = ROOT / "chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv"
AP = ROOT / "atomic_common_4C_frozen_20261023_1344/manifest.json"
BP = ROOT / "v1_DC_age3_boundary_frozen_20261023_1244/manifest.json"
G = json.loads(GP.read_text())["geometry"]
IDS = (0, 1, 4, 5, 6, 7, 8, 9)
NEW = {a: i for i, a in enumerate(IDS)}
COUNTED = {tuple(map(int, line.split()[:8])) for line in CP.read_text().splitlines()}


def rot(p, h):
    x, y = p
    return ((x, y), (y, -x), (-x, -y), (-y, x))[h % 4]


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def base(a):
    return 0 if G[a]["name"][0] == "D" else 4 if G[a]["name"][0] == "V" else 7


rows = []
for a in IDS:
    position = tuple(G[base(a)]["endpoint"][:2])
    heading = 0
    for j in range(G[a]["name"].count("C")):
        output = add(position, rot((2, 0), heading))
        assert list(output) in G[a]["outputs"]
        for b in (4, 5, 6):
            full_position = add(position, rot((-1, 0), heading))
            full_heading = (heading + 1) % 4
            age = 3 + j
            key = (NEW[a], NEW[b], *full_position, full_heading, *output, age)
            assert (sum(full_position) + full_heading) % 2 == 0
            excluded = key in COUNTED
            if not excluded:
                assert a == 1 and j == 0 and b in (4, 5)
                assert full_position == (0, 1) and full_heading == 1 and output == (3, 1) and age == 3
            rows.append({
                "full_source": a,
                "full_source_name": G[a]["name"],
                "C_atom_number": j + 1,
                "atomic_birth_clock_shift": j,
                "atomic_entry_in_full_frame": [*position, heading],
                "protected_full_source_output": output,
                "target_full_packet": b,
                "target_full_name": G[b]["name"],
                "target_pose_in_full_frame": [*full_position, full_heading],
                "atomic_entry_C_gap": 3,
                "full_source_included_C_age": age,
                "counted_query": key,
                "reason": "SIGNED_COUNT5_EXCLUDED" if excluded else "SIGNED_1244_DC_MUST_BE_FACTOR_FIRST",
            })
        position = add(position, rot((0, 1), heading))
        heading = (heading - 1) % 4

assert len(rows) == 21
assert sum(row["reason"] == "SIGNED_COUNT5_EXCLUDED" for row in rows) == 19
assert sum(row["reason"] == "SIGNED_1244_DC_MUST_BE_FACTOR_FIRST" for row in rows) == 2

endpoints = []
for b in (0, 4, 7):
    for inp in G[b]["inputs"]:
        offset = rot(inp, 1)
        position = (2 - offset[0], -offset[1])
        endpoint = add(position, rot(G[b]["endpoint"][:2], 1))
        assert endpoint[0] >= 2
        endpoints.append({"consuming_base": b, "input": inp, "entry": position, "exit": endpoint})
assert all(rot(G[b]["endpoint"][:2], 1)[0] > 0 for b in (0, 4, 7))
assert len(endpoints) == 8

result = {
    "status": "AUTHOR_C_FIRST_E_THREE_C_CROSSING_INITIAL_DC_CLASSIFICATION_PASS",
    "scope": "Actual C atom at (0,0,N), later V base at (-1,0,E), entry C gap three. Old source common output survives until target by signed atomic maturity and E zero-cone; all 21 protected-source queries leave only the factor-first DC source and V/VC target tails. No first-contact premise needed for this explicit E3 statement.",
    "all_21_role_tail_cases": rows,
    "all_eight_E_retiring_base_endpoints": endpoints,
    "dependency_hashes": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (GP, CP, AP, BP, Path(__file__).resolve())},
}
(ROOT / "chronology_dcuv/C_first_E_crossing.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"role_tail_cases": len(rows), "existing_counted_exclusions": 19, "signed_boundary_cases": 2, "retiring_E_endpoints": len(endpoints)}))
