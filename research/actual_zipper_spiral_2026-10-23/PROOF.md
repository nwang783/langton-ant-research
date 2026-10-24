# Actual paired-forest spiral zippers: square-root epoch mass gain is sharp

23 October 2026. Frozen author proof for independent review. This construction
uses literal ordinary Langton dynamics on an explicitly specified finite full
board. It is not a synthetic cursor path or a final-XOR-only board.

## Claim

For every integer q>=1 there is a finite full black board of mass

    M = n = 4 floor((q+1)^2/4)

and a proper post-L entry pose whose NEXT n complete ordinary blocks form one
maximal ordinary w-bridge epoch. Its full physical trajectory has:

- n initial black cells consumed once each, no new black lifetime consumed;
- signed physical clockwise w-path turning S=q-1;
- exactly n+q-2 R updates and n L updates, hence T=2n+q-2;
- both complete black graphs forests at EVERY fine cut, so no cycle birth
  and no cycle erasure within this epoch;
- complete-board mass gain q-2 >= sqrt(M)-3;
- next complete block RRRRL, which is exceptional and has mass gain 3.

Thus the O(sqrt(M)) one-epoch mass-growth order cannot be improved uniformly
to o(sqrt(M)), even for actual erasure-free paired-forest zippers starting
immediately after an L. Likewise the O(sqrt(n)) signed-turn order cannot be
improved for this executable subclass. Constants here are not optimal.

This does NOT prove the cubic global elapsed-time bound is sharp in the
number E of renewals. That would require an actual repeatable concatenation
of growing near-extremal epochs, not merely this one-epoch family. The seed
mass here grows with q; no infinite finite-seed orbit is constructed.

## Coordinate conventions and the COMPLETE board

In the w lattice let (a,b) range over Z^2 and put its doubled physical vertex
at

    X=2a+2b+1,  Y=2a-2b+1.

A w unit edge {u,v} is the physical cell

    ((X_u+X_v)/4, (Y_u+Y_v)/4).

This is the k=0 diagonal black graph. The map (a,b)->(X,Y) reverses
orientation: a counterclockwise turn in (a,b) is clockwise physically.
The black edge in the opposite z graph at the same physical cell is the
planar dual of the w edge. In these same (a,b) coordinates the z vertices
are (Z+1/2)^2. Explicitly:

- w edge (a,b)--(a+1,b) has z dual (a+1/2,b-1/2)--(a+1/2,b+1/2);
- w edge (a,b)--(a,b+1) has z dual (a-1/2,b+1/2)--(a+1/2,b+1/2).

Let P_q start at (0,0), with q counterclockwise straight runs, directions
E,N,W,S,E,... and lengths

    4,4,8,8,12,12,..., 4 ceil(j/2) for run j.

Let v_0,...,v_n be EVERY unit-spaced vertex of this path, not just its corners.
The initial physical black board B_q consists of EXACTLY the n cells of its
n edges. Every other physical cell is initially white. No passive components,
remote caps, or earlier writes are omitted. All new writes remain in the
actual board through the epoch.

The usual square-spiral geometry gives a vertex-simple path. For clarity,
the successive run endpoints after runs 4k+1,4k+2,4k+3,4k+4 are respectively

    (4(k+1),-4k),
    (4(k+1),4(k+1)),
    (-4(k+1),4(k+1)),
    (-4(k+1),-4(k+1)),             k>=0,

with the first run starting at (0,0). The total edge count is
4 sum_(j=1)^q ceil(j/2)=4 floor((q+1)^2/4).

Two NONCONSECUTIVE closed straight-run segments have L-infinity distance
at least 4. This follows directly from the displayed endpoint formulas:
parallel nearby old sides are separated by a positive multiple of 4; a new
perpendicular side lies on the next outside extreme and its only old
intersection is the immediately preceding corner. At nonconsecutive
perpendicular sides the nearest endpoints/side points remain separated by
at least 4. Consecutive sides meet only at their common corner. Distinct
corners are at least 4 apart along either incident side. Hence radius-one
neighborhoods of nonlocal parts are disjoint, and every possible interaction
of path edges and unit outside arms is either a straight patch or one
isolated two-run corner patch.

## Physical entry, including the proper post-L condition

Start at physical p=(1,1), heading E. Its w cursor is the initial w vertex
(a,b)=(0,0), and its current cell is the first black edge of P_q. The first
update is L and crosses that edge.

This state really can be the state immediately after an L. Take the
predecessor full board B_q union {(0,1)}, physical pose p_prev=(0,1), heading
S. The additional cell is the w edge (0,-1)--(0,0) and is not in B_q. Its
literal L update deletes this cell and gives precisely B_q, p=(1,1), E.
The predecessor board is also a forest in both graphs: the extra w edge
extends the initial path, and its z dual touches at most the first-edge dual
in one endpoint. All other path portions are separated by the spacing.
Thus that predecessor L is a bridge deletion in both graphs too.

## The forced local scan and candidate word

After a w move arriving along E in (a,b), the incoming w port W has just
been deleted. At the next physical read the port is S, and successive R's
scan S,E,N,W while w stays fixed. Rotations give the corresponding statement
for every incoming direction. This is the literal Langton turn/move rule;
R inserts its current black w/z edge and moves z, while L deletes its edge
and moves w.

For a straight continuation E the correct block is RL: insert the outside
S arm and delete/cross the old E path edge. For a counterclockwise w corner
E->N the correct block is RRL: insert the outside S arm, then the forward
E arm, and delete/cross the old N path edge. All turns of P_q are of these
two types, after rotation. The initial block is just L. Therefore the
candidate word is obtained by following each successive unit path edge:
initial L, then RL at each straight internal vertex and RRL at each run
corner. We next prove these reads and bridge statuses against the full board.

## Full w-graph invariant: old suffix plus disjoint outside stars

At a completed L cut, the undeleted old edges are exactly the suffix of P_q.
The newly written edges are, at each departed internal path vertex:

- the right/outside unit arm for a straight passage;
- that right/outside arm plus the forward unit arm for an E->N corner,
  with the rotated versions at other corners.

Those arms never coincide with an old path edge. Their outer endpoints
are not vertices of the original path, and arms rooted at different path
vertices have distinct outer endpoints. The spacing statement excludes all
nonlocal contacts. In a straight patch the arms are parallel disjoint teeth.
At the normalized corner E->N at (0,0), the last incoming straight tooth
ends at (-1,-1), the two corner arms end at (0,-1),(1,0), and the first
outgoing straight tooth ends at (1,1); these are all distinct and outside
the two incident runs. The same calculation covers all nearby roots.

Consequently all previously written w components are disjoint one- or
 two-edge stars, physically retained behind the cursor. During an R prefix
only the current such star is attached at its root to the old suffix. The
actual w graph is a forest at every fine cut. Every prescribed R arm is
white; every prescribed L edge is the next old black path edge and remains
a bridge. This proves the candidate word is the actual physical word,
inductively, and proves exact old-bridge traversal without relying on a
synthetic path's realizability.

## Full z-graph invariant: one output offset chain plus old tiny paths

The duals of the original path edges form isolated edges and two-edge
paths: two consecutive duals meet only when their w edges form one of the
counterclockwise corners. Straight consecutive w edges have disjoint duals;
all other possible contacts are ruled out by spacing. Since corner patches
are separated by run lengths at least 4, no three-edge old dual component
is possible.

Let C_i be the union of the z duals of ALL R arms already written immediately
after the ith old-edge L deletion. These are never removed during this
epoch. Regard C_1 as an empty chain with a marked initial endpoint at the
right face of the first path edge. For i>=2, C_i is the right/outside
unit-grid offset chain from the right face of edge 1 to the right face of
edge i. It is geometrically simple. Straight patches extend it by one edge;
corner patches extend it by two edges. Nonlocal contacts are impossible:
all its vertices are within L-infinity distance 1/2 of an original run or
its corner, while nonconsecutive runs are separated by 4. The local corner
trace below has no self-contact. Thus C_i is a single simple path, and at
completed L cuts it is disjoint from every remaining old z-dual component.

Here is the entire normalized local calculation. The cursor has arrived
along E at w=(0,0); the current output-chain endpoint is (-1/2,-1/2).

Straight E continuation:

    R adds z edge (-1/2,-1/2)--(1/2,-1/2).
    The departing old E edge has z dual
        (1/2,-1/2)--(1/2,1/2).

The new chain touches that old component in precisely its lower endpoint.
If the old component also includes the next corner edge, it continues
through the upper endpoint, not through the output chain. The following L
deletes the displayed vertical old dual and leaves the new endpoint
(1/2,-1/2), disjoint from the remaining old duals.

Corner E->N:

    First R adds (-1/2,-1/2)--(1/2,-1/2).
    Second R adds (1/2,-1/2)--(1/2,1/2).
    The departing old N edge has z dual
        (1/2,1/2)--(-1/2,1/2).

The R prefix attaches the output chain to at most ONE endpoint of that old
component. The incoming old E edge, which could otherwise close the local
square, has already been deleted by the preceding L. The next corner is
at least four edges away. Thus no cycle is created. The following L removes
the horizontal old dual, leaving endpoint (1/2,1/2), disjoint from the old
suffix duals. Rotate these two patches for all other directions.

This proves by induction that at every fine cut the complete z graph is a
disjoint union of paths, or paths joined at the single current frontier
endpoint. In particular it is always a forest, every R is a bridge insertion
in z, and every L is a bridge deletion in z. Together with the w invariant,
there is no cycle birth or erasure in either full graph through the stated
epoch. The argument explicitly retains the entire output chain and all
remaining old duals rather than dropping inactive state.

## Exact counts, endpoint corrections, and maximality

There are q-1 run corners, each clockwise in physical w coordinates. All
other internal vertices are straight, so S=q-1. There are n L updates.
After the first block L, each of n-1 remaining blocks has one R for the
straight base count plus one extra R for each of q-1 corners. Hence

    R=n+q-2,   T=R+L=2n+q-2,
    final mass=M+R-L=M+q-2=M+S-1.

The -1 is the EXACT first-block correction, not an unspecified O(1).
There is no final R run included: the interval ends immediately after the
last old-edge L. At its arrival vertex, no old edge remains and no previous
outside arm touches it. The w cursor is isolated. Its next four reads are
white and scan all four ports; its next read is the first inserted edge,
so the next complete block is RRRRL. This is an exceptional block (it erases
the opposite unit cycle), so the displayed ordinary epoch is maximal.

Finally M is (q+1)^2 when q is odd and (q+1)^2-1 when q is even. Therefore
q-2>=sqrt(M)-3 and S=q-1>=sqrt(M)-2. This is the desired all-parameter actual
square-root lower bound.

## Controls and honest limitations

check_spiral.py builds EVERY initial black cell from the formula, executes
literal full-board physical updates, checks all intended reads and w cursor
vertices, and recomputes full-graph connectivity for every insertion and
deletion in both graphs. It checks proper post-L entry and the next RRRRL
block. controls.json contains fixed q=1,2,3,4,8,16,32 controls at spacings
1,2,3,4. Spacings 2,3,4 have no cycle births or erasures. Spacing 1 develops
cycles and erasures for longer paths, despite still following the same
physical read word, demonstrating why the spacing/complete-graph proof is
not optional. Only spacing 4 is claimed by the conservative general proof.

These finite checks audit the formula and signs; they do not substitute for
the geometric and full-graph induction above. The previously signed universal
upper-bound proof is unchanged. This result gives no repeating near-extremal
renewal mechanism and no sharpness claim for the global cubic recurrence.
