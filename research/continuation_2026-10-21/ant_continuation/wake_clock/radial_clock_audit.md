# Independent review of the two-cell radial-clock obstruction

Date: 21 October 2026.

Reviewed the parent's `global_structure/radial_clock_obstruction.md` and
`check_radial_clock_obstruction.py` against the clock definition in
Hao Ke's `clock_escape/PROOF.md` (source link and reviewed snapshot hash in
`../SOURCES.json`).

The ten piecewise formulas are correct. For z=x+y the field contribution
is f(4n+1-c)-f(2n-c), the candidate head has coordinate -2n and sign e=-1,
and the blank source head has e=+1. For z=x-y the rotated invariant is -1,
the field contribution is f(-2n-c)-f(1-c), the candidate head has coordinate
6n+2 and e=+1, and the blank head has e=-1. Expanding these expressions gives
all five displayed ranges in each table, with agreement at shared endpoints.

Every stated lower bound holds for a=3^(2n)>=9. In the final rotated range,
the coefficient exceeds a-1 because A=9a^3>9. In the outer unrotated range,
the coefficient exceeds a/2 because 3/2-1/a+1/(3a^2)>0. The remaining bounds
follow from the displayed ranges of U and 1/U and have positive margins.

The cited integer radial clock increases by at least one per actual update.
Consequently a difference at least 3^(2n) passes every necessary elapsed-time
clock budget T<=3^(2n), uniformly over all integer centres in both diagonals.

The scope is stated correctly: these are inequalities against one fixed
blank source. No chronological path to the proposed states, no pairwise
clock monotonicity along the proposed sequence, and no counterexample to
the highway conjecture follows. No algebraic or scope correction is needed.
