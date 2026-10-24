# Chronology checkpoint, 2026-10-23 05:29 UTC

Read `producer_chronology_checkpoint_2026-10-23_0511.md` first for signed scope.
Coverage is unchanged: **eleven of thirteen** canonical DCUV strict unfunded
record cases signed; only V1 and U1 remain open. The global ant conjecture and
DCUV tail theorem remain unresolved. The conditional cubic assembly is reviewed
but still has those two genuine premises.

## Latest useful methods and controls

1. Transverse-band far geometry is independently reconstructed on a sparse V1
   control. Full23-color V1 and22-color U1 default-band models cap2m nodes. Exact
   phase-height color reorder also caps. Do not call those models impossible.
2. Global residual-height Q is analytically approved, including conservative
   upward grid rounding. All initial residuals satisfy height<=F after global
   high-fuel whitening, F=floor((S-I-1)/2). Every packet requires its full input
   heights<=Q, then Q=max(Q,full output heights). Exact low-bin interval relations
   jointly account for before/after head height and Q. No freshness hypothesis.
3. Generators:
   - `refine_record_global_residual_height.py FIRST_FAR_BANDS.json PREFIX`.
     Adds5 low-order bits on V1 (Q=-10..11), shifting colors by5. Records full
     finite geometric Q relations and exact interval details.
   - `compress_record_global_height_relations.py EXACT_Q.json PREFIX`.
     Exact finite relation compression: guard cubes plus identity/fixed-output
     updates. All32 before codes independently enumerated for equality, including
     unused binary values. This cuts2.16m edges to650k on the first sparse control.
   - `coarsen_record_global_residual_height.py EXACT_Q.json PREFIX VALUES`.
     Grid[-10,-6,-2,2,6,11] adds3 bits; always rounds upward and never interprets
     Q as an attained maximum. Its pilot witnesses. The exact Q model is stronger.
   These implementations are analytically inspected but **not independently
   computationally signed yet**; auditor will reconstruct a useful final closure.
4. Forward reachability is substantially better than backward with Q. Sparse14
   exact-Q V1 reaches3,389,506 states atdepth21 with229k live BDD nodes, whereas
   backward caps2m. Its witness is NOT physical: three fresh illegal6 factors
   are recorded in `global_record_transverse/v1_14_selective_Q_exact_witness.json`.
5. `guarded_reset_bdd_forward_v3` adds mid-layer GC retaining seen/frontier/next,
   with the backward-v3 25%-growth threshold to avoid thrashing. All250 explicit
   random reset-graph controls pass, including221 forced tiny-threshold collections
   and independent checking of every no-hit invariant. CLI DAT CAP OUTPUT.bdd
   [GC_MIN] [GC_SLACK]. This is an engine control, not a new theorem.
6. Symbolic's cumulative selective DFA is now
   `chronology_dcuv/record_literal_cegar/k5_patterns06.json`,148 classes. It
   contains six separately literally impossible6-packet factors. Sparse14
   V1+patterns06+bands+exactQ still witnesses atdepth21/3,253,673 states.
   Full k6 is independently checked and has527 classes; I am trying it once on
   the small14-color V1 Q model rather than endlessly adding6-factors.

## Active processes and ownership at this checkpoint

  compression, live pruning and forward-v3 with2m cap. Check before rerunning.
  order changed from Q-low to Q-high: `v1_full_Qhigh.*`. Pure bijection wrapper
  `permute_guarded_reset_model_generic.py` also accepts models without pose fields.
- Own full23+old-selective+Q forward-v3 already genuinely capped2m near1.62m live
  nodes; first layer-GC version had only662k live at its transient cap.
- Symbolic results cover U1 and is combining exactQ with the independently approved latest
  output C-age clock for all three fixed U upper goal inputs. It also queries the
  existing counted relation for any useful V input age bound.
- Auditor has approved all analytical protocols but deliberately postpones huge
  witness-model reconstruction until a useful no-hit exists. Keep exact final
  wrapper dependencies immutable and explicit.

No  or communications.

