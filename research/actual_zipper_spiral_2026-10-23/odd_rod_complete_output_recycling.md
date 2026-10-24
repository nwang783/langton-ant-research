# Complete first-epoch R-output recycling after one actual reset

23 October 2026. Frozen all-r author theorem for independent review.
The LRRL rod transport is already retained; the new control here is exact
ordinary-epoch ownership: ALL fuel of the second large epoch was R-born in
the first, with the original seed, turnaround writes and both graphs retained.

## Statement

For every r>=1, prepare EXACTLY the finite black board

    B_0 = {(x,0): 0<=x<=2r},

of mass2r+1, head(0,0),E. The literal physical word is

    (LRRL)^r L  |  RRRRL  |  (LRRL)^r.

The first and third pieces are maximal ordinary w-bridge epochs. The middle
piece is one exceptional block: one z cycle birth and its immediately
following erasure, but no w cycle event. Both full graphs are forests at
every fine cut of both ordinary epochs, and again after the reset.

The FIRST epoch consumes all2r+1 initial black lifetimes and writes exactly
2r new black lifetimes on row y1. NONE is consumed during that epoch or the
reset. The SECOND ordinary epoch consumes ALL2r of those first-epoch R-born
lifetimes and NO initial or reset lifetimes. Thus100% of its old bridge fuel
was produced in the immediately preceding ordinary epoch. There is no
pre-funded second branch, collector, return rail or omitted background.

Exact counts:

    first:  T=4r+1, L=2r+1, R=2r, gain=-1;
    reset:  T=5,    L=1,    R=4,  gain=3;
    second: T=4r,   L=2r,   R=2r, gain=0.

Total time8r+6, final mass2r+3. This rules out a universal chronology claim
that a long next epoch must use mostly fuel older than the preceding epoch.
It does NOT give positive square-root gain plus recycling, a repeatable
growing loop, or a sharp cubic lower construction. Both large transports
here are mass-neutral up to the single terminal -1.

## Exact complete states and proper entry

Use heading indices N,E,S,W as0,1,2,3. The initial state is literally a
proper post-L state: add physical cell(-1,0) to B_0, start at(-1,0),S, and
perform L. This deletes only that cell and gives precisely B_0,(0,0),E.
The predecessor board is a row and both graphs are forests.

The first4r updates are the already retained LRRL rod transport. Its block i
(i=0,...,r-1) reads

    (2i,0)L, (2i,1)R, (2i+1,1)R, (2i+1,0)L.

The extra initial cell(2r,0) is untouched until the following terminal L.
Therefore the first epoch ends after4r+1 updates with EXACT state

    B_1 = {(x,1): 0<=x<2r},
    head(2r,1),N.

The current w cursor is isolated, so the next block is RRRRL. Its four R
reads are

    (2r,1), (2r+1,1), (2r+1,0), (2r,0),

and its L deletes the first of these. Hence its exact output is

    B_2 = B_1 union C_r,
    C_r = {(2r+1,1),(2r+1,0),(2r,0)},
    head(2r-1,1),W.

The three turnaround cells are retained, not cropped away. Unlike the even
rod's lower first reset, they do NOT dirty the second transport's read region
x<=2r-1, y0/1. The odd terminal cell is what makes this turnaround work.

Now the180-degree rotated LRRL transport moves left. Block j reads

    (2r-1-2j,1)L, (2r-1-2j,0)R,
    (2r-2-2j,0)R, (2r-2-2j,1)L,

j=0,...,r-1. Thus the second epoch ends with EXACT complete state

    B_3 = {(x,0):0<=x<2r} union C_r,
    head(-1,1),W.

Every C_r cell survives unchanged. No additional seed was introduced. Its
arrival w cursor is isolated, so the second epoch is maximal too.

## Full paired-graph bridge/cycle proof

The retained all-r rod argument is in
../global_cycle_birth_2026-10-23/cycle_birth_or_finite_fuel.md, Section4,
SHA2567bd38a60ed9d0f104d44503a4ac1de09ab5d6afd89069f3203483da1393f8c42.
At every fine cut of a transport the physical black set consists of two
row intervals with an ordered frontier. In either diagonal graph each row
is a zigzag path, and the two row pieces have at most one common vertex.
Their union is a forest. The same proof includes the extra terminal cell
in the first epoch and rotates180 degrees for the second transport.

For the reset, use doubled physical w coordinates. Its stationary w cursor
is v=(4r+1,1). The first R joins it to the right output-row endpoint
(4r-1,3); its other three arms meet fresh vertices, and none has another
contact with the output-row w graph. Thus all four R insertions are w
bridges, and the following L removes the sole output attachment and crosses
into B_1. The remaining3-edge star C_r is left behind. Active w mass becomes
exactly2r, not the full mass2r+3.

In z the four arms are a four-edge unit cycle. Its vertices are

    (4r-1,1), (4r+1,-1), (4r+3,1), (4r+1,3).

Only(4r-1,1) meets the old output-row z graph. Its fourth R is therefore the
only z cycle birth; the L deletes the first cycle edge and erases it.
Afterward C_r is a3-edge z path attached at that single old endpoint.

During the second rod transport, all black row w vertices have X<=4r-1.
The fixed C_r w star has its sole possible contact with them at
(4r-1,-1), the new lower-row right endpoint; it has no contact with the
unconsumed upper row. Its attachment is on the departed side and cannot
bypass a departing bridge. All other C_r w vertices have X>=4r+1.
Likewise the C_r z path has its sole possible contact with the moving
row graphs at(4r-1,1); all its other z vertices have X>=4r+1. Thus in each
graph it attaches a tree at at most one vertex to the two-row forest, or
is disjoint. It never creates a cycle. Every ordinary L is a bridge in both
COMPLETE graphs, with all three turnaround cells retained throughout.

## Exact lifetime pairing

Number actual updates globally from1. First-epoch births at cells
(2i,1),(2i+1,1) occur at times4i+2,4i+3, respectively. The second epoch
starts after update4r+6 and deletes the upper-row cells in descending x.
For second block j, put i=r-1-j. Then:

    odd cell(2i+1,1): birth4i+3, death4r+4j+7, age8j+8;
    even cell(2i,1):  birth4i+2, death4r+4j+10, age8j+12.

These are all2r first-R lifetimes exactly once, with ages ranging from8 to
8r+4. The reset consumes only its own first R lifetime. No reset lifetime
or original-seed lifetime is counted as recycled first output.

## Frozen controls and limits

check_odd_rod_recycling.py performs literal full-board updates, retains
birth labels, verifies every ordinary bridge and BOTH graph event types,
checks all complete states, proper entry and the displayed birth/death
pairing. Fixed r1,2,3,10,30,100 controls all pass.
Checker SHA25637f3b5bc48b17418253446b8b68aa7c0e5070e5b47859508068716ad8560287c.
Output odd_rod_recycling_controls.json
SHA256e33beccea329d555423f2c158086a1c9c9b7b09eb20e8dc39cf89468c902b4ac.

Independent review is requested. The proof is all-r; finite controls check
its literal details and ownership but are not the general argument.
The remaining unproved target is positive-gain regeneration with substantial
output recycling, not the already demonstrated possibility of recycling.
