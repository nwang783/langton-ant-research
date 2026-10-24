# Seed-independent eventual bounds for a fixed core period

22 October 2026. Independently analytically audited effective corollary of the periodic-core bridge. The estimates below are deliberately loose. They do not enumerate or classify all possible full periods.

## 1. Period convention

Let a limiting core tail repeat after P complete stages, with the alternating generator sign and the physical heading also restored. Its nonzero translation is d. The physical stage-root increment has l_infinity norm at most1: one core turn moves one lattice edge, while two identical turns move to an adjacent diagonal cell. Thus within a P-stage period, each coordinate range is at most P and |d.x|,|d.y|<=P.

The period may be enlarged to include both signs. A nonzero heading rotation or zero translation would give bounded roots and is already excluded by the physical-spine theorem.

## 2. Diagonal case: remove the initial mass from eventual bounds

Rotate so d=(u,v), with u,v positive integers. Use the notation of `periodic_core_decoration_stabilization.md`. Choose the valid, not necessarily minimal retreat constants Bx=By=P, and take Vx,Vy<=P. The coordinate ranges are at most P, so

    Delta<=u*P+v*P<=2P^2.

The analogous inequality in terms of MINIMAL retreat constants need not hold: a monotone staircase can have zero retreat but nonzero oblique-strip width. Only the chosen P bounds are used below.

Fix the initial cut at the beginning of this periodic core, with finite black set B0. Since both root coordinates tend to positive infinity, every sufficiently late horizontal rail row is above all rows of B0, and every sufficiently late vertical rail column is right of all columns of B0.

In the forward supplier proof, the only use of m was to count initial black bits on the CURRENT rail row or column. That contribution is therefore zero for all sufficiently late packets. All earlier horizontal/vertical far-corner additions remain covered by the same total line-multiplicity count. Consequently

    E0=Bx+8+27Vy,    N0=By+8+27Vx

are valid eventual forward depth bounds, each at most28P+8.

There are only finitely many north packets before the N0 bound starts, and only finitely many east packets before E0 starts. Each is a finite completed word. Add their finite read supports, along with B0, to a finite exceptional set F. At all sufficiently late stage roots, neither current horizontal rail row nor current vertical rail column intersects F.

Now revisit the backward supplier proof. An earlier exceptional north packet cannot supply the current horizontal rail because that rail misses its entire read support. Every remaining north packet has depth at most N0. The same supplier calculation therefore applies with N=N0, and with no initial black term on the current row. It gives

    J0=ceil((u(N0+9)+Delta)/v),
    W0=J0+8+27Vy.

The south bound analogously uses E0:

    K0=ceil((v(E0+9)+Delta)/u),
    S0=K0+8+27Vx.

All exclusions are retrospective statements about finitely many early packets, not assumptions that future decorations already stabilize. The permanent roots are known to advance by the hypothesized core period, independently of decoration duration.

Since u,v>=1 and u,v<=P,

    J0,K0 <= P(28P+17)+2P^2 =30P^2+17P.

Thus every sufficiently late G has depth at most

    D(P)=30P^2+44P+8.                                  (1)

This bound depends only on the chosen core stage period P, not the seed mass or the length of its transient.

## 3. Axial case: a seed-independent eventual strip

Rotate so d is vertical. The permanent core has column width at most P+1 and at most P root events on every row. In the axial bridge,

    H0 <= P+9.

Again, every sufficiently late horizontal G uses rail rows beyond all rows of B0. The row-supply estimate therefore loses its initial m term, while vertical G effects remain within the H0-column core band and earlier horizontal corner additions remain bounded by27P. Hence all sufficiently late horizontal depths are bounded by

    R0 <= H0+27P <=28P+9.

All subsequent physical reads then lie in a vertical strip of width at most

    H0+2(R0+1) <=57P+29.                               (2)

Earlier packets may have visited arbitrarily distant columns, and old black bits may remain there. They are not included in this eventual strip claim; the derived bound shows that the later trace does not read them. The separate axial crossing proof still supplies uniform row multiplicity and full translating periodicity.

## 4. Effective but not practical classification consequence

For each fixed P, (1) gives a seed-independent finite decoration alphabet for diagonal periodic cores, and (2), together with the axial crossing bound, gives a seed-independent finite complete-history bound for axial cores. The inherited splice theorem then provides a finite theoretical bound on an eventual full turn period, depending only on P.

This does not make an unbounded search over all P finite. Nor has the resulting enormous bound been used to enumerate a complete class. A proof that every finite seed has a periodic core, or a proof excluding all nonstandard periodic core classes, remains open.
