# Canonical sheet clocks and the chronological sign of a bridge

23 October 2026, 16:29 UTC. Exact addendum to the pending sheet-exchange
interface. No delay is made additive over unrelated paths and no sheet
of zero total homology is treated as finite fuel.

Use the full notation and hypotheses of
chronological_stream_sheet_exchange.md. Let sigma be the actual one-cycle
successor on P edge-occurrence classes, sigma_0 the repaired sheet
permutation, and G its connected cycle graph. At a two-R physical cell v
put

    Delta_v=T2(v)-T1(v)=4q_v, q_v>=1.

The multiple of four is the signed same-cell return fact. Delta_v is an
actual physical return span and may exceed P.

## 1. Exact clocks on each repaired cycle

Give a physical outgoing edge occurrence its actual departure time.
For a repaired successor transition, its time difference is

    incoming L1 -> outgoing R2: 1+Delta_v;
    incoming R2 -> outgoing L1: 1-Delta_v;
    every unchanged transition: 1.

These follow directly from the incoming edge times T1-1 and T2-1.
For any canonical sheet cycle gamma, let ell be its edge length and k
its actual full-drift winding. Then

    kP = ell + 4(sum_positive q_v - sum_negative q_v).             (1)

Occurrences and signs are retained separately even if one physical cell
supplies both transitions to different cycles. These canonical sheet
circles are embedded, so k is 0,+1 or -1. This is not a primitivity claim
about the old mixed-rank dependency cycles.

For a maximum C four-edge cycle, (1) becomes

    sum_negative q_v - sum_positive q_v =1,

recovering the signed first-port curl with its actual L1/R2 delays.

A contractible canonical cycle has a well-defined earliest actual edge
in any physical lift. Its predecessor transition cannot be unchanged or
positive, since those advance actual time. Therefore that earliest edge
is outgoing L1 at a negative repaired transition. Its actual incoming
L1 edge, one read earlier, belongs to the adjacent partner sheet-cycle.
If that partner is also contractible, its own earliest time is strictly
smaller. Essential partner cycles and full-drift shifts are retained;
no global acyclic forest is inferred merely from quotient finiteness.

## 2. Cutting one exchange in actual time

Undo just ONE exchange from sigma, keeping all other actual successors.
Equivalently form sigma_cut=tau_v sigma, where tau_v exchanges outgoing
L1 and R2. A transposition cuts the single P-cycle into two cycles.
The cycle containing outgoing L1 follows the actual forward itinerary
from L1 to the R2 occurrence modulo the period, then closes using the
repaired transition back to outgoing L1.

Write

    Delta_v=mP+r, m=floor(Delta_v/P)>=0, 0<r<P.

The strict inequalities hold: Delta_v cannot equal a positive multiple
of P, because actual time advance mP displaces the ant by m*d, whereas
the two physical reads are at the SAME v and d is nonzero.

The outgoing-L1 cut cycle has length r and winding -m. Indeed the actual
r-step segment starting at L1(v) reaches the translated R2 event at
v-m*d. The other cut cycle therefore has length P-r and winding 1+m.
This retains potentially nonprimitive cut-cycle windings. Neither cut
cycle is asserted embedded.

## 3. A bridge separates nonpositive from positive total winding

Suppose v's exchange edge is a BRIDGE of G. Removing it separates G into
two components, one containing outgoing L1's canonical node and the
other containing outgoing R2's canonical node. All other exchange
transpositions stay inside one of these two node unions. The two unions
are therefore invariant under sigma_cut. Since sigma_cut has precisely
two cycles, each union is exactly one cut cycle's edge set.

Its total canonical-node winding is unchanged by internal repairs.
Consequently

    total winding on the outgoing-L1 side = -m <=0;
    total winding on the outgoing-R2 side = 1+m >=1.               (2)

Both separated subgraphs also have nonnegative EVEN cycle excess,
because each internally repaired successor is a single cycle on its
own edge set; the same connectivity/parity proof applies there.

Equation (2) is an exact chronology orientation on bridges, not an
assumption that all canonical nodes have nonnegative winding. Opposite
essential cycles on a zero-total-homology sheet must not be discarded.

## 4. One safe leaf corollary

If a global top-sheet max-C four-edge node is a LEAF of G, its winding
zero rules out the outgoing-R2 side of (2). It must be the outgoing-L1
side, with m=0. Its cut-cycle length is exactly four, so

    Delta_v=4.

Thus a top max-face leaf has an actual four-step L1-to-R2 boundary
return, the old local LRRR control, rather than a free terminal. A leaf
on another sheet is not asserted to be a four-edge loop: its full cycle
length and winding must be retained. A four-L old-stock loop is allowed
when its actual canonical geometry supplies it.

This addendum supplies clocked global sheet coupling. It does not prove
a bound on cycle excess, forbid the row-5 near-return, or make local
return spans into disjoint global payments.
