# Strict straight K=1 is obstructed by a four-port chronological closure

23 October 2026, 14:20 UTC. New unbounded ANALYTIC obstruction, submitted
for independent review. No finite factor enumeration enters the proof.
It excludes the extra straight/strict-left subcase, NOT K=1 in general.

## Hypotheses and retained prior reduction

Use EXACTLY the hypotheses and normalization of
strict_straight_K1_port_reduction.md, Sections1-3:

- complete bi-infinite WHITE cap-four front, actual full P,d;
- positively oriented first-L birth curve Gamma with K=M-c_right=1;
- Gamma straight, selected v_i=(-i,i), d=(-ell,ell), LEFT x+y<0;
- the other C face G_i at z_i=(-i,i-1) is strictly lower than M,
  for EVERY lifted i. No restriction on RIGHT neighbors or detours.

The prior reduction, by actual ordinal matching and K=1 chronology, gives

    v_i: RLRL, incoming N,N,S,N;
    z_i: RLRL, incoming W,W,W,E;
    h(G_i)=M-2.

Put q_i=(-i,i-2). It has the complete necessary history

    R0(S), L1(N), R2(N), optionally L3(N).

The actual interval D_i starts at R2(v_(i-1)), enters q_i at R0 two
steps later, and leaves q_i at R2 two steps before its endpoint
L3(v_(i-1)). Future q_(i+1) has not yet had ANY read during D_i. The
complete proof of these facts is retained in Sections2-3 of the prior
note, including the first-white-R/S and future-port arguments. No helper
color, optional L3 or physical current boundary is silently dropped.

## 1. Two west arrivals must BOTH be L reads

Let

    u_i=q_i+(-1,0)=(-i-1,i-2).

During D_i, q_i emits W at its R0 and again at its L1. These are the first
two W outputs of q_i and hence the first two W arrivals at u_i.

Either R read at u_i, if arriving W, would depart N and enter

    u_i+(0,1)=q_(i+1).

But both arrivals under consideration occur before the end of D_i,
while future q_(i+1) has not had its first read. Therefore BOTH W
arrivals at u_i must be L, not R. The complete white cap-four history
has only two L reads, L1 and L3. These two W arrivals must be exactly
those, in order. Both R reads must arrive E (the only other permitted
incoming direction at this parity). Thus the COMPLETE history is forced:

    u_i: RLRL, incoming E,W,E,W.                    (1)

This is where earlier local prepared-packet controls lack their omitted
first-R provenance. It is not enough for each visible helper history to
be independently cap-four-completable: its omitted R emits a real edge.

## 2. The whole opposite rail is forced back to height M

At u_i, the NE C face is G_i, already at height M-2. Let H_i be its SW
C face, whose lower-left coordinate is

    H_i: (-i-2,i-3).

Both R reads in(1) arrive E and turn S around H_i; none turns around G_i.
The exact local R-count height identity therefore gives

    h(H_i)-h(G_i)=2,
    h(H_i)=M.                                     (2)

This is not an added geometric assumption. It is forced by the actual
two L suppliers and their forbidden future-port alternatives.

## 3. All four physical outputs have one recipient, which is impossible

Every one of the four reads in(1) departs S:

    R(E)=S, L(W)=S, R(E)=S, L(W)=S.

Consequently their SINGLE physical south neighbor

    b_i=u_i+(0,-1)=(-i-1,i-3)

has at least four actual incoming S traversals. Cap four makes these its
ENTIRE four-read white history; both R reads thus arrive S and turn W.
Both R reads select its NW C face, which is H_i.

Its other C face is the SE face with lower-left coordinate

    (-i-1,i-4)=H_(i-1).

By(2), BOTH incident C heights at b_i equal M. The cap-four local R-count
identity requires one R around each C face at an active equal-height
corner. Equivalently, the two S R reads would require

    h(H_i)-h(H_(i-1))=2,

whereas(2) makes the difference zero. This is the contradiction.

## Conclusion and exact scope

There is NO complete white cap-four translating front with K=1 whose
chosen first-L birth curve is straight and whose EVERY immediate LEFT
other-C neighbor is strictly lower than M.

The argument retains both L suppliers, all omitted earlier helper
outputs, optional L3, the actual continuous cursor and both side-current
boundaries. It uses no bounded period/drift/radius search and no finite
short-factor exclusion. In particular the previously proposed
conditional P>=30*ell clock is superseded here by an analytic obstruction
under the SAME extra geometric hypotheses.

This does NOT exclude K=1 generally, does NOT exclude bent birth curves,
and does NOT remove equal-M branches to the LEFT of a straight curve.
For a possible K=1 front, every straight first-L birth curve must have
at least one immediate equal-M neighbor on its LEFT. Extending the
argument to bends and those retained max branches is an open next step.
The prepared period10 and finite deep positive-mass controls remain
valid in their stated relaxed/prepared scopes, but they cannot supply a
whole white front satisfying these stronger shared-edge histories.
