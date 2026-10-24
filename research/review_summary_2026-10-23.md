# Langton ant investigation: proof-status index

Working checkpoint: 23 October 2026, 16:15 UTC. This is a historical mathematical review checkpoint.

## Bottom line

**The universal finite-seed standard-highway conjecture is still unsolved.** We have neither a proof that every finite initial pattern reaches the standard104 highway nor a finite initial pattern proved to avoid it forever.

The strongest progress is a set of completed, carefully delimited theorems: one troublesome family of continuing behavior is impossible; several kinds of alternative repeating highway are impossible; broad proposed self-replicating constructions are impossible; and several unbounded families of prepared seeds are proved to reach the standard highway. A separate exact procedure now tests whether a specified class of recursive construction can run from any finite seed.

A newly verified nonstandard travelling wave repeats1564 turns while advancing(14,14), with infinitely many actual defects. It requires a specifically prepared INFINITE trail. Its full field and infinite future are certified. Exact counting shows that N periods require197N+1 pre-existing black cells, so this particular wave cannot persist forever on any finite board. The remaining construction question concerns arbitrarily long finite episodes from a fixed original black count, not a finite-seed infinite counterexample. A simpler exact input consists of five ordinary bi-infinite standard bands and two local color toggles; this still does not construct a finite-seed itinerary. See [independent full-field certificate](audits/check_prepared_wave_independent.json), audit LT.

A second verified infinite prepared wave has period 4352 and drift (26,26). Three ordinary infinite standard bands plus 68 specified color edits suffice, but the bands alone fail immediately. Its exact finite supply is 406N+57, so it too cannot repeat forever on a finite board. One explicit 56-cell attempt to connect the required routing stations instead reaches standard capture. The construction problem remains open. The1564 bulk writer profiles are now completely classified in the untouched-common-bulk setting. A changed-endpoint geometric routing order survives, but all four immediate final-writer joins need erasures or changes to already-read cells; a physical scattering prelude is still missing.

These conclusions have been independently reconstructed within this investigation. That is not external peer review, a proof-assistant formalization, or a claim of priority over the literature. “Expanded” below means expanded relative to the recovered starting material and earlier verified checkpoints.

## 1. A stronger exact reduction of the global capture question

A six-label union theorem permits arbitrary mixtures of six specified local defect labels. If only finitely many defects lie outside that union, standard104 capture follows. Conversely, capture has that finiteness property.

This is a genuine global equivalence, not merely a finite experiment or a theorem for one repeated label. It enlarges the previously handled local language. **The missing step is proving that defects outside this union occur only finitely often on every finite-seed trajectory.** Dense mixed defect patterns are not classified.

- Statement and complete bridge: [six-label union capture](word_stabilization/six_label_union_capture.md).
- Independent reconstruction: [global bridge checker](audits/check_six_label_bridge_independent.py) and [context checker](audits/check_six_label_context_independent.py).
- Audit reference: DQ in [audit.md](audit.md).

### Finite observations also admit a two-sided standard completion

Twelve added black cells, placed sufficiently far away, can preserve any chosen finite history both before and after the starting time while making the modified ant standard in both time directions. The two remote ports have disjoint full future read regions, so neither spoils the other. This extends the retained one-sided completion theorem, not a proof that the unchanged seed captures.

It identifies a precise possible route to a global proof: a uniform bound, depending only on initial black count, on the number of actual defects even among already two-sided-standard scattering trajectories would be enough. Such a bound remains entirely unproved. In fact the completed proof gives b(m) <= B_all(m) <= b(m+12), so this is equivalent, up to twelve cells, to uniform fixed-mass defect budgets over all finite inputs. It is not a weaker global premise just because the tested inputs are already capturing. See [two-sided completion and remaining budget](global_architecture_2026-10-23/two_sided_quadrant_completion.md), [independent checker](audits/check_two_sided_completion_independent.py), audit LO.

### A structural restriction on arbitrary trajectories

On any actual one-sided trajectory, follow the first departure from each visited cell that was initially white, stopping at initially black cells. Every such path ends at an initially black cell or the single unit-square cycle made by an initial RRRR. Thus an m-black-cell seed has at most m+1 rooted components. This needs no eventual periodicity, width or visit cap.

The restriction is genuinely global and nonperiodic, but it does not bound the size, branching or later revisits of those components. An infinite incoming tree can feed one root, and recurring branching already occurs on the standard highway itself. That uncontrolled nonstandard complexity, not an unbounded number of finite first-departure cycles, is the remaining gap. See [finite-root first-departure forest](periodic_classification_new/one_sided_first_departure_forest.md), [independent controls](audits/check_one_sided_departure_forest_independent.py), audit LR.

### A new spatial reduction for a possible mass-only defect budget

If a uniform defect-count budget first fails at some initial black mass, then either a finite noncapturing seed already appears as a compact limit, or the first remote seed contact exposes one of three problems: a fresh finite perturbation of the exact one-sided standard front that does not return to standard motion; a standard response aimed exactly back toward its old archive; or another original seed cluster still escaping farther away. Every other standard response, once all extra cells are in the contact cluster, automatically misses the old archive and cannot cause divergent defect counts. This keeps the complete old field and true past, rather than treating the front as a reset.

A further exact corollary shows that any fixed, already certified capturing finite seed tolerates all sufficiently far single-black additions on21 of the22 fresh standard channels. The remaining channel sends the ant exactly back toward its old archive. The distance cutoff depends on the complete base seed, so this is not an induction proving all seeds capture.

The reversing singleton channel now has an exact full-field return map for any such base. It leaves twenty-four growing strings, so it does not restore a bounded board. Its remaining difficulty is reduced to a universal two-rail prepared background with a finite inherited cap and a possible return toward the remote endpoint. This reduction is conditional, not a classification of that scattering. The universal remote endcap reached by a standard outward response has now been completely classified: all106 possible contacts return to standard motion, but three point back toward the changed old cap. That leaves the initial two-rail scattering and those changed-cap returns, rather than an uncontrolled endpoint inventory.

This is a necessary global reduction, not control of those three alternatives. As a small exact base case, the retained all-position one-black theorem now yields a distance-independent bound of106268 actual defects. It does not bound capture time, and it does not justify induction through arbitrary old archives. See [critical scattering reduction](nonlinear_global_budget_2026-10-23/critical_scattering_compactification.md), [one-black count consequence](nonlinear_global_budget_2026-10-23/one_black_uniform_defect_budget.md), and audit LT.

## 2. An entire three-word behavior is excluded, with quantitative bounds

No finite-support ant can have an infinite tail made solely from the exact turn words D, C and V defined in the theorem. The proof tracks which black cells are consumed and produced, establishes the required protected-transfer exclusions, and bounds four directional potentials. It is not an extrapolation from searching long prefixes.

There is also a cubic upper bound, depending on starting black mass but **not on the distance between seed cells**, for arbitrary finite factors in that language. Further bounds allow specified foreign words or arbitrary exceptional fine steps. These quantify the cost of repeatedly leaving the language; they do not prove that the number of departures is finite.

- Complete theorem: [D/C/V finite-tail exclusion](word_stabilization/dcv_finite_tail_theorem.md).
- Quantitative extension: [arbitrary-factor cubic bound](word_stabilization/dcv_arbitrary_factor_cubic_trim.md); [sparse perturbation bound](word_stabilization/dcv_sparse_perturbation_bound.md).
- Decisive independent checks: [closed producer-family checker](audits/check_closed_producer_family_independent.py), [literal boundary and residual ledger](audits/check_dcv_tail_boundary_ledger_independent.py).
- Audit references: GW, GX, HE, HZ.

### The nearby four-word extension is NOT finished

For D/C/U/V, the proposed final confinement argument needs thirteen funding-aware record cases. Eleven are independently proved; the V phase1 and U phase1 cases remain open. They are not interchangeable with the older69 transfer list, and the count is not a percentage estimate of how close the proof is.

An exact residual-age theorem now gives a spatial genealogy: produced black cells remain within controlled expanding boxes around original residual cells. A fixed-heading projection sharpens the duration bound to quadratic in the number of C words, independently of the distance between initial black cells. This forces C words to recur at least at square-root rate in any hypothetical infinite tail, but supplies no upper bound on their number. The counted refinement further requires five C words before produced cells can feed the two VCC inputs or upper U-family inputs; it removes one sharp genealogy escape and lowers the ancestry coordinate-speed bound to two thirds, but does not bound recurrence. A subsequent complete historical-color check also excludes the only repeating role pattern that attained that relaxed speed, without excluding all slower ancestry. Exact unbounded low-excursion summaries are also available. Some weaker resource models have explicit abstract paths, demonstrating that those relaxations alone cannot close the gap. Such paths are **not actual ants or counterexamples**.

- Conditional conclusion and missing premises: [record confinement assembly](core_periodicity_new/chronology_dcuv/record_conditional_quantitative_assembly.md).
- Established finite-C result: [spatial genealogy](word_stabilization/dcuv_c_age_spatial_cubic_bound.md), [quadratic projection bound](word_stabilization/dcuv_c_age_projection_quadratic_bound.md), and [two-thirds role-speed refinement](core_periodicity_new/genealogy_role_speed_frozen_20261023_0840/genealogy_role_two_thirds_speed.md).
- Exact low-excursion method: [compiler lemma](core_periodicity_new/exact_low_excursion_summary_lemma.md).
- Audit references: JD, JH, JO, JW, KA, KG, KL, KP, KV, KY, LA, LB, LH. No unconditional D/C/U/V theorem is asserted.

A different exact accounting keeps every consumed and produced residual identity, including reconvergences between siblings. If its historical cycle rank is bounded, the existing epoch-reset theorem gives a cubic duration bound in entry mass and that rank. The required rank bound is still missing. An actual nine-black-cell ant factor creates a reconvergence entirely inside one residual-root component, so a cycle cannot simply be charged to a newly imported root. Other physical helpers remain fully present.

- [Conditional rank theorem](cut_order_obstruction_2026-10-23/mass_sensitive/all_input/cubic_rank_corollary.md); [actual single-root reconvergence](core_periodicity_new/all_input_reconvergence_frozen_20261023_0945/00_all_input_single_root_reconvergence.md); [independent physical replay](audits/check_actual_reconvergence_independent.py). Audit LM.

A new all-age multi-cell obstruction uses the actual core, not only ancestry distances: a U-family packet cannot consume all four still-current outputs of one DC. Its forced fifth input begins in the source core, and every later attempt to create that input must first retire a protected sibling. The same argument gives universal correlations between the birth times of several U inputs, and excludes seven exact same-source cleanup arrangements at every age. It still allows earlier retirement and replacement and does not bound total U behavior. See [core-shadow theorem](core_periodicity_new/dc_core_shadow_frozen_20261023_1007/dc_protected_core_shadow_obstruction.md), [independent reconstruction](audits/check_dc_core_shadow_independent.py), audit LN.


A stronger chronological restriction now distinguishes the beginning of a factor from its interior. The youngest produced lower U inputs can only come from the factor's first packet. A separate three-C DC-to-V pose pattern likewise cannot occur after an earlier retained packet. Initial-cell funding then eliminates those specific unfunded record branches. The proof follows a mandatory predecessor-created cell that must disappear before the target, and excludes every possible retirement using the actual head path. Higher-age and other-origin branches remain open. See [young-input boundary checker](audits/check_U_young3_boundary_independent.py) and [DC-to-V boundary checker](audits/check_v1_DC_age3_boundary_independent.py), audit LN. An actual age-four interior example prevents extending the youngest-input result indiscriminately.



A stronger predecessor-cell law now covers a whole halfplane. Every retained packet leaves a specific fresh residual cell that cannot be consumed for two further C steps. After exactly three, it must still exist whenever the head is back anywhere in a specified halfplane. This is proved for arbitrarily long intervening words, using actual head motion and exact birth identities, not a simulated horizon. It rules out eight last-three-C approach positions for an unfunded U1 event and another whole conditional V1 return geometry. The barrier is not closed: the head can remain outside it or skip that clock with a two-C packet. See [halfplane reconstruction](audits/check_exit_bud_halfplane_independent.py) and [U1 port barrier](audits/check_U1_shadow_ports_independent.py), audit LN.

## 3. Alternative repeating highways are more restricted

For a complete translating front whose cells are initially white before the front reaches them:

- Some cell must be visited at least four times. A front with at most three visits per cell is impossible, with **no restriction on period, width or displacement**.
- A full-period displacement of two cells along an axis is impossible, with **no visit cap**. Together with the previously retained unit-diagonal exclusion, this gives a general minimum displacement restriction, but not uniqueness of the standard highway.
- If every cell is visited at most four times, the full displacement (a,b) must satisfy |a|+|b| at least8 and a²+b² at least40. The supplied smaller drift cases are excluded at every period and width. No front is asserted to exist at the first remaining displacement.
- Every such front also obeys the cap-free chronological speed restriction P at least8D, rounded to8D+2 when D is odd, where D is the largest absolute drift coordinate. This comes from coupling successive first-read dependencies, not a period scan.
- Every such front has period at least28. This follows from exact short-return and drift-packing constraints, not a bounded-period scan or a claim that104 is minimal.
- A full displacement of four cells along an axis requires some cell to be visited at least six times and its period to be at least40. This strengthens the previous cap-four exclusion to cap five, again at all periods and widths.

A further cap-four argument follows actual first reads through the global stream-height field. Every active height level has an essential chronological backbone; a bounded isolated active island is impossible. This couples geometry and chronology but still allows long strips. See [first-read backbones](periodic_classification_new/cap_four_first_read_stream_backbone.md), audit LL.

For a fixed oblique drift and fixed finite read-orbit cylinder with a prescribed input profile, a strict clock gives a computable bound on the period and all visit counts. Existence in that particular cylinder is therefore decidable without guessing a cap. Width and drift remain fixed; there is no corresponding axial or global conclusion. See [the cap-free cylinder bound](causal_reduction/unit_scale/oblique_cylinder_capfree_bound.md), audit LK.

Finite-seed periodic tails satisfy the required white-front condition sufficiently far from their finite prelude. These theorems constrain **hypothetical eventual periodicity**; they do not prove that every trajectory becomes periodic. “Full displacement” means the actual displacement over the supplied event period, not a primitive direction obtained by dividing coordinates.

- All-cap-three proof: [shifted stream-height theorem](periodic_classification_new/cap_three_shifted_stream_height.md).
- Unrestricted two-cell-axis proof: [negative-axis extreme exclusion](periodic_classification_new/axis_negative_drift_extreme_exclusion.md).
- Latest finite-certificate framework: [normalized real-clock frontiers](periodic_classification_new/normalized_real_frontier_abstraction.md).
- Independent checks: [cap-three geometry](audits/check_cap_three_stream_height_independent.py), [generic full-drift frontier checker](audits/check_general_normalized_real_independent.py), [combined small-drift inventory](audits/cap_four_small_drift_inventory_norm40.json); [axis-four cap-five reconstruction](audits/check_axis4_adaptive_frontier_independent.py).
- Audit references: GG, JC, JI, KH, KI, KR, KS, KW, LC, LD, LI.

A separate cap-free first-departure graph must also carry essential cycles opposing the net drift. Distinct such components impose an additive transport cost, rather than merely separate bounds to be maximized. The two opposite dependency-cycle families cannot share edges, permitting simultaneous flow subtraction with an exact remaining-displacement cost. This is a new structural restriction on complete white fronts, not a proof that arbitrary trajectories become periodic. See [first-departure counterflow](periodic_classification_new/white_first_departure_counterflow.md), [independent history controls](audits/check_first_departure_counterflow_independent.py), audit LQ.

A new second-visit argument retains the left-turn events that can supply a cell's second right turn. It gives an exact alternative: second visits either form another essential corridor or drain through synchronized first-visit gates. Same-face gates require at least sixteen steps, and neighboring gates have strictly nested timing spans. The gate-forest alternative is not excluded and no global count bound is proved. See [second-R gate/corridor theorem](rank_two_plateau_2026-10-23/second_R_gate_or_corridor.md) and [independent local reconstruction](audits/check_second_R_gate_independent.py), audit LS.


For hypothetical cap-four fronts, the maximum stream-height region now has a closed backbone made from actual first-left turns, even when the second-right graph drains into gates. Its ordered contact times divide the actual continuous ant path into backward excursions on one side and forward excursions on the other. This is stronger coupling of geometry with the real cursor, not a new exclusion: the side excursions may still take complicated detours. [First-left backbone](rank_two_plateau_2026-10-23/max_C_first_L_face_birth_backbone.md) and [actual side-current theorem](rank_two_plateau_2026-10-23/face_birth_curve_cursor_counterflow.md), audit LS.

## 4. Broad recursive construction routes are ruled out

Several results concern a **fixed substitution presentation**: each direction or physical heading/turn state is replaced by a specified finite word, with exact prescribed spatial scaling. They do not cover every possible algorithm an ant might implement.

All growing fixed substitutions on the four undecorated directions with a common finite-order spatial matrix are excluded, even with unequal image lengths and on arbitrary initial colorings. The analogous eight-undecorated-physical-state class is also excluded when exact boundary headings are preserved. Singular finite-power spatial matrices are excluded even with finite hidden decorations, under the stated exact geometric presentation assumptions. That last obstruction uses unit-movement bases; it is not silently extended to arbitrary finite macro bases.

For fixed half-turn-symmetric uniform four-direction refinements, the surviving matrix branch is therefore fully expanding, with spectral radius smaller than the substitution length and length no greater than the absolute determinant. This sharply narrows that architecture, not the whole counterexample search.

Decorated, nonsingular recursive transport remains a substantive escape route. There are proved all-depth local transport components, but they require growing prepared fuel. Their existence prevents treating the remaining construction problem as vacuous; no finite-seed growing wrapper has been built.

- [Unequal-length finite-order direction obstruction](causal_reduction/unit_scale/nonuniform_direction_finite_order_obstruction.md).
- [All physical unit-controller obstruction](computability/finite_power_exact_validator/all_physical_unit_controllers_obstruction.md).
- [Singular finite-power obstruction](computability/finite_power_exact_validator/singular_finite_power_obstruction.md).
- [Half-turn matrix dichotomy](causal_reduction/matrix_candidates/halfturn_matrix_dichotomy.md), read with its finite-order branch removed by the later obstruction.
- Audit references: IH, JJ, JM, JN, JP.

A different construction class is now excluded by complete chronology: follow the reversed standard104 coarse path, replacing each step by any legal exact-pose word of length1,5 or9. Even when the choices change at EVERY occurrence, five coarse periods cannot cross untouched standard-rail bulk. The proof grants arbitrary colors to every cell that any earlier allowed period might have touched, so it does not assume the front resets. A separate disjoint-new-cell argument shows that an unbounded such traversal cannot be prepared with bounded initial fuel, a bounded number of standard flights and a bounded amount of other work. Longer replacements, other coarse paths and arbitrary nonstandard preparation remain outside the claim.

- [Nonstationary slab obstruction](causal_reduction/unit_scale/nonstationary_short_slab_obstruction.md); [independent physical encoding and proof checker](audits/check_nonstationary_short_slab_independent.py); [actual-flight preparation bound](global_architecture_2026-10-23/nonstationary_slab_preparation_lift.md). Audit LO addenda.

## 5. Exact finite-seed testing is now executable for a defined construction class

For a fixed exact finite-power recursive presentation, the reviewed theory decides whether some finite seed realizes its chosen rooted path. This is a decision problem about a **supplied presentation**, not whether an arbitrary ant seed eventually reaches a highway.

The executed implementation now handles arbitrary-branching additive-I presentations with finite nonempty physical base words, including hidden decorations, unequal lengths and unknown seed mass and radius. It constructs genuine occurrence covers, derives all selected initial-color requirements, and checks complete all-depth frames for the resulting candidate seed. A verified powering adapter handles finite-order matrices with exact boundary-heading compatibility. All positive executed controls are nongrowing; no growing ant model has been accepted.

The macro-base extension and its finite-order adapter are separately checked; no unit-step subdivision is silently assumed. Singular finite-power matrices and changing boundary-heading maps remain outside this executed solver. Resource limits return UNKNOWN, not impossibility.

- Theory: [automatic forced seed](computability/finite_power_exact_validator/automatic_forced_seed.md) and [finite-power extension](computability/finite_power_exact_validator/automatic_forced_seed_finite_power.md).
- Executed general unit pipeline: [selector-free generated covers](computability/flat_exact_validator/general_selector_free.md); [finite-order adapter](computability/flat_exact_validator/finite_order_adapter.md).
- Independent checks: [general frames and arithmetic](audits/check_general_given_seed_independent.py), [generated-cover reconstruction](audits/check_generated_cover_independent.py).
- Executed macro extension: [general macro realization](computability/flat_exact_validator/general_macro_decider.md); [finite-order macro adapter](computability/flat_exact_validator/finite_order_macro_adapter.md).
- Audit references: JE, JF, KE, KJ, KK, KM.

This does not establish undecidability, independence from a formal axiom system, or decidability of the universal capture conjecture. A hard general parity-graph problem was identified, but no faithful reverse compiler from that problem to arbitrary finite-seed ants has been supplied.

## 6. Unbounded prepared-seed families provably capture

Let J_r consist exactly of the horizontal black row from(0,0) through(2r,0), plus(-1,1), with the ant at(0,0) facing east. For **every integer r at least20**, it enters the standard104 highway at time60r+777, at(2r+2,7) facing north, then repeats forever with displacement(-2,2) per period.

The proof checks all parameters and all future repetitions symbolically, not a finite simulation horizon. The threshold20 is sufficient, not claimed minimal. This resolves the actual continuation of a genuine local rod-growth operator, but only for this exact seed and phase family.

- Statement: [capped-rod capture](causal_reduction/unit_scale/domino_growth_capture.md).
- Independent all-parameter checker: [capture reconstruction](audits/check_domino_capture_independent.py).
- Audit reference: KC.

A genuinely two-dimensional family of chamfered frames is also settled for every pair of parameters r,k at least10. Its first closed excursion produces exactly the complete black pattern for a larger frame. Nevertheless, the required next head pose lies in the wrong conserved parity sector, so that apparent regeneration cannot be physically continued as proposed. Its actual trajectory instead enters standard104 at the certified total time36r+8k+291, with pose(2r+1,4) facing north.

- Exact frame identity and interface obstruction: [chamfered frame](causal_reduction/unit_scale/chamfered_frame_nearrenewal.md).
- Actual all-parameter continuation: [chamfered capture](causal_reduction/unit_scale/chamfered_capture.md); [independent checker](audits/check_chamfered_capture_independent.py).
- Audit reference: KN. This concerns those exact prepared boards, not modified corners or all finite seeds.

The inherited strict clock also orders complete parallel oblique wake profiles: no same-sector periodic return, at any finite width or period, can erase the entire standard104 wake back to white. This does not rule out returns that leave a different wake or unbounded debris. See [exact profile irreversibility](causal_reduction/unit_scale/oblique_wake_irreversibility.md), audit LK.

A separate exact interaction example shows that a finite prepared obstacle can reflect an incoming standard104 highway into another standard104 tail at every sufficiently large approach distance. The complete obstacle damage is tracked, and a required guard is erased, so this is a one-shot scatterer, not a reusable component or a counterexample.

- Statement: [finite highway-wake scatterer](causal_reduction/unit_scale/highway_wake_reflector.md); [independent all-future audit](audits/check_highway_wake_reflector_independent.py).
- Audit reference: KU.

A further family uses exactly43 initially black cells at increasing distances. It makes an arbitrarily long closed-pose four-corner excursion, but does not restore its input. For every pair of alternating arm lengths r,s at least50, the unmodified seed is proved to capture after a first temporary highway and a second collision with its own distant wake. The proof retains that second contact and the whole output field. A long periodic-looking segment is not treated as final capture.

- [Closed excursion](causal_reduction/unit_scale/four_corner_closed_loop.md); [two-contact capture](causal_reduction/unit_scale/four_corner_capture.md); [unequal-arm capture certificate](causal_reduction/unit_scale/unequal_four_corner_capture_certificate.json); [independent continuation](audits/check_four_corner_capture_independent.py). Audit LF.

These examples also show why an unrestricted capture-time bound cannot depend on initial black-cell count alone: even a fixed33-cell one-shot corner can be placed arbitrarily far away. This does not rule out bounds depending on seed diameter.

## What was already in the retained baseline

The retained source material already included the standard104 behavior and several finite-domain/strip and mass/charge constraints. In particular, eventual global black mass at least five and the **all-cap unit-diagonal front exclusion** were not newly proved classification improvements here. Later cap-limited unit-diagonal graph runs are useful independent method controls, not extensions of that existing boundary.

The index deliberately does not count every new certificate, repeated control, implementation optimization or finite failed search as a mathematical advance. A complete independent replay establishes the stated scope; finite searches alone do not establish unrestricted conclusions. No broad literature novelty claim has been checked.

## The remaining global gap

There is still no argument forcing every arbitrary finite seed into a proved capture region or forcing all residual defect events to stop. The unresolved possibilities include nonperiodic behavior outside the restricted macro languages, larger or more repeatedly visiting translating fronts, and more complicated decorated or expanding construction mechanisms.

A separate explicit construction shows why one tempting global simplification is insufficient: binary, monotonically growing face height can keep only twelve black cells while being built from individually legal square loops, if the live ant is allowed to teleport between those loops. A real ant cannot teleport. The missing continuous-cursor coupling cannot be replaced merely by positivity, low mass or local feasibility. This is a limitation of the relaxation, not an ant counterexample.

An additional literal staircase shows that even perfectly ordered, minimally costly transport need not be standard if infinitely many initial black cells are allowed. Finite zero-charge completions reproduce arbitrarily long prefixes, with growing initial fuel. Therefore a successful ordering bridge must retain a mass or causal-freshness term, not just cut crossings and transport slack. See [the exact limitation](cut_order_obstruction_2026-10-23/cut_order_minimal_transport_obstruction.md), audit KX.

A finite-root, collision-free resource model also shows that positive growth, minimum production age, expanding root boxes and monotone planar ancestry can coexist forever when literal packet masks and head chronology are omitted. The recent two-generation historical-color exclusion retains some of that missing information, but it has not yet been turned into a bound on all descendants. See [the exact resource limitation](cut_order_obstruction_2026-10-23/mass_sensitive/global_fifo_packing_obstruction.md) and [the coupled history theorem](core_periodicity_new/vcc_d_vc_joint_history_exclusion.md), audits LE and LH.

Closing the two D/C/U/V cases would finish an important restricted-language theorem, **not by itself the universal conjecture**. Finding a locally legal self-replicating component would likewise not be a counterexample until one common finite seed produces its entire infinite evolution. These distinctions remain the test for any claimed solution.

### Latest structural refinement: exact scope

An all-period chronological argument now excludes a straight, minimal-counterflow maximum-face path whose immediate neighbors on one side are all strictly lower, for complete white fronts with at most four reads per physical cell. Two forced helper arrivals and their missing earlier suppliers produce an impossible four-edge balance. This is stronger than checking a finite period range, but bent paths and equal-height branches remain. See [four-port obstruction](K1_pipeline_detours_2026-10-23/strict_straight_K1_four_port_obstruction.md) and [independent proof review](audits/strict_straight_K1_four_port_independent.md).

The straight-path exclusion now also covers equal-height branches: a straight branch forces the next face to bend. Every six-face window of a minimal-counterflow maximum-face curve must therefore contain a bend. This remains a cap-four/K=1 structural theorem, not a bound on the cost of bends or a general front exclusion. See [branch-to-bend proof](K1_pipeline_detours_2026-10-23/K1_branches_force_bends.md).


### Restricted-language center simplicity, with a sharp limitation

The complete exact first-contact analysis now proves that a valid recurrent-eight factor starting with U, UC or UCC has an injective corrected-center path. A finite footprint calculation bounds each physical cell to104 raw reads, so an infinite such factor leaves every fixed finite set. This does not establish an eventual straight highway or cover arbitrary ant behavior. An actual19-cell seed has a simple center path while its all-input incidence graph acquires a cycle, preventing a shortcut from this geometry to zero reconvergence. See the independently verified U-entry simplicity and simple-center reconvergence bundles in core_periodicity_new.


## A count-only defect budget is now disproved

There is an exactly verified family with184 initial black cells and arbitrarily many nonstandard defect events. For every positive integer N, moving those184 cells to the supplied affine positions produces N consecutive periods of the1564 nonstandard wave, with614N+92 defects in the complete prefix. The seed diameter grows; no cell is edited during execution. This is an all-parameter chronological certificate, not a finite scan.

This rules out bounding all future defects solely by the number of originally black cells. Combining the family with the already proved12-cell completion also supplies known bi-standard capturing examples with at most196 cells and unbounded defect counts. It does not give one finite seed that avoids capture forever. The universal conjecture remains open, and spatially sensitive or trajectory-sensitive bounds are not excluded. See [the exact independent proof](audits/constant184_wave_family_independent.md).

## 17:15 UTC: exact original184-cell bi-standard family
Every member of the constant184-cell affine construction now has independently certified forward AND backward standard tails. The exact complete future defect count for N>=4 is614N+25508; N1/2/3 are separately replayed. Hence the at-most184 bi-standard defect supremum is infinite, without completion overhead. A self-contained theorem/data/exact-verifier bundle is frozen in deliverables/constant_184_capturing_family.zip. This disproves uniform mass-only total-defect budgets, not universal finite-seed standard capture.
