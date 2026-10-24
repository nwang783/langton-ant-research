# A periodic limiting core forces a periodic full ant trace

22 October 2026. Independently analytically audited conditional reduction. The full highway conjecture remains open: neither eventual core periodicity nor selection of the standard104 period is proved here.

## 1. Statement

For a finite-seed square ant, suppose its limiting free-product boundary ray is eventually periodic as a sign/exponent word. Then its full turn stream is eventually periodic, with a nonzero Euclidean translation per period.

No bound on G/B decoration lengths or on the decoration-state sequence is assumed. In the diagonal-drift case below, bounded G depths are derived. The axial case follows from the separate packet-crossing bridge, not from an assumption that axial confinement alone implies periodicity.

The proof uses the audited permanent-spine decomposition, the unbounded physical spine, the exact G rail patterns, and the inherited complete-crossing-history/non-axis-strip theorem. It does not classify the resulting periodic word.

## 2. A general diagonal-core criterion

Work after a permanent cut, with finite initial black mass m. Let q_i=(x_i,y_i) be stage roots. Suppose positive integers u,v and finite nonnegative constants Bx,By,Delta,Vx,Vy satisfy:

1. all roots lie in one oblique strip:

       eta_i = v*x_i-u*y_i belongs to [c,c+Delta];

2. past roots never lie too far ahead in either coordinate:

       j<=i implies x_j<=x_i+Bx and y_j<=y_i+By;

3. each integer column contains at most Vx stage-root events, and each integer row at most Vy stage-root events, over the entire tail.

Then all completed G depths are uniformly bounded. Consequently the entire ant tail lies in a fixed non-axis strip, and is eventually translating-periodic.

As in `axial_core_periodicity_bridge.md`, expand B into its four elementary turns and one or two G packets. Each stage has at most three Gs and six elementary turns. Every elementary read and both cells of each G near-end pair lie within l_infinity distance4 of q_i. The only persistent G changes are its four corners. A G of depth n requires n initially black strict-interior cells on one longitudinal rail.

A horizontal G touching row y can only belong to a stage with root row in [y-4,y+4]. There are at most9Vy such stages and at most27Vy such Gs in total. Similarly, at most27Vx vertical Gs touch any fixed column.

All supply arguments below concern EVENT BOUNDARIES after whole Gs or elementary turns. Temporary interior flips cannot act as input to another packet.

## 3. First bound the forward fingers

Consider an eastward G in stage i. Set

    X_i = x_i+Bx+4.

All earlier vertical G supports lie at columns <=X_i, regardless of their unknown lengths: their two columns are determined by near-end pairs at earlier stage roots, and x_j<=x_i+Bx. The same holds for all earlier elementary reads and all horizontal G near-end pairs.

Therefore, on either rail row of the current G, the only possible net black additions at x>X_i before its entry are far corners of earlier horizontal Gs. There are at most27Vy such packets, each changing at most one bit on that row. Together with initial support, there are at most m+27Vy black bits on that row to the right of X_i.

The current near-end column is at least x_i-4. Hence at most Bx+8 of its n strict-interior columns can lie at or left of X_i. The entire black rail must be present at entry, so

    n <= E := Bx+8+m+27Vy.                             (1)

This proves a uniform bound for EVERY eastward G. It does not presume that westward fingers are bounded: their earlier far endpoints are already among the at most27Vy events counted on this row.

Exchanging the coordinate roles gives, for every northward G,

    n <= N := By+8+m+27Vx.                             (2)

Again, no bound on southward fingers was used. Thus there is no mutual assumption or induction on an unproved global depth bound.

## 4. Then bound the backward fingers

Consider a westward G in stage i, and one of its rail rows y. We have |y-y_i|<=4.

Suppose an earlier VERTICAL G touches row y. If it is northward, (2) bounds its depth by N, so its highest row is at most y_j+4+(N+1). Therefore

    y_j >= y-N-5 >= y_i-N-9.

If it is southward, it cannot reach a row above its near-end pair, so y_j>=y-4>=y_i-8, which implies the same weaker bound. Any earlier elementary read on row y, and any earlier horizontal G near-end corner on row y, also have y_j>=y_i-8 and satisfy this lower bound.

The oblique-strip condition yields, for every such possible supplier root,

    v(x_j-x_i)
      = u(y_j-y_i) + (eta_j-eta_i)
      >= -u(N+9)-Delta.

Define the integer

    J = ceil((u(N+9)+Delta)/v).

Every earlier vertical G touching row y, every earlier elementary read there, and every earlier horizontal near-end corner there consequently lies at column at least

    X^-_i = x_i-J-4.

To the LEFT of X^-_i, the only possible net additions on row y are again far corners of horizontal Gs. Their number is at most27Vy, giving at most m+27Vy black bits there at the current entry.

The current near-end column is at most x_i+4. Thus at most J+8 of its strict-interior columns can lie at or to the right of X^-_i. Its black rail gives

    n <= W := J+8+m+27Vy.                             (3)

This argument uses only the already established northward bound, not a bound on southward fingers. In particular, a long southward finger can touch the current row only if its root starts high enough; the core strip then puts that root within the same supplier slab.

Interchanging x and y, a southward G is bounded using the already established eastward bound. Put

    K = ceil((v(E+9)+Delta)/u),
    S = K+8+m+27Vx.                                   (4)

Every southward depth is at most S. The possible westward vertical analogue needs no depth assumption, because it can only reach the current column from a root on the appropriate side.

Together, (1)-(4) give the finite uniform bound

    D = max(E,N,W,S)

for every G depth in the tail.

## 5. Enclose the full trace

Each G starts within distance4 of its stage root and has longitudinal extent at most D+1. Every physical read in the stage is therefore within l_infinity distance D+5 of that root. Consequently every read p satisfies

    c-(u+v)(D+5) <= v*p.x-u*p.y
                   <= c+Delta+(u+v)(D+5).

This is a fixed-width NON-AXIS strip. Section2 of the inherited theorem

`first_principles_2026-10-21/ant_rethink/constructive_alternatives/oblique_strip_pumping.md`

then supplies a translating-periodic full tail. Its proof derives uniform visits from the strip and splices equal COMPLETE crossing histories; no first-arrival or bounded-decoration-state shortcut is used here.

This proves the general diagonal-core criterion in Section2.

## 6. Why every periodic diagonal core meets the criterion

Take a full core period with P stage phases, including both alternating signs as necessary. Its Euclidean action cannot have nonzero net heading rotation or zero translation, because either would make the physical roots bounded. The independently audited theorem `unbounded_physical_spine.md` excludes bounded physical roots. Thus the period acts by a nonzero translation d.

If both coordinates of d are nonzero, a quarter rotation makes d=(u,v) with u,v positive. No reflection or color complementation is needed. The roots have the form

    q_(nP+j) = q_j+n(u,v),    0<=j<P.

The strip coordinates v*q_j.x-u*q_j.y have a finite range, furnishing c and Delta. Let

    Bx = max_j q_j.x-min_j q_j.x,
    By = max_j q_j.y-min_j q_j.y.

For an earlier root the period index is no larger, so these are valid past-retreat bounds. On a fixed row, each phase contributes at most one root because v>0; similarly, on a fixed column each phase contributes at most one because u>0. Thus Vy<=P and Vx<=P. Section2 applies.

If d is axial, the hypotheses instead reduce to a fixed axial core strip with at most P root events per transverse row. The separate theorem `axial_core_periodicity_bridge.md` derives a full strip and uniform full-row visits without bounding all depths a priori, then applies the complete-history theorem. It covers arbitrary finite core width, not just the widths excluded by the separate height9 certificate.

This establishes Section1 in every possible drift direction. Both packet-supply bridges have passed independent analytic audit.

## 7. What remains open

The new implication removes decoration stabilization as an EXTRA hypothesis once eventual periodicity of the limiting core has been proved. It does not prove that the core becomes periodic. The exact corner-consistency equations still allow an unbounded chronological supply network, and finite square support has not been shown to force a repeating core.

Even eventual full translating periodicity would not by itself identify the standard period104 stream. A classification or exclusion of other finite-seed periodic fronts remains a separate necessary step.

The stronger general diagonal criterion also makes the unresolved geometric alternative concrete: a nonperiodic orbit cannot simultaneously have an obliquely confined core, bounded coordinate retreat, and uniform core multiplicities on rows and columns. No one of these properties is asserted for arbitrary finite seeds.

## 8. Elementary converse and exact equivalence

Conversely, suppose a full tail translates periodically, with literal turn period w and nonzero displacement d while preserving heading. Evaluate w in G=C4*C4. Its image under the physical pose homomorphism is a nonzero translation, so this group element has infinite order.

Cyclic reduction in a free product writes

    w = g c g^-1,

where c is cyclically reduced. A cyclically reduced element of syllable length0 or1 belongs to a finite factor and has finite order. Hence c has syllable length at least2, with its first and last factors different. Its powers concatenate without cancellation. Therefore

    w^n = g c^n g^-1

converges to the boundary ray g c c c ... . The finite prefix before the periodic tail merely left-translates this boundary point, changing only a finite initial segment after normal reduction. Prefixes lying inside individual w periods differ from their period endpoints by one of finitely many bounded right words and have the same boundary limit.

The limiting boundary ray is thus eventually periodic. This refers to the reduced-prefix boundary ray used throughout the module construction; coset lamps do not alter the group or its boundary convention. Its eventual syllable exponents are already known to be1 or2 for legal square-ant traces.

Together with Section1, this gives the exact finite-seed equivalence:

    limiting boundary core eventually periodic
        if and only if
    full ant trace eventually nonzero translating periodic.

Neither side of this equivalence has been established for every finite seed. Even a universal proof of either side would still need standard104 selection to settle the stated highway conjecture.
