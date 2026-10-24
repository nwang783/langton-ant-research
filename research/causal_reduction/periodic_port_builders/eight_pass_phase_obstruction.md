# A four-phase obstruction for the eight-pass builder

Status: elementary exact proof, 22October2026. Independently analytically audited.
This rules out the SAME-CAP version at every cap height, not only the previously
excluded rows0..11 version. It does not rule out four-phase controllers.

## Contract and separation

Use the eight bulk passes and ports in `eight_pass_builder_plan.md`. In particular
R=L+2n is even; the return W20 pass starts at(R,8,E), and the following upper S
pass starts at(R,10,W). Each repeats n times. The settled hardware has black
rows0,9 and odd black cells on rows1,2, so its row11 is white.

Assume left cap reads remain in a fixed bounded neighborhood of L and right cap
reads remain in a fixed bounded neighborhood of R (allowing any finite vertical
height). Right cap segments join the four pairs of specified ports. The entire
right cap may translate by any fixed EVEN growth between excursions. For large
n choose an even cut c=R-2M, strictly left of every right cap read and strictly
right of every left cap read, with0<M<n. Increase M once to include both old
and new right-cap supports. These are precisely the intended finite isolated
cap hypotheses, not assumptions about arbitrary ant histories.

## The row-charge calculation

Let Q be the alternating black charge on the part of row11 at x>=c:

    Q = sum_(x>=c) (-1)^x B(x,11).

This sum is finite on every finite board. An R read adds (-1)^x to Q and an L
read subtracts it, whenever the read lies in this half-row.

The literal W20=LLRLRRRRLRRRRLLLLRLL, started at(R,8,E), has exactly two row11
reads, both R, at x=R-2 and R-1. Hence W20^n writes exactly the row11 interval
[L,R-1], each site once. Its portion x>=c is[c,R-1], of even length2M and
alternating sum0.

The later literal S=RLLR, started at(R,10,W), has exactly two row11 reads, both
L, at x=R and R-1. Hence S^n erases exactly[L+1,R], each site once. Its portion
x>=c is[c,R], of odd length2M+1, with both endpoints even. Its alternating sum
is1, so the corresponding charge change is-1. No other bulk pass reads row11.

Each right cap begins and ends strictly below row11. Apply the independently
audited alternating-row invariant with a(y)=1_(y=11) and A(y)=1_(y>11). Its
head correction is0 at both endpoints, regardless of heading. Therefore each
right cap changes the FULL row11 charge by0 modulo4. All of its reads lie to
the right of c, so this is also its half-row charge change. This conclusion
holds even if the cap travels above row11: a boundary-reflection hypothesis
is neither used nor needed. The left caps contribute nothing to this half-row.

Consequently EVERY feasible complete excursion in the specified architecture
must satisfy

    Q_after - Q_before = -1 (mod4).

## Consequences

If the final right cap is an even horizontal translate of the identical initial
cap, and old/new settled hardware is white on row11, its half-row charge is
unchanged exactly. This contradicts the required change-1. Thus no same-phase
fixed cap can fulfill the proposed regenerative contract, at ANY finite height.
The earlier global row-charge check missed this because the two endpoint fluxes
cancel when the entire row, rather than an isolated right end, is summed.

More generally let C_j be finitely many cap states, with even translations and
unchanged blank row11 outside the caps. Their charges must obey

    Q(C_(j+1)) - Q(C_j) = -1 (mod4).

Any periodic cap cycle therefore has period divisible by4. A period-four cap
cycle remains logically possible. Its left controller would also need phase
states; this argument does not supply their words, restore other rows, prove
finite fuel, or construct an autonomous orbit.

## General endpoint-flux lesson

For a fixed separated-arm architecture, compute conserved row charges at ONE
end, not only globally. The literal bulk arms determine a finite boundary flux;
cap endpoint poses determine their allowable modular charge increments. A
translated fixed cap must preserve its own row charges under even translation.
A mismatch either excludes the architecture or forces nontrivial controller
phase cycling. Permanent distributed writes or interaction with the opposite
endpoint invalidate the isolated-cap reduction and require new calculations.
