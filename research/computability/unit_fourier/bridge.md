# Exact Fourier fuel tests for nonexpanding turn refinements

2026-10-23 02:12 UTC. Analytic bridge and frozen implementation controls
independently signed as audit HN. This is a necessary test, not a decision procedure.

## 1. Model and the finite-support invariant

Let phi(R)=u and phi(L)=v be two nonempty finite words, not necessarily of
the same length. Write l_r=|phi^r(R)|. The initial
heading is north, and R/L mean clockwise/counterclockwise quarter turns,
followed by one unit move. Suppose each image preserves its coarse final
heading and has displacement a times its coarse displacement, where

    a in {1,i,-1,-i}.

Assume exact signed-charge preservation: e(u)=1 and e(v)=-1. The independent
all-length reduction in ../../causal_reduction/unit_scale/README.md shows
why this charge condition is necessary for an ant-legal rooted word in the
UNIFORM unit-scale two-image model. That reduction is not asserted here for
unequal lengths. The present theorem may instead take charge
preservation directly as an explicit hypothesis.

For a refined word phi^r(R), let its signed occupation Laurent polynomial be

    F_r(X,Y)=sum over reads t [turn(t)] X^(p_x(t)) Y^(p_y(t)),

where turn(R)=1 and turn(L)=-1. If the word is an actual ant prefix, then

    [X^x Y^y] F_r = 1_(B_(l_r))(x,y) - 1_(B_0)(x,y).       (1)

This is exact: at one cell white-right adds a black bit and black-left
removes it. It needs literal chronological ant legality, not only parity.
Charge preservation implies |B_(l_r)|=|B_0|+1. Thus, writing m=|B_0|,

    ||F_r||_1 <= 2m+1,                                  (2)

UNIFORMLY in r. In particular every evaluation on the unit torus is uniformly
bounded. Moreover every negative coefficient is supported on the fixed
initial seed. The latter is an additional necessary condition, not used by
the Fourier test below.

No equal-length premise is used by the Fourier bridge. For a fixed finite
coarse prefix w of any length n, its refinements similarly
have charge e(w), so their endpoint masses are m+e(w), independent of r.
The same bounded-Fourier conclusion holds for every actual refined prefix.
For a first-letter root cycle, use only the refining powers that are genuine
prefixes, or pass to that cycle power. Do not silently test a phase that is
not part of the proposed trajectory.

By contrast, without finite support, consecutive cell reads give coefficients
in {-1,0,1}, while unit-scale refinement confines phi^r(R) to radius O(r).
Only an O(r^2) Fourier bound follows. Thus linear/Jordan growth is a genuinely
finite-support obstruction, although exponential growth also violates
arbitrary-background legality.

## 2. Exact eight-state periodic Laurent transfer

States are (h,s), where h is one of the four incoming headings and s is R or L.
Let p_j(h,s), h_j(h,s), s_j be the position, incoming heading and letter of
read j in the ordinary image of (h,s). Let F_r(h,s) denote the polynomial
of its r-fold refinement relative to its starting cell.

Heading preservation and displacement scaling give the exact recurrence

    F_(r+1)(h,s) = sum_j X^((a^r p_j)_x) Y^((a^r p_j)_y)
                               F_r(h_j,s_j).             (3)

The initial vector consists of the constant signs +1,-1 at each heading.
This is an 8 by8 Laurent matrix recurrence M_r. Since a has finite order q_a,
M_r is periodic with period q_a. Define

    T=M_(q_a-1) ... M_1 M_0.

Then F_(q_a r)=T^r F_0, and each intermediate phase is a fixed finite matrix
prefix times T^r F_0. No expansiveness or bounded-carry claim is used.

## 3. A terminating exact test at each torsion character

Choose a root of unity zeta of order q and integers u,v. Substitute
(X,Y)=(zeta^u,zeta^v). Work in the exact integral coefficient basis
1,zeta,...,zeta^(phi(q)-1) modulo the cyclotomic polynomial Phi_q.
Each periodic transfer becomes an integer matrix of dimension D=8 phi(q).
For every selected root output and refining phase, each coefficient sequence
is therefore an integer linear recurrence of order at most D.

Finite-support boundedness of all torus evaluations implies boundedness of
these coefficient sequences: every Galois conjugate is another torus
character and has the same bound, and the finite conjugate evaluation matrix
is invertible. It would be invalid to infer coefficient boundedness from a
single complex evaluation without this conjugate argument.

The test computes the minimal scalar recurrence exactly from at most2D+1
moments. The implementation uses rational Berlekamp-Massey, then independently
checks its identities through at least D further shifts and a nonzero leading
Hankel determinant of the asserted recurrence order. Cayley-Hamilton extends
the D checks to all times. The Hankel determinant proves minimality, so an
unobservable growing matrix mode cannot cause a false exclusion.

An integer scalar recurrence sequence is bounded if and only if its minimal
characteristic polynomial is a power of X times a product of DISTINCT
cyclotomic polynomials. Proof: bounded integer windows form a finite set;
recurrence determinism makes a repeated window eventually periodic. The
minimal polynomial then divides X^N(X^T-1). Conversely such a polynomial
forces eventual periodicity. This proof avoids numerical root estimates.

Thus an unbounded output certificate at ANY tested character excludes a
finite-support realization of the proposed rooted substitution. A bounded
answer merely passes this necessary test; it is not a realizability or
finite-support certificate. Searching finitely many characters is sound
but not asserted complete. This is not the expansive automatic verifier.

## 4. Exact controls and a strict Jordan example

fourier_transfer.py implements (3), cyclotomic embeddings and the exact
minimal-recurrence criterion. run_controls.py compares all four unit
rotations and an unequal-length9/13 control against direct expanded words
at250 checkpoints totaling232,690 letters, using characters of orders2,3,4 and5. Geometric control images need
not themselves be ant-legal.

All24 internally legal, R-prolongable, charge-preserving k9 unit-scale image
pairs in the frozen analysis inventory have an unbounded cubic-root character.
These pairs were already rejected by finite literal conflicts; the new value
is an all-level, reusable finite-fuel certificate, not a new open-class closure.

In particular, for

    R -> RLLRRRRLL,    L -> RRLLLLRRL,

all parity characters and total charge are bounded. At (X,Y)=(1,zeta_3),
exactly

    F_r = (1-4r)-2r zeta_3.

Its minimal polynomial is (T-1)^2, so the finite-support test rejects it
although this linear growth does not violate the arbitrary-background O(r^2)
bound. This checks that polynomial growth is treated correctly and that the
checker is stronger than a mere spectral-radius-greater-than-one filter.

The JSON summary and complete recurrence records are frozen alongside this
note. The executable's default root output is the north-incoming R prefix;
all_states=True is an algebra option, NOT permission to assume every state
is a prefix of a proposed ant. 