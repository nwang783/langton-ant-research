# Every undecorated same-sector pose on one bilateral standard wake captures

Status: independently audited on2026-10-22 at21:26 UTC. The auditor replayed22,958,288 physical moves over all1508 near poses and used a distinct phase-threshold oracle for all-future certification. The complete715-cell cap transfer and all-far normalization also passed. It concerns an infinite but explicitly fixed clean background, not arbitrary finite seeds or arbitrary finite perturbations of this background.

## Statement

Let T be the canonical settled bilateral standard104 wake, whose black cells are the twelve classes listed in reverse_standard_wake_fuel.md. Initialize the ant at ANY lattice pose(p,h) in the invariant sector of the writer of T, and leave the field exactly T, with no extra flipped cap cells. Then its turn stream is eventually standard104.

Furthermore, the total number of adjacent bad-ten events K at nonnegative reads is at most150000, using true inverse histories. This generous uniform bound is independent of the initial ant's distance from the wake. No uniform capture-time bound is claimed over all starting positions.

## 1. Exact periodic-word oracle

The background predicate is

    T(x,y) = [(x-y,x mod2) is one of the12 specified black classes].

A finite actual trajectory is represented by T xor E, where E is the complete finite set of toggled cells, not a local window or discarded history.

For a proposed period w of length P and nonzero displacement d, first verify heading restoration. Partition its read phases into full-drift orbits. Write each read q_i=c+k_i d. A cell c+n d is read at the phases with k_i<=n, in decreasing k_i and then increasing phase i order. The ordered list must alternate R/L. For all n>=max_i k_i the full list applies; the first letter gives its required initial color. Cells with min_i k_i<=n<max_i k_i form a finite boundary list, which is checked exactly.

For the infinite stabilized part, if d_x-d_y is nonzero, the line c+n d meets the transverse support of T at only finitely many n. Enumerate those exact integer n, and require the stable first letter R elsewhere. If d_x=d_y, T along this orbit is periodic with period at most two in n, so check its two parities against the stable first letter. Finally check each point of E that lies in a touched forward orbit. This proves every required future read color, not just repetitions in a sample. The code is periodic_wake_fronts.py, function certify_period.

The finite-boundary check includes the entire relevant phase list, so it also independently guards any alternation failure. No phase is omitted because a cell was previously outside a sampled region.

## 2. The1508 finite near-wake classes

Translation by the wake period(2,2) does not change T. Normalize a starting pose to

    p=(a,a-t), a in{0,1}, t=x-y.

The same-sector condition is(h-t) mod2=1, leaving two possible headings for each(t,a). Exhaustively take -188<=t<=188. There are377*2*2=1508 poses. Every one has an exact standard104 tail certificate with its full actual finite error set retained.

The largest certified capture boundary is149968 updates. All tails have period104 and growth12. The outgoing drift counts are:

    (2,-2):416, (-2,-2):379, (-2,2):364, (2,2):349.

These are finite certificates, not evidence extrapolated to untested positions. Reproduction uses periodic_wake_fronts.py --limit 200000 --lo -188 --hi 188; the output JSON contains each starting pose, certified boundary, and literal tail word. The analytic reduction below covers all remaining positions.

## 3. The complete blank cap

Starting from the empty field at origin heading north, after9977 updates the pose is(-15,10),west and the complete field has715 black cells. Translating this field by(15,-10) gives A, a finite seed at origin heading west that executes the canonical W forever. This fact is checked by an exact finite-field period oracle. We do not replace A by the smaller sufficient13-cell canonical core.

The initial9977 read positions satisfy

    -34<=x-y<=48,          -21<=x+y<=35.

All subsequent blank standard reads still satisfy -34<=x-y<=48 and x+y<=35. The first inequality follows by checking one standard period; later periods change x-y by zero. The second follows from the same finite check and the standard displacement(-2,-2).

For an arbitrary initial heading h0, rotate this entire description clockwise h0 times and translate by p. When |t|>188, the old rail T is not touched during the blank prefix. Hence that prefix really occurs on T, and at its end the complete field is the rotated/translated A together with the untouched T.

For h0=0 or2 the subsequent blank highway is parallel to T, and its entire transverse read band misses T at these large offsets. For h0=1 and negative t, all future reads have transverse coordinate at most t+35<-3, so the ant moves away from T. For h0=3 and positive t, all future reads have transverse coordinate at least t-35>7, again moving away. These cases therefore have the ordinary blank standard tail without interacting with the old rail.

## 4. Every far approaching case is one of eight protected crossings

The only remaining cases are h0=1 with t>188, and h0=3 with t<-188. Same-sector compatibility forces t even.

Normalize the blank standard boundary to origin heading west by undoing the initial rotation. The old rail becomes T_r+v, where

    h0=1: r=3, v=(a-t+15,-a-10),
    h0=3: r=1, v=(t-a+15,a-10).

Let a'=v_x mod2 and s'=v_x+v_y mod4. Then s' is odd, so this is one of the eight same-sector clean transverse classes from ../scattering/transverse/PROOF.md. Translation along the old rail leaves it invariant, giving the normalized offset

    (a',s'-a'-4n),
    n=(s'-5+t)/4 for h0=1,
    n=(s'-5-t)/4 for h0=3.

Here n>=47. The reference certificates use n=20, so the extra incoming age is k=n-20>=27.

The old transverse transfer was proved for the canonical13-cell input. blank_crossing_transfer.py reruns its complete discrepancy-half-ray argument with SEED replaced by the entire715-cell A. In each backward drift class, the support union of all delayed discrepancies is the half-ray starting at the minimum support coordinate plus k. The complete finite recovery and all infinite output rays are checked against these half-rays. No black blank-prefix debris is dropped.

For all eight classes the largest required additional gap is25. Therefore every k>=27 is protected. Each far approaching case executes the corresponding fixed recovery and then an exact standard104 tail. The longest of the eight fixed recoveries is43161 updates after first contact. This completes all starting positions.

## 5. Uniform K count and limitation

In the finite1508 cases, after the certified standard boundary only the ten straddling history windows can still matter, so the K count is at most149968+10<150000. The true inverse history can change the first ten initial predicates but cannot increase the crude bound of one event per read.

In each far approaching case, separate the9977 blank prefix, an arbitrarily long standard flight, a fixed recovery of at most43161 updates, and a standard output tail. Only the fixed pieces and at most thirty seam reads can contribute K. Thus their count is at most9977+43161+30<150000. Far noninteracting cases have the blank bound. This establishes the stated uniform bound without bounding the flight length.

The theorem does not cover even one arbitrary additional flipped cap cell, let alone all finite perturbations of T. A general cap may steer the ant through a completely different interaction. Nor does a theorem on one infinite clean rail imply capture for arbitrary finite-seed histories containing several old rails and debris. These are exactly the next, unresolved supply questions.

Independent audit artifacts: ../audits/check_bare_wake_independent.py/json and ../audits/blank_full_cap_transfer_hardened_replay.log. Four deliberately incorrect perturbations at10^60 periods in the future were rejected by the independent oracle.
