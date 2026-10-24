# A same-Gamma row-5 return on the leftmost branch-free curve is nonbridge

23 October 2026, 17:52 UTC. New conditional separator argument, submitted
for independent review. This removes one local graph alternative, not
positive cycle excess or K=1 itself.

## 1. Exact signed local configuration

Assume the signed leftmost branch-free K=1 collar theorem. Thus every
strict-LEFT C face has height <=b=M-2, every selected contact has LEFT L3,
and there is exactly one LEFT canonical MIDDLE node A, of winding +1.
All canonical sheets at levels <=M-1 stay on their geometric side of
Gamma, and adjacent-level exchange edges between those levels do too.

Use the signed conditional same-Gamma return normalization:

    main RIGHT row-4 face F, lower-left (0,0);
    older return RIGHT row-5 face H, lower-left (-2,0);
    Z=(0,0): W,W,W,E; Y=(0,1): N,N,N,S;
    O=(-1,1): E,E,E,W; E=(-1,0): S,N,S,S.

All four complete histories are RLRL. The return is traversed downward
through A'=(-2,1), B'=(-2,0); the main face is traversed upward through
A_main=(1,0), B_main=(1,1). Their two low intermediate C neighbors have
height b. The signed chronology gives H's selected exit at least ten
reads older than F's selected exit, so H precedes F in the positive
lifted face order of Gamma.

At E the exchange e_E has outgoing L1 on A at MIDDLE M-1, and outgoing
R2 on a LOWER b node D. We prove e_E is NOT a bridge.

## 2. The already forced cleanup is one distinct LOWER leaf

The exact actual consecutive word is

    Y.L1 -> O.L3 -> E.L3 -> Z.L3 -> Y.R2.

All four outgoing edge occurrences before the terminal Y.R2 have level
b. Canonical repair keeps the three L3 transitions unchanged and sends
incoming Y.R2 to outgoing Y.L1. They therefore form ONE canonical
four-edge, four-L, counterclockwise square C at level b.

Its only cycle-graph incidence is the exchange at Y, because its other
three corners are L3. Thus C is a graph LEAF, attached to A by e_Y.
In particular C is not D: outgoing E.R2 is not one of these four edge
occurrences. This retains the source-L old stock; it does not erase the
actual old-stock square or replace it by black input.

## 3. A short physical LEFT chord cuts off a bounded ear

Join the two C centers H=(-3/2,1/2) and F=(1/2,1/2) by the horizontal
segment chi. Apart from its endpoints this chord lies strictly LEFT of
Gamma. It passes through the intermediate L face and the two physical
vertical edges O-E and Z-Y. No other Gamma face or contact lies in its
interior: the two intermediate C-contact neighbors are the fixed low b
faces, and the selected curve stays in maximum C faces. At the endpoints
it leaves through the LEFT sector of the two oppositely oriented RIGHT
bends.

The finite positive lifted Gamma arc from H to F, together with chi
from F back to H, is a simple closed curve in the physical PLANE. It
bounds a bounded Jordan disk Omega on LEFT. Its orientation is fixed by
the downward departure from H and upward arrival at F; locally it is
the region below chi. A winding or short-quotient shortcut is not used:
we first take the actual physical lifts H and F at distance two, then
the unique finite arc of the embedded lifted Gamma between them. The
chronology identifies its direction as H to F. If its quotient drawing
overlaps a translate, the physical Jordan disk still supplies the
bounded separator used below.

Outgoing E.R2 travels W toward B', below chi on the LEFT side of the
outgoing H arc. Hence node D starts strictly inside this ear.

For every sheet j<=b, the only occurrences crossing chi are the two
level-b occurrences on edges O-E and Z-Y, both belonging to the single
cleanup cycle C. Indeed these physical edges have their last occurrence
at level b, and the chord meets no other primal edge. There are no
crossings at lower levels. Choose all corner roundings and exchange
connectors in small primal-cell neighborhoods, away from chi's interior.
Thus no other lower-sheet cycle or lower-level exchange can cross chi.

## 4. A bridge would trap its positive-winding component in that disk

Suppose e_E were a bridge. Its outgoing-R2 component Q cannot reach any
MIDDLE node: the signed collar theorem's path argument would make its
first such node the unique LEFT node A, which lies in the opposite
component. Therefore all nodes of Q have levels <=b and stay on LEFT.

The cleanup leaf C also lies in the opposite component, since its sole
edge e_Y still attaches it directly to A. So Q cannot use the ONLY
lower-sheet crossings of chi. It cannot cross Gamma either. Starting
at D inside Omega, every lifted canonical node and exchange path in Q
therefore remains inside the bounded physical disk Omega.

Every canonical node in Q consequently has winding zero. An essential
node would lift to an unbounded embedded line and could not remain in
this disk. The argument also covers quotient identifications: following
a component path is lifted continuously in physical space, and repeated
use of a nonzero deck displacement cannot stay in a bounded disk.

But the signed chronological bridge formula gives

    total canonical winding of Q=1+m >=1,
    m=floor((T2(E)-T1(E))/P).

This contradicts the zero winding of every node in Q. Therefore

    e_E is nonbridge; in particular N2-C_nodes+1 >=2.           (1)

## 5. Scope and next remaining escape

For this specific same-Gamma row-5 renewal, neither a separate LEFT
middle node nor a LEFT lower essential pair can substitute for graph
nonbridge excess. The bounded-ear argument, not a global ban on lower
essential pairs, removes that bridge possibility. Such lower pairs may
exist elsewhere and are not discarded from any other argument.

Equation (1) forces even positive cycle excess in the full repaired
graph. It does not bound that excess, say it is paid by finite seed mass,
or make it additive over distinct returns. Multiple row-5 suppliers can
share the same cycle space. No planar/Reeb or genus-zero shortcut has
been assumed, and no complete WHITE row-5 connector is constructed.

Sources retained unchanged:
K1_leftmost_branch_free_middle_collar_v2.md, SHA
313509cb42cf3cb2ceb8a395896665aaddc58032de65b0af6a392ca963c3e466;
K1_secondary_return_strand_row5.md, SHA
a46d61d8a2b88f9f8ba8525bf8c1d4d58a1a122c04e443be3e7c968721909e46;
stream_sheet_clocks_and_bridge_sign.md, SHA
552d5aa8cc604cb3899291d688f016652fcd00ab6108e24eb44efa86ea9efe84.
