# Every white translating front has essential first-departure counterflow

23 October 2026, 10:55 UTC. New analytic candidate for independent review.
No novelty, general capture or unrestricted multiplicity exclusion claim.

Let a COMPLETE bi-infinite initially-WHITE Langton front have actual full
drift d!=0 and full event period P. There are finitely many active cell
classes modulo Z*d. Every physical active cell v has a complete finite
history beginning R, and first read time T(v), with T(v+d)=T(v)+P. There
is no initial-head exception. Put D=||d||infinity.

Define b(v) as the physical cell entered immediately after v's FIRST R.
It is active, b(v+d)=b(v)+d, and its arrival time is T(v)+1. Thus b induces
an outdegree-one functional graph on active full-drift classes. Every
component has a cycle.

THEOREM: every such quotient cycle has winding -1 in the ACTUAL-edge
orientation. In particular the full directed cell-flow graph contains an
essential cycle opposite the ant's full drift, supported entirely by
first-R departures. This is a different graph from the first-arrival
predecessor graph; no uniqueness or connectivity of either is claimed.

## 1. Exact local times on a b-cycle

A cycle has distinct cell classes before closure. Its directed unit checker
edges therefore form a simple embedded cylinder circle. Lift it to
v_0,...,v_ell=v_0+k*d. Let I(v) be the incoming heading at v's first R.
By definition the cycle OUTGOING direction at v is R(I(v)). Every
selected source departure is that physical source's first read, hence the
FIRST use of this outgoing port. Exact physical-edge ordinal matching
identifies its target arrival as the FIRST arrival on that incoming port.

At a RIGHT geometric corner v of this cycle, its incoming cycle heading
is I(v). Thus v's first incoming edge comes from the cycle predecessor u.
The first R at u already departs along u->v, and no u read precedes T(u).
Consequently this is v's first read exactly:

    T(v)=T(u)+1.                                      (1)

At a LEFT geometric corner v, its incoming cycle heading is -I(v), so
this arrival is not v's first read. If its complete local rank is j_v,
then j_v>=1. Any physical zero-displacement gap has positive length
divisible by four, whence

    T(u)+1=T(v)+4q_v,       q_v>=j_v>=1.             (2)

Take q_v=0 at right corners. Summing around the lifted cycle gives

    kP=ell-4Q,       Q=sum_v q_v>=number_of_L_corners. (3)

For an essential simple cylinder circle the signed total turning is zero,
so m_R=m_L=ell/2. Equation(3) gives kP<=-ell<0. Embedded simplicity permits
only k=+1 or-1 for an essential circle, therefore k=-1.

## 2. There is no contractible b-cycle

A counterclockwise physical Jordan polygon has m_L=m_R+4, hence
m_L=(ell+4)/2. For k=0, (3) would give
ell=4Q>=4m_L=2ell+8, impossible.

For a CLOCKWISE physical Jordan polygon, consider all active physical
cells in its closed bounded interior, including its boundary. This is a
nonempty finite set. It is closed under the actual FIRST-READ predecessor:
- At a boundary R corner, that predecessor is the preceding boundary cell,
  by exactly the heading observation in(1).
- At a boundary L corner, the first incoming heading is opposite the
  incoming cycle heading. Its source neighbor lies in the polygon's
  interior, because this is a concave corner of the clockwise boundary.
- For a strict interior cell, a unit grid edge from outside the closed
  polygon cannot reach it without crossing the boundary at a grid vertex;
  such a unit edge has no interior grid vertex. Its predecessor is therefore
  also in the closed polygon.
Every actual first-read predecessor is active and has strictly EARLIER
first time. A finite nonempty predecessor-closed set has an oldest first
time and cannot have such a predecessor. Contradiction.

Both orientations are excluded. Thus every b-component has an essential
winding-minus-one cycle. This argument is cap-free and uses no stream
height or white-output premise. Prepared first colors, a one-sided initial
head, or arbitrary nonperiodic paths are outside its stated scope.

## 3. Integral counterflow accumulation, across all components

Let any k distinct b-cycles have lengths ell_1,...,ell_k. Functional-graph
cycles are vertex-disjoint, so their directed edges are disjoint. Each
edge occurs at least once in the full integer cell-flow f, once as the
source's first-R departure. Subtract one copy of each cycle. The residual
flow is still nonnegative and balanced at every cell. Its homology is
1+k, since the full event loop has homology+1 and each removed cycle -1.

At every checker vertex incoming and outgoing axes differ. Thus any
balanced residual flow has equal total horizontal and vertical edge counts.
Its full displacement is(1+k)*d. Its total edge count is at least
2D*(1+k). Since the original edge count is P,

    P>=sum_i ell_i+2D*(1+k) >= 2D*(1+2k).           (4)

This is an ADDITIVE global necessary condition across distinct completed
first-departure cycles, unlike time-debt maxima that can overlap. It holds
already for any subset of the eventual cycles and does not assume the
residual flow is one event orbit or white.

The separate per-cycle rank bound from(3) is

    P=4Q-ell >= sum_L (4*j_v-2),                     (5)

using m_R=m_L. Each term is nonnegative; at R corners j=0. This is a
possible nonnegative path-debt weight in a reversed b-graph monitor, not
permission to add(5) to(4). Use a maximum between different bounds.

## 4. Possible implementation, not yet coded or signed

Reverse b edges to obtain indegree1/unrestricted-outdegree components with
required cycle winding+1. For an actual arc u->v, it is selected exactly
when u's first R departs along this arc. It matches the first occurrence
of that output port to the first occurrence of the incoming port at v;
let j be that target complete rank. Reverse the seam sign, use debt0 if
j=0 and4j-2 otherwise. Rooted-tree addition of these nonnegative debts may
be saturated at fixed scale S, just as in the independently signed first-
arrival monitor. Winding zero or minus one must be rejected at closure.

For the additive bound(4), separately retain a saturated edge count on
root-to-frontier paths. At a closure, add ell+2D to a GLOBAL cumulative
counterflow lower-bound register initialized at2D, saturating at S. This
is sound for every completed subset by(4). It is not a maximum over
components. Do not add the rank debt to that cumulative register: those
are overlapping necessary estimates and must combine by maximum.

Both graph abstractions must permit multiple essential components. Actual
standard104 has two first-arrival cycles and two first-departure cycles.
No new run, graph exclusion or finite-seed capture follows from this note.
