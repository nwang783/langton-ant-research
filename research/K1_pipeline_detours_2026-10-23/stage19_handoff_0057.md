# Stage 19: literal triple-use cycles and a second-exchange obstruction

24 October 2026, 00:57 UTC. Both new results have independently passed.
They are structural exclusions in a complete WHITE cap-four translating
front with actual full period P and nonzero drift d. No K1, zero-output,
leftmostness or initial-fuel hypothesis is added to either theorem.

## 1. A flow-three cycle must be essential

`triple_use_cycles_cannot_be_contractible.md`
SHA 5036e7c2a06f291cd6ccada4c73ff7079521cd8641a9bc6444f805e8cd0966e2.

For fixed c, retain only physical directed edges with flow three and
incident heights C=c, L=c-3. The signed local inventory gives degree at
most one in each direction. Every cycle vertex has four WHITE reads.
There are four types up to rotation, retaining all complete port ranks.

A finite physical cycle has a first and last ACTUAL edge traversal.
The first can only depart at positive-flat LEFT R0, entering the curve
from RIGHT. No earlier boundary read is possible, because every boundary
R0 uses a cycle edge. The last can only arrive at strict same-R RIGHT
L3, leaving the curve to LEFT. No later boundary read is possible,
because every boundary L3 uses a cycle edge. These statements also rule
out unused chords between boundary vertices.

The flow-three circuit is a simple embedded Jordan curve. A clockwise
orientation traps the entire past on bounded RIGHT; a counterclockwise
orientation traps the entire future on bounded LEFT. Bi-infinite nonzero
translated periodicity puts the cursor outside every fixed bounded set
in both directions, a contradiction. Thus cyclic components in the full
quotient are essential. Infinite essential lifts have no first/last use
and are explicitly retained.

This is not the claim that a static flow-three path is a consecutive
actual ant factor. No new period or root charge is inferred.

## 2. The restricted max-RIGHT penultimate graph-leaf family is empty

`max_RIGHT_penultimate_graph_leaves_are_impossible.md`
SHA b1ae9995011bf8b048714664c60c040c194909ec5a35db3ae30caa0a258702f2.

The family is exactly the old contractible repaired sheet M-1 GRAPH
leaves whose sole exchange is a RIGHT turn around a global maximum C
face. GRAPH degree counts parallel exchanges with multiplicity. This is
not a canonical maximum-face p-leaf.

The signed contractible-leaf clock sign puts outgoing L1 on that node.
At its same-R root, this L1 is the second occurrence of a physical port
used at least three times. Physical chronological ordinal matching sends
it to the second occurrence of the neighboring incoming port. At most
four complete reads force that arrival to be L1 or R2, never R0 or L3.
Thus the repaired node meets another exchange at the target cell.
Neighboring cells have opposite checker parity, while full drift
preserves checker parity, so the target exchange is a distinct full
quotient class. This contradicts graph degree one.

The old restricted leaf count h is therefore zero. Previously frozen
length and clock lower bounds remain true but become vacuous for this
family; no sources are edited. Nonleaf stock holes, arbitrary other
contractible cycles, other leaf root types, prepared controls, and general
K1 fronts remain open. This argument does not use Section 1.

## 3. Independent certificates

Auditor: continue_ant_independent_audit.

`audits/check_G3_contractibility_and_max_leaf_independent.py`
SHA 2624d1116bc5e9ef7b3f779df656e0afbfeaddc48ddf8af2c28e549e81ba0707.

`audits/check_G3_contractibility_and_max_leaf_independent.json`
SHA 5f41b889a8d9dd2686ed419f3838a5bba132b3f3fbbbdc26847f3958416976f1.

The independent reconstruction starts from all 30 physical complete
WHITE histories, checking all eight internal flow-three rows and all six
root/target ordinal rows. It independently reviews the physical lifts,
first/last boundary inventory and checker-parity alias obstruction.

## 4. Continuing scope

Stage 18's endpoint pairing and Nodd >= Ntop >= 3 nA remain available.
These new exclusions remove two previously permitted topologies, not all
old-stock mechanisms. Essential flow-three cycles and repaired nonleaf
cycles are genuine open alternatives. There is still no original-fuel
upper bound, paid renewal count, complete WHITE positive example, or
cap-four all-drift exclusion.
