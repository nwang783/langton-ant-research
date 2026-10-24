# Prefix-charge graphs and finite-fuel Dyck restrictions

23 October 2026, 02:45 UTC. Independently signed analytic necessary filter.
It is not an ant-realizability certificate and does not settle unit scale.

## General exact-charge refinement

Let a finite alphabet S describe physical turn states. Each s has a signed
turn charge eps(s) in{+1,-1}, and a nonempty image phi(s)=s_0...s_(l-1)
satisfying exact charge preservation

    sum_j eps(s_j)=eps(s).

The image lengths may vary, and the states may retain headings or context.
For each image occurrence j put an edge s -> s_j with integer weight

    w(s,j)=sum_(i<j) eps(s_i).

For any nested choice of image occurrences, the signed charge preceding
that final letter in the refined root is exactly the sum of its edge
weights. This follows by induction: every fully preceding refined child
has the same total charge as its unrefined symbol. Therefore the set of
signed prefix charges at refinement depth r is precisely the set of
length-r path weights from the root in this directed weighted graph.
Here these are the prefixes BEFORE a selected nested letter. The complete
refined image has the fixed charge of its root symbol, so adding whole-image
prefixes does not change any bounded-below conclusion.

If a growing rooted power-limit is an actual ant from a finite seed of
mass M, every prefix charge is at least -M. Thus no negative cycle may be
reachable from the root. Repeating such a cycle gives path weights tending
to negative infinity, hence negative required black mass. For a root
cycle of length m, only refinement depths divisible by m need be actual
prefixes. Pad the repeated negative-cycle walk by at most m-1 edges to
that residue class; bounded extra weights cannot remove the divergence.

Conversely, if no negative cycle is reachable, every walk can have its
nonnegative cycles removed without increasing its weight. The finite set
of simple paths therefore bounds all prefix charges below. This proves
an exact equivalence with bounded-below total charge, NOT with legal
same-cell colors or finite first-L support. The latter conditions are
strictly stronger. A shortest-path calculation yields a necessary seed-
mass lower bound. For exact minima in a root power-limit, use the product
with the refinement-depth residue modulo m.

This graph test needs no spatial expansion, unit geometry, or uniform
image length. It only needs exact charge preservation and an actual
rooted refinement limit.

## Complete simplification for two turn letters

Suppose S={R,L}, eps(R)=1, eps(L)=-1, both letters are reachable, and
charge(u)=1,charge(v)=-1. Absence of reachable negative cycles is equivalent
to these two simple ballot conditions:

    Every prefix of u has charge at least0.
    Every prefix of v has charge at least-1.

Necessity: if u ever falls below0, its final charge1 forces a later R read
whose preceding prefix charge is negative. This is a negative R->R edge,
hence a negative self-cycle. If v falls below-1, the first step reaching-2
is an L read at preceding charge-1, giving a negative L->L self-cycle.

Sufficiency: under the two ballot conditions, every R->R edge has weight
at least0. Every R->L edge has weight at least1, since an L from height0
would create a negative prefix. Every L->R edge has weight at least-1,
and every L->L edge has weight at least0. All self-cycles and every
alternating cycle therefore have nonnegative weight. Equivalently the
potential V(R)=0,V(L)=1 satisfies w(s,j)>=V(s_j)-V(s).

In particular u necessarily starts R. Thus a genuinely finite-fuel
unit-scale two-turn candidate cannot use a first-letter R/L two-cycle;
that cycle can exist only after dropping the finite-fuel requirement.
For an R-root all refined prefixes have charge>=0. For an L-root they
have charge>=-1. These sharpen the generic bounded-below conclusion.

Combined with nonuniform_charge_reduction.md, EVERY growing rooted legal
finite-seed model in that undecorated heading-preserving unit-scale class
must use these exact charge-preserving ballot images, at arbitrary image
lengths. Decorated/context-dependent models retain the general graph
criterion but not this two-letter simplification.

## Small diagnostic

Among the six legal unit9 right images, only RRRRLLLLR and RLRRRRLLL meet
the right ballot condition. Among the six left images, only RRRLLLLRL and
LRRRRLLLL meet the left condition. Thus just four of the24 prolongable
pairs pass this necessary total-charge test. All four are already excluded
by literal conflicts, independently of this argument. Do not interpret
passing this diagnostic as finite support or ant legality.
