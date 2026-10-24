# The homogeneous negative G3 circle is impossible in a complete WHITE cap-four front

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d and positive required output. No K1, global-height, root-free or
zero-output premise. Pending independent review.

THEOREM: no G3(c) cycle can be everywhere incoming R2 -> outgoing L1
at its canonical middle node, for ANY C level c. Thus an essential G3
circle with negative winding must have BOTH positive and negative
incidences. Mixed-sign circles and homogeneous positive sinks remain
live; this is not a whole-front exclusion or all-cap theorem.

The signed diagonal rigidity2bcd69ed reduces the homogeneous negative
case, after a genuine quarter rotation and cyclic index choice, to

    A_k=(k,k): NSNN,
    B_k=(k+1,k): WEEE,
    gamma: A_k -> B_k -> A_(k+1).

Gamma's physical orientation is NE and winding-1. Write ell=2a, a>=1;
then actual full d=(-a,-a). No primitive quotient is substituted.

## 1. The fourth cell has exactly three complete WHITE possibilities

Put U_k=(k+1,k-1), southeast of the three-edge arc
B_(k-1)->A_k->B_k. The complete main ports are

    A_k -> B_k, E:       (0,1,2) -> (1,2,3);
    B_(k-1) -> A_k, N:   (0,1,3) -> (0,2,3);
    B_k -> U_k, S:       B_k has ONLY rank2;
    U_k -> B_(k-1), W:   B_(k-1) has ONLY rank0.

Therefore U has exactly ONE incoming S read and ONE outgoing W read.
Exhaust all complete1..4 WHITE histories on incoming axis N/S. The only
possibilities are

    S, NNNS, NSNN.

Equivalently, if r_S counts S arrivals on R reads, port equations give
l_S=l_N=1-r_S. Thus either r_S=1 and there is no L read (singleton S),
or r_S=0 and both L headings occur once (the two four-read histories).
No two- or three-read case is omitted.

## 2. Literal main clocks retain only U=NNNS

Let alpha=T1(B_k), beta=T2(B_k), beta-alpha>=4. Full ordinal matching
on the first two displayed main ports gives

    T0(A_k)=alpha-1,
    T0(B_(k-1))=alpha-2.

The two one-use U ports consequently occur at the EXACT times

    incoming S at U: beta+1;
    outgoing W at U: alpha-3.

The output is strictly EARLIER than the input. Singleton S uses them
at the same read, impossible. NSNN uses incoming S at rank1 and outgoing
W at rank3, the wrong chronological order. Only NNNS survives, with

    T1(U_k)=alpha-3,
    T3(U_k)=beta+1,
    T3(U_k)-T1(U_k)=Delta(B_k)+4.

This is an actual source-L1/target-L3 relation, not a first-R-only map.
The opposite C face is at c+2; its L sectors both have height c-1. That
higher-height obligation alone would not prove a contradiction.

## 3. The next cell retains BOTH allowed modes but forces one actual factor

The forced U=NNNS has exactly three outgoing E uses at ranks0,2,3,
and exactly three incoming N uses at ranks0,1,2. Let

    V_k=(k+2,k-1).

Its incoming E port is fed by U_k and its outgoing N port feeds U_(k+1).
Both ports therefore have flow THREE. The complete WHITE cap-four
inventory permits exactly

    V_k=EEWE or WEEE.

Do NOT select one of these modes. Their complete ports are

    EEWE: incoming E (0,1,3), outgoing N (1,2,3);
    WEEE: incoming E (1,2,3), outgoing N (0,1,3).

In BOTH cases the third incoming and outgoing occurrences are L3.
Thus the full chronological ordinal3 matching forces the literal
consecutive factor

    U_k.L3 -> V_k.L3 -> U_(k+1).R2,

and the exact identity

    T2(U_(k+1))=T3(U_k)+2 >= T2(U_k)+6.             (1)

R0 and L3 suppliers, including both V modes, are retained. This is not
an inferred routing of a static flow or a guessed higher-rail connector.

## 4. Full-drift closure, not an infinite spatial regress

The original circle has actual d=(-a,-a), so

    U_(k+a)=U_k-d,
    T2(U_(k+a))=T2(U_k)-P.

Iterating(1) through EXACTLY a cells instead gives

    T2(U_(k+a))>=T2(U_k)+6a.

Contradiction. This explicitly closes in the actual full quotient. The
U and V roles cannot alias the original A/B roles: x-y is respectively
2,3 versus0,1, and actual diagonal drift preserves x-y. Within a role,
classes repeat only after a index steps. No off-curve ancestry, parent
iteration, unproved mode persistence, or new Gamma membership is used.

The two allowed V modes need not repeat; the ordinal3 factor is identical
in both, which is exactly the invariant required for closure. This
eliminates the homogeneous negative family at ALL heights and K values,
not merely the K1 height-limited subcase. It leaves mixed-sign G3 circles
as the genuine unresolved essential assembly mechanism.

Companion negative_triple_secondary_rail_obstruction.py/json independently
reconstructs all1..4 WHITE U/V histories and every asserted port rank.
There is no front, drift, period, radius, width or seed search.
