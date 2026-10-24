# Opposite first-arrival and first-departure backbones share no edge

23 October 2026, 11:06 UTC. Analytic candidate for independent review.
Uses only the separately signed complete WHITE first-arrival and first-
departure theorems. No cap/width/period/drift cutoff. ACTUAL full quotient.

Let A be any reversed first-arrival dependency cycle (actual-edge winding
+1) and B any first-R departure cycle (actual-edge winding-1). At a common
vertex v, let I be the incoming heading of its first R. Then:

    A enters with I and leaves either R(I) or L(I).
    B leaves with R(I) and enters either I or -I.

This gives four local possibilities, labelled by their GEOMETRIC turns:
- A=R,B=R: both incoming and outgoing edges are shared.
- A=R,B=L: different incoming edges merge into a shared outgoing edge.
- A=L,B=R: a shared incoming edge splits into different outgoing edges.
- A=L,B=L: no edge is shared; the two arcs use opposite quadrants and
  can be rounded apart without crossing.

The conserved checker sector orients each undirected physical grid edge
in one FIXED direction: one parity departs horizontally and the other
vertically. Thus an edge shared by A and B is traversed in the SAME
direction; opposite-direction edge overlaps are not possible.

Every maximal common directed path therefore begins at a MERGE(R,L) and
ends at a SPLIT(L,R). A common cycle would make A=B with the same
orientation, impossible because their windings have opposite signs.

At a merge, normalize I=N, so A enters from S, B from N, and both leave
E. Relative to that common direction E, A joins on the RIGHT side and B
on the LEFT. At a split, normalize the common incoming heading to N;
A exits W (LEFT) and B exits E (RIGHT). Transport these side labels along
the common path. Its common internal corners are R/R; rotations preserve
left and right. Thus after a small transverse resolution of the common
path, A crosses from the RIGHT of B to its LEFT exactly once. Every such
path has the SAME oriented crossing sign.

All isolated common vertices are L/L kisses and can be resolved apart
without a crossing. Distinct common paths have disjoint small regular
neighborhoods (the curves are individually simple), so these local
resolutions give transverse representatives whose algebraic intersection
is one fixed nonzero sign times the number of common paths. Two closed
curves in a cylinder have algebraic intersection ZERO, because its first
homology has rank one and the intersection pairing of the generator with
itself is zero. Consequently there are no common paths:

    A and B are EDGE-DISJOINT.                         (1)

An elementary equivalent to the intersection-pairing step is that the
simple essential B circle separates the cylinder into globally consistent
left and right sides. Every resolved common path changes A from B's right
side to its left; every isolated L/L kiss changes no side. A closed curve
cannot make only one-direction side changes. Again no common path exists.

They may share L/L vertices. No claim of vertex-disjointness is made.
This is not a generic claim about arbitrary oppositely winding flow cycles;
the fixed first-R local table is essential.

## Simultaneous integral flow subtraction

Different A-cycles are vertex-disjoint within their functional graph;
different B-cycles likewise. By(1), the two families also share no edge.
For ANY selected a A-cycles and b B-cycles, remove one copy of every
cycle from the complete nonnegative integer cell flow. The remaining flow
is nonnegative and balanced, with homology1-a+b. Equal horizontal/vertical
edge totals give its length at least2D*abs(1-a+b). Therefore

    P>=sum ell_A+sum ell_B+2D*abs(1-a+b).              (2)

This can be stronger than keeping the two separate family bounds when
individual cycles have excess length. It is valid for arbitrary selected
subsets, including cycles already completed in a frontier prefix.

## Finite nonnegative accumulation, if implemented later

Write the right side of(2) as the maximum of

    Fplus = 2D +sum_A(ell-2D)+sum_B(ell+2D),
    Fminus=-2D +sum_A(ell+2D)+sum_B(ell-2D).

Every cycle has ell>=2D, so ALL increments are nonnegative. One register
may start at2D and the other at-2D; saturating each only from above at a
fixed scale S is safe. Do not clip the initial negative register upward
to zero before additions: that would overstate the lower bound by2D.
Alternatively store Gminus=Fminus+2D nonnegative with capS+2D and use
max(0,Gminus-2D) when forming a period lower bound. Separate rank-debt
bounds still combine by maximum, NOT addition.

No changed monitor, certificate or exclusion is asserted by this note.
The sign-uniform intersection argument is the new proof obligation and
must be independently checked before using simultaneous subtraction.
