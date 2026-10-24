# Exact one-ray parity extraction and executed finite-seed pipeline

Date: 2026-10-23. This is a restricted automatic extraction bridge, not a model,
new counterexample exclusion, or the complete general finite-power compiler.

## Input and rational transfer

There are exactly eight nonempty R/L image words, indexed by incoming heading
and turn. Every image has the same endpoint and final heading as its single
coarse unit action. Thus the spatial matrix is I. Images need not have equal
lengths, exact charge, or opposite-image symmetry.

Write T_st(X,Y) for the sum of monomials at the read offsets of children t in
image s. Choose nonnegative C,D clearing all negative exponents in T and set
T'=X^C Y^D T. The signed occupation of the r-fold refined state s is the
coefficient of z^r in [(I-zT')^{-1} epsilon]_s, where epsilon_s is +1 for R
and -1 for L. Spatial coordinates have been shifted by (Cr,Dr).
Reducing the exact integral rational expression modulo two gives the read
parity series, because +1 and -1 both reduce to one. Constant denominator is
odd; reduction and polynomial gcd cancellation are exact over F2.

## A terminating extractor on the one-ray subclass

After reduction, suppose H is a polynomial in t=z^a X^b Y^c with a>0 and
nonnegative b,c, and H(0)=1. The exponent vector may be made primitive.
In the finite quotient ring F2[t]/(H), t is invertible. Consequently t has
finite multiplicative order N. Compute that order exactly by repeated modular
multiplication; this terminates without a guessed bound.

Then H divides 1+t^N. Multiplying the numerator by (1+t^N)/H puts the series
in the form P'/(1+t^N). Each monomial of P' generates one affine ray in
(r,X,Y), and addition is symmetric difference, not union. This handles
cancellation of overlapping rays correctly. Undo (Cr,Dr) on both their bases
and period vectors to obtain an exact parameter-free Presburger set [r,x,y].
Polynomial series are a finite-point special case. A denominator not supported
on one monomial ray, or a ray with zero time component, returns UNSUPPORTED,
never NONREALIZABLE.

The polynomial reductions, divisibility equality, and ISL symmetric differences
are exact. The downstream bounded-seed solver independently rechecks the base
parity and the complete all-depth substitution recurrence. It therefore does
not trust an extraction certificate merely because several depths matched.

## Executed controls

Implementation: `ray_parity_extractor.py`; output: `ray_parity_extractor.json`.

* Identity and R5/L5 presentations: all eight state parity relations extracted
  automatically, with 80 complete finite-depth fiber comparisons to literal
  refined words. R5 parity is genuinely nonconstant in depth (period two).
* Both R/L roots and mass bounds 0/1 fed end-to-end into the arbitrary-coordinate
  solver: exactly four identity outcomes and four growing-five negative outcomes.
  Identity acceptance is explicitly nongrowing. No growing model is accepted.
* Synthetic controls cover order-three univariate factors, repeated factors,
  overlap cancellation, polynomial transients, and an unsupported Pascal
  denominator.
* A fixed actual-geometry unit-nine pair RLLLLRRRR / LRRRRLLLL has a non-ray
  reduced signed denominator in all eight states. The already signed necessary
  denominator filter rejects finite-valued signed occupation, so the rooted
  repeated word cannot be ant-legal on any initial board. The same presentation's
  non-ray F2 denominator is simply unsupported by this restricted extractor.
  This repeats a known excluded control, not a new family exclusion.

An ant-legal finite block has signed occupation at each cell in {-1,0,1},
regardless of whether the initial board is finite. Thus a certified failure of
finite-valued signed occupation is a valid arbitrary-background obstruction.
The converse is false: finite-valued occupation or correct parity does not prove
chronological legality. That is why the frame/seed solver remains essential.

The integrated procedure is now executable for this one-ray parity subclass.
The general supplied-parity interface, and the mathematical complete finite-
power given-seed and mass-bounded existence procedures, retain their prior
scope. Unknown unbounded seed mass is still not decided.
