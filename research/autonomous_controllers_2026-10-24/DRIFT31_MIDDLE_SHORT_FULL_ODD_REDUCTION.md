# Complete odd-inventory reduction of the middle short all-quadruple mode

24 October 2026. Author proof submitted for independent review. This reduces
one remaining mode to a live two-parameter family; it does not close that mode.

## Exact hypothesis and conclusion

Assume a complete WHITE front with actual full drift(3,1), growth8, and the
all-quadruple single-used F-circle, in the specific complete short mode
T6=NNNSS,T7=EEEWW. Its lower complete histories are
T0..5=S,W,S,EEWE,SSNS,EEWE. Then its FULL odd inventory must be

O={0,1,2,6,7,6c+1,6a+2,6a+4}, with 2<=c<=a.

These are complete full-drift classes T=3y-x, not a selected subset of emitted
output. No claim of realization is made. The two other short modes are not
covered by this reduction.

## Full residual ownership

The five named odd classes are0,1,2,6,7, with signed T-mod3 fibre charges
(2,-2,1). Signed full-fibre matching requires charge2 modulo4 in every fibre,
so the three remaining odd classes have residual charges(0,0,1) modulo4.
Each remaining class has T>=8, since every lower history is complete.

Consequently precisely one of these alternatives occurs:
- all three are in residue2: either two positive and one negative, or all
  three negative;
- one positive residue2 class and an opposite-sign pair in residue0;
- one positive residue2 class and an opposite-sign pair in residue1.
There is no omitted residue allocation: residues0,1 have even population,
residue2 odd population, and total residual population is3.

The all-negative alternative has odd COMPLETE READ maximum and is impossible
by signed read-extreme lemma2d5bb1e6. Write the remaining families as follows:

r2: P=6a+2,Q=6b+2,N=6c+5, with1<=a<b,c>=1.
r0: P=6a+2,Q=6b,N=6c+3, witha,c>=1,b>=2.
r1: P=6a+2,Q=6b+4,N=6c+1, witha,b>=1,c>=2.

P,Q are positive checker classes; N is negative. Their actual positions may
have any order permitted by these bounds. The fixed base is0,1,2,6,7.

## All-parameter quadratic proof

The retained general wake quadratic theorem requires q=0. The certificate
constructs the exact step-two edge runs symbolically for every position order:
three orders in r2 and six each in r0,r1. Integer parameters are represented by
nonnegative ordered gaps, with explicit domain splits enforcing their distinct
lower bounds. Finite affine interval-overlap counts reconstruct every inversion
term. Every comparison and domain split is retained; this is not sampled
interpolation, a period search, or an SMT status.

The result is:
r2 has q=1 in all three orders and is excluded.
In r0 and r1, q=0 exactly for N<P<Q or Q<P<N.
The second order has negative/odd maximumN, so the actual read-maximum lemma
excludes it. Therefore only N<P<Q remains in r0 or r1.

The signed fibre congruences hold by construction. Winding is1 in every family:
the five base classes have odd total canonical y parity, while the three new
classes have even total canonical y parity. The endpoint quadratic correction
has C parity1 throughout. Literal compressed-run controls are included, but the
finite affine-domain cover, not those samples, proves the all-parameter claim.

## The refined top boundary excludes the whole r0 family

In r0 with N<P<Q, Q=6b is the actual maximumM. We havea<=b-1 andc<=a-1.
Ifa<=b-2, every other odd is at least10 belowM, contradicting signed six-level
top-gap theoremb74ec866. Ifa=b-1, the only odd within eight belowM isP=M-4:
N<=M-9, and the base0,1,2,6,7 is still lower becausea>=2,b>=3.
Signed refined top-gap theorem73bded4f forbids this too: one of
M-1,M-2,M-3,M-5,M-6 must be odd. Thus no r0 member is possible.

## The live r1 family

In r1, N<P<Q givesa<=b andc<=a. Ifa<=b-1, all other odd classes are at least8
belowQ=M, violating the signed six-level theorem. Hencea=b. Substitution gives
the stated full inventory with2<=c<=a.

When c=a, its upper odd cluster is M,M-2,M-3.
When c<a, the upper odd classes are M,M-2, with the next odd at mostM-9.
Both cases remain OPEN here. In particular, no unproved chronological ordering
c>a is assumed. The exact a=c=2 inventory is the separately signed supplied
O16 failure3779f9e7/reportcceafe8f, not a proof for larger parameters.

## Artifacts and limitations

`certify_drift31_middle_short_wake_families.py` produces
`drift31_middle_short_wake_families_certificate.json`, retaining all15 complete
order cases, affine runs, valid and invalid integer-domain leaves, comparison
proofs and literal controls. It uses the previously signed exact run-overlap
algebra fromb5f64068, with all new family endpoints reconstructed explicitly.

This result is conditional on this precise short mode, actual full drift and
growth. It does not show that arbitrary finite-seed trajectories are periodic,
that all fronts have a single-used circle, or that a new controller exists.
