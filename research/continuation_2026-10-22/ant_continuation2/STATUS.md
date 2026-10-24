# Research status — 22 October 2026

## Proved within this continuation

The main computer-assisted theorem is eventual black mass at least five for
every finite seed and initial pose. The complete combined proof is
`chronology/eventual_mass_five.md`. Its analytic prerequisites, exact
all-parameter witnesses, full-field guards and implementation audits are
included in this bundle.

The decisive family is

    B_n = {-33-2n,8+2n} x {-14-2n,41+2n},  n>=200,
    initial pose (0,0),N.

By time `728n+200304` its pose is `(-2n-58,2n+98),N`, followed forever by a
standard 104-word with drift (-2,2). The northeast initial corner is never
read. The all-parameter verification retains the complete field. The finite
probes used to suggest its witness are not substituted for the exact proof.

## Not established

- The full finite-seed highway conjecture.
- A finite-seed counterexample.
- Black mass tending to infinity on every finite-seed orbit.
- Highway capture for every input containing at most three or four black
  cells; the eventual-mass theorem has different quantifiers.
- A universal closed scattering system for arbitrary old debris.
- The five-block fuel-hull conjecture or exclusion of the full infinite H
  branch.
- Exclusion of infinitely many adjacent forbidden ten-letter factors.

## Concrete next obstruction

Under infinitely many mass-at-most-K checkpoints, the head is bounded, the
four clocks diverge, and a fixed-pose locally convergent subsequence has a
limit with at most K-4 black cells. At K=4 this is uniquely the blank state.
Three forced exceptional channels then suffice for the rectangle reduction.

At K=5 or K=6 the limit may contain one or two black cells. Existing capture
results give a baseline highway for that limit, but a remote bit can interrupt
it and cause a return to its different nonblank core. One must retain all
prior marks and prove closure of those later interactions. For general K the
limit may itself be an unclassified finite seed. A mass-bound induction alone
does not supply a highway baseline, and compactness gives agreement only on
each fixed finite prefix.

The public two-black corridor proof also requires new work before arbitrary
finite induction: preservation of constraints involving two other corridors,
coverage of every new first read, a representation for one parameter that
lengthens several tracks, and a well-founded closure or termination theorem.

## Verification boundary

The new result has ordinary Python exact-integer/rational certificates and
independent literal audits. It has not been formalized in Lean or reviewed by
an external mathematician. The public two-black Lean build was inspected but
not rebuilt here, and it is not a dependency of the main eventual-five proof.
No publication-priority claim is made.

All active searches were stopped after the recorded results. This checkpoint
does not imply that research continues after delivery.
