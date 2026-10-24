# Uniformly bounded core dwelling in a fixed-size box

22 October 2026. Independently analytically audited strengthening of the bounded-root packet lemma. The application is to remove an extra line-multiplicity assumption from the diagonal-core bridge, not to prove global core confinement or bounded retreat.

## 1. Uniform finite-interval statement

Let a finite consecutive interval of COMPLETE permanent stages have all its stage roots in an integer rectangle Q of width w>=1 columns and height h>=1 rows. No assumption is made about any stage outside this interval or about the sizes of its completed G decorations.

There is a bound U(w,h), independent of the rectangle's location, the initial black mass, the starting colors, and the decoration depths, on the number of stages in the interval.

Here is an explicit, intentionally enormous bound. Put

    W = w+8,    H = h+8,
    C(r) = r(r-1)/2,
    F(r) = [C(r)+1] floor(r/2),
    F = 2F(W)+2F(H),
    A = (w+10)(h+10),
    U(w,h) = (F+1) 4A 2^A.                            (1)

## 2. Bound the exceptional packets

Expand B into elementary turns and G children. Every elementary read and G near-end pair lies in Q0=Q+[-4,4]^2, whose width and height are W,H. Let Q1=Q+[-5,5]^2, of area A.

Call a G exceptional if its read support leaves Q1. An eastward exceptional packet must end strictly beyond the first column immediately right of Q0. At that column, only eastward Gs can read; every elementary turn and every other packet orientation is on the root side or has transverse coordinates within Q0.

The finite-interval version of the one-sided endpoint argument in `unbounded_physical_spine.md` applies without change. At most C(H) packets end at this column. Between these events there are at most floor(H/2) eligible disjoint rail pairs, each admitting at most one far endpoint beyond the column. Thus at most F(H) exceptional packets extend east, and at most F(H) west. Similarly, at most F(W) extend north and F(W) south. In total there are at most F exceptional packets.

This count does not assume an infinite extension with roots in Q. It bounds every finite packet sequence directly by the finite range of the signed endpoint moment. Arbitrary colors inherited from before the interval are permitted.

## 3. Bound ordinary pieces by finite complete states

Delete the exceptional packets as indivisible intervals of time, leaving at most F+1 ordinary pieces. This deletion is only a counting operation; the pieces are not concatenated or asserted to form a legal new ant path.

Within an ordinary piece every read lies in Q1, and the head at each update boundary lies in Q1. Elementary turns read in Q0 and move at most one unit, while ordinary Gs have support and return pose in Q1. All lamps outside Q1 stay fixed during that piece.

A local state is the Q1 bit mask plus a head position and heading in Q1. There are at most4A*2^A such states. If one repeated within the same ordinary piece, the outside lamps would also be identical, so a COMPLETE square-ant state would repeat. Determinism would make the future periodic in a bounded set, contradicting the already established finite-seed unboundedness theorem. Therefore an ordinary piece has at most4A*2^A updates.

Each complete permanent stage contributes at least one permanent core turn, which is an elementary update outside every exceptional G. Thus the number of stages is at most the total number of ordinary updates, bounded by (1). This proves Section1.

The exceptional Gs may themselves have arbitrarily many updates, and their outside effects may differ between pieces. Neither fact affects the count: there are uniformly few exceptional Gs, and no comparison of states ACROSS different ordinary pieces was made.

## 4. Oblique confinement plus bounded retreat supplies line multiplicity

Suppose the permanent roots lie in

    c <= v*x_i-u*y_i <= c+Delta,

where u,v>0, and their longitudinal coordinate has bounded retreat:

    j<=i implies y_j<=y_i+B.

The strip relation then also bounds x retreat by (uB+Delta)/v.

Fix an integer row r and any two root indices j<=i on that row. For every k between them, the retreat inequality applied to (j,k) and (k,i) gives

    r-B <= y_k <= r+B.

The strip confines x_k to an interval of length at most (2uB+Delta)/v. Hence the entire stage interval from j through i has roots in a rectangle of uniformly bounded dimensions. A safe choice is

    h_* = 2 ceil(B)+1,
    w_* = ceil((2uB+Delta)/v)+2.

Section1 gives at most U(w_*,h_*) root events on row r. If there were infinitely many, applying the finite bound between the first and arbitrarily late visits would be a contradiction. This is a uniform TOTAL row multiplicity, not merely a bound during one excursion.

The same argument with coordinates exchanged and the derived x-retreat bound gives uniform total column multiplicity.

Therefore the assumptions of the diagonal criterion in `periodic_core_decoration_stabilization.md`, Section2, hold. It follows that all G depths are bounded and the full ant is eventually translating-periodic.

## 5. Resulting stronger conditional bridge

A finite-seed ant whose permanent core is eventually confined to a fixed non-axis strip AND has bounded retreat along that strip has an eventually translating-periodic full trace. No separate line-multiplicity or decoration-size assumption is needed.

Neither premise is proved for arbitrary finite seeds. In particular, confinement alone does not supply bounded retreat: excursions can leave every fixed local rectangle and later return. The finite-interval dwelling bound cannot be summed over such separated visits without the bounded-retreat hypothesis.

## 6. Axial version and combined strip statement

If the core instead lies in a fixed vertical strip and satisfies y_j<=y_i+B for j<=i, the interval between two roots on row r has all roots in that same fixed column band and rows[r-B,r+B]. Section1 therefore gives uniform total row multiplicity. The independently audited axial bridge applies. Rotate for a horizontal strip.

Thus, in either axial or non-axis directions, core confinement to a fixed-width strip together with bounded longitudinal core retreat suffices for full translating periodicity, without a separately assumed decoration or line-multiplicity bound. The non-axis proof above is stated with positive rational direction coordinates u,v; its inequalities also hold verbatim for positive real u,v, since only positivity, the strip relation, and ceiling bounds are used. Quarter rotations cover the other directional quadrants.

An irrational-slope core strip with bounded longitudinal retreat is consequently impossible: the resulting full translating tail would have a nonzero integer drift parallel to that strip. This remains a conditional exclusion, not a proof that every core has a rational asymptotic direction.
