# The voltage counter is a stream height, but its tempting local monotonicity fails

24 October 2026. Author derivation and actual standard control, for independent
review. No new exclusion of the remaining middle-short family is asserted.

## Exact cap-free stream formulas

Use the cap-free stream integration from retained
`periodic_classification_new/cap_three_shifted_stream_height.md`, Section1,
not that note's cap-three exclusion. Its unrestricted local count formula is
also explicit in `white_front_stream_defect_criterion.md`.

For actual full drift(3,1), label the unit face whose lower-left corner is
(-j,0) by j, and write its unshifted height as h_j. In our incoming-axis sector,
odd-j faces are C and even-j faces are L. For odd t and even t respectively,
the directed physical flows are

N_t = h_t-h_(t+1), S_t = h_(t-2)-h_(t-3),
W_t = h_(t+1)-h_(t-2), E_t = h_(t-3)-h_t.

Increasing T is LEFT of positive drift. Thus its decreasing-T exterior has
constant c_right, and increasing-T exterior c_left=c_right-1.

At a proper even prefix cut t, internal north edges have odd source q<=t-3;
internal south edges have odd source q<=t-1. Their voltage sum telescopes:

K = sum N_q - sum S_q = c_right-h_(t-2).

The sums start in the genuinely unread lower exterior, not an arbitrarily
cropped support. Hence the weighted-cut counter is exactly an L-face height,
not an unspecified history statistic.

For cut counts v=(w,n,s), the four incident heights can be reconstructed from
h_(t-2)=c_right-K. In particular h_t=h_(t-2)+s-n, and therefore

K_new = K+n-s

under the two-level transfer. Combining this with the signed count map gives,
with eta=N/L count of the new even cell and lambda=W/L count of the new odd cell,

B=2K+w,       B_new-B=4(eta-lambda).

Thus B modulo4 is invariant through an even gap. A sign for eta-lambda would
be an attractive monotonicity theorem, but has NOT been proved for the signed
middle-short reachable family.

## An actual complete-WHITE local sign countercontrol

The retained standard104 complete front has adjacent complete histories

H at(1,-1): WWEWWEEW,
V at(0,-1): NSSSSNSN.

The horizontal cell has lambda=3 W arrivals at L ranks; its western vertical
neighbor has eta=2 N arrivals at L ranks. Hence eta-lambda=-1. Both histories
are even and start WHITE. Their full stable chronological orders, rather than
phase-reduced orders, are stored in the certificate.

After translating the coordinate origin by(1,0), these cells have precisely
the horizontal-odd / vertical-even sector used in the local count transfer.
The ACTUAL standard full drift remains(-2,-2), not(3,1), and its growth is12.
Accordingly this is a counterexample only to a UNIVERSAL LOCAL argument that
WHITE even histories force eta>=lambda. It is NOT a counterexample to a
possible drift(3,1),growth8,reachable-prefix-specific invariant. No such
stronger invariant is presumed or refuted here.

This control is physically grounded in an already certified standard tail,
unlike the separate arbitrary-k OPEN clock relaxation. It prevents importing
an unjustified local sign into the weighted-gap argument.

## Next unresolved issue

The stream representation makes the missing condition more precise: can the
actual single-used boundary and its fixed odd-output inventory bound the
reachable L-face heights, or constrain cumulative eta-lambda across a whole
six-level block, despite individual local decreases? The cap-four maximum
rules cannot be imported into arbitrary interior histories. A boundary-only
stream localization is being reviewed separately by the coupling analysis.

`check_drift31_voltage_stream_counter.py` and
`drift31_voltage_stream_counter_certificate.json` retain the telescoping
algebra and complete actual standard control. Random signed-height controls
are algebra checks only, not physical-front evidence or the proof premise.
