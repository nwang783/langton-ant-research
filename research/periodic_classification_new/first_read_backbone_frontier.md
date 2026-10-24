# A finite first-read CELL-graph and period-debt monitor

23 October 2026, 10:21 UTC. Implementation candidate; code review pending.
No new exclusion follows until a complete graph and independent replay pass.
The generic backbone theorem is separately signed in
white_front_first_read_speed_bound.md.

For every active complete cell history, the predecessor of its FIRST read
is the neighboring physical cell opposite its first incoming heading.
Use the REVERSED dependency orientation here: actual predecessor source u
points to first-read target v. Thus indegree is exactly one in the complete
graph, while outdegree is unrestricted (at most the two outgoing ports).
This is NOT the event-permutation graph and may have multiple disjoint
components. Each component may have an essential cycle with trees attached.

Any completed cycle is simple in the full cylinder. The signed physical
first-time argument forces its winding+1 in this reversed orientation.
Tracking seam modulo THREE distinguishes it exactly from winding0 and-1;
there are no larger windings for a simple embedded circle. Multiple
essential components are retained. A tree may attach after a component's
cycle has already closed; the component is NOT discarded at cycle closure.

The finite state stores each frontier component, its seam-tree potentials
mod3, and either its unique root or an already-cyclic flag. In an acyclic
partial component, the unique root has its incoming first-read edge still
unexposed. It lies on the frontier; all earlier-row incoming edges have
already been exposed. When adding u->v, v must be that component's root.
Different components merge, retaining the source component's root or cycle.
An edge closing an acyclic component creates its sole cycle. A second cycle
in one component would violate indegree<=1 and is rejected. A closed fully
forgotten acyclic component is likewise impossible. These local graph
properties should be independently checked, not inferred from controls.

## Saturated lower period debt

At the first arrival v along that physical directed edge, the source read
is the FIRST occurrence of that outgoing source port. Let its complete
local rank be j. Then

    T_first(v)>=T_first(u)+1+4j.

Tree depths add these NONNEGATIVE weights from the component root and are
saturated at a fixed S. Saturation is exact for the capped sum because all
addends are nonnegative. When a tree root merges below a source node, all
its depths gain the source depth and the joining edge weight. When a cycle
closes, its capped depth-plus-edge sum is a safe lower bound on P. Store
the maximum such lower bound seen so far, also cappedS. Tree branches which
attach to an already-cyclic component need no depth, since they cannot
create a second cycle.

Combine this with the already signed exposed-event lower counter T and
fixed minimum period N. With one unchanged real-clock scale S, use
L=max(N,T_capped,cycle_debt_capped) and U=ceil(S/L) for new clock bounds.
All older weaker constraints stay valid. No period cap or rescaling is
introduced. This raw rank debt does NOT include the stronger left-run-start
correction; the global signed speed bound supplies any desired baseline N.

Producer module first_read_backbone_frontier.py has author positives on
standard104/208/312 of BOTH diagonal signs, with correct pose sectors and
four saturation scales16/64/120/512. Synthetic graph-only controls reject
contractible and negative-winding cycles, retain a positive-winding cycle,
and allow a tree branch to attach after cycle closure. Those synthetic
histories are NOT port-balanced ant fronts and are explicitly not used as
positive front evidence. The corrected nonvacuous window positives remain
separate and independently signed. No code theorem is inferred from a
finite control set.
