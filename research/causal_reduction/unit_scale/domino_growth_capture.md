# All-parameter highway capture of the capped growth seed

23 October 2026, 06:43 UTC. Independently signed exact all-parameter/all-future certificate.
This closes one specified seed family, not any general finite-support class.

## Statement

For every integer r >= 20, start the standard R-white/L-black ant at (0,0,E)
with exactly

    J_r = {(x,0): 0 <= x <= 2r} union {(-1,1)}

black. At time 60r+777 the ant is at (2r+2,7,N), after which its turns repeat
the following 104-letter word forever, with displacement (-2,2) per period:

    LRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLR

Thus the signed growth excursion H_r in `axial_domino_transport.md` does occur,
but its actual continuation is not a renewable growing countermodel. The
r >= 20 threshold is sufficient only; no minimal-threshold claim is made.

## Explicit finite candidate

The certificate JSON supplies all literal cap strings and their order. The
seven repeated arms are respectively

    LRRL, RLLR, LRRL,
    RRRLLLLRLLLLRLRRRRLR, RRRRLRRRRLLLLRLLLLRL,
    RLLR, LRRL,

with counts r, r+1, r, r+1, r-2, r-2, r-2. The fixed intervening caps have
lengths 0,4,4,24,260,204,4; the final fixed segment has length309. Direct
geometric summation gives total duration60r+777 and the stated final pose.
The candidate was extracted from finite samples, but sample agreement is NOT
used as the all-parameter or all-future proof.

## Exact chronology certificate

`certify_domino_growth_capture.py` compiles every letter slot of every finite
arm/cap and the infinite period into973 read families. Every family has:

* an exact Presburger domain of triples (r,x,y), with r >= 20;
* a fixed required turn;
* an exact affine chronological time at that cell.

For a repeated word, the occurrence index k satisfies 0 <= k < r+c; for the
infinite tail it satisfies k >= 0. Every repeated word has nonzero displacement,
so each family has at most one read of a given cell for a fixed r. A cap is a
single read. Every prescribed read belongs to exactly one family occurrence.

For each family f, begin with the intersection of its domain with J_r. For
every other family g, intersect their same-cell domains and require t_g < t_f;
XOR this entire earlier-read domain into the current-color domain of f. This
is exactly the ant color before f, including interactions arbitrarily far out
in the infinite tail. Compare with L=black and R=white. Every bad set is empty.
Skipping f itself is valid because its spatial map is injective in k.

The compatibility optimization skips only provably disjoint domains. All finite
stages have constant y and even horizontal displacement; their signatures record
x parity and y. The tail has displacement(-2,2), so its signatures record the
fixed affine x+y and y parity. Cross-type pairs are never skipped. The frozen
script performs211,034 candidate intersections, of which2,493 produce nonempty
earlier-read relations. A separate checker can avoid this optimization entirely.

Because the proposed geometric path has the correct turn at every read on the
specified initial board, deterministic ant evolution proves it is the actual
trajectory for all times. No bound on tail periods is used.

## Frozen provenance

The result records libisl version isl-0.27-GMP. The source has an explicit
operation budget; any resource exception is an error, never interpreted as
an empty bad set. Exact hashes are in `domino_growth_capture_hashes.txt`.
The candidate-selection helper merely extracts one fixed literal tail at r=20;
all selected words are also stored explicitly in the result JSON. Selection
from a simulation does not confer legality: the all-read checker establishes it.

Independent no-import replay in `audits/check_domino_capture_independent.py/json`
uses direct two-index chronology and no compatibility pruning. All946,729
ordered pairs recover exactly2,493 nonempty earlier-read relations; every one
of973 bad sets is empty. Actual-board controls at r=20,21,40,100,1000 also pass.

Scope remains this one prepared rod family. Other endpoint patterns, rail
heights, alternating cap schemes, or two-dimensional mechanisms are untouched.
