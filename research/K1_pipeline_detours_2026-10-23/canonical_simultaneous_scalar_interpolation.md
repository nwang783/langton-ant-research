# A single scalar terrain realizes every canonical sheet simultaneously

24 October 2026, 01:29 UTC. Complete WHITE cap-four translating front,
actual full P,d. No zero-output or K1 hypothesis. Pending independent
review. This adds simultaneous CROSS-SHEET geometry to the signed
within-sheet repair fd20e425; the former is not imported from the latter.

THEOREM: all canonical circles, across ALL sheets, are simultaneously
realized by disjoint half-integer level curves of one continuous
piecewise-linear scalar field on the dual triangulation.

A consequent essential-node rule is that every repaired graph exchange
whose TWO endpoint nodes are essential joins nodes with the SAME full-
drift winding sign. In particular a flow-four parallel pair, when both
its nodes are essential, cannot connect opposite signs.

## 1. The exact local scalar value

Normalize the incoming axis at a primal vertex v to E/W. Let r_E,r_W
count the R headings and l_E,l_W the L headings in its COMPLETE WHITE
history. The exact incident heights have an integer a_v satisfying

    C_NE=a_v+r_W,   C_SW=a_v+r_E,
    L_NW=a_v-l_E,   L_SE=a_v-l_W.

Assign the face centers their integer stream heights h. Assign v the
integer value a_v. In particular all C sectors are >=a_v and all L
sectors are <=a_v. The value is determined from the four heights:

    4a_v=C_NE+C_SW+L_NW+L_SE-delta_v,
    delta_v=n_v modulo2.

Here n_v<=4 is the complete number of reads; WHITE alternation makes
r_E+r_W-l_E-l_W=delta_v. Inactive n_v=0 corners have all four heights
and a_v equal. Rotations define the same construction in the other
checker phase. At even histories a_v is exactly the arithmetic mean
of the four incident face heights; no even-history assumption is needed.

## 2. A globally consistent dual triangulation

The four face centers around each primal vertex form one square dual
cell. Add its central primal vertex v, and triangulate into four
triangles by joining v to those face centers. These triangles tile the
plane. Linear interpolation of the assigned vertex values defines one
global continuous scalar field F, invariant under the full spatial
drift translation. Adjacent dual cells agree on their shared edge,
which joins one C face center and one L face center.

For sheet j use the level F=j-1/2. All triangulation vertex values are
integers, so no such level passes through a vertex. Across a dual edge
joining C and L, the level is crossed exactly when

    h(L)<j<=h(C),

the signed active physical port g_j(e). Its orientation has larger F
on RIGHT, matching the physical edge orientation C-right/L-left.
For a multiply used physical edge, its chronological r-th occurrence
has j=h(C)-r+1. As r increases the level crossings move monotonically
from the C side toward the L side. Thus this single triangulation also
fixes the required simultaneous order of all parallel occurrence tracks.

## 3. The local level arcs are exactly the canonical repair

If j>a_v, the central value is below j-1/2. All L sectors are below as
well, so the level curves turn RIGHT around the high C sectors. If
j<=a_v, the center and all C sectors are above the level, so its arcs
turn LEFT around low L sectors. Four active ports give respectively
two RIGHT or two LEFT arcs with the corresponding central patch.

The WHITE cap-four canonical repair has EXACTLY this rule:

    every canonical arc at j>a_v is RIGHT;
    every canonical arc at j<=a_v is LEFT.

Indeed R0 is on the local C top, above a_v. One-R final L1 is at a_v.
A flat two-R exchange uses a_v+1 (RIGHT) and a_v (LEFT); a same-R
exchange has the SAME two levels and directions. Optional L3 is at
most a_v and is LEFT. These cover all R,RL,RLR,RLRL histories, with
all incoming headings retained. At two active ports there is only one
possible corner; at four the two R/R versus L/L pairings agree exactly.

Therefore the global half-integer contours reproduce every canonical
cycle and its full-drift winding. Distinct sheets are levels of the SAME
continuous field, so they cannot cross. This is stronger than merely
checking that each individual sheet can be drawn without crossings.

## 4. Essential exchange endpoints must have the same winding sign

At every two-R exchange, L1 and R2 share one physical port. Its two
exchanged occurrences are consecutive chronological port ordinals and
have adjacent sheet labels. Let the upper/lower endpoint circles of
this exchange BOTH be essential, hence embedded winding+1 or-1.

Their two crossing points on the shared dual edge bound a short open
connector. By the monotone scalar interpolation, its interior meets
neither selected circle. It is on LEFT of the upper contour and RIGHT
of the lower contour. The circles are disjoint essential circles in
the cylinder. The complementary component incident to BOTH is their
intermediate annulus; the connector identifies precisely that component,
not an unproved inference from equal local tangents.

Orient its boundary with that annulus on LEFT. The two components are
the upper circle in its canonical orientation and the lower circle in
reverse canonical orientation. The annulus boundary has zero total
homology, so

    winding(upper)-winding(lower)=0.

Their winding signs therefore agree. Full drift is retained throughout;
only the signed embedded canonical circles have primitive winding here.
No such primitivity is asserted for actual chronological cut cycles.

## 5. Scope

This is an all-output geometrical constraint on ESSENTIAL assembly.
Opposite-sign essential nodes can still communicate through contractible
nodes or longer graph paths. Canonical circles are not actual continuous
cursor factors, and the scalar terrain does not certify realization of
an arbitrary necessary height profile or graph. No graph-excess upper
bound, paid renewal count, original-fuel bound or complete-front exclusion
is inferred. The zero-output face-loop classification is not needed
for sections1-4.

Control `canonical_simultaneous_scalar_interpolation.py/json` checks
all78 nonempty sheets and98 canonical arcs from all thirty complete
histories, including the exact center formula and all four-port repairs.
The global triangulation and intermediate-annulus identification are
proved separately above; no bounded spatial search is substituted.
