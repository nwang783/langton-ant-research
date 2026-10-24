# Finite frontier chronology zones: a sound all-width relaxation

23 October 2026, 02:43 UTC. The analytic framework and the cap-ten and cap-twelve unit-diagonal
certificates have passed independent audit. General full drift (2,2),
cap five has also passed independent reconstruction. The unit-diagonal
applications are method controls: the retained source already excludes
that drift without any multiplicity cap.

The input is a fixed full diagonal drift (currently the implementation
uses (1,1)) and a finite visit cap. Each row has finitely many complete
white histories. All directed-edge counts and ordinal traversal matches
are exact. Previously signed local-window tests may also be applied.

## Partial successor components

Expose rows from the empty lower exterior upward. Each processed event has
at most one predecessor and one successor, and missing arcs can only meet
the latest frontier row. Unless a closed component has appeared, every
partial successor component is a directed path. Its first and last events
are frontier events. A singleton is a zero-edge path with the same two
endpoints. Compress each path to its endpoints, retaining its total seam
voltage modulo q (q=2 in the saved tests).

When a row is appended, splice old paths with all new-row event nodes by
the exact internal physical arcs. Every old missing port is now resolved.
If a closed cycle appears alongside another component, reject: no later
row can reconnect it. A sole closed cycle must be the entire global event
cycle. Its voltage must be1 modulo q; a sole such cycle is retained as an
explicit possible-front outcome unless another necessary test fails.
No positive result is inferred from parity alone.

## Cyclic order of path blocks

In a genuine global event cycle, each unfinished path is one consecutive
block of events. Therefore the old path blocks have a cyclic order, and
splicing cannot interleave or rearrange them. Store this order. Choose its
canonical cut immediately before the path with the smallest frontier
start-event index. Each path lies wholly on one side of this cut.

For every candidate ordering of the new path blocks, concatenate the old
path IDs encountered while traversing them. It must be a cyclic rotation
of the stored old order. Enumerate every permutation of new blocks modulo
cyclic rotation, fixing the block with smallest start index first. This
is exhaustive even for new blocks containing no old events.

A sole closed component is cut at its smallest new-row event index; its
old block order must satisfy the same cyclic-rotation condition.

## Integer normalized-clock variables

For the eventual full period P, write each representative event clock as

    t_e/P = phi_e + z_e,

where 0<=phi_e<1 and z_e is an integer. All event phases phi_e are distinct.
The chosen cyclic cut determines their linear order, but their exact
fractional values are unnecessary.

If local visits j and j+1 are chronologically consecutive, t_j<t_(j+1)
is equivalent to

    z_j-z_(j+1) <= 0       if phi_j<phi_(j+1),
    z_j-z_(j+1) <= -1      otherwise.

For a physical successor arc u->v with seam voltage k, the relation
`t_v+kP=t_u+1` gives

    z_v-z_u = -k + 1[phi_v<phi_u].

For an unfinished path the cut is outside the entire path, so none of
its actual successor arcs crosses the cut. In a sole closed cycle exactly
one arc crosses it. The sparse compressed skeleton retains the relative
phase order of all currently named new-row events, which determines the
new local inequalities and the crossing indicator of each newly exposed
physical arc. The exact duration of old compressed paths is not assumed.

## Cut reanchoring

Let the stored old path order be0,1,...,r-1. Suppose its order in the new
cut is a,a+1,...,r-1,0,...,a-1. Apart from one irrelevant common integer
shift, every old normalized z variable in a block with ID<a decreases by
one, and the others are unchanged. This follows by subtracting the new
cut phase from t/P and reducing the fractional part to [0,1).

Thus a bound z_u-z_v<=b transforms to b+delta_u-delta_v, where delta is
-1 on that prefix of old blocks and0 elsewhere. The new cut is at a new
frontier event, between old blocks, so it never divides an old compressed
path. This coordinate change must be applied to the whole old difference-
bound matrix before adding new constraints.

## Projection and finite safe weakening

A difference-bound matrix stores all current inequalities z_u-z_v<=b on
old path endpoints. Add the new event variables and exact physical-arc and
local-order constraints above, then take ordinary min-plus transitive
closure. A negative diagonal proves inconsistency and permits rejection.
All constants are integers, so integer difference constraints introduce
no extra feasibility issue. Discarding retired variables after closure
is exact existential projection for these difference constraints.

To make the state space finite, fix M>=0. After projecting onto new path
endpoints, weaken every finite bound b as follows:

    b>M   becomes infinity;
    b<-M  becomes -M;
    otherwise it remains b.

Both replacements weaken the inequality. The matrix is stored AFTER this
weakening and need not be transitively closed until the next transition.
All its entries belong to the finite alphabet {-M,...,M,infinity}.
Consequently histories, path endpoint pairings, path voltage residues,
cyclic block orders and weakened matrices form a genuinely finite graph.
An actual front always has a represented feasible zone; spurious zones
may survive, but no true front can be lost merely by the weakening.

## All-width bridge and proposed certificates

Start with empty rows and an empty matrix. A true finite-width front would
follow this finite graph and eventually seal one whole voltage-one cycle.
If complete graph reachability has no permitted sole-cycle outcome, the
front is impossible at every width and period. A state limit is UNKNOWN;
a surviving whole-cycle zone is only a relaxation unless separately replayed.

Producer: `probe_diagonal_zone_frontier.py`.
Proposed cap-eight, two-row, M=2, q=2 certificate:260 states,270 accepted
edges. Proposed cap-ten, three-row, M=2, q=2 certificate:747 states,747
accepted edges. Neither run encounters a potential whole-front outcome.
Files have prefix `diagonal_zone_cap{cap}_window{k}_bound2_mod2`.
These are not signed until the analytic cut/zone proof and complete finite
reconstruction have passed independent review.

## Independent signoff and provenance correction

`../audits/check_frontier_clock_zones_independent.py` regenerates all
unpruned histories, physical splices and cut changes, and uses independent
Bellman-Ford closure rather than the producer's min-plus implementation.
It verifies the complete cap-ten and cap-twelve reachable graphs. The
finite infinity sentinel is larger than any relevant bounded-edge simple
path sum, so it cannot suppress a genuine finite constraint.

The earlier source
`../sources/kehao95-core/wake_synthesis/verification/unit_diagonal_analytic/PROOF.md`
already gives an analytic exclusion of full unit-diagonal drift at every
cap. The new unit-diagonal certificates are therefore controls for this
general finite abstraction, not improvements to that classification.

The same proof works for any fixed finite row frontier: use event IDs
(column, local rank), with the lexicographically smallest start as the
canonical cut. Full diagonal drift (n,n) has representatives (i,i+t),
0<=i<n. Physical splicing is the only geometry-dependent change.
The separate generalized independent checker signs the cap-five
full-drift (2,2) graph; see `two_diagonal_zone_exclusion.md`.
