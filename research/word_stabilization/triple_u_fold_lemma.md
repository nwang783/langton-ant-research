# Three folds separated only by U are impossible

## Statement

For all A, F, D in {B,Q} and all integers n,m >= 0, the turn word

    A U^n F U^m D

is not physically realizable on any initial coloring. Consequently, an infinite
physically realizable five-macro word with finitely many V blocks eventually
consists only of U blocks. On a finite-support board this is impossible.

This is a realizability lemma, not just a necessary local-language condition.
All phases below are zero-based and all coordinates are physical cells. The
initial head is (0,0), north. Right turns are clockwise.

## Footprint facts

The literal words and the finite facts used below are checked by
`verify_triple_u_fold_lemma.py`. Let A=B for e=0 and A=Q for e=1; likewise let
F=B for f=0 and F=Q for f=1, and put d=f-e.

- U ends at (0,4), still north.
- A ends at (-3-e,-5+e), facing south.
- The head after A U^n F is (d,-d-4n), facing north.
- U has x-coordinate range [-1,2]. Its reads on the line x=-1 are exactly
  phase1 at y=0 (L), phase2 at y=-1 (L), phase14 at y=1 (L), phases13
  (L) and21 (R) at y=2, and phase22 at y=3 (R). Its sole read at (0,4) is phase24 (R).
- The last read of (-1,-1) in either fold is phase46 (R).
- The last read of (-1,1) in Q is phase30 (R).
- The last read of (0,-1) in B is phase3 (L).
- The last read of (-2,-3) in B is phase67 (R); that of (-3,-2) in Q is
  phase57 (R).
- Both folds first read (-2,1) at phase15 (R), and first read (-3,1) at
  phase18 (L).
- The minimum y-coordinate in B is -5; in Q it is -4. On the line x=-1,
  both have minimum y=-1. Q never reads (-3,-4).

A north-facing U occurrence with local phase coordinate (u_x,u_y) reads
that coordinate translated by its head. A south-facing occurrence reads
the negative local coordinate translated by its head.

## Case 1: m<n and the middle fold F=B

Set k=n-m>=1 and q=(-2-e,1+e-4k). The last fold D first reads q at phase15,
with R.

In the outward U run, reading q requires the local coordinate (-1,2), hence
zero-based occurrence index j=k-2. If k>=2, this occurrence exists because
0<=k-2<n, and its last read at q is phase21, also R. The initial fold cannot
reach q, since q lies below its minimum y-coordinate.

If k=1 there is no such U occurrence; instead q is (-2,-3) in B or (-3,-2)
in Q, whose last initial-fold read is R at phase67 or phase57 respectively.

The middle B could read q only at local coordinate (-1,-6-4m), which is
outside its footprint. The return U run would need local x=-2, also
impossible. Therefore the identified R and final phase15 R are consecutive
reads of q, a contradiction.

## Case 2: m<n and the middle fold F=Q

Set k=n-m>=1 and q=(-2-e,e-4k). The last fold D first reads q at phase18,
with L.

In the outward U run the only possible reads occur at local (-1,3) in
occurrence j=k-2, when that index is nonnegative, and at local (-1,-1) in
occurrence j=k-1. The latter always exists because 0<=k-1<n, and is phase2,
with L. It is the last outward-run read of q.

The middle Q could read q only at local (-1,-5-4m), which is outside its
footprint. The return U run would need local x=-3. Thus the outward phase2 L
and final phase18 L are consecutive reads of q, again a contradiction.

## Case 3: m>=n and (A,F)=(B,B) or (Q,Q)

First take n>=1. Let q=(-1,-1). The initial fold's last read is phase46 R.
The outward U run cannot reach q by its x-coordinate. The middle fold could
reach q only below its minimum y-coordinate. In the return U run the first
read of q is occurrence j=n-1 at local (-1,3), phase22 R. That occurrence
exists since m>=n. These consecutive R reads conflict.

For n=0 the finite words BB and QQ already fail: the second-fold reads
B68 R or Q58 R at q immediately follow the first-fold phase46 R.

## Case 4: m>=n and (A,F)=(Q,B)

For n>=1 take q=(-1,1). The initial Q's last read is phase30 R. Neither the
outward U run nor the middle fold can reach q, by the same coordinate
bounds. The return run first reaches it at occurrence j=n-1, local (0,4),
phase24 R. This is a consecutive R/R conflict. For n=0, QB already fails
at the second fold's phase70 R after the initial Q phase30 R.

## Case 5: m>=n and (A,F)=(B,Q)

Take q=(0,-1). The initial B's last read is phase3 L. The outward U run
cannot reach q. The middle Q would require local (-3,-4-4n); this is absent
for n=0 and below its footprint for n>=1. The first n U blocks of the
return run cannot reach q: they would require local x=-1 and y>=4.

If m>n, occurrence j=n reads q at local (-1,0), phase1 L. If m=n, the next
macro D reads q at that same local coordinate and phase, since all macros
begin with the common marker. In either case these are consecutive L reads.
This exhausts all eight choices of the folds and all n,m>=0.

## Consequence for finite-support tails

The exact short-gap grammar says that after a non-C block every positive C
run must be followed by V, if another non-C block follows. Therefore an
infinite five-macro word with finitely many V blocks has a suffix over
{U,Q,B}. Three Q/B blocks in that suffix would give the forbidden pattern
proved above; hence the suffix eventually consists only of U.

The cell (0,3) in U is first read L at phase23. In U occurrence j it is
(0,4j+3), strictly above every cell read by previous U occurrences, whose
maximum y-coordinate is 4j. Thus every U in that suffix consumes a distinct
black cell present at suffix entry. A board with finite black support cannot
sustain U forever. (The sharper exact U/V fuel formula gives 4+5r distinct
first-L cells in U^r, but is not needed here.) Thus any infinite finite-support
five-macro tail must contain infinitely many V blocks.

In particular, proving freshness of the V tip (1,2) in all actual five-macro
H tails would by itself rule out those tails. Freshness of U, Q, or B is not
needed for that sufficient route. This does not yet prove V freshness.

## Quantitative V-free corollary

Let a physically realizable V-free interval start from a board with m black
cells. Its non-C part is of the form

    U^r0 F1 U^r1 F2 U^r2,

with zero, one, or two folds; unused runs may be set to zero. There is at most
one leading C when a non-C follows, and at most three trailing C blocks.
If there are no non-C blocks, C^5 is impossible and the result is immediate.
There are no other C blocks by the exact gap grammar.

A run U^r needs at least 5r+4 entry-time black cells when r>0. Here is a
literal footprint proof: the first U has nine first-L cells. For every later
north-oriented U, the five local cells (-1,0),(-1,1),(-1,2),(0,2),(0,3) are
first read L and are above all previously visited cells in their respective
columns. Every other first-L cell in that U was already visited by its immediate
predecessor. Thus the exact number is 9+5(r-1). Rotation does not change it.

The net black-cell changes of C,U,Q,B are respectively 3,4,6,6. Therefore,
writing s1=r0+r1 and s2=r0+r1+r2, we have the safe inequalities

    r0 <= m/5,
    5 r1 <= m+5+4 r0,
    5 r2 <= m+11+4 s1.

These also hold for empty runs. The constants allow the one leading C and
one or two preceding folds, and drop the -4 required by the U-run fuel bound
only where convenient. Substitution gives

    s1 <= 14m/25 + 1,
    s2 <= 151m/125 + 4.

There are at most six non-U blocks (two folds and four C blocks). Hence the
total number of macros is at most

    floor(151m/125 + 10) <= 2m+10.

In particular this is a finite-fuel theorem for the entire alphabet {C,U,Q,B},
not merely an asymptotic exclusion of its infinite tails. It does not bound
intervals containing V blocks.
