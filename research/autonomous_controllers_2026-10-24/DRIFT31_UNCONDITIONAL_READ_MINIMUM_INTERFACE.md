# An unconditional all-cap read-minimum interface for full drift (3,1)

24 October 2026. Author local theorem with a small complete certificate,
submitted for independent review. No period, width, growth, or visit cap is
assumed. This does NOT exclude the drift or produce a complete controller.

## Retained scope checked first

The retained `../periodic_classification_new/general_drift_frontier_geometry.md`
independently excludes whole-front cap FOUR for full drifts(3,1) and(3,-1),
separately, at every period and width. It does not exclude either drift at all
caps. The retained general-wake parity proof excludes one explicit unbounded-
width g8 family at(3,1), not every wake of this drift. Neither result is silently
promoted to the stronger conclusion. The present derivation uses actual read
history minima instead of imposing the earlier four-read bound.

## Exact uneven-step geometry and the minimum

Let T(x,y)=3y-x. Each integer T is exactly ONE orbit modulo the FULL supplied
d=(3,1): choose representative p_T=(-T,0), since

    (x,y)=(-T,0)+y*(3,1).

A physical step changes T and the translation lift by

    N: (+3,+1), E: (-1,0), S: (-3,-1), W: (+1,0).

The first entry in each pair is the normal change; the second is the FULL-drift
voltage. These unequal jumps cannot be replaced by adjacent diagonal rows.

Take the minimum of the COMPLETE read footprint, not a field-color maximum,
odd-wake minimum, or contour potential. It exists because a period has finitely
many full-drift classes. Translate one minimum read cell to(0,0), giving minT=0.
At that cell, incoming headings can only be E or S, because N and W would arrive
from forbidden lower read levels. The fixed incoming-axis invariant allows only
one of these. Horizontal E would make the first WHITE R exit S to T=-3,
impossible. Thus the minimum is vertical and all incoming headings are S.
Its L exit E would also go below the minimum, so the entire history is exactly
one S/R. The lower levels are UNREAD, not assumed WHITE or cleared of black data.

## The first derived complete histories

Denote levels0,1,2,3,4 by V0,H1,V2,H3,V4. Incoming axes alternate V/H.
At H1 every outgoing S would fall to unread level-2; every read exits N.
The sole W input comes from V0's singleton, so H1 is exactly W or WE.
At V2 there is no N input from level-1, hence all headings are S. Its outgoing
E count equals H1's E count. Consequently

    H1=W  implies V2=empty or S;
    H1=WE implies V2=SS or SSS.

Let a=ceil(|V2|/2). At H3 there are exactly a incoming W occurrences and exactly
one outgoing S occurrence, feeding V0. If X counts its R reads arriving W, then

    1=ceil(n3/2)+a-2X,

so n3<=2(a+1). This DERIVED bound is at most6. Enumerating ALL two-heading words
with those exact counts gives17 complete lower choices. Three have explicit
clock cycles of weights P+10 or P+18 and fail for every P>0. No exterior history
is assigned. The14 remaining choices are all retained.

## Literal four-step first return and the next derived cell

Every remaining lower choice has one physical four-step return from V4's
outgoing E ordinal a0 (a0=0 or1) to its FIRST incoming N ordinal. The path is

    V4 -> H3 -> V0 translated by -d -> H1 translated by -d -> V4.

All intermediate positions differ from the physical V4, and all port ordinals
are fixed. Therefore the first N read occurs immediately after that E departure
in V4's complete rank order, with actual clock gap FOUR. This is not a quotient-
only return or an arbitrary skipped-period connection.

At V4 the mandatory incoming N count is I=|H1|, and the mandatory outgoing E
count is J=number of E occurrences at H3. If X is V4's R/N count, then

    J=floor(n4/2)-I+2X,

so n4<=2(I+J)+1, with maximum derived bound13 in this cover. All N/S words up to
that derived bound with the exact counts and physical consecutive-rank return
are enumerated. Three lower choices have empty domains. The others give30
complete V4 choices; five have explicit positive clock cycles P+6 or P+14.
Exactly25 five-level interfaces remain necessary and OPEN.

In EVERY survivor the first N is a RIGHT read at rank2 or4. Thus V4 begins SSN
or SSSSN, and its preceding E departure is respectively L1 or L3. All25 exact
complete histories are in the certificate, not a sample. Higher levels and all
remaining boundary ports stay unrestricted. In particular no global cap4 or
cap13 conclusion is made, and no support-termination case is silently discarded.

## A concrete surviving obligation, not an alternative controller

One surviving interface is

    V0=S, H1=W, V2=empty, H3=EE, V4=SSN.

It contains seven named events and two open successor chains. For P=202, full
representative read clocks are

    V0:208; H1:209; H3:5,9; V4:0,4,8.

All internal ordinal edge equations, same-cell rank gaps, physical mod4 phases
and the seven distinct phases modulo202 hold. The unknown boundary requires
two S departures from level7 into V4, one W arrival at level5 from V4, and one
N arrival at level6 from H3. The other195 phases are NOT supplied, so this is
only a consistent OPEN clock interface, not a202-event completion or a seed.

For a literal local sanity check, a blank ant at(-4,0), incoming S, performs
the ten actual reads RRRRLRRRRL and ends at(-3,1), incoming N. The factor realizes
the displayed named histories within those ten reads; its entire final black
field is retained. Their LAST status in the future is not certified. This
blank ten-read factor is not a translating word or regenerative controller.

## Certificate and scope boundary

`certify_drift31_read_minimum.py` constructs every derived domain directly by
binary enumeration, all eight positive clock witnesses, all physical return
paths, the25 open interfaces, the seven-event clock model, and the actual blank
factor. `partial_drift31_graph.py` uses the exact nonprimitive-normalized FULL
voltage y and all internal physical ordinal matches; omitted levels stay
unknown. Initial negative levels are named EMPTY read histories, not colored
WHITE input fields. `DRIFT31_READ_MINIMUM_SHA256SUMS` binds exact dependencies.

Proper rotations/translations transport the result. Reflection does not, so
(3,-1) is not silently covered. No all-drift growth-eight, autonomous-controller,
standard104 uniqueness, or finite-seed attraction conclusion follows.
