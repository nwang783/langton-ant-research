# Exact unknown-seed realization at each supplied mass bound

2026-10-23 04:01 UTC. Independently analytically signed on 2026-10-23 04:06 UTC.
This is existence of an unspecified finite seed for a FIXED finite-power
morphic path presentation, at a supplied initial black-mass bound M.

## Theorem

Given the presentation in theorem.md and any integer M>=0, one can decide
whether SOME seed with at most M black cells realizes the prescribed infinite
path. The seed coordinates have NO supplied or guessed spatial bound. If the
answer is yes, an explicit realizing seed can be returned.

One proof adds M existential coordinate pairs to IJ's automatic first-order
frame conditions and represents B as their union. For M>0, allow duplicate
points and an additional active/inactive bit per point, so all sizes <=M,
including zero, are represented. This remains a finite automatic sentence.
M=0 uses the empty board. This proof alone gives a total decision procedure.

## A more explicit finite-component algorithm

Use the exact bounded-displacement XOR graph from finite_seed_parity_graph.md.
If its label-one edge set E1 is infinite, no finite seed can work. Otherwise
list E1 and put C equal to its endpoints together with every pinned vertex.
All graph neighbors are effectively computable from the finite displacement
set and the automatic membership test. Let E0 be the zero-edge graph.

A valid seed is a union of E0 components. Every black component not touching
C can be changed to white without affecting a pin or label-one edge. Thus
one may restrict attention to components meeting this finite critical set.

For each c in C, breadth-first search its E0 component, but stop immediately
when M+1 distinct vertices have been found. There are two outcomes:

- Search exhausts with <=M vertices: record the entire finite component and
  its weight, the number of its vertices. Deduplicate identical components.
- Search reaches M+1 vertices: every seed of mass <=M must color this whole
  component white. Its remaining size and possible mergers with other such
  large components need not be decided.

Each search terminates after inspecting at most M+1 vertices and their
finite neighbor sets. A finite component of size <=M is known completely,
so membership of every critical vertex in it is exact. All other critical
vertices are known to be in components too large to color black under M.

Make one binary variable for each recorded small component. Substitute zero
at every large-component critical vertex. Impose all E1 XOR equations and
pins. The cost of a one-valued variable is its component weight. Decide the
finite weighted XOR system with total cost <=M. This may be done by finite
enumeration, or by taking the cheaper consistent orientation of each XOR
constraint component after propagating pins. Return the union of all
one-valued small components.

The returned board obeys every E0 edge by complete component closure, every
E1 edge by construction, and all pins. IJ and the exact graph equivalence
therefore prove that its ENTIRE prescribed trajectory is legal. Conversely,
any realizing seed of mass <=M can be pruned as above and appears among the
finite assignments, proving completeness.

## Explicit radius bound, not an assumption

Let L be the largest infinity norm of a permitted displacement and R the
largest infinity norm of a critical vertex. After pruning, every vertex in
a seed of mass <=M is connected to C within its black component by a simple
path of at most M-1 edges. Hence it lies in the box of radius R+(M-1)L.
The bound is deduced from the frame constraints and M, not guessed from
simulation. If C is empty the empty seed is a solution. M=0 is handled
separately. Pins and inconsistent label-one loops remain explicit.

## Scope

There is no computable bound on M asserted in terms of the presentation.
The general parity-graph hardness example shows why the unbounded-mass
problem cannot be settled just by this bounded-component algorithm.
Enumerating M recognizes finite realization and returns the least possible
mass once a model exists, but may run forever on a negative instance.

This is stronger than supplying the whole finite seed in advance, but it
still concerns a fixed morphic path presentation. It does not decide general
finite-seed capture or certify a nontrivial counterexample. The all-level
automatic graph constructor is not yet integrated into an executable solver.

The generic bounded-component implementation bounded_seed_graph.py has also
passed independent exhaustive review:49,152 complete three-vertex labelled
graph comparisons and44 infinite-line/remote-component controls. This signs
the graph solver, not the still-unimplemented ant graph compiler.
