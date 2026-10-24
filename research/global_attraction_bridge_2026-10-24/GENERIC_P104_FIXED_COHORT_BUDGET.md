# A distinct generic-P104 pristine-record budget before a third fixed-cohort input

Status: author proof and read-only source extraction; submitted for independent audit. This result uses generic `PermanentP104`, NOT the canonical standard104 word or its eight-guard catalogue. Those predicates and their counts must not be merged.

## Predicate and result

For a full state s, let GP104(s) mean that there is a displacement d in {(2,2),(2,-2),(-2,2),(-2,-2)} such that all future position, incoming heading and read-color observations repeat every104 moves, translated by d each period. This is exactly the retained two-black `PermanentP104` predicate. It permits any104-letter word compatible with that complete physical future; no canonical-word identification is assumed.

Fix ANY finite full board and pose at a chosen cut, and fix its entire black-lifetime cohort C0. Before the THIRD distinct C0 lifetime is consumed, the number of genuine pristine strict-record TIME CUTS in the eight axis/diagonal directions at which GP104 is false is at most

    629616.

A direction-marked count is bounded by5036928. There is no bound on elapsed time, original seed mass, age, or eventual consumption count. The chosen cohort is not reset or replaced. This is NOT a bound on avoidance of the canonical104 guards, and it does NOT prove eventual canonical104 capture.

Dependencies are the signed all-position two-black corridor/coverage assembly, its literal finite checker budgets, and the new elementary record-window lemma below. No new ant-state search is needed for this GP104 statement.

## 1. Exact 53-period pristine-window lemma

Let w have length104. Starting from its given pose, suppose its geometric endpoint has the same heading and displacement d=(±2,±2). Suppose the actual ant executes w^53 from a cut p with a genuine pristine half-plane n·(z-p)>=0 entirely WHITE, for one of the eight normals n. Assume delta=n·d>0. Then the complete state at p satisfies GP104 with the word w.

Proof: translate p to0 and let q_i, 0<=i<104, be the phase read positions of w. Every unit step has n-projection of absolute value at most1. Therefore

    n·q_i >= -103,
    |n·(q_j-q_i)| <= |j-i| <=103.

For the eight normals and the allowed d, positive delta is at least2. The hypothetical infinite periodic path has reads q_i+k d. At every k>=52, its initial field bit is WHITE, because n·(q_i+k d)>=-103+104>0.

A previous future-read event at the same site has a phase j and period k-m, with m>=0, where q_j-q_i=m d; m=0 requires j<i. If m>0 then m delta<=103, so m<=51. Thus the parity of all earlier reads at phase i stabilizes once k>=52. At those periods the initial field is white and the toggle parity is independent of k. The actual53 copies check all phases at k=0,...,52, including this final stable parity. The proposed infinite read colors are therefore valid for every k. Ordinary read induction gives the exact physical infinite word and observations. All old field bits are retained: none can lie at a future ray position with k>=52 because of the ACTUAL pristine half-plane.

This proof concerns arbitrary geometric104 words; it does not assert that a noncanonical word can actually satisfy its53-copy premises.

## 2. Record cuts inside a periodic word piece

Suppose an actual strict n-record cut t has at least104 preceding moves in the same repeated104-word piece. The head104 moves earlier is p-d. Strictness gives n·d>0. If at least5512=53*104 subsequent moves remain in that same piece and the current forward half-plane is white, Lemma1 proves GP104 at t.

Consequently, in a history partitioned into arbitrary pieces of total length L and at most s finite/infinite repeated104-word pieces, each with restored heading and displacement(±2,±2), at most

    L + 5616 s

pristine record time cuts can fail GP104. Here5616=104+5512 charges the first104 and last5512 time cuts of each piece conservatively. Endpoints, short pieces, and truncation are included. This is different from the canonical-word375 fringe bound.

## 3. What the retained corridor theorem transports

The required observation transfer is not merely `Step.corridor_pos` or `perLoop`. Use the full state relations from `Corridor.corridor`, together with `Succ.obs_of_Rid` and `Succ.obs_of_Rtr`. On relation interval q, the successor member's full observations at time t+104q equal the base observations at t, up to the prescribed spatial translation. The overlapping104 windows show that the successor is obtained by duplicating the base104 switch word once at every switch.

For one corridor, `CorridorData.succ` shifts switch j by104j. Induction therefore replaces the104 word at each of the J base switch windows by k+1 consecutive copies when the parameter is raised by k. Every other finite word segment is copied once. The terminal observation relation applies already at the listed certificate time s because `check1` verifies start(J)<=s; it need not use the looser existential witness in `corridor_reaches`.

For two corridors, `h1pB_sound` and the perpendicular/parallel succession theorems ensure that one corridor's insertion window lies wholly in a single relation interval of the other. Hence an insertion cannot cut the other switch word, and its word is transported unchanged. Repeatedly raising the two parameters duplicates only the finitely many original switch words. Their time order remains the certified order. No new arbitrary word segment or new switch type is introduced.

Thus every member of a one-/two-corridor family has a word decomposition with arbitrary total length at most the finite base certificate start s, and at most J+1 repeated104 pieces, where J is the total number of the base's switch windows. The last piece is its actual certified generic-P104 tail. The switch and tail displacement/heading premises are supplied by `switchB` and the terminal certificate, not by a supposed canonical word.

The channel/parent coverage theorems identify the actual original two-cell board with one of these families, a raised-base direct leaf, a concrete finite leaf, or an unread-parent branch. They do not prepend another uncontrolled run to each selected family: the family itself is run from the original two-cell initial state.

## 4. Exact finite bounds, not a simulation maximum

A separate literal-only parser reads the immutable source tables. It finds:

-99550 one-corridor hints, including all parent-tail families, channel children and one-dimensional slabs;
-506 two-corridor hints;
-maximum one-corridor certificate start270504;
-maximum two-corridor certificate start166816;
-maximum total switch count5 in either dimension class;
-direct certificate searches use at most6000 candidate periods, hence a sufficient finite-prefix bound624000. The blank/singleton auxiliary budgets are smaller.

The corresponding conservative bounds from Lemma2 are:

    families: at most270504+6*5616 =304200;
    direct leaves: at most624000+5616 =629616.

The unread single-parent branch is covered by the retained one-black exact decomposition, which is also below629616 with the generic fringe. These source-bound maxima are independent of all spatial family parameters. The parser and inventory contain source hashes; the billions of prefix reads that would be needed to recover every actual word are NOT required for these generic estimates.

## 5. Fixed-cohort coupling and full-field transfer

Choose the first two C0 lifetimes actually consumed, if two are ever consumed before the truncation. From the ORIGINAL chosen cut, run the comparison board consisting only of their two cells, with the same pose. Until the third C0 consumption, every omitted C0 cell stays black and unread, so a direct step induction couples the whole physical path to this at-most-two-black parent. All R-born output and every historical revisit of that output are produced in both histories. No restart at the first or second collision is used.

A strict record of the actual history is also a strict record relative to the compared suffix. In an interior repeated-word window with enough future moves before the third input, the actual complete state has the same53-copy turn word. Apply Lemma1 directly to THAT complete state and its current pristine half-plane. Extra omitted old cells cannot invalidate it: every potential old-side read lies in the finite checked horizon, and the entire later half-plane is actually white. A discrepancy in that checked horizon would be a third C0 read, contradicting the comparison interval.

Truncate the parent's finite decomposition at the third contact if it exists. The final truncated periodic piece receives its5512 fringe allowance. Lemma2 then yields629616. If fewer than two C0 inputs occur, use the corresponding zero-/one-cell parent. The argument never charges a later fresh lifetime as one of the original C0 inputs.

## 6. Canonical bridge remains separate and conditional

If every pumped104 switch word and every terminal base/direct-leaf certificate in the retained finite cover is separately verified to be a cyclic canonical H word, the same full-observation transport preserves that identification for every parameter. The sharper canonical fringe375 then gives a candidate before-third-input bound

    max(270504+6*375, 624000+375) =624375

for avoidance of the canonical outward guards.

That finite word-identification premise is NOT included in the retained Lean P104 statement. At the time of this note, the complete annotation is being investigated separately; a representative benchmark or external partial rerun is not complete coverage. No629616-to624375 substitution, standard-word conclusion, restarted-cohort fuel, or global mass-only budget follows without the extra premise.
