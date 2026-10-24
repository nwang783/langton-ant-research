# A sharp initial-color allowance when no A bridge occurs

Working analytic consequence, 21 October 2026. This is a local completed-cap
theorem, not a proof of global highway capture.

## Statement

Use the rows, heading sector and completed-cap hypotheses of
`../global/fresh_a_cap_shift_inequality.md`, but permit arbitrary initial
colors on A as well as all the other rows. Let `b_A` count initially black
A cells on the visited footprint. Assume no black A upper bridge occurs:
`H=0`. Define

    S=7 Delta_A-4 Delta_B+Delta_C-8M.

Then

    S+L_C <= 2 b_A.

Only the initially black A cells used as the indexed cell of a positive run
are needed on the right. Thus the bound also applies to infinite initial
support when the right side is restricted to the finite visited footprint.

## Proof

The scattering decomposition and the run classification in the cited proof
use A's freshness only to exclude bridges and to obtain the earlier-short
sponsor in its Section 5. Here bridges are excluded explicitly. All roofs
are zero-bridge diamonds; all remaining C upper excursions are the same short
right moves or left chains through black lower A events. The run accounting,
endpoint restrictions, and capacity inequalities in Sections 2--4 and 6
therefore remain valid.

In particular, every positive run has the same form, with a unique index s:
a zero excursion z_01 based at C_(s-1), a short through B_s, and a zero
excursion z_10 based at C_s. Its contribution is exactly `S_run=2`. It visits
T_s and T_(s+2), requires A_s black at its start, and requires A_(s+1) white
at its start.

If A_s was initially white, the original earlier-short sponsor proof still
applies. Neither T_s nor T_(s+2) was previously visited. The black state at
A_s must have been produced by its earlier white departure to T_(s+1), and
no later black read at A_s could have been repaired before T_s is visited.
The visit to T_(s+1) then arrives at A_(s+1) on white: a black upper arrival
would be a bridge, which H=0 excludes. To make A_(s+1) white again requires
one intervening black lower read. Its following B_s event must be black to
avoid erasing A_s; this leaves B_s white. Before the positive run, the first
visit restoring B_s black must be a short C upper excursion. These sponsors
are distinct for distinct indices s.

If A_s was initially black, omit the sponsor obligation and call that positive
run exceptional. There is at most one positive run for each s, because two
would repeat T_s and T_(s+2). Hence the number E of exceptional runs is at
most b_A.

Let B count all positive runs. Assign the earlier shorts to each of the
nonexceptional positive runs, and let c count the assigned shorts in each
run. Then `sum c=B-E`. The capacity inequalities remain unchanged: every
nonpositive run satisfies `S_run+2c<=0`, and each positive run has c=0 and
`S_run=2`. Therefore

    sum S_run <= 2B-2 sum c = 2E <= 2 b_A.

The exact whole-segment identity is `S=sum S_run-L_C`. This proves the bound.

## Scope

This proof permits old A colors without treating them as fresh. It does not
handle H>0: positive roof chains change the excursion decomposition. It also
does not turn b_A into a fixed global budget when the cap moves. Each of
those extensions requires a separate argument.

## Sharp witness

Start at `(0,-4)` facing west. Make exactly these four cells black:

    (1,-3), (1,-2), (1,-4), (2,-4).

After twenty updates with word `RRLLRRRRLLRLLRRRRLLR`, the ant returns to
`(0,-4)` facing west. The path never exceeds the cap. An independent literal
replay of the events in `../root/cap_shift_old_counterexample.json` gives

    M=2, H=0, L_C=0,
    (Delta_A,Delta_B,Delta_C)=(2,-1,0),
    b_A=1, S=7(2)-4(-1)+0-8(2)=2.

Thus `S+L_C=2 b_A`. Coefficient two cannot be decreased while holding the
other displayed coefficients fixed.
