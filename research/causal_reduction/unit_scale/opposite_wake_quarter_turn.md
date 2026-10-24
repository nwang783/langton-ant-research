# Same-sector quarter turn against a mature104 wake

23 October2026,10:21UTC. Author exact certificate complete, independent review
requested. This is a ONE-SHOT prepared interface, not a renewable device.
It differs from KU's reversal: the incoming NW drift turns90 degrees clockwise
to NE, parallel to the old wake, instead of reversing on its original slope.

## Complete finite input

Let H and S be the retained standard104 word and13-cell seed, with incomingW.
For integers n,m>=50, construct Old_n by running H^(2n) from(-2n,-2n,E) on
CCW^2(S)+(-2n,-2n). Retain its COMPLETE board but not its ant. Add the disjoint
CCW^3(S)+(2m+3,-2m), and start the actual ant there with incomingN.
Both old generator and actual ant have invariant sector x+y+h=1 mod2.
The initial mass is24n+26; all seeds and both endpoint fringes are retained.
No path positioning the actual ant after generating Old_n is assumed.

## Exact routing and ownership

The actual word is H^(m-10) C H^infinity. The fixed word C is frozen in
`opposite_wake_quarter_turn_word.json`, length43871. It starts at(23,-20,N)
and ends at(91,-63,E). It reads5530 distinct cells in[-44,93]x[-85,29], has
complete XOR2857, and increases black mass by2121. It erases187 old-wake black
cells and changes332 cells within the old wake's complete strip.

The permanent tail starts at time104m+42831, at(91,-63,E), with drift(2,2)
and complete mass24n+12m+2027. Its canonical line x-y=154 is parallel to the
old generator line x-y=0. The incoming canonical line is x+y=3.

`certify_opposite_wake_quarter_turn.py` checks that the entire old wake misses
the incoming prefix, verifies every first-black/first-white collision guard
against the COMPLETE parametric entry board, applies the full XOR, and checks
all104 infinite tail families and262 prior same-cell relations. The JSON
preserves initial, collision-entry and postcollision fields. No sampled period
match, discarded remote fringe, or temporary highway supports the conclusion.

## Composition boundary

Every erased old black cell remains accounted for. This certificate supplies
neither the same old input again nor a trajectory that builds the old wake and
then reaches the incoming pose. Its outgoing NE wake is genuine newly written
material, but reusing it requires another actual arrival with the correct phase,
sector and complete surrounding guard.

Under physical rotations, this particular right-turn rule shifts each outgoing
line154 toward its right normal relative to the old parallel line. Consequently
an ideal clockwise ring using only this rule has inward, not outward, line
updates. This is geometric orientation bookkeeping only: no all-r ring
composition or global contraction theorem has been proved here.
