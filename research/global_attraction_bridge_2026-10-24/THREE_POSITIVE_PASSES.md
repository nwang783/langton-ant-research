# A charged third positive ordinary pass, with the exact regeneration failure retained

24 October 2026. AUTHOR finite construction; independent review requested. The universal finite-seed standard104 conjecture remains unsolved.

## 1. Falsifiable target and outcome

The live target was whether the full output of the retained chronological positive-positive recycler is an actual dead end for a further gaining ordinary pass, or whether an initially unread finite perturbation can supply the missing return while keeping the original two passes genuinely ordinary on the enlarged board.

There are four explicit positive controls, q=3,5,7,9. Each uses ONE complete initial finite seed and ONE continuously moving ant. No cells are inserted later, no old field is discarded, and there is no reversal or pose reset. An extra pre-funded outer guide and q−1 unread stitches preserve both original positive ordinary epochs, then enable a THIRD maximal ordinary epoch with the SAME gain q−2. It consumes all but FIVE of the second epoch's R-born lifetimes, together with all q−1 added stitches.

This is not a regenerative loop. Almost all additional old guide lifetimes are spent. The direct next-stage stitches are white, and the pose-compatible repetition of this precise return protocol fails at its second read. Alternative repairs and routes remain open.

The earlier temptation to use a shorter word-preserving guide was rejected: its unread support made many second-pass L edges nonbridges. The frozen construction below passes full-board bridge checks at every L, not merely color-word checks.

## 2. Exact supplied seeds and chronology

`THREE_POSITIVE_PASSES_CERTIFICATE.json` is self-contained: every initially black cell, the actual initial pose (1,1),E, the five literal stage words, and the following RRL exception are supplied for each of the FOUR cases. The original first two passes and their first return are the retained family from `../actual_zipper_spiral_2026-10-23/chronological_stitched_return.md`, but no all-q result from that note is assumed. Every finite prefix is replayed here from its literal whole seed.

The extra inputs are:

- q−1 one-edge stitches connecting successive second-output rods;
- a separate outer guide on a coarse right-offset lane, d=−4, with its actual endpoint patches;
- one four-edge old w cycle at the outer departure port.

All these extra physical cells are UNREAD during the entire original two-pass prefix. This preserves the original physical turns. Independently of that fact, the full graph checks prove both positive passes are still ordinary. Initially unread does NOT by itself imply this topology preservation.

For readability put n=12((q+1)/2)^2. The following formulas describe exactly the four supplied cases; they are NOT promoted to a theorem for every odd q:

- Extra initial black cells: 2n+15q−8.
- Total initial black cells: 6n+6q+35.
- First positive epoch: time 4n+q, gain q−2.
- First charged return: time 4n−21q+91, gain 9−q.
- Second positive epoch: time 4n+5q−2, gain q−2.
- Second charged return: time 4n+27q−15, gain 3−q.
- Third positive epoch: time 4n+9q−18, gain q−2.
- Complete elapsed time: 20n+21q+56. Complete mass gain: q+6.

The numerical complete initial masses are 341, 713, 1229, 1889. Additional seed masses are 133, 283, 481, 727. Total certified durations are 1079, 2321, 4043, 6245.

The second return actually reaches (2,4),E. It consists of an initial RL old-cycle erasure, the charged guide traversal, and a final RRRRL. Its complete w-exception count is TWO, including every old attachment. The ant is not placed at that inner port by hand.

## 3. What “ordinary” and complete preservation mean here

An ordinary block is R^r L with r≤2 and the L a bridge in the COMPLETE w-black graph. All three positive epochs satisfy this at every block. Every stage ends at a real post-L cut. Each positive epoch ends immediately before a nonordinary block: the first and second are followed by the actual old-cycle RL of the corresponding return; the third is followed by the actual RRL whose L is w-nonbridge. Thus the third interval is not a hand-picked favorable proper subinterval of a longer ordinary epoch.

The full original first-R cohort survives the first return and is entirely consumed in the second positive epoch, unchanged from the baseline construction. The ENTIRE second-R cohort survives the second return. It has 2n+3q−2 lifetimes. The third epoch consumes 2n+3q−7 of these, exactly q−1 additional initial stitches, and no other lifetimes. Its counts are

    L=2n+4q−8,   R=2n+5q−10,   gain=q−2.

Five second-R lifetimes remain, with their actual birth times and coordinates recorded. They are not silently removed from the field.

Initial cycle ranks are (w,z)=(2,0). Both graphs are updated and their actual births/erasures counted on every read. For q=5, the five stages have respectively:

- births (0,0), erasures (0,0);
- births (0,2), erasures (1,1);
- births (0,115), erasures (0,116);
- births (1,5), erasures (2,4);
- births (1,116), erasures (0,117).

Thus the three ordinary w epochs are NOT asserted to be paired-forest epochs. Opposite-graph events remain substantial. The final complete ranks are (1,0), so even the existence of one newly available w cycle is not dismissed as absent; it simply has the wrong immediate gate for this particular repeated return.

## 4. Exact regeneration comparison

`REGENERATION_BOUNDARY_CHECKED.json` checks the following on every complete final board.

1. Exactly THREE lifetimes from the additional initial seed survive. They are the three unconsumed edges of the added outer cycle. Every added guide lifetime and every added stitch lifetime has actually been consumed. Every extra initial cell's FIRST read time, or a null value for never read, is recorded in the main checked file. This identity statement does not pretend that later R writes cannot recolor those positions.
2. Exactly THREE original baseline seed lifetimes survive as well. All later output from both return guides and all three positive passes remains present and is labeled by its real birth stage/time.
3. The third-R output consists of q rods with q−1 direct adjacent-tip joining gaps. All these specific next stitches are WHITE and were never read anywhere in the complete certified history. The five surviving second-R lifetimes are at different cells; they do not supply these missing bits. An alternative nonlocal connecting path is not excluded.
4. Compare the full post-second-epoch entry field with the actual final field under the unique proper rigid motion aligning their true poses. The required motion is a clockwise quarter-turn plus the recorded translation; all missing and extra full-board cells are listed. More sharply, the minimal first-read black/white guard of the exact proposed next `second_return + third_epoch` word is tested against the complete final field. It fails at offset ONE: that word requires L, but the actual cell is white. The actual local continuation is RRL, not RL. Extra inert archives cannot repair this wrong read.

The full minimal guard mismatch counts are 228, 504, 876, 1344 for q=3,5,7,9. These are checks of one specified pose-compatible repetition, not a search over all possible future repairs, phases, controllers or target sizes. No claim that every missing initial-template cell is dynamically necessary is made: the minimal guard test is retained precisely to separate that issue.

## 5. Audit package and stopping boundary

`check_three_positive_passes.py` is a self-contained literal verifier importing no geometry generator. It reconstructs all actual colors, flips, poses, lifetimes, both graph event types, complete bridge tests, full checkpoint fields, and first reads of the additional initial cells. It also verifies the next RRL exception. `THREE_POSITIVE_PASSES_CHECKED.json` records the complete fields at every stage boundary and all final lifetime identities.

`THREE_POSITIVE_PASSES_FULL_COMPONENTS.jsonl.gz` records the complete active w AND z edge sets, actual pose and time at EVERY fine cut from initial cut through the third endpoint: 1080, 2322, 4044 and 6246 cuts respectively. No radius-limited component approximation is used. Each case's uncompressed line stream is hashed in the main checked file.

`check_regeneration_boundary.py` separately reconstructs the complete physical history and checks the current missing-stitch and next-word guard statements. Discovery scripts and the six irregular F_q capture controls are not proof dependencies for this finite construction.

An explicit parallel-guide geometry works in these four cases and suggests an all-odd-q extension. That would require a genuine all-parameter proof of BOTH the original two-pass interface and the new full exterior separation/return guards; numerical formulas alone are not that proof. The finite result already refutes the claim that the specific two-pass output cannot be made to feed a third positive ordinary pass by a charged initially unread perturbation. It does not refute any finite initial fuel budget: the added guide and stitches are paid in full and are not regenerated.
