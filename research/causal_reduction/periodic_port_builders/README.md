# Three-phase half-plane builder exploration

Status, 22 October 2026: no renewable builder, finite-seed counterexample, or
all-width obstruction has been found.

The conditional half-turn gluing theorem is in
computability/halfstrip_builder_reductions.md. A controlled right builder with
entry rows(0,4,8), exit rows(1,9,5), phase offset2 and half-turn height sum9
would autonomize with a second, disjoint half-turn copy. Both complete fields
and all future excursions must be certified; an externally reset controlled
trace is not itself an ant orbit.

## Necessary minimal bulk

For a same-phase cap translated two columns while its left fringe restores,
row mod4 charge requires odd columns to contain rows0,1,4,5,8,9 and even
columns to omit them. The gap rows2,3,6,7 may be filled uniformly in both
column parities. Column charge requires equally many filled even/odd gap
rows, leaving six possible fillings. The minimal masks are(0,819).

Six-row versions are not finite-seed counterexample targets: the existing
independently audited height-nine strip exclusion already rules them out.
This ten-row target avoids that specific barrier but is not known feasible.

## Exact finite-interface graph controls

front_graph.cpp and synthesize_striped_front.py implement the same explicit
bounded-memory front model. An H-by-W board window follows the rightmost
visited column. On first entry into the next right column, the window shifts,
loads that column from the specified two-column-periodic infinite input, and
discards the leftmost column. Exiting left or vertically is rejected. Every
initial window coloring, phase and head pose is included. A positive-shift
cycle is an exact infinite-input traveling front, not a finite-support orbit.

The C++ graph completed all167,772,160 states for each of the six ten-row,
two-column gap fillings. Minimal masks(0,819) have no cycle. Four fillings have
only the saved period4 or period12 cycles; the fully filled gap case has none.
All maximum transient paths are54. Raw results are
three_band_gap_rails_h10w2.json. These exhaustive graph counts have not yet had
an independent audit. The known S=RLLR solid-row transfer is a positive control.

## New literal bulk transfer

three_band_front_profiles.json gives complete displacement-class read strings.
With rows4 and5 black at odd x and white at even x:

- LRLLRRRRLLRL from(0,3,E), sector0, drift(2,0), moves a solid row3 to row6.
- RRRRLRLLLLRL from(0,4,E), sector1, drift(2,0), moves a solid row6 to row3.

Both restore the alternating rows4,5. Their read strings are RL in each even
column and LR in each odd column on those interior rows. The removed solid
row reads L once per column, and the new solid row reads R once per column.
All other rows are spectators. Thus these are exact all-epoch bulk identities,
not sampled repeated tails. They do not provide either required finite cap.

## Wider search status

sat_front_cycles.py is an SMT bounded-cycle synthesis for the same model with
larger window width. It uses the already installed Z3 C API and literally
replays every SAT model. A positive period12 control passes. The first
H10,W4,T64 minimal-mask attempt timed out at every tested period4..64; all are
UNKNOWN, not exclusions. No claim follows from those timeouts.

## Same-sector bulk inverse pair, independently checked

The period12 upward transfer on masks(1,7) has a different period28 inverse
traveling in the SAME direction and SAME sector1:

    A12 = LRLLRRRRLLRL, entry(0,0,E), (1,7) -> (8,14)
    B28 = RRRLLLLRLLLLRLLLLRRRRLRRRRLR, entry(0,2,E), (8,14) -> (1,7).

Both drift(2,0). A restores the two interior alternating rows after two reads
per drift class; B restores them after six reads. The stable quotient identities
passed independent no-import replay in audits/check_12_28_bulk_independent.json.
This is not a claim that the unmodified bilateral source board at epoch zero
supplies every interface read. B needs a prepared finite left interface.

The full four-row, three-column interface catalog visits100,663,296 graph states
over all256 two-column-periodic inputs and finds140 cycles of periods4,8,12,20,28.
The catalog is an exploratory bounded-memory result, not independently audited.

## Finite three-port negative controls

A3,000,000-seed evolutionary search in an8x10 initial rectangle completed at
most two prescribed excursions, never a complete three-phase cycle. The literal
best prefix is saved in three_port_seed_search.log. A separate exact short-word
search fixes the first excursion LL and excludes completion of the next two
excursions through52 updates inside the12x10 rectangle; at56 it hits a100m-node
cap. Both are scoped controls, not an all-width or all-length obstruction.

## Withdrawn white-input axial wake target

Correction22October22:25UTC: masks(513,519) are impossible. I incorrectly
transferred the returning-builder column-charge condition0 mod4 to a front
that crosses each column from left to right. Such a crossed column must
instead gain alternating vertical black charge2 mod4. The proposed masks
have charge0 and therefore fail an exact invariant, regardless of period.
All SMT timeouts on that target are discarded as searches on a bad target,
not exclusions or evidence about viable fronts. The A12/B28 nonwhite bulk
identity and the three-port returning-builder filters are unaffected.

A simple charge-compatible replacement adds a solid EVEN row10, giving
masks(1025,1031), height11. A height10 alternative adds solid rows4,6,9 to
the catalyst, giving masks(593,599). Both still need drift divisible by8
by their alternating-only rows1 and2. Neither is a constructed front, and
neither has been searched here. Passing these filters does not imply existence.
