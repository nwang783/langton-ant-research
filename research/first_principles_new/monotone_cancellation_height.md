# A monotone plaquette height for arbitrary ant turn histories

22 October 2026. This is an exact chronological representation, independent of eventual factor-language assumptions. It does not prove highway attraction.

## 1. Signed deposition and the mixed difference

Let chi(x,y)=(-1)^(x+y), and let sigma be the fixed checkerboard/heading sector: sigma=chi(p) for a vertical heading and -chi(p) for a horizontal heading. Write

    rho_t(x,y) = -sigma chi(x,y) 1_{B_t}(x,y).

For any positive word w in R,L, follow its geometric head motion from the chosen starting pose and define its formal deposition D(w) by adding -sigma chi(q) at each R read q, and +sigma chi(q) at each L read q. No coloring feasibility is required to define D(w). For an actual ant history w_t, flipping the read bit gives exactly

    rho_t - rho_0 = D(w_t).

For a finitely supported integer function K on unit plaquettes, indexed by their lower-left corners, put

    (partial_xy K)(x,y)
      = K(x,y)-K(x-1,y)-K(x,y-1)+K(x-1,y-1).

A unit of K at plaquette (i,j) contributes +1 at its southwest and northeast corners and -1 at its southeast and northwest corners.

## 2. Every positive face cancellation deposits one positive plaquette

Four consecutive equal turns a^4 return to the same physical head pose. Direct inspection for a=R,L and the four incoming headings shows

    D(a^4) = partial_xy 1_P,

where P is the single physical unit plaquette enclosed by that four-turn cycle. The coefficient is +1 in ALL cases. The sigma/chi factor is essential: the two physical orientations do not produce opposite signs in this signed height convention.

Consequently, deleting any consecutive R^4 or L^4 from a positive word preserves every later geometric read position and subtracts exactly one positive unit plaquette from its deposition.

Reduce a word online in G=C4*C4, using a stack of reduced syllables of exponent1,2,3. Appending a fourth copy of the last generator removes that four-cycle. Record its physical plaquette in K. If r_t is the reduced word after t letters, then

    D(w_t) = D(r_t) + partial_xy K_t,

with K_0=0. At each input letter, either K is unchanged or one plaquette is increased by1. Therefore K_t is a pointwise nondecreasing, nonnegative, integer-valued chronological height.

Combining this with the actual lamp update yields the exact global decomposition

    rho_t = rho_0 + D(r_t) + partial_xy K_t.                 (1)

This holds for EVERY square-ant trace and every finite time. It does not use the no-interleaving theorem, finite initial support, eventual standard factors, or bounded retreat. Finite support is needed only when one wants all fields and sums in (1) to be finite.

## 3. Uniqueness and a nonnegative concatenation defect

The mixed-difference operator is injective on finitely supported functions: summing partial_xy K over x<=i,y<=j recovers K(i,j). The reduced positive normal form r is unique. Therefore the plaquette count K does not depend on the order of legal R^4/L^4 deletions. This is an exact confluence statement for the physical cancellation counts, not merely uniqueness of the group element.

For concatenated histories uv, one may first reduce u, then v in its translated/rotated physical starting frame, and finally reduce the join of the two reduced words. Thus

    K(uv) = K(u) + K(v at the endpoint of u) + K_join,

where K_join>=0 pointwise. In particular K is superadditive under temporal splitting after the segment heights are put in their actual physical coordinates. The join term records cancellations whose supporting letters straddle the split.

## 4. Exact relation to completed module fingers

For a north-facing R module rooted at (0,0), the complete G call of depth n has

    K = 1_{ {(i,-1): 0<=i<=n} }.

Its four-corner toggle is the mixed boundary of this unit-height horizontal strip. The reflected L version and rotated/translated versions also have positive strip height.

A complete B_R call consists of the root unit plaquette, the mandatory north G finger, and possibly an east G finger. Its K is the indicator of their disjoint-interior union: a vertical strip when the second finger is absent, or a one-cell-thick L shape when it is present. It never has a negative height contribution. These identities are also immediate by applying the return grammar and reducing each child call before its parent face.

Hence the packet corner ledger can be viewed as a monotone sum of positive strip and L-shaped heights. Equation (1) is stronger in scope: it records all partial histories online, including histories not yet decomposed along their limiting module spine.

## 5. Charges, clocks, and the obstruction to using K as finite fuel

Since a finite mixed difference has zero sum on every row and every column, the exact signed row and column charges of rho_t-rho_0 are determined by D(r_t) alone. Completed packets change none of these exact charges; any charge change is carried by the unreduced symbolic spine.

For lambda>0, finite summation gives

    sum partial_xy K(x,y) lambda^(x+y)
      = (lambda-1)^2 sum K(i,j) lambda^(i+j),

    sum partial_xy K(x,y) lambda^(x-y)
      = -(lambda-1)^2/lambda sum K(i,j) lambda^(i-j).

Thus all four exponential field clocks receive nonnegative contributions from K when their z/u sign conventions are used. The remaining terms are the formal deposition of the reduced word and the usual head correction. This identifies one exact chronological source of the clock positivity; it is not a new proof that their remaining terms are monotone.

For finite black support, however, ordinary mass satisfies

    |B_t|-|B_0|
      = -sigma sum chi(x,y) D(r_t)(x,y)
        -4 sigma sum (-1)^(i+j) K_t(i,j).

The height appears with ALTERNATING plaquette signs. Therefore its pointwise positivity does not bound it by the initial black mass. A long G finger can restore its interior lamps and leave only four corner changes; it can reuse a previously prepared corridor. The mixed-difference operator also has no elliptic maximum principle. These are genuine obstructions to treating K as a finite fuel budget.

## 6. Explicit open global target

The no-interleaving theorem now supplies a proper symbolic lift and a limiting module spine for every ant trace. Equation (1) separates that spine's formal deposition from an online monotone height. A useful next theorem would constrain the interaction of these two terms using a finite initial rho_0, for example ruling out indefinitely reused physical parity chains or proving a finite-state frontier for their support. No such constraint is established here. Proving eventual standard ten-factor membership remains an independent missing step.
