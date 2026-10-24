# The same two-cell endpoints also pass every integer radial clock

Date: 21 October 2026.

This is a limit of an endpoint-only proof strategy. None of these states is
asserted reachable from the blank start. It is not a counterexample to the
highway conjecture, to eventual mass growth, or to any claimed dynamical theorem.

## Statement

Let X_0 be the blank state at (0,0),N. For n>=1 define the candidate state

    B_n={(0,2n),(2n+1,2n)},
    p_n=(2n+1,-4n-1),       h_n=S.

Use either z=x+y or z=x-y. For every integer centre c let Theta_c be Ke's
integer radial clock in that diagonal coordinate, including its rotated
heading and invariant-sign convention. Then

    Theta_c(X_n)-Theta_c(X_0) >= 3^(2n)                  (1)

for BOTH diagonal coordinates and EVERY integer c. Thus these states pass
not only the four directional endpoint inequalities, but the uniform clock
budget for any proposed elapsed time T<=3^(2n). This is an inequality test;
it supplies no path of length T.

Together with the companion note, the same candidates pass corrected row
and column parity, heading versus mass, and all critical anisotropic one-sided
endpoint clocks. The hulls conv({(0,0),p_n} union B_n) are nested in n.

## Exact calculation

Put a=3^(2n)>=9 and U=3^(-c)>0. The clock uses f(s)=3^|s|-1, with head term
f(s)/2 if e*s>=0 and -3*f(s)/2 otherwise.

For z=x+y, sigma=+1. The two black coordinates are 2n and 4n+1, with
checkerboard signs +1 and -1. The head coordinate is -2n and e=-1. Direct
substitution gives the following value D=Theta_c(X_n)-Theta_c(X_0):

| Centre range | D |
| --- | --- |
| c<=-2n | (3a^2-a-3/(2a)-1/2)U+2 |
| -2n<=c<=0 | (3a^2-a-1/2)U+a/(2U) |
| 0<=c<=2n | (3a^2-a)U+(a/2+3/2)/U-2 |
| 2n<=c<=4n+1 | 3a^2 U+(a/2+3/2-1/a)/U-2 |
| c>=4n+1 | (1/(3a^2)-1/a+a/2+3/2)/U-2 |

The formulas agree at their shared endpoints. In the first two ranges U>=1,
so the first positive coefficient alone is greater than a. In the third
range U>=1/a, giving D>=3a-3>=a. In the fourth range 1/U>=a, giving
D>=(a/2+3/2-1/a)a-2>=a. In the last range 1/U>=3a^2 and its coefficient
exceeds a/2, giving D>(3/2)a^3-2>=a.

For z=x-y use the rotated invariant -sigma and e=+1 for E,S. The black
coordinates are -2n and 1, and the head coordinate is H=6n+2. Put A=3^H=9a^3.
The blank heading has e=-1 and the candidate heading has e=+1. Substitution
gives:

| Centre range | D |
| --- | --- |
| c<=-2n | (A/2-3/2+1/a)U-2 |
| -2n<=c<=0 | a/U+(A/2-3/2)U-2 |
| 0<=c<=1 | (a-1/2)/U+(A/2-3)U |
| 1<=c<=H | (a-5/6)/U+(A/2)U |
| c>=H | (a-5/6-3/(2A))/U+2 |

In the first two ranges U>=1, so A/2-7/2>=a is enough. In the third range
U>=1/3 and 1/U>=1, giving D>=a-1/2+A/6-1>=a. In the fourth range
1/U>=3, giving D>=3a-5/2>=a. In the final range 1/U>=A and the coefficient
exceeds a-1, giving D>(a-1)A+2>=a. This proves (1).

## What follows, and what does not

For any desired finite clock budget T, choosing n large enough makes all
these radial-clock necessary inequalities hold simultaneously, with only two
black cells. It is therefore invalid to conclude eventual mass growth from
these endpoint inequalities alone. Chronological reachability, or additional
constraints not covered here, must supply a further argument.

The argument does not say that X_n and X_(n+1) pass every pairwise clock test.
It says that all X_n pass the stated necessary tests against the same blank
source. It does not replace the source by a fictitious orbit through X_n.

## Reproduction and source

`check_radial_clock_obstruction.py` compares both piecewise formulas with
direct exact rational evaluation for 1<=n<=12 and all integer centres from
-12n-6 through 12n+6. It also checks (1), invariant parities, and hull nesting.
The analytic proof, not this finite test range, covers all n and all centres.

Clock definition:
https://github.com/kehao95/langtons-ant-core/blob/22e0c9edcc566a4c2f7a9bf92f5cd05c19199617/clock_escape/PROOF.md
