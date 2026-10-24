# Exact cap-seven word-pair existence, with separate future-trap annotations

24 October 2026. Exact common-initial-board tests for529 ordered pairs of the
23 independently validated cap7 first-return words. This is WORD existence,
not fixed-profile compatibility. Every positive edge has a literal finite
seed; every negative edge excludes every unread exterior. Pairwise cycles
are not asserted to be infinitely composable.

## 1. Why the minimal first-read seed decides these pairs exactly

The retained finite-word first-read principle supplies a unique minimum
black board for any alternating physical word: initialize precisely cells
whose first read is L. Every other realizing board is this minimum union
black cells NEVER read by the whole word. Thus at EVERY fine cut its black
field is a superset of the minimum's current field, with the SAME coupled
physical pose and fixed w sector. Its active black-edge component is also
a superset. This is the usual exact word-verifier algebra, not a new parity
or finite-word decidability theorem.

Consequently added unread black cells cannot repair either a cap7 overflow
of the minimum component or a nonempty minimum component at a required
empty start/seam/end cut. Same-cell turn contradictions are immutable too.

Interior NONEMPTY requirements would in general be a different lower-bound
question. For THESE23 words, however, each one's own minimal seed has already
been independently replayed as a genuine first return. Any realization of
that local word contains its local minimum current black field, even if the
word starts after an earlier macro. Therefore all its interior cuts remain
nonempty automatically. No SAT decision or assumed profile is needed.

**Exact pair criterion.** Integrate the physical turns continuously, check
read alternation, construct the COMBINED word's minimum initial seed, and
replay its COMPLETE field. A pair exists if and only if that replay has
active mass<=7 throughout and empty w components at start, seam and end.
Sufficiency is the constructed literal board; necessity is the monotonicity
above. Each interior nonempty condition follows from the individual minima.

The criterion is special to this validated word list. It is not permission
to replace arbitrary full-profile/resource constraints by a minimum board.

## 2. Exact529-pair partition

The vertices are the23 remaining words in the independently signed
CAP7_WORD_MANDATORY_FIELD_FILTERS.md, normalized to head(0,0),N. The code
retains every physical head turn and the actual rotation/translation at the
seam, with the same fixed w graph sector1 throughout.

    78   positive common finite-board realizations;
    220  literal repeated-cell turn contradictions;
    20   nonempty mandatory component at an empty seam/endpoint;
    211  mandatory complete active component of more than7 edges.

These categories partition all529 ordered pairs. All78 positive seeds have
at most5 initially black cells. The exact input seed, all complete fields,
actual imports, births and consumptions are retained for every positive.
The negative witnesses identify the actual cells or overlarge components;
they are not failures to match a selected minimal PROFILE.

The existence graph has78 edges and one recurrent SCC with five words:

    RRRRLRL, RRRRLRLRL, RRRRLLLLRL,
    RRRRLRLRRL, RRRRLLLLRLRL.

## 3. The27 future-trapped positives are a SEPARATE exclusion

Every positive pair's minimum FINAL field is a mandatory black subset of
every realizing board at its final empty cursor. Apply the independently
signed general import-budget trap at M=7 to that subset. For27 of the78
positive pairs, the next neighbor import has mass>3, or mass3 saturated
away from the first tip. Each such pair really CAN occur as a finite prefix,
but active mass>7 is inevitable within9 further updates for any exterior.

The exact existence graph remains78 edges. Deleting ONLY those27 separately
proved future traps gives a51-edge graph necessary for a sustained cap7 tail.
The certificate keeps both edge sets and their distinct meanings.

Its only recurrent SCCs are:

    { S=RRRRLRLRL, T=RRRRLLLLRLRL },
    { U=RRRRLLLLRL }.

All FOUR S/T ordered edges survive, including both self-edges. This is a
genuinely nondeterministic binary tail obligation, not a single periodic
word. U has its self-edge. No compatible graph cycle is being substituted
for a common finite board over arbitrarily many cycles.

## 4. Actual paid output transport, not a regenerative circuit

The positive S followed by T executes from the COMPLETE initial mass4 seed

    {(-4,4),(-3,1),(-2,2),(-1,1)}, pose(0,0),N,

with maximum active mass7. At update9, T imports the two-edge component

    {(-3,1),(-2,1)}.

The cell(-2,1) is an ACTUAL R-born output of S, born at7. The connector
(-3,1) is pre-funded input. T consumes that connector at14 and the R-born
tooth at15. The additional pre-funded cell(-4,4) is imported at10 and
consumed at20. No input was added mid-run and no component was relocated.

Thus a real chronological transport exists, but it spends prepared support.
It does not regenerate its whole input or demonstrate a repeating circuit.
The contrasting T followed by S positive control has initial mass5 and
different actual old-module costs; both full traces are recorded.

This is why the earlier fixed-profile noncomposition and the present positive
WORD edge are compatible: outside input can alter the first word's complete
profile while preserving its turns, and that changed profile may transport
one output to the next word. Universal resource claims must cover all such
realizing fields, not only these chosen minimal controls.

## 5. A finite-support exclusion of the singleton SCC

For U=RRRRLLLLRL the heading restores and its drift is(1,1). At phase5 its
cell is(-1,0), and its turn is L. That phase is the ONLY read phase with
x-y=-1. Because the drift preserves x-y, in copy k this required L is at

    (-1,0)+k(1,1).

No earlier or other U-copy read can occur at that cell: another phase has
the wrong x-y, and phase5 in a different copy is a different cell. Therefore
each U copy consumes a distinct lifetime already BLACK AT THE START of
that U-run. These may have been R-born before the run; they are not claimed
to be time-zero seed cells. A prefix of n copies requires at least n black
cells at that one starting cut, and U forever is impossible from finite
support. This is a supplied-word fresh-input argument, not a
claim that all old imports obey such a bound.

Conditionally on the separately checked cap7 grammar/return coverage, any
hypothetical sustained-cap7 finite-support orbit must therefore eventually
use only the S/T SCC. The substantive remaining question is the complete-
field resource and causal organization of arbitrary nonperiodic S/T mixtures.
No cap7 exit or global capture follows from the current graph alone.

## 6. Artifacts and audit boundary

`check_cap7_word_pairs.py` replays each individual minimum and all529 pair
minima, constructs both exact edge sets and their SCCs, and retains literal
lifetimes in every positive model. `cap7_word_pairs_certificate.json` binds
the source word-filter certificate, all529 witnesses/models and both graphs.
Its negative checks are monotonic necessary conditions and its positive
checks are complete actual-board executions.

Grammar coverage, exact58-word projection, the individual23 first returns,
and general import-budget lemma are separate dependencies; no154M-profile
expansion or solver claim is made. The existing cap6 theorem, fixed-profile
obstructions and cap7 nonempty-core result remain unchanged.
