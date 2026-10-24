# Deciding a supplied flat finite-prefix budget falsifier

23 October 2026. Analytic proposed application of retained Presburger and
uniform-fiber machinery. Not an executed general solver or an accepted pump.
Universal capture and uniform fixed-mass defect budgets remain unresolved.

## 1. Why final recovery is not needed for this target

Suppose for every n>=n0 a finite seed B_n, with one UNIFORM initial black-mass
bound m, executes a finite prefix w_n containing an unbounded number of actual
adjacent-bad-ten K events. There is no need to determine the unmodified seeds'
entire subsequent futures in order to refute the uniform budget target.
The independently signed twelve-cell completion produces bi-standard seeds
of mass at most m+12 preserving each finite prefix and ten preceding turns.
Their K counts are therefore unbounded:

    b(m+12)=infinity.

This does NOT refute universal capture. The prefixes can begin with increasingly
long standard flights, so the defects can escape to later times in a bounded-
mass compact limit. No claim of one finite seed running every w_n is made.

A concrete architecture is a standard producer H^n, a fixed finite turn cap C,
then n copies of a nonstandard periodic wake rewriter P. Here P must have
positive cyclic K cost kappa(P); merely being nonstandard is not enough.
If kappa>0, n repeated copies contain at least n*kappa-10 K events wholly
inside them. Initial/final windows change only a bounded number.

Infinite prepared-wake legality of P is not a finite-seed launch proof. The
producer, cap and all rewriter reads must be compatible on ONE initial finite
board for each n, with a uniform bound on its initially black cells.

## 2. Exact flat-pump decision problem

Supply fixed finite words A,H,C,P,B and a launch pose. Assume H and P restore
their incoming headings. Fix n0>=1 and define

    w_n=A H^n C P^n B, n>=n0.

The words need not be nested. The seed may depend on n. The following are
effectively decidable:

1. Every w_n is ant-legal on some board.
2. If so, their exact MINIMUM initial black masses are uniformly bounded.

In the bounded case the procedure returns a numerical uniform bound and an
eventually affine, residue-class finite seed family realizing every w_n,
plus the finitely many exceptional n. In the unbounded case it returns a
semilinear witness yielding linearly growing required mass along an arithmetic
subsequence. This is a decision theorem for a SUPPLIED flat presentation,
not for existence of any presentation and not for arbitrary seed capture.

The algebraic uniform-fiber test and affine-track conclusion are retained
results in `../computability/finite_power_exact_validator/finite_value_decider.md`
Section 2 and `bounded_particle_structure.md` Section 2. They are not claimed
as new general algebra here. The application differs from the existing rooted
finite-power solver: different n may intentionally use different seeds, and no
single infinite rooted ant is asserted.

## 3. Presburger read and legality relations

For each fixed word, compute its literal phase positions, headings and turns.
A copy of H has phase positions q_H(i)+j*d_H and time |A|+j*|H|+i,
with 0<=j<n. C begins at the position after A plus n*d_H. A copy of P has
position equal to that C endpoint plus j*d_P, with 0<=j<n, and time
|A|+n*|H|+|C|+j*|P|+i. The final fixed word B has affine starting position
and time. All coefficients are constants; no variable multiplication occurs.

Thus Read(n,t,x,y), L(n,t) and R(n,t) are effective Presburger relations.
For one physical cell, consecutive requested reads must alternate R,L.
A violation is exactly a tuple n,t1,t2,x,y with

- t1<t2 and both times read (x,y);
- both requested letters equal;
- no intermediate t reads that same cell.

The existence of such a tuple is a Presburger sentence and is decidable.
If absent, every w_n is legal. Its canonical minimum input is exactly

    F(n,x,y) iff some FIRST read at (x,y) requests L.

The first-read condition is a bounded-time existential followed by the
Presburger assertion that no earlier read is at that cell. The resulting F
is effective Presburger, and each n-fiber is finite. Its cardinality is the
exact minimum initial black mass, not current mass at the rewriter entry.

## 4. Exact uniform-fiber test and seed extraction

Obtain an effective finite union of linear sets for F. Spatial coordinates
can first be shifted by a known affine function of n to make them nonnegative:
all phase paths have coordinate magnitude O(n). Undo the shift afterward.
Write one linear component as

    b + N*v_1 + ... + N*v_k in N^3,

with the first coordinate n. Any nonzero period vector with zero n-coordinate
would produce an infinite fiber; this cannot occur for the finite-prefix
relation. Ignore zero vectors. Every remaining period has positive n-component.

If two periods v,w have different spatial velocity ratios, then at

    n=b_n+N*v_n*w_n

the combinations j*w_n copies of v and (N-j)*v_n copies of w, j=0,...,N,
produce N+1 distinct initial-black cells. Hence the masses are not uniformly
bounded, and this displays an explicit linear lower bound on an arithmetic
subsequence.

If no component has such a pair, each contributes at most one spatial point
at every n. The number of linear components is therefore a uniform mass bound,
regardless of overlaps. Deduplicate identical points; never sum overlapping set
representations as if they were separate black cells.

Each component lies on one rational affine spatial track, and its allowed n
values form a translate of a finitely generated additive subsemigroup of N.
Those allowed times are eventually periodic. Split into a common residue
period and enlarge the finite threshold to cover the finite exceptions.
This gives an explicit eventually affine finite seed family. Its exact
realizability follows from the first-read construction and the legality test,
not merely signed occupation or an endpoint XOR.

All of these steps are effective mathematical algorithms. No practicality or
implemented general semilinear extraction is claimed.

## 5. Consequence for the two-block wake-rewriter search

Given H=standard104 and any fixed C,P, one can therefore decide whether the
finite words H^n C P^n are all legal and have uniformly bounded first-L fuel.
If the answer is YES and kappa(P)>0, the twelve-cell completion rigorously
refutes fixed-mass budget finiteness. It does not decide the HC conjecture.
If  the failure is either an explicit chronological conflict or an explicit
unbounded initial-fuel obstruction, not absence of an observed simulation.

The missing substantive object is one accepted fixed cap/rewriter pair C,P.
No such pair has been found here. The reverse-complement104 P has kappa52,
but the retained complete-history union theorem forces

    initial mass >= 4n-|C|-238

for one producer standard block followed by C then n reverse periods.
The ten-turn P=LLLLRLRRRR has kappa1, but its retained complete-history bound
forces

    initial mass >= n-|C|-175.

The constants here allow the fixed cap as individual other steps and use one
producer block. They are applications of existing supply exclusions, not new
bounds. They show why increasing a standard flight's length cannot pay these
two particular consumers from bounded initial fuel. Different output-profile
rewriters remain outside those exclusions.

This provides a concrete, checkable construction search rather than treating
arbitrary long flights or a finite count of prepared components as a proof of
bounded interactions. It deliberately targets a uniform-budget countercontrol,
not a finite-seed noncapturing orbit.
