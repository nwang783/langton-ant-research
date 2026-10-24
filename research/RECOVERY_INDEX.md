# Langton's ant research recovery and audit index

Recovered 22 October 2026. This index records source provenance and proof status; it does not establish a new theorem. No original external document was changed.

## Exact current conjecture

For every finite initial black set B_0 on Z^2, every initial ant position, and every initial heading, the right-on-white / left-on-black / flip / move ant eventually has a turn stream equal to a cyclic phase of the standard 104-letter highway word. Translation and quarter-turn rotation are allowed.

 Its literal word is:
LRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLR

The target sufficient statement is: only finitely many length-ten windows lie outside the 84 cyclic length-ten factors of this word. The source factor-language theorem supplies the implication to eventual standardness. This implication itself is being independently audited.

## Provenance


   Provider modified time: 2026-10-21T20:37:22.419Z.
It reports eventual mass at least four and a U-shaped four-cell family.
3. sources/Langton_Ant_Research_2026-10-21.zip:
   Exact extracted contents in recovered_bundle/. 82 archive entries; 80 embedded-manifest hashes checked successfully.
4. sources/Langton_Ant_First_Principles_2026-10-21.zip:
   Exact extracted contents in first_principles_2026-10-21/. 116 entries; 114 embedded-manifest hashes checked successfully.
5. sources/Langton_Ant_Continuation_2026-10-21.zip:
   Exact extracted contents in continuation_2026-10-21/. 126 entries; 125 embedded-manifest hashes checked successfully.
6. sources/Langton_Ant_Continuation_2026-10-22.zip:
   Exact extracted contents in continuation_2026-10-22/. 223 entries; 222 embedded-manifest hashes checked successfully.

ZIP-level SHA-256, entry sizes and CRC values are recorded in sources/*_manifest.json and sources/zip_manifest.json. The consolidated hash audit is audits/recovered_integrity_audit.json. File integrity is not mathematical correctness.

## Important source discrepancy

The attached continuation names global-mass.md, mass-four-obstruction.md, u_family_all_proof.md and u_family_all_certificate.py. Those filenames do not occur in any of the four recovered archives. Thus the attached text's specific U-family proof has not been recovered.

The latest Library continuation instead contains a separate or later research branch claiming eventual mass at least FIVE for every finite-seed orbit. Its exact analytic reduction, affine rectangle certificate and full-field guards are present. Do not replace this distinction with the claim that the attached proof itself was recovered. The recovered branch is stronger in conclusion but remains subject to current independent proof audit.

The source URLs, pin commits and stated trust limits are retained in each archive. The supplied width-ten growth-eight raw computation is not a fully recovered replay package; only its historical descriptions remain here.

## Established within prior records, versus current trust status

All entries below are reported completed prior results, not newly proved by this recovery. The prior records say internally reviewed, not externally peer reviewed or Lean formalized unless specifically noted. Current analysis audits may revise status.

- Explicit uniform low-mass occupation:
  #{t in [s,s+N): |B_t|<=K} <= min(N, C_K N^(1-1/D_K)),
  D_0=1, D_K=2K D_(K-1)+1, C_K=2(K+1)9^K.
  Proof: first_principles_2026-10-21/ant_rethink/constructive_alternatives/explicit_low_mass_occupation_bound.md.
  This allows infinitely many sparse returns.
- Sharp axial midpoint displacement:
  |B_s symmetric_difference B_t| >= 2 ||(p_t-d_h_t/2)-(p_s-d_h_s/2)||_infinity.
  Proof: continuation_2026-10-22/ant_continuation2/chronology/axial_separator_proof.md.
- All four one-sided clocks receive a positive increment within 2K+4 updates starting at mass <=K. Bounded-mass recurrence implies all four clocks diverge. Hence only finitely many mass<=3 checkpoints.
  Proof: ant_continuation2/chronology/low_mass_recurrence.md.
- Eventual mass>=5:
  ant_continuation2/chronology/eventual_mass_five.md reduces a hypothetical recurrent four-cell subsequence to
  {-33-2n,8+2n} x {-14-2n,41+2n}, with n tending to infinity.
  ant_continuation2/planar_structure/exceptional_rectangle_proof.md certifies capture at time 728n+200304 for all n>=200.
  Crucial guard audits: chronology/mass4_first_collision.md, chronology/mass4_later_collision_guards.py, chronology/exceptional_stage_core_audit.md.
  This is NOT capture of every seed initially containing <=4 cells and is NOT mass divergence.
- Bounded retreat in two independent directions implies translating periodicity, and a nonperiodic orbit needs growing retreat area.
  Proofs: ant_continuation/global_structure/retreat_area.md and first_principles_2026-10-21/ant_rethink/constructive_alternatives/bounded_directional_retreat.md.
  Neither proves bounded retreat for arbitrary inputs nor classifies all periodic words.
- Reconstructed canonical-highway one-bit certificate: all 739 leaves and independent verifier present at ant_continuation/one_bit_certificate_restored.json and verify_one_bit_independent.cpp.
  This does NOT iterate automatically through arbitrary old debris.
- Five-macro no-adjacent-defect language reduction: ant_continuation/factor_language/five_macro_status.md.
  Graph has standard W104, impossible T24 finite-support mode, and nonstandard H component.
  H reduces to C,V,U,Q,B with lengths 15,18,28,64,74.
  Any aperiodic U/V mixture with a U blocks and b V blocks requires exactly 4+5a+2b initial black cells.
  Therefore an infinite finite-support H path must contain infinitely many C/Q/B turns.
  This does not exclude H and does not exclude infinitely many adjacent forbidden windows.
- Restricted backward-converter exclusion: recovered_bundle/ant_global/sources/negative_converter_exclusion.md.
  It is only for displacement (2,2), standard heading sector, band -3<=x-y<=7, standard periodic input, and output fewer than twelve black translation classes.
- Exact delayed-record obstruction: recovered_bundle/ant_global/boundary/delayed_record_family.md.
  Fixed five-cell family has identical four active rows at t=83, Q=3, but Q_next=59+7n. Nonstandard-window count remains 96.
  Thus raw energy production is not defect production.
- Newer failed-ansatz records: ant_continuation/wake_clock/fold_farkas_proof.md and ant_continuation2/fold_geometry/arbitrary_lookahead_obstruction.md.
  Each excludes the precisely stated candidate class, not every possible global invariant.

## Independent workstreams and stopping conditions

1. Global constraints: audit clocks/cuts, then seek a genuinely stronger recurrence, mass-growth or retreat statement. Deliver theorem with complete proof or exact obstruction; do not confuse zero density with event finiteness.
2. Word stabilization: audit 84-factor attraction and five-macro reduction; seek exclusion of infinite C/Q/B or infinitely many adjacent bad windows. H exclusion alone is partial.
3. Scattering mechanisms: retain complete XOR history, extend exact parent/affine guards, and test renewable feedback only with all-time certificates. A long repeated trace is not a counterexample.
4. Certificate and quantifier audit: replay exact checks independently and scrutinize the analytic links, especially arbitrary cells becoming a rectangle and full-field first-difference coupling.
5. Literature/inspiration: verify pinned/current primary sources and relevant OpenAI mathematical methods; distinguish source claims from formally checked propositions and avoid priority claims.
6. Recovery/knowledge integration: keep source snapshots and index fixed, record missing artifacts and reconciled differences, and relay new evidence without overwriting original external documents.

## Global unresolved obligation

Exclude or construct a finite seed whose old information causes infinitely many forbidden ten-turn windows. The support can grow, the path can leave a fixed strip, and future scatters can encounter old wakes and scars. No recovered result resolves that combination.

Do not use reversible local monotone-energy arguments, endpoint-only clock compatibility, bounded-seed compactness, finite simulations, solver timeouts, or no-counterexample findings as a proof of capture.

