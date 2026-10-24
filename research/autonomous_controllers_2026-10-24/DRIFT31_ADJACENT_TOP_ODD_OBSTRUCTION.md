# Adjacent top odd classes force another odd class four levels below

24 October 2026. Author proof submitted for independent review.

## Exact all-cap statement

In a complete WHITE front of full drift(3,1), use T=3y-x with incoming vertical
headings at even T. Let M be the COMPLETE READ maximum. If M-1 is odd-read and
M-2,M-3 are even-read, then M-4 is odd-read.

The signed complete-read maximum lemma2d5bb1e6 gives even M and singleton N/R
there. This theorem has no growth, period, global visit cap, lower support or
single-used F-circle hypothesis. Empty classes count as even. Omitted lower
classes are UNKNOWN and may contain arbitrary complete histories.

## Direct proof

Normalize M=20. The upper no-read boundary gives T19 exactly one incoming E
and no outgoing N. Its odd parity therefore forces the singleton E/R.
T18 has no incoming S and no outgoing W. It can only be empty or singleton N;
its even parity makes it empty. T17 then has no incoming E and one outgoing N,
so its even complete history is WW.

At Q=T16 the physical ports have exactly one S arrival (from T19) and two W
departures (to T17). The first W departure follows the literal four-step path

(-16,0) ->(-17,0) ->(-17,1) ->(-16,1) ->(-16,0).

The three intervening reads are T17.R0, T20.R0+d, T19.R0+d. The final event is
Q's FIRST S arrival, with no intermediate Q read. Thus

rank(first S arrival)=rank(first W departure)+1.

Suppose Q has even length2m. Let u be the number of S arrivals at L ranks.
Its total S arrivals is1, and W departures consist of S/R plus N/L, so

2 = (1-u)+(m-u), hence m=1+2u, with u in{0,1}.

If u=0, Q has length2 and its unique S is at the sole R rank0. It cannot follow
any departure, contrary to the exact return equation.
If u=1, Q has length6 and its first/only S is at an L rank. A W departure
immediately preceding an L read must come from an R turn on S, which would be
an earlier S arrival. This contradicts that the following S is first.
Both cases fail. Therefore Q has odd multiplicity, proving the claim.

The certificate also directly lists all four even words with the fixed ports:
SN, NNNNNS, NNNSNN, NSNNNN. All fail the recorded rank equation. The only odd
word passing that equation among the complete port-count domains is NNS.
This is a local OPEN control only, not a finite factor, completed front or seed.
The bound7 used to enumerate these controls is derived from the two port counts;
the analytic proof above uses no enumeration or cap.

## Consequence for the remaining two-quadruple parameter branch

The signed interleaving/extreme results leave
O={0,1,2,5,6,6a+1,6b+2,6c+2},c>=3,1<=b<a<=c.
The separately submitted uniform top-gap theoremb74ec866 forces a=c.
Then M=6c+2 and M-1=6a+1 are odd, but M-2,M-3,M-4 are all even in this EXACT
FULL inventory. The boundary theorem contradicts the last parity.

Hence, conditional on the uniform top-gap theorem, the entire two-quadruple
single-used F-circle branch is excluded. This is NOT an exclusion of the
all-quadruple circle branch, an unconditional full(3,1) growth8 exclusion, or
an attraction theorem. Actual single-used-circle existence remains an explicit
hypothesis of the branch reduction.

## Artifacts

`certify_drift31_adjacent_top_odd.py` and
`drift31_adjacent_top_odd_certificate.json` reconstruct the physical ports,
upper forced words, same-physical return and all four failed even controls.
The analytic parity contradiction is separately explicit above.
