# Deciding a fixed coefficient range, then exact bounded occupation support

2026-10-23 03:55 UTC. Analytic corollary independently signed on 2026-10-23 03:57 UTC.
This is an algebraic filter for supplied finite-power path presentations,
not an ant model, general highway theorem, or unknown-seed decider.

## 1. A prescribed finite coefficient set is decidable

Input is an integer rational formal power series F in d variables, represented
by P/H with integral polynomials and H(0)=1, and a specified finite set S of
integers. Decide whether EVERY coefficient of F belongs to S.

Run these two searches in parallel:

1. Enumerate coefficient indices by increasing total degree. Compute the
   exact integer coefficient recursively from H F=P. Halt NO upon finding
   a coefficient outside S.
2. Enumerate finite disjoint unions of simple linear sets labelled by S.
   A simple linear set is b+N v_1+...+N v_j, where all vectors are nonnegative,
   the nonzero v_i are linearly independent over Q, and j may be zero.
   Require all components to be pairwise disjoint, checked by Presburger
   arithmetic. If zero belongs to S, unlisted points receive value zero.
   Otherwise also require that the components cover N^d. Their labelled
   rational generating function is the finite sum

       sum_components label * X^b / product_i(1-X^v_i).

   Compare this rational function EXACTLY with F by polynomial cross
   multiplication. Halt YES and return the decomposition if equal.

The YES branch is sound because independent periods make each component's
monomial representation unique, and disjointness prevents coefficient
multiplicity. The NO branch is sound by construction.

If all coefficients belong to S, the finite-valued rational-series theorem
in bounded_particle_structure.md says every coefficient-value set is
semilinear. Every semilinear set has a finite disjoint decomposition into
simple linear sets. Therefore a certificate occurs in search2. If not,
search1 finds a witness. Exactly one branch must terminate, proving a total
algorithm with no finite-value promise and no complexity claim.

The semisimple decomposition fact is stated explicitly on page5 of Kevin
Woods, "Presburger arithmetic, rational generating functions, and
quasi-polynomials", Journal of Symbolic Logic80(2015),433-449:
https://www2.oberlin.edu/faculty/kwoods/research/Presburger_full.pdf .
Its effective construction need not be used here: enumerating all proposed
simple-set lists and checking the finite Presburger/rational certificates
is enough. The finite-valued rational-series ingredient is Bell–Chen
Proposition4.3 with its finite-value extension already audited separately.

This does NOT decide arbitrary positivity or whether the range is finite
without a specified bound. The latter has no complementary finite witness.

## 2. Exact uniform-fiber boundedness after the range check

Suppose the indices are (r,x,y) and the coefficient range check passes.
For each nonzero-labelled simple component inspect its period vectors.
A nonzero period with zero r-coordinate produces infinitely many spatial
points in one time fiber. Two positive-r periods with distinct ratios
(v_x/v_r,v_y/v_r) produce arbitrarily many spatial points at one time by
cross-multiplying their r-coordinates. Either certifies UNBOUNDED support
fiber size.

If neither occurs, each component contributes at most one spatial point
at every r, so the total fiber size is bounded by the number of nonzero
components. Thus this necessary-and-sufficient test is effective from the
returned decomposition. Since the nonzero coefficient values form a fixed
finite set of nonzero integers, uniform support-fiber boundedness is
exactly uniform coefficient l1 boundedness.

In the bounded case, the numerical-semigroup/residue construction in the
particle note gives an effective finite collection of eventual affine
tracks. Duplicate set representations are removed, never summed as if they
were distinct coefficients. Finite isolated points remain explicit.

## 3. Application to finite-power refinements

Every grouped-phase signed occupation array of a supplied finite-power
refinement has the rational form required above, after a known linear
spatial shift. Apply the total range test with S={-1,0,1} to each reachable
letter and genuine phase. A failure is an exact impossibility certificate
for any ant realization of the corresponding block: a legal block's turns
at each cell alternate, so its total excess is only -1,0,1.

If every check passes, all signed occupation arrays are extracted as
Presburger sets. Their parity is therefore Presburger too; canonical frame
checks and the unknown-seed XOR graph can now be represented in Presburger
arithmetic rather than only base-two automatic arithmetic. This is an
exact stronger representation after a necessary filter, not chronology
itself. The general zero-component finiteness barrier remains even for
Presburger graphs, as the separate Morita reduction demonstrates.

For any fixed prefix family whose checkpoint total charge is known to be
uniformly bounded, finite initial fuel requires uniformly bounded signed
occupation l1. Section2 decides that algebraic necessity COMPLETELY, unlike
checking only selected Fourier characters. If it passes, it extracts the
only possible affine-particle occupation structure. It still does not
certify that the path is ant-legal or that one finite seed realizes it.

No integrated enumerative coefficient-range solver or semilinear extractor
has been run here. The claim is a terminating mathematical decision
procedure with finite checkable positive and negative certificates.
