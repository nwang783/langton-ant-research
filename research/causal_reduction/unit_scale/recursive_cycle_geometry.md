# Geometry required of hidden recursive transport cycles

23 October 2026, 06:00 UTC. Independently reviewed analytic deductions.
These are architecture filters, not a general ant theorem or a construction.

## Scope and occurrence graph

Fix a finite nonerasing typed substitution with additive spatial matrix I.
Each letter represents one unit physical movement. Images have the same net
movement as their parent, and a growing fixed root a defines genuine nested
prefixes phi^r(a) of one actual ant trajectory. A root-cycle/finite-order
presentation is first replaced by its actual fixed-root, spatial-I power.
No intermediate phase is assumed legal. Arbitrary initial backgrounds are
allowed throughout this note.

The finite occurrence multigraph has one edge s->t for every child occurrence
in phi(s), labeled by its integer read-position offset from the image start.
Restrict it to states reachable from a. A leaf read position is exactly the
sum of the labels along its depth-r occurrence walk. Let Q be the finite set
of nonzero sums of all directed SIMPLE cycles in this reachable multigraph.
Parallel occurrences are distinct edges. A simple path has bounded length;
removing cycles decomposes every walk's offset into one of finitely many base
offsets plus a nonnegative integer combination of simple-cycle offsets.

The root-prefix endpoint is always the fixed vector v_a. Its incoming heading
belongs to a finite set, regardless of whether the images preserve headings.
Since the root is growing, the prefix endpoints supply infinitely many actual
checkpoints at that fixed position.

## 1. The cycle shifts cannot all point into one strict half-plane

If Q is empty, all leaf positions lie in the finite set of base offsets. This
contradicts finite-domain escape for a growing actual ant path.

If there exists a real linear functional ell with ell(q)>0 for every q in Q,
let E be the set of all possible occurrence-walk offsets. It has finite
ell-sublevel sets. Indeed, for ell(p)<=M the total multiplicity of all nonzero
cycles is at most (M-min_base ell)/min_Q ell. Zero-offset cycles can be removed
without changing position. There are then finitely many possible integer sums
and base choices, independently of the order of cycles in a walk.

The actual trajectory stays in E, because every read belongs to a sufficiently
large nested root prefix. The signed quantitative cone-transience theorem
(`../../computability/one_sided_cpu_hull_obstruction.md`, Section4) says that
an ant path in such a domain visits every finite pose set only finitely often,
even on an arbitrary background. This contradicts the root checkpoints.

Consequently Q is nonempty and admits no common strictly positive functional.
Equivalently, zero belongs to the convex hull of its nonzero vectors. In the
plane the necessary cycle geometry must have opposing directions or surround
the origin. A single drifting hidden component with only zero-offset cycles
downstream cannot by itself support a growing rooted ant presentation.
This does NOT forbid that component as a finite local factor: the independently
legal U^r R V^r oblique hairpin is an explicit such local example.

## 2. An oblique line of cycle shifts is also impossible

Suppose all simple-cycle offsets, zero included, belong to one line L whose
direction has BOTH coordinates nonzero. Cycle removal puts all read positions
in a fixed-width strip around L, and bounded individual edge offsets put every
depth-r block inside a longitudinal interval of length O(r). Thus its read set
has O(r) cells. The strip's normal has both coordinates nonzero.

Apply the signed uniform-gain one-coordinate clock from
`../../computability/oblique_strip_clock_obstruction.md`, Sections1-2, choosing
one fixed weight that is bounded above and below on this strip. Its field
coefficient and head correction are uniformly bounded there. For each finite
root prefix, copying its entry colors on its finite read set to an otherwise
white board preserves the actual interval. The complete field-change term is
O(number of read cells)=O(r); the endpoint-head term is bounded. The clock
increases by at least2 per step. Therefore

    |phi^r(a)| = O(r).

This is a time bound for these specific finite strips, not a global linear
escape estimate and not an assertion about axial strips.

### Linear-growth fixed-root lemma

Write phi(a)=a u, with u nonempty because the fixed root grows. Then

    phi^r(a) = a u phi(u) ... phi^(r-1)(u).

Nonerasing implies that the integer lengths |phi^j(u)| are nondecreasing.
Their partial sums are O(r), so the lengths are uniformly bounded: a
nondecreasing unbounded sequence has unbounded Cesaro means. There are only
finitely many words of bounded length on the fixed alphabet. Iteration of phi
on this finite set is eventually periodic. Hence the infinite fixed root word
has an eventually periodic physical-movement tail.

If that periodic tail has nonzero net movement per period, its positions at
unbounded times cannot remain in a fixed finite set. But the root-prefix
endpoints are all v_a. Thus the periodic tail has zero drift and is confined
to a finite footprint. This contradicts finite-domain escape on every board.

Therefore all cycle offsets cannot be collinear in an oblique direction.

## Precise remaining geometry

A legal growing fixed hidden-state unit-spatial presentation must have cycle
shifts balanced in the sense of Section1 and must NOT have all cycle shifts on
one oblique line. This leaves genuine two-dimensional configurations and
opposing AXIAL cycles. No obstruction to those residuals is claimed here.
The conditions concern every reachable occurrence cycle, not merely the
Perron-one cycles in the separately signed drifting-cycle necessity theorem.
They do not classify changing directives, moving-scale matrices, or arbitrary
ant trajectories without this fixed presentation.
