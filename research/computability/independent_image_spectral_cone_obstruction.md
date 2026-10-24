# A spectral cone obstruction without half-turn symmetry

2026-10-23 01:34 UTC. Independently signed as audit HA at01:39 UTC.
It concerns exact finite-support substitution models, not arbitrary seeds.
The half-turn hypothesis is deliberately absent.

## Statement

Let phi be a length-k substitution on the four ABSOLUTE movement directions,
k>=2, with net displacement A d for each image phi(d). Assume A is an
expansive integer2x2 matrix and every image alternates movement axes. Require
the usual global axis compatibility:

- for odd k, all images use one common permutation of the two source axes;
- for even k, all images have the same first movement axis.

Suppose k>|det A|. If an actual fixed point P=phi(P), from either permitted
initial incoming heading, is a finite-support ant, then rho(A) MUST itself
be a positive real eigenvalue of A.

Consequently a complex-conjugate eigenpair, or a strictly dominant negative
real eigenvalue, excludes every fixed-root finite-support model in this
class, at every radix above the determinant. No coarse-vertex separation,
opposite-image symmetry or bounded read multiplicity is assumed.

For a first-letter root cycle of length m, apply the same conclusion to
phi^m and A^m. One may NOT apply the unsquared conclusion to A itself.
An explicit corollary below excludes all root cycles when A has nonreal
eigenvalues and nonzero trace.

## 1. Exact four-dimensional incidence decomposition

For a function on directions, use the basis

    1, chi(d), d_x, d_y,

where chi=+1 on horizontal directions and -1 on vertical directions. The
incidence operator is (M f)(d)=sum_{z in phi(d)} f(z). Its actions are

    M 1=k,
    M chi=epsilon chi,
    M(v dot d)=v dot A d,

where epsilon=+1 or -1 for the odd axis-preserving or axis-swapping cases,
and epsilon=0 for even k. These are identities of compass counts, independent
of their order and independent of all opposite-image relations.

Let T_r(d) be the INTERNAL signed turn excess of phi^r(d), excluding the
turn from its incoming heading. Concatenating the k old refined blocks gives

    T_r=M T_(r-1)+b_r,       |b_r(d)|<=k-1.

Axis compatibility guarantees every seam is a quarter turn. Decompose

    T_r(d)=s_r+u_r chi(d)+v_r dot d.

The exact recurrences are

    s_r=k s_(r-1)+beta_r,
    u_r=epsilon u_(r-1)+gamma_r,
    v_r=A^T v_(r-1)+eta_r,

with uniformly bounded forcing. Because A is expansive, the convergent sums

    C=sum_(j>=1) beta_j/k^j,
    ell=sum_(j>=1) (A^T)^(-j) eta_j

give

    T_r(d)=C k^r+ell dot A^r d+O(r).                 (1)

The coordinate error is uniformly bounded: subtract the infinite series,
then its remainder is sum_(i>=1)(A^T)^(-i) eta_(r+i). The chi error is O(r).
No periodicity of b_r is needed for this estimate. For a fixed substitution
it is eventually periodic, since first- and last-letter maps have eventually
periodic powers, so C and ell are effectively computable rational values.

## 2. The determinant area bound kills the k mode

Every prefix of phi^r(d) is a sum of offsets A^j b_j, 0<=j<r, with uniformly
bounded b_j. Thus A^(-r) times every such prefix lies in one fixed ball K:
the series sum_(i>=1)||A^(-i)|| converges.

The unit pixel squares centered at distinct lattice read cells are disjoint
up to boundaries. Their union is contained in A^r(K+A^(-r)Q), where Q is the
unit square. The sets K+A^(-r)Q fit in a fixed bounded ball because the
inverse powers are uniformly bounded. Their areas are uniformly bounded.
Hence the number of read cells in each refined image is O(|det A|^r).

For any ant-legal finite interval, even on an infinite background, the signed
turn excess has absolute value at most the number of cells read: each cell
contributes -1,0,or1 by alternating reads. Internal curvature differs by one
initial turn. For the genuine prefixes phi^r(d_0) of P this bounds (1).

Expansiveness implies rho(A)<|det A|<k, so the coordinate term grows strictly
slower than k^r, even with a possible Jordan polynomial factor. The area bound
therefore forces C=0. This step uses neither half-turn symmetry nor a
particular real/complex spectral type.

## 3. Finite support forces a cone inequality

Write p(0)=0 for the actual path, and let w_n be its first n movement letters.
Because P is a fixed point, phi^r(w_n) is exactly its length-k^r n prefix,
and its endpoint is A^r p(n). Summing (1) over these n images, with their n-1
bounded joining turns, yields for every FIXED n>=1

    |B_(k^r n)|=|B_0|+ell dot A^r p(n)+O_n(r).        (2)

The finite-support axial midpoint inequality gives

    |B_0|+|B_(k^r n)| >= 2||A^r p(n)||_infinity-O(1).

Combining it with (2) yields the necessary asymptotic cone condition

    ell dot A^r p(n) >= 2||A^r p(n)||_infinity-O_n(r). (3)

The two vectors p(1),p(2) are linearly independent: the first two unit
movements are perpendicular. They suffice to detect any dominant eigenspace.

## 4. Oscillating dominant modes contradict the cone

If A has nonreal eigenvalues, put rho=rho(A), B=A/rho. The powers B^r are
uniformly bounded and uniformly invertible, since B is real-conjugate to a
rotation with angle neither0 nor pi. Also I-B is invertible. Thus

    (1/N) sum_(r=0)^(N-1) B^r ->0.

Take n=1 in (3) and divide by rho^r. Its right side is bounded below by a
fixed positive constant for all large r, since ||B^r p(1)|| is uniformly
positive and r/rho^r tends to0. Averaging the left side instead tends to0.
Contradiction. This covers rational as well as irrational rotation angles.

If A has a unique strictly dominant negative eigenvalue -rho, choose one
of p(1),p(2) with nonzero projection v onto its eigenspace. Then

    A^r p(n)/rho^r=(-1)^r v+o(1),        v!=0.

Inequality (3) along even and odd r would require both ell dot v and its
negative to be at least2||v||_infinity, impossible. This argument also works
if ell annihilates v: then the left side tends to zero while the right does
not.

The remaining case without a positive spectral-radius eigenvalue is a
repeated negative eigenvalue. If A=-rho I, the same parity argument applies.
Otherwise write A=-rho I+N, N^2=0, N!=0, and choose p(n) with N p(n)!=0.
Dividing (3) by r rho^r gives the same opposite nonzero limits on the two
parities, using A^r=(-rho)^r(I-r N/rho). Again impossible.

These cases exhaust real2x2 matrices for which rho(A) is not itself a
positive real eigenvalue. If eigenvalues are +rho and -rho, the theorem
asserts no exclusion, because +rho DOES occur. Positive-dominant matrices
remain a genuine escape class.

## 5. Root-cycle corollary and limits

The first-letter map has root cycle lengths only1 or2 in the odd
axis-preserving case, only2 or4 in the odd axis-swapping case, and only1 or2
in the even common-first-axis case. A cycle limit is a fixed point of the
corresponding power, which preserves the axis hypotheses, has matrix A^m
and length k^m>|det(A^m)|.

For a nonreal eigenpair rho exp(+/-i theta), 0<theta<pi, a positive
spectral-radius eigenvalue of A^m would require m theta=0 modulo2pi. Among
m in{1,2,4}, the only possibility is m=4,theta=pi/2, equivalently trace A=0.
Therefore every root-cycle limit is excluded when A has nonreal eigenvalues
and nonzero trace. With trace0, fixed roots and two-cycles are still excluded,
but a four-cycle is NOT excluded by this theorem.

This does not claim that a positive-spectral-radius model exists. It also
does not cover larger hidden-state alphabets, arbitrary directive limits,
or state-dependent aligned offsets. In particular a root cycle must not be
silently treated as a one-step same-path identity.
