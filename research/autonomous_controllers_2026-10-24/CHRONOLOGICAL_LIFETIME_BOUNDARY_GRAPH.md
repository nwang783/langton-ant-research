# A chronological lifetime boundary graph for complete translating fronts

24 October 2026. Author all-cap construction and proof for independent review.
This is a nonadditive boundary-pairing state, not a classification theorem or
a claim of priority relative to literature. The retained chronological Whitney
identity is not being rediscovered as a new invariant here.

## 1. Scope and why this is a different question

Use exact R on WHITE, L on BLACK, flip, move. Assume a complete alternating
translating read front with full period P and full drift d=(a,b), both a and b
nonzero. Every physical read cell has a finite complete history. For a finite-
seed autonomous periodic tail, the retained stable-class argument makes every
such history start R. Prepared waves may instead have BLACK-first histories;
these will be kept explicitly, not treated as autonomous fronts.

The earlier paid201 obstruction does not give height escalation. It ties a
fixed fragment at T29 to the actual maximum34. Moving that maximum changes
the upper ports and does not force a translated copy of the fragment. No
self-replicating obligation has been established. The construction below
instead retains how actual BLACK lifetimes connect the output boundary.

## 2. Exact event definition and full voltages

Let sigma be the actual one-step event cycle. Pair each actual R read with
the NEXT L read at the SAME physical cell. Call this partial involution alpha.
Its unpaired reads are exactly the first L of a BLACK-input cell and the last
R of a permanent-output cell. All other reads are paired. Let I and O denote
those typed endpoint sets. A BLACK-first even history can contribute BOTH
an I and an O endpoint, which must remain distinct.

Make a second matching beta=sigma alpha sigma^{-1}. The multigraph consisting
of the alpha and beta edges has degree at most two. Parallel edges remain
distinct, so a two-vertex internal cycle is not suppressed. Its components
are paths, isolated vertices with two missing half-edges, or alternating
cycles. A missing alpha half-edge is an I/O event itself; a missing beta
half-edge is the successor of an I/O event.

Full-period seams are essential. If q_i=r+k_i d and alpha pairs phase i to j,
the alpha edge from i to j has voltage k_i-k_j. The beta edge from sigma(i)
to sigma(j) has voltage

    k_i-k_j + 1[j=P-1] - 1[i=P-1].

This is conjugacy under the ACTUAL event cycle, not a physical ant splice.
No arbitrary visit cap or phase-order substitution occurs.

## 3. Space-time interpretation and planarity

For a fixed physical horizontal row, draw a point (x,t) for each actual read
on that row. Draw a vertical segment for every BLACK lifetime from its R
birth to its next L consumption. A first-L BLACK input gives a ray to time
minus infinity; a last-R permanent output gives a ray to plus infinity.
A BLACK cell never read by the ant gives a full vertical line and must be
retained when the supplied prepared background contains it.

Draw every actual HORIZONTAL ant move on that row as the slanted unit segment
from (x,t) to (x+/-1,t+1). Every read has exactly one horizontal move incident
to it: either its incoming or outgoing move, because the ant turns90 degrees.
Thus each nonboundary read has degree two in this lifetime/move graph.

This is an EMBEDDED graph in the (x,t) plane. Distinct BLACK lifetimes on a
cell have disjoint time interiors. A unit move has no integer-x point in its
interior, so it cannot cross another lifetime segment. Different actual moves
have disjoint open time intervals, and consecutive moves cannot both be
horizontal. Consequently no two move edges cross either. The only contacts
are the intended common read endpoints.

Because b is nonzero, a fixed row has only finitely many reads in the full
bi-infinite translating trace. Indeed the read footprint per period is finite
and translation changes the row by b. Therefore each component is a finite
Jordan loop, or a simple arc between the indicated input/output rays. The
boundary pairing is noncrossing in the rectangle order

    input rays from left to right, then output rays from right to left.

The same proof in (y,t) holds for each physical vertical column because a is
nonzero. Unread BLACK cells supply explicit passive input-to-output strands
in both descriptions; paths cannot silently cross them.

Compressing a V-arrival cell's lifetime together with its two incident
horizontal moves produces precisely a beta edge on H-arrival events.
The alpha edges are the H-arrival lifetimes. Thus the horizontal components
of alpha union beta are exactly this embedded row graph with subdivisions
removed. The vertical components are the analogous column graph. This
interpretation proves the noncrossing assertion for the exact event matching,
not merely for a numerical drawing.

## 4. Finite boundary graph, with internal traffic retained

Map each path's missing beta half-edge back to its owner I/O event via
sigma^{-1}; a missing alpha half-edge already names that owner. Each I/O
owner has one horizontal endpoint and one vertical endpoint. Hence the path
components define a finite degree-two multigraph on the I/O endpoint orbits,
with one H edge and one V edge incident to every vertex. An H edge joins two
physical roots on the SAME row, and a V edge joins roots on the SAME column.
Use the path's full voltage to identify their physical representatives.

For a complete WHITE front I is empty. The resulting graph has exactly

    g=|O| vertices and g pairing edges,

independently of total period, width or visit multiplicity. It is a union
of alternating H/V cycles. The horizontal and vertical pairings are each
noncrossing along every corresponding physical fibre. There is no self-edge
at a single output orbit when both drift coordinates are nonzero: two
translates of one root cannot lie on the same row or column unless they are
the same physical point, which cannot supply two distinct endpoints of that
one fibre graph. Parallel H/V edges between different roots remain allowed.

Internal alpha/beta cycles are NOT deleted physically or asserted harmless.
Each lies on one spatial fibre. Its total full-drift voltage must be zero,
since a nonzero multiple of d cannot stay on that row or column. Its spatial
projection and lifetime span may still be complicated. These cycles retain
unresolved traffic which a candidate controller must actually realize.

There is a useful but weak mod-two homology check. Every actual ant step
appears once among the horizontal and vertical move graphs. BLACK lifetime
segments have zero spatial projection. After projecting the boundary paths
and internal cycles to the spatial cylinder, the latter have zero winding.
Thus the unoriented boundary-cycle windings satisfy

    sum of windings = 1 modulo2.

Changing a cycle's orientation changes its sign, not this parity. An integer
sum with fixed sign, unit winding for each cycle, a single boundary component,
or absence of contractible output cycles is NOT proved.

Changing the cyclic phase cut or applying a genuine rotation only relabels
the construction and changes voltage gauges. Replacing the full period by a
multiple gives its corresponding covering graph; do not divide the drift to
its primitive direction while keeping the same event inventory.

## 5. Tests on the actual standard word and complete supplied waves

The checker uses full stable physical ordering, not raw phase order.

- Standard104 has no input roots and12 output roots. It has12 boundary paths
  forming one12-root cycle of absolute winding1. There are FIVE internal
  lifetime components: one14-event cycle and four two-event cycles. Therefore
  an acyclicity or 'no unresolved internal traffic' shortcut is already false
  for the genuine standard controller. Genuine phase14/37/71 controls and
  full208/312 period covers give the corresponding exact graphs.
- Supplied1564 has197 BLACK-input roots and301 output roots,498 boundary paths,
  and26 internal cycles. Its boundary graph has nine cycles. The one essential
  component has366 roots; other components have zero winding. Two zero-winding
  components have only output endpoints, of sizes4 and6. They are not autonomous
  subcontrollers.
- Supplied4352 has406 input roots and590 output roots,996 boundary paths and123
  internal cycles. Its boundary graph has16 cycles, including a606-root
  essential component and several zero-winding pure-output components.

The prepared fields are retained in full. For1564 the full bulk has420 BLACK
classes, its full output524 and223 untouched BLACK classes; the finite XOR
cap has2 cells. For4352 those counts are468,652,62 and68. Every untouched
class is included as a passive input-to-output strand in the fibre planarity
checks. The exact normal forms, poses, full class sets and finite caps are in
the certificate. They are infinite prepared backgrounds, NOT finite-seed
regenerative controllers. Their positive net output104/184 does not remove
those input obligations.

The checker verifies all noncrossing pairings for the2+2 standard fibres,
14+14 first-wave fibres and26+26 second-wave fibres, including every passive
BLACK strand. The standard finite-seed realization and the literal wave
replays remain the separately retained signed controls; this new graph does
not replace their full-field verification.

## 6. A finite boundary-type target for the live g8 family

For the signed full(3,1) middle-short odd set

    O={0,1,2,6,7,6c+1,6a+2,6a+4},   3<=c<=a,

each horizontal row contains all eight output classes, in this fixed normal
order. Its noncrossing matching has14 possibilities. Columns split them by
normal residue modulo3, into the groups

    {0,6}, {1,7,6c+1,6a+4}, {2,6a+2}.

The two two-point groups have forced partners; the four-point group has two
noncrossing choices. Therefore there are exactly28 NECESSARY H/V boundary
pairing TYPES, valid at unbounded period, multiplicity and parameters a,c.
The certificate lists all28, with every edge's full voltage as an affine
function of a,c. No type is claimed physically completable or excluded.

All28 already pass the mod-two homology check identically, so that check is
not a new exclusion of this family. The nonadditive information is the actual
matching and its unresolved internal lifetime components, not that parity.
The new proof obligation is to constrain how the horizontal and vertical
pairings can share ACTUAL BLACK lifetimes and one actual event cycle. It is
not legitimate to assume that the projected boundary cycles are simple or
have unit winding merely because the three controls have that property.

## Limits

This establishes a global chronological boundary reduction and a finite
set of boundary pairing types for a live infinite family. It does not make
the full state finite: the internal components, lifetimes, clocks and field
completion remain unbounded. No standard104 uniqueness, new autonomous
controller, debt escalation, global g>=12 or finite-seed attraction theorem
is claimed. No independent audit of this new package is claimed in this note.
