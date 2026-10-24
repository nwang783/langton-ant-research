# Coupling adjacent first-read runs gives eight-per-coordinate time

23 October 2026, 10:25 UTC. Analytic candidate; independent review pending.
This uses the separately signed generic first-read backbone theorem and the
already signed length-eight first-return classification. It searches no
new local palette, drift family, period range or multiplicity cap.

For ANY complete bi-infinite WHITE translating front, retain the first-read
backbone notation in white_front_first_read_speed_bound.md. It has length
ell, m=ell/2 R corners and m L corners, s R/L runs, and first-time increments
1+4q_i. Right corners have q=0. Every left corner has q>=1, and each start
of a left run has q>=2.

Pair each R run with the following L run, of lengths r_i,l_i in{1,2,3}.
Let t count paired runs with BOTH r_i>=2 and l_i>=2. We claim

    Q=sum q_i>=m+s+t.                                  (1)

The terms m+s are already signed. Here is the additional coupling.

Suppose v starts an L run following at least TWO R corners. Let u be its
R predecessor and p the preceding R vertex. Normalize v=(0,0) with incoming
N. The first read at u=(0,-1) is at time-1 and at p=(1,-1) at time-2,
because both are R corners with exact q=0. v's first R is at time0.

If q_v=2 and its selected predecessor read has rank j_v=1, that selected
second L occurs after one physical first return of length8. To exit along
the backbone's left edge it must arrive again with incoming N. The only
color-consistent first-return words of length8 with initial R and final
incoming N are

    A=RRRLLLLR,       B=RRLLLLRR.

This two-word classification is part of the previously independently
replayed four/eight-return table; it assumes arbitrary input colors, not
individual white input for the loop.

A reads p with R at time+2, with no intervening p read since its first R
at-2. B reads u with R at+7, with no intervening u read since its first R
at-1. Both violate consecutive-read alternation. Therefore q_v=2 cannot
have j_v=1. Since1<=j_v<=q_v=2, it must have j_v=2, an R.

If the L run has a second vertex w with q_w=1, its RRRR four-step return
forces the selected read at its predecessor v to be L, by the same exact
consecutive-read argument used in the signed run-start debt. This contradicts
j_v=2. Thus for every pair counted in t, either q_v>=3 or q_w>=2. Each pays
one additional unit beyond its run's signed minimum. Different runs have
disjoint start/second vertices, proving(1).

## Global combinatorial consequence

For each pair with t_i=0, at least one of r_i,l_i is1, so r_i+l_i<=4.
For t_i=1, their sum is at most6. Thus

    2m=sum(r_i+l_i)<=4s+2t,       m<=2s+t.

It follows that s+t>=m/2 and hence Q>=3m/2. Therefore

    P=ell+4Q>=4ell>=8D,       D=norm_infinity(d).        (2)

Round upward to P=2D modulo4: P>=8D for even D and P>=8D+2 for odd D.
These are necessary ALL-CAP WHITE period/speed bounds. They imply neither
an all-front exclusion nor104minimality, periodicity or finite-seed capture.
For small D the separate universalP>=28 or supplied-drift exclusions can
remain stronger. No equality or nearby-period scan is proposed here.
