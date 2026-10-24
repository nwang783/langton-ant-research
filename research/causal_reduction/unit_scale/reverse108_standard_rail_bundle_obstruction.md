# The prepared108 rewriter cannot be funded by a parallel bundle of standard wakes

Author-only profile proof, 2026-10-23. This is about the ONE literal P108 word in `reverse108_prepared_control.json`, not arbitrary nonstandard rewriters. No finite endcap is synthesized and no general highway conclusion follows.

## Positive finite-board family

`certify_reverse108_prepared_family.py` reconstructs P with complex headings and proves, for every n>=1, that P^n is internally ant-legal on its minimal input board. Its exact cardinalities are

- input black11n+13;
- output black3n+13;
- complete read support23n+19;
- complete XOR12n+20.

The output pose is(-2n,6-2n,W). The proof records each read as representative a plus l(-2,-2), with internal time t. At cell a+k(-2,-2), retain exactly events with0<=k-l<n and order them by t-108l. Each orbit's offset span is at most2. For n>=3, its histories split into two fixed endpoint fringes and a stable middle interval. The frozen tables verify all three parts; n1 and2 are checked directly. Thus these are all-n whole-field formulas, not extrapolated numerical counts.

## Why more disjoint standard rails do not supply its input

A mature standard NE or SW front has a complete read band of11 consecutive normal coordinates x-y, with both parity classes at each normal. Both extreme normals have black output in both parity classes.

Consequently two sequential standard WHITE-input writers cannot have overlapping bulk read bands. The second band's11-normal interval, if it overlaps the first interval of the same length, contains at least one first-band endpoint unless the intervals are identical; identical intervals contain both. That endpoint is black and belongs to the second writer's required-white read set. This is a literal first-color contradiction. Fixed finite endpoint work does not alter the remote bulk conclusion.

P108's required-black classes span only11 consecutive normal coordinates. Such an interval can meet at most two pairwise disjoint11-normal writer bands. Any remaining standard rails supply none of its required black cells and can only add unwanted black at its required-white cells. It therefore suffices to compare one rail or two rails.

`check_reverse108_parallel_rail_bundle.py` performs that exact comparison. Proper half-turn symmetry normalizes one contributing rail to NE, leaving NE/NE and NE/SW pairs; both possible consumer orientations are retained. All translations are derived by matching one required black class to the first rail, then a still-missing black class to the second rail. This is a complete finite difference set, not a displacement cutoff. Sector conservation is imposed, and every candidate second writer's full read set must avoid the first black wake.

All four one-rail orientation cases fail. The59 geometrically possible anchored two-rail interfaces also fail, each with explicit missing-black and/or polluted-white witnesses. Hence no finite parallel bundle of white-written standard NE/SW wakes supplies the complete prepared bulk input of P108, in either direction and with any longitudinal/transverse phases.

This does not exclude intersecting nonparallel writers, a writer that itself rewrites prepared bulk, an additional nonstandard bulk phase, or initial black fuel growing linearly with n. It also does not infer an actual producer itinerary from an abstract union of profiles.

Artifacts: `reverse108_prepared_family.json`, `reverse108_parallel_rail_bundle.json`, their generators, and the original `reverse108_prepared_control.json`.

## Exact finite profile data

Orbit coordinates are `(x-y, x mod 2)`. The NE writer starts at `(0,0,E)`;
its read normals are `[-7,3]`, both parity classes at every normal, and its
black output is

    (-7,0), (-7,1), (-6,1), (-5,1), (-3,0), (-2,0),
    (-1,1), (0,0), (1,0), (2,1), (3,0), (3,1).

The SW writer is the proper half-turn: negate the normal and preserve the
parity. P108's SW presentation starts at `(0,6,W)`, with black requirements

    (-12,1), (-11,0), (-10,0), (-8,1), (-7,1), (-6,0),
    (-5,1), (-4,1), (-3,0), (-2,0), (-2,1).

Every compared entry heading is E or W, so conserved-sector translations
have even coordinate sum, equivalently even normal shift. The longitudinal
quotient retains both x parities. After normalizing the first writer to NE,
the two-rail counts by `(second writer, consumer direction)` are
`(NE,SW):18`, `(NE,NE):15`, `(SW,SW):14`, `(SW,NE):12`, totaling 59.

A separate analytic lift under preparation is intended to apply this table
to any fixed finite number of actual standard flights and fixed finite caps.
For that lift, finite endpoints and the bounded intersections of nonparallel
strips must be discarded explicitly; the profile table itself is not a
certificate for a finite producer itinerary. The table and lift remain
pending independent audit as of 2026-10-23 11:31 UTC.

## Independent signoff, 2026-10-23 11:35 UTC

`../../audits/check_reverse108_rail_bundle_independent.py/json` independently
reconstruct both literal writer profiles, all P108 endpoint histories, all four
single-orientation cases and all 59 pair cases. The exact all-n complete-field
formulas and the finite bulk-bundle exclusion are signed. The later finite-
flight/cap lifting theorem is separate and is not included in this signoff.
