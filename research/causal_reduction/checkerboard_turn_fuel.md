# Checkerboard-specific turn fuel and positive revisit density

Status: independently audited analytic result, 22 October 2026, 20:52 UTC.
No inflation, eventual macro language, bounded retreat, or finite-control premise.

## Exact short normal form

Start an arbitrary finite interval with north heading and group its reads into
N consecutive pairs. Suppose the first turn of every pair is R. Write s for the
N second turns. Then s is a prefix of one of

    L^a R R                 (a >= 0),
    R L^b R R               (b >= 1).

In particular s contains at most three R's. Every L in s reads a distinct cell
that was black at the interval's entry. If m_odd is the number of entry-black
cells on the checkerboard parity read by the second turns, then

    N <= m_odd + 3.

The constant3 is attained for every m_odd>=1 by the literal turn word
RR (RL)^m_odd RRRR with its minimal first-L seed. A rotation gives every initial
heading; translation gives every initial position.

### Proof

At pair boundaries the heading is vertical. Let a paired displacement be
(dx,dy), where both coordinates are ±1. If the previous vertical heading is
encoded by e in {+1,-1}, the first turn R says dx=e. The second turn is L exactly
when dy=dx, and R exactly when dy=-dx. In coordinates
X=(x+y)/2, Y=(x-y)/2, an L therefore moves horizontally, and an R switches between
two adjacent rows and reverses the horizontal direction.

All pair-start sites are distinct within the interval: a second R read at one
of these sites, with no intervening L at that checkerboard parity, would violate
alternation. If a nonempty horizontal L run is followed by an R switch, the next
possible horizontal L would read exactly the last odd-parity cell of that run.
That cell has just been turned white, so the next second turn, if present, must
instead be R. This second switch returns to the pair-start site immediately
before the first switch, ending the R-first interval. Its endpoint may be old:
that endpoint is not assumed read within the finite interval.

Before the sole nonempty L run there can be no switch or exactly one switch.
Two initial R switches already return to the original pair-start site. These
observations give exactly the stated prefix language. In either branch the L
run reads distinct odd-parity cells, none of which is the optional initial R
cell. Hence all its L's consume distinct entry-black cells. At most three other
pairs remain. The sharp witness follows by literal geometry, or the same normal
form with b=m_odd.

## Global counting theorem

For an arbitrary N-pair interval, let b be the number of first-position L turns
and c the number of second-position R turns. Split at the b first-position L
pairs. Each of at most b+1 remaining R-first runs has at most3 second-position
R's. Each separator pair adds at most one more. Thus, on ANY initial coloring,

    c <= 4 b + 3.

Now suppose the interval's entry field has finite m_odd black cells on the
second-position checkerboard. Its black count after N pairs is

    m_odd + c - (N-c) = m_odd + 2c - N >= 0.

Consequently every finite-seed ant satisfies

    b >= ceil((N - m_odd - 6)/8).

Apply the same theorem to an interval starting one update later to exchange the
two physical checkerboards. In particular, on EACH checkerboard the lower
asymptotic density of L reads among that checkerboard's read times is at least1/8.
The ordinary checkerboard black-balance identity gives upper density at most1/2.
Only finitely many L reads can be first visits, so each checkerboard also has a
positive lower density of repeat visits. Any candidate path that is eventually
self-avoiding on either checkerboard, including a self-avoiding paired Hilbert
curve, is thereby excluded for finite support.

## Scope and controls

This is a turn-frequency and revisit constraint, not highway stabilization or a
classification of recurring geometry. It allows standard104 and does not bound
when a repeated cell was last read. The factor8 is a safe counting bound; no
optimality is claimed for the global coefficient.

morphic_candidates/check_checkerboard_turn_fuel.py exhaustively checks all
R-first words through16 pairs against literal same-cell alternation and verifies
the sharp examples for1<=m<=20. These are controls, not the all-length proof.
Earlier two-switch reasoning without the final endpoint convention would have
been incorrect: a third switch may land on an old even site at the very end.
The normal form above explicitly includes that possibility.

## Independent audit

computability/check_checkerboard_fuel_independent.py uses separate vector-heading
geometry and no imports from the source checker. It classifies all131,071 binary
second-turn words through16 pairs and checks20 sharp witnesses. The analytic
audit independently verifies the exact normal form, endpoint convention, and
global coefficient8. Its JSON report is saved alongside the checker.
