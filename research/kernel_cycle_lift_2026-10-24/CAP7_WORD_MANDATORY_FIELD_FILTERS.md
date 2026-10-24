# Sound complete-field filtering of the supplied fifty-eight cap-seven return words

24 October 2026. Targeted symbolic filtering of a supplied bounded-core word
grammar, without expanding its154,794,412 local profiles. This is not a cap7
exit theorem or a decision that any remaining word has a cap7 realization.

## 1. Source, physical conventions and scope

The source is `../reframe_finite_seed_2026-10-24/
cap7_turn_word_quotient.json`, an author58-word grammar whose coverage is a
separate dependency. Each proposed first return starts at head(0,0),N,
with COMPLETE active w component empty, fixed sector1, and is required to
be nonempty at every interior cut and empty again at its end. Every fine
cut is required to have active mass<=7. The head follows its literal turns,
not a chosen macro displacement.

For EACH supplied word this note derives actual initial/read constraints and
mandatory complete-field subsets. Exclusions apply to ANY realization of
that word under these first-return hypotheses, with arbitrary unread extra
initial black cells. The source's profile multiplicities are not treated as
physical trajectories and are not needed for the filter proof.

## 2. Minimal actual word field and surviving input bits

Consecutive reads of one physical cell must alternate R/L. A repeated equal
letter gives an immutable color contradiction, independent of the exterior.
For a word passing that test, the exact minimal initial black set B_min is
the cells whose FIRST physical read is L. The complete minimal field at
each cut is B_min XOR the parity of ALL earlier physical reads.

Any realizing initial board is exactly B_min union E, where E is black only
at cells NEVER read by the word. Therefore its complete field at every cut
is the minimal field union the SAME unread E. In particular every minimal
field is a mandatory BLACK subset, and its active component is a subset of
every realizing active component at that cut.

This calculation includes every forced first-L input and all of its actual
toggles. For a bare literal word, a visited cell is black at exit precisely
when its LAST read is R: an original first-L lifetime was consumed at that
first read. Additional OLD unread input members from a particular full
kernel profile must NOT silently be imported into a whole-word assertion.
Such extra members can be used only if the first-return/cap constraints
actually force them, or under a separately qualified profile hypothesis.

It follows at once that a mandatory black incident port at an endpoint
contradicts the required empty cursor, and a mandatory active component with
more than7 edges at ANY fine cut contradicts the cap. Adding unread black
cells cannot repair either obstruction; connected components only grow.

## 3. Sound first-return/cap unit propagation, not a SAT decision

The checker also retains variables for unread initial cells. Empty endpoint
cursors force all four incident bits white. At an interior cut the nonempty
condition is the positive clause that at least one incident port is black.
Known visited-cell bits come from the complete word history above.

Two sound propagation rules are used:

* If a previously unknown unread edge would make the mandatory complete
  active component exceed7 when set black, it is forced initially white.
* If an interior nonempty clause has no currently mandatory black port and
  only one unread port remains possible, that port is forced initially black.
  No remaining port is an exact first-return contradiction.

All consequences and their current-component/port witnesses are recorded in
order. Unknown fields can only enlarge a hypothetical black-edge component,
so these rules are necessary constraints, never assumptions of cleanliness.
This is limited unit propagation; OPEN does not mean the remaining cap7
constraint problem has been solved. On these58 words it adds NO forced
unread initial BLACK cells. The retained old-profile dimers used at cap6 are
therefore not claimed mandatory for these whole words.

## 4. General symbolic future-import trap at M=7

At an empty endpoint, let F be the derived mandatory final black subset.
Take U_F to be the union of its components meeting any of the four neighbor
vertices of that empty w root, and let u be the first-R other endpoint.
Apply the separately independently signed general theorem in
EMPTY_CURSOR_IMPORT_BUDGET_TRAPS.md:

    |U_F|>3, or |U_F|=3 with u outside all U_F vertices,

forces active mass>7 within at most9 more updates, for ANY unread exterior.
This is an unavoidable continuation exit, not necessarily impossibility of
the preceding word as a finite prefix. The first-tip qualification remains
essential; occupied-first-tip transport is left open.

## 5. Exact outcome and handoff

The58 supplied words split as follows:

    5   literal same-cell color contradictions;
    2   mandatory black ports at an empty endpoint;
    13  mandatory active components with more than7 edges during the word;
    11  future imported mass above the old-edge budget3;
    4   future budget3 saturated away from the first tip;
    23  OPEN for the compressed cap-consistency circuit.

Thus35 whole-word classes are excluded from a sustained cap7 tail by exact
finite-history or future-import arguments. Only the last15 are future traps;
the first20 cannot satisfy the finite-word hypotheses themselves.

The23 remaining words, handed to the kernel analysis without a realizability
claim, are:

    RRRRLL, RRRRLRL, RRRRLRLL, RRRRLRLRL, RRRRLRRLL,
    RRRRLLLLRL, RRRRLLRLRL, RRRRLRLLRL, RRRRLRLRLL,
    RRRRLRLRRL, RRRRLRRLRL, RRRRLLLLRLL, RRRRLLRLRRL,
    RRRRLLRRLRL, RRRRLRLRLRL, RRRRLRLRRLL, RRRRLRRLRLL,
    RRRRLLLLRLRL, RRRRLLRRLRRL, RRRRLRLRLRRL,
    RRRRLRLRRLRL, RRRRLRRLRLRL, RRRRLRRLRRLRRLL.

Examples of exact immutable witnesses:

* RRRRLRRLLLLRRLLRL requires R at(0,-1) at both updates3 and15 with no
  intervening read of that cell.
* RRRRLRRLLLLRRLL leaves mandatory black(0,-1) incident to its final cursor,
  contradicting empty at cut15.
* RRRRLRRLLLLRRLRLL has an eight-edge mandatory active component at cut13.
* The ordinary empty reset RRRRL leaves a mandatory3-star at a NONfirst
  port of its next empty root and is consequently future-trapped under cap7.

The certificate gives every excluded word's specific cells, read times,
components, initial requirements and/or forced neighbor union; it does not
replace them by a guessed turn-language overapproximation.

## 6. Artifacts and preserved scope

`check_cap7_word_budget_filters.py` performs the exact word integration,
minimal full-field replay, endpoint and cap constraints, sound propagation
and final import-budget test. `cap7_word_budget_filters_certificate.json`
binds the58-word source, all raw/propagated rows and the explicit remaining
word list. No profile expansion, SAT solver, added mid-run input, rotated
archive or finite-time capture scan was used.

Kernel coverage, full constraint solving on the23 words, productive-input
organization after those words, and general finite-seed attraction remain
separate obligations. The signed cap6 theorem and cap7 six-step core
obstruction are unchanged.
