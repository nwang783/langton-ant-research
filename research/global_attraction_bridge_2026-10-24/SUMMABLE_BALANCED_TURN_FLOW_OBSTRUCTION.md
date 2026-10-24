# A summable stationary flow survives the one-site alternation relaxation

24 October 2026. Explicit abstract countercontrol; independent audit pending. This is NOT a Langton ant trajectory, a finite seed, or a recurrent ant construction.

## 1. The precise candidate being refuted

The signed visit-flow hierarchy uses the fixed directed checkerboard lattice and actual R/L alternation. On taking time-normalized visit counts, it is tempting to retain only:

1. nonnegative directed edge and turn flows;
2. flow conservation at every physical cell;
3. equal total R and L turn flow at every cell;
4. compatibility of each turn with its two incident directed edges.

The following explicit nonzero flow satisfies all four conditions and has FINITE total flow, with exponentially decaying spatial tails. Thus those stationary one-site conditions alone cannot rule out a localized probability profile or prove zero asymptotic occupation of every finite box. Any such proof must retain stronger chronological or global constraints of the deterministic ant.

No existence of a deterministic ant orbit realizing this flow is claimed. In particular, equality of R/L frequencies is much weaker than alternation at EVERY successive visit.

## 2. Closed-form construction

Index unit faces by their lower-left corner f=(i,j). Choose

    1/3 <= r < 1,
    A_f = r^(|i|+|j|).

Each physical edge separates two faces f,g. Give its sector-permitted direction the flow

    E_edge = A_f + A_g.

At a physical vertex v there are four surrounding faces. For any one of them f, let f_op be the diagonally opposite face and f_1,f_2 the two adjacent faces at v. Give the unique sector-permitted turn around that corner face the flow

    T_(v,f) = (3 A_f + A_(f_1) + A_(f_2) - A_(f_op))/4.       (1)

Every perpendicular incoming/outgoing pair is precisely one such face corner. The two opposite corner faces have the same turn letter; the other two have the other letter. This remains true in both checkerboard sectors, with R/L exchanged when appropriate.

### Nonnegativity

At any vertex the four face weights, up to a common positive factor u and a rotation/reflection, are

    u, ur, ur, ur^2.

The smallest corner's numerator is

    u(3r^2+2r-1) = u(3r-1)(r+1) >= 0.

The largest corner's numerator is u(3+2r-r^2)>0, and either middle numerator is u(r+1)^2>0. Thus (1) is nonnegative for every vertex. All turns are strictly positive when r>1/3.

### Exact edge matching and conservation

For adjacent faces f,g at a vertex, their two corner turns are exactly the two turns using the edge between them. Direct addition gives

    T_(v,f)+T_(v,g)=A_f+A_g=E_edge.

The same value is assigned at the other end of the physical edge. Hence incoming edge flow equals outgoing edge flow, and every edge/turn incidence matches exactly.

The total turn flow at v is the sum of its four surrounding A values. The sum of the two opposite corner turns is one HALF of that quantity. Therefore total R flow equals total L flow at every cell, exactly, not just approximately.

### Finite total mass

The face sum is

    sum_f A_f = ((1+r)/(1-r))^2.

Each face borders four physical vertices, so

    sum_v sum_f T_(v,f) = 4 ((1+r)/(1-r))^2 < infinity.        (2)

Divide all edge and turn flows by this finite constant. The resulting head occupation profile is a probability distribution, strictly positive at every cell, with exponential tails. For r=1/2, the normalization is36; the head weight at v=(0,0) is1/16.

## 3. Relation to the new finite-interval hierarchy

For any choice of one horizontal and one vertical predecessor edge, the unique turn avoiding both is one letter. Equal R/L totals therefore imply the zero-error version of the local exceptional-turn inequality. Matching those incidences to directed edge flows gives the corresponding stationary predecessor inequalities.

Thus the stationary limit of the new local visit-count inequalities is compatible with this summable profile. The finite-interval confinement theorem remains valid: its constant and endpoint terms, actual chronology, and finite support of the interval's head trace supply the constructive escape bound. The present infinite spatial flow is not confined to any finite rectangle.

This is a precise obstruction to a proposed frequency-only upgrade, not a counterexample to the confinement theorem or to finite-seed attraction. A finite ant might have no such occupation limit. Establishing that would require information absent from this relaxation, such as chronological correlations of successive arrivals, full color transport, or an independently justified nonlocal invariant.

## 4. Verification

The checker uses exact rational arithmetic at r=1/2 on a fixed finite range to verify every directed edge incidence, equal R/L balance in BOTH sectors, and the local predecessor inequalities in all four orientations. It separately verifies the three symbolic numerator types and the exact infinite normalization formula. The all-lattice claim is the closed-form proof above, not finite-range extrapolation.
