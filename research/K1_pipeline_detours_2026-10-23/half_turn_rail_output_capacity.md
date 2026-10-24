# Half-turn rails have a finite aggregate odd-output capacity

23 October 2026. Complete WHITE cap-four front, actual full P,d. This quantitative extension does NOT assume zero output or K = 1. It counts the exact initial half-turn interfaces below, not arbitrary D-shaped faces or renewals. It is an OUTPUT capacity, not an initial-fuel bound.

## 1. Sources, clean steps and the exact residual set

Let H count distinct full-quotient initial rail sources. Each source is an ACTUAL positive all-four duplicator with the displayed initial interface of 45753ce6, up to a quarter rotation and translation:

- D_0 has NW,NE,SE,SW histories SSNS,EEWE,SNNN,WWEW;
- its actual NE child Q1 is terminal, with SW EEWE, NW NNNS, NE EWEE, SE NSSS;
- its associated opposite leaf T_0 has NW SNNN, NE WWEW, SW WEWW, SE SSSN.

All actual parent/child identities in that interface are retained. The canonical incoming contact of D_0 fixes its quarter-rotation frame uniquely.

Let U be the exact residual negative set of f02b2276: q = -1 faces not equal to I of an ACTUAL positive D4. The signed identity and output theorem give

    |U| = N_O + N_D - D4 <= N_odd - n_Sanc,

where the optional n_Sanc family can be set to zero. No particular odd cell is assigned to a U face by this inequality.

At a prospective step with D_n = (x,0), inspect these EIGHT physical cells, in the rail's fixed local frame:

    (x-1,2), (x,2), (x-1,1),
    (x,-1), (x-1,-1), (x-1,0),
    (x-2,1), (x-2,0).

If any has an odd complete history, stop at an odd-cell defect. Otherwise every active new corner is even. A maximum parent with a flag-one child must then have incoming flag one: incoming zero would make it an O producer with an odd canonical entry among the inspected corners. Thus the same seven even profiles as in 45753ce6 apply locally, without assuming other cells of the front even.

The upper candidates reduce by the exact +12 ordinal clock cycle, retaining the full k = EEWE and j = NNNS child histories. The lower a = NNSN alternatives are excluded by the physical canonical cycle. The remaining new R_n is a terminal flag-one leaf with the stable WEWW/SSSN/SNNN/WWEW profile.

If R_n belongs to U, stop at this residual-leaf defect. If it is outside U, it equals I of an actual D4; the unique physical source is D_(n+1). This activates that actual next duplicator and gives the full propagated interface, including its NE degree-one child U_n and the stable opposite leaf R_n.

These are all ways the clean transition can fail: odd canonical entries are included in the inspected parent corners; other odd local helper/child corners are included too; and failure of all-four leaf saturation is exactly R_n in U. No same-Gamma or cross-Gamma ancestry assumption is used.

## 2. Every source stops

If a source never stopped, the exact clean interface would propagate for all n with D_n moving by (-2,0). The proof of 45753ce6 uses only this propagated interface, not zero output at uninspected cells. Nonhorizontal drift gives infinitely many active quotient classes. Horizontal drift eventually translates the initial terminal Q1 with SE NSSS to a later degree-one U with SE SSNS. Both are impossible.

Thus each source has a finite clean prefix and a first stopping D_n, of odd-cell or U type.

## 3. Distinct source rails cannot merge before their stops

Suppose two clean prefixes meet at the same full-quotient D face. Translate one physical lift by an integer multiple of the ACTUAL full drift so the faces coincide. Their canonical incoming contacts fix the same rotation frame. Both spines then run along the same horizontal line in that frame, in steps of two.

If the two source classes differ, one initial source lies strictly farther west on the other's prefix. At that positive prefix index its NE child must be degree one with SE history SSNS. But as an initial source its NE child is terminal with SE history NSSS. Contradiction.

This proves that all spine classes, including first stopping classes, are disjoint for distinct sources. It also rules out quotient recycling within a clean prefix. Different physical rows or orientations do not evade the argument: once a common quotient face is aligned, its unique canonical entry aligns the frames and rows. No primitive drift assumption is used.

## 4. Defect multiplicities

For an odd-cell stop, the inspected offsets from the lower-left index of D_n are

    S = {(-1,2),(0,2),(-1,1),(0,-1),
         (-1,-1),(-1,0),(-2,1),(-2,0)}.

Rotate physical cell offsets about the face center (1/2,1/2). The union of the four rotated sets has exactly TWENTY distinct offsets:

    (-2,0),(-2,1),
    (-1,-1),(-1,0),(-1,1),(-1,2),
    (0,-2),(0,-1),(0,2),(0,3),
    (1,-2),(1,-1),(1,2),(1,3),
    (2,-1),(2,0),(2,1),(2,2),
    (3,0),(3,1).

A fixed odd cell class can therefore be incident to at most twenty distinct stopping D_n classes. Choose one inspected odd cell for each odd stop. Since stopping D classes are distinct, the number of odd stops is at most 20 N_odd. Quotient identifications can only reduce the twenty candidate classes.

At a U stop, the residual leaf R_n has unique ACTUAL canonical parent D_n. Hence one U class determines at most one stopping D class, and therefore at most one source. The number of U stops is at most |U|.

Consequently

    H <= 20 N_odd + |U|
      <= 21 N_odd - n_Sanc.

In particular H <= 21 N_odd holds without any optional K = 1 family. The zero-output half-turn exclusion is recovered by setting N_odd = 0.

## 5. Scope

This bounds exact initial half-turn sources, not all maximum branches. The constant is deliberately a safe geometric multiplicity, not claimed sharp. It is an aggregate output lower bound; no injection into original black seed cells or a specific one-output-per-source assignment is asserted. Do not add it to overlapping odd-output counts: combine with those by maximum unless disjointness is proved.

An actual half-turn gate origin determines its displayed D_0 by a fixed displacement and frame, so a family of distinct such complete gates may be counted through these distinct source classes. This statement still requires the complete terminal NE-child and opposite-leaf interface; it cannot be applied to a relaxed RIGHT-turn row or an unconnected synthetic table.

Dependencies: signed rail interfaces and periodicity proof 45753ce6; exact U residual/output theorem f02b2276; global canonical flag inventory d1f7304b; opposite-I source recovery 9868024f. The local clean rules are exactly the signed rail rules with odd/U interruptions retained explicitly. No new front or parameter scan is used.
