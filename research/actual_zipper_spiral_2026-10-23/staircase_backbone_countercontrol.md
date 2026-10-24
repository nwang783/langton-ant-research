# A charged positive-gain output with no off-path branches

Frozen 2026-10-24. This note distinguishes a verified finite countercontrol from an unproved all-parameter extension. It does not change the signed-turn theorem or claim repeatable positive growth.

## Exact finite statement

The literal complete board `staircase_backbone_witness_q3.json`, initial pose (1,1), E, has 35 black cells, including the two charged passive stitch cells (9,2) and (9,-9). The exact 67-update first word recorded there is an ordinary w epoch with 33 old-bridge L updates and 34 R updates. No new lifetime is consumed. Both complete black graphs are forests after every update, with no cycle births or erasures. The final complete w graph is a SINGLE SIMPLE PATH with 36 edges, all 34 first-R lifetimes and both original stitch lifetimes. No old input-path lifetime remains. The final current w vertex is isolated, so the epoch is maximal.

After the exact RRRRL reset, the next ordinary word is (LRRL)^7 L. It consumes 15 first-R lifetimes, has mass gain -1, and remains a paired forest throughout. Its following RRL block is exceptional in w. It does not consume a stitch during the ordinary piece. Thus a static claim that positive ordinary gain must appear in off-backbone pendant branches is false. A dynamically defined decomposition that permits most of this path to be classified as unusable remains possible: the complete first output path is NOT all immediately consumable as another ordinary epoch.

The full seed, including the two old stitches, is charged. This is not endogenous growth, positive-positive concatenation, or global cubic sharpness.

## Parameterized construction and certified fixed controls

Take the spacing-4 q-run CCW square spiral in old w coordinates, with coarse edge count n=4 floor((q+1)^2/4). Replace each coarse vertex (a,b) by (a-b,a+b), replacing each coarse unit edge by its horizontal step followed by its vertical step. This gives a vertex-simple staircase with 2n edges. At each consecutive pair of positive quarter turns, with roots v_i,v_(i+1) and incoming unit direction d_i, seed the old edge from v_i+d_i to v_(i+1)+d_i. There are q-1 such stitches. Finally append one clockwise unit hook to the fine input path.

Only ODD q is retained. The same hook at even q can meet a later R arm and produces a nonbridge before completion; those candidates were rejected, not silently generalized.

The exact full-board checker passes q=1,3,5,7,9,15,25. For every listed odd q:

- M=2n+q seed edges, all seed cells explicitly generated before execution;
- L_1=2n+1, R_1=2n+q-1, G_1=q-2, T_1=4n+q;
- both full graphs remain forests at EVERY first-epoch fine cut;
- complete final w graph is one simple path of 2n+2q-2 edges;
- that path contains all first-R output and all q-1 old stitches;
- reset is RRRRL;
- for q>=3 the next ordinary word is (LRRL)^(2q+1)L, L_2=4q+3, R_2=4q+2, G_2=-1, and all its L lifetimes are first-R output;
- both full graphs remain forests throughout that second ordinary piece;
- following RRL is exceptional in w.

The formulas are supported by these exact fixed controls, not yet promoted here to an independently audited all-q theorem. The construction is deterministic and geometrically motivated; the checks are not a scan-depth claim.

## Consequence for the proposed decomposition

The one-renewal marked-path lemma remains intact. Here the marked-path parameter mu can equal the whole first-R output, since all of it lies on one simple path. Consequently that lemma gives no constant recycling bound. Nonetheless actual cursor dynamics stop the next ordinary epoch at the first coarse corner, before crossing an old stitch. A successful generic resource theorem may therefore need to charge (i) off-backbone excess, (ii) old component mergers, AND/OR (iii) dynamically unavoidable exceptional cycle barriers. Static branch shape alone is insufficient. No such general decomposition is proved by this example.
