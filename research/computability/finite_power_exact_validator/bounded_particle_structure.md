# Bounded integer Laurent transfer implies eventual affine particles

2026-10-23 03:34 UTC. Analytic deduction independently signed on 2026-10-23 03:50 UTC.
No ant model is constructed. The rational/semilinear ingredient is established
literature, not a newly claimed general algebraic theorem.

## 1. Finite-valued rational coefficient arrays are semilinear

Let f(n,x,y) be an integer array with finitely many values. Suppose, after
an affine spatial shift making the support nonnegative, its multivariate
generating function is rational with an integral polynomial denominator
whose constant term is1.

Choose distinct primes p,q larger than the diameter of the finite value set.
Reduction modulo either prime is injective on that set. The rational-series
Cartier construction in the accompanying theorem, with numerator transition
P->Lambda_e(P H^(p-1)) in characteristic p, makes each coefficient-value set
p-automatic; likewise it is q-automatic. The multivariate Cobham–Semenov
theorem therefore makes every such set Presburger-definable, hence semilinear.
Undoing the affine spatial shift preserves this conclusion.

This is the finite-valued version of the rational 0/1-support fact in Bell
and Chen, Proposition4.3, “Power Series with Coefficients from a Finite Set”,
https://arxiv.org/pdf/1606.04986. Their proof uses the same finite-field and
Cobham–Semenov route. The hypotheses above avoid issues with a denominator
vanishing on reduction. There is no assertion that rational F2 arrays alone
are semilinear: Pascal parity is a countercontrol.

The representation can be recovered effectively under the finite-value
promise: build one prime-base automaton for each value, enumerate Presburger
formulas, translate each into that same base, and test automaton equality.
Semilinearity guarantees eventual success. This is not a practical bound.

## 2. Uniformly bounded support fibers force affine tracks

Assume also that at every n the number of nonzero spatial coefficients is
bounded by one constant K. Write each nonzero-value set as a finite union of
linear sets

    b + N v_1 + ... + N v_j  in N^3,

using the shifted nonnegative coordinates. Any nonzero generator with zero
time component would give an infinite spatial fiber, impossible. Thus every
nonzero generator has a positive time component.

If two generators v,w have different spatial velocity ratios
v_space/v_time and w_space/w_time, then at the common time

    b_time + N*v_time*w_time

the choices j*w_time copies of v and (N-j)*v_time copies of w, j=0,...,N,
give N+1 distinct spatial points. This contradicts the uniform fiber bound.
Hence all generators in one component have the same rational velocity.
At each allowed time that component has just one point on one affine track.
Its allowed times form a translate of a finitely generated additive
subsemigroup of N, and are eventually periodic (all sufficiently large
multiples of their generator gcd occur).

Split into one common residue period for all components. On each residue
class, beyond a finite threshold, the array is a finite sum of monomials
with coordinates affine in the residue counter and fixed integer weights.
Different affine tracks intersect only finitely often unless identical;
deduplicate identical representations of the SAME coefficient set and enlarge
the threshold past the exceptional collisions. Do not sum duplicate set
representations. Distinct coefficient-value sets are disjoint. Undoing the original affine spatial shift leaves affine tracks.

Therefore EVERY uniformly l1-bounded integer Laurent-polynomial sequence
with the rational shifted generating function above is eventually a finite
collection of affine particles on residue classes. Signed cancellation is
fully allowed: the theorem concerns the final coefficient array, not a
nonnegative transfer representation.

## 3. Application to finite-power ant refinements

For a fixed finite-power typed substitution, the SIGNED occupation vector
F_s(r) uses the same periodic Laurent matrices as the parity construction,
but over Z and with initial entry +1 for R and−1 for L. Its grouped-phase
generating functions are rational after a linear spatial shift.

If a refined word is ant-legal, consecutive turns at each repeated read
cell alternate. Thus every signed occupation coefficient is in{−1,0,1}.
For a genuine rooted model, all reachable refined blocks are actual factors,
so their occupation arrays are semilinear by Section1. Canonical input and
output board templates for a finite B are then Presburger, not just automatic.
This supplies completeness of the earlier supplied-Presburger-template
format for genuine finite-power models, without assuming first-read colors
are directly semilinear.

At root checkpoints suppose total signed charge is uniformly bounded.
Finite initial fuel then bounds the l1 norm of F_root(r), as in the signed
Fourier bridge. Section2 implies that the complete checkpoint black boards
are eventually a fixed finite part plus finitely many affine moving particles,
on each residue class of refinement depth.

Every nonzero-velocity NEGATIVE track is impossible: a negative occupation
coefficient can occur only at a cell black in the fixed initial seed. Thus
all genuinely moving particles have positive coefficient+1. This does not
exclude two-sided or spatially two-dimensional collections of positive
particles. In particular, affine-particle structure alone is not a highway
proof and does not improve the known mass-five lower bound.

## 4. Scope

The affine-particle conclusion requires a UNIFORM checkpoint charge/l1 bound;
finite-valued coefficients alone give only semilinear sets with possibly
unbounded fiber size. The current argument uses a fixed finite controller
and eventually periodic spatial matrix powers. It does not apply to changing
directive sequences or unrestricted finite-seed ant trajectories.

This is a structural necessity and an existence theorem for effective
representations under the stated promises. No extraction has yet been run
for a successful nontrivial ant model, because none is known here.
