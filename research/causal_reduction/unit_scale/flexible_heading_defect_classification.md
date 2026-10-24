# Minimal heading defects with no fixed pair alignment

23 October 2026, 14:31 UTC. Author semantic proofs and checked RUP certificates; independent review requested. This removes fixed alignment from the signed minimal-heading architecture. It does NOT combine its six-read tiles with the separate ten-read full-pose bypass palette.

## 1. Exact position-preserving tilings

The coarse path is the fixed inverse104 V, incoming W and drift(-2,-2). Tile boundaries retain their coarse POSITIONS. Their actual heading may be the coarse heading or its opposite, represented by one sign bit.

Allow a monomer at any uncovered coarse index. From positive heading it reads the coarse turn; from opposite heading it reads the opposite turn. In either case it makes the same coarse physical move and resets the outgoing heading to the coarse one.

Allow a two-index tile at any coarse index. It is one of the three analytically minimal six-read routes to the coarse pair's endpoint with final heading opposite the coarse endpoint heading. Both incoming signs are allowed and determine the first turn. All route cells, source/endpoint visits and colors are retained. Tiles cannot overlap. The old unique two-read reset is exactly two monomers, so the new language contains every old fixed-alignment schedule and permits arbitrary alignment changes.

At every genuine boundary the adjacent tiles share the same heading bit. No heading is independently reset or ignored.

Every one-sided infinite legal schedule in this architecture eventually has only ordinary V periods or the known P108 square insertion at phase31. In particular it cannot start from finite black support: each such period has turn excess -12 or -8.

## 2. Eliminate genuinely backward tiles

Among the three six-read routes, exactly one first moves opposite the coarse first movement. The other two follow the coarse pair's physical moves and then make a four-read square at the endpoint.

The complete potential read geometry, over all104 possible tile start phases and both heading signs, has same-cell period span at most THREE. Use seven periods, coarse indices0..727, with optional COMPLETE crossing pairs starting -1 and727. Monomers occur only at internal uncovered indices. Boundary heading bits are free at every vertex -1..729, including both true endpoints; bits at an interior vertex hidden by a two-index tile are unused.

Six pair selectors at each start represent incoming sign times route choice. They imply their actual incoming boundary bit and a negative outgoing bit two indices later. Pair-presence bits prohibit overlaps. Each monomer has two incoming-sign selectors, requires the corresponding incoming bit and positive outgoing bit, and is present exactly when neither adjacent pair covers it.

Every physical cell has an arbitrary input bit and unconstrained output. Selected reads are ordered by coarse start/local read index and use the exact event OR/current-color/XOR recurrence. Require one backward tile starting312..415.

UNSAT:28691 variables,122459 clauses,16819 checked monotone RUP additions.

CNF SHA256 b47def387c7951e18c379d62d1fa470bf336016fa70a041b337cdbe20dd71f58
RUP SHA256 4a909083fdfe6f4a59e1267191018eac1bd543f7d8f1886e9d0d1f2f2f8bd8ea
Source SHA256 709eb77ce949002caf744d6b2af06c6527efa745d9abd4bb6142d862ec582b24

As in the separately signed flexible full-pose bypass theorem, every actual tiling restricts to one of these finite assignments, including crossing tiles. Sliding the window excludes all backward tiles after a finite prefix.

## 3. Exact recut of the remaining squares

Beyond the last backward tile, every remaining two-index flip first executes the coarse pair and then a four-move square at its endpoint. Take the next coarse boundary BEFORE this square rather than after it. The square starts at the ordinary coarse incoming heading and returns to the same cell with opposite heading. The following physical move follows the prescribed coarse direction, because it is either a monomer or the first move of another nonbackward tile.

Combine that square with the following move. The square's first read and the following move read the SAME source cell, and the square's other three reads are at distinct cells. Internal alternation therefore forces their turn letters to be opposite. For a coarse R, the combined word is precisely RLLLL; for coarse L it is LRRRR. The other orientation of the square would repeat its source color and is illegal.

Thus the literal infinite tail, after a harmless finite boundary cut, is an exact unit-pose refinement of V, with independently optional five-read square images at arbitrary coarse positions. This argument uses no common pair alignment. There is at most one square before each coarse move because the two-index tiles do not overlap.

## 4. Classify unit squares without parity restrictions

A second seven-period circuit independently allows every one of728 coarse reads to choose its identity or c opposite(c)^4 image. ALL221 physical input bits are free; all output bits are free. It requires a central-period square at some coarse phase OTHER THAN31. This is a stronger relaxation than the recut schedule: it imposes no restrictions inherited from the tiling.

UNSAT:8957 variables,27665 clauses,88 checked monotone RUP additions.

CNF SHA256 57fe051aad75c2590536cbb4d98440e65553ea02abba58b0bfe2a911718c519a
RUP SHA256 ae765fa25a43bcf4aa44f12c00c7469f653fecd645cc07ba34539bad22df25ad
Source SHA256 491f08bee6e7c3bee36e27a39a47ea9bbc904c232ea4b41eb8d660a26fa9b271

Sliding this circuit along the recut tail proves eventual square insertions only at phase31. Here V[31]=L, so the only two eventual physical periods are V and V with that L replaced by LRRRR, exactly P108. Their turn excesses are -12 and -8. Since every R adds one black cell and every L removes one, infinitely many such periods are impossible from a finite black field. No exact final threshold is claimed after the recut.

## 5. Nonvacuous controls and limits

check_flexible_heading_controls.py checks29 complete heading-compatible physical tilings against direct literal traces, every active event order, and the entire circuit, including both crossing boundaries and both initial heading signs. The identity seven-period word and all-P108 seven-period word are legal positives with minimum input97 and90 respectively.

The separate square controls include ALL128 seven-period binary V/P108 mixtures. Every one is legal, with minimum input97 minus its number of P108 periods. Twenty arbitrary square assignments and the identity/all-P controls bring the square-control total to150; all literal/Boolean comparisons agree. These are genuinely nonstationary prepared-input positives, not finite-seed realizations.

Files: check_flexible_heading_backward.py; flexible_heading_backward/flexible_heading.{architecture.json,cnf,rup,result.json}; check_unit_square_flexible_classification.py; unit_square_flexible_classification/square.{architecture.json,cnf,rup,result.json}; check_flexible_heading_controls.py; flexible_heading_backward/controls.json.

This is an inverse-scaffold position/heading result. Do NOT infer a forward-H corollary by the full-pose reversal proof: reversing an opposite-heading boundary also changes the transformed boundary position. Longer images, a mixture with ten-read bypasses, other scaffolds, and other endpoint geometries remain outside. No global highway theorem follows.
