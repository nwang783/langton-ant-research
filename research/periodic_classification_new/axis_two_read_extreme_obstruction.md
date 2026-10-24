# An all-cap obstruction to a two-read extreme row at full drift (2,0)

23 October 2026, 03:39 UTC. Independently signed analytic lemma.
This is a local structural restriction, not an all-cap axis exclusion.

Normalize the lowest active row to y=0, with A=(0,0) the vertical-exit
class and B=(1,0) the horizontal-exit class, modulo full d=(2,0).
Because the row below is empty, every complete B arrival is S, while A's
headings alternate W,E,W,E,... . Exact horizontal matching makes their
history lengths equal, say m. Let C=(0,1), D=(1,1). Their history lengths
also agree, say n, because every horizontal edge in this upper row joins
these two full-drift classes. All letters below are incoming headings.

Let p_0<...<p_(m-1) be C's N-arrival ranks, and q_0<...<q_(m-1) be D's
S-departure ranks. Let c_k,d_l be their increasing representative clocks.
The lower excursion from D_(q_j) through B_j,A_j to C_(p_j) gives

    c_(p_j) = d_(q_j) + 3 - (j mod 2)*P.                (1)

Every C->D horizontal edge has

    d_l = c_k+1          for E,
    d_l = c_k+P+1        for W.                         (2)

If a_k marks C's N arrivals, C's E-output bit is a_k XOR (k mod 2).
If b_l marks D's S departures, D's E-input bit is b_l XOR (l mod 2).
Their E occurrences match by ordinal, and so do their W occurrences.
A four-step zero-voltage excursion is a first return to its starting
physical cell, hence advances that cell's read rank by exactly one.
For m>=2, P>=2m+2n>=8, so these short paths are proper segments.

## First forced ranks, valid for any m>=2

The first lower excursion forces q_0 even and p_0=q_0+2.

If q_0 were odd, D_(q_0) would have W input. Its source C_k precedes p_0
by (1)-(2). Before p_0, C has only S input, so its W-output ranks are even.
Before q_0, D has no downward departure, so its W-input ranks are even;
the extra W at odd q_0 has W ordinal (q_0+1)/2. Thus k=q_0+1.
But C_(q_0), an earlier odd S-arrival, outputs E with ordinal (q_0-1)/2.
There are only (q_0-1)/2 E inputs strictly before D_(q_0), so this E output
must reach a later D rank. Its clock is instead

    c_(q_0)+1 < c_k+1 = d_(q_0)-P < d_(q_0),

a contradiction. Hence q_0 is even. Its E-input ordinal is q_0/2, and its
source before p_0 must be C_(q_0+1). The ensuing four-step excursion has
zero voltage and no intermediate physical return, giving p_0=q_0+2.

## The second downward rank must also be even

Assume m>=2. If q_1 were odd, its W input comes from C_k, and (1)-(2) give
c_(p_1)=c_k+4. Thus p_1=k+1. Before p_1 only p_0 is an N arrival, and p_0
is even, so k must be even and larger than p_0. Its W ordinal is k/2-1.
D_(q_1)'s W ordinal is (q_1+1)/2-1, since q_0 removed one earlier W.
Consequently k=q_1+1 and p_1=q_1+2.

Now C_(q_1) is an odd S arrival before p_1. Its E ordinal is (q_1+1)/2,
including the extra E at even p_0. There are exactly (q_1+1)/2 E inputs
strictly before D_(q_1), including q_0's extra E, so its target has rank
greater than q_1. Yet its time is less than
c_k+1=d_(q_1)-P. Contradiction. Thus q_1 is even.

## Contradiction when m=2

Suppose the entire lowest row has m=2. Since q_1 is even, its input is E,
from some C_k. Equations (1)-(2) give

    c_(p_1) = c_k+4-P < c_k,

so k>p_1. If p_1 were odd, its W output would reach D at time d_(q_1)+4.
The first-return rule forces that rank to be q_1+1. This rank is odd and
has W input, hence departs S, creating a third downward rank. That is
impossible when m=2. Therefore p_1 is even.

There are exactly two N-arrival marks, p_0,p_1, both even. The E ordinal
at D_(q_1) is q_1/2+1. Its unmarked odd source C_k has E ordinal
(k-1)/2+2. Hence k=q_1-1 and p_1<=q_1-2. In particular q_1>=q_0+6.

C_(q_1) exists because C and D have the same length n. It is an unmarked
even S arrival, so outputs W. Its W ordinal is q_1/2-2, matching exactly
D_(q_1-2), whose W input has the same ordinal. Thus

    d_(q_1-2) = c_(q_1)+P+1.                            (3)

D_(q_1-1) has E input, with ordinal q_1/2. There are q_1/2+2 E outputs
strictly before C_(q_1), so its source is some C_r with r<q_1. Therefore

    d_(q_1-1) = c_r+1 < c_(q_1)+1 < d_(q_1-2),

contradicting D's chronological order. This excludes m=2 independently
of every upper-row multiplicity, width and full period.

The argument does NOT yet exclude m>=3, nor prove that every extreme row
is a singleton. The cap-eight finite graphs suggest that stronger boundary
forcing may exist, but no such extrapolation is asserted here.

Independent analytic review verifies every ordinal identity, seam sign and
four-step first-return use. The signed scope is exactly the m=2 exclusion,
not arbitrary bottom multiplicity.
