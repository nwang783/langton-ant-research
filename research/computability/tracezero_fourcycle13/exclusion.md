# The first nonsymmetric trace-zero four-cycle residual

2026-10-23 01:56 UTC. Frozen proof and finite certificate. Independently
signed as audit HK at02:22 UTC, including a separate complete enumeration.
This is a precise construction-family exclusion, not a global ant theorem.

Let phi be a length13 substitution on the four absolute compass directions,
whose images alternate axes and have net endpoint A d for

    A=[[0,-3],[3,0]]=3J,

where J is the counterclockwise quarter rotation. No opposite images are
identified. No heading preservation or coarse-vertex avoidance is assumed.
Then no rooted first-letter-cycle limit is a finite-support ant.

The signed spectral theorem HA supplies the reduction. Here det A=9<13,
and A^2=-9I. Parity of the geometric endpoints forces every image to start
on the axis opposite its source. A first-letter cycle therefore has length
two or four. Two-cycles have matrix A^2 with negative spectral radius and
are excluded by HA.

A four-cycle must be one of the two quarter rotations F=J or F=-J. For
either, phi^4 fixes the root and has endpoint matrix A^4=81I. The HA cone
inequality consequently becomes the exact necessary condition

    ell dot p(n)>=2||p(n)||_infinity        for EVERY n>=1,

where ell is the rational coordinate-curvature coefficient of phi (the
same coefficient applies to its fourth power). The Perron coefficient C
must vanish. The O_n(r) error disappears on dividing by81^r.

If F=-J, the first movement of a root-d limit is d, but its first13-move
prefix is phi(F^3 d), with endpoint A F^(-1)d=-3d. The cone would require
both ell dot d>=2 and -3 ell dot d>=6, impossible. This branch is excluded
analytically without enumeration.

It remains only F=J. Rotating the entire candidate by a quarter turn commutes
with A and preserves the independent-image class, so normalize root d=N.
The initial incoming heading may be E or W; the cone condition is independent
of this bounded initial-turn choice.

For source N, a raw image ends at(-3,0), starts W, and has compass counts
W5,E2,N3,S3. Choosing the five west slots among seven (including slot0)
and the three north slots among six gives300 raw words. Only56 are internally
ant-legal for at least one perpendicular incoming heading; the other244
cannot occur as any actual ant interval on any board. Every image contains
all four directions, so all four source images occur in any putative limit.
Quarter rotation gives the same56-word inventory for each other direction.
Opposite directions still choose their words INDEPENDENTLY.

The exact coefficient test covers56^4=9,834,496 controllers. Partition by
the16 possible final-direction maps G. For fixed F,G, the seam forcing is
eventually periodic; its rational contributions to C and ell are additive
over the four selected source images. The separated pair dictionaries in
cone_filter.py and finish_cone_candidates.py enumerate every C=0 combination
exactly, without a heuristic or node cap.

Exactly1,224,564 controllers have C=0. Since p(1)=N, the cone also requires
ell_y>=2, leaving20,475 controllers. For EVERY one, a literal geometric
prefix of phi^4(N) violates the cone. The latest first violation is at
prefix489. This prefix is part of the genuine root limit because phi^4
is prolongable on N. The complete canonical records, including all image
indices, rational ell, first failing prefix and point, are in
cone_only.records.json with its SHA256 in cone_only.json.

The authoritative final exclusion uses these geometric cone violations,
not a long finite ant simulation. A separate current-color check happened
to reject many remaining candidates even earlier; those diagnostics are
preserved but unnecessary for the proof.

The result includes all root cycles in this k13,A=3J four-direction class.
It does not cover larger alphabets, arbitrary changing images, nonconstant
aligned offsets, other radices, or other trace-zero matrices. The general
trace-zero four-cycle exception in HA is not erased by this one result.
