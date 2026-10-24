# A one-sided plateau at the right exterior height cannot hide behind a low C row

23 October 2026, 15:35 UTC. Analytic barrier lemma and locked-rail corollary,
submitted for later independent review. No general K=1 exclusion.

## 1. Exact barrier hypotheses

Use a complete WHITE cap-four translating front, actual d=(0,2a), P,
with integer stream f=h(C_right)-h(L_left). Normalize C faces to even
lower-left x+y parity. Suppose the exterior constants are

    c_left=b, c_right=b+1=lambda,

and EVERY C face in the separating row x=-1 (odd lower-left y) has
height b. Suppose further that

    every C face with x<=-2 has height<=lambda,
    at least one such face has height=lambda.

No hypothesis is made on C heights to the right of the low row. In
particular higher global maxima there are retained. The active strip is
finite in the full-drift quotient, as for any translating finite word.

## 2. All boundary ports of a left lambda face are positive

Let F be a C face at lambda with x<=-2 and let L be any edge-neighboring
L face. Nonnegative flow gives h(L)<=lambda. Equality is impossible.

If L is in row x=-1, its C neighbors immediately above and below lie in
the prescribed low C row at b, contradicting h(L)=lambda>b. Otherwise
L has x<=-2 and all its C neighbors have height<=lambda. Equality would
force all four neighboring C heights to lambda and all four boundary
flows of L to0.

At each corner of such a zero-boundary L face, either possible R turn
uses one of its two incident zero-flow edges. A visited WHITE vertex has
a first R, so the corner cannot be visited at all. All four physical
port flows there vanish, forcing the opposite diagonal L face also to
have height lambda. Repeating at westward diagonal corners propagates
L height lambda arbitrarily far LEFT while remaining in x<=-2.
Eventually this reaches the empty left exterior, whose stream is b.
This contradiction rules out equality. Integer heights therefore give

    h(L)<=lambda-1 for every L adjacent to a left lambda C face.

All FOUR physical boundary edges of every such F have positive flow.

## 3. The left lambda faces have their own closed first-L birth curve

At any corner of a left lambda face, the other incident C face is still
at most lambda: it is either to the left, or in the low row x=-1.
The signed cap-four local R-count rule therefore makes every R select a
maximizing incident C face, exactly as in the signed first-L birth proof.

That proof uses only positive boundary ports, local C maximality and
finitely many face classes. They all hold here, WITHOUT importing the
global-H maximum theorem at level lambda. For each left lambda face F,
its earliest physical boundary departure is a negative flat contact,
L1 from another lambda face G, with R0 around G and R2 around F. Its
birth predecessor stays in the left lambda set and lowers B by at least5.

There are finitely many left lambda face classes: lambda>b excludes the
left exterior, and the low row bounds them on the right. The predecessor
closes on an embedded essential cycle. Reverse orientation gives a
positive full-winding-one first-L curve Gamma_lambda entirely LEFT of
the low row, with strictly increasing selected L1 times.

## 4. Its actual cursor current has incompatible homology

The signed cursor proof likewise uses just that embedded first-L curve,
its AAB prefixes and selected L1 chronology. R0 crosses LEFT-to-RIGHT,
R2 crosses back, and each actual right excursion ends at an earlier
selected contact. The equivariant endpoint bijection has positive integer
retreat K_lambda>=1. Thus the physical RIGHT current has homology
-K_lambda<0. All L suppliers and mixed winding cases remain retained.

But Gamma_lambda cuts only C faces of height lambda. Its right current
has the piecewise stream h-lambda on RIGHT,0 on LEFT,0 on cut faces.
The oriented exterior jump is

    c_right-lambda=0.

That same physical right current has homology0, contradiction.

THE BARRIER LEMMA: under the low-C-row and exterior hypotheses, the LEFT
C maximum cannot be exactly c_right=b+1. If any left C height exceeds b,
there must also be a left C height exceeding c_right.

The last sentence assumes the left C maximum exists in the finite strip;
it is not a claim about a local bump adjacent to a higher left peak.

## 5. Consequence for a white completion of the locked bent rail

Apply this to bent_secondary_rail_height_obligation.md. Its four main
locked histories force the low C row x=-1 to b=M-2 and have
c_right=M-1. The secondary-rail chronology already forces some deeper
C height at least M-1.

If there were NO global-M C face to the LEFT of the low row, all left C
heights would be<=M-1. The secondary obligation makes their maximum
exactly M-1=c_right, forbidden by the barrier lemma. Therefore

    any COMPLETE WHITE completion of the locked bent main rail needs
    at least one GLOBAL-M C face on the LEFT of its low row.

That maximum component is DISTINCT from the main one: a path in the
C-contact lattice changes x by1 each step, so it cannot cross the entire
x=-1 row at height M-2 while staying at M. Consequently the LEFTMOST
maximum component of a K=1 front cannot have this prescribed locked
alternating-bend main architecture.

This is necessary supplier geometry, not an infinite regress: another
maximum component may have different bends, branches or rank3 gates.
It does not prove K>=2, exclude arbitrary K=1 curves, or construct a
white completion. The prepared W20 control still works because its LEFT
fuel cells start with L and violate the complete-white premise.
