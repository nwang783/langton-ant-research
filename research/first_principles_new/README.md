# Independent first-principles continuation,22 October2026

The full finite-support standard-highway conjecture remains unresolved. This directory contains an independently reviewed symbolic non-recurrence theorem and a precise obstruction to a tempting finite-seed shortcut.

## Reviewed structural theorem

For every square-ant turn stream, including arbitrary initial square colorings:

- each reduced prefix state in G=<R,L|R^4=L^4=1> is visited at most five times;
- each right coset of H=<RL^3> is visited at most six times;
- visits to a coset form one contiguous block in the visit chronology of its projected square cell;
- the reduced walk converges to one infinite boundary ray, whose eventual internal runs have lengths one or two.

The bounds are sharp, attained by the independently recorded37-letter witness. These statements do not bound physical-cell visits, prove physical transience, select a periodic boundary ray, or bound side-excursion lengths.

Proofs and exact finite certificates:

1. `coset_canonicalization.md`: exact quotient lookup and cell aliases.
2. `face_module_return_lemma.md`: module trapping, completed-return language {empty,G,B,GB}, sharp five-group/six-coset bounds. Checkers: `check_module_ledger.py`, `check_six_cell_bound.py`, `check_root_cell_bound.py`, `check_five_group_bound.py`, `check_root_group_bound.py`.
3. `completed_fingers_and_no_interleaving.md`: exact return-word grammar; G axial ladders and B two-finger geometry; finite-interface no-A-B-A proof; noncircular transfer from square traces.
4. `symbolic_boundary_corollary.md`: properness, boundary convergence, and realization of every run-1/2 ray with unrestricted lift lamps.

Independent audit snapshots and replays are in `../audits/face_module_snapshot/`, `face_module_replay.log`, `face_group_replay.log`, `module_inclusion_snapshot/`, and `module_inclusion_replay.log`. The independently written all-parameter incidence checker is `../audits/check_module_projection_neighborhood_global.py`.

Square-language inclusion is also an existing primary-source claim in Gajardo2003 Theorem3. This work independently reconstructs the inclusion route and supplies corrected sharp visit bounds; it does not claim priority. The historical four-visit assertion was independently contradicted by an exact six-visit hyperbolic witness in `../literature_work/`.

## Exact finite-seed obstruction

`standard_lift_infinite_seed_obstruction.md` and `certify_standard_lift_seed.py` prove that standard104 itself needs nineteen fresh initially black cosets per period in an autonomous lift. Distinct highway periods have disjoint lifted-cell sets. Therefore finite square support cannot be replaced by finite lift support, even in the desired standard regime.

The outstanding task is to control the structured infinite lift input induced by finite square support. No-A-B-A gives each physical cell a chronological sequence of nonrepeating coset blocks, each of length at most six. Successive first-read colors are coupled by the parity of the preceding block. The exact G ladders change only four rectangle corners. Whether this forces standard periodic selection remains open.

## Other exact reduction

`recurrent_boundary_current.md`: recurrent directed-edge support has degree at least three; a recurrent finite-height axial strip has entire recurrent boundary rows; a reflecting horizontal boundary passage is exactly a one-dimensional exclusion move after alternate-site complementation. This is not a convergence proof.

## Experiments and their scope

The various C++ probes and logs were discovery aids, not substitutes for the reviewed lemmas. The500x200k and1000x100k square probes found maximum five reduced-state visits. The10m square-step and1m autonomous-coset-step no-interleaving probes found no violations; the later proof is independent of those finite runs.

`search_sixth_return.cpp` exhaustively excludes a further group return after the sharp witness within20,28,36,44,52 steps; its120-step100m-node run is INCONCLUSIVE. `search_coset_interleaving.cpp` excludes an H return after a fixed12-step physical loop within20 or28 further steps; its deeper2m-node runs and the60-step autonomous counterpart are INCONCLUSIVE. No capped search is presented as an exclusion theorem.

## Structured finite-seed input after the bridge

`spine_corner_consistency.md` gives the independently reviewed unique nonreturning spine grammar (at most three straight fingers per boundary syllable), exact packet color requirements, and necessary/sufficient corner-parity consistency criterion for a finite square seed. This is still an infinite constraint system, not a finite-state attraction theorem.

`static_lift_gauge_obstruction.md` and `check_static_lift_gauge_obstruction.py` give an exact50-/10-letter witness ruling out a universal pointwise gauge from the projected seed bit and lifted coset alone.

## Finite-support boundary exclusions

`alternating_boundary_exclusion.md` is independently audited: exponent2 must occur infinitely often in the limiting ray. Its all-exponent1 staircase forces every optional B to the depth-zero one-finger form, each charged to a distinct initial black off-diagonal cell. `check_alternating_spine_local.py` replays the two exact finite packet tables.

`doubled_boundary_exclusion.md` independently proves the complementary exclusion of an all-exponent2 tail using disjoint north-finger input cells and one-way east endpoint flips. It has also passed independent analytic review. Thus both exponents1 and2 occur infinitely often in every finite-support limiting ray; no density bound or highway selection follows.

## Further audited quantitative and return-window consequences

- `quantitative_boundary_mixing.md`: homogeneous1/2 blocks have lengths at most2m+4 and2m+13 at entry mass m. A spine syllable changes mass by at most6. Among the first N syllables, exponent2 occurs Omega(sqrt N) times and exponent1 Omega(log N) times. These are not physical-time density bounds.
- `coset_return_cross_and_mask.md`: between two reads of the same lifted coset, the physical trace stays in the axial cross of width2 about its projected cell, and the black sets immediately before those reads differ at at most34 sites. Return time and arm lengths remain unbounded.
- The exact nineteen-black-first-cosets-per104 certificate has now independently passed audit as well; independent output is `../audits/standard_lift_seed_independent.json`.

None of these results closes the recycling of physical black fuel across differently directed spine runs, bounds the active corner frontier, or proves highway attraction.

## Run-transition and physical-spine continuation, 22 October 2026

- `b_packet_spine_constraint.md`: audited exact refinement. A preceding B with one/two G fingers forces the ensuing permanent exponent1/2; a two-finger B excludes the next optional child1 G.
- `run_transverse_mask_bounds.md`: audited net-mask bounds. Any horizontal2 block changes at most4 bits in each column; a1 block changes at most8 bits in each row/column. Direct additions on a later perpendicular two-line charge set are therefore at most8 and16 respectively. These are not indirect causal-influence bounds.
- `homogeneous_run_endpoint_barrier.md`: audited chronological ordering. Beyond a horizontal2 block's final core slab, at most one horizontal G far endpoint occurs; tail net mask is at most one vertical pair. Direct transfer to the immediately next parallel2 block's charge set is at most2. Longer recycling cycles remain unresolved.
- `physical_time_boundary_mixing.md`: audited aggregate duration bound T_N<=36N²+(12m+150)N. Hence completed permanent stages are Omega(sqrt t), exponent2 stages Omega(t^(1/4)), exponent1 stages Omega(log t). No positive density or attraction follows.
- `unbounded_physical_spine.md`: audited bounded-root packet lemma and unbounded physical permanent-spine corollary. A signed first moment at a column outside all roots bounds endpoint updates there; frozen compatible rail pairs then permit only finitely many crossing fingers.
- `sector_sensitive_rail_transfer.md`, `check_rail_sweep.py`, `rail_sweep.json`: exact A=RRLRRRRL sweep n->5n mass, with opposite-sector literal reversal D=RLLLLRLL. This is NOT a reusable counter interface. No sector0 translate of literal D fits the unmodified infinite output rail. Other rewrites are not excluded.
- `check_standard_packet_decomposition.py`, `standard_packet_decomposition.json`: source-bound literal parse of standard104 into22 core syllables and7 deleted G/B gaps. Core imbalance-4, packet imbalance+16, total+12. This is a canonical control, not an attraction proof.

## Periodic-core bridge, 22 October 2026

- `axial_core_periodicity_bridge.md`: independently audited. Fixed axial core width plus uniform total root multiplicity per transverse row imply full translating periodicity, with no decoration bound. Row supply bounds transverse G depths; one-sided endpoint epochs bound longitudinal crossings. A periodic axial core satisfies the hypotheses. This is compatible with the separate height9 exclusion and does not exclude arbitrary-width axial fronts.
- `periodic_core_decoration_stabilization.md`: independently audited. For a periodic diagonal core, past-root slabs first bound forward E/N fingers, then oblique supplier geometry bounds backward W/S fingers. Full oblique confinement follows. Combined with the axial bridge, EVENTUAL PERIODICITY OF THE LIMITING CORE SUFFICES FOR EVENTUAL FULL TRANSLATING PERIODICITY. Core periodicity and standard104 classification remain open.
- `w20_rail_profile.md`, `check_w20_rail_profile.py/.json`: exact same-sector bulk rewrite, moving a solid black row three cells transversely while preserving mass. No clean cap or finite-seed renewal is claimed.
- `bounded_core_dwelling.md`: independently audited. A finite core interval confined to a fixed-size rectangle has uniformly bounded stage count, independent of mass and finger depths. Thus a core in any fixed-width strip with bounded longitudinal retreat forces full translating periodicity; separate line multiplicity and decoration bounds are unnecessary.

The periodic-core bridge is an equivalence: a full translating period is an infinite-order free-product element, whose cyclically reduced powers converge to an eventually periodic boundary ray. See Section8 of `periodic_core_decoration_stabilization.md`.

- `fixed_period_core_uniform_bounds.md`: independently audited. For a fixed P-stage core period, late rail lines miss the finite initial support and finitely many early exceptional fingers. The eventual diagonal G-depth bound30P²+44P+8 and axial full-strip width57P+29 are seed-independent. This yields a theoretical finite full-period bound for each fixed P, not a global bound on P or a standard104 classification.

- `one_sided_cap_forward_depth.md`: independently audited finite-cap endpoint flux. With bounded northeast core retreat Bx,By, all E/N depths are bounded by m+Bx+6By+62 and m+By+6Bx+62, without strip or multiplicity assumptions. An oblique core strip then bounds W/S by a whole-region backward cap, yielding direct quantitative decoration control. Unconditionally, a finite core history of spans Dx,Dy encloses the full read history in its bounding box widened by m+6Dy+67 horizontally and m+6Dx+67 vertically. This is historical extent, not transience or bounded retreat.

- `fixed_core_realizability_decidable.md`: independently audited effective result. For any supplied periodic reduced core q, existence of any finite seed realizing it is decidable. Explicit seed-independent row/crossing bounds give a bounded translating displacement; the identity T<=kL bounds the temporal period even with backward excursions. A finite word search then uses exact displacement-class white-front chronology and primitive cyclic core matching. This does not decide capture for an arbitrary supplied seed or range over all core periods.
