# Producer chronology checkpoint, 2026-10-23 00:43 UTC

## Validated current status

The universal finite-seed standard-104 conjecture remains unsolved. The signed conditional D/C/V transfer count is now 39 of the original 69 (symbolic analysis and independent auditor); the remaining list is `../word_stabilization/dcv_conditional_confinement_anchored30.json`. Cumulative signed relation: `dcv_anchored_signed40.tsv`, including the original off-list DC→D result. Existing signed36 and signed38 files remain frozen.

No new producer-label or reverse-flag numerical exclusion below is unconditional. Their required hypothesis families have NOT been discharged. All current conditional results must be kept separate from signed39.

## Exact producer labels

`add_protected_producer_labels.py` enriches a frozen forward color-patch model at selected fixed patch cells. A label is unknown or an exact producer type/output slot/heading (hence exact physical producer pose). A separate outer-origin code prevents an internal producer with identical geometry being mistaken for the source. Every complete RAW+M11 context touch clears a label; packet outputs then install new internal labels. OUT preserves labels because watched cells are retained in the patch.

At a residual input consumption, signed forbidden relations always apply. An unproved candidate family H applies only when the producer/consumer gap is strictly smaller than the outer gap: any known label at a strict intermediate consumer; only INTERNAL-origin labels at the outer goal. All outer-origin labels are exempt at the goal. The independent auditor has approved this analytic least-gap protocol, not yet audited its numerical generator.

Engine `protected_patch_bdd_labels.cpp` implements guarded XOR plus constant reset, with nine-field transitions. `verify_protected_patch_bdd_labels.py` verifies inductive closure independently of reachability. `protected_patch_bdd_labels_witness.cpp` reconstructs abstract witnesses, inverting resets by exact predecessor cubes. 250 small random graphs agree with explicit reachability, and every random no-hit invariant verifies. These are development controls, not an independent implementation audit.

Physical controls: `replay_producer_label_controls.py` replays all19 provided literal transfer controls through H202 models, updating labels independently. All19 survive. The two adjacent controls also survive with all221 hypotheses, explicitly testing the outer-origin goal exemption. Reports `producer_label_observed19_controls.json` and `producer_label_adjacent_outer_exemption_controls.json`.

## Conditional numerical closures

H202 is the full221 residual transfer candidate universe minus19 observed controls. H202 is UNPROVED.

- D→D at (3,0,W), q=(2,0), original index1: source∪target19 color cells plus labels at (3,1),(2,2),(1,3); 40 variables; no-hit with H202, 256,508,000 assignments, depth57. The frozen invariant remains valid using only23 hypotheses in `producer_labels_hypothesis_case01_reduced.tsv`. Models/certificate `protected_labels_case01_202` and `protected_labels_case01_reduced`.
- D→DC at (3,0,W), q=(2,0), original index2: 21 colors plus the same three labels, 42 variables; no-hit with H202, 580,989,656 assignments, depth87. Reduced24 dependencies in `producer_labels_hypothesis_D_DC_reduced.tsv`; same invariant verified after regeneration.
- The corresponding three-label D→V/VC(5,0,W) models reached the explicit two-million-node cap. They are inconclusive, not no-hit.

`reduce_producer_label_hypotheses.py` identifies rows needed by a fixed invariant by examining signed-only transitions. Its result is never trusted alone: regenerate the reduced-H graph and verify the full invariant against it, as done above.

The symbolic analysis's source-companion fixed-family exploration already leaves14 of the23 case1 dependencies unsupported. Therefore the conditional D→D certificate is not yet a mutual induction proof.

## Reverse target-input flags

`add_protected_target_flags_reverse.py` first reverses the color graph exactly, including XOR-transformed guards and OUT identities, then adds suffix-untouched flags for target inputs other than designated q. Every flagged cell is asserted in the color patch. Starts from target-entry guard cube with live flags; the goal is the original post-source cube and is never candidate-filtered. A strict reversed intermediate producer may be filtered by a protected producer→target candidate while the suffix flag is live; full-context touch clears it. The auditor has approved the analytic protocol, not yet replayed these generated models.

Conditional H202 no-hit:
- D→V(5,0,W), q=(2,0): one target flag at (3,1), 26 variables,18,529,358 assignments,depth90. Reduced8 dependencies in `producer_reverse_hypotheses_D_V_reduced.tsv`.
- D→VC(5,0,W): same flag,28 variables,5,799,468 assignments,depth105. Reduced5 dependencies in `producer_reverse_hypotheses_D_VC_reduced.tsv`.

Both reductions were regenerated and the original invariant verified. They require opposite-input-slot D→V/VC(4,-1,W) rows, which still have abstract witnesses with reverse flags alone, even under H202. `reduce_reverse_flag_hypotheses.py` performs the fixed-invariant reduction.

## Work running / next

Dynamic producer labels at watched (3,1) are being tested on those slot1 D→V and D→VC cases, based on explicit witnesses containing an internal DC→V(5,0,W) transfer. Files `protected_labels_D_V_slot1_202` and `protected_labels_D_VC_slot1_202`. Session status must be checked before rerunning.

The symbolic analysis is independently pruning the source-companion family, pursuing a new max-plus potential, and searching for literal counterexamples to14 unsupported auxiliary dependencies. The depth14 helper search exhausted3,845,686 nodes without a witness; this is bounded negative evidence only.

`analyze_patch_witness_labels.py` now clears on every full-context touch; its previous residual-only diagnostic is preserved as `_v1.py`. It is a witness diagnostic, not a proof.
