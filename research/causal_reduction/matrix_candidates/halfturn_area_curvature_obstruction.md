# All-length half-turn matrix obstruction above the area scale

23 October 2026. **Independently signed in audit FZ, 00:20 UTC.**
This is a construction-family theorem, not universal finite-seed capture.

## Statement

Let phi be a constant-length substitution on the four ABSOLUTE unit movement
directions E,N,W,S. Assume:

1. Its length k>1 is odd. Every image alternates movement axes, beginning on
   the same axis as its source letter.
2. phi(-d)=-phi(d), with minus applied to every movement in an image.
3. Each image has vector sum A d for A=diag(a,b), where integers a,b>1.

If k>ab, no fixed-root or first-letter-cycle limit of phi is the direction
path of a finite-black-seed classical ant, for either perpendicular initial
heading. This imposes NO internal-sublattice separation assumption. In
particular all half-turn-symmetric radix17, diag(3,5) constructions are
excluded at all future times without enumerating image words.

An axis-swapping version follows by replacing phi with phi^2: this preserves
half-turn symmetry and squares k,a,b, so k>ab is unchanged. That extension
requires each image to begin on the axis opposite its source letter and to
alternate axes throughout; arbitrary image axis choices are not claimed.

## 1. Exact curvature recurrence

For a finite alternating-axis direction word w, define its INTERNAL signed
curvature T(w) as the number of clockwise quarter turns minus counterclockwise
quarter turns BETWEEN consecutive letters. It omits the initial turn from
the incoming heading. Put T_r(d)=T(phi^r(d)), so T_0(d)=0.

Let F(d),G(d) be the first and last directions of phi(d). Half-turn symmetry
makes both maps commute with d -> -d. Axis preservation makes their
restrictions to each two-element axis either identity or swap. Thus F^2=G^2=id.

By concatenating the k refined image blocks exactly,

 T_r(d) = sum_(z in phi(d)) T_(r-1)(z) + b_r(d),

where b_r(d) is the signed curvature of the k-1 joining pairs

 (G^(r-1)(u), F^(r-1)(v))

for adjacent letters u,v in phi(d). These are perpendicular pairs, so their
signed turns are +/-1. Consequently |b_r(d)|<=k-1, and b_r(d) is2-periodic in r.
No physical ant legality is used here.

Half-turn symmetry preserves turn signs, hence

 T_r(E)=T_r(W)=U_r,    T_r(N)=T_r(S)=V_r.

An E/W image has (k+1)/2 horizontal letters and (k-1)/2 vertical letters;
a N/S image has the reversed counts. Set S_r=U_r+V_r and D_r=U_r-V_r. Then

 S_r = k S_(r-1) + beta_r,
 D_r = D_(r-1) + gamma_r,

with beta_r=b_r(E)+b_r(N), gamma_r=b_r(E)-b_r(N). Both forcing sequences are
bounded and2-periodic. In particular D_r=O(r), and

 S_r = C k^r + O(1)

for one explicitly rational C. For even r=2m,

 S_(2m) = (k beta_1 + beta_2) * (k^(2m)-1)/(k^2-1).

Thus each T_r(d)=C k^r/2 + O(r).

## 2. Exact area ceiling for any ant-legal prefix

The net displacement identity implies that every prefix position of phi^r(d)
is a sum of r terms A^j v_j, with v_j among the finite image-prefix offsets.
For constants C_x,C_y depending only on the given images, all these positions
lie in

 [-C_x a^r, C_x a^r] x [-C_y b^r, C_y b^r].

Therefore the number of distinct read cells is O((ab)^r).

For ANY actual ant interval, on any initial coloring, its signed total turn
excess equals final black count minus initial black count ON THE FINITELY MANY
READ CELLS. Each cell contributes -1,0,or1. Its absolute value is at most the
number of distinct read cells. The internal curvature differs by only the
first prescribed turn, hence |T_r(d)|<=number of read cells+1.

In a fixed-root or first-letter-cycle limit, arbitrarily large even iterates
phi^(2m)(d) are genuine prefixes: F^2=id makes every root prolongable for
phi^2. Apply the preceding ceiling to these prefixes. Since k>ab, a nonzero
C would violate it exponentially. Thus every ant-legal candidate in the
stated class must have C=0, and T_(2m)(d)=O(m).

## 3. Finite support contradicts the midpoint displacement bound

The actual total turn excess of the prefix phi^(2m)(d) is T_(2m)(d) plus its
one initial turn. If the initial finite black mass is M, the black mass at
that prefix endpoint is consequently M+O(m).

Its endpoint is A^(2m)d. Its infinity-norm distance from the starting point
is a^(2m) for a horizontal root or b^(2m) for a vertical root. Initial and
final heading-midpoint corrections have bounded norm. The independently
signed axial midpoint inequality for finite-support ants gives

 |B_0| + |B_t| >= 2 ||(p_t-d_h/2)-(p_0-d_(h0)/2)||_infinity.

Its left side is O(m); its right side is at least2 min(a,b)^(2m)-O(1).
This is impossible because min(a,b)>1. QED.

## Scope and construction consequence

The area argument does not alone exclude arbitrary backgrounds: it only
forces zero leading mean curvature. The midpoint step specifically uses
finite support. The theorem does not cover k<=ab, independent opposite
images, larger hidden-state alphabets or variable-length substitutions.
Section4 below DOES extend the result to arbitrary nonuniform level schedules
with common length and common endpoint matrix. It also does not assert that the individual
image words are ant-legal: an internally illegal image merely fails sooner.

For this symmetric direction-only architecture, increasing the time radix
past the area determinant can never rescue a construction. The way forward
must change that structural premise, not merely enlarge k. A separate
coarse-vertex theorem concerns overlap; this proof works even when internal
image reads hit A Z^2.

## 4. Stronger theorem: arbitrary, nonperiodic level schedules

The computability analysis separately reviewed this extension at00:16 UTC;
independent auditor signoff is still requested. No finite-control hypothesis
is needed.

Let phi_0,phi_1,... be ANY sequence of length-k substitutions, each satisfying
the same half-turn, axis-preserving and common A=diag(a,b) assumptions above.
They need not repeat or be computably selected. Define the ordered composition

 Psi_r = phi_0 o phi_1 o ... o phi_(r-1),    Psi_0=identity.

Choose a compatible sequence of root directions d_0,d_1,... with

 first(phi_r(d_(r+1))) = d_r.

Then W_r=Psi_r(d_r) are nested words of length k^r. Their limit cannot be a
finite-support ant path if k>ab.

Indeed set T_r(d)=T(Psi_r(d)). To pass from r-1 to r, expand the NEW INNER
word phi_(r-1)(d) into its k old Psi_(r-1) blocks. This gives the SAME two
curvature recurrences as before. The seam correction now uses the first and
last letters of Psi_(r-1) and the adjacent pairs of phi_(r-1)(d). Each summand
is still +/-1 and there are k-1 of them. Thus beta_r and gamma_r are uniformly
bounded, though no longer necessarily periodic.

Consequently D_r=O(r), while the absolutely convergent series

 C = sum_(j>=1) beta_j / k^j

gives S_r=C k^r+O(1): the normalized tail, multiplied back by k^r, is uniformly
bounded by a geometric series. Every image prefix offset has coordinates
bounded by k, uniformly over the directive sequence. The same box bound
O(a^r) by O(b^r) therefore holds for every W_r. Axis preservation keeps the
root axes constant; half-turn symmetry removes any changing root signs from
the U_r or V_r curvature. The area ceiling on the actual nested prefixes
forces C=0. Their net endpoints are exactly A^r d_r and have norm at least
min(a,b)^r. Finite-support mass is only O(r), contradicting the same midpoint
bound. This proves the stronger theorem.

Thus even changing the complete local recipe arbitrarily at EVERY scale cannot
rescue this symmetric architecture above the area scale. The obstruction is
not a finite enumeration of period-two or other finite-controller schedules.

## 5. Bounded variable radices and signed monomial matrices (new extension)

This section was added after audit FZ and independently passed analytic
review at00:37 UTC. It does not alter Sections1–4 or their signed status.

The same argument allows a bounded sequence of odd radices k_j>1, and a
sequence of signed monomial integer matrices A_j: each has one nonzero entry
per row and column, and the magnitudes of its two nonzero entries are at
least2. For each j, phi_j is a length-k_j half-turn-covariant substitution,
with net image displacement A_j d. Its images alternate axes and use the
same axis permutation as A_j. Thus a whole level may preserve or swap axes;
there is no arbitrary per-letter mixture. Assume compatible nested roots.

Set

    K_r=product_(j<r) k_j,
    P_r=A_0 ... A_(r-1),
    Q_r=abs(det P_r)=product_(j<r) abs(det A_j).

If limsup_(r->infinity) K_r/Q_r is infinite, no finite-support ant can
realize the resulting nested direction word. This includes arbitrary
nonperiodic schedules that mix area-subcritical and area-supercritical
levels, provided the accumulated time/area ratio is unbounded. The matrices,
radices and their schedule need not be computable.

Proof: append the new INNER image as before. An axis-preserving level gives
D_r=D_(r-1)+gamma_r, while an axis-swapping level gives
D_r=-D_(r-1)+gamma_r. In either case

    S_r=k_(r-1) S_(r-1)+beta_r,
    abs(beta_r),abs(gamma_r)<=2(k_(r-1)-1).

Consequently D_r=O(r), since the radices are bounded. There is a real C with
S_r=C K_r+O(1). In fact the tail bound is uniform even without bounded radices:
abs(S_r-C K_r)<=2, by telescoping
(k_j-1)/(k_r ... k_j). All four internal curvatures are therefore
C K_r/2+O(r).

Every prefix position in a level-r image is a sum of vectors P_j v_j,
0<=j<r, with ||v_j||_infinity<=max k_j. Write R_(j,x),R_(j,y) for the
magnitudes of the unique nonzero entries in the rows of P_j. Right
multiplication by A_j multiplies each such row magnitude by an integer at
least2, even if the active column swaps. Thus

    sum_(j<r) R_(j,x) <= R_(r,x),
    sum_(j<r) R_(j,y) <= R_(r,y).

The prefix box area is consequently O(R_(r,x) R_(r,y))=O(Q_r), with a
constant depending only on the bounded radix ceiling. Alternating reads
bound the turn excess by this area. Along a subsequence with K_r/Q_r
unbounded, the coefficient C must vanish. The finite-seed mass is now O(r),
while the endpoint P_r d_r has magnitude at least2^r. The same midpoint
mass inequality is a contradiction.

This is not a theorem for arbitrary matrices with mixing rows, unbounded
radices, independent opposite-direction images, or general hidden-state
alphabets. It still permits arbitrary internal coarse-lattice overlap.

## 6. Even-radix half-turn direction images (new extension)

Added23 October2026 at00:41 UTC, **pending independent review**.
Let a stationary half-turn-covariant direction substitution have even length
k and positive diagonal endpoint matrix A=diag(a,b), a,b>1. Assume each image
alternates movement axes and ALL images begin on the same axis. Then it
cannot yield a finite-support ant whenever k>ab, for fixed or antipodal
first-letter-cycle roots.

The common first axis is exactly what makes even-length blocks concatenate
with perpendicular seams: every image ends on the opposite axis. Both the
horizontal and vertical movement counts in EVERY image are k/2. Hence

    U_r=(k/2)(U_(r-1)+V_(r-1))+b_r(E),
    V_r=(k/2)(U_(r-1)+V_(r-1))+b_r(N).

The seam corrections are uniformly bounded by k-1. Thus

    S_r=kS_(r-1)+beta_r,
    D_r=gamma_r=O(1).

As before S_r=Ck^r+O(1), the O((ab)^r) area ceiling forces C=0 when k>ab,
and finite-seed mass O(1) contradicts exponential endpoint displacement.
No internal coarse-lattice separation is used.

For a genuine finite-support limit of a positive-diagonal half-turn direction
substitution, the common-first-axis premise is necessary, not a controller
restriction that can hide a survivor. First, all four compass directions
occur infinitely often in any finite-support ant: if one direction eventually
never occurs, the perpendicular axis forces strict progress along its opposite
direction every second step. Each future read is fresh, so eventually every
turn is R, contradicting the missing direction.

If the actual limit P is fixed under a positive power phi^m, every intermediate
word phi^j(P) contains all four directions: positive diagonal net displacement
of each corresponding image retains at least one copy of each source direction.
Every image phi(d) therefore appears inside P, so each alternates axes. Let
f(d) be its first axis. At a seam between phi(u),phi(v), perpendicular movement
requires f(u)=f(v), since k is even. The intermediate infinite word
phi^(m-1)(P) contains all four letters, and adjacent equality along it forces
f constant on all four. This proves necessity.

With the common first axis, the first-letter map sends every letter to that
axis. Half-turn covariance makes its restriction to the two letters on that
axis either identity or interchange. Thus its periodic root is fixed or
antipodal two-cycle, and in the latter case phi(P)=-P as in the signed
fresh-record reduction. The same-path relation is p(kn)=+/-A p(n).

## 7. Consequence for minimum diagonal stretch two (pending Section6 review)

For the even-radix family in Section6, parity forces a,b even. Suppose a=2
and b>=2. Its necessary area condition is k<=2b. Pure signed rectangular
fresh-record bounds give k=4ell and

    s_b=ell-b/2 >= c(max(0,b-ell-1)).

Since ell<=b/2, this forces ell=b/2 and b<=2. Thus only(k,a,b)=(4,2,2)
remains. It is already excluded by the signed scalar eventual-affine bound
k>=3A, including its explicit small-owner inventory at A=2,k=4.
Consequently every such positive-diagonal half-turn direction construction
with minimum stretch2 is impossible, at every length. Coordinate swaps and
antipodal root cycles are included. This remains a restricted construction
family, not a statement about independent opposite images or hidden states.
