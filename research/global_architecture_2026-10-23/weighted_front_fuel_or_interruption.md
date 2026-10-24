# Exact colored-front costs give fuel-or-interruption bounds

23 October2026. Analytic quantitative corollary submitted for independent
review. No new consumer scan, graph enumeration or generic ownership compiler.
Finite weighted-graph arguments themselves are standard; the indexed claim is
their exact fresh-cell/fuel interpretation and conditional preparation lift.

## 1. Exact weighted input, not a necessary-history abstraction

Take one of the exact finite colored-front/history constructions already
proved in this directory, with an explicitly finite prepared-input phase.
Hold the selected prepared profile fixed. Permit finite controlled changes on
GENUINELY NEW physical cells, then literal toggling thereafter.

For black-additions-only input, assign each edge nonnegative integer cost

    number of its new T-white cells initially chosen black.

T-black cells remain black. For arbitrary XOR-cap decisions one can instead
count all changed fresh cells, but that is a COLOR-FLIP budget, not automatically
an initial-black budget over an infinite prepared background. Keep these
interpretations separate.

Exact geometric retirement is essential: a 'new' cell cannot merely be absent
from a guessed local mask. Distinct fresh assignments along a path are distinct
physical cells. Within-edge repeats use one assigned bit and its literal
updates. Initial inherited-front choices can be assigned their exact cap cost,
or granted free as a conservative relaxation for a NECESSARY lower bound.
They are never reset physically between edges.

Let G be this finite weighted graph, I its valid initial-state set, and restrict
to vertices reachable from I in the full controlled graph. The zero-cost edges
are precisely the uncontrolled fresh-input transitions. All statements below
are finite-graph statements; interpreting them as finite-cap existence requires
the exact initialization and reachability semantics, not arbitrary fictional
inherited histories.

## 2. Zero-cost cycles are exactly the finite-total-cost alternative

An infinite path of finite total cost exists iff a zero-cost directed cycle
is reachable. A reachable zero cycle gives a finite-cost entry and endless
free continuation. Conversely, finite total nonnegative integer cost permits
only finitely many positive-cost edges, so an infinite tail is zero-cost and
contains a cycle.

If there is no reachable zero-cost cycle, the zero-cost subgraph is a DAG.
Let h be its maximum edge-path length and T=h+1. Every T consecutive edges
contain a positive-cost edge. Hence every N-edge execution satisfies

    cost >= floor(N/T).                                   (1)

T is effectively computable and at most the number of reachable vertices.
If the full graph itself is acyclic, execution has a finite maximum horizon;
there is no unbounded family to fund.

A finite arbitrary-front zero-input UNSAT slab of length T is an alternative
certificate of the same bounded zero-run property, without building a huge
graph. In particular the signed five-period short-refinement proof supplies
T=5 for its own exact profile/scaffold contract. This observation does not
silently import its physical constants into other architectures.

## 3. Sharper mean-cost and potential certificates

If the reachable graph has cycles but no zero-cost cycle, let

    mu=min_C cost(C)/length(C)>0                           (2)

over directed simple cycles. This is a computable positive rational. Removing
closed cycles from an N-edge path leaves at most V-1 edges, where V is the
reachable-vertex count. Removed cycles cost at least mu times their lengths,
and all remaining costs are nonnegative. Therefore

    cost >= mu*(N-V+1).                                   (3)

A negative right side is vacuous. Integer costs permit taking its ceiling.

Equivalently there is a rational finite potential psi satisfying

    w(e)+psi(target)-psi(source)>=mu.                     (4)

To construct it, the weights w(e)-mu have no negative directed cycle; use
shortest-path difference constraints exactly as in the supplied control-progress
certificate. Telescoping gives the potentially sharper certificate

    cost >= mu*N-osc(psi).                                (5)

These are resource potentials on an EXACT colored-front graph, not a claim
that the unrestricted ant has a finite resource automaton.

## 4. Piecewise preparation and routing interruptions

Supply an actual N-step consumer prefix and an explicit ownership partition:
R exceptional steps are discarded; the remaining steps form J>=1 consecutive
intervals of lengths N_1,...,N_J. In each interval its prepared profile beta
is fixed, its actual inherited front is admitted, its graph transitions are
exact, and the extra black fresh-input cells charged there are initial black
cells of the original finite seed. A cell is charged at most once across ALL
intervals. No later repair or earlier writer is omitted from this contract.

For a finite supplied profile family, suppose every relevant zero-cost graph
is acyclic, and let T be the largest h_beta+1. Then

    |B| >= sum_j floor(N_j/T)
         >= floor((N-R)/T)-(J-1).                         (6)

Alternatively choose one positive mu valid for all cyclic components of all
these graphs, with potential ranges at most C. Acyclic graphs can also satisfy
(4) at this mu by finite difference constraints. Then

    |B| + mu*R + J*C >= mu*N.                             (7)

Thus the consumer must use linear original fuel OR linear interruption/
routing complexity. The profile selector must remain fixed within each
interval; allowing a free new profile every edge would change the theorem.

The signed endpoint/fringe, enlarged-envelope and black-persistence arguments
explain how standard-flight preparations can discharge such contracts for a
SUPPLIED finite architecture. All relevant physical levels must use one common
gauge; discarded windows must cover cap reads, perpendicular strips and every
possible writer-overlap repair. A generic numerical R,J bound or ownership
compiler is NOT supplied by this note. Without that premise, (6)/(7) must not
be advertised as an all-standard-itinerary theorem for arbitrary palettes.

## 5. Concrete controls and provenance

For the supplied word RL from north on white input, the full-drift front is
empty and each block's new L cell needs one initial black. The exact weighted
graph is one vertex with one edge of cost1: N blocks require N distinct initial
black cells. On the periodic prepared RL input, that same edge has cost0,
allowing an infinite execution with no EXTRA cap but an infinite black rail.
This does not produce a finite-seed infinite orbit.

For RLLR on white input, its four read classes are fresh per block and exactly
two require black. Its one-edge graph has cost2, so mu=2, whereas the coarser
zero-run bound gives only one black per block. Both words have net turn charge
zero. Thus fresh first-read fuel is stronger information than total signed
charge alone.

The retained `../causal_reduction/unit_scale/prefix_charge_graph.md` already
uses finite weighted cycles and potentials to bound nested substitution
prefix charge. That is a NECESSARY nonspatial charge abstraction, expressly
not exact same-cell chronology or finite first-L support. It is not relabeled
new. The exact graph reduction and source-specific five-period fuel ownership
are also attributed dependencies. The new combination is the generic fresh-
input cost interpretation and interruption inequalities above.

A nonstandard repair writer changes the prepared-input family and may create
a zero-cost cycle absent from all-standard profiles. Such repairs are outside
a standard-only ownership contract unless explicitly included and verified.

## 6. Missing global premise remains explicit

This theorem does not bound the unrestricted ant's defect count. It requires
an exact finite front architecture, a globally finite input observer, and an
honest physical ownership partition. Arbitrary finite-seed trajectories are
not known to enter such a representation; balanced return itineraries and
unbounded footprints can defeat the bounded-memory hypothesis.

A zero-cost cycle is an architecture opportunity, not by itself an autonomous
finite-seed construction from a different producer. Its cap launch, prepared
background and physical connectors still require proof. Conversely zero-cycle
absence supplies a rigorous quantitative obstruction WITHIN the supplied
architecture, not universal standard104 capture.
