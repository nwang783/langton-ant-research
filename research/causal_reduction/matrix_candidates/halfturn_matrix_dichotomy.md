# A spatial-matrix dichotomy for half-turn uniform refinements

23 October 2026, 03:18 UTC. Independently signed analytic review at 03:24 UTC;
finite-order parity sharpening independently signed at 03:27 UTC.
Dependencies: the signed parabolic/even-prefix proof, diagonal finite-fuel
lemma, axial midpoint inequality, and existing finite-strip escape clocks.
This is a classification of a construction architecture, not the ant conjecture.

## Statement

Let phi be a uniform length-k>=2 substitution on E,N,W,S with

    phi(-d)=-phi(d),       net(phi(d))=A d,

for an integer two-by-two matrix A. If a growing rooted power-limit is an
actual ant trajectory from finite black support, then A must be either:

1. fully expansive (both eigenvalue moduli>1), with

       rho(A)<k<=|det A|;

2. invertible and of finite order, with order in{1,2,4}.

The second case reduces after a finite substitution power to spatial matrix
I. In particular unbounded shears, saddles, rank-one dilations and singular
power-bounded matrices do not supply a third intermediate construction route.

This is for a fixed half-turn-symmetric four-direction substitution and its
rooted power-limits. Independent opposite images, contextual/state-dependent
refinements and arbitrary directive sequences are not classified here.
The expanding-case area theorem has separately proved broader directive
scope; that does not enlarge the present dichotomy automatically.

## 1. Root powers and geometry

Pass to psi=phi^m for which the actual movement word is a fixed point. The
length becomes K=k^m and spatial matrix becomes B=A^m. Half-turn symmetry
persists. Each occurring image alternates movement axes. Since both axis
classes occur and opposite images are half-turn copies, every image does.
Odd K forces a common source-axis permutation; even K forces a common first
axis. Thus the two-axis curvature recurrence from the signed parabolic proof
applies. All spectral inequalities below are invariant under taking powers.

Rename psi,K,B as phi,k,A for the proof.

## 2. A general footprint area bound

Define

    G(A)=product over the two eigenvalues lambda of max(1,|lambda|).

Every read position in a depth-r image belongs to a sum

    b_0+A b_1+...+A^(r-1)b_(r-1),

where the local offsets b_i range in one fixed finite set. There are constants
C,d, depending only on the substitution and matrix, such that the number of
lattice sites in this footprint is at most

    C(r+1)^d G(A)^r.                                      (1)

For distinct real eigenvalues, work in an eigenvector basis: each coordinate
has width at most C(r+1)max(1,|lambda_i|)^r. A fixed parallelogram and its
unit-square thickening have the asserted area. For a complex pair, a fixed
real change of basis makes A a dilation times a rotation; the sum of inverse-
or forward-scale radii gives the same bound. For a real Jordan block,
||A^j||<=C(j+1)max(1,|lambda|)^j, so a disk bound loses only a polynomial
factor and gives (1). Nilpotent matrices have an eventually finite sum.
Thickening by unit lattice squares accounts for lattice counts, including
contracting directions whose geometric width would otherwise approach zero.

## 3. If k>G(A), every even-prefix endpoint has bounded A-orbit

Write U_r,V_r for internal signed turn excesses in the horizontal/vertical
refined images, equal for opposite directions by half-turn symmetry. As in
parabolic_halfturn_obstruction.md,

    S_r=(U_r+V_r)/2=C_0 k^r+O(1),
    D_r=(U_r-V_r)/2=O(r).

The actual rooted refined prefix reads only the polynomial-times-G(A)^r
number of sites in (1). Legal alternating reads bound its absolute signed
excess by that number. If k>G(A), this forces C_0=0, hence U_r+V_r=O(1).

Every fixed even prefix of length2n has n letters of each axis. Its refined
charge is n(U_r+V_r), plus only2n-1 inter-image seams and the initial turn,
so it is O_n(1). Finite initial support therefore gives bounded checkpoint
mass. The signed axial midpoint inequality implies

    sup_r ||A^r p(2n)|| < infinity   for every fixed n.     (2)

Let V_b be the linear subspace of vectors with bounded A-orbit. If the powers
of A are unbounded, V_b is proper. Since p(2) is a nonzero grid diagonal,
(2) either immediately fails or forces V_b to be that diagonal line. In the
latter case all even positions lie on the same grid diagonal. The signed
finite-fuel diagonal lemma excludes this: one checker sector has infinitely
many fresh odd L reads; the other has no repeated directed coarse edge and
therefore eventually has fresh even L reads.

Thus

    unbounded powers of A and k>G(A) are impossible.      (3)

## 4. The critical spectral radius k is also impossible

Each image consists of k unit moves, so ||A||_1<=k and rho(A)<=k. Suppose
rho(A)=k. Let ell be a complex left eigenvector for an eigenvalue lambda of
modulus k, normalized by max(|ell(E)|,|ell(N)|)=1. Choose a source direction
d attaining that maximum. Then

    k=|ell(A d)|=|sum_(e in phi(d)) ell(e)|<=k.

Equality forces every summand to have modulus1 and a common complex phase.
Both movement axes occur in the image, so |ell(E)|=|ell(N)|=1 and their
ratio is+1 or-1. After multiplying by a phase, ell is the real functional
x+y or x-y. Hence lambda is real and equals+k or-k. Applying equality to
all four images gives

    ell(e)=(lambda/k)ell(d) for EVERY letter e in phi(d).

Take a further even power if needed, while retaining the actual fixed root.
Every letter in every refined root then has the same sign of ell. The entire
rooted limit is a strictly ell-monotone staircase using one direction from
each axis. Every cell read is fresh and its quarter turns alternate R,L.
Infinitely many first-L cells contradict finite initial support. Thus

    rho(A)<k                                                   (4)

is necessary. This saturation argument only uses literal alternating image
axes and the rooted geometric refinement, not the curvature estimate.

## 5. Every not-fully-expansive matrix with unbounded powers is excluded

If at least one eigenvalue has modulus<=1, then

    G(A)=max(1,rho(A)).

By (4) and k>=2 we have k>G(A). If A has unbounded powers, (3) is therefore
a contradiction. This handles saddles, signed unipotents and singular
expanding matrices, not just matrices with both eigenvalues bounded by1.

If A is fully expansive, G(A)=|det A|. Equation (3) yields the claimed
upper bound k<=|det A|, while (4) gives the strict lower spectral bound.

## 6. Singular matrices with bounded powers are also impossible

For a singular integer two-by-two matrix with bounded powers, its eigenvalues
are0 and t=trace(A), where t is0,1 or-1.

If t=0, Cayley-Hamilton gives A^2=0. The offset sum then has uniformly bounded
support, while the actual refined-prefix length k^r tends to infinity. The
existing finite-domain escape theorem excludes this on any initial coloring.

If t=+1 or-1, Cayley-Hamilton gives A^2=t A. All offset terms after the first
lie in the fixed line im A, and ||A^j|| is uniformly bounded. Hence the whole
depth-r read footprint lies in a fixed-width strip about im A, of length O(r).

- If im A is axis-parallel, the signed fixed-height rectangular escape bound
  in sources/kehao95-core/clock_escape/PROOF.md, Section3, is polynomial in
  this O(r) length. It cannot contain a legal interval of length k^r.
- If im A is oblique, choose the strict scalar-coordinate clock from
  computability/oblique_strip_clock_obstruction.md, Sections1-2, with normal
  perpendicular to im A. On the fixed-width strip all its field weights
  and head corrections are bounded constants. The strip segment contains
  only O(r) lattice sites, so the clock range on the finite read set is O(r),
  whereas every step gains at least2. Again k^r steps are impossible.

For an infinite initial background, copy its colors on that finite read set
into a finite otherwise-white board. The entire finite interval is unchanged.
Thus this singular power-bounded exclusion needs no finite-support assumption
and no half-turn hypothesis beyond the footprint recurrence itself.

## 7. The remaining power-bounded matrices have finite order

An invertible integer matrix with bounded powers has both eigenvalue moduli1,
since its nonzero integer determinant has modulus at least1. Bounded powers
exclude a nontrivial Jordan block. If det A=-1, the eigenvalues are1,-1 and
A^2=I. If det A=1, the integer trace is in{-2,-1,0,1,2}; the semisimple
characteristic polynomials give orders2,3,4,6,1 respectively. Hence only
finite-order matrices remain in the not-fully-expansive case.

In fact the original uniform geometry excludes orders3 and6. Every length-k
lattice movement word has endpoint coordinate sum congruent to k modulo2.
If k is even, both columns of A lie modulo2 in the one-dimensional span of
(1,1), inconsistent with unimodularity. Thus k is odd. Each endpoint column
is then either(1,0) or(0,1) modulo2; odd determinant makes them different.
Consequently A modulo2 is I or coordinate swap and trace(A) is even. Orders
3 and6 have trace-1 and+1, respectively. Only orders1,2,4 survive. This
argument applies to the original A before taking any root power and needs
no image-axis assumption beyond unit lattice moves. A nonorthogonal
finite-order matrix is NOT identified with a physical Gaussian rotation.

Take a common multiple of the root-cycle length and this matrix order.
The corresponding substitution power has spatial matrix I. This explains
why a genuinely stationary, possibly nonuniform or context-dependent unit-
scale construction is a substantive residual route rather than merely the
next small expansive matrix to enumerate.
