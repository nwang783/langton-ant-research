# The general parity-graph target has a halting barrier

2026-10-23 03:44 UTC. Separate analytic observation independently signed on 2026-10-23 03:50 UTC.
This is NOT a reduction of halting into finite-seed Langton-ant behavior.

## 1. A narrowly stated graph problem

Input: a finite displacement set D subset Z², Presburger guards specifying
undirected zero-labelled edges {u,u+d}, and one distinguished vertex v0.
Question: is there a finite subset B of Z² containing v0 such that every
zero-edge has either both endpoints in B or both outside B?

Equivalently, is the connected component of v0 finite? A finite B is a
checkable certificate: for every u in B, test its finitely many possible
neighbors and require each actual neighbor in B. Thus the problem is c.e.

## 2. Halting reduces to this general graph problem

Use a deterministic reversible two-counter program, with a designated source
configuration having no predecessor and with the simulated halting state
having no successor. Computation universality of reversible two-counter
machines is established by Kenichi Morita, “Universality of a reversible
two-counter machine”, Theoretical Computer Science168(1996),303–320,
https://doi.org/10.1016/S0304-3975(96)00081-3.
The source convention is explicit in the higher-counter reversible
simulation in Theorem3.1; replacement by the disjoint reversible two-counter
instruction simulations preserves the no-incoming start state. Legal
instruction simulations terminate, so an infinite simulated computation
remains infinite, rather than getting stuck inside a macro.

Encode a configuration(q,a,b), with q in{0,...,m-1} and a,b>=0, as

    (x,y)=(m*a+q,b).

Each unit increment/decrement/test instruction becomes a fixed-displacement
edge. Its displacement is

    (m*delta_a + q'-q, delta_b),

and its guard is a combination of x mod m=q, nonnegativity, and zero/positive
counter tests. These are Presburger. Add the reverse of each edge to make
the graph undirected. Other lattice vertices may be isolated.

Determinism and reversibility give degree at most two. The chosen source has
no incoming edge, so its component is exactly its forward computation path.
No configuration can repeat: a first repetition would give either a
predecessor of the source or two predecessors of another configuration.
Therefore this component is finite exactly when the simulated computation
halts. Pinning b(v0)=1 forces the whole component black. A finite-support
solution exists exactly in the halting case.

Consequently the general bounded-displacement Presburger zero-edge problem
with one black pin is c.e.-complete, already at degree two and with no
label-one edges. Its negative instances are not generally recognizable.

## 3. What this says about the ant bridge

The preceding file maps a finite-power ant path presentation into a very
special automatic parity graph. The present reduction shows why first-order
automatic descriptions and local bounded degree alone do not settle the
remaining finite-component question.

It does NOT prove that the hard counter-machine graphs occur among graphs
produced by ant refinements. Establishing that reverse realization, while
retaining all typed geometry and literal ant chronology, would be the actual
missing finite-support compiler. It has not been supplied. A reduction
FROM ant realization TO a hard graph problem is not a hardness proof for
ant realization.

This distinguishes the real finite-fuel issue from the already established
undecidability phenomena with arbitrary infinite pre-coloured boards.

## 4. Update after the exact forced-seed theorem (05:16 UTC)

The previously missing reverse realization is now known to be impossible if
it is required to be a computable many-one reduction into the fixed finite-
power presentation class of JE/JF. The signed `automatic_forced_seed.md` and
`automatic_forced_seed_finite_power.md` give a terminating arbitrary-mass
finite-seed realization decider for that class. Composing a purported faithful
compiler with this decider would decide the c.e.-complete graph problem above,
a contradiction. Thus Section3's missing compiler is not merely unimplemented
under those exact fixed-presentation restrictions.

This does not refute a reduction through a broader class of actual ant
trajectories. In particular no faithful compiler into arbitrary finite seeds
has been supplied or excluded. The separately signed fully expansive fixed
presentation realization decider likewise prevents using that precise
structured target for a faithful undecidability reduction. These are barriers
to particular proof architectures, not decidability of finite-seed capture.
