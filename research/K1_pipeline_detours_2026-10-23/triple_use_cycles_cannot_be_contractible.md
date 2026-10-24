# Literal first/last crossing excludes contractible triple-use cycles

24 October 2026. Complete WHITE cap-four translating front, actual full
P and nonzero d. No K1, global maximum, selected Gamma or output-zero
hypothesis is needed. The physical graph G3(c) is defined and locally
classified in the independently signed3ffd2f42.

THEOREM: no component of G3(c) can be a finite physical directed cycle.
Equivalently, a cyclic component in the actual full quotient must be
essential; a contractible quotient cycle is impossible.

This is a chronological first/last theorem about ACTUAL edge uses.
It does not treat a spatial G3 circuit as a consecutive ant itinerary.

## 1. Exact complete boundary inventory

Every vertex of a G3 cycle has four WHITE reads R0,L1,R2,L3 and one
triple-use incoming port and one triple-use outgoing port. The other
ports are single-use. Up to rotation there are exactly FOUR types:

    type          triple input ranks  triple output ranks  single ports
    RIGHT EEEW        0,1,2                0,2,3               LEFT
    RIGHT EWEE        0,2,3                0,1,2               LEFT
    LEFT  EEWE        0,1,3                1,2,3               RIGHT
    LEFT  WEEE        1,2,3                0,1,3               RIGHT.

The representative headings use incoming axis E/W. RIGHT/LEFT denotes
the geometric turn of the oriented G3 path: for EEEW/EWEE it arrives
E and leaves S; for EEWE/WEEE it arrives E and leaves N. The two
unused single ports are both on the stated geometric side of that
oriented corner. E/W-swapped cases and rotations have the same ranks.

In particular every R0 read at a boundary vertex uses at least one
cycle edge, and every L3 read does too. This stays true for all four
types, not only the two types selected as first and last below.

## 2. The first actual cycle edge is entered from RIGHT at positive R0

Suppose gamma is a finite physical directed G3 cycle. Each of its
finitely many edges has exactly three traversals in the complete
history, so its earliest actual traversal exists. At that edge's
source read, the incoming edge cannot be a gamma edge: that would
have been an earlier traversal. Hence this read uses the single input.
Nor can this vertex have an earlier triple output, which would also
be an earlier gamma traversal.

The complete table leaves ONLY the positive-flat LEFT WEEE type at
its R0. The incoming single port is RIGHT of gamma. Thus immediately
before the first cycle traversal the actual cursor lies on gamma's
RIGHT side.

There was NO earlier read at any gamma vertex. If there were, its R0
would be at or before that read and would use a gamma edge, contradicting
the first traversal. Consequently the cursor cannot have crossed gamma
at a boundary vertex before this first entry. Unit square-lattice edges
also cannot cross a gamma edge in its interior without using it.

This handles unused chords between nonconsecutive gamma vertices too:
if the incoming single edge came from another gamma vertex, that earlier
read would already contradict the first traversal. The immediately
preceding position is genuinely on the open RIGHT side, not another
boundary point.

## 3. The last actual cycle edge leaves to LEFT at strict L3

The latest actual traversal exists as well. On arrival at its target
vertex, the ant cannot immediately depart by a gamma edge, which would
be a later traversal. Therefore the read uses the single output. It
cannot have any later triple input at this same cell, since that would
require a later gamma traversal.

The complete table leaves ONLY strict same-R RIGHT EWEE at L3. Its
outgoing single port is LEFT of gamma. Thus the cursor next lies on
gamma's open LEFT side.

There can be NO later read at any gamma vertex: any such read implies
that cell's L3 is still to occur or is that read, and every L3 uses a
gamma edge. That contradicts latest traversal. This also excludes a
single outgoing chord landing at another gamma vertex. The whole
future cursor path avoids the boundary and stays on its LEFT side.

## 4. Either contractible orientation contradicts translation

A finite physical G3 cycle is a simple embedded square-lattice Jordan
curve: G3 has only adjacent two-port internal vertices and no degree-four
crossing. Its right and left sides are therefore well-defined.

If gamma is CLOCKWISE, its RIGHT side is the bounded interior. Section2
places the cursor there before the first traversal, with the entire
past avoiding gamma. Hence the past must remain in that bounded
interior. This is impossible for a complete translating history with
nonzero d: x(t+P)=x(t)+d puts the cursor outside any fixed bounded set
for all sufficiently negative t.

If gamma is COUNTERCLOCKWISE, its LEFT side is the bounded interior.
Section3 places the cursor there after the last traversal, with the
entire future avoiding gamma. The same complete translated periodicity
makes this impossible for all sufficiently positive t.

Both orientations are excluded. The argument uses literal port ranks,
first/last physical traversals and the actual cursor. No spatial flow
cycle is falsely promoted to a chronological cycle.

## 5. Exact scope

An essential quotient cycle lifts to an infinite periodic physical
curve and has no globally first/last edge use. It is NOT excluded.
The theorem adds no period cost, no root count per renewal and no
original-fuel bound. WHITE four-read boundary histories are essential;
black-start LRLR boundary cases are not imported. The conclusion may
also be used for any prepared situation whose boundary vertices obey
the displayed complete WHITE inventory and whose cursor is eventually
outside the bounded cycle in both time directions, but no such extension
is needed here.

Control `triple_use_cycle_first_last_crossing_table.py/json` reconstructs
all eight rotated-axis internal histories, actual incoming/outgoing
ranks, single-port sides and the only first/last eligible reads. It
performs no front or period scan. A prescribed prepared W20 check has
an essential G3 staircase rather than a contractible counterexample;
that finite existing control is not a WHITE-front existence claim.
