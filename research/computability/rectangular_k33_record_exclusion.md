# Controller-free exclusion of rectangular inflation (k,a,b)=(33,3,11)

2026-10-23 00:30 UTC; affine extension added00:35 UTC. Status: analytic proof,
all425 local nodes and eventual affine extension independently reviewed.
This is not a general highway theorem.

## 1. Statement

No actual finite-support Langton ant has, for all sufficiently large n,

    p(33n+c)=sigma*diag(3,11)p(n)+d,

where c is an integer time offset, d is a lattice vector and sigma is+1 or-1.

Compare the coarse ant p and the fine ant q(t)=sigma*(p(t)-d), so that
q(33n+c)=diag(3,11)p(n). Both are actual finite-support ants. This is the
same turn-preserving comparison as the signed-diagonal extension of
`rectangular_fresh_record_bounds.md`. Coordinate rotations give
the swapped positive diagonal case as well. No uniform substitution, finite
controller, image-word independence or heading-preservation hypothesis is used.

## 2. Saturated pristine climb forces a unique suffix

Take a sufficiently high coarse north record so that the corresponding fine
band lies beyond all finite initial support and all finite early history.
Normalize the predecessor coarse north move's fine macro to displacement
(0,11). Since k=33=4*8+1, it has14 north moves and3 south moves.
The vertical displacement is odd, so the33-step macro has17 vertical moves
and16 horizontal moves; its first and last movement axes are vertical,
regardless of the time offset c. The audited pristine-band bound supplies
two pristine rows at the macro's top:
its suffix from the first arrival two rows below the endpoint is a climb of
height2, with at most3 south moves. Since c(2)=3, all three south moves occur
in that climb, and no south move is left over before or after it.

Every one-row crossing requires at least one south move. The complete audited
one- and two-south catalogs consist respectively of

    F=RRRRLR,              G=RRRLLLLRLR.

Thus the two-row climb is either FG or GF. The latter has a same-turn reread
at its fourteenth read, so only FG is legal. FG has length16, displacement
(-2,2), and final heading north.

The climb reaches the predecessor macro's final height. No further vertical
move is possible before its endpoint: a north move would require an unavailable
south move to return, while south is exhausted. At most one horizontal move
could therefore remain. But k is odd and the macro's movement axis is vertical
at both ends, so that extra horizontal move is forbidden. The macro ends
EXACTLY in FG, and its aligned endpoint has heading north.

## 3. The next east macro is locally impossible

At the high coarse north record the coarse read is R, because it is a fresh
white cell beyond the seed. Consequently the next fine macro must have net
displacement(3,0) in33 moves. Starting with incoming heading north, its exact
movement counts in order(N,E,S,W) are

    (8,10,8,7).

Place the FG entry at(0,0,N), with every initially unread cell on or above
row0 white and arbitrary colors below row0. Replay FG and retain ONLY the
nine resulting cell colors which FG itself read. Forgetting any earlier
prefix history only enlarges the allowable continuation class. The endpoint
is(-2,2,N); the retained output colors are explicitly stored in the certificate.

The finite search `check_k33_fresh_tail.py` explores every possible continuation:
- A known cell gives its one forced turn.
- A previously unread cell at y>=0 gives R.
- A previously unread cell below0 permits either R or L.
- A branch stops as soon as it would exceed any required direction count.

There are exactly425 nodes and no33-read continuation. This is a complete
finite decision tree, not a time-capped search. The full tree, including every
read choice and count-pruned branch, is `check_k33_fresh_tail.json`.
Hence the required east macro does not exist, proving the exclusion.

## 4. Scope

The result removes the(3,11,33) member of the independently signed four-triple
list for fixed and antipodal roots of a single half-turn-symmetric rectangular
direction substitution with minimum multiplier3. It is actually stronger than
that application because the proof uses only actual inflation endpoints.

It does not impose same-path inflation on arbitrary directive sequences and
does not exclude general finite-seed aperiodic ant paths.

## 5. Record existence and finite early history in the affine setting

For all sufficiently large n, iterating n->33n+c stays in the identity's
domain and tends to infinity. Each coordinate obeys an affine recurrence
z->sigma*m*z+d_j with |m|>1. Unless the starting coordinate is exactly its
unique affine fixed point, its values are unbounded in absolute value.
Alternating unit movements ensure arbitrarily late indices whose coordinate
differs from that fixed point, for each coordinate separately. Thus at least
one vertical sign has arbitrarily high records; a180-degree rotation makes
that sign north without changing the diagonal matrix.

Choose records beyond the finite initial supports of both compared ants and
the finitely many coarse/fine moves before the identity applies. The same
maximum-height calculation then makes the claimed top two rows pristine.
All suffix and continuation arguments are local, so no earlier offset or
history changes them.

Independent no-import audit: `../audits/k33_fresh_tail_independent.json`
regenerates the short crossing catalogs and matches the whole425-node tree
using immutable boards and complex headings. Analytic audit message at
2026-10-23 00:33 UTC also reviews the eventual affine extension.
