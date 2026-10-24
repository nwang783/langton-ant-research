# All-length budget for an outward solid-rail corner

Status: exact elementary necessary condition, analytically audited.
Scope: a fixed finite north-to-east cap K between semi-infinite S=RLLR arms,
whose successive occurrences are translated by d=(-1,+1). Assume maturation
and isolation: for each fixed translated cell class, all stated half-arm events
eventually occur, and no other circuit region reads those physical cells.
For fixed bounded caps on separated growing rectangle sides, this is the
intended geometric condition; it must be checked in any proposed full device.
Without isolation an external read can repair a leading L or erase an odd
wake, and the conclusion need not apply. This is not an
obstruction to arbitrary tracks, changing cap geometries, or all ant orbits.

Normalize the cap entry to(0,0,N), exit to(a,b,E). The incoming arm advances
north to the entry; the outgoing arm advances east from the exit. Each S
period shifts its solid black right-hand rail one cell left.

## Complete translation classes of the arms

A physical cell class modulo d is specified by s=x+y. Chronological events
at a fixed cell are ordered by increasing x, then within-lap phase, because
the longitudinal rank along d is -x.

The incoming half-arm supplies, for each s<0:

    R at (0,s), then L at (1,s-1).

At s=0 it supplies only L at(1,-1). There are no incoming-arm reads for s>0.
The cap has not yet begun at any incoming-arm phase.

The outgoing half-arm supplies, for each s>=a+b:

    R at (s-b,b), then L at(s-b+1,b-1).

At s=a+b-1 it supplies only L at(a,b-1). There are no outgoing-arm reads at
smaller s. All outgoing-arm phases follow the cap.

When both arms and cap contribute to one class, their events must be merged
in the stated rank/phase order. The two RL pairs above need not remain adjacent
after merging; the argument below uses only their net counts, not adjacency.
Outside the finite range containing all cap sums x+y and the two endpoint
classes, the classes are pure RL and have zero net excess.

## Finite-support necessity

If this corner is used indefinitely in an expanding finite-seed circuit,
then every fixed complete class eventually encounters only cells that were
initially white. The cell's full ordered event string must startR and
alternate. Its number of R reads minus L reads is therefore either0 or1;
it is1 exactly for an odd-length class, which remains permanently black after
its last read. No finite initial seed can pay for a leading L at infinitely
many translations of one class.

Let r(K),l(K) be the counts in the finite cap. Sum R-minus-L over the complete
classes in the finite nontrivial range. The arms contribute exactly -2, one
unmatched L at each endpoint (possibly in the same class). The cap contributes
r(K)-l(K). Therefore

    number of odd complete classes = r(K)-l(K)-2 >= 0.

Since K changes heading from north to east,

    r(K)-l(K) = 1 (mod 4).

Consequently every such renewable cap must satisfy

    r(K)-l(K) >= 5,
    number of odd classes = r(K)-l(K)-2 = 3 (mod 4),

and in particular it leaves at least three black diagonal wake classes.

## What is ruled out and what is not

The elementary bend RLR has r-l=1, so its budget is -1. Direct chronology
locates the shortage precisely: class s=1 consists of a single L. It therefore
requires a new initially black corner cell each lap and cannot renew from a
finite initial board, regardless of the distant seam used by the rest of the
circuit (provided no other read source reaches this remote corner region).

A clean outward corner with no odd complete classes is also impossible at any
length: it would require r-l=2, inconsistent with a quarter turn. This does
not exclude caps with extra rotations and a permanent diagonal black wake.
Those caps are the remaining construction target, not a disproved possibility.

## Changing corner states: an essential limitation

For a q-phase cycle of caps K_0,...,K_(q-1) with common geometric endpoint,
use translation q*d and retain the q separate within-period phases. Each phase
contributes two unmatched arm L reads, so under the same maturation/isolation
premise the corresponding budget is

    g = sum_j (r(K_j)-l(K_j)) - 2q >= 0,
    g = -q (mod 4).

Thus the fixed-cap lower bound of three wake classes must NOT be imposed on
arbitrary changing-state corners. For q=4 a clean cycle is not excluded: cap
excesses5,1,1,1 sum to8 and give g=0. This was a useful count-level construction target, not a successful corner.
The subsequent row-parity theorem in `corner_row_parity_obstruction.md` now
excludes clean cycles for every q; debris-emitting cycles remain open. Exact two-phase tests with caps through17
found no local corner, but neither that finite search nor this budget settles
four-phase or aperiodic changing corner states.
