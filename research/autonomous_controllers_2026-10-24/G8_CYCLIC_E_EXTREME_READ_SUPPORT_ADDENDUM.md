# Exact mandatory-odd-read-extreme lemma for the final stock rejection

24 October 2026. Mandatory scope clarification for the author
G8_CYCLIC_E_EXCLUSION.md8981c7ff. This supplies the full elementary lemma,
not a generic finite-maximum heuristic. Submitted for independent review.

## Spatial object and hypotheses

Work in the canonical complete initially WHITE front with actual full
period P, full drift d=(2,-2), and checker/heading-axis sector sigma=+1.
Let q_0,...,q_(P-1) be the physical READ positions of one event period.
The complete bi-infinite read footprint is

    R = { q_i + k*d : 0<=i<P, k in Z }.

It may be infinite along the drift. Its normal coordinate t(x,y)=x+y is
unchanged by d. Therefore

    H = max_i t(q_i) = max_{q in R} t(q)

exists and is finite. This is the maximum of the ACTUAL READ FOOTPRINT,
not the maximum of the black field, odd emitted wake, a C/L potential,
an active component, or a chosen finite patch.

Every read has an actual previous read and next read in this complete
front, even at a chosen period seam. Every active physical cell has a
complete finite alternating history beginning R. These hypotheses remove
the one-sided initial-head and final-cropped-event exceptions.

## Literal extremal proof

Fix any read at a physical cell q with t(q)=H. Its predecessor cannot
lie at level H+1, so its incoming direction increases t: it is N or E.
Its successor also cannot lie at H+1, so its outgoing direction decreases
t: it is S or W.

The invariant sector sigma=+1 gives vertical incoming headings at even
t and horizontal incoming headings at odd t. Thus:

* If H is even, EVERY read at q must arrive N and leave W, hence turn L.
  But its complete WHITE history begins R. This is impossible.
* If H is odd, EVERY read at q must arrive E and leave S, hence turn R.
  Alternation of the complete history permits exactly ONE read at q.

Consequently H is odd and every visited full-drift class at level H has
multiplicity exactly one. At least one such class exists by the definition
of H. It is an odd class of the emitted wake O. The fact that it is an
odd output is derived from the full read history, not inferred by taking
the maximum of an already selected output set.

The same statement in other physical orientations follows by a genuine
quarter rotation of the entire state and coordinate convention. No
reflection, primitive-drift replacement, or finite-support truncation is
performed.

## Application to the338 odd/odd terminal-row candidates

In the candidate patch all named classes have t<=3. The lower four rows
already have six odd classes. Both new C classes at t=3 are odd, giving
eight distinct full-drift odd classes within the patch.

Each new C has exactly five outgoing S occurrences. Its outgoing axis is
vertical, so all remaining departures are N. Its complete history length
is9 or13 in these odd/odd cases, giving respectively FOUR or EIGHT N
outgoing occurrences, each forcing an actual next READ at t=4. Hence the
full footprint has H>=4. The extremal lemma forces H odd, so H>=5, and
at least one additional odd class at t=H. It is distinct from every named
class because its t-coordinate exceeds3.

Therefore these candidates would have at least nine odd classes, contrary
to g=|O|=8. Higher support is allowed to terminate, widen longitudinally,
or change shape arbitrarily; the argument follows the actual finite H,
not any assumed row recurrence. Every upper port remains open. It is
precisely its required use, not its omission, that causes the contradiction.

No initially BLACK reverse output root is discarded. No fact about an
unread field, potential maximum, or trajectory entrance is used.
