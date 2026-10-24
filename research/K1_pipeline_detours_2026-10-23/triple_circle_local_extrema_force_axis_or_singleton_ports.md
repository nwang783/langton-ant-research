# G3 local extrema force axis geometry or explicit singleton ports

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d and positive output retained. Any C level c, either winding sign,
and arbitrary positive/negative middle incidences. No K1 or root-free
premise. Pending independent review.

Let gamma be a G3(c) cycle. The entire physical circle preserves ONE C
level component at c and ONE L level component Q at m=c-3. Turns below
mean the physical gamma edge turns, NOT max-face birth turns.

## 1. Every L,R,L triple forces a singleton or a higher C neighbor

Normalize three consecutive corners to

    B_(k-1)=(k,k-1), A_k=(k,k), B_k=(k+1,k).

Both modes at every corner are retained:

    A: NNNS or NSNN; B: EEWE or WEEE.

At U=(k+1,k-1), the remaining unit-face corner, B_k supplies exactly one
S arrival and B_(k-1) accepts exactly one W departure. All complete
WHITE possibilities at U are

    S, NNNS, NSNN.

If U=S, it is an actual singleton-R output and the opposite C face has
height c-1. In the other modes U is four-read, and the opposite C face
has height c+2. The shared NW C face inside the three-edge arc is at c;
both L faces at U are c-1 in all cases.

Therefore if gamma's C level component is LOCALLY MAXIMAL, every LRL
triple has an explicit adjacent singleton-R output incident to that
component. In particular this holds for c=M. This is one local witness,
not an injection from repeated overlapping triples or renewals.

## 2. Every R,L,R triple forces a strictly lower L neighbor

Normalize the three consecutive corners instead to

    A_k=(k,k), B_k=(k+1,k), A_(k+1)=(k+1,k+1).

The inside unit face is the low L face Q0 at lower-left(k,k), height
m=c-3. At its fourth corner W=(k,k+1), A_(k+1) supplies exactly one
incoming W and A_k accepts exactly one outgoing S. Exhaust every
complete WHITE history on incoming E/W. Exactly four remain:

    EEW, WEE, EEWE, WEEE.

At each, the shared SE L face is m and both C faces are c-2. The opposite
NW L face has height

    c-4=m-1 for EEW/WEE;
    c-5=m-2 for EEWE/WEEE.

This uses all modes, including both odd three-read histories. There is
NO BLACK-first singleton-L alternative in an original WHITE front.
Thus the component Q has a strictly lower corner neighbor whenever an
RLR triple occurs. If Q is LOCALLY MINIMAL, RLR is impossible, regardless
of whether Q has other odd corners or a root-free reverse birth curve.

## 3. A G3 circle incident to a local L minimum is necessarily axis

Gamma is a simple embedded essential physical circle by signed5036e7c2.
It cannot have THREE consecutive equal turns: three same90-degree turns
complete a four-edge physical square and revisit the preceding vertex,
contradicting essential simplicity. Hence each cyclic L or R run has
length at most two.

If Q is locally minimal, section2 forbids RLR, so every L run has length
at least two, hence exactly two. An essential translated circle has
zero total signed turning and equal L/R counts. There are equally many
L and R runs, so each R run must also have length two. Consequently

    gamma's physical word is cyclically (RRLL)^a,
    ell=4a, and actual d is axis with ||d||_infinity=2a.

Winding may be+1 or-1; the direction of d is handled by that actual
winding and no primitive quotient reduction is made. The statement
allows odd corners of Q and arbitrary mixed middle signs. It is stronger
than a root-free-only restriction, but it concerns minima incident to
a G3 CYCLE, not arbitrary minima without such a boundary.

For a NON-AXIS front, no G3 cycle can lie beside a locally minimal L
plateau. In particular a G3 cycle at the global minimum L level is
impossible in a non-axis front. Such a cycle may instead have a lower
neighbor (and eventually a deeper minimum); source-sink G3 paths with
odd endpoints remain allowed. Axis RRLL circles remain an actual open
assembly mechanism; no whole-front exclusion follows.

## 4. Exact scope and controls

The all-negative G3 family is already independently excluded by
 a31d409e. The present local corner statements do not assume that
homogeneity and apply to genuinely mixed circles. They do not produce
an odd root for every return, bound output by initial fuel, classify
arbitrary contours, or prove a translating positive exists.

triple_circle_peak_valley_corner_inventory.py/json exhausts only fixed
1..4-read local WHITE histories and their exact face levels. No period,
drift, width, radius, seed or front scan is performed.
