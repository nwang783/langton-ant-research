# Two large executable epochs: long reimport is possible with charged old fuel

23 October 2026. Author construction and targeted full-board controls.
Independent audit is pending. The all-parameter w-routing argument below is
separate from the paired-forest event counts, which are claimed here only
for the stated fixed controls. No regenerated-fuel or global sharpness claim.

## Outcome

The original collector endpoint forces a short local-star excursion. That
is NOT an obstruction for every modified collector: a final input hook and
a hidden old-side branch allow reimport to feed a second genuinely large
ordinary epoch. The second fuel is explicitly pre-funded, physically present
in the complete entry board, and pruned near the end of the first epoch.
It is not created from the first epoch's mass gain or recycled R outputs.

For q=2 modulo4, q>=2, put n=8 floor((q+1)^2/4). The complete initial board
has mass

    M = 3n+4q+17.

The two ordinary epochs have respectively

    L counts n+1 and n+19,
    times 2n+q-1 and 2n+q+35,
    mass gains q-3 and q-3.

They are separated by ONE exceptional RRRRL block, mass gain3. The complete
prefix time is4n+2q+39 and total gain2q-3. For q>=6 both ordinary gains are
positive and of square-root order in their full charged entry masses.
The interval still has total time only O(M), not a cubic lower example.

Fixed whole-board checks q=2,6,10,14 verify the exact words, proper post-L
entry, every ordinary w bridge, all active-component changes, and EVERY
cycle birth/erasure in BOTH full graphs. In these controls both graphs stay
forests in both ordinary epochs. The reset has exactly one z cycle birth
and one z cycle erasure, and no w cycle event. This is one physical erasure
in the entire two-epoch prefix, not one event charged twice.

At q14 the board mass is1417: first path449, collector499, connector3,
pre-funded second branch466. Epoch1 lasts909 updates/gains11; the reset
lasts5/gains3; epoch2 lasts945 updates/gains11 on467 old bridges.

## Exact complete-board formula

Use the reflected (a,b) w-lattice and physical midpoint map from PROOF.md.
All coordinates below are w coordinates, and every unit edge is an actual
physical black cell. All unspecified physical cells are white.

1. Take the spacing-eight outward counterclockwise q-run input spiral P
   with lengths8,8,16,16,... . Because q=2 modulo4, its final run is N.
   Write its endpoint u=(A,B). Its preceding vertex is b=(A,B-1).
2. Append ONE old input edge u--v, v=(A+1,B). This final N->E right turn
   has block r0 and writes no arm. The first epoch's old path has n+1 edges.
3. Take the detoured collector of one_component_paired_forest_collector.md,
   but REMOVE its last edge a--v, where a=(A+1,B-1). Its endpoint is now a,
   and it has n+4q-5 edges. This removal matters: retaining a--v would put
   the collector on the future input endpoint and invalidate bridge routing.
4. Retain the same three-edge initial-root connector
   (0,0),(-1,0),(-1,-1),(0,-1).
5. Add a hidden branch rooted at b. Go W2 to(A-2,B-1), then N16 to
   c=(A-2,B+15). From c follow an INWARD counterclockwise q-run spiral:
   generate a spacing-eight clockwise outward spiral E,S,W,N,... from0,
   reverse its complete unit-vertex list, then translate its first vertex
   to c. Because q=2 modulo4, the reverse starts N and lies entirely in
   the box above c. It joins the N16 stem without another bend. This
   branch has n+18 edges.

The inward orientation is essential. An outward spiral entered at its
center from a long external stem would cross that stem; it is NOT a valid
substitute. The reversed clockwise spiral is entered at its outside
bottom-right endpoint and lies in y>=B+15. Its n-edge bulk is separated
from the first input/collector and the N16 stem reaches it from below.

The complete entry board is exactly the union of these five finite edge
sets. The branch meets the first input only at b and does not meet the
collector or connector. It is one initial w tree, so no passive source or
unreported cycle is used. Its size is

    (n+1)+(n+4q-5)+3+(n+18)=3n+4q+17.

Initial physical pose is(1,1),E. As before, the board union physical cell
(0,1), at pose(0,1),S, has an L giving exactly this entry. The preceding L
is outside the claimed prefix and need not be a w bridge.

## Why the first epoch still executes

Its word is the base outward-spiral word followed by one L for the hook
u--v. The new branch at b is in the W port, AFTER the departing old N port
in b's first-epoch scan. It therefore does not alter b's RL block. The R
at b writes the E arm b--a, attaching the pruned branch to the collector
when the following old N edge is deleted. The hook u--v has r0 and no R.

The removed collector edge a--v leaves the final endpoint v isolated after
the hook is consumed. All collector/branch/connector cells are retained.
The w forest/old-suffix argument works as before: R arms meet the known
collector or new leaves, never the remaining old input suffix. The hidden
branch is pruned at b and cannot connect a newly attached archive to an
uncrossed input edge. All first-epoch L's are old w bridges.

There are q-1 positive physical turns in the base spiral, minus1 for the
right-turn hook, and the first-block correction is-1. Thus G1=q-3.

## Exact reimport and the second ordinary path

At v, the next block is RRRRL. Its first arm goes to a, the endpoint of the
archive containing the collector AND the hidden branch (joined through
b--a). The other three arms are a local star at v, including v--u. The
first arm is a w BRIDGE: u has no surviving first-epoch arm because the
hook block had r0. Deleting this first arm moves the cursor into the large
archive and leaves the3-edge star behind. The block is nevertheless
exceptional, because it erases the opposite z unit cycle.

At a the next block is L, crossing the surviving arm a--b. This cuts the
whole collector away and enters the hidden old branch, not a local star.
At b the next read N is white (old b--u was consumed), so R reinserts
b--u and attaches the3-edge local star on the DEPARTED side. The next W
port is the old hidden branch, so L crosses it. This is an ordinary RL
block. The following old path is exactly the hidden W2,N16,inward-spiral
branch. Thus the second epoch's old bridge path is a--b followed by that
entire n+18-edge branch, n+19 edges in all.

The near-end patch cannot touch any later branch edge. The straight W
prefix writes one upward arm; the first N-stem arm may meet its endpoint,
but only in an already departed component. All later branch/output contacts
are excluded by spacing8 and the separation of the second spiral box.
Consequently every R attachment remains on the old side and every L is an
initial bridge of the second epoch. All w graphs remain forests. This is
an exact all-parameter w-routing argument, with every pre-funded old cell
retained, not a synthetic second word imposed independently.

The second path starts W, continues W, turns right to N at the stem (-1),
then has q-1 counterclockwise turns in the inward spiral. Its signed
physical turn is q-2, and its first block L contributes-1. Therefore
G2=q-3 and its time is2(n+19)+(q-3)=2n+q+35.
The current w endpoint is isolated again at its end.

## The actual causal restriction and what this does not show

The new branch cannot already have been connected to the earlier collector
while its root b remained in the first epoch's far future component.
If it had, an earlier R attachment to that collector would have supplied a
bypass of the departing initial bridge. This violates exact far-side
inheritance. In this construction the branch and collector meet only when
b's own R arm is written, immediately before b is departed. Hence the large
second fuel is genuinely old pre-funded branch input, not earlier output
reproduction concealed by a connector.

This shows that big reimport can feed a large next ordinary path when the
old fuel is explicitly placed in the appropriate ports. It does NOT show
that first-epoch produced fuel can regenerate a comparably long positive-
gain next epoch, nor that an unlimited sequence can reuse fixed total seed
mass. The global cubic upper bound's exponent remains untested by such a
construction: M already pays for both large old paths.

## Frozen controls

check_two_prefunded_epochs.py
SHA256367a0e58145f96fab74cc3e37274f75aad02950e39a2cc9a049f1009db3662ff.
two_prefunded_epochs_controls.json
SHA256cdec40a8948c2d105989ac70d50142c8015a6794d33544ded4d213c6434f3267.

The fixed controls certify paired forest event counts only at q2,6,10,14.
Those full checks corroborate, but do not independently audit, the general
geometric w-routing proof above. The collector dependency itself remains
pending independent review. No new signed global conclusion is asserted.
