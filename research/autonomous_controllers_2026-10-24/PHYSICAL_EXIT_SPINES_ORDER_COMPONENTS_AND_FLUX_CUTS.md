# Exit spines order the component adjacency, with exact adjacent-cut flux

24 October 2026. Author topological proof; independent review pending.
This is a companion to cdff2e60's exact color/turn accounting, NOT a component
output bound. It applies to both WHITE and genuine prepared translating orbits.

## Hypotheses and graph distinctions

Use the full-drift physical last-departure graph on ALL read classes. Its
selected edges are actual unit grid moves. Assume the separately signed
primitive-spine theorem: each quotient cycle is an embedded essential cylinder
curve of winding+1. There are k finite quotient basins. The lifted versions of
each quotient cycle connect into one physical spine and its attached basin;
no period power or primitive-drift replacement splits those ends artificially.

The underlying complete read graph contains every ACTUAL movement edge, not
only last edges. It is connected, being the image of the one bi-infinite actual
walk. Passive unread field cells are preserved as board data but are not read
graph vertices. All graph assertions below concern the read graph only.

## 1. The component adjacency graph is exactly a finite path

The k embedded essential last spines are pairwise vertex-disjoint. Because
unit grid edges cannot cross away from grid vertices, their physical embedded
curves are disjoint. The cylinder separation theorem orders these curves from
the negative transverse end to the positive transverse end. Label their basins
C_1,...,C_k in that order; the transverse coordinate may be taken as det(d,p).
No claim that each spine has a monotone transverse coordinate is needed.

Each basin is connected to its own spine by its selected last edges and does
not meet any other basin's spine. Therefore the whole basin C_i lies on the
same side of each foreign spine as its own spine: a selected connecting path
could not cross that foreign essential curve without meeting its vertices.

Suppose an actual used unit edge joined C_i to C_j with i<j-1. Every
intermediate spine separates its endpoints. The edge would have to intersect
such a spine. Since all curves are made of physical unit grid edges, an
intersection requires a shared grid vertex (a common segment also shares
vertices). Its endpoints belong to C_i and C_j, not the intermediate basin,
which is impossible. Thus actual movement crosses only between adjacent
components.

Finally, connectedness of the full read graph forces at least one actual edge
across each division {C_1,...,C_i}|{C_(i+1),...,C_k}. Hence the undirected
component adjacency graph has exactly the path edges i--(i+1). The case k=1
is the one-vertex path. This does NOT prove k>=2.

The statement allows arbitrarily winding branches, repeated reads, cross-period
ages and arbitrary earlier traffic. It does not claim that first departures
preserve the partition: standard R38->R39 explicitly disproves that claim.

## 2. Every cut retains its full earlier movement current

For i=1,...,k-1 and physical direction h, let J_i(h) be the number of actual
C_i-to-C_(i+1) steps in direction h minus the number of reverse component
crossings in that same physical direction h. Set J_0=J_k=0. The direction of a
reverse COMPONENT crossing is its actual heading, not the negation of another
edge's heading; physical directed grid edges keep their actual orientations.

Each cut has equal total numbers of outgoing and incoming actual updates per
full period, so sum_h J_i(h)=0. Both counts are positive because the actual
cyclic event word visits both sides. No last-departure edge crosses the cut;
all these updates retain their later source-cell read obligations.

The component directional boundary vector in cdff2e60 is exactly

    b(C_i) = J_i - J_(i-1).

With the same fixed heading cut N=0,E=1,S=2,W=3, put
Phi_i = sum_h h J_i(h), and use Q_i from the full actual turn inventory.
Then the exact local and prefix identities are

    O_i-I_i = 4 Q_i + Phi_i-Phi_(i-1),
    sum_(j<=i)(O_j-I_j) = 4 sum_(j<=i) Q_j + Phi_i.

This is an adjacent-cut conservation statement, not positivity. A WHITE front
makes each O_i-I_i=O_i nonnegative, but this does not separately sign either
Q_i or Phi_i. No new numerical conjecture is inferred.

The principal-angle flux Psi from the companion note is rotation-invariant
but generally NONADDITIVE under merging neighboring blocks: principal angle
reductions can change the residual integer full turns. Therefore one must not
substitute individual Psi_i into the linear adjacent-cut equations without
retaining the corresponding integer carries. The fixed-heading vector identity
above has no such hidden reduction.

## 3. Complete standard and prepared controls

In standard's normalized drift(-2,2), the4-output spine has transverse range
[-4,-2], and the8-output spine has range[0,2]. Thus the4-output component is
C_1 and the8-output component is C_2. Its only cut has

    J_1 = (0,-4,+4,0),     Phi_1=4.

The exact charges are4=4*0+4 and8=4*3-4. This ordered-cut example is positive;
it does NOT establish a universal ordered-cut sign. The companion's negative
COMPONENT flux is still genuine, and must not be misreported as a negative
ordered-cut flux in this particular frame.

All supplied prepared controls in the companion have k=1 and thus no internal
cut. Their complete prepared backgrounds remain as supplied; they are not
WHITE examples. The topology alone cannot distinguish one from two components.

The general theorem is the cylinder-separation argument, not an extrapolation
from these one/two-component controls. The companion certificate retains every
actual standard crossing and the100 complete representation controls. The
small checker accompanying this note separately verifies the stated cut data,
all standard representation orders and the linear identities, without using
any output bound or equality of effective and actual last turns.

Artifacts: certify_exit_component_ordered_cuts.py and
exit_component_ordered_cuts_certificate.json.
