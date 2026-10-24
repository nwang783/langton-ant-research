"""Check the finite exact angle-order cases for the first-contact horizon.

The all-length first-contact/simple-loop proof is in the accompanying note.
"""

from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
DEPENDENCY = ROOT / "atomic_center_turning_frozen_20261023_1400/manifest.json"
ALPHA_RANK = {"U": 0, "V": 1, "D": 2, "C": 2}

cases = []
excluded = []
for a, ra in ALPHA_RANK.items():
    for b, rb in ALPHA_RANK.items():
        sign = (ra > rb) - (ra < rb)
        for n in range(8):
            # pi < n*pi/2 + alpha(a)-alpha(b) < 3*pi,
            # with |alpha(a)-alpha(b)| <= pi/4 and exact alpha ordering.
            allowed = n in (3, 4, 5) or n == 2 and sign > 0 or n == 6 and sign < 0
            row = {
                "initial_atom": a,
                "final_atom": b,
                "entry_C_clock_gap": n,
                "alpha_difference_sign": sign,
                "final_heading_relative_to_initial": (-n) % 4,
            }
            if allowed:
                assert 2 <= n <= 6
                cases.append(row)
            else:
                excluded.append(row)

assert len(cases) == 58
assert sum(row["entry_C_clock_gap"] == 2 for row in cases) == 5
assert sum(row["entry_C_clock_gap"] == 6 for row in cases) == 5
assert all(sum(row["entry_C_clock_gap"] == n for row in cases) == 16 for n in (3, 4, 5))

result = {
    "status": "AUTHOR_FIRST_CENTER_CONTACT_TWO_THROUGH_SIX_C_ENTRY_HORIZON_PASS",
    "scope": "The earliest repeated center point closes a simple polygonal subarc. The two endpoint atoms' ENTRY C clocks differ by 2..6, not a word-length or head-box bound. No literal collision contradiction follows.",
    "alpha_values_in_exact_increasing_order": [["U"], ["V"], ["D", "C"]],
    "surviving_atom_pair_clock_cases": cases,
    "excluded_cases_for_n_zero_through_seven": excluded,
    "all_n_at_least_seven_excluded_by": "L >= 7*pi/2 - pi/4 = 13*pi/4 > 3*pi",
    "dependency_hashes": {
        str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in (DEPENDENCY, Path(__file__).resolve())
    },
}
(ROOT / "chronology_dcuv/first_center_contact_C_horizon.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"surviving_finite_cases": len(cases), "entry_C_clock_gap": [2, 6], "status": result["status"]}))
