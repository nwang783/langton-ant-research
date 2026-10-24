# Two targeted self-return adaptations fail for explicit physical reasons

24 October 2026. Failed constructions, not a universal obstruction. No random
seed scan, cap8 kernel expansion or evidence for the conjectural16/4 constant
is claimed. Full fields are retained in every executed finite prefix.

## 1. Removing the old remote turnaround from the20-cell circuit

Start from the retained fresh four-cell outgoing port

    G={(0,-1),(1,1),(2,2),(1,3)}, head(0,0),E.

This is the compact first port of the20-cell circuit with the old remote
turning ports removed INITIALLY, not erased during an execution. Its R60
lifetime at(0,2), the marked input in that circuit, is tracked explicitly.

At cut182 the actual pose is(5,1),E and the complete local field has36 black
cells. The retained exact periodic-tail verifier certifies standard104 forever.
Its phase-read x range is[4,9] and drift(2,2), so its later head never reads
the marked cell(0,2). The marked lifetime is not consumed: this attempted
self-made far RETURN simply does not occur.

The same conclusion holds if only the FIRST remote turning port is removed
but the remaining three old ports of the20-cell family are retained. For
even n>=20 their x maxima are -n,-5n+8,-3n+2, all negative. The fresh prefix
and all future H rays have nonnegative x. Those unused old black cells remain
on the board and are never read; removing them initially gives the compact
four-cell version above. This proves failure of this particular adaptation,
not that every compact source needs a remote old turnaround.

## 2. One explicit growing S/T loop fails a repeated-R guard

Try the canonical four-turn expanding lap

    lap n = T^(n+1) S T^(n+1) S T^(n+2) S T^(n+2) S,
    S=RRRRLRLRL, T=RRRRLLLLRLRL, n>=0,

starting north with continuous physical pose. Four S turns restore heading;
the actual lap displacement is(0,-4). This was a specific proposed way to
reuse self-written lanes for a later turnaround, not a family enumeration.

The proposal already fails in its second lap, for EVERY initial board:

* At global update15, lap0's first S, phase3, reads(2,1) as R.
* At global update139, lap1's first S, phase7, requires R at(2,1) again.
* There is NO intervening read of that physical cell.

The cell remains black after the first R, so the second required R is
impossible. Changing any initial exterior bit cannot repair this repeated-cell
conflict. The139-update valid prefix has a concrete25-cell minimum seed and
complete active-w peak10; it is recorded for replay, not presented as a
completed far-feedback test.

Geometrically the successive first-S entries differ by(2,-2). That places
the earlier S's phase3 R on the later S's phase7 R port. Any repaired route
with that placement must include an actual intervening L retirement of the
same lifetime; free relocation or reuse of a stale R port is not permitted.
This is an exact obstruction to THIS route schema, not a theorem excluding
different S/T mixtures or a new supplied-word validation principle.

## 3. Evidence and next obligation

`check_compact_self_return_attempts.py` records the full fresh-port prefix,
the existing infinite H certificate, exact negative-x exclusion of unused
ports, and the complete139-update minimum-board replay with its R/R witness.
`compact_self_return_attempts_certificate.json` binds those results.

Neither attempt supplies a compact self-made far return, so neither decides
RH16/4. The fixed-parameter marked-component erasure lemma remains the proved
spatial fact; the actual-maximum conjecture and any exhaustive compact-search
reduction remain unproved/withdrawn as stated in its corrected v3 note.

A useful next construction must write and legally retire/reinstall its own
turnaround ports while preserving the marked lifetime and a measured full
active cap. Repeating nonqualifying simulations or calling these failures a
global obstruction would not close that obligation.
