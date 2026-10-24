# A strict straight face cannot precede LEFT on the leftmost branch-free curve

23 October 2026, 18:28 UTC. New actual-supplier obstruction, submitted for
independent review. Equality and prior-R0 alternatives are retained. This
does not exclude the remaining straight/right/left architecture.

## 1. Exact hypotheses and main ports

Use the signed complete WHITE cap-four leftmost branch-free K=1 setting.
Write b=M-2. Every strict-LEFT C face has height <=b; every selected
contact has LEFT L3. Suppose a STRAIGHT face F is followed by LEFT G.
Normalize

    F lower-left(0,0), G lower-left(-1,1);
    A=(1,0), B=(0,1), O=(-1,1);
    Z=(0,0), q=(0,-1), r=(1,-1), e=(-1,0), u=(-1,-1).

A and B have N,N,S,N, Z has W,W,W,E, and O has W,W,E,W,
all RLRL. The next Gamma face after G is H with lower-left(-2,0).
It cannot be LEFT: that would next enter the known b C face at(-1,-1).
Thus H is STRAIGHT or RIGHT. In either case its first unused LEFT
helper is e and its strict-helper history begins R0(S). Exact output
ordinals of B and O give

    T0(e)=T1(O)+1=T2(B)+2.                            (1)

In particular e has no actual read before this future first S input.
The main gate ends by A.L3 -> Z.R2 -> B.L1, so all q outputs used below
reach u strictly before T1(B), hence before T0(e).

## 2. The complete q predecessor modes

Retain the independently signed predecessor-supplier table:

- If F's predecessor is S or RIGHT row4, q=S,N,N[,N], current R0(S).
- If it is RIGHT row2/5, q=N,N,S[,N], current R2(S).
- If it is LEFT, q=N,N,N,S, current L3(S).

The current S input is alpha=T1(Z)+1=T2(A)+2. In the first mode q.R0
and q.L1 emit its FIRST TWO W outputs before A.L3. In the second mode
q.L1 and q.R2 emit its FIRST TWO W outputs before A.L3. Their arrivals
at u precede T1(B). In the third mode q has exactly ONE W output, at
q.L1, and its arrival at u is again before T1(B).

Any R read at u arriving W would depart N and visit e before its first
read (1). Therefore EVERY one of these early W arrivals at u is L.
This is an actual future-port restriction, not an assumed helper color.

## 3. Two early W arrivals are impossible

In either of the first two modes, the two early W arrivals must be u's
L1 and L3. Its full history is therefore E,W,E,W, with both R arrivals E
and every output S. The incident NE C face of u is the known b face
at(-1,-1), so both R(E) force its SW C face J at(-2,-2) to height M.

If J were not on Gamma it would be strictly LEFT: the C-contact step
from the known LEFT b face through u cannot cross Gamma, since u has
unequal incident C heights. The signed collar would then forbid M.
Thus J is a Gamma face. At u its other C face is LEFT and below M, so
u is an UNUSED LEFT corner of J.

There are just three possible local Gamma placements with u as an
unused LEFT corner: a straight face, a right face with u its first LEFT
helper, or a right face with u its second LEFT helper. A LEFT face has
no unused LEFT corner. After the appropriate genuine rotations, their
all-LEFT-L3 strict helper histories at u are respectively

    S:             E,E,E,W;
    RIGHT first:   E,E,E or E,E,E,W;
    RIGHT second:  E,W,E; E,E,E,W; or E,W,E,E.

None is E,W,E,W. This is the signed strict straight/right inventory,
not a new search. Hence both two-W predecessor modes are impossible.
One can also recover the stricter south-neighbor four-S rail, but it
is not needed for this all-placement helper comparison.

## 4. The one-W mode, including its M/M escape

It remains that F's predecessor was LEFT, q=N,N,N,S, and u has exactly
ONE W input, before T1(B). That input is L, as already proved. Every
R at u must therefore arrive E.

A one-R complete history would give h(J)=b+1=M-1. The same C-contact
step places J strictly LEFT (it cannot be a maximum Gamma face),
contradicting the collar. Thus u has two R(E), J has height M and lies
on Gamma. With only one W arrival and cap four, its possibilities are

    E,W,E[,E], current W at L1; or
    E,E,E,W, current W at L3.

The second is impossible independently of later geometry: its earlier
L1(E) would already depart N and visit e before (1).

Therefore u=E,W,E or E,W,E,E. Comparing the COMPLETE unused-LEFT-corner
inventory in Section 3, J must be a RIGHT face with u its SECOND helper,
using row2 or row5. This RETAINS the equality escape: its southeast
corner v=(-1,-2) is a selected flat M/M contact, and its next Gamma face
K has lower-left(-1,-3). It is not replaced by a strict b neighbor.

## 5. The equality escape forces the forbidden next LEFT

Cell q has exactly THREE N inputs, supplied by the three N outputs of
its south physical neighbor z_K=(0,-2). This is K's first LEFT corner
in the orientation whose entry is v and whose incoming direction is SE.

If K were STRAIGHT, z_K would be its strict first LEFT helper, with
incoming E,E,E,W and only ONE N output. If K were RIGHT, the first
LEFT helper histories are E,E,E or E,E,E,W, again only ONE N output.
Both contradict the whole physical three-N port count of q.

Thus K is LEFT, and z_K is its selected exit with E,E,W,E and three
N outputs. But J is RIGHT followed by LEFT. The signed R,L theorem
forces J to be ROW4, contradicting the row2/row5 inventory forced by u.
This eliminates the retained equality case without discarding it.

Therefore F cannot be STRAIGHT followed by LEFT.

## 6. Global grammar consequence

Together with the signed R,L,L exclusion and embeddedness (three equal
consecutive bends close a unit zero-displacement square), this implies
that every LEFT face is immediately preceded by RIGHT. Indeed a maximal
LEFT run has length at most two; a double LEFT run must start after S
by R,L,L exclusion, but S,L is now impossible. Thus LEFT runs are single,
and cannot start after S.

Since the embedded essential circle has #R=#L, every RIGHT is then
immediately followed by LEFT as well. The full cyclic face word is a
concatenation of single S faces and R,L pairs. In particular EVERY RIGHT
is row4. The prior-RIGHT row2/row5 straight-supplier modes are eliminated
globally by this grammar, rather than silently removed from the local
table. A straight gate is now funded either by its prior LEFT old-L3
cleanup or the prior STRAIGHT first-R0 mode.

The signed no-(R,L)^3 result bounds each run of pairs by two. Hence if
m=#R=#L, s=#S, ell=2m+s, then m<=2s and

    s>=ceil(ell/5).

Five consecutive S faces are forbidden by the signed five-face escape
criterion in this same branch-free setting, so S runs have length at
most four. These are necessary geometry/chronology constraints, not a
positive-front construction or finite-original-fuel charge.

Dependencies retained unchanged:
K1_strict_straight_predecessor_supplier_table.md, SHA
f1dabd689180c2e1fce744cae34c84226a1078efd03a99b5b50be40158bc9c38;
K1_leftmost_branch_free_middle_collar_v2.md, SHA
313509cb42cf3cb2ceb8a395896665aaddc58032de65b0af6a392ca963c3e466;
K1_right_left_forces_row4_gate.md, SHA
04953c96737e932323f29e343dfd07096401c4fa74f710bec07a3c76a8fcc3ed;
K1_row5_ear_two_early_exits_obstruction.md, SHA
a95c476e7979ac0123c74474bc4228eea32650edc893a1ef6d15b37b21a12228;
strict_left_K1_right_turn_table.md, SHA
63c41e1359c39e52f2f864d9ec8d66c9f52172af9c4969a5a350134a8a87c511.
