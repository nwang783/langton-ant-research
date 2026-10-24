# Canonical sheet contours preserve separated C and L contact levels

24 October 2026, 01:14 UTC. Complete WHITE cap-four translating front,
actual full P,d. Pending independent review. This is a local physical
barrier statement for the signed canonical repair fd20e425, not a new
front search or a genus bound.

For every integer j, draw all canonical sheet-j circles using their
signed disjoint rounded corner arcs. The following diagonal face-contact
graphs can each be embedded in the complement of those circles:

    C faces with h(C)>=j+1;
    L faces with h(L)<=j-2.

A diagonal contact is retained only when BOTH faces satisfy its bound.
Here L height is UNSHIFTED h(L). Therefore an entire such C superlevel
component or L sublevel component stays on one side of every sheet-j
circle. Physical lifts and arbitrarily short quotients are retained.

## 1. Local proof for the L sublevel

At a primal corner let C1,C2 and L1,L2 be its two C and two L heights.
The total number n of complete reads is

    n=C1+C2-L1-L2 <=4.

The sheet-j ports satisfy g_j(e)=1{h(L)<j<=h(C)}. Suppose BOTH L sectors
are <=j-2. If both C sectors are below j, no sheet-j arc occurs. If only
one C sector is at least j, there are just two active ports and their
unique arc is RIGHT around that C sector; both L sectors are joined on
its other side. Their diagonal contact does not cross the arc.

If both C sectors are at least j, the count bound forces EXACTLY

    n=4, C1=C2=j, L1=L2=j-2.

This is the local TOP sheet: both C heights equal j, and the signed
repair pairs its four ports by TWO RIGHT corners around those C sectors.
The central complementary patch joins the two L sectors. Thus their
contact is again disjoint from both canonical arcs.

These cases exhaust every local contact in the indicated L sublevel.
The contact graph may be routed through those central complementary
patches instead of drawing a straight diagonal through the primal
vertex. No face-center position or component identity changes.

## 2. The dual C superlevel

Suppose BOTH C sectors are >=j+1. If both L sectors are at least j,
there is no sheet-j arc. If exactly one L sector is below j, the two
active ports have the unique LEFT corner around that L sector; both C
sectors are connected on its other side.

If both L sectors are below j, the read bound forces EXACTLY

    n=4, C1=C2=j+1, L1=L2=j-1.

The canonical sheet-j repair in this flat four-read case consists of
TWO LEFT corners around the two L sectors. Its central complementary
patch joins the C sectors. Thus this C contact does not cross either
arc. This proves the dual barrier.

## 3. Penultimate specialization

At the global C maximum M, put j=M-1. Every global-max C component lies
in the complement of all canonical penultimate circles, and so does
every L sublevel component with height<=M-3. The C statement recovers
the geometric mechanism in signed a2170bdc; the L statement is the
separate dual interface needed for old-stock interiors.

The result says nothing about L height M-2 or C height M-1. Those
borderline contacts may change sides at a canonical four-port smoothing.
No component count, odd-output capacity or period inequality is inferred
without a separate bounded-region proof.

Control `canonical_sheet_two_level_contact_barriers.py/json` reconstructs
all thirty complete WHITE histories and all78 nonempty local sheets.
It checks both repaired turns in every four-port equality case, not just
port support. Twenty low-L and twenty high-C local sheet cases occur.
