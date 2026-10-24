# The cap-seven structural boundary, without profile expansion

24 October 2026. Author exact structural certificates pending independent audit.
This does not modify the independently passed cap-six theorem.

## First new recurrent core

The cap-seven local kernel has 72,284 rooted active shapes, 550 passive shape
types and 63,244 cap-preserving transitions. Unlike caps at most six, deleting
the empty-active state does NOT leave a DAG. There is exactly one nonempty
cyclic SCC:

    states {98,299,635,6582,9707,41725}.

It has exactly SIX internal edges, one directed cycle with turn word RRLLLL.
The compact certificate checks all internal edges and a topological order of
the entire remaining condensation; no other recurrent core or return path is
being omitted.

At normalized entry (0,0),north, the active component is
C={(1,-1),(2,-1),(2,0)}. The first R imports the complete dimer
D={(-1,-1),(-1,0)}. No component is emitted during the six updates. The head
ends at (1,-1),south, with active component D union {(0,0)}. The same normalized
state is restored, while total black count has decreased by two.

This local cycle is not physically repeatable. At the next cycle's entry the
required imported dimer would be {(2,-1),(2,0)}, exactly two edges just deleted
by the first loop. No intervening update restores them. The next prescribed
R import therefore contradicts the actual lifetimes and full component state.
The physical-lift analysis froze this independently checked argument in
kernel_cycle_lift_2026-10-24/CAP7_NONEMPTY_CORE_DOUBLE_LOOP_OBSTRUCTION.md.
The literal turn word RRLLLL twice MAY still execute; it is the intended full
component recurrence, not merely its turn spelling, that fails.

## A reusable symbolic replacement for literal acyclicity

Two different mechanisms control the core, and should not be conflated.

1. Pure resource criterion, independent of the physical overlap. Every cycle
in the nonempty kernel decreases total black count: the unique elementary
cycle has length six and change -2. There is an exact integer offset A(C),
0<=A<=34, such that every cap-preserving transition with nonempty endpoints
satisfies

    A(C_after)+3*|B_after| <= A(C_before)+3*|B_before|-1.

The checker verifies this on every edge. The offsets are constructed on the
condensation DAG, with cycle offsets 8,4,0,2,4,6. Therefore on finite support a
nonempty cap-seven excursion must reach empty or exit the cap. This is a
special case of a general finite-kernel criterion: if every directed cycle
has strictly negative black-count drift, a sufficiently large multiplier of
black count plus a bounded state offset gives a strict descent rank.

2. Spatial history refinement. From any phase of the six-state core, the anchor
state is reached in at most five internal updates. One complete loop then
cannot be followed by its next required import. Hence at most eleven internal
transitions, or twelve core cuts, occur in one contiguous core visit. Because
the condensed graph is acyclic, an excursion cannot leave and re-enter the
core before visiting empty. A weighted DAG calculation, assigning weight 12
to the core and 1 to every other nonempty vertex, bounds the entire nonempty
excursion by 33 cuts. This bound is conditional on the separate exact
next-import contradiction, not inferred from the abstract cycle alone.

## Exact scaling bottleneck and compressed representation

Allowing the conservative eleven-internal-step core bound and otherwise keeping
the local kernel produces 154,794,412 possible first-return profiles, with maximum
length 25. This is an overapproximation of actual physical profiles. NONE of
those 154 million profiles has been materialized.

They are represented by a DAG plus a six-state bounded counter. A dynamic
program counts the paths, and a turn-word projection reduces them to just
58 words. The entire projection uses 40,432 shared nonterminal-word entries;
no one nonterminal has more than 22 word entries. The map still points back
to complete kernel transitions, so full-component guards can be restored.

The 58 words are only a discovery quotient. Different component profiles with
the same turn word can have incompatible ports or passive histories. Neither
word counts nor the bounded-core graph certify any physical cycle.

This bottleneck motivates a symbolic full-field consistency check per word,
using initial board bits, exact read parity, and bounded black-edge reachability
for the active cap. That route must preserve full component guards and avoid
replacing passive output by erased or freely reusable resources. No such symbolic
solver result or cap-seven exit theorem is asserted in this note.

## Files

cap7_structure_probe.json is immutable first-probe output.
component_kernel_M7_compact.json contains the local transitions.
cap7_core_certificate.py/json check the unique core, condensation, exact rank,
bounded-core path count and weighted excursion bound.
cap7_turn_word_quotient.py/json compute the compact 58-word projection.
All cap-seven statements remain author certificates until separately audited.
