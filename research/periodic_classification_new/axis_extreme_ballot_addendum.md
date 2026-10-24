# A port-ballot restriction and exclusion of three-read extreme rows

23 October 2026, 03:44 UTC. Independently signed analytic addendum. Uses the notation and signed first-rank facts of
`axis_two_read_extreme_obstruction.md`. No upper multiplicity cap is used.

## Horizontal matching has a ballot constraint

Let X be C's complete E/W output word, Y D's E/W input word. Both have the
same length n and the same total counts. Ordered equal-letter occurrences
match. An E edge changes representative clock by 1, a W edge by P+1.
There cannot be an E occurrence before a W occurrence in X whose matched
E target lies after the W target in Y: the two clock equations imply the
opposite target order. Consequently every prefix of Y contains at least as
many E letters as the equal-length prefix of X. To see this directly, a
prefix violating that inequality forces one E source inside the prefix to
have its target outside, and one W source outside to have its target
inside, giving the forbidden inversion.

In terms of the N-arrival marks p_j and S-departure marks q_j, define

    S(r) = sum_(q_j <= r) (-1)^q_j - sum_(p_j <= r) (-1)^p_j.

The ballot constraint is S(r)>=0 at every rank r. Equality of total E
counts also gives sum_j (-1)^p_j = sum_j (-1)^q_j. These statements use
only actual chronology, not any bound on P, n or transverse width.

## Every nonsingleton extreme row has forced odd p_1

Assume m>=2. The signed first-rank argument gives q_0 even,
p_0=q_0+2, and q_1 even. The second lower excursion arrives C_(p_1) from
the E source C_k of D_(q_1), with c_(p_1)=c_k+4-P. Since P>=8, k>p_1.

Suppose p_1 were even. If q_1>p_1, only q_0 lies at or before p_1, while
the two even marks p_0,p_1 both do; hence S(p_1)=-1, impossible. Therefore
q_1<=p_1. Since q_1 and p_1 are even and q_1>=p_0, ordered E matching
now gives k=q_1+1 when q_1<p_1, and k=p_1 when q_1=p_1. Before p_1 the
only marked C rank is the even rank p_0, so these source ordinals are
exactly q_1/2+1, the ordinal of D_(q_1). Either possibility gives k<=p_1,
a contradiction. Thus p_1 is odd.

The four-step path D_(q_1) through the second lower excursion and C_(p_1)
then returns to the same physical D cell. Its next rank is q_1+1, which is
odd and has incoming W, and consequently departs S. It must be q_2. Thus
any m>=2 actually has m>=3 and q_2=q_1+1, an odd rank.

## Exclusion of m=3

If m=3, the downward ranks q_0,q_1 are even and q_2 is odd. Equality of
total E counts forces exactly two even p marks. Since p_0 is even and
p_1 odd, p_2 must be even. The third lower excursion has directions S,W,N,
and C_(p_2)'s R turn then leaves E. This is a four-step first physical
return to D. It advances q_2 to q_2+1, an even rank arriving E and hence
departing S, requiring a fourth downward rank. Contradiction.

Therefore the lowest active row at actual full drift (2,0) has either
one complete visit per class or at least FOUR. This is a structural
restriction, not an exclusion of m>=4 or of all horizontal fronts.

The exploratory Presburger relaxation in `probe_axis_extreme_symbolic.py`
uses unbounded rank variables and independently returns UNSAT for m=2,3,
but the mathematical proof above does not rely on a solver result. It
returns SAT ordinal-only relaxations at m=4,5, which are NOT fronts.
