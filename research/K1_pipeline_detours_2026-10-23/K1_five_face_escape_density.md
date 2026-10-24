# Every five K=1 birth faces require a bend or a left maximum branch

23 October 2026, 14:30 UTC. Localized analytic consequence of the signed
strict-straight four-port obstruction. Submitted for independent review.
No global K=1 exclusion and no finite scan.

## 1. A five-face block is enough

Use a complete WHITE cap-four translating front and its signed first-L
birth curve Gamma with K=1, actual full P,d. Gamma need NOT be straight.
Suppose just SIX consecutive lifted selected contacts can be genuinely
rotated and translated to

    v_j=(-j,j),  j=-3,-2,-1,0,1,2.

The ordered Gamma contacts switch from parent F_j into child F_(j+1).
At ALL SIX contacts, INCLUDING BOTH ENDPOINTS, the selected complete
prefix is RLR with incoming N,N,S. Equivalently the parent is the SE
C face and child is the NW C face at each contact. Thus the five parent
faces F_j, j=-2,-1,0,1,2, are traversed straight through opposite corners.
This endpoint orientation is part of the hypothesis, not an extrapolation
from an unrelated collinear primal path. Suppose each of their immediate LEFT other-C
neighbors G_j, across z_j=(-j,j-1), has h(G_j)<M. No hypothesis is made
on any part of Gamma outside this finite block, on RIGHT neighbors, or
on deeper LEFT helpers.

The local ordinal argument of Sections2-3 in
strict_straight_K1_port_reduction.md gives, using strict G_j alone,

    z_j has prefix RLR, incoming W,W,W;
    h(G_j)=M-2;
    v_(j-1) has L3 incoming N.

Using consecutive strict G_j,G_(j+1) then also forces L3(z_j) incoming E.
Consequently z_j has the full RLRL history W,W,W,E for

    j=-2,-1,0,1.                                   (1)

These are exactly the four near-corner histories needed below; no
near-corner beyond this block is used.

## 2. Three deep ports and two consecutive packets are forced

Put q_j=(-j,j-2). From (1), each of q_(-1),q_0,q_1 has ONE S input
(from L1(z_j)) and ONE E output (into L3(z_(j-1))). The white first-R
and endpoint-order argument in the signed reduction applies separately
to each of these THREE physical ports. It yields

    q_j: R0(S),L1(N),R2(N), optionally L3(N),
    T_0(q_j)=T_2(v_(j-1))+2,
    T_2(q_j)=T_3(v_(j-1))-2.                       (2)

The first-S assertion does not require an unbounded boundary: an earlier
R0(N) would emit the unique E output and force the later root L3 before
its R2. The unique S input is the specified root-R2 entry, two steps
later, so no intermediate earlier-N read can fit either.

Let D_j be the root-R2-to-root-L3 packet at v_(j-1). The global signed
K=1 chronology still orders the selected events even though Gamma may
bend outside this block. Equations(2) imply

    q_0 has NO read during D_(-1),
    q_1 has NO read during D_0.                    (3)

For example D_0 ends at T_3(v_(-1))=T_1(v_0)-2, whereas the first q_1
read is T_2(v_0)+2, strictly later. Only these two future-port facts are
used. There is NO assumption that all earlier or all future deep ports
away from the block obey a halfplane machine.

## 3. The same four-port contradiction is entirely inside the block

For j=-1,0 put u_j=q_j+(-1,0). The R0 and L1 W outputs from q_j both
occur inside D_j. Any R(W) at u_j would depart N into q_(j+1), forbidden
by(3). Both W arrivals must therefore be its L1,L3. Its complete history
is RLRL with headings E,W,E,W. Both R reads turn around its SW C face
H_j, while its NE C face is G_j=M-2, so

    h(H_(-1))=h(H_0)=M.                            (4)

All four outputs of u_0 go S into b_0=(-1,-3). This single recipient
has four S reads and both Rs around NW H_0. Its SE C face is H_(-1).
The exact R-count height identity requires their difference to be2,
contradicting(4). The contradiction uses no physical or face data outside
the specified five-face block.

## 4. Necessary geometry and a safe density statement

Call a parent face of Gamma an ESCAPE if either

- Gamma bends there rather than passing straight through opposite
  corners; or
- it is straight, but the immediate LEFT other-C neighbor has height M.

The preceding proof shows that EVERY consecutive block of FIVE parent
faces contains an escape. In particular no K=1 curve, however bent
elsewhere, has five successive strict-left straight parent faces.

If ell is the number of selected contact/face classes in the ACTUAL full
quotient, then

    number_of_escape_face_classes >= ceil(ell/5).

Indeed each escape lies in five indexed five-face windows, while all ell
windows require one. This counting allows windows to revisit quotient
classes in small full quotients; the lifted five-face proof is physical.
No primitive-period shortcut is used.

An escape is a necessary geometric alternative, NOT a payment, a new
physical cycle, an additive time budget, or evidence that K=1 is globally
impossible. Bent curves and equal-M LEFT branches remain genuine open
cases. The straight-all-strict exclusion is the zero-escape special case.
