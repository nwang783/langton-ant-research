# A finite boundary-current budget, actual interval peeling, and a pinned-hull obstruction

24 October 2026. Author proof and complete finite controls; independent audit pending. This uses retained reflecting-side exclusion dynamics but adds the finite four-corner budget and its quantitative interval decomposition. No global attraction or novelty claim is made.

## 1. A rectangle-confined interval has only quadratically many boundary reads

Let R be a W-by-H cell rectangle, with W,H>=3. Consider an actual ant interval [s,t] whose head stays in R and whose two endpoint heads are in its STRICT interior. The entire board outside R remains present; it is simply unread during this interval. Let D=t-s.

Then the number of updates reading a boundary cell of R is at most

    B(W,H)=2W^2+2H^2+2W+2H-12.                (1)

This bound is independent of D, the interior coloring, initial black mass, and all exterior archive.

### Corners: at most one read each

The invariant checkerboard sector fixes the incoming heading AXIS at each cell. At a corner, only one incoming directed edge and one outgoing directed edge stay inside R. Thus every confined visit to that corner would have the same turn letter. Consecutive actual visits must alternate their read colors and turns, so each corner can be read at most once in this interval.

The strict-interior start matters: there is no exceptional first arrival at a corner from outside R. No physical time-reversal or sector change is used.

### Complete boundary-contact episodes

Starting at the first boundary cell after an interior cut, confinement and90-degree turns force exactly one of:

- two adjacent noncorner cells, word RR or LL, then an interior head;
- three cells around one corner, word RRR or LLL, then an interior head.

There is no longer boundary episode when both dimensions are at least3. The four corners therefore permit at most four three-cell episodes. Straight episodes are the reflecting two-cell moves in the retained exclusion lemma.

### Finite side current

For each side, exclude its two corners, leaving L cells. Order those cells in the tangent direction of an R turn from the inward normal. At normal-arrival sites set eta=BLACK; at the alternate sites set eta=1-BLACK. Every straight RR or LL episode becomes the SAME directed exclusion move01->10.

Let Phi=sum_(j=1)^L j*eta_j. A straight episode changes Phi by-1. A corner episode flips one endpoint bit on each of two adjacent sides, changing each affected Phi by magnitude at most L. Each side has at most two such corner perturbations. Since0<=Phi<=L(L+1)/2, its number of straight episodes is at most

    L(L+1)/2+2L.

Sum over two sides of length W-2 and two of length H-2. Count two reads per straight episode and three per corner episode. The result is exactly(1).

This is not a finite-particle claim about an infinite boundary row. The finite side segment and its at-most-two corner perturbations are essential. The retained infinite-row alternating vacuum can support unlimited current, so it cannot be used as a global finite-fuel argument.

## 2. A genuine nested HEAD-region interval

Between successive boundary-contact episodes, the head stays in the strict inner rectangle R_minus, obtained by deleting one row from each side. There are at most B+1 such interior intervals. The boundary reads and their entry moves use at most2B updates. Thus at least one interior interval has duration at least

    max(0, ceil((D-2B)/(B+1))).                (2)

Every position in that interval lies in R_minus. Its COMPLETE exterior black field is still retained, and may be read later. This is a nesting of selected time intervals and head regions, not a LIFO ordering of lifetimes or a deletion of outer archive.

For arbitrary endpoints of a confined interval, the head reaches strict interior within at most3 updates unless it exits R; the same geometry applies backward to the final boundary run. Trim at most3 updates at each end. Therefore(2) applies with D replaced by D-6, whenever that expression is useful. This derives, rather than assumes, the partial-episode correction.

The lemma may be iterated on a selected inner interval while its rectangle still has both dimensions at least3. It gives an actual finite hierarchy of confined subintervals. It does NOT force the current BLACK hull to become smaller and does not by itself produce a later fast record-clock window.

The scale matters: B is quadratic in the rectangle spans. A long drought merely exceeding a fixed forcing-window number need not exceed the boundary budget of its much larger old rectangle. No uniform strict descent follows from duration alone.

## 3. A literal fixed-cardinality obstruction to BLACK-hull descent

The signed22-cell M-to-T family gives the following exact all-parameter construction. For every integer n>=100, set

    a_n=32433+104n,
    b_n=80270+208n.

Throughout the complete actual interval [a_n,b_n], the CURRENT BLACK hull is EXACTLY

    Q_n=[0,2n+250] x [0,2n+262].              (3)

Every head position in that interval is strictly inside Q_n. No boundary cell is read. Its duration is

    b_n-a_n=47837+104n.

All original BLACK lifetimes have already retired by update27201+104n,5232 updates before a_n. The entire future-relevant population at a_n is exactly807, independent of n.

Three actual R-born lifetimes pin all four sides of(3), and are never read again in the WHOLE infinite future:

- cell(0,0), born at update20, pins the west and south sides;
- cell(2n+250,2n+237), born at27653+104n, pins the east side;
- cell(2n+231,2n+262), born at29695+104n, pins the north side.

These are genuine permanent lifetimes, not inputs later resurrected by a changed continuation.

### Exact all-n proof

At the end of the first standard period the full source board has no BLACK cell with x<0 or y<0 and has the R20 lifetime at0. All later source/M/forward-flight reads have positive coordinates. The signed T prefix has its extremal R births at relative times6452 and8494, positions(20,8) and(1,33). Each is the final T-prefix read at its cell. They attain the upper bounds in(3).

At a_n the T prefix has finished. The remaining SW flight, its exact old-M collision, and all48464 subsequent recovery reads are strictly inside(3). This is checked for all n>=100 by the finite affine phase extrema, including the terminal partial period. Hence no boundary bit changes and no black cell is written outside Q_n: the entire BLACK hull stays identical, not merely similar or translated.

The SW tail lies strictly below the north pin and to the left of the east pin. The complete later fixed recovery and NW tail have x<=240, excluding both upper pins for n>=100. Their y coordinates are positive, excluding0. Thus all three pins are actually permanent.

The807 whole relevant cells at a_n are the21 inputs of the current standard SW phase plus the same786 untouched old-M lifetimes in the signed complete-field transfer. Those sets are spatially disjoint; all21 local inputs are consumed before the first M collision for n>=100. No other old archive is silently pruned in establishing(3).

## 4. Precise quantified countercontrol, and what it does not show

For any prescribed finite integers L,K>=1, choose n large enough that47837+104n>=KL. This ONE22-cell finite seed then has K disjoint length-L subintervals after original-input retirement, all with the same complete current BLACK hull Q_n and with no hull-expansion event even if the clock is reset to the full current board at each selected cut.

In particular L may be chosen larger than an explicit forcing bound at a smaller H. Each such window simply FAILS the fast-clock hypothesis. It does not force a smaller complete BLACK region, consumption of a boundary pin, or a finite initial-fuel decrease. The start relevant population remains807 and the elapsed time from last original consumption remains5232 at a_n.

These K windows lie inside ONE long completed global drought. They are NOT K distinct completed global record gaps separated by new records. No fixed-cardinality family with an unbounded number of those separate completed droughts is claimed here. Nor is one orbit with infinitely many increasingly long droughts constructed. Every member has the signed canonical tail at b_n.

The correct distinction is now explicit: long confinement has an ant-specific boundary-current budget and permits nested HEAD-region subintervals, but the complete BLACK hull can remain permanently pinned. A global hierarchical proof must account for the live remote input across the inner intervals rather than equating head-region peeling with full-state or relevant-state descent.

## 5. Verification

The checker exhausts all512 initial boards of a3-by-3 rectangle, all four center headings,2048 complete finite trajectories. It parses every complete interior-to-interior boundary episode, verifies sector corner uniqueness, each oriented side-current identity and the exact bound(1). This tests the local corner and shortest-side cases; the universal proof is the geometric/exclusion argument above.

Three full MT controls n100/137/500 are replayed from the signed north-record fields through b_n, with complete fields, true lifetime identities and all-future canonical parity. They certify the constant hull, all three permanent pins and the entire807-cell future-relevant set. The all-n claim additionally uses exact affine inequalities and signed source geometry, not interpolation from those three replays.

No global record-clock occurrence, whole-orbit nested lifetime order, mass-only fuel law, or canonical uniqueness is inferred.
