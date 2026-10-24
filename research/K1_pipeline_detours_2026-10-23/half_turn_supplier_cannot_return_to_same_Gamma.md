# The half-turned supplier cannot lie on the same selected curve

23 October 2026. Complete WHITE cap-four K = 1 front. Assume the zero-output activated-child half-turn mode of 4670f374, with original D and successor G on the selected maximum curve Gamma. The statement is conditional on that exact physical local mode. It is a continuous-cursor ear obstruction, not an exclusion of off-Gamma half-turned suppliers.

Write alpha = B(D), beta = B(G). Normalize D = (0,0), G = (1,1), J = (-1,-1), P0 = (-2,0), R = (-3,-1), Q1 = (-3,1), Q2 = (-4,0). The actual canonical path is D -> J -> P0 -> R. Its three intermediate faces are strictly LEFT of and off Gamma. In the half-turn mode Q2 has canonical entry w = (-4,1) = SSNS, SW n = (-4,0) = WWEW, SE m = (-3,0) = SNNN and NE k = (-3,1) = EEWE. It is an actual positive duplicator with parent (-5,1), not R.

## 1. Q2 is strictly earlier than G

The signed D opposite-supplier clocks give T1(u) = beta - 4 at u = (-1,1). Complete ordinal ports then give

    T1(g) = beta - 5,       g = (-2,1) = NSSS;
    T0(f) = beta - 6,       f = (-2,2) = EWEE;
    T0(j) = beta - 7,       j = (-3,2) = NNNS;
    T1(k) = beta - 8,       k = (-3,1) = EEWE.

Here g.L1 -> u.L1, f.R0 -> g.L1, j.R0 -> f.R0 and k.L1 -> j.R0 are actual consecutive physical steps. The exact w.L1 -> k.R0 port gives

    B(Q2) = T1(w) = T0(k) - 1
          <= T1(k) - 5 = beta - 13.

No bound relative to alpha is asserted unless Q2 is itself on Gamma.

Suppose it is on the SAME physical lift of Gamma. Its strictly increasing selected births and the fact that D,G are consecutive imply Q2 occurs strictly BEFORE D. It is physically distinct from both. In fact the center displacement D - Q2 = (4,0) requires at least four C-contact edges along Gamma, so the oriented Gamma arc from Q2 to D contains at least two distinct physical selected contacts. Lifted contacts remain distinct even in a short quotient.

## 2. The physical ear

Adjoin to that oriented Gamma arc the four-edge C-contact chord

    D -> J -> P0 -> R -> Q2.

The first three edges are actual canonical edges. The last is the positive contact m, not a canonical edge. The chord is an embedded four-edge zigzag. Its interior is disjoint from Gamma: J,P0,R are off Gamma; its contacts cannot be selected Gamma contacts without putting both endpoint faces on Gamma. Its only meetings with Gamma are D and the hypothesized Q2.

Thus the finite Gamma arc and chord form a Jordan curve. Since the chord lies in Gamma's LEFT component, its bounded ear lies LEFT of the oriented Gamma arc. The chord orientation D -> Q2 also has the ear on its LEFT. The physical cut can be drawn through face interiors and the specified primal contacts, so no other physical lattice read or edge crosses its boundary.

## 3. Complete crossing inventory

Every selected contact on the Gamma arc has exactly its R0 exit and R2 entry; L1 and optional L3 stay on one side. On each of the three canonical chord contacts Z,e,x, the same table holds in chord orientation: R0 exits LEFT -> RIGHT, R2 enters RIGHT -> LEFT, and both retained L reads stay LEFT. Their physical histories are WWEW, NNSN, WWEW.

At the final positive contact m = SNNN, oriented R -> Q2 to the NW, the complete inventory is reversed:

    R0(S): RIGHT -> LEFT, the sole chord entry of this type;
    R2(N): LEFT -> RIGHT;
    L1(N), L3(N): remain LEFT.

There is exactly ONE additional possible entry through m, at m.R0. No omitted one-R, optional L3 or unused corner is available in this fixed local mode.

## 4. Two early exits, at most one entry

Let v_a and v_(a+1) be the first two selected contacts on the Gamma arc from Q2 to D. The K = 1 pipeline gives

    T0(v_a) < T0(v_(a+1)) < T2(v_a).

The R2 times are increasing along the selected curve, so NO Gamma-arc entry has occurred before that second R0 exit. Both exits occur before alpha: their selected target births are no later than B(D), with the incoming R0 strictly before its target L1 birth.

Every R2 entry on the canonical chord occurs strictly AFTER alpha. Indeed each such R2 follows its actual child birth along D -> J -> P0 -> R, whose births strictly increase from alpha. Hence, before the two early Gamma R0 exits, the only possible ear entry anywhere on the boundary is the single m.R0.

Complete translated periodicity puts the actual cursor outside this fixed bounded physical ear for all sufficiently negative times. An actual continuous cursor cannot make two exits from a bounded region having made at most one entry. This is the contradiction.

Therefore Q2 is NOT on the same Gamma. It lies strictly LEFT: the final positive contact m is not on Gamma, so a path from the interior of the already-LEFT R through m into Q2 avoids Gamma. No global halfplane or leftmostness is used.

The result does not put Q2 in the canonical descendant tree of D, does not identify its upper-left parent, and does not make its half-turned route repeat. Different off-Gamma suppliers or other selected components remain possible. No fuel or general K = 1 exclusion follows.

Dependencies: exact half-turn gate 4670f374; original D supplier clocks 9868024f; canonical off-cycle path/uniqueness 4769bd41; K = 1 cursor pipeline 2e940091; bounded-ear cursor interface fe600cde. The boundary and early-entry proof are supplied explicitly rather than inferred from a repaired flow graph.
