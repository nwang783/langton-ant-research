"""Assemble signed post-exit atomic maturity with exact E/N retirement endpoints."""

from collections import Counter
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
GP = ROOT / "chronology_dcuv/literal_residual_geometry.json"
MP = ROOT / "atomic_exit_bud_frozen_20261023_1325/02_atomic_exit_bud_maturation.json"
MM = ROOT / "atomic_exit_bud_frozen_20261023_1325/manifest.json"
FP = ROOT / "four_C_contact_gate_frozen_20261023_1455/manifest.json"
G = json.loads(GP.read_text())["geometry"]
M = json.loads(MP.read_text())
IDS = (0, 1, 4, 5, 6, 7, 8, 9)


def rot(p, h):
    x, y = p
    return ((x, y), (y, -x), (-x, -y), (-y, x))[h % 4]


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


expected_roles = []
for a in IDS:
    base = 0 if G[a]["name"][0] == "D" else 4 if G[a]["name"][0] == "V" else 7
    p, h = tuple(G[base]["endpoint"][:2]), 0
    for j in range(G[a]["name"].count("C") + 1):
        output = add(p, rot((1, -1), h))
        assert list(output) in G[a]["outputs"]
        expected_roles.append({"full_producer": a, "atomic_prefix_C": j, "atomic_exit": [*p, h], "bud_full_output_slot": list(output)})
        p, h = add(p, rot((0, 1), h)), (h - 1) % 4
assert expected_roles == M["roles"] and len(expected_roles) == 15
assert len(M["queries"]) == 1035 and M["C_residual_inputs"] == []
assert Counter(row["reason"] for row in M["queries"]) == {
    "SECTOR_IMPOSSIBLE": 469,
    "SIGNED_COUNT5_EXCLUDED": 359,
    "CONSUMER_PRECEDES_FULL_PRODUCER_EXIT": 207,
}
assert {row["post_atomic_exit_C"] for row in M["queries"]} == {0, 1, 2}

endpoints = []
r = (1, -1)
for heading in (1, 0):
    for base in (0, 4, 7):
        for inp in G[base]["inputs"]:
            offset = rot(inp, heading)
            head = (r[0] - offset[0], r[1] - offset[1])
            end = add(head, rot(G[base]["endpoint"][:2], heading))
            assert end[0] >= 1
            endpoints.append({"retirement_C_gap_after_A": 3 if heading == 1 else 4, "retiring_base": base, "input_slot": inp, "heading": heading, "base_entry": head, "base_exit": end})
assert len(endpoints) == 16
assert rot((0, 1), 1) == (1, 0)
assert all(rot(G[b]["endpoint"][:2], h)[0] >= 0 for h in (0, 1) for b in (0, 4, 7))

c_word = G[1]["word"][len(G[0]["word"]):]
assert c_word.startswith(G[0]["marker"])
p, h, parity, need = (0, 0), 0, set(), {}
first_read = {}
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
for tick, turn in enumerate(c_word + G[0]["marker"]):
    required = (turn == "L") ^ (p in parity)
    assert p not in need or need[p] == required
    first_read.setdefault(p, tick)
    need[p] = required
    parity.symmetric_difference_update({p})
    h = (h + (-1 if turn == "L" else 1)) % 4
    p = add(p, directions[h])
assert need[2, 0] is False
assert first_read[2, 0] == 8
assert (r[0] - (-1), r[1] - (-1)) == (2, 0)

result = {
    "status": "AUTHOR_ATOMIC_PREDECESSOR_BUD_THREE_FOUR_C_HALFPLANES_AND_INITIAL_D_FOUR_C_CONTACT_PASS",
    "scope": "Actual noninitial atomic cut A has predecessor exit bud r=(1,-1). It stays current at 3C E targets X<=0 and 4C N targets X<=0, all Y, including internal C cuts and partial consumer tails. Consequently A->C(-1,-1,N) at4C is impossible unless A is factor-first; signed1455 then leaves only factor-first D for every first4C center contact. No arbitrary enlarged atomic language or higher-C/global theorem.",
    "all_15_predecessor_atomic_roles": expected_roles,
    "signed_maturation_query_counts": M["query_counts"],
    "all_16_retiring_base_endpoints": endpoints,
    "remaining_E_to_N_C_head_increment": [1, 0],
    "target_C_gate_white_slot": [2, 0],
    "dependency_hashes": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (GP, MP, MM, FP, Path(__file__).resolve())},
}
(ROOT / "chronology_dcuv/atomic_predecessor_bud_halfplanes.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"predecessor_atomic_roles": len(expected_roles), "signed_maturity_options": len(M["queries"]), "retirement_endpoints": len(endpoints), "conclusion": "First4C center contact requires factor-first D"}))
