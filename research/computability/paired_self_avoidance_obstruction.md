# A finite-support ant cannot be eventually self-avoiding on either parity

22 October2026. Status: new analytic lemma submitted for independent review. No highway conjecture is assumed. This excludes a natural paired-time Hilbert-style synthesis target, not general paired-time scaling with repeated cells.

## Statement

Let p(t) be the read positions of an infinite classical ant orbit on a finite initial black set. Then neither sequence

    p(0),p(2),p(4),...    nor    p(1),p(3),p(5),...

is eventually injective. Equivalently, after every time cutoff there are two later even times reading the same cell, and likewise two later odd times.

The proof uses only the local turn rule and finite support. It does not use the current highway results, the finite-domain escape theorem, or any finite simulation.

## 1. Exact paired-step geometry

Normalize the initial heading to north. At even times the heading is vertical and at odd times it is horizontal. Define

    q_n=p(2n),
    q_(n+1)-q_n=(dx_n,dy_n),   dx_n,dy_n in {+1,-1}.

The first physical move of this pair is horizontal, with sign dx_n, and the second is vertical, with sign dy_n. Put dy_(-1)=+1 for the initial north heading. Then

    the turn at time2n is R iff dx_n=dy_(n-1),
    the turn at time2n+1 is R iff dy_n=-dx_n.

These identities are checked directly in the four possible entering directions.

## 2. Eventual injectivity forces eventual first-R pairs

Assume the even positions q_n are eventually injective. Choose a tail on which they are injective. The union of the finite initial black set and the finitely many even cells visited before that tail is finite, so only finitely many tail indices can hit it. Beyond their last hit, every q_n is a previously unread, initially white cell. Hence every even-time turn is R.

Writing tau_n=dy_n, the paired increments from this point satisfy

    dx_n=tau_(n-1),   dy_n=tau_n.

In rotated coordinates X=(x+y)/2 and Y=(x-y)/2, this gives

    Delta X_n=(tau_(n-1)+tau_n)/2,
    Delta Y_n=(tau_(n-1)-tau_n)/2.

Thus Y_n+tau_(n-1)/2 is constant. The paired path lies on two adjacent horizontal rows. On one row it can only move horizontally right; on the other it can only move horizontally left. A change of row is a vertical step and reverses the permitted horizontal direction. The coordinates may be half-integral after an arbitrary translation, which does not affect the argument.

## 3. Directed-ladder lemma

An infinite self-avoiding walk with these two-row rules makes at most one vertical switch.

To prove this, start on the right-moving row at abscissa X0; the opposite case is symmetric. Suppose the first switch occurs at A>=X0 and the second at B<=A. If B>=X0, the second switch already lands on the previously traversed interval [X0,A]. If B<X0, the ant is now on the right-moving row below that interval. Continuing horizontally eventually hits X0. Switching back before reaching X0 instead lands on the already traversed opposite-row interval [B,A]. Either choice gives a repeated vertex after finitely many steps. Therefore an infinite self-avoiding continuation cannot have a second switch.

Consequently tau_n is eventually constant, and the paired positions eventually advance by one fixed diagonal vector (tau,tau).

## 4. The other parity then needs infinitely many initial black cells

With dx_n=dy_n=tau, the second turn in every pair is L. Its read position is

    p(2n+1)=q_n+(tau,0).

These positions form a translating diagonal ray of distinct odd-parity cells. They cannot coincide with even-parity cells, and only finitely many can occur in the finite earlier odd history. Thus infinitely many of these L turns are first reads and require distinct initial black cells, contradicting finite support.

This proves the even-time claim. Shift the orbit by one step and rotate the axes to make its new heading north; the finite updated board is still finite, so the same argument proves the odd-time claim.

## Scope for inverse synthesis

A self-avoiding unit-step curve on a square lattice can be rotated/scaled into a diagonal-step paired curve and decoded into a compulsory-turn ant path. The theorem excludes ALL such self-avoiding paired curves as finite-support ant candidates, including Hilbert-like ones, regardless of their automatic state count or substitution format. Such curves may still produce valid ants on infinite backgrounds.

It does not exclude paired-time self-similarity itself, curves that revisit paired vertices, or the broader hypothesis of at most TWO visits per physical cell. The last class remains a separate open construction/obstruction target here.
