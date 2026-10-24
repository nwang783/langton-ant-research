# Finite second-row alternatives when the sole downward rank is zero

23 October 2026, 04:20 UTC. Independently signed analytic lemma.
Notation and the exact top-port map are from
`axis_singleton_second_row_structure.md`. Here the second row's sole
downward rank is r=0 and its length is n>=3. We prove n is 4 or5, without
any bound on the third row or any later row.

Put m=n-1. At the third row use C'=(1,2), D'=(2,2), renamed C,D below.
Their incoming-N marks are p_j and outgoing-S marks q_j, j=0,...,m-1.
Local E/W matching and the signed ballot apply unchanged. The lower strip
sends input0 to output1 in three steps with voltage0, input1 to output0
in seven steps with voltage1, and every input j>=2 to output j in three
steps with voltage 1-(j mod2). Thus

    c_(p1)=d_(q0)+3,
    c_(p0)=d_(q1)+7-P,
    c_(pj)=d_(qj)+3-(1-(j mod2))*P, j>=2.

The complete front has P>=2n+2+2m>=12, so in particular P>8.
All first physical returns below use literal lower-strip paths and exact
horizontal edges. No period cutoff is imposed.

## 1. The first three ports are forced

Write a=q0, b=q1, u=p0, v=p1. We first prove b is even.
If b were odd, its W source C_k followed by the seven-step lower path
first-returns to C_u in eight steps; hence u=k+1. Since u is the first
N mark, k is unmarked even, and u is odd. W ordinals give

    u=b      if a is even,
    u=b+4    if a is odd.

The latter leaves no C mark before the first odd D mark a, violating the
ballot. In the former case a is even and u=b. The E source C_h of D_a
first-returns through the three-step lower path to C_v, so v=h+1. Since
v>u and C_u outputs W, h>u is unmarked odd. E ordinals give h=a+3,
v=a+4. As b is odd, a<b<v, and h cannot equal u=b, this forces b=a+1.
But D_a through C_v's E output first-returns to D rank a+1=b, whose
input would be E. An odd downward rank b requires W. Contradiction.
Thus b is even.

If a were odd, the ballot forces u odd and u<=a. The seven-step path
D_b to C_u followed by its W edge first-returns to D at rank b+1. This
odd W arrival departs S, so q2=b+1 (and if m=2 there is already a
contradiction). Its W ordinal is b/2+1 because the signs of a,b cancel;
C_u's W ordinal is (u+1)/2. Thus u=b+1>a, impossible. Hence a is even.

Next suppose u is odd, while a,b are even. The same eight-step D return
forces q2=b+1. W ordinals give u=b-3. As above, the E source of D_a must
be an unmarked odd h>u, and v=h+1; its ordinal gives h=a+3,v=a+4.
Therefore b<=a+4. The W source C_k of D_(q2), followed by lower input2
of voltage1, first-returns to C_(p2), so p2=k+1. Because p2>v and C_v
outputs E, k>v is unmarked even. Its W ordinal is k/2, since the signs
of the prior C marks u,v cancel. D_(q2)'s W ordinal is b/2-1, forcing
k=b-2<=a+2<v, a contradiction. Thus u is even.

The ballot now gives a<=u. If a<u, the E source of D_a is C_(a+1),
before u, and its first return would force v=a+2<=u. Hence u=a. Its
E edge goes to D_a, and the three-step return gives v=a+1.

Here b is even and b>a>=0, so the third-row history length is at least
three. With n>=3 and the two bottom events, P>=14; P is divisible by
four, hence P>=16. The following twelve-step path is therefore proper.
The concatenation of lower input1, C_u's E edge, lower input0 and C_v's
W edge is a twelve-step first physical return to D_b. The intermediate
upper D is translated by +d, so the returned rank is b+1, an odd W
arrival and hence q2. W ordinals C_v -> D_(q2) give a/2=b/2-1, whence
b=a+2 and q2=a+3. Finally D_(q2)'s W source is precisely C_v; input2
then first-returns to C_(p2), so p2=v+1=a+2.

We have proved, with a even,

    (p0,p1,p2)=(a,a+1,a+2),
    (q0,q1,q2)=(a,a+2,a+3).                           (1)

In particular m>=3, excluding n=3. The derivation remains valid with
arbitrarily many later ports.

## 2. The remaining suffix is another standard bounce system

If a fourth mark exists, q3>=a+4 automatically. Also p3 cannot be a+3.
For if q3 is even, its E source followed by lower input3 first-returns to
p3=a+3, so that source is p2=a+2. But C_(p2)'s E ordinal is a/2+1,
whereas D_(q3)'s E ordinal is q3/2+1>=a/2+3. If q3 is odd, its W source
C_k has k<p3 because the resulting C-to-C path has voltage -1. Every W
source before p3 has ordinal at most a/2, while D_(q3)'s W ordinal is
(q3-1)/2>=a/2+2. Both cases are impossible. Thus p3>=a+4 as well.

Cut both third-row histories immediately before rank h=a+4, an even
rank. Their prefixes contain exactly the three marked ranks in (1).
Both prefixes have h/2+1 E occurrences and h/2-1 W occurrences.
Consequently ordered horizontal matching never crosses this cut: all
prefix E/W occurrences match within the prefixes, and all later ones
within the suffixes.

The two suffix histories start with turn R because h is even. Their
remaining marked ports are p_j,q_j for j>=3. Reindex j'=j-3. The lower
strip connects each such input to the same output, in three steps, with
voltage j' mod2 and compass word S,W,N for even j', S,E,N for odd j'.
These are exactly the ordered standard bounce hypotheses used in the
singleton-extreme proof. That proof depends only on these white local
histories, exact horizontal matching and the given paths; it does not
need the internal lower-strip cells to begin fresh at this cut.

If there are at least two remaining ports, the same ballot/eight-step
return contradiction applies. Hence m-3 is either zero or one. Since
m=n-1, this gives n=4 or5, as asserted.

The conclusion bounds the original SECOND row only. The third-row
history lengths and the even offset a remain unbounded here. No all-axis
exclusion or restriction on the r=2 alternative is inferred.
