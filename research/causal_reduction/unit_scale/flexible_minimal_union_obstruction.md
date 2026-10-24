# The two minimal bypass mechanisms cannot support one another

23 October 2026, 14:36 UTC. Author full semantics and checked RUP certificate; independent semantic review requested. This checks the UNION of two already derived minimal image families, not longer images or a new numerical length bound.

## 1. Exact combined language

Use the inverse104 coarse path and the position/heading tiling conventions of flexible_heading_defect_classification.md. Every actual tile boundary has its coarse position and either sign of the coarse heading. Allow:

1. A one-read position-preserving reset at every uncovered coarse index, from either incoming heading sign.
2. A two-index six-read heading flip, one of the three minimal geometric routes, from either incoming sign, ending at the opposite coarse heading.
3. A two-index ten-read endpoint bypass, one of the two minimal intermediate-pose-avoiding geometric routes, from either incoming sign, ending at the positive coarse heading.

For negative incoming sign, a ten-read bypass changes only its FIRST turn relative to the positive-input word. This gives the identical physical positions and headings after that first move and therefore the same verified endpoint and intermediate-pose avoidance. The complete per-phase domains are frozen in flexible_minimal_union/domain_manifest.json.

Tiles may start at either parity, may change alignment at any occurrence and may mix mechanisms arbitrarily. They cannot overlap. Adjacent genuine boundary headings must agree. No common controller, periodic assignment, prepared rail, initial mass or output-field condition is imposed.

Every legal infinite schedule in this combined language is eventually an arbitrary binary sequence of V and P108, hence consumes at least8 black cells per coarse period and cannot run from finite black support.

## 2. One exact finite obstruction

The finite domain covers coarse indices0..727 and permits complete crossing pairs starting -1 and727. Each pair start has ten choices: two input signs times three six-read flips and two ten-read resets. Monomers are present exactly at uncovered internal indices. All boundary headings and all275 initial physical-cell colors are free. Output is unrestricted.

Require a central-period tile whose first movement opposes the coarse first movement. This includes ALL ten-read bypasses and the one genuinely backward route among the three six-read flips. Exact current-color/XOR chronology yields:

49117 variables;
234725 clauses;
UNSAT with37510 monotone RUP additions, separately checked without RAT or deletions.

CNF SHA256 83f44a99c6662100b3d3ea2159e1391f85f9658b2fe113b034af4e719511e921
RUP SHA256 218186680b65819dbf7bbc117a1951a91dbc125469bb5f2c9e99052d1b7ed49e
Source SHA256 f5c7813df2fa47bdb66cab9c752a3ff9627070955e2d4b013896a99ea2012f3f

### Important overlap correction

Each separate image palette had same-cell period span3, but their UNION has span4 on the orbit(1,1), with phase levels-2 through2. Every other orbit has span at most3. Therefore seven periods are NOT claimed to contain the full radius-four neighborhood.

This does not weaken the finite obstruction or its infinite-schedule implication. All entry colors are arbitrary, and the window is an ACTUAL continuous finite word with complete crossing boundary tiles. Every actual infinite schedule restricts to one such finite word, regardless of how often its cells were read earlier or will be read later. Outside histories can constrain the free entry colors but cannot rescue an internally inconsistent finite word. The explicit seven-period problem already fails; no horizon escalation or assumption about forgotten memory is needed.

## 3. Consequence and exact remaining positives

Sliding the seven-period finite obstruction excludes all sufficiently late backward tiles of either type. Thus every late ten-read bypass disappears, as does every late genuinely backward six-read flip. The remaining nonbackward six-read flips are square insertions at coarse endpoints.

The analytic recut in flexible_heading_defect_classification.md applies unchanged: combine each square with the following coarse move; alternation at the square source forces exactly RLLLL or LRRRR. The separate, stronger free-input square-classification circuit permits only phase31 insertions after a finite prefix. Hence only V/P108 periods remain, with turn excess-12/-8.

The all128 binary seven-period V/P108 prepared positives are retained from that independent square-classification control. There is no assertion that they share one finite seed. There is also NO forward-H time-reversal claim for the combined position/heading language, since opposite boundary headings change the reversed boundary positions.

## 4. Full controls and limits

check_minimal_union_controls.py reconstructs34 complete finite tilings, including both optional crossing boundaries, mixtures of six- and ten-read tiles, changing alignment, both initial heading signs, and dense/sparse random choices. Every active physical event and all Boolean clauses agree with direct literal traces. Identity inverse104^7 and all-P108^7 are legal positive controls with minimum inputs97 and90. The explicit union footprint control gives the corrected span4 above.

Files: check_flexible_minimal_union.py; check_minimal_union_controls.py; flexible_minimal_union/minimal_union.{architecture.json,cnf,rup,result.json}; domain_manifest.json; controls.json. The square-recutted conclusion additionally uses the separate square CNF/RUP and analytic recut from flexible_heading_defect_classification.md.

This theorem covers exactly these supplied minimal position/heading-reset, heading-flip and endpoint-bypass shapes. It does not cover nonminimal images, overlapping edits, other coarse scaffolds, extra off-backbone interventions, or arbitrary ant paths. It does not solve the global highway conjecture.
