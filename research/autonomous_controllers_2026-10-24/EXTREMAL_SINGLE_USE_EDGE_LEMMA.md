# Exact single-use edges and the unique possible extremal cycle

24 October 2026. Author proof, submitted separately for independent review.
No priority, general classification, or finite-seed capture claim.

## Model and hypotheses

Use a COMPLETE initially WHITE translating front on the physical square
lattice, with full nonzero drift d and full event period P. Equivalently,
these are the stable complete histories of an eventual finite-support
periodic realization. Each active physical cell has a finite history
R,L,R,L,...; its full-drift translates have the translated chronology.
Keep all permanent odd-output BLACK roots in the reverse graph.

Let E contain an actual directed unit edge u -> v precisely when the FIRST
read of u is immediately followed by the LAST read of v. The graph is
translation-equivariant. It has outdegree at most one and indegree at most
one: the last read of a target has a unique preceding physical event.
The definition includes last R and last L, rather than discarding BLACK
output classes. Complete histories, not cropped factors, are meant.

## 1. Every marked physical edge is used exactly once

The selected departure is the first read of u, hence the first departure
along that physical edge. Therefore its arrival is the first arrival along
that edge at v. It is also v's last read, so no later traversal is possible.
Ordinal matching of occurrences on a physical edge proves its total count
is exactly one. No period-origin or visit-count bound is used.

Consequently the COMPLETE incoming-heading words at the two endpoints are
forced up to their lengths and a rotation. Write A for the first heading,
and -A for its opposite.

* SOURCE of E, length m: A at rank 0; A at every odd rank; -A at every
  positive even rank. In symbols A,A,-A,A,-A,A,... .
  After rank 0 every departure uses the opposite outgoing port.
* TARGET of E, length n>1: A repeated n-1 times, then -A.
  No earlier read can use the incoming port of the last read.
* A singleton has its sole heading A, with no opposite-heading condition.

These formulas follow directly from alternating R/L and the two allowed
incoming directions at a physical cell. They strengthen the previously
signed endpoint parity/type table rather than replacing its hypotheses.

## 2. Exact internal vertices

An internal E vertex is both a source and a target. For m>1, the two
formulas agree only when m=3, with incoming word A,A,-A and turns R,L,R.
For m=2 their final headings disagree; for m>=4 they disagree already
between the positive-even source rank and the constant target prefix
(or at the last rank). Thus EVERY internal E vertex is exactly

    singleton R, or the three-read history (A,R),(A,L),(-A,R).

In particular arbitrarily large odd-opposite histories are NOT internal
vertices. This is an all-cap theorem about the selected graph, not a
cap-three restriction on the rest of the front.

## 3. A possible E cycle is a one-sided exterior boundary

A quotient E cycle is also a first-R-departure cycle. Invoke the signed
all-cap first-departure counterflow theorem: it is a simple essential
cylinder circle of winding -1 relative to the ACTUAL full d. Every cycle
vertex is internal. At a singleton the geometric turn is R; at a triple
A,A,-A it is L, since the cycle enters on the last heading -A and leaves
on R(A). Essential total turning is zero, so half the vertices are
singletons and half are triples. All are odd output classes.

At a singleton, the two cycle edges are the only used physical edges.
At a triple the off-cycle edges are the predecessor of its first two
reads and the common successor of its last two reads. Each is used twice.
They occupy the other two compass ports. Both lie locally to the RIGHT
of the oriented E circle at this geometric L corner. Thus no used
non-cycle edge is incident from the LEFT side of the circle.

The full used-edge graph is connected, since it is the image of the single
actual event orbit. A simple essential circle separates the infinite
cylinder into a left and a right component. A used edge cannot cross it
away from a lattice vertex. Hence every other used vertex and edge lies
on its RIGHT side; the LEFT component is entirely unread. This is a
geometric support statement, not a claim that an output field was erased.

There is AT MOST ONE quotient E cycle. If two existed, their common
winding -1 gives consistent orientations. One lies to the right of the
other, while the first lies to the left of the second. Connected used
support would violate the preceding right-side-only property for one
of them. Disjointness follows already from E's indegree/outdegree bounds.

## 4. Consequences and the exact remaining growth-eight gap

Every E component is now a directed path or this unique possible cycle.
If a cycle exists and has length ell, it consumes exactly ell odd output
classes, ell/2 singleton and ell/2 A,A,-A triple classes. Therefore

    2 ||d||_infinity <= ell <= g,    ell is even,
    ell/2 is congruent to each component of d modulo two.

At growth eight, a possible cycle therefore has length 4, 6, or 8 after
the signed exclusions of full unit-axis/unit-diagonal drift. When ell=8,
ALL odd classes lie on the circle. When ell<8, only 8-ell additional odd
classes remain. This reduces a selected-cycle subcase, not all growth
eight: E can be acyclic or empty. The theorem does not force existence
of an E cycle or bound arbitrary even histories away from it.

The previously signed age/spatial bounds remain separate necessary tests.
No addition of overlapping period estimates is justified here. No
controller realization or entire growth-eight drift/width exclusion has
yet been obtained from this lemma.

## Dependencies

* ALL_CAP_EXTREMAL_READ_COUPLING.md, SHA256
  1687855302eb19190f3a42be7f8fb047ad3b7874d166c7e3b668eb37e85a65b3.
* EXTREMAL_PORT_TYPE_REFINEMENT.md, SHA256
  fdde77939e853ddeeba708e300a44b668224f3c80ea0fbbdc7979869801f0eef.
* ../periodic_classification_new/white_first_departure_counterflow.md.
  Its independent signed status is recorded in that directory's README.

The source/target formulas in Sections 1-2 have no dependency on an
external classification or a bounded enumeration. Section 3 uses the
signed first-departure theorem plus elementary planar separation.
