# Full-five ancestry height: evidence and unresolved renewal

The audited height-eight theorem currently covers only C/V/B intervals. A possible extension to all five macros is a conjecture, not a result.

## Discovery controls

`five_macro_depth_samples.json` independently replays all 192 distinct feasible macro words extracted from the other analysis's saved discovery logs. All have cut ancestry depth at most eight. Some exceed 120 macros. `five_macro_edge_samples.json` records their positive-node parent types. The only nontrivial phase-type SCC observed is C6 <-> C11; none of the terminal stars V14,U24,Q60,B70 has an internal parent in these samples.

`search_five_ancestry_depth.cpp` is a targeted randomized depth-first probe. It tracks exact last-letter consistency and active token-owner depth using unsigned-safe integer coordinate keys. Ten seeds, each capped at two million feasible prefix nodes and 300 macros, found no depth-nine prefix. Seed 6 reaches depth eight at CCCVU; the others reach seven. These are finite discovery controls, not an exhaustive bound or proof of terminal freshness. Random DFS also oversamples long shared prefixes, so the nominal node count is not a count of independent geometries.

## New proved local constraint

The full-five common-node6 producer restriction is in `five_macro_common_star.md`. It confines this renewal route to C11 and the four terminal stars, with no intervening non-C macro allowed on a C11 route. Other positive-node routes and terminal-star parentage are not controlled by that theorem.

## Unsuccessful small abstractions

`probe_terminal_parent_patch.py` uses a nine-cell square centered on the terminal input site and asks whether its previous R could belong to a terminal star. For each V,U,Q,B target, the unrestricted conservative abstraction has a target path. The same holds when the candidate producer is a common phase4/6/11 node. These are abstract paths only, not physically feasible counterexamples.

`probe_terminal_actual_ports.py` adds the recovered actual H-port language, minimized to 77 states, and retains oriented OUT excursions. With nine cells, even the terminal-star-only producer restriction still has abstract witnesses for all four targets. The grammar is an extra conditional dependency; its use does not turn those abstract paths into literal realizations.

Four 25-cell BDD tests (V14->V14, U24->V14, V14->U24, U24->U24) using unrestricted macro excursions all reached the 250,000-created-node cap without a conclusion. The old script does not garbage-collect BDD nodes, so those caps are not measurements of minimal proof complexity.

`probe_nonterminal_parents.py` tests observed-parent restrictions at the nonterminal Q/B inputs. Every initial nine-cell test produced an abstract witness. Thus the observed acyclic phase graph cannot simply be promoted to a theorem from those samples.

A joined patch combining the target's nine-cell neighborhood with the common phase-5 nine-cell neighborhood is being tested with the 77-state port grammar and garbage collection. Its live status is in `terminal_joined_patch.log`; a running or capped computation is not a proof.

## What a height theorem would imply

A uniform finite cut-forest height bound H for every five-macro prefix would exclude every finite-support infinite five-macro stream: the finite initial black field gives finitely many cut roots, each has outdegree at most four, and height H gives finitely many descendants. This would close the five-macro intermediate reduction, not the separate problem of infinitely many adjacent forbidden ten-windows in arbitrary trajectories.

Terminal-site freshness is sufficient but stronger: if every non-C terminal star is a cut root, each non-C macro spends one distinct entry black token. The ancestry route seeks a weaker acyclic or bounded-renewal classification even if some terminal star is not fresh.

## Joined-patch test and seam correction

The 77-state actual-port grammar plus the union of the exit 3x3 patch and the common-phase5 3x3 patch did not exclude terminal-star-to-terminal-star renewal: abstract witnesses occur for V, Q and B; U reaches the 250,000 live-BDD-node cap. These are abstraction failures, not physical counterexamples. See `terminal_joined_patch.log`.

The earlier common-star finite closure has an elementary stronger proof: each macro ends RRRR and the next begins LLLLRL, so the parent is exactly the immediately preceding terminal star. See `macro_seam_identity.md`; do not count this forced seam identity as a new global restriction.

## Further nonterminal-parent abstraction failures

The 77-state port grammar with a nine-cell patch does not exclude either (a) node4 or terminal-star sources for any Q/B first-L positive input at phases13,35,38,40,43,51, or (b) all higher nonterminal sources, allowing common6, node4, terminal stars, and Q/B52-to-phase35. All twelve targets in each family have abstract witnesses, not physical counterexamples; logs `weak_branch_parents.log` and `nonterminal_rank.log`. Enlarging Q phase13 to its entire prior read footprint plus the local 3x3 patch gives 17 tracked cells, but still an abstract witness (`prefix_rank_q14.log`). No new nonterminal rank exclusion follows from these runs.
