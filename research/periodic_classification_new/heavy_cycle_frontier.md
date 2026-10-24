# Finite cell-flow cycle parity monitor

23 October 2026, 08:22 UTC. New implementation, analytic semantics reviewed;
no completed graph using it is claimed.

For cap4, signed KT forbids finite physical count-three directed cycles.
Track the count-three CELL graph while exposing rows, separate from the
full event-permutation graph. Each cell has at most one high-flow incoming
and one outgoing port. A cycle closed by a new edge is simple in the actual
full-drift cylinder embedding. A simple embedded cylinder circle has
winding0 or±1, so even seam parity is exactly the contractible case. Reject
such a closure; retain odd essential cycles. Never use a primitive quotient.

heavy_cycle_frontier.py retains a weighted union-find partition of the
current-row high-flow cells, with seam potentials modulo2. Add every new
physical high-flow edge, including edges wholly inside the new row. A
same-component edge of even cycle voltage is rejected. Project the
partition onto the new row after each step, forgetting components without
frontier contact. This is finite for each supplied circumference.

An already closed odd component has no unprocessed incident high-flow
port because both directed degrees are exhausted. Its arbitrary spanning
tree potential can be retained for this projection without creating an
extra possible extension. Complete histories determine every future port.

Author controls check_heavy_cycle_frontier_controls.py/json reject a
contractible high-flow unit face and retain a full(+4,0) essential zigzag.
The exploratory full(4,4)cap4 run was stopped UNKNOWN as dominated by the
completed simpler three-row first-return certificate, which needs no cell
monitor. No result depends on this new implementation.
