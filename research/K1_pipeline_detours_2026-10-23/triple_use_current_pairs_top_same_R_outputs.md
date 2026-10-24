# Triple-use physical edges pair same-R odd outputs within a level plateau

24 October 2026. Complete WHITE cap-four translating front, actual full
period P and nonzero drift d. No K1 hypothesis for sections1-4. This is
an exact finite-quotient physical-edge graph, not a literal cursor
itinerary or a new additive flow budget.

## 1. The physical graph and its exact local degrees

In the retained checkerboard/Manhattan orientation, every physical edge
has one possible travel direction. Its complete traversal count is
f(e)=h(C_right)-h(L_left). Let G3(c) contain exactly those directed
physical edges with f(e)=3 and h(C_right)=c; their left L height is
necessarily c-3. Keep ordinary physical cell vertices and retain
lifted edge/port incidence multiplicity in the actual full quotient.

A complete cell has one fixed incoming axis. Normalize it to E/W.
Let r_E,r_W and l_E,l_W count its R and L headings. For an additive a,

    C_NE=r_W+a, C_SW=r_E+a,
    L_NW=a-l_E, L_SE=a-l_W.

The FOUR physical port traversal counts are

    west incomingE: r_E+l_E; east incomingW: r_W+l_W;
    north outgoingN: r_W+l_E; south outgoingS: r_E+l_W.

They agree exactly with the adjacent C-minus-L differences. Inspect
all alternating WHITE histories of1..4 reads, retaining every heading
choice. The30 E/W words give:

-18 with no triple-use port;
-4 three-read same-R words, each with ONE triple-use port;
-8 four-read words, each with TWO triple-use ports, one incoming and
  one outgoing.

There are no other cases. Rotations cover the other incoming axis.
At each two-port vertex BOTH triple ports have the SAME C height c
and L height c-3. Thus restricting to G3(c) removes neither port.

The degree-one cells are precisely RLR with equal R headings. If all
three headings agree (EEE or WWW in this frame), its triple port is
INCOMING: it is a sink. If L1 has the opposite heading (EWE or WEW),
the triple port is OUTGOING: it is a source. Every internal vertex has
one triple input and one triple output. Inactive cells have no ports.

## 2. Actual full-quotient source/sink pairing

There are finitely many active cell and edge classes in the actual
full-drift quotient. In this finite directed multigraph, every vertex
is absent, a source, a sink, or has one input and one output. Components
are directed cycles or directed paths from one source to one sink.
A path starting at a source cannot enter a cycle: the first entering
vertex would then have two incoming edges. It cannot revisit any
vertex for the same reason, or revisit its source, whose indegree is
zero. Thus it reaches a sink after finitely many quotient edges.

This gives a bijection between the source and sink classes of G3(c).
It also lifts to finite physical paths and a full-drift equivariant
endpoint pairing. A physical path may wind before reaching its sink;
no primitive winding, zero winding or short quotient is assumed.
Its endpoints are different full-quotient classes, in particular
because source and sink degree types differ.

Hence the number of odd three-read same-R classes at any fixed high
C level c is EVEN, with equally many incoming-saturated sinks and
outgoing-saturated sources. This is a graph incidence identity, not
strict chronological descent along the path.

## 3. The pairing preserves both level components

At a two-port four-read vertex either both triple edges have the same
C face, or their C faces are the two diagonal sectors both at c; in
the latter case those faces are adjacent in the retained diagonal
C-face graph. Likewise either they have the same L face or both
diagonal L sectors at c-3, adjacent in the retained diagonal L-face
graph. Therefore a physical triple-use path keeps the SAME connected
C level component and the SAME connected L level component throughout.

In particular, a top same-R odd output touching global C=M has low L
height M-3 and pairs with another top same-R odd output touching the
SAME L plateau at M-3. Endpoints can be far apart, lie in the same
maximum component, or have a path winding in the quotient. None of
these facts allows one endpoint to disappear or become a singleton.

Do not read this path as an actual consecutive cursor factor. At a
four-read vertex the three incoming edge occurrences may use its other
single port, so the chronological occurrence matching can leave the
spatial triple-use graph. No physical time-cycle contradiction or
extra per-path period payment is claimed.

## 4. Level-M notation

Let Ntop count odd classes incident to a global maximum C face M.
Let Nsame count its SAME-R three-read classes, which are exactly the
endpoints of G3(M). Let Nshallow=Ntop-Nsame; these are singleton or
opposite-R three-read top classes. Then

    Nsame=2J, J=number of source-sink path components of G3(M),
    J=number of its source classes=number of its sink classes.

Cycles of G3(M) have no odd endpoint and do not contribute to J.
The equality counts path components in the finite full quotient, not
arbitrary translated physical copies as new components.

## 5. Ordinary lower-band root capacity under K1

Use the ordered disjoint maximum curves of signed6376fdc5. Every
inter-curve band has an L minimum <=M-3, confined inside that band by
the signed selected-contact barrier. A top odd root at such a minimum
can only be SAME-R: singleton/opposite-R top classes have incident L
levels above M-3. Thus its minimum is exactly M-3.

If a band has no non-top odd root but does have a top odd root, section3
pairs that root within its SAME L minimum plateau. The other endpoint
is another top root strictly inside the same band. Same-R endpoints
cannot lie on a selected max curve, whose contacts have opposite Rs.
The low plateau cannot cross the curve. Therefore every such band
uses at least ONE source-sink pair; different spatial bands use different
pairs. Bands with a non-top root can instead be paid by one of the
Nodd-Ntop non-top classes. These payments are disjoint by type.

Consequently the number of rooted bands is at most

    Nodd-Ntop+J = Nodd-Nshallow-J.

The signed physical current partition therefore improves to

    P >=6D+12D max(0,r-1-Nodd+Nshallow+J),
    D=||d||_infinity,

for r chosen ordered maximum curves. This counts only their actual
r-1 spatial bands. It does not produce a band per renewal or forbid
cross-Gamma transfer. Arbitrary minima at different levels or overlapping
components are not added. No original-fuel upper bound follows.

Control `triple_use_edge_graph_local_inventory.py/json` reconstructs
all30 local words, exact physical port counts, source/sink/internal
degrees and both face levels at every triple port. It performs no
front, period, drift, width, radius or multiplicity scan.
