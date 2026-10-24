# Area/curvature obstruction for arbitrary common expansive matrices

23 October 2026, 01:27 UTC. Independently passed analytic audit at01:34 UTC.
This extends the common-matrix theorem beyond diagonal and monomial matrices.
It does not claim a universal finite-seed theorem.

## Statement

Let A be ANY expansive integer 2x2 matrix. Let phi_0,phi_1,... be arbitrary
constant-length k substitutions on the four absolute compass directions.
At every level require half-turn covariance phi_j(-d)=-phi_j(d), net image
displacement A*d, and axis-alternating image words. For odd k, require one
common source-axis permutation per level (all images preserve axes, or all
swap them). For even k, require one common first axis for the four images
at each level, and that the composed words are axis-alternating.
Assume compatible nested root images under the order

    Psi_r = phi_0 o ... o phi_(r-1).

If k>|det A|, the limiting word is NOT an actual finite-black-seed ant path.
The directive sequence need not be periodic, finite-state or computable.
For a single substitution this covers every fixed-root and first-letter-cycle
limit, by taking the appropriate power if necessary. In that application the
power must satisfy the displayed axis conditions; for odd substitutions with
a common source-axis permutation this is automatic.

No source/target separation or prohibition on alien coarse-vertex visits is
assumed. The matrix may mix coordinates, have negative entries, negative
determinant, complex eigenvalues, or a one-step singular value below one.
Expansiveness, not direct Euclidean expansion, is the relevant hypothesis.

## 1. The image lies in an expanding linear image of one bounded set

The familiar prefix expansion gives, for every read position p of a level-r
image,

    p = sum_(j=0)^(r-1) A^j b_j,

where b_j is a proper-prefix offset in one length-k image. Thus ||b_j||<=k
in the Euclidean norm. Because A is expansive, there are C>0 and 0<q<1 such
that ||A^(-i)||<=C*q^i for all i>=0. Therefore

    ||A^(-r)p|| <= k * sum_(i=1)^r ||A^(-i)|| <= R

for one finite constant R independent of the directive schedule, root and r.
All read positions lie in A^r K for the fixed radius-R ball K.

To turn volume into an exact lattice-count bound, place a closed unit square
Q around every visited lattice point. Their interiors are disjoint, so the
area of their union equals the number of distinct points. The union lies in

    A^r K + Q = A^r (K + A^(-r) Q).

The sets A^(-r)Q are uniformly bounded. Hence K+A^(-r)Q lies in one fixed
ball K', and the number of distinct read cells is at most

    area(K') * |det A|^r.

This avoids the unjustified replacement of a skew expanding shape by a large
axis-aligned bounding box. No lattice-point asymptotics are needed.

## 2. Curvature uses only axis counts, not the endpoint matrix

Let U_r be the internal turn excess of Psi_r(E), equal to that of Psi_r(W)
by half-turn covariance; define V_r from N/S. Appending the new INNER image
concatenates k previous-level words. Every seam contributes +/-1 because
composed words alternate axes. Thus seam terms are uniformly bounded.

For odd k, its two axis counts are (k+1)/2 and (k-1)/2. Writing S_r=U_r+V_r,
D_r=U_r-V_r, the exact recurrences are

    S_r = k*S_(r-1) + beta_r,
    D_r = epsilon_r*D_(r-1) + gamma_r,  epsilon_r in {+1,-1},

with bounded beta,gamma. Therefore S_r=C0*k^r+O(1), D_r=O(r). In the even
common-axis case each image has k/2 letters on either axis, and D_r is just
a bounded seam difference. Consequently, in both cases every actual nested
root prefix has internal turn excess C0*k^r/2+O(r).

On ANY initial coloring, the total turn excess of a legal finite ant segment
has magnitude at most its number of distinct read cells. At each cell the
successive reads alternate R/L, so its net contribution is -1,0 or1. The
initial turn omitted by internal curvature changes this bound by only1.
The preceding exact area ceiling and k>|det A| force C0=0.

## 3. Finite mass versus displacement

For a finite initial black support, black mass changes by exactly total R-L.
The black mass at each level-r prefix endpoint is consequently O(r), with
its fixed initial mass absorbed into the constant. Its displacement is
A^r*d_r, where d_r is a unit compass direction. The inverse-norm estimate gives

    ||A^r*d_r|| >= 1/||A^(-r)|| >= C^(-1)*q^(-r).

The signed axial midpoint inequality bounds twice the infinity-norm midpoint
displacement by initial plus final black mass. Norm equivalence and bounded
heading midpoint corrections make the right-hand requirement exponential,
while available mass is only O(r). Contradiction.

## Exact scope

This generalization concerns a COMMON expansive A. For varying noncommuting
A_j, individual expansiveness does not automatically give uniform control of
inverse products. The previously signed variable signed-monomial theorem
remains valid, but no unrestricted varying-matrix extension is inferred here.
Independent opposite images or extra hidden states can retain extra curvature
modes and are not excluded by this half-turn argument. The critical region
k<=|det A|, including the current mixing targets, is deliberately left open.
