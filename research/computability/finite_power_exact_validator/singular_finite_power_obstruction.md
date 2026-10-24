# Singular finite-power spatial refinements cannot grow legally

2026-10-23 05:40 UTC. Analytic theorem independently signed as audit JP at05:42 UTC.
It removes uniformity and all symmetry assumptions from the earlier singular
bounded-power footprint obstruction.

## Statement

Let phi be a fixed finite nonerasing substitution on states representing unit
square-grid movements; extra finite decorations are allowed. Suppose its exact
geometric images satisfy net(phi(s))=A v_s for one singular integer matrix A
with finitely many powers. Any iterated words under consideration must be
geometrically interpreted with the usual additive refinement offsets.

No growing rooted power-limit of phi is a Langton-ant trajectory, on ANY
initial coloring. No image-length bound, uniformity, charge condition, heading
preservation, physical-state uniqueness or finite-support assumption is needed.
Only the actual rooted phase must be a physical ant path; intermediate root
phases need not be legal.

Together with the separately signed finite-order theorems this sharpens the
scope of possible fixed finite-power constructions. This note itself concerns
SINGULAR matrices, and makes no assertion about general invertible decorated
nonuniform controllers.

## 1. Reduce to an idempotent geometric matrix

Take a power defining the actual fixed growing rooted word. Since A has finite
powers, take a further common power P satisfying P²=P. For example choose an
exponent at least the supplied preperiod and divisible by the eventual period.
The matrix remains singular, and the exact refinement geometry persists.
Denote the resulting fixed substitution again by phi.

If P=0, every depth-r read position lies in one fixed finite local-offset set:
all higher terms in the nested sum are zero. A growing legal root prefix is
then impossible by finite-domain escape. Hence assume rank(P)=1.

Every depth-r read position has the form

    b0+P b1+...+P b_(r-1),

where the b_i come from one finite local-offset set. It therefore lies in a
fixed-width strip about im(P), with longitudinal extent O(r).

The already signed strip argument gives a polynomial-in-r upper bound on the
length of any legal interval in that footprint: fixed-height rectangular
escape for an axis-parallel strip, or the bounded-weight strict oblique clock
for an oblique strip. These are exactly the ingredients of
`causal_reduction/matrix_candidates/halfturn_matrix_dichotomy.md`, Section6,
which explicitly require neither symmetry nor finite initial support. For an
infinite background, copy its colors on this finite footprint to a finite board.

## 2. Every reachable incidence component has Perron value at most one

A reachable irreducible incidence block with Perron value lambda>1 contributes
at least c lambda^r letters to some depth-r reachable image. This follows by
comparison with its positive Perron eigenvector; the component may have a
period, but its total row sums still have this exponential lower bound.
The image appears inside a root power with only a fixed extra depth.

That contradicts the polynomial strip-duration bound. Thus every reachable
recurrent SCC has Perron value one. A recurrent irreducible nonnegative integer
matrix of Perron value one is a single directed permutation cycle, with exactly
one internal child occurrence per state. Transient singleton SCCs have no cycle.

Take one more substitution power divisible by all these cycle lengths. This
does not change P or the actual fixed root. Now every cyclic state s has
exactly one self occurrence and every other child lies strictly downstream.
Transient states remain in acyclic parts of the condensation graph.

## 3. A lowest emitting cycle forces a parallel repeated block

Call a cyclic state emitting when its image contains something besides its
unique self occurrence. Such a state exists: the growing prolongable root is
cyclic, and if it had no extra child its image would be just itself and its
root powers would not grow.

Choose an emitting cyclic state s with no emitting cyclic state strictly below
it in the reachability DAG. Write

    phi(s)=U s V,

where at least one of U,V is nonempty. Every cyclic state reachable from U or V
has image equal to itself. Every other reachable state is transient, so after
a finite common depth N its image consists solely of these identity states.
Consequently there are fixed words U*,V* over identity states such that

    phi^j(U)=U*,    phi^j(V)=V*       for all j>=N.

Nonerasing ensures U* or V* is nonempty. Expanding the displayed recursion
shows that phi^(N+r)(s) contains (U*)^r or (V*)^r as a contiguous factor.
The precise central finite word and the reverse order on the suffix do not
matter, because the eventual repeated factors are identical.

For every identity state d, exact geometry gives P v_d=v_d. Its physical unit
movement therefore lies in im(P). If im(P) is oblique, it contains no compass
unit vector, so no such identity state exists, already a contradiction. If
im(P) is axis-parallel, every identity state's movement is parallel to that
one axis, possibly with opposite signs.

Thus any nonempty U* or V*, repeated twice, contains two consecutive movements
on the same axis. But every physical ant path turns by ninety degrees at every
read. This contradicts the fact that each reachable refined image is a factor
of the actual ant path. The remaining polynomial-growth case is excluded.

## Limits and relation to decidability

This proof uses both finite-power rank-one geometry and the finite fixed
substitution. It does not rule out arbitrary ant motion in an infinite strip,
or nonstationary directives, or general rank-one expanding matrices.

The exact finite-seed decision theorem JE/JF remains valid. This new theorem
says its singular finite-power growing inputs are always  even with finite
context decorations. The surviving fixed finite-power construction problem is
therefore invertible finite-order geometry with decorations not already covered
by the physical-state/direction obstructions. No positive construction follows.
