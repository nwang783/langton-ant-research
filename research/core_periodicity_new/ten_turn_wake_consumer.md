# The ten-turn diagonal consumer cannot recycle same-sector standard rails

Status: independently audited on 2026-10-22 at 21:10 UTC. The independent checker derives the wake directly from the pinned standard word and enumerates every subset of the16 helpful rail profiles, using a different union-enumeration algorithm. This is not a general classification of periodic consumers.

The symbolic analysis identified

    D = LLLLRLRRRR

as a recurrent ten-turn packet, with restored heading, drift(1,1) from heading north, and zero black-mass change. It can consume one diagonal black line while writing a parallel line, so it was a concrete candidate for arbitrarily long nonstandard activity after a long standard flight.

## Single-rail obstruction, with arbitrary finite cap

At origin with heading north, the four displacement classes under drift(1,1), indexed by transverse coordinate t=x-y, have stabilized ordered read lists

    t=-1: L,
    t= 0: RLRL,
    t= 1: RLRL,
    t= 2: R.

Thus an infinite D tail needs a fully black line at t=-1 and fully white lines at0,1,2 before the consumer reaches them.

The canonical settled standard wake has writer heading west and invariant sector1. Its black classes under drift(2,2) are

    (-3,0),(-3,1),(-2,1),(-1,0),(0,0),(1,1),
    (2,0),(3,0),(5,1),(6,1),(7,0),(7,1),

where the second coordinate is x mod2. To put a north-heading D consumer in that same sector, its starting translation must have odd transverse coordinate. Its required-L line then lies at an even transverse coordinate. Every even transverse line of the standard wake has at most one of its two longitudinal parities black. Therefore infinitely many required-L cells are missing. No finite startup cap can repair this.

Rotating both writer and consumer changes nothing. Reversing their common diagonal direction gives the reflected wake profile and the same obstruction. A cyclic phase of D cannot evade the conclusion, since advancing finitely many steps reaches phase0 with only a finite change to the cap.

## Arbitrary unions of parallel same-sector standard wakes

Normalize the D consumer to p=(0,-1), heading north, so its sector agrees with the canonical writer. Use D^2 with drift(2,2). Its eight stable first-read classes require black at

    (0,0),(0,1),

and white at

    (1,0),(1,1),(2,0),(2,1),(3,0),(3,1).

Every same-sector standard rail is either the canonical profile or its half-turn, shifted by an even transverse offset and either x parity. Only16 profiles hit one of the two required-black classes. The exact checker enumerates these derived offsets, not an arbitrary bounded spatial window.

For each of the64 possible allowed white-error subsets A, take the union of ALL helpful rail profiles whose white mask is contained in A. This maximal union covers at least as many required-black classes as any union with white errors contained in A. Every such maximal union has at least2 total guard mismatches. Hence every union of same-sector parallel standard bilateral rails has at least2 mismatches per D^2 block. Empty union attains2, so the bound is exact.

The eight first-read witnesses are chosen at the maximal longitudinal phase of each orbit, with earliest phase breaking ties. They are distinct across all two-period blocks, and are genuine first visits within the factor. The checker records their coordinates and verifies coordinate widths at most9.

## Full chronological-history consequence

Use the previously audited standard_block_union_history.md decomposition: after r actual legal standard-power blocks and a other individual updates from initial mass m, the COMPLETE board differs from a union of r finite standard rails at at most

    e <= m+a+110r

cells. The existing endpoint/crossing calculation applies unchanged because the new witness widths are no larger than the previously audited width9. Delete at most32r two-period indices to ensure that every finite rail acts either as a full parallel bilateral profile or as the empty set on all eight witnesses; perpendicular-rail intersections are among the deleted indices.

For a subsequent D^N factor, put n=floor(N/2). The disjoint witness guards give

    2 max(0,n-32r) <= e,
    2n <= m+a+174r,
    N <= m+a+174r+1.

Thus arbitrarily long earlier standard flights, with a fixed number of legal standard blocks and fixed other work, cannot power arbitrarily long D consumption. This retains all past debris through the explicit error ledger. It does not bound the number of standard blocks or other updates in a general orbit.

Reproduction: check_ten_turn_wake_consumer.py, its JSON, and ten_turn_wake_consumer.log. The single-rail incompatibility is also directly returned by the existing exact arbitrary-finite-cap orbit oracle.

Canonical provenance is bound explicitly in the source by the W104 SHA256 and by recomputing the odd drift classes from the literal word. The independent audit artifact is ../audits/check_ten_turn_consumer_independent.py and its JSON.
