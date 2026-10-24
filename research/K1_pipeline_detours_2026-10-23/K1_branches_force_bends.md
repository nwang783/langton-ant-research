# Equal-height left branches force a bend; every six K=1 faces bend

23 October 2026, 14:45 UTC. New analytic extension submitted for independent
review. No bounded front scan and no global K=1 exclusion.

## 1. Retained complete-front and local straight hypotheses

Use the signed white cap-four first-L birth curve Gamma with K=1 and
actual full P,d. For TWO consecutive STRAIGHT parent faces F_i,F_(i+1),
normalize their THREE ordered selected contacts to

    v_(i-1)=(-i+1,i-1), v_i=(-i,i), v_(i+1)=(-i-1,i+1).

At all three selected contacts the complete prefix is RLR with incoming
N,N,S, parent SE and child NW. The signed K=1 chronology includes

    T_1(v_(i-1)) < T_0(v_i) < T_2(v_(i-1)) < T_1(v_i).

Put z_j=(-j,j-1). Its NE C face is parent F_j at height M; its SW
other-C face is G_j. Put q_j=(-j,j-2). No restriction is made on any
RIGHT neighbor, optional RIGHT L3, or actual side detour.

## 2. A straight equal-M branch has one exact local history

Assume h(G_i)=M. At z_i equal incident C heights force two R reads,
with opposite incoming headings E and W. The selected predecessor
v_(i-1) emits W at both its L1 and R2, so z_i has at least two W inputs.
The selected successor v_i receives N at R0 and L1, so z_i has at least
two N outputs. These two port requirements exclude every three-read
history and leave exactly four possible four-read headings:

    W,W,E,E;  W,E,E,W;  E,W,W,E;  E,E,W,W.          (1)

All have exactly two W inputs and two N outputs. Consequently neither
adjacent selected contact can have a LEFT L3 (incoming N); any optional
L3 at those contacts must stay on RIGHT with incoming S.

Actual ordinal matching and K=1 chronology eliminate the last three:

- W,E,E,W: the second N output is z_i's L1, while its second W input is
  its L3 supplied by R2(v_(i-1)). Thus L1(v_i) precedes that R2, forbidden.
- E,W,W,E: the first N output is z_i's R2, supplied by the second W input
  from R2(v_(i-1)). Thus R0(v_i)=T_2(v_(i-1))+2, forbidden.
- E,E,W,W: the first W input is z_i's R2, from L1(v_(i-1)). Its earlier
  L1 supplies R0(v_i). The local L1-to-R2 gap at z_i is at least4,
  placing R0(v_i)<=T_1(v_(i-1))-2, forbidden.

The ONLY possible complete history is therefore

    z_i: RLRL, incoming W,W,E,E.                   (2)

It has N outputs R0,L3, S outputs L1,R2, W inputs R0,L1 and E inputs
R2,L3. In particular its second E input is source q_(i+1)'s second E
output and supplies L1(v_i) two steps later:

    time(second E output of q_(i+1))=T_1(v_i)-2.   (3)

The tiny executable straight_flat_branch_local_ports.py/json independently
lists the four surviving local tables, which differ ONLY in whether the
two selected contacts retain optional RIGHT L3. The analytic four-case
proof above, not a solver sufficiency assertion, establishes(2).

## 3. The following face cannot be straight and strict

If h(G_(i+1))<M, the signed strict-corner argument requires L3(v_i)
with incoming N: the third W output of v_i supplies R2(z_(i+1)).
But(2) gives z_i only two N outputs into v_i, so such a LEFT L3 is
impossible. This case contradicts the exact physical port count.

## 4. Nor can the following face be straight and equal-M

If h(G_(i+1))=M, apply(2) at z_(i+1). Its first S output is L1, supplied
by R2(v_i) one step earlier. Thus the first S INPUT at q_(i+1) occurs at

    time(first S input of q_(i+1))=T_2(v_i)+2.      (4)

The two C faces incident at q_(i+1) are exactly G_i and G_(i+1), both M.
At this active equal-height corner, cap four forces two opposite-heading
R reads. In a complete white history, at most ONE E output can occur
before its first S input: if R0 arrives S the first S input is already
present; if R0 arrives N, it emits the first E output, L1(N) can emit W,
but R2 must arrive S before any second E output can occur. This retains
all optional L3 possibilities.

Yet(3) and(4), with T_1(v_i)<T_2(v_i), require its SECOND E output to occur
strictly BEFORE its FIRST S input. This is the contradiction.

## 5. Branch-to-bend and the all-curve necessary geometry

The two cases exhaust h(G_(i+1))<=M. Therefore:

    If a STRAIGHT K=1 parent face has an immediate LEFT C neighbor at M,
    the NEXT parent face MUST BEND.

This is local to two consecutive faces and their three explicitly
oriented contacts; no global straightness or leftmost-component
assumption is made.

Combine it with the independently signed theorem that no five successive
straight parent faces can all have strict-lower LEFT neighbors. In ANY
six consecutive faces of a K=1 curve, if all were straight, the first
five would need an equal-M LEFT neighbor. The face immediately after
that one is still inside the six-face block and straight, contradicting
the branch-to-bend rule. Hence

    EVERY SIX consecutive K=1 birth faces contain a BEND,
    number_of_bend_face_classes >= ceil(ell/6).

The count uses indexed lifted windows and actual full-quotient ell, as
in the signed five-face counting argument. It remains valid in small
quotients. In particular a globally straight K=1 first-L curve is
IMPOSSIBLE EVEN WITH equal-M LEFT branches.

This is a necessary curvature-density theorem, not a global exclusion,
new speed constant, charged budget or claim that bends are harmless.
The six local right-turn families and equal-height branches at bent
faces remain open and retain all source-L/RIGHT-L3 cases.
