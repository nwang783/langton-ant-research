# Two-relation first-reuse search: exact scope and outcome

The protocol is in `two_relation_first_reuse_protocol.md`. Its conditional normal relation and exceptional-target relation were analytically reviewed, but the new C++ engine has not received an independent implementation audit.

On the six N-return regression, the search removes the unsupported sixth marked site, converges to the five previously audited phase-7 markers, and reproduces the exact 6,562 ordinary and goal forbidden pairs. An extra explicitly false seam mark at local type 1, site (0,-1), is removed in the first round. It is physically reused in global-type pair (0,3): source phase 8 reads R at (2,-2), and the next macro reads L there at its phase 3. The final regression again reproduces 6,562 pairs.

On all 88 raw macro types with their unconditional literal-compatible 494 pair and 2,240 triple grammar, the 510 empirical raw first-L candidates produce a conditional normal relation of 1,108,698 pairs. The goal relation collapses to empty after six deletion rounds, and all 510 marks are deleted. Thus this run proves NO full-language freshness theorem. An empty proof-method relation is not a physical counterexample.

The compatibility lists deliberately bypass all freshness conditions, including goal-target freshness. They are conservative supersets. Short-gap tables separately impose the exact normal or goal-prefix freshness conditions. Both relations are recomputed from scratch for the same surviving family after every outer deletion.

Artifacts: `two_relation_spatial_kernel.cpp`, `build_two_relation_engine.py`, `two_relation_full.log`, `two_relation_full.status.json`, `two_relation_n_test.log`, `two_relation_n_false_seam.log`, and their certificates.
