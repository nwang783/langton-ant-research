# Coarse-vertex first-L obstruction for anisotropic direction substitutions

2026-10-23 00:00 UTC. Status: Sections 1–5 independently analytically audited on 2026-10-23 at 00:04 UTC.
No successful finite-support model or universal theorem is asserted.
This strengthens the scalar coarse-vertex test by allowing the fine turn at a
coarse vertex to change, provided its finite heading pair returns cyclically.

## 1. Direction-substitution hypotheses

Let phi substitute four absolute movement letters E,N,W,S by words of one ODD
length k>1. Assume:

1. phi(-d)=-phi(d), letterwise half-turn covariance.
2. Every image alternates horizontal/vertical move axes, starting on the same
   axis as d. This is the geometry of any used image in an aligned odd-length
   quarter-turn path.
3. Its total displacement is A d, for an expansive integer matrix A.
4. There is a fixed initial letter, giving an infinite substitution fixed point.
5. Every INTERNAL prefix displacement q_(d,j), 0<j<k, is outside A Z^2.

The integrated positions obey p(kn)=A p(n) and
p(kn+j)=A p(n)+q_(d(n),j). The candidate still needs every ordinary read to be
chronologically color-consistent. Assume that legality only for the implication
below; a finite local contradiction is already sufficient to reject a candidate.

If rho(A)<k, these hypotheses cannot produce a finite-support ant.

## 2. First visits propagate exactly

By hypothesis5, the path occupies A Z^2 at precisely the times divisible by k.
Since A is injective,

    n is a first visit to p(n) iff kn is a first visit to A p(n).

Indeed any earlier read of A p(n) must occur at km and then has p(m)=p(n), and
conversely an earlier coarse read scales to an earlier fine read. This equivalence
iterates at every power of k. It is a statement about the entire actual path,
not merely about one macro's internal consistency.

## 3. A first L cannot disappear permanently under scaling

Let F(d) and L(d) be the first and last movement letters of phi(d). Because k
is odd, both have the same axis as d. Half-turn covariance gives F(-d)=-F(d)
and L(-d)=-L(d). Hence each is a permutation of the four movement directions:
on each opposite pair it is either the identity or the swap.

For every n>0, the incoming/outgoing movement pair at read time n transforms as

    (d(n-1),d(n)) -> (L(d(n-1)), F(d(n)))

at read time kn. This is a permutation of the eight perpendicular direction
pairs. Therefore some positive power restores the original pair. If read n was
L, reads k^(jr)n are L for every j>=0, for some r>=1. Section2 says all of those
reads remain first visits.

If p(n)!=0, the cells A^(jr)p(n) are all distinct. Otherwise equality of two
would make a nonzero vector fixed by a positive power of expansive A, impossible.
Thus any nonzero first-L cell forces infinitely many initially black cells.

This is stronger than requiring every scaled first L to remain L immediately.
The intermediate turns may change. A finite cyclic return of the heading pair
is enough to force infinite first-L support.

## 4. The only finite-support possibilities collapse to blank capture

If the candidate is realized from finite support, Section3 leaves no initially
black visited cell except possibly the origin. The unique minimal seed is
therefore either empty or {0}. The latter becomes an empty board after its first
L read and move, so it is a rigid copy of the certified blank orbit from then on.
Both have a nonzero standard104 asymptotic drift.

On the other hand rho(A)<k gives globally sublinear displacement, by the exact
matrix recurrence theorem. This contradicts that drift. Therefore the stated
subcritical class has no finite-support realization, at ANY image length.

Unvisited extra black cells make no difference. This is an actual finite-support
obstruction, not a conclusion from testing a long finite prefix.

## 5. A more general automaton statement

The same proof works without a four-direction substitution if an expanding
same-path inflation p(kn)=A p(n) has these two properties:

- p(t) in A Z^2 if and only if k divides t, so first visits propagate exactly.
- The actual turn stream has a MOST-significant-digit-first finite-state base-k output presentation whose
  zero-digit transition is a permutation on its accessible states.

For a first-L time n>0, reading additional zero digits cycles its output state;
therefore turns at k^(jr)n return to L infinitely often. The same origin exception
and blank reduction apply; the nonexistence conclusion additionally retains rho(A)<k. A partial permutation suffices if the specific
first-L state's zero orbit is cyclic, rather than merely eventually cyclic.

Thus a separated finite-support candidate with nonblank behavior must allow its
first-L states to be TRANSIENT under zero-digit refinement. A noninjective finite
control can permit that and is not excluded here. Internal reads in A Z^2 can
also destroy the first-visit propagation. These are concrete degrees of freedom
for the next construction class, not sufficient conditions for success.

## Scope limitations

The result does not cover arbitrary direction substitutions whose images read
coarse-lattice cells internally, even if those internal reads appear harmless.
It does not infer that a two-cycle of first letters defines the same one-phase
fixed point; such candidates require a separately verified squared substitution
or a phase-coupled first-visit argument. It does not cover nonexpansive A, critical
rho(A)=k, general recurrent paths, or all finite-state ant candidates.

## 6. Reviewed strengthening: no subcriticality assumption is necessary

Independently analytically reviewed, 2026-10-23 00:07 UTC. This supersedes the
rho(A)<k restriction in the nonexistence conclusions above, but not the other
hypotheses. It applies both to the odd direction-substitution case and the
separated MSB zero-permutation case, for EVERY k>=2.

Separation and injectivity of A forbid ANY positive return to the origin.
Indeed, if t is the least positive time with p(t)=0, then p(t) in A Z^2 forces
t=kn. The equality 0=p(kn)=A p(n) gives p(n)=0 with 0<n<t, a contradiction.

Sections3 and5 already force every finite-support realization to have minimal
seed empty or {origin}, without using rho(A)<k. Both such trajectories return
to the origin after exactly four moves: RRRR or LRRR. Thus they contradict the
no-positive-return conclusion. No known-highway theorem or velocity estimate
is needed. The matrix remains expansive in the main statement to ensure the
nonzero scaled first-L sites are distinct; more generally that particular
orbit-separation condition would suffice there.

## 7. Separation survives powers; an odd axis-swapping application

Independently analytically reviewed,2026-10-23 00:45 UTC. This supplies the
explicit root-cycle treatment required by the scope warning above.

Let every image phi(d) have endpoint A*d and no internal read in A Z^2.
Then phi^r(d) has no internal read in A^r Z^2, for every r>=1.
For r=2, an A^2-lattice point is also in the A-lattice. Every translated
fine block starts in A Z^2, so separation forces such a point to be at a
block boundary. It is then A times a point of phi(d). Injectivity of A
reduces membership in A^2 Z^2 to membership of that coarse point in A Z^2,
which is possible only at the image endpoints. Induct on r.

Consequently first-letter cycles may be handled by taking their root-cycle
power, provided that power has the permutation and heading-axis hypotheses
of the preceding theorem. This makes no unjustified single-phase assertion
about the original substitution.

For the odd axis-swapping half-turn family k=7,A=3I, every east image has
movement axes V,H,V,H,V,H,V, exactly three east moves, no west move, and
two north/two south moves. Its internal reads with x=0 or x=3 have y=+1
or-1; all other internal reads have x=1 or2. Hence it avoids3Z^2 internally.
Rotate for the other directions. First and last direction maps are
axis-swapping permutations; the root cycle has length2 or4. The corresponding
power is axis-preserving and separated, with matrix3^r I. Section6 therefore
excludes every finite-support rooted limit in this family. No finite inventory
or simulation is a premise of this exclusion.

## 8. Origin-only internal overlaps are also impossible

2026-10-23 00:51 UTC; independently signed via the stronger vertex-only
theorem in audit GN at00:59 UTC. Here the images may return to their own
origin internally. The
hypothesis is only

    every internal image read lying in A Z^2 is the origin0.       (Z)

Keep an expansive integer A, a rooted pure inflation p(kn)=A p(n), and
permutation first/last movement maps F,L. A root-cycle power is allowed
as in Section7. No rho(A)<k restriction is required.

Condition(Z) still gives exact first-visit propagation at aligned boundaries.
If A*p(n) was read before time k*n, it lay in an earlier image block m<n.
Its offset in that block belongs to A Z^2, hence is0 by(Z). Therefore
p(m)=p(n). Conversely a prior coarse visit gives a prior aligned fine visit.
Thus First(n) iff First(k*n), although non-first origin returns inside a
block are now allowed.

The incoming/outgoing pair at a nonzero first read transforms by(L,F).
Because both maps are permutations, a first-L pair returns after finitely
many iterations. Expansiveness makes the corresponding nonzero sites
A^j*p(n) distinct. As before, any nonzero first-L site forces infinitely
many initial black cells. Every finite-support realization therefore has
minimal initial support empty or{origin}.

These two actual ants return to the origin at time4, with words RRRR and
LRRR respectively. Pure inflation consequently forces

    p(4*k^r)=0 for every r>=0.

But the independently certified blank-board trajectory eventually follows
the nonzero-drift standard104 highway, so it visits any fixed point only
finitely often. The origin-black trajectory becomes an entirely white
board immediately after its first read, at a translated and rotated pose;
it therefore has the same eventual nonzero-drift property. Contradiction.
This use of the explicit known blank-board trajectory is not an invocation
of the open universal capture conjecture.

Finally(Z) is closed under substitution powers. An internal A^(r+1)-lattice
point lies in the A-lattice, so its fine-block offset is0. Dividing the
remaining aligned point by A reduces to an internal A^r-lattice point of
the coarser word, which is0 by induction. Thus the result also covers
fixed or finite root cycles after passing to their cycle power, whenever
the first/last maps remain permutations.

An early internal visit to the NONZERO endpoint A*d is not allowed by(Z).
Endpoint loops need a separate first-arrival/turn analysis; they cannot be
silently treated as origin loops.

The subsequently signed generalization is
`../causal_reduction/matrix_candidates/vertex_only_overlap_obstruction.md`:
it allows both origin and endpoint loops and replaces the final-heading
context by the actual first-endpoint-arrival context, with an exact parity
correction. Its stated first/first-arrival permutation hypotheses cover
Section8, but not arbitrary nonpermutation endpoint contexts.
