# A paired-left kinematic bound for every heading-restoring turn word

23 October 2026, 06:36 UTC. Independently signed analytic lemma (audit KB).

Let a quarter-turn word of length P restore its heading, have displacement
d=(a,b) with a,b both even, and have excess g=R-L divisible by four.
Compulsory axis alternation gives a=b=P/2 modulo two, so P is divisible
by four. Consequently L=(P-g)/2 is even.

Compare the actual compass directions with the all-R word of length P
from the same initial heading. Let v_j be its j-th move. The v_j repeat
a four-cycle of unit compass vectors, and their full sum is zero. Every
L in the actual word, replacing the baseline R, flips the current heading
by a half turn relative to the baseline; that sign persists until the
next L. Pair the L positions in chronological order. The actual direction
is -v_j on each interval from the first L of a pair through the step
immediately before its second L, and +v_j otherwise. Hence

    d = -2 sum_over_pairs sum_over_its_interval v_j.

Every consecutive block of the four-cycle has each coordinate in
{-1,0,1}. With L/2 intervals, each coordinate of d therefore has absolute
value at most L:

    ||d||_infinity <= L,
    P = g+2L >= g+2||d||_infinity.                 (1)

No color hypothesis or visit cap is used in this kinematic inequality.
For a complete white translating front, the independently signed g>=8
then gives P>=8+2||d||_infinity. In particular every actual full axis-four
front would have P>=16. This is a period lower bound, not a front exclusion.
It permits N=16 in the proposed normalized-real-clock relaxation without
imposing a period cutoff. No priority claim is made.

## Odd-odd extension, independently signed in audit KJ

The same bound holds when P=4q+2 and both displacement coordinates are odd.
Then L is odd. Pair all but the last left turn; its final sign-reversed
interval is the suffix from that last L through the end of the word.
Normalize the all-R baseline directions as E,S,W,N,..., so its total
B=(1,-1). If the last-L index is j modulo4, its suffix sum S and the
residual B-2S are exactly:

    j=0:  S=(1,-1),  B-2S=(-1,1);
    j=1:  S=(0,-1),  B-2S=(1,1);
    j=2:  S=(0,0),   B-2S=(1,-1);
    j=3:  S=(1,0),   B-2S=(-1,-1).

Thus this residual contributes absolute coordinate one. The remaining
(L-1)/2 sign-reversed consecutive four-cycle blocks contribute at most
L-1 in each coordinate. Therefore ||d||_infinity<=L and
P>=g+2||d||_infinity also in this case. This removes the even-even
restriction entirely, since heading restoration makes P even. Combining
with white-front g>=8 gives P>=18 for supplied full drift(5,±1).

Thus the final signed scope is every heading-restoring quarter-turn word:
||d||_infinity<=L and P>=g+2||d||_infinity. The two parity cases above give
the complete elementary proof. The finite literal author controls through
length16 checked43,690 heading-restoring words; they are controls, not the
all-length proof.
