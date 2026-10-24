# Ordered maximum curves force an output contact or lower counterflow between them

23 October 2026. Complete WHITE cap-four K = 1 front, actual full P,d. Let D_norm = ||d||_infinity. This is a conditional geometry/current theorem for two or more DISJOINT selected maximum-C curves. It does not claim another such curve exists, or rule out cross-Gamma supplier transfer.

## 1. The sharper L-sublevel barrier

At a selected flat maximum contact, the complete local possibilities have unshifted L heights

    RLR:                         M-1 and M-2;
    RLRL, equal L headings:      M-1 and M-3;
    RLRL, opposite L headings:   M-2 and M-2.

Thus at least ONE incident L height is at least M-2. Consequently an L-contact path in the sublevel

    h(L) <= M-3

cannot cross a selected maximum-C curve. A crossing occurs only at a primal contact and would require BOTH incident L faces to be in the sublevel, contrary to the table. This is stronger than a lower bound on each individual L face.

If the selected LEFT-L3 flag is one, its LEFT L face has height exactly M-3, and its RIGHT L face has height M-1. The signed constant-zero theorem ensures every K = 1 selected curve has at least one such flag-one contact, with arbitrary maximum branches retained.

## 2. A lower minimum in the intervening band

Let Gamma_L and Gamma_R be disjoint selected maximum curves, both oriented in original drift direction, with Gamma_L strictly LEFT of Gamma_R. At a flag-one contact of Gamma_R the M-3 L face lies in the intervening open band. A small LEFT sector at that contact belongs to the band; the other C curve does not touch that contact. Since no C-contact curve enters the interior of an L face, the whole open L face is in the same band.

Its component S of {h <= M-3} stays between the two curves by the barrier. It has finitely many full-quotient classes. Choose a minimum m in S and a connected height-m plateau Q there. Then m <= M-3 = c_left-1. Every lower neighboring L face would also belong to S, so Q is locally minimal in the entire L lattice, not just relative to the band.

Either Q touches an original odd-output corner, or the prepared reverse plateau theorem supplies a reverse selected L curve inside Q. In the second case the reverse curve is disjoint from and between the two C curves, at height m, with K_rev = c_left-m >= 1.

An odd corner incident to Q cannot lie on either C cut: a selected RLR odd contact has L heights M-1 and M-2, while every selected contact incident to an M-3 L face is the even four-read equal-L case. Thus the retained odd-output contact is strictly in the intervening band. It is output, not initial fuel.

## 3. Four disjoint physical currents

In the odd-output-free minimum case, order the three cuts as

    C at M, L at m, C at M.

They partition physical flow into four nonnegative balanced integer band currents. Define their stream potentials, up to irrelevant additive constants, as follows:

1. h-M left of the left C cut, zero to its right.
2. zero left of the left C cut; h-M between it and the L cut; m-M right of the L cut.
3. zero left of the L cut; h-m between it and the right C cut; M-m right of the right C cut.
4. zero left of the right C cut; h-M to its right.

Their sum is h-M. At each cut the two definitions agree because its face height is the specified constant. As in the signed three-current proof, every physical edge's whole multiplicity belongs to exactly one band current. No diagonal edge is subtracted, and no overlapping chronological budget is added.

Their original-drift homologies are respectively

    M-c_left = 2;
    m-M = -(M-m);
    M-m;
    c_right-M = -1.

They sum to one. The checker-axis length lower bound therefore gives

    P >= 2 D_norm [3 + 2(M-m)] >= 18 D_norm.

If the middle minimum is at most M-5, this same register yields P >= 26 D_norm. These are physical partition bounds, safely combined with old overlapping clocks only by maximum.

## 4. An ordered-family capacity

Suppose there are r disjoint selected maximum curves, ordered LEFT to RIGHT, in the full quotient. Apply section 2 to each of the r-1 intervening bands. Call a band rooted if its chosen lower minimum touches odd output; otherwise choose its qualified reverse L curve.

Odd contacts chosen in distinct rooted bands represent distinct full-quotient classes: the bands are disjoint and invariant under the actual full drift, and those contacts are not on the C boundaries. Thus at most N_odd bands are rooted. If u is the number of unrooted bands, then

    u >= max(0, r-1-N_odd).

Partition physical flow across all ordered C cuts and all u reverse L cuts. A band without an inserted reverse cut has total homology zero. Every inserted reverse cut contributes the two disjoint middle homologies -(M-m_i), M-m_i, with M-m_i >= 3. The two exterior homologies remain 2 and -1. Hence

    P >= 2 D_norm [3 + 2 sum_i (M-m_i)]
      >= 6 D_norm + 12 D_norm max(0, r-1-N_odd).

This is a capacity per distinct SPATIAL band, unlike a per-renewal claim: different routes may still share one minimum within a band. It is not a bound by original black roots, a general K = 1 exclusion or an assertion that supplier ancestry moves to another component. A half-turned supplier may remain in the same canonical component off the selected curve. Cross-Gamma transfer, when it really uses different selected curves, retains precisely this output-contact or physical-current cost.

Dependencies: complete flat max-contact heights from fd20e425 and the signed maximum-port theorem; constant-zero exclusion 71abcb4a; prepared reverse plateau ab9fad0a; physical stream partition f3a81d5f and checker-axis homology bound. No new finite history scan is used.
