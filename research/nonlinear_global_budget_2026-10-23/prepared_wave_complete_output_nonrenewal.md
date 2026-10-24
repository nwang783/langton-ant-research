# Complete mature outputs and the two-word direct-renewal obstruction

23 October2026. Author analytic proof plus exact finite profile reconstruction;
independent review requested. Scope is ONLY the two supplied translating words,
not arbitrary nonstandard consumers or physical endcap itineraries.

## 1. Keep the untouched black background

For the1564 word,197 black input classes and301 black output classes refer
only to its557 physical READ classes modulo drift(14,14). They are not complete
background counts. The five settled standard bands have420 complete black
classes modulo that drift. Exactly223 black classes lie outside READ and remain
unchanged. Thus the COMPLETE mature output has

    301+223=524 black classes, normal hull[-54,30].

For the4352 word, the three settled bands have468 complete black classes modulo
(26,26). Of these62 lie outside its1162 READ classes. Its complete mature output
has

    590+62=652 black classes, normal hull[-16,40].

The finite XOR launch edits do not alter the far mature profile. They remain
finite actual edits near the original launch; they are not globally erased.

These are exact parity identities. For each physical drift orbit, sort the
word's read slots by chronological time i-P*k, where k is its spatial copy
coordinate. The required initial color is its first turn; the final color is
the complement of its last turn. Within each list, alternation is checked.
XOR the odd-length lists into the COMPLETE initial background, leaving every
unread black class untouched. The independent reconstruction matches all301
and590 final read-support colors AND retains all223 and62 untouched classes.

## 2. Neither certified word directly consumes either complete output

The claim permits every translation, every cyclic phase with its exact physical
phase pose, every proper rotation, and arbitrary finite initial XOR edits.
It excludes a different infinite bulk or a different word.

A perpendicular wave drift crosses the complete output's bounded normal hull
and eventually reads entirely white bulk. Each of the two words has nonempty
required-first-black infinite read rays. Hence no perpendicular candidate can
run forever, regardless of finite edits.

For parallel drift, let p be the consumer's axial stride and q the producer
output's period. Along a consumer read orbit the output x-residue runs through
all q/gcd(p,q) residues of its class modulo gcd(p,q). Every such background
color must equal the consumer's required full-list first color. A single
mismatching residue gives infinitely many wrong cells, beyond any finite cap.

Translations normal to the rails are bounded by the necessary condition that
ALL required-black normal levels fit in the complete output's black hull.
The conserved physical sector restricts their normal displacement to even
integers. Translation along the rails then reduces exactly to x mod gcd(p,q).
All remaining alignments are finite and exhaustively checked:

*1564 output to1564 word:154 NE and154 SW alignments. All fail; at least159
 or180 complete read classes disagree, respectively.
*1564 output to4352 word:46 NE and46 SW alignments. All fail; at least946
 or963 read classes disagree. Over each7-copy background cycle, the minimum
 number of wrong physical first colors is3065 or3280, respectively.
*4352 output to1564 word: none can satisfy the necessary black-hull condition.
 The required-black normal span64 exceeds the output black span56.
*4352 output to4352 word:234 NE and234 SW alignments. All fail; at least479
 or478 complete read classes disagree, respectively.

Any translation outside the necessary hull intervals already leaves a required
black ray outside all output blacks. Thus it too fails, not merely the displayed
finite alignments.

Cyclic phase changes do not add a missing case. Place the shifted word at its
exact phase pose on the same physical orbit. The chronological key i-P*k then
changes only by a common time-origin constant, so the mature first-color
profile is unchanged. Finite eligibility fringes may change, but no finite
fringe can repair infinitely many mature wrong cells.

The reconstruction is `check_prepared_wave_bulk_transition_matrix.py` and
`prepared_wave_bulk_transition_matrix.json`. The simpler1564-only check is
`check_1564_complete_output_self_consumer.py` and
`prepared1564_complete_output_self_consumer.json`. The JSON retains both complete
output profiles, every allowed alignment and an explicit wrong-color witness.
No new cap or word search is used.

## 3. A general periodic-background finite-repair lower bound

Let a heading-restoring translating word have drift f, alternating complete
read lists, and maximum spatial slot span Delta. Let Q be a background periodic
under L*f. For one alignment, let A be the sum, over all complete read orbits,
of the number of wrong background residues in one L-copy cycle, compared with
the required first full-list color.

If Q XOR F executes n copies of the word, where F is any finite edit set, then

    |F| >= A * floor(max(0,n-Delta)/L).

Indeed every read orbit has at least n-Delta consecutive physical cells whose
finite-copy histories include its FULL slot list. Each L consecutive cells
contains exactly its count of wrong Q residues. They all require initial edits;
physical orbits are disjoint, so their costs add. Partial eligibility fringes
can only increase the edit requirement. This is an input XOR-repair cost, not
a claim about black mass or post-start repair by other ant motion.

For the listed NE1564-on1564 alignments, Delta=1 and A>=159, giving
159(n-1) necessary finite edits for n copies. For the listed SW alignments the
bound is180(n-1). Similarly the listed4352 self-consumers require at least
479(n-1) NE or478(n-1) SW edits. Cross-word1564-output/4352-consumer uses L=7
and A>=3065 NE or3280 SW.

These quantitative statements are restricted to the alignments satisfying the
necessary all-future black-hull condition. For other alignments the direct
renewal still fails, but the displayed159/479 coefficients have not been claimed
as global minima over every failed translated finite-prefix placement.

## 4. What remains open

This is not a no-renewal theorem for finite Langton ants. Changed endcaps can
cause long transient scattering, create new bulk, or launch another word not
in the supplied two-word set. A finite physical family can also carry a repair
set whose size grows with its written rail length, even though its ORIGINAL
black seed mass was fixed. Such earlier-created edits must be counted in the
current field, not excluded by definition.

The184-cell construction already demonstrates that long standard preparation
can create enough finite fuel for a long nonstandard episode. The present
matrix says only that the two known words do not, by themselves, supply each
other with an unchanged complete mature bulk. It neither restores a mass-only
budget nor settles their actual finite endpoint itinerary.
