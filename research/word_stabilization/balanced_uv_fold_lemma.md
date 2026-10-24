# Balanced mixed U/V returns cannot continue

For any words X,Y over {U,V} having the same numbers of U and V, any folds
A,F in {B,Q}, and any macro D in {C,U,V,Q,B}, the word

    A X F Y D

is physically infeasible on every initial coloring. Except in the case
(A,F)=(B,Q), the shorter prefix A X F Y is already infeasible. No equality
of the order of the letters of X and Y is assumed.

This is an exact all-parameter read-alternation proof. The finite footprint
facts and finite regression controls are in `verify_balanced_uv_fold_lemma.py`.
The controls are not the proof. All phases are zero-based; initial pose is
(0,0), north. The claim is stronger than a symbolic-language restriction.

## Finite facts and coordinates

U translates the physical head by (0,4), V by (1,3), with no heading change.
Both footprints have x >= -1. Their maximum y values are respectively 4 and 3.
The following local reads are unique:

- U at (-1,3): phase22 R; U at (0,4): phase24 R.
- V at (0,2): phase12 R; V at (1,3): phase14 R.
- U never reads (-1,4), and V never reads (0,3).

Both folds last read (-1,-1) at phase46 R. Q last reads (-1,1) at phase30 R;
B last reads (0,-1) at phase3 L. The fold endpoints are B=(-3,-5,S) and
Q=(-4,-4,S). Their minimum y coordinates are -5 and -4. Q omits (-3,-4).
BB,QQ,QB already have equal consecutive reads. Every macro's first read at
(-1,0) is phase1 L.

Let u and v be the common U and V counts. Write

    s=(v,3v+4u).

For a prefix of the return run Y, let (a,b) be the numbers of V,U still to
be executed. These are always nonnegative, and their remaining displacement
is (a,3a+4b). Before any block other than the last, a+b >= 2. Consequently
3a+4b >= 6 there. This simple bound does not depend on letter order.

Write A=B for e=0 and A=Q for e=1, and F=B for f=0 and F=Q for f=1.
The middle fold starts at (-3-e,-5+e)-s, facing south. The return run starts
at (d,-d)-s, facing north, where d=f-e, and ends at (d,-d).

## Equal folds: (A,F)=(B,B) or (Q,Q)

Take q=(-1,-1), whose last initial-fold read is R at phase46. The outward
run cannot reach it: its south-facing local x would be -2-e-v_prefix < -1.
For nonempty X, the middle fold's local coordinates at q are

    (-2-e-v,-4+e-3v-4u),

below the middle fold's minimum y. If X is empty, BB/QQ already fail.

At a return boundary the local coordinate of q is

    (a-1,3a+4b-1).

Before the last block, its y coordinate is at least5, above either footprint.
In the last block it is (-1,3) for U or (0,2) for V, so its first return read
is U22 R or V12 R. This is consecutive to the initial fold's last R at q.

## (A,F)=(Q,B)

Take q=(-1,1), whose last initial Q read is phase30 R. The outward local x
is -3-v_prefix, so q is missed. For nonempty X, the middle B would need

    (-3-v,-5-3v-4u),

below its footprint. For empty X, QB already fails.

At a return boundary q has local coordinate (a,3a+4b). Before the last block
its y is at least6. The last U/V first reaches it at U24 R or V14 R, again
consecutive to the old R. Thus the prefix through Y already fails.

## (A,F)=(B,Q)

Take q=(0,-1), whose last initial B read is phase3 L. The outward local x
is -3-v_prefix, so q is missed. The middle Q would need

    (-3-v,-4-3v-4u).

For nonempty X this is below its footprint; for empty X it is the absent
point (-3,-4). At a return boundary the local coordinate of q is

    (a-1,3a+4b).

Before the last block its y is at least6. In the last U/V it is respectively
(-1,4) or (0,3), both absent. Therefore all of Y misses q. At its endpoint
(1,-1), the next macro D first reads q at local(-1,0), phase1 L. That read
is consecutive to the initial B3 L, a contradiction. This also covers empty
X,Y directly.

## Prefix and tail corollaries

The equality need only hold for X and a prefix Y0 of Y. In an infinite
physically feasible macro stream, a return run following two folds can never
reach exactly the same U/V count vector as the outward run. In the B...Q
case the balanced return may terminate the entire finite word, but no next
macro can follow it.

This does not prohibit arbitrary mixed three-fold words. For example
QUUUUQVVVQ is physically feasible from a 75-black-cell seed. Nor does the
lemma establish V-tip freshness, exclude all C-free tails, or prove highway
attraction. It is an additional exact obstruction to spatial returns.

## A sharp limitation: dominating return counts are possible

The condition of exactly equal U/V counts cannot be replaced by componentwise
dominance of the return counts. For every integer n >= 3, the word

    Q U^n Q V^4 U^n Q

is physically feasible. Its minimal entry fuel is exactly 10n+57, its length
is 56n+264 turns, and its endpoint is (0,8,S) in the initial north-facing frame.
Thus the return run has the same U count and four additional V blocks.

The all-parameter certificate is in
`../audits/certify_quqv4uq_family.py` and
`../audits/quqv4uq_family_certificate.json`. It partitions each physical column
and y-residue mod 4 into affine slabs. Beyond n=4, endpoint order is stable;
every complete read list on every slab alternates, and the first-L slab lengths
sum to 10n+57. The exceptional n=0,1,2,3 are checked literally. Independent
review verified the endpoint-order and chronological-index arguments. This
is not an infinite finite-support trajectory and does not refute V freshness.
