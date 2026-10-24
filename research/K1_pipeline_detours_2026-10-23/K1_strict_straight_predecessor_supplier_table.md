# A strict straight gate has three actual predecessor supplier modes

23 October 2026, 18:18 UTC. New complete-port classification, submitted
for independent review. It retains old R0 and L3 suppliers, and does not
assert that any listed external itinerary has been realized.

## 1. Hypotheses and exact physical ports

Use the complete WHITE cap-four leftmost branch-free K=1 setting of
the signed collar theorem. Thus every selected contact has LEFT L3 and
every strict straight face has its signed rank3-to-rank1 gate. Normalize
one such face F to lower-left(0,0), with selected entry and exit

    A=(1,0): N,N,S,N;
    B=(0,1): N,N,S,N;
    Z=(0,0): W,W,W,E.

All three histories are RLRL. Put

    q=(0,-1), r=(1,-1),
    alpha=T1(Z)+1=T2(A)+2.

Cell q has exactly ONE S input, at alpha, from Z.L1. Cell r has exactly
THREE N outputs, supplying A.R0,A.L1,A.L3 in that order. The q->r physical
edge carries exactly r's E inputs. These are whole-history port counts,
not merely the visible interval after alpha.

Let P be the previous Gamma face, with lower-left(1,-1). Its exit is A.
The other C face incident to r has lower-left(0,-2), denoted D. The
other C face at q is the known low face of height b=M-2 southwest of Z.

## 2. Full predecessor table

The previous face P is LEFT, STRAIGHT or RIGHT. In the RIGHT case the
signed all-LEFT-L3 strict-right table retains only rows2,4,5. A genuine
rotation sends its second LEFT helper to r. The resulting complete
r histories, and the forced complete q histories, are:

    P type       r incoming   q incoming       current q rank
    LEFT         E,E,W,E     N,N,N,S           L3
    STRAIGHT     W,W,W,E     S,N,N[,N]         R0
    RIGHT row2   W,E,W       N,N,S[,N]         R2
    RIGHT row4   W,W,W,E     S,N,N[,N]         R0
    RIGHT row5   W,E,W,W     N,N,S[,N]         R2

Bracketed last N is the genuinely optional L3. Every nonbracketed
history is complete. LEFT has h(D)=M, whereas all other rows have
h(D)=b. No q input color is assumed; its WHITE first read and every
possible earlier R0 are explicitly reconstructed below.

## 3. The R0-current mode: r=W,W,W,E

The first and second N outputs of r are R0 and R2, feeding A.R0 and
A.L1. Its third N output is L3(E), feeding A.L3. Hence q has ONE E
output, and it occurs after the current S arrival: it must feed that
last r.L3 and the later A.L3.

With both incident q C heights b, its R headings are opposite N/S.
Every L arrives N, since another S input would violate the unique S
port. A prior q.R0(N) would already emit the sole E output before the
current S input and would force A.L3 before A.R2. Therefore q's first
R is the CURRENT S input, giving exactly

    q: S,N,N[,N], current q.R0 at alpha,
    T2(q)=T3(A)-2.

This is the first-white-q mode found in the globally straight reduction,
but it is justified here only for the displayed predecessor rows. It
is not a universal rule for every mixed straight gate.

## 4. The R2-current mode: r=W,E,W or W,E,W,W

The first three N outputs of r are R0,L1,R2, feeding A.R0,A.L1,A.L3.
Its only E input is L1, so q again has ONE E output, but this time it
must occur EARLIER than the current S input: it feeds r.L1 and A.L1,
which precedes A.R2 and alpha.

The equal-height opposite-R rule and unique S port therefore force

    q: N,N,S[,N], current q.R2 at alpha,
    T0(q)=T1(A)-2.

The earlier q.R0(N) is a real supplier, not omitted fuel. It writes black
before q.L1, and its E output is physically used by r.L1 then A.L1.
The current S input is R2 and departs W, not an assumed first R0. Any
remaining L3 arrives N and departs W. Its later provenance remains open.

The exact rank-two time identity is

    T2(q)-T0(q)=T2(A)-T1(A)+4.

Both spans are actual physical same-cell spans. They may be long; no
bounded period, fresh-root or disjoint-budget conclusion is inferred.

## 5. The L3-current mode: previous P is LEFT

Now r is the previous selected contact, with complete history E,E,W,E.
Its three N outputs are L1,R2,L3. Consequently q has THREE E outputs,
supplying r.R0,r.L1,r.L3, respectively. Its incident C heights are b
and M=b+2, so both R reads arrive N. The unique S input must be L1 or
L3. If it were L1, the second E output would already feed r.L1 then
A.R0 after alpha, although A.R0 precedes A.R2 and alpha. This is
impossible. Therefore

    q: N,N,N,S, current q.L3 at alpha,
    T2(q)=T0(A)-2,
    T3(r)=alpha+1, T3(A)=alpha+2, T2(Z)=alpha+3.

The actual consecutive cleanup is

    Z.L1 -> q.L3 -> r.L3 -> A.L3 -> Z.R2.

All four displayed departures before Z.R2 are L. This recovers the
signed old-stock four-L cleanup with all earlier R0/R2 reads retained.
It is not a same-full-pose deletion, new black input or permanent bud.

## 6. Consequence for the continuing proof

A strict straight gate's third-entry L3 supplier has THREE genuinely
different chronological modes: fresh q.R0, earlier-source q.R2, or
old-stock q.L3. Merely forcing a third physical entry does not collapse
these into a single deep first-R machine. The preceding RIGHT rows2/5
are the exact hidden earlier-R0 alternatives; a preceding LEFT face
has the exact signed old-L3 cleanup.

This table is necessary port-and-ordinal chronology only. It supplies
neither a connected finite ant factor for the external gaps nor a
complete positive front. No source is charged as a fresh original root.
The future neighboring face may impose further restrictions, but those
must be proved separately without reusing the globally straight unique
output premise in the wrong row.

Dependencies retained unchanged:
K1_leftmost_branch_free_middle_collar_v2.md, SHA
313509cb42cf3cb2ceb8a395896665aaddc58032de65b0af6a392ca963c3e466;
strict_left_K1_right_turn_table.md, SHA
63c41e1359c39e52f2f864d9ec8d66c9f52172af9c4969a5a350134a8a87c511;
K1_left_turn_four_L_cleanup.md, SHA
bb166fa7646904ba293dffb6e6b1023bea8c61b039f3f8c7d32b70dde121a5a1;
strict_straight_K1_port_reduction.md is retained only in its own original
globally straight scope; its deep boundary is not imported here.
