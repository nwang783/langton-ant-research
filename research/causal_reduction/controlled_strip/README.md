# Protected exploration: controller-driven pristine half-strip builders

Started22 October2026,17:46UTC after the independently audited six-row cap
obstruction. The target is deliberately different from increasing a cap-word
or cap-height bound.

An initially white half-strip x>=0, 0<=y<H is driven by arbitrary legal left
entries(0,y,E), y odd, in the sector H-cells at x+y odd. Each excursion must
return left without leaving the top/bottom strip. The external controller
chooses the next odd entry row. Does there exist a fixed H and a safe infinite
controller sequence, ideally an exact regenerative family of finite fields?

This challenges the STRONGER pristine-barrier candidate in
`frontier_exploration/column_exclusion_rank.md`, not directly the finite-seed
highway conjecture. Heights<=9 are already excluded by complete audited block
invariants. No all-height bound or infinite controller witness is known.

## Why an infinite safe controller must build unboundedly

A finite-width controlled excursion graph is acyclic, even from an arbitrary
initial field. If a nonempty sequence returned to the same complete finite
field, choose the rightmost column read during the sequence. Every visit to
it is a reflection from the left, so its exclusion first moment strictly
increases at each visit. It cannot finish with its initial field. Equivalently
an infinite safe sequence confined to finite width contradicts the same rank.
The arbitrary re-entry row does not change any internal lamp between visits.
This is an elementary consequence of the audited column rank, not a new
claim of global convergence.

A rough quantitative control follows. Put K=floor(H^2/4), and suppose all
excursions stay within W columns and return left. Let A_j count entries into
column j from its left. Every crossing into column j+1 eventually returns,
so there are A_(j+1) left-to-right transmissions and the same number of right
entries in column j. Between these exceptional visits there are at most K
left reflections. Thus

 A_j <= (2K+1) A_(j+1)+K,  A_W=0,
 A_0 <= ((2K+1)^W-1)/2.

The qualitative acyclicity is enough here; this bound has not been separately
submitted for audit and is not used to assert a computed infinite behavior.

## Certificate target, and why a finite static controller is insufficient

Seek finite fields C(n) with a proved complete excursion update
C(n)->C(n+1), preserving a fixed-height periodic bulk and extending its width.
All colors, boundary entry/exit rows, and old-cell read sets must be retained.
A finite run or a repeated local pose is not a certificate.

An infinite controlled builder alone would NOT be an autonomous finite-seed
counterexample. A bounded finite external controller cannot return the ant
infinitely often either: the reflected one-sided column-rank argument applies
to it. An autonomous construction would need, for example, TWO expanding
mirror builders with matching port histories, not a static reusable cap. A
certified two-ended fixed-height expanding shuttle would already be a direct
nonstandard finite-seed counterexample, without any universality claim.

## First discovery tool

`periodic_ports.py` tests periodic external entry-row words from a white
half-strip, preserving the complete field as an unbounded integer mask. It
rejects vertical exits. Spatial/step/survival caps produce UNKNOWN candidates,
never infinite certificates. An exact finite board repetition is asserted
impossible by the rank argument. This is discovery, not an exclusion theorem
for longer controllers or transient initialization.

The first height12/period<=6 test covers37,709 feasible initial controller
prefixes; all repeated controllers eventually leave vertically, with maximum
36 excursions. Larger controller experiments are recorded separately. The
reported maximum x is an exploratory statistic; its initial-period value is
inferred from the final mask and may omit a restored frontier cell. Any
candidate or extremal statistic must be literally replayed before citation.

## Further bounded controls and the current structural target

The height24/period<=6 test covered2,959,607 feasible prefixes and ended every
repeated controller vertically (maximum180 excursions). Height32/period<=5
covered1,078,393 prefixes, maximum286. Another450 structured controllers at
heights32,64,128 and6,326 nearest-row feedback controllers also all ended
vertically. These are discovery controls, not all-height exclusion results.

A fixed-source unbounded-height probe from white completed313 excursions;
the next reached its10-million-step cap. It is recorded as UNKNOWN, not as an
infinite builder or a proved highway, even though its endpoint looks highway-
like. These experiments do not establish anything about other initial fields.

The current exact construction target is described in
`swept_front_certificate.md`: a moving right endpoint behind which every bulk
cell is reread forever. Its complete histories are finite transients followed
by periodic strings, rather than the finite histories of ordinary translating
fronts. A separate left-fringe/port certificate would be required for gluing.

The computability analysis independently audited the half-turn-copy gluing
bridge: a right-half-plane builder with appropriately matched periodic ports
can be paired with a phase-shifted half-turn copy. The autonomous finite-seed
orbit would revisit a finite set of cut poses infinitely often and therefore
have no translating periodic tail, even without a height bound. No such
builder is known. Constant ports are a special case; a genuine even minimal
entry-port period cannot match a single constant-offset half-turn copy.

`rail_transducer_search.py` is a DISCOVERY quotient, not a proof automaton.
It keeps finite left/right fringes and compresses a long period-two column run.
A positive run-length cycle would still require independent all-parameter
chronology verification. The column mod4 invariant rejects length growth of
a lone solid rail and of two same-parity rails before any search; the current
eligible prototype uses two opposite-parity rails. Bounded searches and
unexpanded frontiers are retained as controls, not inferred exclusions.

The current paired-arm right-end model is specified in `paired_arm_resets.md`.
Its whole-field cycle test retains all finite defects, but a cycle would still
need a legal far-left turnaround and complete finite-arm gluing. No cycle was
found in2000 bounded charge-compatible cap samples. These all hit declared
bounds and are UNKNOWN, not exclusions. Each reset type must occur a multiple
of four times in any hypothetical complete relative cycle, by row charges.

Provenance caution: informal larger-height transmission observations in the
retired frontier note have no surviving controller trace or final combined
JSON. Only the independently replayed height-nine barrier is used here as a
proved pristine-strip obstruction.
