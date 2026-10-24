# Cut-order transport obstruction, 23 October 2026

The universal finite-seed standard104 conjecture remains unsolved.

## Main result

`cut_order_minimal_transport_obstruction.md` gives an ordinary live ant on an
infinite zero-margin diagonal fuel strip with perfectly monotone axial cut
order and exact minimum transport discrepancy on every subinterval, but
residual UNION6 defect density one. Nested positive binary finite-height
seeds of mass 8K+8 realize its first 4K+6 steps with the same properties.
A separate general margin-completion lemma preserves every finite physically
feasible word while setting all exact initial line margins to zero.

This rules out a residual budget based solely on charge slack, cut recrossings
and initial charge residues, without an initial-information/fuel term. It
neither rules out mass-sensitive freshness arguments nor constructs an
infinite finite-seed ant. Both proof notes have passed independent analytic review, recorded as audit KX.
The separate checker `../audits/check_cut_order_staircase_independent.py/json`
checks 1,350 literal reads, all 47,525 subintervals, and 32 general margin
completions without importing the author geometry.

## Sharper finite family

`optimal_zero_margin_staircase.md` realizes (RL)^N for every even N>=4 by a
finite zero-margin seed of mass exactly 2N. The mass is optimal under the
zero-row-margin condition. Its height is nonnegative binary and finite.
Independent analytic review passed under KX. This family is not certified through its
actual eventual continuation, and is not a capture theorem.

## Controls

- Main control: 24 finite seeds, 1,248 literal updates, 49,904 per-line sharp
  endpoint tests, 1,012 residual eleven-windows, 10 general margin completions.
- Optimal-family control: 63 parameter cases, 8,316 literal updates, through N=128.
- `manifest.json` binds the frozen proof notes and controls.

All quantified family claims have explicit all-parameter inductions and
formula proofs. Finite controls are supporting checks only.
