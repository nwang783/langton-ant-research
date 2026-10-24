# The closed-loop output does not directly supply the retained corner inputs

Author result, 2026-10-23 10:08 UTC. Independent review requested.
Scope: the171 retained single-literal-turn orthogonal104 interfaces in
single_turn_corner_selected.json, four physical rotations, arbitrary placement,
and the COMPLETE output of the signed43-cell square-loop family for every r>=3.
This is not a classification of all corners, connectors, or repair routines.

The exact Presburger black-subset test finds23 nonempty placement families
among684 phase/rotation choices. Its full relations are frozen in
four_corner_all_phases_black.json. Seven phase cases occur:16,17,67,68,69,70,71.
All other retained choices lack a required prepared-black cell.

For each of the23 surviving families, check the ORIGINAL complete-input
contract: an incoming mature standard104 half-ray, the single literal turn,
and its outgoing standard104 half-ray. The first read at a physical witness
is computed from every possible translated incoming/outgoing period, not by
omitting the incoming pass and checking colors at the cap incorrectly.

In every family there is one explicit nearby cell that this complete interface
requires initially WHITE, but the signed loop output has it BLACK for every
placement in the family. The complete parameter relations and first-read times
are in four_corner_known_interface_guards.json. Witness first reads lie in the
last incoming period or at the cap itself. Thus a sufficiently mature approach
cannot avoid the obstruction by changing a distant entry seed.

This leaves a concrete correction obligation, not a repair impossibility.
In finite whole-field probes the nearest alternatives from cases16/17 need44
(or48 at the distinguished final corner) white erasures, independent of r;
other placements need growing corrections. Those numerical repair-count
patterns are DISCOVERY CONTROLS ONLY, not an all-r theorem. No route executing
such a correction has been supplied, and no new initial fuel is silently added.

Files:
- check_four_corner_all_phases_black.py / four_corner_all_phases_black.json
- check_four_corner_known_interface_guards.py / four_corner_known_interface_guards.json
- probe_loop_corner_repair_counts.py / loop_corner_repair_counts.json

A separate direct-cap prefix probe is deliberately narrower: it starts the ant
at the proposed cap WITHOUT executing its incoming front. Do not use that probe
to exclude the complete incoming-corner interface. The first-read white-witness
checker above is the correct complete-input argument.
