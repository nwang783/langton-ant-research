# Row-parity obstruction to clean renewable corners

Status: exact elementary proof; independent analytic audit passed 22 October 2026, including the aperiodic extension under its stated hypotheses. This strengthens
the fixed-cap count in `corner_black_wake_budget.md`; it does not rule out
corners that manufacture a permanent black diagonal wake.

## A universal finite-path parity identity

For any finite ant turn path, regardless of whether its initial colors are
consistent, the parity of visits to a physical row y is

    [entry heading horizontal and entry row=y]
    XOR [exit heading horizontal and exit row=y].

The analogous column parity is the XOR of the entry/exit vertical-heading
indicators in that column. This is purely geometric. At every update, the
heading changes between vertical and horizontal. If the new heading is
horizontal, the position stays in the current row, so the horizontal-row
indicator changes precisely at the processed row. If the new heading is
vertical, the indicator is removed from the processed row. These increments
telescope. Column parity is the rotated identity.

In particular a north-to-east cap K from(0,0) to(a,b) has odd row-visit parity
only in row b, and odd column-visit parity only in column0. The identities do
not depend on cap length, its number of rotations, or repeated physical cells.

## Every periodic changing-state corner must emit wake

Let K_0,...,K_(q-1) be a periodic sequence of caps with the same geometric
endpoint(a,b,E). Cap j and its S arms occur translated by j*d, d=(-1,+1).
Impose the same maturation/isolation hypothesis as in the fixed-cap note.
Group all complete events modulo q*d. The quotient remembers row and column
residues modulo q.

The incoming arms' parity is exactly their q unmatched endpoint cells
(1,-1)+j*d, one in each row residue and each column residue. Their balanced
interior reads cancel after pairing an R from phase j with an L from phase
j+1, cyclically modulo q. Similarly the outgoing arms reduce to
(a,b-1)+j*d, again one endpoint in every row and column residue. Thus the two
arm endpoint families have total even parity in every row/column residue.

Each shifted cap has odd row parity only at b+j modulo q. Summing the q caps
therefore gives odd parity in EVERY row residue. Likewise their odd entry
columns are -j modulo q, one in every column residue. Consequently the final
odd complete classes must have odd cardinality in every row residue and in
every column residue.

Let g be their number. Then

    g >= q.

Combining this with the earlier turn-count identity gives

    g = sum_j(r(K_j)-l(K_j)) - 2q,
    g = -q (mod4),
    g >= q        if q is even,
    g >= q+2      if q is odd.

In particular g=0 is impossible for EVERY periodic corner-state cycle, not
only fixed caps. The preliminary count alone had permitted q=4; the row
identity supplies the missing obstruction. A hypothetical minimum q-phase
wake has odd degree at every vertex of the bipartite graph of row and column
residues; at g=q, it is a perfect matching of those residues.

This theorem explains why the clean four-phase finite-library systems already
contradict their unconditional linear equations, before cap turn guards are
used. Those bounded computations are not the proof of this all-length result.

## Aperiodic bounded-geometry extension

The same row identity excludes a clean aperiodic corner with caps K_j that
all end at(a,b,E) and all lie in one fixed finite relative neighborhood, even
when their turn words and lengths have no period. Require maturation/isolation
and that no additional reads occur at the corner's completed cells.

At a sufficiently far row y, caps contribute odd total visit parity: precisely
K_(y-b) has its exit row there, while all other cap contributions are even.
Only finitely many caps touch that row because their relative footprints are
uniformly bounded.

All following parity sums are restricted to the fixed diagonal band containing
all cap footprints and endpoint classes. Remote finite-arm endpoints lie outside
this band; maturation gives the full stated arm events inside it.

The incoming half-arms, taken over all sufficiently advanced laps, cancel in
pairs except for one cell in that row, at x=-y in the chosen normalization.
Indeed the arm of index j>y contributes one read each at x=-j and x=1-j;
these cancel for x<-y and leave the rightmost endpoint x=-y.
The outgoing half-arms cancel except for one cell at x=a+b-y-1: the R half-row
of lap y-b and the L half-row of lap y-b+1 have starting x coordinates differing
by one. Thus the arms contribute even total row parity. Adding the caps leaves
odd total visit parity in every sufficiently far row.

All noncancelled cells lie in a fixed-width diagonal band. Every cell has a
finite complete history under the bounded-footprint and isolation hypotheses.
Since the initial board is finite, each sufficiently far cell is initially
white. Therefore the completed corner history leaves an odd, nonzero number
of black cells in every sufficiently far row of that band. The rotated
argument gives the corresponding column statement. No periodicity is used.

The conclusion is unavoidable PERMANENT WAKE, not failure of renewal. A
self-reproducing track with such debris is still an open construction target.
