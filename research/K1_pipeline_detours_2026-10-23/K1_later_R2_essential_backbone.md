# A genuine later-R2 essential backbone in the reduced K=1 geometry

23 October 2026, 18:34 UTC. Conditional consequence of the signed
straight/LEFT exclusion, submitted for independent review. This is a
NEW future-paired-R2 family, not the old earlier-paired-R dependency map.

## 1. Reduced maximum geometry

Use the complete WHITE cap-four leftmost branch-free K=1 setting. The
signed straight/LEFT exclusion and turn balance give a cyclic word of
S tokens and R,L pairs. Every RIGHT face is strict row4. A straight face
has one LEFT helper W,W,W,E; a row4 right face has helpers W,W,W,E and
N,N,N,S, in their genuine rotated normalizations. LEFT faces have none.
Every selected contact has LEFT L3.

If ell is the number of Gamma face/contact classes, #R=#L=m and #S=s,
then ell=2m+s. The number of unused LEFT helpers is s+2m=ell. Strictness
prevents one such helper from being another selected contact or serving
two distinct Gamma maximum faces. Thus selected contacts and helpers
give exactly 2ell distinct full-drift physical classes.

The signed collar theorem gives one canonical MIDDLE LEFT circle.
Its physical length is 2ell and winding +1. At every selected contact
and EVERY helper in the reduced row4 geometry, its canonical pairing is

    incoming L1 -> outgoing R2.

In particular every edge of this contour DEPARTS at an actual R2 and
ARRIVES at an actual L1. There are no outgoing-L1 negative-clock corners
on this contour. This is precisely where eliminating RIGHT rows2/5
matters; their old table must not be used to assert this earlier.

## 2. Exact new dependency and chronological identity

At each contour cell y, pair its incoming L1 with its LATER R2 at the
same physical cell. The actual edge supplier is x.R2, with

    T1(y)=T2(x)+1,
    T2(y)-T2(x)=1+[T2(y)-T1(y)] >=5.

Following these future-paired R2 nodes gives the embedded essential
contour just identified. One node occurs per physical quotient class,
not both R0 and R2 at one class. It is a genuine +1 full-winding cycle,
not a dependency forest whose existence is presumed from max-C activity.
Its complete clock telescopes to

    P=2ell+sum_y [T2(y)-T1(y)] >=10ell,               (1)

where y runs over the selected contacts AND the unused LEFT helpers.
All spans are actual physical times and may be longer than P. Their
positive increments on this one cycle justify the telescope; unrelated
gate intervals are not added to it.

The positive-clock TOP-left side contour is NOT canonical TOP nodes.
Its already signed identity is

    P=2ell+sum_selected [T1(v)-T0(v)].

Comparing the two exact clocks gives the genuine first/second-read
coupling

    sum_selected [T1(v)-T0(v)]
      =sum_selected+helpers [T2(y)-T1(y)] >=8ell.     (2)

This is an equality of chronological sums, not an original-root charge.

## 3. Precise relation to the older A/B/C subtraction

The old homogeneous R2 family in second_R_gate_or_corridor.md used
edges arriving R2 and paired a supplier L3 with its EARLIER R2. That
is a different dependency. Our new contour's edges arrive L1 and pair
with its LATER R2. The old C-family definition is not imported unchanged.

Nevertheless the safe occurrence-subtraction argument extends directly.
Let A be chosen first-arrival cycles, B chosen first-departure cycles,
and C_new this later-R2 contour. Every A occurrence arrives R0, whereas
C_new arrives L1. Every B occurrence departs R0, whereas C_new departs
R2. Thus no actual selected occurrence is shared, even if physical
edges overlap. The canonical contour uses distinct edge occurrences.

Subtracting all these balanced selected occurrence currents from the
nonnegative physical flow is therefore valid. With a,b the A/B counts,
total lengths L_A,L_B and D=||d||_infinity,

    P>=L_A+L_B+2ell+2D*abs(1-a+b-1).

This is only the same integral-current proof with the newly verified
source/target ranks. It is NOT asserted to strengthen every pre-existing
coarse speed bound, and no overlap with the clock payments in(1) is
counted a second time.

## 4. Monotone geometry and scope

After one genuine rotation, choose the straight-face direction NW.
Each RIGHT/LEFT pair has outward directions NE then NW, and each S
has outward direction NW. Thus Gamma is globally monotone in the
vertical C-center coordinate and its actual full drift is

    d=(-s,ell).

This is a structural deduction, not a bounded drift scan. The signed
no-(RL)^3 gives s>=ceil(ell/5); the signed no-five-S rule gives S runs
at most four. Neither this monotone geometry nor(1)-(2) excludes the
remaining mixed S/RL architecture. LEFT maximum branches remain outside
these hypotheses. No complete WHITE cap-four front or finite-seed fuel
budget is constructed or claimed.

Dependencies retained unchanged:
K1_straight_cannot_precede_left.md, SHA
ec007322c863fb61411511b006607196ddb52ad0dd9719f474287ebd909269dc;
K1_leftmost_branch_free_middle_collar_v2.md, SHA
313509cb42cf3cb2ceb8a395896665aaddc58032de65b0af6a392ca963c3e466;
chronological_stream_sheet_exchange.md, SHA
fd20e425b8a6bbc3aefd5eca06b4d443c1d2bdfde5f1d2d69c25d5c4d62af484;
stream_sheet_clocks_and_bridge_sign.md, SHA
552d5aa8cc604cb3899291d688f016652fcd00ab6108e24eb44efa86ea9efe84.
