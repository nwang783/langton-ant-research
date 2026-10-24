# An all-cap twelve-time gate at shared counterflow events

24 October 2026. Additive author theorem, pending independent audit. Depends on
the now independently signed complete WHITE-front port theorem fdde7793 and
counterflow theorem16878553, with their full hypotheses unchanged. No claim of
standard104 uniqueness, global periodicity, or new regenerative controller.

## 1. Exact gate

Let one actual traversal u->v be selected BOTH by a first-R departure cycle
and by a reversed last-L cycle oriented as original movement. Both cells are
even, and the signed port theorem says u is even-SAME and v even-OPPOSITE.
The shared event times satisfy

    H(v)=F(u)+1.

Then, without a visit cap,

    H(u)-F(u)>=12,        H(v)-F(v)>=12.

Equivalently F(v)<=F(u)-11 and H(u)>=H(v)+11; the whole first/last span of the
two-cell exchange is at least23 time units. This is a timing COST for an overlap
that must not be treated as a free identification in a controller flow ledger.

## 2. Complete short-gap proof

A physical return to a cell has positive duration divisible by4: movement axes
alternate, and each coordinate has an even number of signed unit movements.
Thus only durations4 and8 need exclusion. This is a local short-gap check, not
a visit-cap, front-period, width or drift enumeration.

At the target v, normalize F(v) to incomingN at the origin. Its first turn isR,
its last turn isL with incomingS, and the preceding event (at u) isR. Any proposed
4/8-step interval therefore starts and endsR, returns to the origin with
incomingS, and leaves origin BLACK for the finalL. All first-read colors of
OTHER cells are arbitrary. Exact local color consistency suffices as a necessary
test. There are no4-step geometric words. At8 there are exactly three:

- RRRRLRRR leaves the origin WHITE, so the required finalL fails.
- RLLRLLLR reads(0,1) twice consecutively withR, conflict at tick7.
- RLLLRRRR reads the origin twice consecutively withR, conflict at tick4.

At the source u, normalize F(u) to incomingN at the origin. The first two turns
areRL because the next read is v's lastL. Its last turn isL with incomingN.
Thus the4/8-step interval beginsRL, returns to the origin with incomingN, and
leaves origin BLACK for finalL. Again there are no4-step geometric words and
exactly three8-step ones:

- RLRRRLRR reads(1,0) twice consecutively withL, conflict at tick5.
- RLLLRLLL reads the origin twice consecutively withR, conflict at tick4.
- RLLLLRRR leaves the origin WHITE, so finalL fails.

The companion script enumerates all4+64 prefix-compatible turn words per side,
reconstructs every physical position/heading, and checks each rejection. It does
not assume those local words have WHITE first colors at every other cell. Thus
prepared BLACK neighbors cannot evade this finite short-gap obstruction.

## 3. A joint counterflow time-debt corollary

Use k_F,k_L,L_F,L_L,C as in the signed overlap-corrected counterflow theorem.
On a first-departure cycle, first-time increments are1 at R corners and1-4q at
L corners, q>=1. A shared edge targets v at its LAST L, so this target corner has
q=(H(v)-F(v))/4>=3. Each overlap therefore supplies TWO additional q units beyond
the generic L-corner minimum. Since the cycle has equal R/L corners and winding
-1, its period obeys

    P>=ell+8c,

where c is the number of shared selected events on that cycle. In the exactly
reversed trajectory, a shared event targets u at its last reverse read; the
same argument and u's gate give the identical bound for its k cycle. Matching
ensures these charges use distinct target vertices. Summing separately within
the two selected families gives

    k_F*P>=L_F+8C,        k_L*P>=L_L+8C.

Use these bounds AND the signed spatial-overlap inequality, not their sum as
though they charged disjoint time. No output or visit multiplicity was capped.

## 4. Both endpoint costs are simultaneously sharp locally

The companion JSON gives an actual26-read finite factor on a SEVEN-black-cell
board, with one actual predecessor and successor surrounding the key24 reads.
The marked source u=(0,1) has exact within-factor history

    R at12 incomingE; L at24 incomingE.

The marked target v=(0,0) has exact within-factor history

    R at1 incomingN; L at13 incomingS.

At12 the physical source firstR enters the target lastL at13. Both complete
within-factor histories have age12, and their combined span is23. Neither
marked cell's first/last event is an endpoint of this26-read factor. The actual
board, all26 events, final full board and final pose are explicitly retained.
This proves the local lower constants cannot be improved using only this
prepared finite interface. LAST still means within this finite factor, not its
infinite future; this is NOT a complete WHITE front, a periodic realization,
proof of essential-cycle attainment, or autonomous regeneration.
