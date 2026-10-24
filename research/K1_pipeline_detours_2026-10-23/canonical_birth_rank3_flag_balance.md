# Canonical rank3 flag balance: odd-entry producers or exact two-child duplicators

23 October 2026. Complete WHITE cap-four translating front, actual full P,d. Sections1-4 do not require K1 or a selected essential cycle. Section5 uses the signed K1 early terminal chains. This is an exact finite canonical-parent coupling, not an original-fuel bound.

## 1. A flag attached to every canonical maximum face

For each maximum C face F, let its unique canonical incoming contact have rank1 heading h. Define s(F)=1 if that contact has rank3 with the SAME heading h, and s(F)=0 otherwise. State0 includes both no rank3 and a rank3 with the opposite heading. On an oriented selected cycle this agrees with the previously signed LEFT-L3 flag. Off that cycle it is defined by the incoming canonical edge alone, not by a presumed global LEFT side or K1 event-index ordering.

Orient canonical edges parent -> child and put

    q(F) = sum_{J: p(J)=F} s(J) - s(F).

There are finitely many maximum-face classes in the actual full quotient, and every such class has one canonical parent. Therefore sum_F q(F)=0 exactly. The child sum retains actual quotient incidence, not just possible local outgoing contacts.

## 2. Complete local necessary inventory

Normalize F to the unit face with canonical entry at SE A=(1,0), incoming N and complete heading NNS, NNSN or NNSS. Let its SW,NW,NE corners be Z,Y,B. Every R at a strict other-C corner chooses F; an equal-M corner has opposite R headings. Thus the complete optimizing histories at Z,Y,B are exhausted by all alternating white histories of1..4 reads with these R choices, including ALL L1 and L3 headings.

The four complete physical boundary ports are

    A(W)->Z(W), Z(N)->Y(N), Y(E)->B(E), B(S)->A(S).

Match physical occurrences in ordinal order. Retain every same-cell rank gap>=4. Retain that A.L1 is strictly earlier than the first departure on each of the other three actual F boundary edges. No K1 interleaving is added.

A possible canonical child at Z,Y,B must respectively have prefix WWE,NNS,EEW. Its flag is1 exactly for complete WWEW,NNSN,EEWE. These are necessary local child ports; the neighboring face's own canonical minimum still decides whether it is an ACTUAL child. Dropping a possible child only decreases q.

The complete necessary corner control starts from27,783 cases and retains110. Its possible-child count histogram is36 with0,55 with1,17 with2 and2 with3. The maximum value of possible child-flag sum minus incoming flag is1. Its ONLY positive rows are:

    A       Z       Y       B       flag1 potential children
    NNS     WW      NSSS    EEWE    B
    NNS     WWE     NSSS    EEWE    B
    NNS     WWEE    NSN     EEWE    B
    NNS     EWW     SSNS    EEWE    B
    NNSN    WWEW    NSSS    EEWE    Z and B.

For the first four, actual q=1 requires B to be an actual canonical child. They have a THREE-read canonical entry A, hence a genuine final-black odd-output class. Call these actual positive faces O.

For the last row, actual q=1 requires BOTH Z and B to be actual canonical children, each with flag1. It is the unique FOUR-read positive profile. Call these actual positive faces D, the duplicators. A face with this local history but only one actual child is NOT a positive duplicator. All two-R other faces at Z,Y,B are maximum in this row; it is a real maximum-branched RIGHT/LEFT canonical fork, not a strict helper mode.

Consequently every actual face satisfies q(F)<=1, and q(F)>0 occurs only in O or D, with q(F)=1 there. The three-child possibilities do not give additional flag capacity: both have incoming flag0 and every possible child flag0. They are not excluded, but do not pay for a flag1 leaf.

The standalone complete control is canonical_max_face_child_ports.py/json. Its survivors are necessary local port/clock inventories, not a realized complete WHITE front or a claimed exterior connector.

## 3. An exact global capacity identity

Let N_O and N_D count actual positive O,D faces in the full quotient. Then

    N_O + N_D = sum_{q(F)<0} (-q(F)).

Because s(F) is0/1 and the child sum is nonnegative, q(F)>=-1. A negative face has flag1 and no flag1 child. In particular EVERY flag1 canonical leaf contributes exactly one negative unit. Thus the total number of flag1 leaves is at most N_O+N_D.

Distinct O faces have distinct canonical incoming contact classes, since a negative flat rank1 contact has a unique target face. Each is a complete RLR three-read class. Hence N_O is an OUTPUT reservation, not original fuel. The D faces are four-read alternatives and remain an explicit uncharged capacity source in this identity.

## 4. Safe combination with existing odd-output counts

When a selected K1 Gamma flag rises0->1, its signed actual entry is RLR and its outgoing right child has flag1. The local inventory above has no other flag1 child for such an incoming flag0. Thus this is an O face, and N_O>=n_up.

The previously signed strict-straight maximum-branch fall reservation uses complete q=SNS up to rotation: its two R headings are the SAME, not opposite. It cannot be a canonical incoming maximum contact, which always has opposite R headings. Therefore these n_SB reserved three-read classes are disjoint from ALL O-entry classes, not merely from the selected rises. The n_Sanc singleton-R ancestor classes are disjoint by their one-read multiplicity. With the signed injections inside those families,

    N_odd >= N_O + n_SB + n_Sanc.

No four-read D face is charged to odd output.

## 5. Application to the signed early terminal chains

Each surviving early bit11 maximum-branched RIGHT package has a distinct terminal leaf I, with canonical entry u=EEWE and flag1. There are n_A such leaves. The exact balance gives

    N_O + N_D >= n_A,
    N_odd >= max(n_up, n_A-N_D) + n_SB + n_Sanc.

Equivalently N_odd+N_D >= n_A+n_SB+n_Sanc, together with the prior n_up bound. This is not a second additive payment on top of N_odd: it describes the same output reservation and the exact remaining four-read duplicator escape.

In particular an attempted leaf-to-odd injection must account for D. A three-child fork cannot replace D for this purpose, because all of its child flags are0. Nor may a local D-shaped face be counted unless BOTH relevant children are genuinely canonical. No claim that D must be on Gamma, reproduce an early package, consume original fuel, or create a new maximum component follows. This is the next chronological gate to resolve.

Dependencies: signed canonical first-L maximum-face birth theorem; signed terminal chains31b34f93; early ancestor injection427658fb; RIGHT-L3/rise output6c107bd7; strict fall730d9bb1; all-straight-branch entrance exclusionc945fd54. No period, drift, radius or multiplicity scan is used.
