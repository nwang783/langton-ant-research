# Oblique rays cannot occur in a fixed one-level emitter

23 October 2026, 14:02 UTC. Author analytic proof, independent review requested. This is a fixed-center, one-level substitution obstruction on ANY initial coloring. It does not exclude a moving emitter or a hierarchy in which one drifting component emits another.

## 1. Exact architecture

Let a have a fixed finite nonempty physical base word A and image a w, where w is a fixed finite typed word closed at the endpoint pose of A. Besides identity read labels, w may contain finitely many occurrences of component labels b_i. Each b_i has a fixed finite physical base word B_i and exactly the image

    b_i -> U_i b_i V_i,

where U_i,V_i contain only identity read labels. Require exact pose compatibility: U_i preserves the incoming heading of B_i and has nonzero displacement q_i; V_i preserves the final heading of B_i and has displacement -q_i. Thus the depth-n component is exactly U_i^n B_i V_i^n and has the same endpoint pose as B_i. Different occurrences may have different fixed centers, base words, bodies and drift speeds. There is no length, charge, symmetry or initial-mass bound.

If at least one q_i has both coordinates nonzero, the actual rooted limit cannot be an ant trajectory on any board.

The theorem does not claim that every one-level AXIAL emitter is impossible. The separately signed supplied-axial-palette theorem uses its special complete row-transfer contract to cover that case.

## 2. Stabilization at each fixed cell

Exact pose preservation makes every occurrence in w have a fixed center c_i in every refinement layer L_n=phi^n(w). The rooted prefix is

    A L_0 L_1 ... L_(r-1).

For any fixed physical cell p, the complete chronological read string in L_n is eventually independent of n. To see this for one component, its U reads occur at

    c_i + j q_i + u,       0 <= j < n,

for finitely many U-slot offsets u. The base reads occur at c_i+n q_i+b and therefore eventually miss p. Its V reads, indexed in reverse order, occur at

    c_i + m q_i + d_i+v,   1 <= m <= n,

where d_i is the displacement of B_i. A fixed p determines finitely many constant indices j,m. For sufficiently large n all are included, the U events retain their increasing-index order, all precede the V events, and the V events retain their decreasing-index order. The finite concatenation across w and its identities therefore stabilizes too.

If all layers are realized consecutively, that fixed local string repeats forever. Any nonempty repeating alternating binary string has even length. Hence every cell has zero complete field change in every sufficiently late layer.

For one component let delta_i^infinity(p) be its eventual signed field change at p, black indicator after minus before. It is uniquely determined by the component's complete read history whenever that component is legal. Legal chronological overlap causes no ambiguity: complete changes add on the actual successive entry boards. Thus

    sum_i delta_i^infinity(p) = 0                       (1)

outside the fixed root/identity support. If an individual component already fails internally, the proposed root has failed and no further argument is needed.

## 3. Isolate one oblique ray

Choose an occurring oriented oblique ray and let v be its primitive integer direction. Retain precisely the component occurrences with q_i=m_i v, m_i>0. Their centers and finite slot offsets give a fixed-width strip parallel to v. At every sufficiently distant cell of this strip, every component on a different ray is absent: its fixed-width positive ray intersects this strip only in a bounded region, and the opposite ray also stays behind. Identities are absent there too. Therefore (1) becomes

    sum_(i on this ray) delta_i^infinity(p)=0            (2)

throughout the far part of this strip.

For each retained component, delta_i^infinity is eventually q_i-periodic along the strip. This follows from the explicit U/V event coordinates above: far from the near end, adding q_i shifts every U/V copy index by one without changing their local chronological order. Only finitely many orbit classes have nonzero changes.

Every q_i has even checker parity, since U_i preserves its incoming heading and hence has even length. Choose a common longitudinal period Q=M v that is an integer multiple of every q_i. It also has even checker parity.

## 4. Strict positive gain of each oblique bulk profile

Use the independently signed scalar clock in computability/oblique_strip_clock_obstruction.md, with an oblique linear form ell perpendicular to v. After a proper quarter rotation its two coefficients are positive. Its field weight f(p) and heading correction J_h(p) depend only on ell(p), and each actual ant read increases

    Theta=-sigma sum_black chi(p) f(p)+J_h(p)

by at least2. The physical sector sign sigma is the SAME for all component occurrences because they lie in one actual typed word. The global checker character chi also has the same physical-coordinate convention throughout.

For component i define its field-clock gain over depth n by

    F_i(n)=-sigma sum_p chi(p) f(p) delta_i(n,p).

This finite sum is meaningful even on an infinite initial board: only the finitely many changed cells are used. The component's endpoint pose is fixed, so its head-clock difference is a constant H_i independent of n. Therefore

    F_i(n)+H_i >= 2[n(|U_i|+|V_i|)+|B_i|].             (3)

All component reads lie in a fixed normal strip. Their far-bulk history is periodic; the near and far endpoint exceptions have a uniformly bounded number of cells, whose clock weights are uniformly bounded because translation by q_i preserves ell and chi. Consequently

    F_i(n)=n alpha_i+O(1),

where alpha_i is the signed clock gain of its eventual bulk profile over ONE q_i period. Equation(3) gives

    alpha_i >= 2(|U_i|+|V_i|)>0.                       (4)

This is not an inference from observed counts: the U/V slot formulas give the periodic bulk with bounded end exceptions, and the all-time clock supplies the strict sign.

## 5. Contradiction

Sum (2) over one far longitudinal Q-period and the finite transverse support, with coefficient -sigma chi(p)f(p). The result is zero. On the other hand its contribution from component i is

    (M/m_i) alpha_i,

and every such term is strictly positive by(4). This contradiction proves the theorem.

Different speeds on the same ray do not evade the argument: the common-period sum weights each positive bulk profile by its positive integer number of q_i periods. Components on different rays cannot supply a cancellation arbitrarily far along this fixed ray. The argument does not assume that all components have the same endpoint distance or that the full global footprint fits in one strip.

## 6. Scope and constructive implication

This strengthens the older all-cycle-offsets-on-one-oblique-line obstruction only in this precise one-level emitter architecture: it permits many ray directions and arbitrary charge-producing root words, because ray isolation is local. A possible construction using the known oblique hairpin must therefore move the emitter centers, add nonidentity work inside its drifting body, or abandon this fixed refinement architecture. Merely adding finitely many opposed or rotated copies at fixed centers cannot work.

A nested component U_i containing another decorated growing label is OUTSIDE the theorem: its read footprint no longer lies in a uniformly bounded strip around one ray, and the fixed-cell stabilization and isolated-profile formulas need not hold. General decorated flat controllers, nonstationary schedules, and arbitrary ant paths are not excluded.
