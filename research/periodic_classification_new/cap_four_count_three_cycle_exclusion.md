# No finite physical count-three edge cycle in a white cap-four front

23 October 2026, 07:53 UTC. Independently signed analytic lemma (audit KT).
This is a structural lemma, not a general cap-four exclusion.

Let a bi-infinite complete initially-white Langton front have at most four
reads per physical cell. Direct every used physical edge by the ant's
checker sector and label it by its complete traversal count. The graph
formed by count-three edges has NO finite physical directed cycle.
Essential cylinder cycles/infinite lifts, and finite paths with endpoints,
are not excluded. No drift, period or width restriction is imposed.

## Local count-three routing

A vertex on a directed count-three cycle has one count-three incoming and
one count-three outgoing port. Its history must have exactly four reads:
a triple cannot have both such ports, since RLR has two R turns and one L.
The remaining incoming and outgoing ports each have count one. The
count-three path turns R or L, never goes straight, by checker orientation.

Write a for its high-flow incoming heading and b for its outgoing heading.
If b=a+1 (R), both R reads use a->b. Thus the FIRST read turns around the
clockwise face in the right-hand corner of the high-flow path. The two L
reads turn around its two left-adjacent faces, one each.
If b=a-1 (L), both L reads use a->b. Thus the LAST read turns around the
counterclockwise face in the left-hand corner of the high-flow path. The
two R reads turn around its two right-adjacent faces, one each.
These conclusions also follow by enumerating the four quad routing types (up to rotation)
 having one count-three incoming and outgoing port.

## The two orientations

A finite count-three directed cycle has no repeated vertex because the
count-three graph has indegree/outdegree at most one. Lattice planarity
makes it a simple rectilinear Jordan polygon. Let V be the actually read
primal vertices on or inside it. V is finite, nonempty, and every boundary
vertex is a complete RLRL quad.

If the polygon is clockwise, its interior is to its right. At a convex R
corner, the FIRST R turns around the common interior right face. At a
concave L corner, both right-adjacent faces are inside, so whichever face
its FIRST R uses is again inside. Therefore the predecessor of the first
read of every boundary vertex is in V. For a strictly interior vertex,
any neighboring predecessor is also on or inside the polygon. Every first
read consequently has an earlier read predecessor in V. Taking the
minimum physical first-read time on finite V is a contradiction.

If the polygon is counterclockwise, its interior is to its left. At a
convex L corner, the LAST L turns around the common interior left face.
At a concave R corner, both left-adjacent faces are inside, so its LAST L
also turns around an interior face. Thus the successor of the last read
of every boundary vertex lies in V; the same holds at strict interior
vertices for geometric reasons. Taking the maximum physical last-read
time on finite V is a contradiction.

The proof uses actual physical first/last times, not phases modulo a
period. It deliberately does not infer that all count-three edges form a
forest on the full-drift cylinder. An essential cylinder cycle has an
infinite physical lift and neither finite extremum argument applies.
Nor does the proof extend to cap-three count-two cycles: their boundary
triples need not end in L, and the earlier doubled-edge counterexample
remains intact.
