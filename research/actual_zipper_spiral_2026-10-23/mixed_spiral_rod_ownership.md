# Positive spiral gain with a recycled carrying rod: exact ownership boundary

23 October 2026. Frozen author construction/control for independent review.
The gaining and carrying portions are kept separate. This is not gain-bearing
regeneration, even though first gain is square-root sized and the next long
epoch's input is100% first-epoch R output.

## Exact complete-board construction

Take the independently passed spacing-four outward square spiral of PROOF.md
with q runs, n=4 floor((q+1)^2/4) input edges, physical initial pose(1,1),E.
Run its prescribed word on a copy to determine its terminal physical pose
(p_*,h_*). Now include, at the ORIGINAL entry, the additional ODD physical rod

    {p_* + j d_(h_*): 0<=j<=2n}.

Here d_h is the physical unit heading vector. This rod is disjoint from the
spiral seed and points outward from its terminal extreme. No second old-side
branch, collector, cap or extra return wire is added. The complete entry
board has exactly

    M = n+(2n+1) = 3n+1

black cells and is one initial w tree. Every seed cell is consumed in the
first ordinary epoch. The full previous seed and all new fields are retained.

The first word is the spiral word followed by (LRRL)^n L. Its counts are

    L1=3n+1, R1=3n+q-2, T1=6n+q-1, G1=q-3.

Thus for q>=4 its gain is positive, with

    G1 >= sqrt((M-1)/3)-4.

The current w is isolated, and the next block is RRRRL. The subsequent
ordinary word is exactly (LRRL)^n L, with

    L2=2n+1, R2=2n, T2=4n+1, G2=-1.

It consumes ALL2n rod-R lifetimes and EXACTLY ONE spiral-R lifetime (the
last straight tooth). It consumes no initial, reset or same-epoch lifetimes.
Hence100% of its old bridge fuel was written by the first epoch, and its
length is a positive fraction of the full charged mass. About2/3 of all
first output is recycled. The intervening reset has gain3 and is z-only
cycle birth/erasure in the fixed controls.

## Separation and local routing

Normalize the spiral's final directed w run to E, translate its endpoint to
v=(0,0), and use the reflected (a,b) lattice. Its last straight root is
u=(-1,0), which writes one S tooth to t=(-1,-1). The appended physical odd
rod's old w path starts S,E,S,E,...,S from v, always advancing outward in
nonnegative a. All earlier spiral portions, except the just-departed final
run, are separated by spacing4. Therefore no earlier spiral R arm touches
the future rod old path. The only output contact between the rod and the
spiral is at t, the tip of u's final tooth.

At rod block j its r2 root is(j,-j-1), writing W to(j-1,-j-1) and S to
(j,-j-2). These2n R edges form one connected staircase output path, with
initial endpoint t. They join the last spiral tooth at t but no other
spiral output star. After the terminal odd L, its endpoint is isolated and
the same exact R4 turnaround as the odd-rod recycling theorem applies.
The reset enters the output component of mass2n+1, not the full board.

The rotated rod transport then consumes the staircase output backward. At
its left endpoint, the last spiral tooth u--t supplies ONE additional L.
After that extra L, u is isolated: all neighboring original spiral input
edges have been deleted, and the other spaced output stars do not touch u.
Thus the second ordinary epoch is maximal. It cannot consume another
spiral output edge before the next exceptional block.

This gives an all-parameter local w-routing/ownership argument, conditional
only on the separately passed spacing-four spiral and all-r rod rules.
The full paired-event assertions are directly checked in the fixed controls;
a separate independent audit of this mixed local join has not yet passed.

## Exact gaining/carrying decomposition

First-epoch spiral output has n+q-2 edges. Of these:

- ONE last straight tooth joins the carrying rod's output and is consumed
  at the very end of the second epoch;
- the other n+q-3 remain in disjoint one/two-edge w stars throughout the
  second epoch, with their complete lifetimes unchanged.

The rod output has exactly2n edges, all consumed in the second epoch. The
second epoch writes2n replacements, while all3 reset edges survive. Thus its
final complete board consists of:

    n+q-3 untouched spiral outputs,
    2n second-epoch rod replacements,
    3 reset edges,

total3n+q. The seed mass, first gain and all dormant output are included.
No input source was treated as free or forgotten.

This is a structural obstruction for THIS exact family's immediate next
epoch: all but one edge of the gain-bearing spiral output is stranded.
It is not an all-future statement and not a universal no-regeneration law.
Adding more mass-neutral carry cannot answer whether the spiral output
itself can feed a long POSITIVELY growing next epoch.

## Fixed full-board controls

q=1,2,3,4,8,16 controls build every original seed cell, execute all literal
updates, classify full-graph births/erasures and ordinary bridge deletions,
and retain initial/spiral-R/rod-R/reset-R/second-R lifetime ownership.
The second epoch is followed until its actual next exceptional block, using
the proved first-exception bound3M+5, not an arbitrary horizon.

At q16, n288, initial M865; first T1743/G13, then one5-update reset; second
577 old bridges/G-1 consumes576 rod-R and1 spiral-R, no other ownership.
Both ordinary epochs have no cycle events in either full graph. The unconsumed
301 spiral-R edges remain physically present. This is not a regenerative loop.

check_positive_spiral_rod_recycling.py and
positive_spiral_rod_recycling_controls.json contain the exact control data.
Existing axial_domino_transport.md, stateful_growth_application README and
stateful_growth_quadratic README were checked before this continuation;
the known rod/cap traces are not claimed new. The new information is the
ordinary-epoch decomposition and explicit ownership with square-root gain.
