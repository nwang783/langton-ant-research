# Exact event interface and local normalizer for the bi-exterior section

23 October 2026, 21:51 UTC. Author deduction from the simultaneous-return
note, not independently audited. This does not change that note's frozen text.

Use the same paired cursors and TWO white diagonal graphs. An actual update
has these white-graph effects:

    R: delete both white edges; z traverses its deleted edge, w stays.
    L: insert both white edges; z stays, w traverses its inserted edge.

Therefore:

1. From a bi-exterior state an L update ALWAYS gives another bi-exterior
   state. Inserting white edges preserves all existing infinite connections,
   and w moves along a newly present white edge from an already infinite
   component.
2. From a non-bi-exterior state an R update CANNOT give a bi-exterior state.
   Deleting white edges cannot make a finite component infinite. If z is
   finite, traversing the just-deleted edge still ends inside its former
   finite component. If w is finite, staying at w cannot restore infinity.
3. Consequently every nontrivial section excursion starts on an R and ends
   on an L. Its intervening arbitrary word and complete mutable board must
   still be retained. No other language restriction is asserted.

## Exact intrinsic locality of the episode

Let R be the fixed terminal entry rectangle supplied by the simultaneous-
return theorem. Until the first simultaneous return, all physical reads lie
inside R and every exterior black cell stays unchanged. More strongly, the
stopping predicate is intrinsic to R too.

Indeed, at every pre-return state, every black cycle in either lattice lies
wholly in ONE of the fixed separated entry rectangles. If its bounding box
is another rectangle R', it cannot enclose either active vertex at a physical
cell inside R, by the same geometric trapping argument. Only cycles supplied
by the evolving black cells inside R can make an active vertex white-finite.
The same conclusion holds at the return state, whose head is in R or a single
unit step outside the entire fixed rectangle union.

Thus deleting all exterior black cells, running the physical ant from the
same entry pose to its first bi-exterior state, then restoring the unchanged
exterior gives EXACTLY the original return time, head, heading, and interior
board. This is a mathematical coupling statement, not an instruction to edit
the actual board. It remains valid for arbitrary unchanged external boards
contained in other rectangles at Chebyshev cell distance at least two from R
and from each other. Arbitrary exterior changes without that separation or
cycle-containment premise are NOT covered.

The map taking a finite complete state to its first bi-exterior state,
including time zero, is a total computable idempotent normalizer. It carries
the whole mutable interior, not finitely many summary labels. Its spatial
reach, time, and return mass have the bounds in the main note. The normalized
section map is: take one actual physical step, then apply this normalizer.
It is a total exact full-board map, not a finite-state quotient.

## Actual smallest-needed countercontrol to a mass descent inference

The blank ant's exact tick7 state is bi-exterior, at pose(0,1,E), with five
black cells. Its next three actual turns are RRL. At ticks8 and9 the paired
white-exterior flags are(true,false); at tick10 both are exterior, pose
(-1,-1,S), with SIX black cells.

Thus even a nontrivial complete section excursion can INCREASE black mass.
No well-founded rank is obtained by merely stopping at this section. The
literal entry board, word and flags are in
first_positive_mass_return_countercontrol.json. For a larger control, the
blank orbit's tick7408..7451 excursion raises mass524 to533; this is saved in
positive_mass_return_countercontrol.json. These finite examples only refute
the proposed monotonicity. They are not noncapture evidence.

The actual blank tick582..585 example in alternating_trap_witness.json also
shows why one cannot replace the simultaneous section by the first individual
white exit: the exterior flags go(true,false),(false,false),(false,true),
then(true,true).

## What the reduction removes, and what it deliberately retains

An indefinitely continuing relay between finite white pockets is impossible
before a simultaneous exterior checkpoint. Every such episode has one fixed
small entry rectangle and a finite exact local response. But the response
may add mass and preserve or create arbitrary interior archive structure.
A trajectory may return to this section arbitrarily often, depart its old
rectangle later, build new ones, and read old external bits.

The proof does not charge the episode's cost to initial black count across
many returns. It does not erase dormant components, convert frozen loops to
a LIFO stack, or substitute a bounded boundary summary. The unsolved global
part is the complete stateful sequence of outer returns and its long-range
archive reactivations.
