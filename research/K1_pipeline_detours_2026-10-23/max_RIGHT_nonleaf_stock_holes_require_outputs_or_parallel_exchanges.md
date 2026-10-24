# A nonleaf max-RIGHT stock hole needs an odd pair or parallel exchanges

24 October 2026, 01:04 UTC. Complete WHITE cap-four translating front,
actual full P and nonzero d. No K1, leftmostness or zero-output premise
for the theorem. Pending independent review.

Let G be the signed connected repaired-sheet cycle graph, retaining
parallel exchange edges. Put beta=|E(G)|-|V(G)|+1, a nonnegative EVEN
integer by fd20e425. Let J be the number of source-sink components of
the physical triple-use graph G3(M), so 2J is the number of top same-R
three-read odd output classes, by signed3ffd2f42.

Let H be ANY family of DISTINCT contractible repaired cycles on sheet
M-1, each having at least one repaired RIGHT corner around a global
maximum C face. No graph-degree or leaf premise is made. Write h=|H|.
Let F4 count all physical flow-four directed edge classes in the actual
full-drift quotient, at all levels.

THEOREM:

    beta >= F4,
    beta >= 2 ceil(F4/2),
    h <= J+F4 <= J+beta.

In particular, if Nodd=0, every such contractible node must contain a
flow-four edge and be incident to a parallel pair of distinct exchanges.
It has no bridge-only escape. Any nonempty family then forces beta>=2;
more generally beta>=2 ceil(h/2). These reserve cycle rank per DISTINCT
node, not per renewal. There is no initial-fuel bound or global exclusion.

## 1. Exact middle occurrence at a max-RIGHT corner

Normalize a chosen max-RIGHT corner's higher C height to M=0, with
incoming axis E/W. Its two R headings agree. For a complete WHITE
history RLR or RLRL, there are exactly twelve heading words in this
axis. Its exchanged sheets are -1 and -2. Its canonical -1 transition
is RIGHT around the higher C sector.

Every one of those twelve histories has an incident physical port
with full flow THREE or FOUR. The canonical middle transition uses
that port's SECOND occurrence. For three reads these are source EWE
or sink EEE, and their W-reflections. For four reads they are the
three-to-three internal cases EEEW, EWEE, EEWE, WEEE and reflections,
or the four-port-saturated source EWEW / sink EEEE and reflections.
The two opposite-R internal cases are retained in this statement's
middle-path continuation, not misclassified as max-RIGHT corners.

Thus the selected node contains an actual edge occurrence of flow
three or four. No physical edge is being counted only by its support.
The occurrence is precisely ordinal two, with label M-1.

## 2. A triple-use component stays in one repaired middle node

At every internal vertex of G3(c), the ordinal-two triple input and
ordinal-two triple output are the two repaired partners on level c-1.
They are actual L1/R2 occurrences, connected by the canonical swap.
Consequently a cyclic component of G3(c), equipped with ordinal-two
occurrences, is exactly one entire canonical node on sheet c-1.

At a three-read source or sink, the same ordinal-two occurrence is
again on sheet c-1, and its repaired partner is the ordinal-two
occurrence of its other physical port, of flow two. Hence the WHOLE
finite source-sink path is a subpath of ONE canonical c-1 node.
This uses the full actual ordinal matching at each directed edge;
it is not the claim that the actual cursor follows G3 consecutively.

By the newly signed5036e7c2, a cyclic component of G3(c) is essential.
Therefore a CONTRACTIBLE canonical node that contains an ordinal-two
G3(c) edge cannot contain a cyclic component: it contains a source-sink
path. Distinct canonical nodes cannot contain the same path component,
since the ordinal-two edge occurrences partition into canonical nodes.

Let h3 be the number of nodes in H containing a G3(M) edge. This gives
an injection of those nodes into the J path components (choose any one
if a node contains several), and hence

    h3 <= J.

Each chosen component has its two distinct same-R odd endpoint classes.
These are old output reservations, NOT fresh original roots; they may
already be charged elsewhere. No extra 2h3 is added to another bound.

## 3. A flow-four edge gives two parallel exchange edges

Any physical directed edge of full flow four is used at ALL four reads
of each endpoint. Normalize its source v=(0,0), its target w=(0,-1),
so all source departures are S. WHITE alternation forces the complete
headings

    v: E W E W,    outgoing S S S S;
    w: S S S S,    outgoing W E W E.

All rotations are identical. The right C face shared by this edge has
some height c; its left L face has height c-4. Both endpoints have the
same-R height-two profile. Actual ordinal matching gives

    T_r(w)=T_r(v)+1 for r=0,1,2,3,
    Delta_w=Delta_v.

The four edge occurrences have labels c,c-1,c-2,c-3 in that order.
At v the outgoing L1 is c-1 and outgoing R2 is c-2. At w the incoming
L1 is c-1 and incoming R2 is c-2. Canonical repair consequently joins

    v.outgoing L1 --physical ordinal two--> w.incoming L1
                   --repaired--> w.outgoing R2,

    v.outgoing R2 --physical ordinal three--> w.incoming R2
                   --repaired--> w.outgoing L1.

Thus the c-1 endpoint cycle of v's exchange is exactly the c-1 endpoint
cycle of w's exchange. The analogous c-2 endpoint cycles agree as well.
These are TWO PARALLEL graph edges between the same pair of nodes.
Their endpoints are on distinct adjacent sheets, so there is no loop.

The source and target exchanges are different full cell classes. They
are physically adjacent, hence opposite checker parity, while the full
heading drift preserves checker parity. Moreover their complete port
saturation types differ. This also handles arbitrarily short quotients.

Every physical flow-four edge is the only saturated port at each of
its endpoints: a four-read cell cannot have both a fourfold input and
a fourfold output, since its alternating turns would force the other
axis to split. Consequently distinct full flow-four edge classes use
disjoint exchange-edge pairs in G. No primitivity of P or d is assumed.

Delete one exchange edge from every such pair while retaining the
other. The graph remains connected, because each deleted edge still
has its retained parallel alternative. This proves beta>=F4. Since
beta is even, beta>=2 ceil(F4/2).

## 4. Distinct contractible stock holes reserve distinct alternatives

A node in H not counted by h3 still has its chosen max-RIGHT corner.
Section1 forces a flow-four edge there. Its ordinal-two occurrence lies
on that node. Section3 assigns every flow-four edge a UNIQUE upper
canonical node at c-1, here c=M. Thus different such nodes choose
different flow-four edges. If h4=h-h3, then h4<=F4.

Combining with h3<=J proves h<=J+F4<=J+beta. More explicitly at least
max(0,h-J) independent parallel-pair cycles must be present, with the
global even rounding retained.

When Nodd=0, J=0. No source-sink endpoint exists, so every contractible
max-RIGHT node in the family is forced into the flow-four alternative.
In particular its chosen exchange belongs to a parallel pair and is
NOT a bridge. Unlike the earlier leaf theorem, this conclusion allows
arbitrary graph degree and arbitrarily many other exchanges at the node.

## 5. Scope and unresolved mechanisms

The result extends the old restricted max-RIGHT GRAPH-LEAF exclusion
to a structural tradeoff for NONLEAF stock holes. It does not bound
beta above or charge it to original black supply. It does not exclude
all contractible middle nodes: all-LEFT old-stock holes and different
root geometries are not in H. Essential triple-use cycles remain legal
and have no odd endpoint. A repeated renewal may reuse one node, one
flow-four pair or one output pair; h counts distinct canonical nodes
only. The inequality is not added to overlapping period or output
registers. It is not an attained front construction or a global cap-four
exclusion.

Control `max_RIGHT_nonleaf_triple_or_quadruple_control.py/json` starts
from all thirty complete E/W histories, verifies all twelve max-RIGHT
rows and all twelve G3 endpoint/internal rows, then reconstructs the
literal flow-four adjacent pair and both repaired sheet connections.
No period, drift, multiplicity, width or radius search is performed.
