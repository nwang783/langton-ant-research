# Axial core confinement plus bounded row multiplicity forces a periodic tail

22 October 2026. Independently analytically audited conditional theorem. No bounded-decoration hypothesis is imposed. This is not a proof of standard104 attraction, nor an exclusion of all wide axial fronts.

## 1. Precise hypothesis and conclusion

Restart a finite-seed square ant at a permanent-spine cut, after any optional B at that root. Let q_i be its permanent stage roots. A stage has exponent1 or2 and alternating sign. The completed decorations return to their entering physical poses, so the roots are the poses of the undecorated core.

Assume there are integers a<=b and V>=1 such that, on this entire tail:

1. every root q_i has a<=q_i.x<=b;
2. for each integer y, at most V indices i satisfy q_i.y=y.

Then the full ant trace has an eventually translating-periodic tail, with nonzero vertical drift.

Hypothesis2 is a uniform bound on the TOTAL number of stage-root events on each row, not a density bound, not eventual avoidance of each individual row, and not an assumption about only one chosen representative per repeated root. The roots need not initially move monotonically, and the decorations may initially have unbounded proposed lengths.

An eventually periodic core with nonzero axial Euclidean translation satisfies both hypotheses, after a rotation if necessary. That corollary is proved in Section6.

## 2. Packet geometry and constants

Expand every B into its four elementary parent-face turns and its one or two completed G children. Each stage then has at most three G packets and at most six elementary turns. All elementary read sites and both cells of every G's near-end pair lie within l_infinity distance4 of the stage root. The slack4 follows directly because the next core root is at distance at most2, a B parent face has radius1, and a G near-end pair is a parent/child boundary. The sharper local radius is unnecessary.

For every G_a(n):

- its support is a width-one rectangle with longitudinal extent n+1;
- its net mask is the four corners;
- every strict-interior cell is read twice and restored;
- one longitudinal rail contains n distinct initially black strict-interior cells;
- on a line transverse to its axis it makes at most four reads.

Write m for the finite black mass at the chosen cut, and set

    H0 = b-a+9,
    R  = H0 + m + 27V,
    H  = H0 + 2(R+1).

Thus the integer column band I0=[a-4,b+4] has H0 cells per row. All elementary turns, all G near-end pairs, and the entire support of every VERTICAL G lie in I0.

We will use event boundaries in the expanded program: before and after each complete G or elementary turn. Temporary interior flips during a G are not treated as persistent changes.

## 3. The horizontal decorations are uniformly bounded

Fix a row y. A horizontal G touching that row belongs to a stage whose root row lies in [y-4,y+4]. Hypothesis2 gives at most9V such stages, and each contains at most three Gs. Therefore at most27V horizontal G packets touch row y over the WHOLE tail.

Outside I0, a horizontal G's only net change on row y is at most one far-end corner. Vertical Gs and elementary turns make no changes outside I0. At every event boundary, the number of black cells on row y is consequently at most

    H0 + m + 27V = R.

This estimate permits arbitrary initial black placement, counts all possible additions, and does not assume mass monotonicity. It also holds at a G's entry, even when the G occurs inside a B.

Every horizontal G_a(n) requires n black cells on one of its two rail rows at entry. Hence n<=R. Its support is therefore contained in the fixed column interval

    I = [a-4-(R+1), b+4+(R+1)],

which has H columns. All other events were already inside I0. The ENTIRE physical tail lies in I.

Only horizontal finger depths have been bounded at this point. Vertical fingers may still be arbitrarily long. The next section controls their crossings without presupposing a depth bound.

## 4. Uniform full-trace row multiplicity

Fix an arbitrary integer row z. Call a stage near if its root row is in [z-4,z+4]. There are at most

    A = 9V

near stages. Their complementary maximal intervals of consecutive stages number at most A+1. Each such interval lies entirely on one side of row z: consecutive core roots move by at most2, so they cannot jump over the nine-row near band.

Consider an interval above z. Every elementary read and G near-end pair is strictly above z; horizontal Gs cannot touch z. Only southward G packets can reach z. The interval below z has the rotated, northward version of the same argument.

Use the one-sided endpoint lemma from `unbounded_physical_spine.md`, rotated so its transverse finite band is the H columns of I. For completeness, its exact counting mechanism is:

- a packet ending at z changes the signed first moment of row z by one unit with a fixed sign;
- that moment has total range width at most C=H(H-1)/2;
- therefore at most C packets end exactly at z;
- between these endpoint events, row-z colors at EVENT BOUNDARIES are fixed;
- packets continuing strictly across z require one fixed oriented01 pattern on their two-column pair;
- eligible adjacent pairs are disjoint, so there are at most floor(H/2) pairs;
- for each pair, at most one packet can end strictly beyond z before a row-z endpoint event: its equal-colored far end is a barrier that other eligible, disjoint pairs cannot repair.

The fixed pose sector makes the required equal far-end color independent of a packet's starting row. All other events in the interval stay on the root side of z, so none can repair the opposite-side barriers. This is why a whole one-sided interval, not an arbitrary mixed-direction packet list, is used.

Thus at most

    K = C + (C+1) floor(H/2)

packets in one interval read row z. Each is vertical, so each contributes at most four row-z reads.

During one near stage, a vertical G contributes at most four row-z reads. A horizontal G has total length at most4(R+1), so certainly contributes no more than that number. The six elementary turns add at most six. Hence a near stage contributes at most12(R+1)+6 reads of z.

The total number of physical reads on ANY row z is bounded uniformly by

    L = A [12(R+1)+6] + 4(A+1)K.                       (1)

This establishes a uniform full physical row-visit bound, not merely a permanent-core bound. In particular, every physical cell is visited at most L times on this tail.

## 5. Complete crossing histories give translation

The trace lies in H columns, and each horizontal row has finitely many visits. It cannot remain in finitely many rows. It cannot visit arbitrarily large positive and negative y repeatedly, because it would then cross a fixed row infinitely often. Therefore y tends to one infinity; rotate by a half turn if needed so it tends to positive infinity.

Every horizontal cut has at most2L crossings, since either adjacent row contains all departure events associated with those crossings. The transverse coordinates of crossings lie in an interval of diameter at most H-1.

The inherited complete-crossing-history theorem now applies after exchanging x and y. Its source is

`first_principles_2026-10-21/ant_rethink/constructive_alternatives/oblique_strip_pumping.md`, Section1.

For sufficiently far cuts the initial outward half-planes are white. There are finitely many complete crossing-history types. Two equal histories can be spliced; deterministic equality of the resulting run with the original gives two infinite suffixes related by a nonzero lattice translation and a positive time shift. Since the entire tail is in a fixed vertical strip, the translation's horizontal component must be zero. This proves the theorem.

No bound on future retreat was assumed. Complete histories, including all returns, are essential; matching first arrivals would not justify this step.

## 6. Eventually periodic axial core corollary

Suppose the limiting core's stage/sign/exponent word is eventually periodic. Take a period containing an even number of syllables if needed to preserve the alternating sign. Repeating its Euclidean motion either:

- has nonzero net heading rotation, in which case the roots stay bounded;
- has zero heading rotation and zero translation, again giving bounded roots; or
- has zero heading rotation and nonzero translation d.

The first two alternatives are excluded by the independently audited physical-spine unboundedness theorem in `unbounded_physical_spine.md`. Thus only the third remains.

If d is axial, rotate so d=(0,d_y), d_y!=0. For P stage phases j, the tail roots are

    q_(nP+j) = q_j + n*d.

Their x coordinates occupy one fixed finite interval. For each phase j and each integer row y, the equation q_j.y+n*d_y=y has at most one integer solution n. Therefore every row contains at most P stage roots: the theorem applies with V=P.

Consequently:

    Eventually periodic boundary core with axial drift
    implies eventually translating-periodic full ant trace,
    without any a priori bound on decoration lengths or states.

The implication does NOT assert that every core is periodic. Nor does it classify the possible axial full periods or identify the standard104 word, whose drift is diagonal.

## 7. Compatibility with the finite-width obstruction

The existing independently audited pristine-block certificate excludes any finite-seed tail confined to nine or fewer horizontal rows, or nine or fewer vertical columns after rotation. Its source is `frontier_exploration/column_exclusion_rank.md` and the height9/width11 certificate summarized in `audit.md`, SectionAO.

The present derived width H depends on initial mass, core width, and row multiplicity, and can be arbitrarily large. Thus there is no conflict. If additional information forced H<=9, the hypotheses would be impossible. No all-width axial-strip exclusion has been proved or used here. In particular, neither this theorem nor the height9 certificate decides whether ANY finite-seed axial traveling front exists.

## 8. Exact diagonal gap

A periodic diagonal core gives bounded stage-root multiplicity on each row AND column, but it does not lie in a fixed vertical or horizontal strip. Section3 then fails: vertical G far endpoints can place black bits on a chosen row at unboundedly many columns, while horizontal endpoints can analogously supply unboundedly many rows. The fixed finite-band term H0 and the resulting one-sided rank bound are unavailable.

This is the precise missing extension, not a conclusion that diagonal decorations must be unbounded. One would need to control the coupled horizontal/vertical far-endpoint supply outside an oblique core strip, or otherwise enclose the full trace. If full non-axis strip confinement were independently established, the inherited strip theorem would already yield full translating periodicity. No such enclosure has been derived here.
