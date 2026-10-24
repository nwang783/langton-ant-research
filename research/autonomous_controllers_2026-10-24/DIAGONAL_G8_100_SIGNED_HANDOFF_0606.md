# Signed diagonal growth-eight remainder: one hundred open interfaces

24 October 2026, 06:06 UTC. This is a binding handoff, not a new exclusion.

## Exact scope and current conclusion

Consider a complete WHITE translating Langton-ant front with actual full drift
(2,-2), or a genuinely rotated/translated version, and growth g=8. WHITE means
that every physical drift-orbit complete history starts R and alternates R/L.
All initial-support realizations remain finite under the retained finite-overlap
theorem. No whole-front visit cap, period bound, normal width bound, reflected
rule, or truncated field is being imposed.

The signed read-footprint-minimum cover and subsequent finite local obstructions
leave exactly 100 necessary OPEN interfaces, with exact IDs retained in
`diagonal_selected_pair_exclusions_certificate.json`:

- Four one-minimum-singleton interfaces.
- Twenty-two interfaces with one quadruple corner on the forced single-used F4 circle.
- Seventy-four interfaces with two quadruple corners on that circle.

No one of these interfaces is claimed to have a physical completion. The region
above the named rows remains unbounded. Other permitted drift types also remain
open. In particular this is NOT a proof that g>=12, not a classification of all
translating controllers, and not an attraction theorem.

## Set-accounted reduction and stronger all-growth statement

The complete lower cover leaves 227 all-growth interfaces. The nine cyclic-E
cases are impossible at g8 by the independently signed all-cap cyclic-E theorem.
The later two skipped-middle cases are separately impossible at every growth.
The first-N rules reject 68 of the 227: their overlap with the cyclic nine is
exactly seven, and with the skipped two exactly zero. This leaves 155 g8 cases.
The mixed-corner cover removes twelve explicit cases, leaving 143. The selected
pair cover removes forty-three further explicitly disjoint cases, leaving 100.
Every subtraction is backed by retained ID sets and their checked intersections.

The mixed-corner theorem has an ALL-GROWTH structural consequence: whenever both
minimum-row singleton classes are present in a complete WHITE full diagonal-two
front, the next two cells both have complete history SSN or SSNS. They therefore
form a genuine single-used first-R-departure F4 circle with the two singletons.
The one-singleton branch is not covered by this structural consequence.

## Mandatory correction and independent audit status

The original mixed-corner note's paragraph describing its 24 closed components
contains a winding-sign prose error. The mandatory separate correction
`DIAGONAL_MIXED_CORNER_WINDING_CORRECTION.md` is part of its statement: the frozen
certificate correctly gives winding -1, so each cycle directly forces 4=-P.
The original is preserved and MUST NOT be cited without that correction.

Independent audits reconstruct all 4,692 mixed helper pairs and all 2,896 selected
helper pairs from complete port-count bounds, with outside ports open. The latter
cover includes 2,846 genuine first-return skipped-rank witnesses (1,544 length
four and 1,302 length eight), 22 negative event cycles, and 28 full-inventory
growth-eight residue-budget failures. The ten admissible full parity vectors
are all retained; a named odd subset is never substituted for a physical wake.

The two new independent reports are PASS, with exact hashes below. Neither audit
uses a solver UNSAT claim, nor the missing historical width-ten exhaustion.

## Exact dependency hashes

- `DIAGONAL_READ_MINIMUM_COMPLETE_INTERFACE.md`: `77fde6d49196db1c3074c9db7adfa1abda3a80500213f0c0d712bdeb0505b274`.
- `certify_diagonal_read_minimum.json`: `a4de122acffd766aee76c6676bb247f02c8754fc9ecfd5949cd20c5478929c7f`.
- `FIRST_N_RETURN_RULES_DIAGONAL_REDUCTION.md`: `961b19e632cae7084d29cae71bdc9aa3400bbe655694cd69b3b10fd776c66c00`.
- `first_N_return_rules_certificate.json`: `948b8dcb5b36bcc70ea1da36d2bac51c47ee54528582bbfb19c808944369dfa9`.
- `ONE_SINGLETON_FOUR_STEP_SKIPPED_MIDDLE_EXCLUSION.md`: `fb198c975d85b70f8f931db303f48fff183c8ba6c79271fb8d083ec4f811a010`.
- `CYCLIC_E_G8_SIGNED_HANDOFF_0442.md`: `d840be7b7b6ef5f70e951a54d0561019ba907059bc32a7d4d384f442e2072bee`.
- `DIAGONAL_TWO_SINGLETONS_FORCE_FIRST_CIRCLE.md`: `3efd718ef7613128f71b76114837cf7e4641d78a4388809c180b450cc73395dd`.
- `DIAGONAL_MIXED_CORNER_WINDING_CORRECTION.md`: `81383bd15b4bead3dc87df3d1616ad3fe4854db0a8271a358e5d23faab70d8b9`.
- `diagonal_mixed_corner_exclusion_certificate.json`: `89d65aaf7f0d492c81094c064e9182d936e8c36466ad20e6d3eaf7183e01e89d`.
- `DIAGONAL_SELECTED_PAIR_G8_EXCLUSIONS.md`: `e2e81e31f57b715452227e34f221a54937465fa4cf931440dca002c75d6413a7`.
- `diagonal_selected_pair_exclusions_certificate.json`: `85fab3456d7f7285e67171f88852fa3e5b5e7281fa2feaa91f63988b3a5e3cad`.
- `../audits/check_diagonal_mixed_corner_independent.py`: `c7d9a7cd62c2189a81778791efef5e6ba1b91277366560719ee048e881089e95`.
- `../audits/check_diagonal_mixed_corner_independent.json`: `7573760d0256aa1f0b443f55f8226e36d71e9cf328002d46f045fd9ffcde830e`.
- `../audits/check_diagonal_selected_pair_independent.py`: `3b676b2bff5a5975c929e84852a499fa2ffd2360dca00f262854718f0759eadf`.
- `../audits/check_diagonal_selected_pair_independent.json`: `eb6317a272f3a573feebd3a9c147d862b04f9ab2a52d412c917ea9e66e5940dc`.
- `../audits/check_first_N_rules_independent.json`: `61f072f4f95ae663ff2654124039f4e47e274d58c62642c66d8b67acfbd8270c`.
- `../audits/check_diagonal_read_minimum_cover_independent.json`: `9d8ef1d347591cf209339aea28b9e4b07b040d23ae84204ce52461d0f29e9a73`.
- `../audits/check_one_singleton_skip_independent.json`: `11beb4ad096149b958246bfe8399a26e5eb92daa98276cdb668bbbe1d3d70062`.
- `../audits/check_g8_two_row_covers_independent.json`: `e1d595f2e56726f41cf3efa7e8baaccd87f0949ecd2ace9bdad88e0c78b3670a`.
