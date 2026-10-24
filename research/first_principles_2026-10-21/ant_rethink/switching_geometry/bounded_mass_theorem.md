# Uniform escape in density from every bound on black-cell count

## Status and scope

This is a global consequence of two existing nonexistence theorems. It does
not prove the highway conjecture. The argument does not assume a repeating
trace. The strongest conclusion is uniform zero density of low-mass times,
and hence divergence of the time-averaged black-cell count. It does not give
an explicit useful numerical rate or prove pointwise divergence of the count.

The inherited premises are:

1. No finite-support Langton-ant state has a periodic orbit with zero drift.
   Such an orbit would stay in a finite region. This contradicts the
   Bunimovich--Troubetzkoy unboundedness theorem.
2. No finite-support state is a clean translator with nonzero drift.
   This is Theorem 6.1, "Even-winding theorem", in Jillhewar's
   `paper/main.tex` at commit
   `76a7e234e577d992d086c204c3dea00ae72cf10a`:
   https://github.com/Atharva12456/langtons-ant-highway/blob/76a7e234e577d992d086c204c3dea00ae72cf10a/paper/main.tex

A clean translator means that the **entire** finite black set, the ant
position, and its heading repeat after a fixed spatial translation. It has
no emitted wake. This premise is much weaker than classifying all highways.

The compactness argument below is elementary. No finite search is a premise.
The exact source statements above remain dependencies. The inherited signed
cut potentials also imply unbounded black count, as explained in Appendix A;
unboundedness of the count is not claimed as a new result. The proposed
extension is the uniform zero-density statement in Sections 6--7. A limited
search of the inspected primary notes did not locate that consequence.
No claim of priority is made.

## 1. Center the board at the ant

Let

    X = {0,1}^{Z^2} x {N,E,S,W}

with the product topology. A state records the complete board, with the ant
at the origin, and its heading. Let G be one Langton update, followed by the
translation that puts the ant back at the origin.

The map G is continuous. Its output on any finite set of coordinates depends
on finitely many input coordinates and the heading.

It is also a homeomorphism. To invert a centered update, the new heading
gives the cell from which the ant moved. Its new color determines its old
color and therefore its old heading. Undo that one toggle and translation.

For each integer K>=0, put

    X_K = {x in X: the board in x has at most K black cells}.

This set is compact. Indeed, its complement is open: a board with more than
K black cells has a finite witness consisting of K+1 specified black cells.
Thus X_K is a closed subset of compact X. Every element of X_K has finite
support. There is no restriction on the positions of those cells.

The set X_K is also countable. The grid is countable, and its finite subsets
form a countable set. There are only four headings.

## 2. A finite-mass compact invariant set contains a periodic point

### Lemma

If Y is a nonempty compact subset of X_K and G(Y) is contained in Y, then Y
contains a periodic point of G.

### Proof

Take a nonempty compact subset M of Y that is minimal under the condition
G(M) subset M. Such a set exists by the nested-intersection argument (or
Zorn's lemma applied to nonempty compact forward-invariant sets).

Also G(M)=M. The image G(M) is a nonempty compact forward-invariant subset
of M, so minimality gives equality.

The black-cell counts attained in M form a nonempty subset of the finite
set {0,...,K}. Let m be their maximum, and choose x in M with exactly m
black cells, at positions z_1,...,z_m.

Consider the cylinder that fixes the heading of x and requires all of
z_1,...,z_m to be black. Any point of M in this cylinder already has m
black cells. It cannot have another black cell, by the definition of m.
Hence this cylinder meets M in the singleton {x}. Thus x is isolated in M.

The closure of the positive tail {G^n x:n>=1} is a nonempty compact
forward-invariant subset of M. Minimality says this closure is M. Since
x is isolated in M, some positive iterate G^n x equals x.

Therefore x is periodic. QED.

## 3. Black-cell count cannot stay bounded

### Theorem

For every finite-support initial state, the black-cell count is unbounded
along its forward orbit.

### Proof

Suppose it were always at most K. The closure Y of its centered forward
orbit is a nonempty compact subset of X_K. Continuity gives G(Y) subset Y.

The lemma produces a periodic centered state x in Y. It has finite support.
After its period, the uncentered state is the initial state translated by
the ant's displacement d over that period.

If d=0, this is a bounded periodic orbit, contrary to premise 1.
If d is nonzero, this is a clean finite translator, contrary to premise 2.

Both cases are impossible. QED.

## 4. A uniform bound exists for each mass ceiling

### Uniform theorem

For every integer K>=0 there is a finite integer T(K) such that every initial
state with at most K black cells has more than K black cells after some
t in {1,...,T(K)} updates.

T(K) does not depend on the locations of the initial black cells or on
their diameter. It can be chosen for all four headings.

### Proof

For n>=0, define the survivor set

    S_n = {x in X_K: G^t x is in X_K for every 0<=t<=n}.

Each S_n is compact, and S_(n+1) is contained in S_n. If every S_n were
nonempty, their intersection would be nonempty. An element of that
intersection would have a forward orbit whose mass never exceeds K.
Section 3 excludes that possibility. Therefore S_n is empty for some
finite n. Use this n as T(K). QED.

### Consequence along one orbit

For each fixed K, times when the black-cell count is greater than K occur
with bounded gaps. In every time interval [s,s+T(K)], at least one state
has more than K black cells: either the initial state already does, or
the uniform theorem applies from time s.

This is stronger than limsup |B_t|=infinity. It is **not** a proof that
|B_t| tends to infinity. The orbit can in principle make large excursions
and return repeatedly to a small black-cell count.

## 5. Why the uniform bound is computable in principle

One can enumerate all physical prefixes while their total black count
stays at most K. Fix an initial count m in {0,...,K}. At each previously
unread cell, branch on its initial color, allowing at most m first-read
black cells. At each previously read cell, its next color is forced.
Keep the total mass as m plus the signed toggle sum.

Every finite branch is realizable by a board with exactly m initial black
cells: put the unused black cells outside the finite visited footprint.

An infinite branch would define a finite initial black set of size at
most m (the first-read black cells). Some unused initial black cells in
the finite-prefix bookkeeping might never be assigned. Removing those
unused cells only lowers the actual global black count. The resulting
actual infinite trajectory would still stay below K, which is impossible.

The finitely branching prefix tree thus has no infinite branch. By
Konig's lemma it is finite. A complete depth-first traversal halts and
gives the exact largest first-exceedance time. This is a termination
argument, not a claim that the computation is practical for large K.

## 6. Every invariant probability gives zero mass to finite-support states

### Lemma

If mu is a G-invariant Borel probability on X, then mu(X_K)=0 for every K.

### Proof

There are no finite-support periodic points of G, by the two inherited
premises and the zero-drift / nonzero-drift distinction in Section 3.

Suppose x is a finite-support point with mu({x})=a>0. Since G is a
homeomorphism and mu is invariant, every point G^n x has the same mass a.
The forward orbit of x contains infinitely many distinct points: equality
of two iterates, followed by inversion, would make x periodic. A probability
cannot give the same positive mass to infinitely many disjoint singletons.
Thus every finite-support singleton has mass zero.

The set X_K is countable. Countable additivity gives mu(X_K)=0. QED.

## 7. Low-mass times have uniformly vanishing density

### Theorem

For every integer K>=0,

    lim_(n->infinity) sup_(x in X)
        (1/n) #{0<=t<n : G^t x in X_K} = 0.

In particular, for every epsilon>0 there is N(K,epsilon) such that every
orbit interval of length n>=N(K,epsilon) spends less than epsilon*n of its
states at black-cell count at most K. This is uniform in the initial board,
its black-cell locations, its heading, and the starting time of the interval.

### Proof

Suppose the conclusion fails. There are epsilon>0, integers n_j tending to
infinity, and points x_j in X such that the empirical probability measures

    nu_j = (1/n_j) sum_(t=0)^(n_j-1) delta_(G^t x_j)

satisfy nu_j(X_K)>=epsilon. The space X is compact metrizable, so a
subsequence of these probabilities converges weakly to a probability mu.

For every continuous real-valued f on X, telescoping gives

    | integral (f o G - f) d nu_j |
        = | f(G^(n_j) x_j) - f(x_j) | / n_j
        <= 2 ||f||_infinity / n_j.

Pass to the weak limit. Both f and f o G are continuous, so
integral(f o G)dmu=integral f dmu. Thus mu is G-invariant.

Because X_K is closed, the closed-set direction of the Portmanteau theorem
gives

    epsilon <= limsup_j nu_j(X_K) <= mu(X_K).

Section 6 gives mu(X_K)=0, a contradiction. QED.

The proof applies to every x in X. Infinite-support states never have
finite mass after finitely many toggles, so their low-mass density is zero
without further argument. The content concerns finite-support states.

### Divergence of the mean black-cell count

For a finite-support orbit, write b_t for its number of black cells. For
every K and every interval of n consecutive states starting at time s,

    (1/n) sum_(t=0)^(n-1) b_(s+t)
      >= (K+1) [ 1 - (1/n) #{0<=t<n : b_(s+t)<=K} ].

The term in braces divided by n tends uniformly to zero. Therefore the
lower limit of these interval means is at least K+1, uniformly over the
initial state and s. Let K increase. The mean black-cell count diverges to
infinity uniformly over all finite-support initial states and all interval
starting times as the interval length tends to infinity.

This is an average statement. It permits infinitely many sparse returns
to a fixed small black-cell count.

### Effective strengthening

The companion note
`../constructive_alternatives/explicit_low_mass_occupation_bound.md`
gives a quantitative proof. Let A_K(N) be the largest number of mass-at-most-K
states in any N-state orbit interval. It establishes

    A_K(N) <= 2(K+1)9^K * N^(1-1/D_K),
    D_0=1,  D_K=2K*D_(K-1)+1.

The recurrence has the exact solution

    D_K = 2^K K! * sum_(j=0)^K 1/(2^j j!).

Its key estimate is

    A_K(N) <= sum_(j=0)^K binom((2R+1)^2,j)
              + ceil(N/R) A_(K-1)(R).

Complete centered low-mass states whose whole black support lies within
distance R occur at most once each. At every other low-mass state, delete
one black cell farther away than R. The following R states follow the same
physical trajectory with total mass lower by one. Disjoint blocks starting
at such events give the second term. The companion note supplies the full
counting argument and constants; it was checked independently in this branch.

### Abstract form of the argument

The same proof works for any homeomorphism of a compact metrizable space
and any closed countable subset containing no periodic point. Such a subset
has zero mass for every invariant probability and has uniformly vanishing
orbit-occupation density. The application here uses the concrete closed
sets X_K and the inherited finite-support nonperiodicity results.

## 8. Limits of this result

* The compactness argument uses a bound on the **entire orbit's** black
  count. Repeated visits to X_K do not supply that bound.
* If a sequence of low-mass states converges, the future orbit of its limit
  can leave X_K. One cannot apply the lemma to the low-mass return set
  without proving invariance.
* Escape in density and divergence of the mean do not imply pointwise
  divergence of black-cell count.
* Growing black-cell count does not imply a bounded transverse width, a
  repeating trace, or a standard highway.
* The proof allows all the stored black information to remain on the board.
  It does not erase dormant trails or identify them with white cells.

The remaining global target is still to control nonstandard turns, not
merely the number of black cells.

## Appendix A. Direct dependency route through the existing signed cut

The exact column potential below is inherited from Jillhewar's pinned
`lean/Langton/DirectedPoseDiscrepancy.lean`:
https://github.com/Atharva12456/langtons-ant-highway/blob/76a7e234e577d992d086c204c3dea00ae72cf10a/lean/Langton/DirectedPoseDiscrepancy.lean

Fix an integer column c. At ant position (x,y), set

    chi = (-1)^(x+y),
    a = 1 if x=c, and 0 otherwise,
    G = 0 if x<c, 1 if x=c, and 2 if x>c.

Define the heading correction by

| Heading | Correction F |
|---|---|
| N | -chi*G |
| E | chi*(G-a) |
| S | chi*(-G+2a) |
| W | chi*(G+a) |

Then

    sum_(black cells z on column c) (-1)^(z_x+z_y) + F

is invariant modulo four. This follows by the eight local heading/color
checks, allowing the ant's position to be left of, on, or right of the cut.

Off the column, F is zero on the left and two modulo four on the right,
independently of heading and checker parity. Thus for any two times s,t and
every integer column strictly between x_s and x_t, the checker-signed
black-count difference in that column is two modulo four. Its support in
the symmetric difference B_s triangle B_t therefore has at least two cells.
Summing over the intervening disjoint columns gives

    2 max(|x_t-x_s|-1,0) <= |B_s triangle B_t| <= |B_s|+|B_t|.

A quarter-turn rotation gives the same inequality for y coordinates.

This immediately rules out a clean finite translator: its mass is constant,
while one coordinate of its displacement between period endpoints increases
without bound. The zero-drift periodic case is excluded by the inherited
unboundedness theorem. Hence the no-finite-support-periodic-point premise
of Section 6 has a short route through this signed-cut invariant.

The same inequality also shows that if black mass stays at most K on an
interval, then the ant stays within K+1 in each coordinate of its position
at the start of that interval. Only finitely many physical cells can be
processed. A long enough such interval repeats a complete relevant state,
which would give a bounded periodic orbit. This supplies a direct finite-state
route to a uniform mass-ceiling escape time. The companion note
`../constructive_alternatives/signed_cut_and_explicit_mass_bound.md` gives
the resulting explicit bound and source checks.

The two-endpoint inequality does not control all black-cell locations.
Cells far from both endpoint ant positions can remain on the board. It does
not make the set of low-mass return states finite.
