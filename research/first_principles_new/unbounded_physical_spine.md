# Bounded packet roots force a bounded physical trace

22 October 2026. Independently analytically audited consequence of the exact packet decomposition and the endpoint barrier. The conclusion below is unboundedness of the physical permanent spine, not physical transience or highway attraction.

## 1. A general bounded-root packet lemma

Consider a square-ant-legal infinite program consisting of elementary turns and completed G packets, with a fixed checkerboard/heading sector sigma. Suppose every elementary-turn location, every G starting pose, and the one-unit transverse width at each G start lie in one fixed finite rectangle Q. The G depths need not be bounded a priori.

Claim: the entire physical read trace is bounded.

Fix an integer column z strictly to the right of Q. Only eastward G packets can touch it. A packet ending before z does nothing there; a packet passing through z reads each bit there twice and restores both. Only a packet with FAR endpoint at z changes the column at packet boundaries.

All horizontal packets use rows in a finite interval [a,b], since their starting poses lie in Q. Set H=b-a+1. Put

    rho(x,y) = -sigma (-1)^(x+y) black(x,y),
    F_z = sum_{y=a}^b (y-a) rho(z,y).

An eastward G far endpoint has signed change -1 at its lower corner and +1 at its upper corner. This is the right boundary of its positive unit-height strip in the cancellation-height identity. Therefore EVERY far-endpoint update at z increases F_z by exactly1.

The coefficient of each bit in F_z is fixed, and each bit is0 or1. The entire range of F_z has width at most

    C = sum_{j=0}^{H-1} j = H(H-1)/2.

Thus at most C packets can have far endpoint exactly z, regardless of the initial colors in those H cells. Between these finitely many events, the column's colors at packet boundaries are constant.

During one such interval, any eastward G extending strictly beyond z must see upper0/lower1 at z. The row pairs on which this is possible are pairwise disjoint: two adjacent pairs would require their shared bit to be both0 and1. There are at most floor(H/2) possible pairs.

For each fixed eligible pair, at most ONE packet can end beyond z during this interval. Indeed, after its first far endpoint f, any later endpoint before f sees the restored interior01, one at f sees the flipped equal endpoint rather than the required equal color, and one beyond f would cross the equal-colored barrier. The required equal endpoint color is fixed by f, the row pair, and the conserved sector, independent of the packet's starting column. Other eligible row pairs are disjoint, and packets ending at or before z cannot repair the tail. This is precisely the endpoint-barrier argument.

Consequently the number of eastward packets with far endpoint greater than z is at most

    (C+1) floor(H/2),                                    (1)

and in particular is finite. Every one of these completed packets is finite. All other eastward packets remain to the left of or on z. Hence the union of all eastward read supports has a finite rightmost coordinate.

Apply the same argument after each of the three quarter rotations to bound the west, north, and south excursions. Elementary turns are already in Q. This proves the claim.

The word 'constant' above always refers to colors at the boundaries between completed packet events. A crossing packet can temporarily flip the selected column; the interior pattern lemma guarantees that it restores those flips before another event starts. No pointwise-in-time freezing is assumed.

## 2. Application to the limiting spine

The audited spine decomposition consists of permanent core turns, at most one optional G per stage, and at most one optional B. Expand each B into its four parent-face turns and its one or two G children. If the physical permanent-spine roots stayed in a bounded set, all the resulting elementary-turn locations and G starting poses would lie within a fixed two-unit enlargement of that set. The hypotheses of Section1 would therefore hold.

The entire ant trajectory after the finite initial prefix would then be bounded. This contradicts the already established unboundedness theorem for the ordinary square ant (equivalently, a bounded finite-color trace would repeat a complete state, while the strict complete-state clock forbids repetition).

Therefore:

    The projection of the limiting permanent spine is unbounded in Z^2.

This conclusion does not say that every physical site has finitely many spine visits. It does not bound retreat, number of repeated physical coset blocks, finger lengths along an unbounded spine, or the frequency of directional changes. A spine may still be unbounded and recurrent in a bounded region; that possibility is not excluded by this argument.

## 3. Scope of the mechanism

The bounded-root lemma uses the chronological positive sign of endpoint updates, not ordinary black mass. The vertical signed first moment is bounded only because the set of horizontal-packet row pairs is finite. For an unbounded set of roots, that finite-band hypothesis can fail, and the proof supplies no global fuel budget.

Its explicit crossing bound (1) may be useful in a later strip or bounded-retreat argument. At present it is only a bounded-root obstruction, not a standard-highway classifier.

## 4. A periodic-boundary corollary

If the eventually repeating boundary core word had nonzero net heading rotation, its repeated Euclidean poses would be bounded, because finitely many rotated copies cancel its displacement. If it had zero rotation and zero displacement, they would also be bounded. The unbounded-spine theorem excludes both cases. Thus any eventually periodic boundary core must have, after at most four repeats, zero rotation and a NONZERO translation. This elementary corollary alone does not control the decorations. The subsequent independently audited bridges in `axial_core_periodicity_bridge.md` and `periodic_core_decoration_stabilization.md` do show that an eventually periodic core forces a full translating-periodic tail, without a separate decoration hypothesis.
