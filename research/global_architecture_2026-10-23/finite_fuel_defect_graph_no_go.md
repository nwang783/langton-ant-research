# Defects, not duration: finite-fuel graph certificates and a global no-go

23 October2026. Analytic resource-graph lemma and architectural consequence,
submitted for independent review. The quadratic spiral is RETAINED signed
source material, not a new construction or event-count calculation.

## 1. Supplied finite resource graph

Let G be a finite directed multigraph, restricted to vertices reachable from
its permitted initial states. Each edge has nonnegative integer fuel cost w(e)
and nonnegative integer defect count k(e). Put V=|Vertices| and
r=max_e k(e), using r=0 for an edgeless graph.

For exact ant front graphs, augment the finite state by the TRUE preceding
ten turns. Then k(e) counts adjacent bad-ten events K ending during that edge's
literal updates, including windows crossing macro boundaries. This extra
finite suffix cannot be omitted or reset. For a sound overapproximation,
k may dominate the actual event count instead of equaling it.

Fuel costs must be honest nonrenewable physical charges. In the initial-black
interpretation, each charged unit is a distinct original initially-black cell,
so the total path fuel is at most the initial black mass. Arbitrary-XOR caps
must instead charge every exceptional flip if finite total COLOR-CHANGE cost
is the intended resource. Free whitening is not admitted.

## 2. Exact cycle criterion for a finite graph's defect budget

There exist finite constants A,C such that EVERY finite path from an allowed
initial state obeys

    sum k(e) <= A*sum w(e)+C                             (1)

iff every reachable zero-fuel directed cycle has defect sum zero.

Necessity: repeat a reachable zero-fuel positive-defect cycle. Its entry cost
is fixed, while its defects diverge.

Sufficiency permits zero-fuel ZERO-DEFECT cycles of arbitrary duration. In any
zero-fuel path, remove all closed cycles. They all have defect sum zero, and
the remaining simple path has at most V-1 edges. Thus any zero-fuel run has at
most C0=(V-1)*r defects. A path with s positive-fuel edges has s+1 such runs;
s<=sum w because positive fuel costs are integers. Therefore

    sum k(e) <= V*r*sum w(e)+(V-1)*r.                    (2)

This is a defect bound, not a time bound. An arbitrarily long standard highway
cycle can have w=0,k=0 and is completely compatible with (1).

The test is finite and effective: inspect cycles of the zero-fuel subgraph,
or its strongly connected components. A positive-k edge inside a cyclic
zero-fuel component is exactly a violation, since k is nonnegative.

A sharper slope is the largest k(C)/w(C) over simple cycles with w(C)>0
(take zero if there are none);
zero-fuel cycles are separately required to have k(C)=0. There are finitely
many simple cycles. Taking that slope (or the safe V*r slope) makes every
cycle's k-A*w nonpositive. Finite longest-path/difference constraints then
give a potential Phi with

    k(e) <= A*w(e)+Phi(target)-Phi(source).              (3)

Telescoping yields (1) with C=osc(Phi). These are standard finite weighted-
graph facts; the important ant premise is the honest fresh-fuel interpretation.

## 3. Conditional fuel-or-routing defect budget

Suppose a physical execution is honestly partitioned into J fixed-profile
intervals represented by such graphs, with at most R exceptional macro steps.
Carry the actual ten-turn suffix and inherited front into each interval;
neither is reset. Suppose all interval fuel charges concern distinct original
black cells across the WHOLE execution. If their certificates use common
bounds A,C, and every exceptional macro has at most M literal reads, then

    total K <= A*|B_initial| + J*C + M*R.                (4)

Each update ends at most one K event, including the exceptional-window joins.
Actual suffix carriage counts joins inside the interval graphs without an
extra hidden boundary debt. Equation(4) allows indefinitely long zero-defect
highways while controlling actual nonstandard interactions.

The physical ownership partition is a supplied premise, as in the signed
weighted-front fuel note. This is not asserted for every ant trajectory or
for all nonstandard wake preparations.

## 4. A universal FIXED finite fresh-fuel graph is already impossible

Assume one FIXED finite graph G, with finite edge defect counts, soundly
represents every finite prefix from every finite seed. Assume that for each
such physical prefix its graph path satisfies

    graph fuel <= |B_initial|,
    graph defect count >= actual K count,

and that G passes Section2's zero-fuel-cycle criterion. The initial abstract
state may depend on the whole seed; only finitely many graph states exist.
Then (2) gives a universal LINEAR initial-mass bound

    actual K <= V*r*|B_initial|+(V-1)*r.                 (5)

But the retained independently signed source
`../computability/quadratic_capturing_defect_lower_bound.md` gives, for every
n>=11, an ORIGINAL capturing seed with

    mass m_n=11n+2,
    actual K >=8(n-2)^2.

It cites the complete all-parameter inward spiral and its independently
verified eventual standard104 tail. The K lower bound counts eleven-letter
windows inside explicit RLLR runs, not just long elapsed time. It contradicts
(5) as n grows.

Therefore no such universal fixed finite fresh-fuel/K graph certificate can
exist, even when restricted to this already-CAPTURING family. The same no-go
holds for a FIXED FINITE COLLECTION of such graphs, or any fixed affine fuel
allowance a*|B_initial|+b. This does NOT exclude a finite graph with spurious
positive-defect zero-fuel cycles whose unrealizability requires an additional
unbounded side condition; it excludes using the finite cycle criterion alone
as a universal fresh-fuel budget certificate.

The forced alternative is explicit: a universal fixed graph satisfying the
honest-fuel and defect-dominance assumptions MUST retain a reachable zero-fuel
positive-K cycle. In an overapproximation it may be spurious. Only an additional
exact cycle-lifting theorem, preserving one realizable finite-board entry and
all its future compatibility, would turn it into a genuine noncapture
candidate. That lifting theorem is not inferred from the spiral.

The new result here is this architectural consequence, NOT the retained
quadratic lower bound, and NOT fixed-mass divergence or noncapture.

## 5. Quantitative model-complexity requirement and remaining route

If a graph G_n covers the n-th spiral and passes the same cycle criterion,
with honest fuel <=m_n, its V_n and r_n must satisfy

    V_n*r_n >= 8(n-2)^2/(11n+3).                         (6)

Indeed (2) is at most V_n*r_n*(m_n+1). With uniformly bounded literal macro
length, r_n is bounded, so the graph-state count must grow at least linearly
with n. A growing edge description or nonlinear initial credit can also
escape the fixed-model contradiction; neither is supplied for free.

A MASS-DEPENDENT graph family G_m remains a logically possible global route.
If, uniformly for every mass bound m and every placement of at most m initial
black cells, one constructs a finite sound graph with honest fuel<=m,
correct true-history defect counts and no zero-fuel positive-defect cycle,
then it proves the computable bound

    B(m) <= V_m*r_m*m+(V_m-1)*r_m,

and hence standard104 capture via the retained finite-K equivalence. No such
global graph family or ownership reduction is known here. Its uniform soundness
and nonrenewable charging are the EXACT missing premises. A local necessary
macro grammar, finite root count, or finite prepared-front graph does not
establish them.

Thus the proposed resource route remains useful only with mass-sensitive or
unbounded structural information. One fixed finite macro automaton with
initial-black fuel cannot close the global gap: known positive inputs already
rule that architecture out.
