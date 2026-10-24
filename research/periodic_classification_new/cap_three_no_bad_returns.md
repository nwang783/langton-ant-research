# Multiplicity three excludes recurrent completed B packets

22 October 2026. Analytic proof independently reviewed by the proof-certificate auditor on 22 October 2026. Here B is the bad-return label of the audited module grammar, not a lamp color. This does not yet exclude all multiplicity-three fronts.

## Proposition

Let an infinite finite-black-support square-ant trace read every physical cell at most three times. In the audited spine-and-module decomposition, at most m completed B packets occur, where m is the initial black mass. More specifically, every completed B packet forces a distinct cell whose initial color is black. For a white-input translating periodic front with displacement-class multiplicities at most three, no completed B packet can recur in its eventual spine code.

## Established module facts used

For a module of sign a, let b be the opposite sign. Write w for its root, x for its first interior cell, y for its second interior cell, and p for its predecessor. Its face is w,x,y,p,w. The exact completed-return words are

    G_a = a^4 or a^2 G_b a^2,
    B_a = a G_b a^3 or a G_b a G'_b a^2.

A G child call reads its root once, and its predecessor once at its final boundary; these statements hold at every finite recursion depth. A completed B returns to w with w still requesting a and forces immediate reentry into the same module. All square reads of these displayed boundary cells have the stated physical identities, by the audited completed-packet projection theorem. The root and predecessor statement for G follows directly from its two-row ladder footprint, or by induction in its grammar.

## Case 1: sign a=L

During B_L, w is first read L at entry and then R as the predecessor of the mandatory first G_R child. The B completion returns to w without another read there. Immediate reentry reads L again. Thus w has the chronological subsequence L,R,L.

Under a three-read cap this must be its entire history, and consequently w was initially black. If w were initially white, an earlier R would be required, giving at least four reads.

## Case 2: sign a=R, one child

The word is R G_L R^3. The mandatory child root x is read L when that child begins. After its G return, the next parent-face step reads R at x. At completion, w requests R and x requests L. The forced reentry therefore reads R at w and then L at x. Thus x has the chronological subsequence L,R,L and must have been initially black under the three-read cap.

No assumption is made about the depth of G_L. In particular its root x is read once, and its predecessor w is read once, irrespective of that depth.

## Case 3: sign a=R, two children

The word is R G_L R G'_L R^2. The first child root x is read L on entry and R on return to the parent face. In the second child G'_L, x is the predecessor, so its last-boundary read is L. Thus x already has L,R,L within the completed B packet and again must have been initially black.

## Finiteness and periodic consequence

Each completed B packet has therefore supplied a read of an initially black cell. Distinct completed B packets cannot be nested: every child call inside a completed module must return G, and the same applies recursively inside those completed G calls. Thus their time intervals are disjoint. Under the three-read cap, the displayed first L of LRL is necessarily that cell's globally first read. Different packets therefore charge different initially black cells. There are m such cells, proving that at most m completed B packets occur in the entire decomposition.

For a translating periodic tail, first cut at its exact periodic boundary. The board there still has finite black support, and each future physical cell is read at most three times because its full displacement class has at most three phases. No global cap on the original preperiod is assumed. The preceding finite-B argument applies to this cut. Equivalently, sufficiently forward translated copies of all finite packets miss the finite initial support and have complete white-input histories. A recurrent B packet would contradict one of the three cases above. Therefore the eventual spine code contains no B decoration. Its syllables have only the forms

    child1: a,
    child2: a [optional G_b] a.

The optional G is the completed call at the unchosen first child. It can have arbitrary finite depth. This reduction does not prove that those G-only codes are impossible from finite square support, and it does not justify deleting the G decorations.
