# A white translating front cannot fit in two horizontal read rows

23 October 2026, 09:08 UTC. Analytic candidate; independent review pending.

This is an ALL-MULTIPLICITY width lower bound, not an all-width drift
exclusion. No claim of external novelty is made.

Let an initially-white complete translating ant front have nonzero full
horizontal drift (2K,0), K any nonzero integer. Its physical read support
cannot be contained in two adjacent horizontal lattice rows. Genuine
quarter rotations give the analogous statement for vertical drift.

The proof is restricted to the bi-infinite complete-front lift: every event
has a predecessor. A finite trace or an arbitrary one-sided trajectory
can have an initial-head exception, and is NOT included in this statement.

## Exact boundary words

Translate coordinates and choose the checker sector so the four cell
families are

    A_i=(2i,0),    B_i=(2i+1,0),
    C_i=(2i,1),    D_i=(2i+1,1),       i in Z.

At A and D, departures are vertical. At B and C, departures are horizontal.
Since no read can lie outside rows0,1, the complete histories are forced:

    A: departures N; arrivals W,E,W,E,...
    B: arrivals S; departures W,E,W,E,...
    C: arrivals N; departures E,W,E,W,...
    D: departures S; arrivals E,W,E,W,... .

Ranks j start at zero in each cell's COMPLETE physical chronology, with R
at even j and L at odd j. Empty cells cause no exception.

The kth traversal of a fixed directed physical edge is necessarily the
kth corresponding arrival at its target. Consequently every matched edge
in the displayed words preserves the entire rank j, not just its parity:
vertical ports contain all ranks in order; each horizontal port contains
exactly either the even or the odd ranks, in order. This is a physical-edge
ordinal statement and never folds the supplied drift to a primitive one.

## Every event lies on an impossible zero-voltage four-cycle

Take any B_i event of rank j. If j is even its four successive events are

    B_i[j] -> A_i[j] -> C_i[j] -> D_i[j] -> B_i[j].

If j is odd they are

    B_i[j] -> A_(i+1)[j] -> C_(i+1)[j] -> D_i[j] -> B_i[j].

The existence of each successor and the equality of its complete rank
follow from physical edge-ordinal matching. Each is a unit-face loop in
the physical plane, returning to the SAME rank of the SAME physical cell.
Actual event times strictly increase along successors, so this is
impossible. All active events reach a B event in at most three steps.

Equivalently, in the actual full-drift cylinder every successor component
would be a contractible four-cycle of total seam zero. It cannot be the
single whole-front event cycle of seam one. The argument works at arbitrary
K, arbitrary complete read counts, arbitrary period, and does not rely on a
multiplicity or width search.

A one-row support is already impossible because the heading alternates
horizontal and vertical at every step. Therefore a horizontal white front
must read at least THREE distinct horizontal rows. This does not exclude
three or more rows, axis-four fronts at higher multiplicities, prepared
input strips, or nonperiodic paths using infinitely many reads of a cell.
