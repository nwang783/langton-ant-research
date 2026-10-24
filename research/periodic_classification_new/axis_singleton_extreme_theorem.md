# The lower extreme row is singleton at full drift (2,0)

23 October 2026, 03:56 UTC. Independently signed analytic theorem.
No multiplicity, transverse width, or full-period bound is assumed.

Theorem: in a complete white-input translating Langton front with actual
full drift (2,0), each of the two translation classes in its lowest active
row is visited exactly once. Quarter rotations give the corresponding
right-side extreme for the rotated full drift. The opposite transverse
extreme is NOT included by a reflection assumption.

Use A,B in the lowest row and C,D immediately above, with the conventions
of `axis_two_read_extreme_obstruction.md` and the independently signed
`axis_extreme_ballot_addendum.md`. Their respective history lengths are
m,m,n,n. The C incoming-N ranks are p_0<...<p_(m-1), and D outgoing-S ranks
q_0<...<q_(m-1). Every lower excursion has

    c_(p_j) = d_(q_j) + 3 - (j mod 2)*P.

Horizontal C-to-D E edges change clocks by 1 and W edges by P+1.

Suppose m>=2. The signed ballot argument already proves:

    q_0 even, p_0=q_0+2, q_1 even, p_1 odd,
    q_2=q_1+1 (odd).

If m=2, the required q_2 is already a contradiction. We may therefore
assume m>=3. Since p_0>=2 and there are m marked C ranks, n>=m+2;
consequently P>=2m+2n>=4m+4>8. Every path below is a proper segment.

## 1. The second arrival is immediately before the second departure

The forced W edge C_(p_1) -> D_(q_2) matches W occurrences by ordinal.
At C_(p_1), only the even mark p_0 is earlier, so its W ordinal is
(p_1+1)/2 - 1 = (p_1-1)/2. At the odd D rank q_2=q_1+1, the two earlier
even downward marks q_0,q_1 remove two W inputs, so its W ordinal is
(q_2+1)/2 - 2 = q_1/2-1. Therefore

    p_1 = q_1-1.                                      (1)

## 2. An eight-step first return forces the third arrival

Let C_k be the E source of D_(q_1). The signed second-excursion equation
gives c_(p_1)=c_k+4-P, so k>p_1. Exact successors force the path

    C_k -> D_(q_1) -> B_1 -> A_1 -> C_(p_1)
        -> D_(q_2) -> B_2 -> A_2 -> C_(p_2).

Starting at physical C=(0,1), its compass word is E,S,E,N,W,S,W,N.
The intermediate C visit is (2,1), while its endpoint is (0,1). No other
intermediate vertex is the starting physical C. This is therefore a first
physical return, forcing p_2=k+1.

As p_2 is the next marked C rank after p_1 and k>p_1, k=p_2-1 is unmarked.
Its E output then makes k odd, so p_2 is even. Its E ordinal is (k-1)/2:
the earlier even p_0 and odd p_1 contributions cancel. D_(q_1)'s E ordinal
is q_1/2+1. Thus

    k=q_1+3,             p_2=q_1+4.                    (2)

## 3. The fourth lower excursion reverses chronological order

The third lower excursion, followed by C_(p_2)'s E output, has compass word
S,W,N,E. It first-returns to its physical D cell, so its endpoint is rank
q_2+1=q_1+2. This is an even D rank arriving E, hence it departs S. Therefore

    q_3=q_1+2.

If m=3 this is already impossible. Otherwise D_(q_3)'s E ordinal is
q_3/2+1 = q_1/2+2: its preceding downward marks q_0,q_1,q_2 have signs
+1,+1,-1. C_(p_2)'s E ordinal is p_2/2 = q_1/2+2, because the preceding
p marks have signs +1,-1. These are exactly the same matched E occurrence,
so C_(p_2) is the source of D_(q_3).

The ensuing fourth lower excursion is thus a four-step path from C_(p_2)
to C_(p_3) of full-drift voltage +1. Its clock equation is

    c_(p_3) = c_(p_2) + 4 - P < c_(p_2),

contradicting p_3>p_2. This excludes every m>=2 and proves m=1.

Only exact physical paths, local parity, port ordinal matching and the
signed prefix ballot are used. The unbounded-rank SMT probes helped find
the eight-step return but are not premises. This result does not itself
exclude a full axis front: the singleton boundary must still be propagated
through the remaining rows. No all-axis exclusion or full conjecture claim
is made here.
