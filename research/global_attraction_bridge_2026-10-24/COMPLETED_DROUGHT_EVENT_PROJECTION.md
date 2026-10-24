# Completed drought counts: exact record projection and the missing renewal interface

24 October 2026. Author proof and complete-field controls, frozen for independent audit. The finite-seed attraction conjecture remains open.

## 1. Result first

Use the union of the four strict AXIAL record clocks of the rectangle containing the ENTIRE initial black seed and every earlier head position. These are genuine pristine records. The waiting time before the first such record is not a completed inter-record drought.

The supplied fixed-cardinality families have the following exact inventories:

- **184 cells, every N>=1:** exactly four completed gaps longer than 104, of which exactly two are longer than 3390. For N>=4 the two growing lengths are `5824N+20959` and `13940N+94279`. The other two lengths are 1615 and 1213. All other completed gaps are at most 104.
- **394 cells, the signed capturing family N=3M+4, M>=1:** exactly four gaps longer than 104, of which exactly two are longer than 3390. Their lengths are `32448M+84966`, `77052M+349745`, 1721, and 1609. No extension to other original N is asserted.
- **16 cells, every n=2k>=20:** exactly three gaps longer than 104, with lengths `728k-209`, `208k-291`, and `936k+7756`. Thus every k>=18 has exactly three gaps longer than 3390. For every prescribed H, choosing k sufficiently large makes all THREE exceed H, without increasing the initial cardinality.
- **22-cell MT, n>=100:** the separately signed exact inventory gives ONE completed gap longer than 3390, of length `58697+104n`.

None of these one-parameter families yields arbitrarily many distinct large completed droughts. This is not evidence for a universal mass-only bound. It distinguishes the number of renewal episodes from both their individual lengths and the number of nonstandard updates inside one episode.

The two signed paid 28-cell concatenations also have exactly THREE gaps longer than 104, not the sum of two isolated-module counts. Enlarging the original support to include the second module deletes the first module's SOUTH and EAST records. Full initial geometry, rather than the unchanged first local return, controls this count.

## 2. Exact finite-template projection lemma

Consider a supplied legal word block w of length P, beginning at head q with heading h, repeated C times. For C>1 require that one copy restores h. Write its head cuts as q+u_i for 0<=i<P and its drift as d. Thus cut i in copy k is q+kd+u_i. Each block includes its read-position cuts and excludes its final endpoint; the next block includes that endpoint. The final infinite tail uses the same convention.

Fix one axial normal a. Let M be the maximum a-coordinate of the initial seed and all head cuts preceding the block, let v_i=a.u_i, B=max_i v_i, and delta=a.d.

The exact new-record conditions are:

1. In copy zero, phase i is a record exactly when `a.q+v_i > M` and `v_i > max_{j<i} v_j`.
2. If delta<=0, there are no new records in any copy k>=1. Its same-phase earlier copy already dominates it.
3. If delta>0, a phase i is a record in a copy k>=1 exactly when
   - `v_i > max(max_{j<i} v_j, B-delta)`, and
   - `k >= floor((M-a.q-v_i)/delta)+1`.
   Intersect this lower bound with k>=1 and k<C (or no upper limit for a tail).

The previous full-copy maximum is q+(k-1)d+B. Since delta>0 it dominates every still earlier copy. These two comparisons therefore account for ALL preceding head positions, not only the immediately preceding visit to that cell. Including M accounts for every remote initial black cell whether or not it has yet been read.

The resulting event set is a finite first-copy list plus finitely many arithmetic phase rays. A full block updates M by its exact first/last-copy extrema. Iterating this operation gives the exact global record clock. This is a geometric projection of an independently certified entire word, not a legality or capture detector for an unknown orbit.

### A uniform finite-template renewal obstruction

Suppose a complete legal future is represented by f finite one-copy blocks of lengths L_j, r heading-restoring repeated blocks, and a final heading-restoring translating periodic tail. Let H be at least the period of every repeated block and the tail. Treat the tail as one additional repeated block, so r includes it.

A repeated block has at most ONE internal completed gap longer than H: its first-copy events occupy less than P<=H time; after the first event of any stable ray, that same ray recurs every P steps. Only the transition from the initial event packet to the first stable ray can be long. A one-copy block has at most floor((L_j-1)/(H+1)) internal gaps longer than H. There are at most f+r-1 inter-block event gaps, including across empty blocks. Therefore

`number of completed gaps > H <= f + 2r - 1 + sum_j floor((L_j-1)/(H+1))`.

The bound is independent of the repeat counts and of all placements. It is intentionally coarse. It applies only to a GIVEN finite template decomposition. The Langton orbit is not known universally to admit one with bounded f,r,L_j or periods. Applying this lemma to an unrestricted orbit without that premise would be circular. If H is smaller than a nonstandard repeated period, a stable periodic record pattern could itself contribute many >H gaps; the exact projection below, rather than this coarse lemma, excludes that possibility in the supplied wave families.

## 3. Exact all-parameter event lists

Normal labels are N,E,S,W, with projections y,x,-y,-x. All times are head CUTS. The following lists include every finite pre-tail event; there are no omitted events inside the growing waves or free flights.

### 184-cell family, N>=4

The initial augmented support bounds in the order N,E,S,W are

`(56N+209, 56N+228, 56N+225, 56N+213)`.

At router stage 5, beginning at `9464N+35556`, the only events are

`14 W, 28 W, 1643 S, 1657 S`.

At router stage 7, beginning at `15288N+58158`, the only events are

`14 E, 28 E, 1241 N, 1331 N, 1345 N`.

The exact canonical SW tail begins at `e=25588N+148251`. Its complete event rays are

- W at `e+104j+19` and `e+104j+33`, j>=35N+53;
- S at `e+104j+76`, j>=35N+98;
- S at `e+104j+66`, j>=35N+99.

The first tail event is therefore `29228N+153782`. The ray already present at that first event recurs every 104, so all subsequent gaps are at most 104. Subtraction of successive listed times gives the result in Section 1. The separately certified literal exceptional N=1,2,3 continuations retain exactly the same two finite router packets; their exact tail rays are retained in the checker. Their four >104 gaps are respectively

- N=1: 1615, 26783, 1213, 104587;
- N=2: 1615, 32607, 1213, 223314;
- N=3: 1615, 38431, 1213, 188344.

These are whole finite-seed capturing histories, not completions with additional seed cells.

### 394-cell family, M>=1

The initial bounds N,E,S,W are

`(312M+815, 312M+863, 312M+823, 312M+849)`.

There are eight finite events:

- E: `36504M+96906`, `36504M+96996`, `36504M+97010`;
- N: `36504M+98731`, `36504M+98745`;
- S: `68952M+183711`, `68952M+183721`;
- W: `68952M+185330`.

The canonical SW tail starts at `e=137892M+514609`, with rays

- S phase 82 from j>=78M+196;
- S phase 72 from j>=78M+197;
- W phase 39 from j>=78M+223;
- W phase 25 from j>=78M+224.

The first tail event is `146004M+535075`. In particular BOTH the arbitrarily long supplied 4352 outward phase and the arbitrarily long supplied 15324 return phase produce ZERO pristine union records. The long source-end transition and launch-end recovery also produce none. The repeated nonstandard behavior stays within the already prepared augmented rectangle.

### 16-cell family, n=2k>=20

The initial bounds N,E,S,W are `(18k-3,14k,1,0)`.

The complete finite event list is

- S at 3;
- E at `728k-206`;
- N at `936k-497` and `936k-483`.

The exact SE tail begins at `e=1560k+7779`, with

- S phases 14 and 28 from j>=3k-5;
- E phases 61 and 71 from j>=4k-11.

Its first event is `1872k+7273`; for k>=10 it is the S phase 14 event. This gives the three growing gap formulas. They are genuinely completed separate gaps, not three selected windows inside one larger drought.

### How the parameter quantifier is certified

Every stage start, count and seed coordinate is an exact integer affine function of the sole parameter. Full read-cut extrema of each repeated stage occur in its first or last copy. Every candidate phase is checked, not only the phases displayed above. All maximum and positivity comparisons reduce to `a z+b>=0` on z>=z0; the checker verifies a>=0 and a*z0+b>=0. In every nonempty stable record condition, the slope is divisible by the axial drift, so its floor yields the displayed exact affine first epoch without a hidden residue case.

The all-parameter proofs use 2017 inequalities for 184, 4179 for 394, and 565 for 16. The finite lists, exact whole-stage hulls, every inequality and the nonempty phase-ray bounds are retained. Empty stage event sets are explicitly proved. Concrete parameter 10^9 is evaluated by these finite phase rules without expanding a long word or a large board; it is a regression control, not the all-parameter premise.

## 4. Paid concatenation does not preserve record counts

The signed two-module boards have 28 original cells. The first module has n1=20. The second has n2=40 with 100 intervening canonical periods, or n2=80 with 200 periods. Every extra bit, its first read and both complete futures are already signed; the new checker independently replays both whole histories and full terminal fields.

For the isolated n1=20 source, the initial bounds N,E,S,W are `(177,140,1,0)`. Its early records are S at cut 3, E at 7074, and N at 8863/8877.

Adding the twelve second-module original cells leaves the entire first-module word unchanged, but raises the EAST and SOUTH original support bounds. The new hull is computed from all 28 literal cells. Consequently S at 3 and E at 7074 are no longer pristine records; N at 8863/8877 survive. The full new record clock, including all infinite-tail rays, gives:

- n2=40: completed >104 gaps `39074, 3869, 27979`;
- n2=80: completed >104 gaps `64034, 8029, 48779`.

Both cases have exactly three such gaps, all also >3390. This is not an all-length concatenation theorem.

The exact mask principle is simple: if an added initial cohort A is unread while a fixed head prefix is preserved, a previous strict record at p in normal a survives iff `a.p > max_{q in A} a.q`. Added unread bits can delete earlier pristine records but cannot create new ones along the same prefix. The removed events and complete original support extrema are retained in the artifact. Therefore locality of an unchanged turn word does not establish locality of the global record clock.

## 5. Remaining live construction obligation

The current controls realize one, two, or three independently long completed gaps at fixed cardinality, but not an unbounded number. Merely increasing the number of copies of the existing wave or feedback words cannot do it: their exact phase projection has already exhausted every possible event.

A composable construction must ensure that each proposed intermediate endpoint genuinely expands the rectangle containing ALL future original ports as well as all earlier writes. The existing paid concatenation fails that condition at two explicit early events. A mechanism using self-written return material could avoid charging every future port at time zero, but it must still create an outward event between successive returns, and preserve the required later read colors on the complete field. Neither the old-M register nor the finite transverse feedback packages presently prove that regeneration interface.

The generic finite-template lemma provides a falsifiable architectural requirement: an unbounded-count construction at a fixed H cannot remain in a fixed finite stage decomposition whose repeated periods are <=H and whose finite transients are uniformly bounded. It must generate new temporal stage structure, a longer-period record pattern, or a presently unclassified interface. This is a necessary condition on a proposed construction, not a universal ant invariant or a proof that such a construction is impossible.

No universal completed-drought budget, compact-return occurrence, eventual lifetime-age bound, or unrestricted canonical104 classification is inferred.

## Evidence and provenance

`COMPLETED_DROUGHT_COUNTS_CHECKED.json` binds the signed complete 184/394/16 sources and the signed 28-cell controls, the retained MT inventory, all affine inequalities, exact event rays, and fresh literal complete-field replays. The source manifests are immutable. The 394 capture manifest's old candidate status is resolved by the separately bound all-M independent capture report, not by reinterpreting its historical status label. Independent signoff for this new projection remains separate.
