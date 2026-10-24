# A decorated stationary construction must contain a drifting recursive cycle

2026-10-23 05:35 UTC. Analytic criterion independently signed as audit JP at05:42 UTC.
This is necessary architecture, not an ant construction or undecidability proof.

## Statement

Consider a fixed finite typed, nonerasing substitution with exact additive
unit-spatial geometry. A state specifies one physical quarter-turn read and
unit displacement v_s; its image has net displacement v_s. Assume the iterated
words are genuine physical read-state words and their endpoint headings are
fixed or eventually periodic with depth. This includes exact unit-pose typed
controllers and the previously verified adjacent-direction pair lifts.

Suppose a growing rooted fixed limit is an actual Langton-ant trajectory, on
any initial coloring. Then its reachable occurrence graph contains a strongly
connected component which has BOTH properties:

1. its internal ordinary incidence Perron value is exactly one;
2. the sum of its read-offset labels around its unique directed cycle is a
   nonzero vector in Z².

Such a component is a simple directed cycle of recursive labels, with exactly
one internal child occurrence per state. It may emit arbitrary lower-component
children. Its nonzero cycle displacement means the recursive label actually
moves under refinement, rather than merely receiving a different decoration.

For a genuine first-letter root cycle, apply the statement to the fixed-root
power defining that actual growing limit. For finite-order spatial geometry,
first take a common spatial-order/root-cycle power with the same exact typing
conditions. No intermediate phase is assumed ant-legal.

## 1. Incidence components

An irreducible nonnegative integer matrix with spectral radius one is a
permutation matrix of a single directed cycle. Indeed every internal row of
an irreducible component has at least one edge. If any row has two occurrences,
strong connectivity produces branching closed walks and spectral radius>1;
equivalently strict Perron comparison with a selected internal cycle gives the
same conclusion. When every row has exactly one child, irreducibility makes
the component one cycle. Singleton components without a self edge are transient
and have spectral radius zero.

Call components with ordinary Perron value>1 branching. Every other recurrent
component is therefore a single cycle. If its offset sum is q and its length
is l, its weighted spectral radius at positive characters is

    (X^(q_x)Y^(q_y))^(1/l).

In particular a zero-displacement cycle has weighted radius one at EVERY
positive character, regardless of its individual edge offsets.

## 2. If no component branches, zero cycle shifts bound the footprint

Assume, for contradiction, that every recurrent Perron-one cycle has offset
sum zero. If there is no branching component, any leaf path in the occurrence
graph crosses its SCC DAG in a fixed finite order. Inside a cycle, remove all
complete laps without changing its displacement. The remaining partial lap
has bounded length. Transient components and intercomponent edges are visited
at most once. Thus all leaf-position sums belong to a fixed finite set,
independently of depth.

The entire growing root prefix would remain in that finite footprint. The
finite-domain escape theorem excludes this on every coloring. Hence some
branching component exists.

## 3. A bottommost branching block and its clock domain

Choose a branching SCC T with no branching SCC strictly downstream. On T and
its descendants the exact weighted incidence has block form

    M(X,Y) = [[B(X,Y),C(X,Y)],[0,D(X,Y)]].

The irreducible block B has lambda(1,1)>1. Every downstream SCC is transient
or one of the assumed zero-displacement cycles, so rho(D)<=1 at all positive
characters. Polynomial couplings between such SCCs are allowed.

There is a nonempty rotated positive-clock domain U where lambda_B>1. To see
this, regard every separate child occurrence as an edge with integer offset.
If an internal directed cycle has nonzero sum q, choose z with nonzero
coordinates and z dot q>0. Along characters(exp(t z_x),exp(t z_y)) its cycle
weight diverges, so lambda_B>1 for large t. A quarter rotation puts the same
large characters in the strict clock cone.

If all internal cycle sums are zero, fix paths from a reference state. Path
independence, checked by appending a common return path, gives vertex potentials
a_s with each edge offset a_target-a_source. Thus B is diagonally monomial-
conjugate to B(1,1), and lambda_B is the constant lambda_B(1,1)>1. Any strict
clock domain works. Parallel occurrences cause no problem: under this case
they necessarily have equal offsets, while their multiplicities are retained.

## 4. The downstream modes cannot cancel the genuine pole

On U choose the corresponding literal positive clock vector g=H-d>0. At
 t0=1/lambda_B in(0,1), the downstream resolvent converges nonnegatively because
rho(D)<=1. Consequently

    h(t0)=g_T+t0 C(I-t0 D)^(-1)g_downstream

is strictly positive. The irreducible Perron pole in (I-tB)^(-1)h(t) is genuine
in every T coordinate. A fixed or eventually periodic endpoint head sequence
has no pole inside the unit disk and cannot cancel it in the exact identity

    M^r g = H(r)-M^r d.

Ant legality bounds every coefficient of M^r d by one in absolute value, using
the fixed incoming-axis parity at each position within each depth-r word.
Unit-spatial geometry gives O(r) read offsets. The signed finite-valued rational
array theorem therefore gives a fixed semilinear denominator, a product of
1-t^a X^b Y^c with positive integer a.

This denominator must vanish at t=1/lambda_B throughout U. Real-analytic
continuation over the connected positive quadrant forces the same at X=Y=1,
contradicting lambda_B(1,1)>1. Thus the assumption that all nongrowing cycles
have zero displacement was false.

## Interpretation and limits

The minimal unresolved stationary mechanism is genuinely recursive transport,
for example a decorated label b with image U b V where net(U)=-net(V) is
nonzero. The count of b need not grow exponentially, but its read position
moves. No legal growing example is asserted, and a single drifting cycle does
not imply consistency, finite initial support or a counterexample.

The exact arbitrary-mass realization decision JE/JF still applies to a supplied
finite-power presentation of this kind. This theorem gives a structural filter
and a focused construction target, not a route to undecidability inside a class
already proved decidable. Changing directive schedules and arbitrary finite-seed
trajectories are not classified by this fixed-transfer argument.
