# Signed affine-count growing-lap decision reduction

Completed 23 October 2026, 20:42 UTC. 
original-document edit, cap/horizon/seed search, or running process remains.
Universal standard104 capture and a finite-seed infinite nonstandard orbit
both remain open. No actual new nonstandard finite-seed mechanism is claimed.

## New useful result

Every SUPPLIED fixed finite literal expression

    W(n)=w_0^(alpha_0*n+beta_0)...w_t^(alpha_t*n+beta_t), n>=0,

with nonempty words and nonnegative integer affine counts has an exact decision
procedure for complete infinite-path finite-seed realizability and standard104
capture. Arbitrary headings and actual constant-stage turns are retained.

- Whole-field/head-continuous preprocessing rejects impossible unbounded
  nonrestoring or zero-drift powers, or groups real consecutive laps.
- Nonconstant affine lap displacement gives actual quadratic starts A*n^2+B*n.
  A scalar projection proves a computable ALL-HISTORY bound K on the lap
  separation of same-cell reads. For each fixed delta, quadratic terms cancel,
  so the COMPLETE same-cell relation is Presburger.
- Exact previous-read alternation and FINITE globally first-L events give the
  unique common finite seed. No old cap state or retired black garbage resets.
- Actual event successor, powered104, decides standard suffixes exactly.
- A repeated L arm requires positive-width PARALLEL previous-R affine resonance;
  transverse crossings fund only O(N) of its Theta(N^2) reads through N laps.

The genuinely new geometric ingredient is the quadratic-start collision
reduction. General inverse/ordered-event principles and the affine-position
branch are retained precedents, explicitly credited in the main note.

## Independently signed bindings

1. Main note `quadratic_lap_finite_seed_decision.md`, SHA
   0aca7916e6bc3fc9c4fb2c9e1f8469d650653e848315749018481f6532ec7524.
   Core `quadratic_lap_validator.py`, SHA
   aacac03e02ecf0d332ed1bfe1f46ee9e813901194b9a71e217c8e31768e7a337.
   Audit: `../audits/check_quadratic_lap_validator_independent.py/json`.
   Independent geometry, augmented-shift Eq and intervening-event Previous
   all agree exactly with saved FirstL/Bad sets. Odd coefficient bundling and
   rotating constant stages are separately controlled. Analytic sections1--8
   including the parallel-resonance corollary pass.

2. Fixed104 query `quadratic_lap_standard_query.py`, SHA
   242d8627502409388a721d1a486be12c8192a17a0d6b377993c82c435c2c8755.
   Audit: `../audits/check_quadratic_lap_standard_query_independent.py/json`.
   Auditor independently selects the global least-later event, composes104,
   compares exact mismatch sets and checks rotating-stage joins.

3. Arbitrary-heading addendum `arbitrary_heading_affine_lap_addendum.md`, SHA
   df9ebd03a6499635f7470593a2230a9cc3cebae6dd415d3b9ba0a4b24a32292e.
   Wrapper `normalize_affine_laps.py`, SHA
   424d18c1691e5e795d721178796f428ded9cd73ac7cd7042373e4e8131de12ad.
   Audit: `../audits/check_arbitrary_heading_lap_normalization_independent.py/json`.
   Independent controls add theta2/theta3, empty/skip-index and odd-displacement
   cases to all five frozen controls. Bookkeeping caution: the wrapper's
   `original_laps_per_group` is the HEADING-PREPROCESSING factor only. If its
   returned Program also has `bundled=True`, multiply that factor by2 for the
   total original-to-final lap mapping. Both flags are retained; no theorem
   or field-continuity correction is needed.

## Exact controls, not candidate discoveries

Grouped standard104 reconstructs exactly its original13-cell finite seed and
passes the canonical suffix query. Pure LRRL is internally alternating but
requires N(N+1) initial black cells through N laps. Punctuated LRRL also passes
alternation and is nonperiodic, but its globally first-L set is infinite, so
it is NOT a finite-seed counterexample. Equal-L and repeated-square controls
fail actual same-cell chronology. No successful nonstandard model was found.
