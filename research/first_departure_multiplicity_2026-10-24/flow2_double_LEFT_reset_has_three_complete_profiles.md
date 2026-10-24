# A flow-two double-LEFT reset has three complete profiles

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. A fixed four-corner necessary interface, pending independent review.
No global-maximum C assumption or period cutoff is used.

Take a constant-flow-two RLLR subpath, physically

    B=(1,1) -> Y=(0,1) -> Z=(0,0) -> A=(1,0).

The first and last displayed corners are RIGHT, the two middle ones LEFT.
Their full alphabets are

    Z: NSS, NNSS, NSSN; A: EEWW, EWWE;
    B: SNNS, SSNN;     Y: EWW, EEWW, EWWE.

The missing fourth edge A->B points N, with exactly two physical uses at
both ends by their complete RIGHT profiles. Match ALL physical ordinal
edges around this square, including the unused-as-b fourth edge. Retain
all same-cell rank gaps>=4. Any forced literal return to a named cell must
hit its NEXT rank, not skip an intermediate read.

Of all 36 complete profile choices, 21 violate that exact next-read
condition and 12 have a positive physical clock cycle. Exactly three
necessary OPEN rows remain:

    Z NNSS, A EEWW, B SNNS, Y EWW;
    Z NNSS, A EEWW, B SNNS, Y EWWE;
    Z NNSS, A EWWE, B SNNS, Y EEWW.

Thus, in rotation-invariant local profile names RIGHT X=EEWW/Y=EWWE and
LEFT O=WEE/U=WEEW/V=WWEE:

    the second LEFT is always V;
    the preceding RIGHT is always Y;
    first LEFT O/U forces the following RIGHT X;
    first LEFT V forces the following RIGHT Y.

This is the complete necessary ordinal/clock relation for the unit reset
square, not a claim that one of these rows has a complete board exterior.
All external ports and each complete ingress-to-egress actual channel are
recorded in check_flow2_LL_reset_square.py/json. No same-cell gap upper
bound, fresh-output payment, or closure of those external ports is added.

For comparison, the signed C-square part of 9276befb makes every LRRL
flow-two subpath have BOTH LEFT contacts V. That local RR gate also
forces an actual four-R square: at the upstream LEFT, its R0 returns to
its L1 after four consecutive R reads. Together these two finite local
gates distinguish a genuine O/U reset from an all-V event wall, while
retaining every L1/L3 supplier. General mixed geometry remains open.
