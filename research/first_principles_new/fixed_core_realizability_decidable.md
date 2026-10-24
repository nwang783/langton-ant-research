# Fixed periodic core realizability is decidable

22 October 2026. Independently analytically audited effective consequence of the periodic-core bridge and fixed-period bounds. This is not a decision procedure for the full highway conjecture: its input includes a fixed candidate periodic core, or a fixed bound on core period.

## 1. Statement and conventions

A core period is a finite cyclic alternating-generator syllable word with exponents1 or2. Its stage length is P. The period must restore the alternating generator sign and physical heading. If repeating the proposed core has bounded physical roots, it is impossible by the physical-spine unboundedness theorem, and is rejected immediately.

For any remaining fixed core word q, it is decidable whether some finite black seed has eventual limiting core q repeated forever, up to cyclic phase, translation and physical rotation. More generally, this is decidable for the finite collection of all core words admitting a period of at most P stages.

The important point is that decorations and the eventual full temporal period are NOT supplied as input. The effective bounds below replace those unbounded existential choices by a finite search.

## 2. Explicit uniform row and crossing bounds

Use the audited bound

    D=30P^2+44P+8.

### Diagonal drift

Rotate so the core period has drift d=(u,v), u,v>0. We have u,v<=P. The core is contained in a strip of normal width Delta<=2P^2 for eta=v*x-u*y. Eventually every G depth is at most D, so every read lies within l_infinity distance D+5 of its stage root. Therefore the full eventual trace satisfies an eta interval of width at most

    W=2P^2+4P(D+5).

At any horizontal row it occupies at most

    H_d=W+1

integer columns. Every row contains at most P stage roots. Every read on row r comes from a root within D+5 rows of r, so at most P(2D+11) stages can contribute. Each stage lasts at most12(D+1)+6 turns. Thus a uniform total read bound per row is

    L_d=P(2D+11)[12(D+1)+6].

Take horizontal cuts separated by v rows. Translating a cut by d translates its allowed column interval by u exactly, so each complete crossing history can be normalized into an alphabet of at most2H_d letters: transverse column and crossing direction. Every history has length at most2L_d.

The initially supplied black field and every finite pre-bound read history can be avoided by taking the cuts sufficiently high. Their outward half-planes are then initially white, and all their crossings satisfy these bounds. This discards finitely many cuts, not a possible infinite family of long decorations.

### Axial drift

Rotate so drift is vertically positive. From the audited axial bound, eventually the trace lies in a fixed strip of at most

    H_a=57P+29

columns and all horizontal G depths are at most R=28P+9. The core has at most P roots per row. Apply the audited axial complete-row-history argument with

    A=9P,
    C=H_a(H_a-1)/2,
    K=C+(C+1)floor(H_a/2),
    L_a=A[12(R+1)+6]+4(A+1)K.

These bounds are valid for sufficiently high rows whose entire histories occur after the eventual strip/depth bound. Old off-strip garbage is not assumed absent; those later histories do not read it. Vertical G depths need not yet be bounded.

Finite row histories imply that the physical head tends to one vertical infinity: it cannot stay in finitely many rows or cross a fixed row infinitely often. The permanent roots tend to positive y, so the physical head must also tend to positive infinity. This verifies the one-endedness premise of the splice theorem.

Use adjacent horizontal cuts. Again each complete normalized history has at most2L_a letters in an alphabet of size at most2H_a.

## 3. A bounded spatial period also bounds the temporal period

For integers H,L define

    S(H,L)=sum_(j=0)^(2L) (2H)^j.

Among S(H,L)+1 successive eligible cuts, two have identical complete crossing histories. The audited pristine-half-plane splice theorem gives two future suffixes related by a positive time shift T and the corresponding positive vertical translation k.

In the axial case k<=S(H_a,L_a). In the diagonal case the cuts are v rows apart, so k<=v*S(H_d,L_d)<=P*S(H_d,L_d). The diagonal translation is a positive integer multiple of d, because histories were normalized by d.

A general counting observation now gives

    T<=kL.                                            (1)

Indeed, write the resulting T-periodic translating read trace as phases p_0,...,p_(T-1), repeated with vertical displacement k. In any sufficiently high block of k consecutive horizontal rows, each phase contributes exactly one read: its unique translate in that block has nonnegative period index. There are therefore exactly T tail reads in that block. The uniform row-read bound gives at most kL. This argument counts all translated periods, and is valid even if an individual temporal period has a very long backward excursion.

Consequently a realizable candidate with P-stage core has an eventual full period no longer than the explicit computable bound

    N(P)=max( L_a*S(H_a,L_a),
              P*L_d*S(H_d,L_d) ).                     (2)

The bound is enormous and is not proposed as a practical search limit. Its role is termination.

## 4. Exact finite-seed test for one translating word

Let w be any finite turn word of length T whose physical heading is restored and whose displacement d is nonzero. Trace its phase read positions p_i, 0<=i<T. Partition them into equivalence classes modulo the subgroup Z*d. In one such class choose a representative p and write p_i=p+k_i*d with integers k_i.

Sort that class's phase letters by decreasing k_i, then by increasing i. This finite list is the chronological list of all reads of a far-forward physical cell by the infinite repetition w,w,...: the corresponding period index is n=m-k_i and the read time is (m-k_i)T+i.

The exact criterion is:

    Every class list starts with R and alternates R,L,R,L,... .       (3)

Necessity follows by choosing a sufficiently far-forward cell of the class outside any finite initial support; its entire history is the displayed list and its first color is white.

For sufficiency, start w at period index0. At a physical cell p+m*d, only phases with k_i<=m occur. This restriction deletes a prefix of the sorted full list, leaving an alternating suffix. If the suffix is nonempty, set that cell's initial bit to the first required color. When m>=max_i k_i the full list startsR, so this initial bit is white; when m<min_i k_i the cell is never read and is also white. Only the finitely many integers min_i k_i<=m<max_i k_i can require black; the lower endpoint is included. There are finitely many classes. The resulting finite seed makes every prescribed read legal, hence realizes w forever. No output-wake pattern is imposed.

This is the inherited independently reviewed criterion from `first_principles_2026-10-21/ant_rethink/defect_dynamics/direct_periodic_chronology.md`, restated here to make the decision procedure self-contained.

Thus (3) is a terminating exact test, not a finite-horizon simulation. Nonprimitive d causes no difficulty: equivalence means an INTEGER multiple of d, not merely collinearity.

## 5. Finite decision algorithm

For fixed q of stage length P:

1. Reject a bounded-root core, including zero drift or a nontrivial finite-order physical rotation.
2. Enumerate all binary turn words w of lengths at most N(P).
3. Keep only heading-returning words of nonzero displacement that pass (3).
4. Compute their cyclically reduced free-product element in C4*C4 and its eventual periodic boundary word. Compare its primitive cyclic syllable word to q's primitive cyclic syllable word, respecting R/L labels. Cyclic phase and physical rotation are allowed; reflection/color complementation is not silently allowed.
5. Answer YES if one matches, and NO after exhausting the finite list.

Correctness of YES is the explicit finite seed from Section4. Correctness of NO follows from the audited bridge, the seed-independent bounds, and (2): any finite-seed trajectory with this eventual core would have a matching full translating period in the enumerated range. Cyclic free-product reduction and finite-word primitive-period comparison are elementary terminating operations.

The same finite search handles any bounded collection of candidate core periods. It does not decide whether an arbitrary finite seed has an eventually periodic core, supply a bound on the eventual core period, or show that the only realizable core is the standard104 core.

## 6. Effective finite fibers, not just a yes/no test

The same finite enumeration lists every primitive translating turn-period compatible with q, up to cyclic phase and physical rotation. A nonprimitive accepted word is replaced by its primitive temporal period. That primitive word must itself restore heading: a nontrivial quarter-turn rotation would have zero displacement after its finite rotational order, contradicting the nonzero translation of the accepted power. Its translation is consequently nonzero as well. Thus the map from finite-seed translating attractors to their periodic reduced cores has an effectively finite fiber over every supplied core q.

In particular, for a fixed q one can decide whether its only compatible translating turn stream is a specified candidate such as standard104. This is a finite mathematical decision procedure, not a classification that has been carried out. Even eventual agreement with the standard reduced core has not yet been shown here to select its unique full104 decoration.

## 7. A bounded finite seed witness

The construction in Section4 also bounds the seed size. In each displacement class, every initially black cell lies between two phase read positions on their common d-line. It therefore lies in the coordinate bounding box of the first-period read positions. For a period of T turns that box has both coordinate spans at most T, so the constructed seed has at most(T+1)^2 black cells and lies within l_infinity distance T of the period's entry position.

Accordingly, a realizable supplied q has a witness seed of at most(N(P)+1)^2 black cells within radius N(P), starting directly on an appropriate periodic turn tail. This does not bound the seed or transient of an arbitrary trajectory that eventually reaches q; it supplies one bounded witness for the existential decision problem.
