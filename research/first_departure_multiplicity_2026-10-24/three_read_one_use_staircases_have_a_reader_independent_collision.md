# Three-read one-use staircases have a reader-independent return collision

24 October 2026. Author all-multiplicity local obstruction, pending review.
This is a precise application of the first-port return rule, not a new
assumption that physical first-R edges are single-used. The selected
boundary edges in the stated subpath actually have total use one.
No criticality, period, age bound or paid stock assumption is used.

## 1. The fixed physical eight-cell interface

Use the actual one-use b subpath A->r->B->s->C with geometric turns
LEFT,RIGHT,LEFT,RIGHT,LEFT. Its three LEFT words are all three-read;
the RIGHT words are singleton. Normalize the complete WHITE words to

    A=(0,-1):WWE, r=(0,0):N, B=(1,0):WWE,
    s=(1,1):N, C=(2,1):WWE.

The two common readers are U=(1,-1), V=(2,0). If the selected C level
is GLOBAL maximum M, signed58fb5427's cap-free 0->0 LRL case forces
BOTH readers to be SSNN, without imposing an exterior cap. Alternatively,
if U/V are explicitly complete WHITE cap-four, their exact port counts
and physical ranks force SSNN without a maximum premise. The core
obstruction below takes these two COMPLETE SSNN words as supplied.

Let the outer reader Z=(2,-1) have ANY complete history. It may start
WHITE or BLACK and may have arbitrarily many reads. The complete ports
of U/V force

    E_in(Z)=2, N_out(Z)=2.

All other Z ports and every old stock read are retained; nothing is
assumed about their suppliers.

## 2. Exact second-N to first-E return, with no missing exterior step

The SECOND north departure of Z arrives at V's SECOND N input, its L3.
The FIRST east arrival of Z is supplied by U's FIRST E output, its L1.
Every intervening physical ordinal is fixed, giving the actual channel

    Z.Nout_second -> V.L3 -> B.L1 -> U.R0 -> A.R0
    -> r.R0 -> B.R2 -> U.L1 -> Z.Ein_first.

This has exactly eight physical steps. There is no intermediate visit
to Z. No quotient voltage or repaired edge is involved: both endpoints
are at the SAME physical Z. The channel preserves all earlier R0s and
late L3s of the named cells.

Since the endpoint is Z's FIRST E arrival, every previous Z read arrived
W. Every previous N departure there was therefore a RIGHT turn W->N.
In particular the second N departure leaves that physical cell BLACK.
Its next read, the channel's first E arrival, must be a LEFT turn E->N.
That would be a THIRD north departure, contradicting N_out(Z)=2.

This is independent of Z's initial color, total multiplicity and old
unread stock. If a proposed complete word places the first E before the
second N, the same channel is already a backward-rank contradiction;
if it inserts a W read between them, it contradicts that this actual
channel has no intermediate Z visit. Thus no hidden prior/future read
can repair the exact physical return.

## 3. Exact domains corroborate the all-size argument

Let R_E=R_W=a, which follows from Ein(Z)=Nout(Z)=2. Then a<=2. A complete
WHITE history has n=4a or4a-1, so n<=8; a complete BLACK history has n=4a
or4a+1, so n<=9. These are consequences of the exact two port totals,
not imposed read cutoffs. The certificate retains every such complete
word:18 WHITE and22 BLACK histories. Each physical eight-step channel
is checked and each word has the recorded ordinal collision.

In particular WWWWEWE and WWWWEWEW are NOT uncapped completions. They
satisfy a naive before/after port inequality, but the channel returns
from their R2 directly to R4, skipping L3. Their apparent seven/eight-read
shield is removed by actual chronological matching, not by GLOBAL-M
height or an arbitrary multiplicity limit.

## 4. Structural scopes

Consequently the GLOBAL-M one-use subpath L0,R,L0,R,L0, where bit0 means
a three-read LEFT, is impossible with UNBOUNDED exterior multiplicity
and arbitrary initial color at the outer reader. All supplied boundary
cells and U/V are still complete WHITE histories. No arbitrary all-cap
first-R maximum rule or constant-height theorem for every b-circle is
exported.

A separate corollary holds in a complete WHITE cap-four front even at
a nonmaximal selected level: U/V's cap-four port/rank closure supplies
the same SSNN words. This does not bound the length of a general one-use
run, whose bits may rise to four reads, encounter LL/RR, change heading,
or leave this exact staircase geometry.

The four-read alternating mode remains open: its outer suppliers lie
on a lower C terrace and have different first-port orders. The present
obstruction must not be carried to that mode or to a mixed triple by
forgetting optional L3. No whole-front/capture exclusion follows.
