# Constraints on arbitrary-choice geometric inflations

22 October 2026. Status: Sections 1–5 passed independent analytic audit.
This applies to a broader class than finite substitutions or automatic walks.
It does not assume a finite-state choice rule for the refined macro images.

## 1. Bare geometric hypothesis and subcriticality

Normalize p(0)=0. Let p(n) be an infinite unit-step square-lattice walk with
successive perpendicular steps, as in any Langton ant. Suppose for fixed k>1
and expanding scalar a it satisfies

    p(kn)=a*p(n) for every n>=0,     |a|>1.

For the ant's initial heading north, p(1) is1 or-1 in Gaussian coordinates;
hence a=p(k)/p(1) is a Gaussian integer. Also |a|<k: equality in the k-step
triangle inequality would require all k unit moves aligned, impossible for
successive quarter turns. No assumption about h(kn) is needed for this bound.

For every0<=j<k there is a possibly arbitrary history-dependent offset

    p(kn+j)=a*p(n)+delta(n,j),      |delta(n,j)|<=j<=k-1.

Thus the bounded-offset argument used in the common-scale automatic class
continues to hold without a finite controller.

## 2. Uniform all-window displacement bound

Put b=|a| and

    R_r=(k-1)(b^r-1)/(b-1).

Iterating the offset identity proves, for0<=u<k^r,

    |p(k^r n+u)-a^r p(n)|<=R_r.

Every aligned block therefore has diameter at most2R_r. If1<=t<=k^r,
the two times n,n+t lie in either the same aligned block or two adjacent
blocks. Adjacent blocks are connected by exactly one unit move, so

    |p(n+t)-p(n)|<=4R_r+1.

Choosing r minimally with t<=k^r gives

    |p(n+t)-p(n)| <= C*t^alpha,
    alpha=log_k(b)<1,
    C=4(k-1)b/(b-1)+1.

This is uniform in the starting time n, not merely a bound from the origin.
It is independent of the coloring and any refinement-choice computability.

## 3. A fully effective bound forbidding a long standard episode

A standard104 word repeated q times displaces the ant by norm q*sqrt(8).
Therefore a fixed q=q(k,a) can be computed for which NO such episode occurs
anywhere on a walk satisfying the bare inflation equation.

Here is an integer/rational algorithm avoiding real-logarithm comparisons.
Let s=|a|^2 and A=(k^2+s)/(2k), so b<A<k. Let ell be least with104<=k^ell.
Search R>=0 until

    k^R > 4(k-1) * sum_(j=0)^(R+ell-1) A^j + 1.

The search terminates because A<k. Set q=k^R. A104q-step interval has length
at most k^(R+ell), so Section2 gives an upper bound strictly below q, whereas
a q-period standard episode has displacement q*sqrt(8)>q. Contradiction.
All quantities in the search are rational with exact integer arithmetic.

## 4. Consequence for any finite-support ant in this class

If such an inflation is realized by a finite black seed of mass m, it avoids
the fixed q-period standard episode from Section3. Consequently the audited
explicit dichotomy in adjacent_defect_quantitative_compactness.md gives

    at least r+1 adjacent bad-ten pairs by time
    T_explicit(m,r,q), for every r>=0.

This is a uniform primitive-recursive divergence schedule for the number of
adjacent pairs, conditional on the proposed inflation being a valid finite
seed. It does not require the turn word to be substitutive or automatic.
It does not establish positive pair density, and it is not a contradiction:
the unrestricted possibility of infinitely many adjacent pairs remains the
open part of the highway conjecture.

The causal analysis's new arbitrary-macro heading-preserving inflation search
is a subfamily of this class. Its per-scale finite incompatibility certificates
are separate stronger exclusions, not consequences of this geometric bound.

### Uniform primitive-recursive construction of q

The auditor supplied an explicit bound for the rational search. Since s is an
integer below k^2,

    A/k <= 1-1/(2k^2),       A-1 >= 1/2.

The integer

    R_max=32k^2(k-1)k^ell

already satisfies the displayed strict inequality. Indeed, the right side
before its final +1 is at most8(k-1)A^(R+ell). After division by k^R and using
(1-1/N)^R <= 1/(1+R/N), this is strictly below1/2 at R=R_max. The remaining
k^(-R) is at most1/2. Thus q can be obtained by bounded primitive recursion,
uniformly in k and the Gaussian integer a; ell<=7 since k>=2.

## 5. Adaptive macro charge filters

Status: analytic deductions independently audited. Here additionally require
heading preservation h(kn)=h(n), so each refined block is one of finitely many
k-letter images with the appropriate coarse R or L quarter-turn endpoint.
The actual image may depend arbitrarily on the entire history.

Let Q and V be the maximum signed turn excess #R-#L among all allowed R and L
images respectively. Both image sets must be nonempty, and expanding geometry
excludes monochromatic images, hence -k<Q,V<k. For the actual first-N-turn
signed excess E(N), counting the two coarse letters gives

    E(kN) <= alpha*N + lambda*E(N),
    alpha=(Q+V)/2,   lambda=(Q-V)/2.

A finite seed of mass m imposes E(N)>=-m at every N.

**Negative maximum bias.** If Q+V<0, no finite-support inflation exists.
If lambda<0, the displayed inequality directly gives
E(kN)<=alpha*N-lambda*m, tending to minus infinity. If lambda>=0, iteration
at N=k^n gives an upper bound with leading term
alpha*k^n/(k-lambda), which tends to minus infinity because lambda<k.
Both contradict the fixed lower bound -m.

**Zero maximum bias.** Suppose Q+V=0. If Q<=0, then
E(kN)<=Q*E(N)<=-Q*m, a uniform upper bound; the midpoint inequality contradicts
p(k^n)=a^n*p(1) escaping to infinity. If Q>0 and the initial turn is L,
E(k^n)<=-Q^n; for Q>1 this violates the mass lower bound, while Q=1 gives
bounded mass at expanding endpoints and again contradicts midpoint escape.
If Q>0 and the initial turn is R, E(k^n)<=Q^n. The midpoint inequality

    sqrt(2)|a|^n <= 2m + E(k^n) + 2

excludes Q<=|a|, including equality. Therefore the only case not excluded by
these maximum-charge filters when Q+V<=0 is an R-starting path with
Q+V=0 and Q>|a|. A large UPPER bound Q by itself is not an area contradiction;
the actual adaptive blocks need not attain it.

**Sub-area-density bias interval.** Let q and v be the corresponding MINIMUM
image excesses, and suppose k>|a|^2. Complete visit alternation implies
|E(k^n)| is at most the number of distinct visited cells. The block-radius
bound makes this O(|a|^(2n)), so E(k^n)/k^n tends to zero on ANY legal initial
coloring, even one of infinite support. Applying the minimum and maximum
coarse-count inequalities and taking limits gives the necessary condition

    q+v <= 0 <= Q+V.

Thus a uniformly positive minimum bias or uniformly negative maximum bias
excludes even arbitrary backgrounds in the sub-area-density case. This is
an adaptive-choice extension of the fixed-substitution growth obstruction,
not a new assertion that every adaptive family has a fixed signed bias.
