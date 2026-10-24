# A pre-funded collector keeps all outputs in one tree without any cycle events

23 October 2026. Frozen author proof for independent review. This strengthens
the executable one-epoch countercontrol; it is not a global renewal theorem.

## Result

For every q>=1 there is an explicitly specified finite complete board whose
w graph is initially ONE tree, with no passive w edge component. Its next
maximal ordinary epoch has positive gain G=q-2 (for q>=3), yet finishes with
ALL surviving black edges in ONE dormant w TREE and an isolated current w
cursor. Both full black graphs are forests at every fine cut; no cycle is
born or erased in either graph. Therefore one-epoch positive square-root
mass gain does not force output fragmentation or cycle creation.

The collector is pre-funded, physically present, and fully charged:

    n = 8 floor((q+1)^2/4)       old spiral path edges,
    K = n+4(q-1)                collector edges,
    M = n+K+3 = 2n+4q-1        ONE initial active tree,
    G = q-2 >= (1/2)sqrt(M)-4,
    T = 2n+q-2                 actual physical updates.

The epoch consumes n old edges and prunes K+3 old edges into the archive;
its final active mass is0 and final sole dormant component has M+G edges.
It creates exactly q-1 NEW marked w vertices, so with all isolated old
vertices retained, C_w(entry)=1, C_w(final)=2 and G=A_w-1. This realizes the
new-vertex term in the exact Euler bookkeeping without any cycle payments.

No repeatable concatenation, global monotone potential, or sharpness of the
cubic elapsed-time/renewal exponent follows from this one-epoch family.

## Fixed geometric/physical dependency

Use the same (a,b) w lattice, physical midpoint map, z dual convention,
initial physical pose (1,1),E, first-block L and local straight/corner
word as PROOF.md (SHA25647ca17aa70bbb2a01720ce86066bee05120fd5f9890fe05d278bc357ff4faae2),
which received an independent PASS. Replace spacing4 by spacing8. The base
input path P has q counterclockwise runs E,N,W,S,... of lengths8,8,16,16,...
Its complete physical word and output arms are exactly the same local
L/RL/RRL construction. All nonconsecutive straight runs are now separated
by at least8, so the radius-two collector modifications below cannot create
nonlocal contacts. The orientation map is reflected: these are clockwise
physical w turns.

## The complete collector path

The ordinary outside parallel collector would run one unit to the right of
each w run. Modify it at every counterclockwise corner as follows. Normalize
the incoming direction to E and the outgoing direction to N, and place the
corner at(0,0). The incoming collector line is y=-1; the outgoing collector
line is x=1. Instead of passing through the forward corner-arm tip(1,0),
route it through the following points, using EVERY unit edge:

    (0,-1), (2,-1), (2,1), (1,1),

then continue up the line x=1. Before this detour it followed the line y=-1.
Rotate this same patch for each other corner. Start the whole collector at
the first input endpoint plus the first run's right normal; end it at the
last input endpoint plus the last run's right normal. Thus it starts at
(0,-1). Every run is at least8, so patches at consecutive corners do not
overlap, and the separation of nonconsecutive runs excludes other contacts.
This is a simple w path K, disjoint in vertices from the original path P.

At a normalized corner the right arm tip(0,-1) lies on K, but the forward
arm tip(1,0) does NOT. At every straight internal root, the outside arm tip
lies on K. All missed forward corner tips are distinct, absent from both
P and K, and become genuinely new w vertices when their R arms are written.

Compared with the original parallel offset, which adds2 edges per corner,
the displayed detour adds two more. Hence |K|=n+4(q-1).

Finally attach the collector to the INITIAL input root by the three-edge
path

    (0,0), (-1,0), (-1,-1), (0,-1).

It touches P and K only at its respective endpoints, and none of its edges
is a future R arm. The complete initial black board consists of EXACTLY
P, K and these3 connector edges, interpreted as physical midpoint cells.
There are no other black cells. It is one w tree of mass M=n+K+3.

The proper post-L condition is literal: add the physical cell(0,1) to this
board and start at(0,1),S. Its L deletes this cell and produces the required
entry(1,1),E and exactly the specified board. That preceding L is allowed
to be a w nonbridge erasure (the added edge closes the short connector
cycle); it is OUTSIDE the claimed epoch. No bridge claim about this
predecessor is needed.

## Actual w dynamics and one-tree output

The base physical candidate word reads only old P edges at its L's and its
prescribed outside arms at its R's. None of the K/connector cells is one of
these read cells, so it does not change the actual word. This assertion can
also be proved inductively by the following full w-graph invariant.

After the first L, the whole collector/connector is behind, attached to the
old initial root. The unconsumed active old graph is the strict suffix of P.
At each following root:

- a straight block's R adds one arm to the single existing collector archive;
- a corner's first R does the same;
- the corner's second R adds a new LEAF at the skipped forward tip, not a
  second edge back into the collector.

Thus every R is a w bridge insertion. No arm touches any future vertex of
P, so the departing old edge is always a w bridge and its L leaves the
collector archive behind again. After that L, the exact active component
is the old path suffix. Every written edge is retained, all previous roots
are joined to the same collector, and no w cycle is created. At the end,
all black edges belong to this one archive tree; only the current endpoint
is isolated. In particular the claimed absence of fragmentation is about
the FULL output, not about discarding old inputs or passive components.

## The opposite z graph remains a forest, with all collector edges retained

The independently passed base spiral proof establishes a forest at every
fine cut for the board consisting only of P and its prescribed R arms.
Let V_base be the union of the z vertices of ALL base P edges and ALL its
prescribed R arms, including those edges not yet present at a given cut.
Adding the fixed collector/connector cannot create a z cycle if each of
its dual components is a tree and meets V_base in at most ONE vertex.
This condition is enough at every cut, not merely at the endpoint.

Here is the full local verification. Away from collector corners its dual
components are isolated edges with one endpoint on the potential base
offset chain and the other outward. At each normalized detour corner,
there are, in addition to such single edges, exactly:

A two-edge component

    (3/2,-3/2)--(3/2,-1/2)--(5/2,-1/2),

which meets V_base in NO vertex; and a three-edge component

    (5/2,1/2)--(3/2,1/2)--(3/2,3/2)--(1/2,3/2),

which meets V_base only at(1/2,3/2), the outside face of the first outgoing
straight input edge. The corner's first incoming collector edge has dual
(1/2,-3/2)--(1/2,-1/2), a single edge meeting the base only at the intermediate
corner-output vertex(1/2,-1/2). Rotate these coordinates at other corners.
All remaining single dual edges have the same one-contact property.

The3 connector duals form a star centered at(-1/2,-1/2), with other vertices
(-1/2,1/2),(-3/2,-1/2),(-1/2,-3/2). This star is disjoint from both V_base
and the collector duals. Nonlocal contacts are excluded by spacing8 and
the fact that every modification lies within distance2 of its own corner.
Thus all fixed collector/connector dual components are disjoint trees,
each with at most one contact with the base vertex union. Adding them to
the full base forest at any time preserves a forest. This proves that
every actual R is also a z bridge insertion and every L is a z bridge
deletion. No z births or erasures are hidden by the construction.

For an optional count check, the collector dual components consist of
n-q+1 single edges with one base contact, q-1 two-edge paths with zero
contacts, and q-1 three-edge paths with one contact. Their total edges are
n-q+1+2(q-1)+3(q-1)=n+4(q-1), as required.

## Exact counts and resource cost

The physical word is unchanged from the base spiral: n L's and n+q-2 R's.
The initial first block contributes -1 and the signed internal turn is q-1,
so G=q-2 exactly. The whole initial input is one connected w tree of mass
M=2n+4q-1, not merely the n-edge live path. The collector is never consumed.
The final retained tree has M+G edges and the current cursor is isolated.
The next block is RRRRL, so this ordinary epoch is maximal.

All R roots are initial P vertices. All straight/corner-first-arm tips are
initial K vertices. Each of the q-1 second corner-arm tips is new and distinct.
Hence A_w=q-1, while B_w=D_w=B_z=D_z=0. Retaining all marked vertices leaves
one final archive tree plus the isolated input endpoint, so Delta C_w=1
and G=A_w-Delta C_w=q-2. The initial active old-fuel loss is M=n+(K+3),
consisting of n consumed edges and K+3 pruned but retained archive edges.

As q varies, M is at most(2q+3)^2, so G=q-2>=(1/2)sqrt(M)-7/2 and certainly
G>=(1/2)sqrt(M)-4. Thus even these consolidated paired-forest epochs have
square-root gain in their FULL charged entry mass.

## Controls and boundaries

check_detoured_collector.py and its exact imported helper check_collector.py
construct the finite full boards and use literal physical updates with full
graph connectivity checks at every update. Both entry passive and entry
connected variants are checked, with the full collector mass charged, all
active-component changes and cycle events retained, and the marked-vertex
Euler identity checked. The q8 connected control has M351, n160, G6,
final archive357, A_w7, both initial/final ranks0 and no cycle events.

These controls do not replace the all-parameter local geometry proof.
Independent review is requested. Nothing here bounds future reuse of this
archive, assumes a stack order, or establishes a sharp global renewal law.
