# Cap-four continuation checkpoint

23 October 2026, 01:01 UTC. Unrestricted cap four remains OPEN.

## Signed reduction

The unrestricted cap-three exclusion is now signed in
`cap_three_shifted_stream_height.md` (audit GG). The cap-free necessary
unique-maximum condition is signed in `white_front_stream_defect_criterion.md`
(audit GH). Under cap four, every candidate must contain one of the six
normalized incoming-heading lists WEW, WWW, WEWE, WEWW, WWWE, WWWW.
The corresponding turns are RLR or RLRL. The independently signed
01:17 strengthening guarantees that at least one of these defects attains
the global shifted-height maximum uniquely among its four incident faces.
A local search may therefore impose that every nearby face has height at
most that selected peak; it must not impose this on every defect.

## Exact methods in progress

1. `synthesize_white_cylinder_cap.py` is a generalized exact cylinder-clock
   encoding with all31 complete white histories through four visits. It does
   not apply the special11-state cap-three pruning. It currently has fixed-
   strip UNSAT results for d=(2,0), width3; d=(2,2), widths3 and6. Broader
   cases are UNKNOWN. These are solver outcomes, not unrestricted theorems
   or independently checked UNSAT proof certificates.

2. `cylinder_voltage_order_criterion.md` replaces integer clocks by an exact
   event-permutation/voltage condition. The associated implementation
   `synthesize_white_cylinder_lazy.py` learns clauses from nonpositive-voltage
   cycles and positive-voltage wrong-order segments. The analytic criterion
   and both lazy clause types are independently signed. Its first cap-four d=(2,2), width6
   run reaches fixed-strip UNSAT after1945 learned clauses, about34 seconds.
   Larger strips are running. Standard104 and full-drift repetitions at
   periods208 and312 pass author controls and100-period finite-seed replay.

3. `search_cap4_patch_chains.py` is a faster exact open-patch chronology
   relaxation. Internal successor chains must be acyclic and cannot be
   interleaved in time. Their whole-chain precedence graph must be acyclic.
   This is equivalent to existence of distinct integer local read times
   obeying all internal edge-successor equalities and local history orders.
   It does NOT construct outside connectors or an actual full ant orbit.

All six necessary cap-four defect types have such locally consistent
5-by-5 open-patch models, saved as `cap4_chains_r2_c0.json` through c5.
Consequently their exclusion cannot follow solely from these radius-two
local edge-count and chronology conditions. Larger-radius searches are
running; no local UNSAT or genuine new periodic front is claimed.

## Additional exact static structure, not yet separately audited

Look at physical edges used at least three times. Every nonisolated edge
has count exactly3. Their components are directed paths/cycles. A path end
is a repeated-R-heading triple; internal vertices are quadruples. At a
quadruple whose two R headings agree and two L headings differ, the count3
path turns right. At a quadruple whose two R headings differ and two L
headings agree, it turns left. The remaining two quad cases have either
all four ports of count2, or one count4 edge and two other count2 ports.
A count4 edge is an isolated high-flow component, pairing an ABAB source
(all four exits agree) with an AAAA target (all four arrivals agree).
This follows directly by enumerating the16 four-visit heading lists per
checker sector. Unlike cap three, arbitrary left/right high-flow paths
and four-valent odd-edge vertices now occur; no global separation or
balance theorem is inferred from this table.

## Status discipline

All prior cap-three artifacts and searches are preserved. The older
one-A injection route is bypassed by the shifted-height theorem, not
retroactively declared solved. No finite width, period, iteration limit,
local SAT patch or timeout is evidence for a full classification. No
novelty claim or claim to have settled the finite-seed conjecture is made.

## Global maximum plateau restriction (signed 01:25 UTC)

`cap_four_top_plateau_essential.md` proves that every component of the
clockwise faces attaining the global shifted-height maximum is essential
on the full-drift cylinder. The graph is nonempty, and no finite lifted
component can occur: its incident vertices are closed under strictly
earlier first-visit predecessors. This is an unrestricted necessary
condition for cap-four fronts, not their exclusion.

The plateau argument has a separately signed strengthening: EVERY
C-superlevel graph has no finite physical component. For levels above
both exterior C heights, every cylinder component is essential. Internal
empty vertices are omitted from the first-predecessor set. No ridge
exclusion follows merely from this maximum principle.

## Signed unit-diagonal full-drift exclusion (02:01 UTC)

`cap_four_unit_diagonal_drift.md` excludes cap-four fronts with full drift
(1,1), and its quarter-rotations, at every period and width. Static local
count constraints force even seam voltage, while a full-drift front has
voltage1. The independent complete transfer graph has62 states,148 edges,
and24 reachable states with an exact parity potential. This does not
exclude larger diagonal drift vectors or cap-four fronts generally.

- `unit_diagonal_window_exclusion.md`: full drift(1,1) and its quarter
  rotations are excluded through visit cap SEVEN, all periods and widths.
  Independent reconstruction starts from all510 unpruned histories and
  verifies the18-state finite chronology-window certificate. This does
  not exclude cap eight or other full drift vectors.

## Signed full drift (2,2) cap-four exclusion (02:22 UTC)

`full_two_diagonal_window_exclusion.md` excludes complete white-input
cap-four fronts with full drift (2,2), and its quarter rotations, at every
width and period. The independently reconstructed three-row chronology
automaton has1,275 reachable lifted states and4,944 accepted edges. All
empty-to-empty paths have even voltage, whereas a full front has voltage
one. Nonempty even-voltage returns remain; larger drift and cap five are
not inferred.

## Signed finite chronology zones (03:01 UTC)

`frontier_clock_zone_abstraction.md` gives an independently audited finite,
safe all-width abstraction retaining global path connectivity, cyclic
block order and integer clock inequalities. Its unit-diagonal cap-ten and
cap-twelve applications are method controls, not classification advances:
the retained source already excludes that full drift at every cap.

`two_diagonal_zone_exclusion.md` independently excludes visit cap five
for full drift (2,2), and quarter rotations, at every width and period.
Thus such a front must have some cell visited at least six times. General
cap-four fronts and standard104 uniqueness remain open.

The full-drift (2,2) finite-zone exclusion is now independently signed
through cap SIX, so every such front needs a cell visited at least seven
times. Its complete graph has 46,969 states and 46,969 edges. See the
addendum in `two_diagonal_zone_exclusion.md`. Cap seven remains unresolved
by the current method.

## Signed axis and chiral small-drift extensions (03:33 UTC)

`axis_frontier_zone_geometry.md` independently excludes visit caps through
EIGHT for actual full drift (2,0) and quarter rotations, at all widths and
periods. Its complete cap-eight graph has 17,736 states and edges. Thus
such a front needs at least nine visits somewhere.

`general_drift_frontier_geometry.md` gives exact nearest-row representatives
for any supplied full drift, including negative slopes. Independent
physical reconstruction excludes cap FOUR for full drifts (3,1) and
(3,-1), separately, and their quarter rotations. The complete graphs have
440 and 400 states/edges. Thus these drifts need at least five visits
somewhere. Reflection is not assumed. These finite supplied-drift results
do not classify all drift vectors or settle general cap four.

## Signed all-cap axis boundary restriction (03:44 UTC)

`axis_extreme_ballot_addendum.md` proves that at actual full drift (2,0),
the lowest active row is either singleton in both classes or has at least
FOUR visits per class. There is no cap on upper-row multiplicities. Ordered
horizontal E/W matching satisfies a necessary prefix ballot inequality;
combined with physical first-return ranks it excludes bottom multiplicities
two and three. This does not yet exclude larger multiplicities or all
horizontal fronts.

## Signed singleton axis boundary theorem (03:56 UTC)

`axis_singleton_extreme_theorem.md` strengthens the previous boundary
restriction to ALL multiplicities: at actual full drift (2,0), the lowest
active row has exactly one complete visit in each of its two classes.
Quarter rotations preserve the corresponding right-side extreme. An
eight-step first physical return closes the port-ballot argument, with no
cap, width or period cutoff. The opposite transverse extreme is not silently
identified by reflection. Propagating this singleton boundary through all
remaining rows is still open; no all-axis exclusion is claimed.
