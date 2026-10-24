# Actual outward duplicators fail only at a bounded output-defect set

23 October 2026. Complete WHITE cap-four translating front, actual full quotient. This is the quantitative version of zero-output saturation. It does NOT assume N_odd = 0 and does not bound output by original fuel.

## 1. A precise residual negative set

Let U be the set of faces with q = -1 that are NOT equal to I(D) for an actual positive all-four duplicator D. Each of the D_4 such duplicators has a distinct actual flag-one I leaf. The finite flag identity therefore gives the exact count

    |U| = N_O + N_D - D_4
        = N_O + D_C + D_H + D_S.

The signed output partition implies

    |U| <= N_odd - n_Sanc,

when the optional previously signed singleton-ancestor family is present; set n_Sanc = 0 otherwise. This is an exact residual set and an aggregate output-capacity upper bound, not a constructed injection from U to particular output cells.

All negative faces outside U are known terminal I leaves of actual positive D_4 sources. There are no nonleaf negative exceptions outside U.

## 2. Quantitative actual-child activation in outward late routes

Take any family of distinct actual late canonical routes D -> J -> P0 -> I with outward Q1 at M, as covered by the new outward-leaf theorem. Their Q1 leaves are distinct by the physical D -> Q1 injection.

If a Q1 is outside U, it equals I(D') for an actual positive D_4. The complete physical overlap analysis excludes both SSNS/EEEW profiles and the singleton NSSS/EWEE profile. The only remaining square is

    k = EEWE, j = NNNS, f = EWEE, g = NSSS,

and physical recovery forces D' = P0. Thus P0 is an actual positive all-four duplicator and its left WWEW contact is an actual canonical child, not merely a possible port.

Consequently at most |U| <= N_odd - n_Sanc of the outward source classes can fail this precise activation. Every unactivated source injects into U by its Q1 leaf. Every activated source injects into a distinct actual D_4 face P0 through the inverse I association.

This is stronger than a zero-output statement but weaker than charging each source a fresh odd cell. Different activated descendants may still belong to the same maximum component, and the output-defect capacity can overlap other output counts. No recursion follows unless the activated descendant's own canonical parent path is separately proved.

## 3. Selected-cycle consequence with off-cycle suppliers retained

For selected-Gamma sources, each activated P0 is off Gamma, by the actual canonical path D -> J -> P0 and parent uniqueness. In particular it is distinct from every selected-Gamma D_4 source. With n_L exact late Gamma sources and outward subset n_Lout, this gives a literal source partition:

    outward sources with Q1 in U;
    OR distinct off-Gamma actual D_4 descendants P0.

Hence n_Lout <= |U| + (D_4 - n_L), consistent with the stronger signed flag/output inequality that also retains the early leaves. This is an actual-source geometry statement behind that capacity inequality. It does not remove the remaining off-Gamma D_4 term.

Under zero output, U is empty and the one-step activation holds for every outward route, recovering 56b51121. The subsequent repeat-versus-half-turn extension is separate and does not need to be imported for this theorem.

Dependencies: finite flag balance d1f7304b; output partition bf0785e8; D_4-to-I injection and terminal status 9868024f; outward Q1 leaf, injection and physical overlap 6d7d60d4; selected off-cycle placement 4769bd41. No new local enumeration or exterior realization is used.
