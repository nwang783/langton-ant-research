# Oblique ownership at the unresolved critical k=8 scale

Status: exploratory exact finite inventory, not a global exclusion. 2026-10-22.

`probe_oblique_record_owners.py/json` reuses the causal analysis's complete internally legal position-only image inventory and owner calculation. It tests all primitive integer normals (u,v) with -8<=u<=8 and 1<=v<=8. A target first-L cell is protected for that normal if every possible coarse owner q obeys u*q_x+v*q_y>=0. Such a cell cannot have been prepared before a strict coarse record for that functional, apart from the finite initial support and finite uncontrolled prefix.

For k=8, a=2+2i, normalized coarse entry heading N, and vertical fine entry heading (theta=0), all17 R images are protected for normals (2,1), (3,1), (4,1), (5,1), (5,2), and others. At normal (1,1), just RRLLRLLR with fine heading N and LRLLRLLR with fine heading S remain unprotected.

For the opposite fine-entry axis, no tested normal protects every image. The best normals leave five images unprotected. At normals with negative horizontal component, all17 can remain unprotected. Conjugating a swaps the two fine-axis cases in this inventory.

This does NOT yet exclude the k8 critical scale. An oblique coarse record can be entered in two different coordinate directions, and after normalizing each entering heading the fine-axis phase and the normal both change. In particular, a record of 2x+y entered east has normalized normal -x+2y and the other phase; the successful north-entry calculation does not cover it. Nor does unboundedness of the functional force records of both entering directions.

Potential continuation: predecessor-context ownership, or a finite first-record language tracking the entering direction, could conceivably close the residual phase. An unsupported transfer of the axis-record or heading-preserving proof would not.
