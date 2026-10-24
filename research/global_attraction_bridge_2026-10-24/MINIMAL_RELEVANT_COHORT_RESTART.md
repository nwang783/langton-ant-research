# Three greedy pristine-record restarts grow even the minimal relevant cohort

24 October 2026. AUTHOR exact finite/infinite countercontrol; independent audit requested. This tests the actual composition gap left by the signed 272754 fixed-cohort theorem. It is not a noncapturing orbit or a refutation of every amortized potential.

## 1. Precise candidate and its canonical strongest pruning

For a complete state at cut t, let C*(t) consist of exactly those currently BLACK lifetimes whose present lifetime will be consumed at some later physical read. A cell whose present black lifetime is never read again is omitted. This definition is retrospective and need not be effectively decidable on arbitrary inputs.

The corresponding black-cell subset is the unique inclusion-minimal deletion-only subboard preserving the ENTIRE future physical trajectory from t. Deleting never-read black cells changes no read, by induction. Conversely, if a deleted cell is eventually read, the earliest such read would see WHITE instead of BLACK, so the original trajectory cannot remain unchanged. This is stronger pruning than discarding only disconnected, distant, or apparently dormant archive.

A natural restart candidate is:

    At a guard-avoiding pristine record, fix C*(t). After its third
    lifetime is consumed, go to the FIRST subsequent pristine record u.
    If u is still guard-avoiding, then |C*(u)| < |C*(t)|.

This candidate would make a useful fixed-cohort theorem composable without free new fuel. It is FALSE, even for three consecutive greedy renewals with complete never-read pruning. The countercontrol below also refutes the weaker nonincrease candidate.

## 2. Literal finite seed and genuine pristine entry

The chosen-cut board consists of these fourteen black cells:

    (-4,1), (-4,2), (-3,-1), (-3,0), (-3,3),
    (-2,-1), (-2,1), (-2,2), (-2,3),
    (-1,1), (-1,2), (0,1), (0,2), (1,2).

Its head is (0,0), E. The whole half-plane x-y>=0 is WHITE. To make this an actual new record, begin instead at (-1,1), E with (-1,1) removed from the displayed black set and (-1,0) added. Two real moves RL reach the displayed state. All following times are measured from that cut. No field or cursor sector is discarded.

This is the retained missing-phase45-bit control, but the present result computes a new complete future-relevance ledger and new greedy restarts, not merely its local defect count. All pristine assertions below use the entire current board, including every remote black cell; globally unvisited alone is not substituted for whiteness.

## 3. Exact greedy-renewal ledger

The first three increases are:

| entry t | third input | first later pristine record u | full mass t -> u | relevant mass t -> u | relevant retired | relevant new survivors |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 31 | 71 | 14 -> 19 | 14 -> 16 | 14 | 16 |
| 71 | 93 | 104 | 19 -> 26 | 16 -> 23 | 5 | 12 |
| 104 | 135 | 169 | 26 -> 33 | 23 -> 25 | 11 | 13 |

The record normals at cuts 0,71,104,169 are respectively (1,-1), (-1,-1), (1,-1), (1,1). Each is strict relative to the complete earlier head history and has every current black cell strictly on its old side. All 32 properly rotated outward capture guards fail at each of these cuts, on both the full board and its minimal relevant subboard.

The original fourteen lifetimes are ALL gone by time 70. Thus every relevant member at 71 is newly born after the chosen cut. The later increases do not rely on a hidden survivor of the original cohort.

The greedy cut is not selected by waiting past an inconvenient intermediate record. Every strict/pristine cut in all eight normals is tested. Even if every forever-unread bit is deleted at each entry, the first pristine cut after the third input remains 71,104,169 respectively. The physical trajectory is unchanged by that deletion, and the stronger pristine check is explicitly repeated.

For a fixed-normal version, choose only n=(1,-1). The first such pristine record after the third C*(0) input is 104. Its relevant size is 23 rather than 14, with the whole original cohort already gone. Thus the basic strict-drop failure does not require allowing normal changes. The three-step greedy chain does use the displayed changing normals and is not claimed as a three-step fixed-normal chain.

## 4. All-future relevance is certified, not guessed from a long run

The checker starts from the literal preparation and independently simulates all 308 moves, preserving every cell and genuine lifetime identity. There are 27 actual pristine strict-record time cuts in the eight normals. It tests every one against all 32 guards on the complete and relevant fields.

At time 308, the entire 54-cell board and actual cursor satisfy the signed phase45 guard. A separate exact ray-parity calculation checks the actual 104-word continuation with drift (2,-2) forever. For each phase i, initial-black membership along q_i+k d can change only at its finitely many exact board intersections, while prior-read parity changes only at the exact phase-ray overlap thresholds. Testing all change points gives 154 parity tests covering EVERY k>=0, not a truncated number of periods.

For every lifetime still black at 308, solve q=q_i+k d, k>=0, over all 104 phases. Its earliest solution is its exact future first read; absence of every solution means the lifetime is never read. Combined with the finite death ledger, this decides C*(t) exactly at all earlier cuts. At 308, fifteen of the 54 current lifetimes are relevant, all consumed by 379; the other 39 are never read again. These unused cells remain in the certified full board.

The later greedy steps have relevant sizes 25 -> 18 at cut 225 and 18 -> 15 at cut 308. The first of these is still guard-avoiding; the second reaches the certified guard. This is why the example is a finite obstruction to monotone restart, not a repeatable growing controller. Time 308 is a sufficient record-guard certificate, not earliest standard-word onset; the retained timing clarification gives onset 262.

## 5. Relation to the other countercontrols and remaining target

The prepared 184-cell long-wave and 20-cell long-wait families have signed all-parameter obstructions to being pristine at their long prepared stages. They are not used to falsify a pristine-record budget here. This fourteen-cell control has genuine full-field pristine half-planes and is funded by actual fresh births, not unread prelaid rails.

The fixed-cohort 272754 theorem remains valid: none of the displayed short intervals violates it. What fails is the additional claim that retiring a third old member at a greedy new record produces a smaller canonical relevant cohort. The first three intervals retire 30 distinct relevant lifetimes and leave successively more relevant descendants; none of those actual deaths is counted twice.

The example does not rule out credits assigned to earlier inputs with multiplicity, a spatially weighted invariant, or an amortized inequality over longer blocks. Such a claim must explain the positive relevant production rather than hiding it in permanently unused archive. The exact spatial support of each relevant field and its original-seed hull is retained for the next test; hull expansion generated by fresh output must not be counted as new pre-funded seed resource.

## Artifacts

`check_minimal_cohort_restart.py` and `MINIMAL_COHORT_RESTART_CHECKED.json` contain the literal preparation, all physical reads, all 27 record cuts, the complete selected fields and lifetime death times, every greedy third-input cut, exact pruning checks, all infinite-tail parity changes, and all terminal first-read/never-read classifications. The manifest binds the signed guard, original control and canonical fixed-cohort dependencies. Independent audit is pending.
