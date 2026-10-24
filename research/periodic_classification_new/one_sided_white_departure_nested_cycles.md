# Finite white first-departure cycles are clockwise and nested at the initial head

23 October 2026, 11:16 UTC. Nonperiodic analytic candidate for audit.
No periodicity, finite black support or bounded visit cap is assumed.

Consider ANY ordinary one-sided Langton trajectory, on an arbitrary initial
black/white board, from one initial head position o at time0. On each
visited INITIALLY-WHITE physical cell v, its first read is R. Define b(v)
to be the target of that first R departure. Restrict to edges whose target
is also an initially-white visited cell. This is a PARTIAL outdegree-one
graph; an edge may leave the domain into an initially-black cell.

THEOREM CANDIDATE. Every finite directed cycle of this partial graph:
1. is a clockwise simple physical Jordan polygon;
2. contains o in its CLOSED bounded interior;
3. is nested with every other finite cycle of this graph.
At most one cycle contains o on its boundary, and then it is the innermost
of all finite cycles. If o was initially black, every cycle contains it
strictly inside, since the graph's vertices are initially white.

The result does NOT bound the number or size of nested cycles, exclude an
infinite trajectory, or prove eventual standard capture. Infinitely long
first-departure components need not contain any cycle.

## 1. Geometry and exact boundary times

The conserved checker sector orients every physical grid edge in one fixed
direction. A directed cycle with distinct vertices is therefore a simple
embedded unit-edge polygon, with no straight corners. Let T(v)>=0 be its
first read time and I(v) its first incoming/read heading. At o, I(o) means
the given initial heading, not a fictitious actual predecessor.
Every cycle vertex's outgoing edge is R(I(v)).

At a RIGHT cycle corner v!=o, the incoming cycle heading equals I(v), so
its source u is literally the first-read predecessor neighbor. The first
R at u is the earliest possible departure from that physical source to v,
so exact chronology gives T(v)=T(u)+1.
At a RIGHT corner v=o, the cycle arrives later than its time0 read; write
T(u)+1-T(o)=4q_v with q_v>=0. We do NOT claim q_v=0 here and do NOT use
an uncorrected initial incoming-port ordinal.

At EVERY LEFT corner, including o if it lies there, the incoming cycle
heading is -I(v). Its arrival is a later read than v's first read, so
T(u)+1-T(v)=4q_v with q_v>=1. Every zero-displacement gap is divisible by
four; if v=o the same holds between its time0 read and the later return.
Set q_v=0 at all nonhead RIGHT corners. Summing around the finite cycle:

    0=ell-4Q,        Q>=number of LEFT corners.

A counterclockwise Jordan polygon has m_L=m_R+4 and thus
m_L=(ell+4)/2. It would require ell=4Q>=2ell+8, impossible.
So every cycle is CLOCKWISE, even if it passes through the initial head.

## 2. The initial head must be enclosed

Suppose o is outside the CLOSED polygon. Take all visited physical cells
in its closed bounded interior. This is a nonempty finite set, including
all boundary vertices, and it does not contain o. It is closed under the
ACTUAL first-read predecessor:
- At a boundary RIGHT corner, that predecessor is the previous boundary
  vertex, as above.
- At a boundary LEFT corner of a clockwise polygon, the first incoming
  heading is opposite the incoming cycle heading, and its source neighbor
  is geometrically inside the concave corner.
- A first incoming unit grid edge to a strict interior vertex cannot cross
  the polygon boundary without a grid vertex, so its source also lies in
  the closed polygon.
Interior cells can be initially BLACK: their first read still has an
actual earlier predecessor unless it is the initial head. No color premise
is needed for these strict interior cells. Only the initially-WHITE cycle
boundary is used for the R-corner geometry.

Every member of this finite set therefore has a predecessor in the set
with strictly earlier first read time. The least first time is impossible.
Consequently o belongs to the closed polygon.

## 3. Nesting

Distinct cycles of a partial functional graph are vertex-disjoint. Their
unit grid polygon boundaries cannot cross in edge interiors either, and
opposite traversals of one edge are disallowed by the checker sector.
Thus their Jordan boundaries are disjoint. Two disjoint Jordan polygons
both enclosing the same point in their closed interiors cannot have
separate interiors; one encloses the other. Every pair is therefore nested.
Only one functional cycle can contain o as a vertex. All others must
enclose that boundary and are outside it, so it is the innermost cycle.

This identifies a genuine one-sided exception rather than suppressing it:
all finite white first-departure cycles can recycle the SAME initial-head
exception through nesting. A count or fuel budget does not follow.
