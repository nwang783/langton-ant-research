# Runtime checkpoint, 23 October 2026, 04:27 UTC

No producer computation is currently running; all exploratory symbolic
sessions have completed and been polled. The general finite-seed conjecture
and all-axis-front exclusion remain open.

New signed analytic results, not solver premises:
- `axis_singleton_extreme_theorem.md`: the lowest active row at actual
  full drift (+2,0) is singleton in both classes, with no multiplicity cap.
- `axis_singleton_second_row_structure.md`: the next row's sole downward
  rank is 0 or2, with its incoming-N rank two later.
- `axis_second_row_r0_bound.md`: rank0 forces second-row length4 or5, with
  all higher-row multiplicities unbounded. A balanced-prefix cut reduces
  the suffix to the standard-bounce singleton obstruction.

Pending independent review: `axis_reverse_bounce_obstruction.md`, including
its separate parity-padding extension, and `axis_second_row_r2_bound.md`.
The proposed rank2 conclusion is second-row length exactly5. No pending
claim should be promoted before the auditor confirms it.

Exploratory symbolic scripts `probe_axis_extreme_*` and
`probe_axis_singleton_*` use unbounded rank variables, not period cutoffs.
Their SMT UNSAT outputs are not independently checked proof certificates.
SAT outputs are ordinal/local relaxations, not ant fronts. Some earlier
weaker relaxations remain SAT and are preserved, even where stronger
analytic arguments now rule out their physical interpretation.
