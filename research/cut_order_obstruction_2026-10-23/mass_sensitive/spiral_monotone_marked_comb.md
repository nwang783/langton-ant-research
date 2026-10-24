# A literal monotone marked comb inside the inward spiral

23 October 2026. New genealogical extraction from the previously audited
finite inward-spiral family. It is not a new noncapturing construction.

Inherited dependency: ../../core_periodicity_new/quadratic_inward_spiral.md
proves the complete geometry and physical feasibility of

    W_n = product for j=n,n-1,...,1 of
          (RLLR)^j L (RLLR)^j RLL (RLLR)^j L (RLLR)^j L,

from the first-L seed of mass 11n+2, with no cell read more than twice.
For n>=11, its unmodified finite seed is independently proved to capture standard104.
The present note derives an exact all-n component of its token forest.
Assume n>=2. Use initial pose (0,0),N and the Tait offsets

    o_N=(0,-1), o_E=(-1,-1), o_S=(-1,0), o_W=(0,0).

## 1. The spine producers

Circuit k, 0<=k<n, has j=n-k and starts at physical time

    t_k=k*(16n+6)-8k*(k-1).

Its south rail begins after 8j+4 reads. Define P_k to be the cursor node
starting at the last R of the first RLLR on this south rail, at time

    tau_k=t_k+8j+7,
    a_k=(-2n-2+k, 2n-1-k), heading E.

Its Tait cursor is

    v_k=a_k+o_E=(-2n-3+k,2n-2-k).                     (1)

For k<n-1 this node reads R,R,L. Its two R outputs are at

    a_k=v_k+(1,1),
    b_k=v_k+(1,0).

For k=n-1 the south rail has only one RLLR; its last R is followed by the
standalone L corner. Hence P_(n-1) reads R,L and emits only a_(n-1).

Before P_0 the L at

    q_0=v_0+(0,1)=(-2n-3,2n-1)

is a first read in circuit zero. It therefore consumes one initial-black
identity, and P_0 is the unique child of that virtual input root.

## 2. Exact two-child reproduction, including dormant lifetimes

The inherited adjacent-circuit overlap says that a_k and b_k are both read
L in circuit k+1, consecutively, as the first and second L of its FIRST
south-rail RLLR. There are no other reads of those sites.

Consumption of a_k creates a cursor node Q_(k+1), which immediately reads
b_k L and has r=0. Its starting pose is b_k,S, so its Tait location is

    b_k+o_S=v_k.

This is a zero-displacement parent-child edge P_k -> Q_(k+1).
Consumption of b_k creates P_(k+1). By (1),

    v_(k+1)-v_k=(1,-1).

Thus P_k has exactly the two cursor children Q_(k+1),P_(k+1).
Every Q is a leaf. P_(n-1)'s one output is not read again inside W_n and
is a boundary bud, not an assertion of an eternal token.

These exhaust the entire cut component of q_0: each P has only the stated
one or two R outputs, and each Q has none. The component is precisely an
n-vertex spine with n-1 single-node side leaves and one final boundary bud.
The spine crosses each causal axial cut at most once and has no backtracking;
all side ancestry displacements vanish. This statement is about ancestral
edges, not the full chronological cursor path.

For j=n-k>=2, tau_(k+1)-tau_k=16j-2. Both output black lifetimes have age

    16j-4,

because a_k is consumed at tau_(k+1)-2 and b_k at tau_(k+1)-1. These actual
lifetimes are retained; the comb is not obtained by silently erasing dormant
tokens or assuming immediate consumption.

## 3. Every one of these nodes carries residual UNION6 events

The full eleven-labels at the three updates of a nonfinal P_k are respectively

    RLLRRLLRLLR,
    LLRRLLRLLRR,
    LRRLLRLLRRL.

At the two updates of final P_(n-1) they are

    RLLRRLLRLLR,
    LLRRLLRLLRL.

At Q_k the label is RRLLRRLLRLL when its circuit has j>=2, and
LRLLRRLLRLL in the last j=1 circuit. These fixed labels follow from the
last west-rail RLLR, the RLL corner, and the first south-rail RLLR; for the
last Q the preceding standalone L supplies the one extra letter.

For EACH of these six labels, both overlapping ten-factors lie outside the
pinned 84 cyclic standard factors, and the eleven-label lies outside UNION6.
This is a complete six-item finite membership check. Consequently all reads
of these nodes are residual events. The component has exactly

    M=n+(n-1)=2n-1 marked cursor nodes,
    R=3(n-1)+2+(n-1)=4n-2 residual events.             (2)

For the marked skeleton of this component,

    r=1, S=n-1, I=n-1, b=n, c=n-1.

In particular M=r+S+I exactly, as in the companion skeleton theorem.

## 4. What this disproves and what it leaves open

There is no uniform per-initial-root bound on residual descendants merely
from monotone spatial ancestry, no causal cut recrossing, outdegree at most
two, and side-bush depth one. All those properties hold in this one exact
component for every n, while (2) diverges. Spatial ordering does not itself
make historical splitting or marked-generation counts bounded.

This is not a fixed-total-mass counterexample. The complete seed still has
mass 11n+2, and many other roots support the actual chronological excursion.
It does not exclude bounds that use full mass, source radius, marked-chain
length, lifetime scales, complete live-cursor cut crossing complexity, or
other ancestry components. It also does not produce an infinite marked comb
from one finite seed: the displayed family is independently proved to capture
standard104 for every n>=11. No smaller-parameter continuation is used here.

The contribution is a literal all-parameter realization of the marked-comb
obstruction with straight monotone ancestry, not just an abstract forest
with arbitrarily assigned marks. Independent review requested.
