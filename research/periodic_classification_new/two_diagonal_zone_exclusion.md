# Full drift (2,2) requires a cell with at least six visits

23 October 2026, 03:01 UTC. Independently signed analytic and complete
finite-graph certificate. No width or period bound is imposed.

Every complete white-input translating Langton front with full displacement
(2,2), or an orientation-preserving quarter rotation, has a physical cell
whose complete history contains at least six visits. This is a cap-five
exclusion, not a classification of all fronts of that displacement.

## Model and geometry

Use representatives (i,i+t), i=0,1, for transverse row t. Each representative
has a white alternating local turn history of length at most five, including
the empty history. Incoming headings lie on the parity-prescribed axis.
Before any pruning there are 2*63^2 = 7,938 parity-labelled row states.
Vertical edges change t by plus or minus one, preserve i and have seam
voltage zero. At an odd row an east edge goes to column i+1 modulo two and
row t-1, with voltage one exactly when i=1. A west edge goes to column i-1
and row t+1, with voltage minus one exactly when i=0.

The port-count balance reduction from an empty exterior leaves 723 even
and 1,089 odd row states, with 31,992 static adjacent-row transitions.
The independent verifier starts before this pruning. Directed-edge exits
and arrivals are matched by their exact chronological ordinal.

## Finite all-width obstruction

Apply the independently signed finite frontier construction in
`frontier_clock_zone_abstraction.md`, with three-row local chronology
windows, voltage modulus two and difference-bound weakening threshold two.
A state retains the two most recent row histories, unfinished successor-path
endpoints and voltage residues, their cyclic block order, and a finite
integer normalized-clock zone. Complete local histories and physical edges
are never relaxed; only the stored clock bounds are safely weakened.

Every potential whole event cycle is explicitly retained as an exceptional
terminal outcome unless its voltage residue or clock inequalities reject it.
A sealed cycle with another component is impossible. Both reanchoring of
cyclic cuts and existential projection of retired clock variables are part
of the construction, not assumptions about a small period.

The complete reachable graph has 3,945 states and 3,945 accepted edges.
There is no terminal possible-front outcome. Every genuine finite-width
front would begin at empty lower rows, follow a path through this graph,
and eventually close its one full event cycle. The absence of any such
outcome proves the theorem at every width and period.

After deleting the two empty-state transitions, the producer graph is
acyclic; its longest path has five appended rows. This is an auxiliary
check, not needed for the all-width bridge.

## Independent reconstruction and controls

Producer: `probe_diagonal_n_zone.py` and `probe_diagonal_zone_general.py`.
Frozen full certificate:
`diagonal_n2_zone_cap5_window3_bound2_mod2.certificate.json`.
Independent checker: `../audits/check_diagonal_general_zones_independent.py`.
Independent result:
`../audits/diagonal_n2_zone_cap5_window3_bound2_mod2_independent.json`.

The independent code imports no producer, regenerates all 7,938 unpruned
row histories, derives physical coordinate edges and cut changes, and uses
Bellman-Ford closure. It checks all 49,997 outgoing extensions and 36,811
clock-zone closures, reproducing the complete graph exactly.

The generalized producer also retains standard104, doubled208 and
tripled312 as positive controls at their actual full drifts (2,2), (4,4)
and (6,6). Their actual integer normalized clocks satisfy a retained zone
at every frontier, and each reaches the explicit whole-cycle outcome.
They have maximum physical multiplicity ten and are not counterexamples
to the cap-five theorem.

No external novelty, formal-verification, standard104 uniqueness or
finite-seed eventual-periodicity claim is made.

## Independently signed cap-six strengthening (03:08 UTC)

The same full-drift (2,2) theorem holds with cap SIX: every such front must
have a physical cell visited at least seven times. The independent checker
starts from all 32,258 unpruned row histories and checks every extension
of the 46,969-state, 46,969-edge graph. There are 929,479 outgoing
extensions and 2,351,455 independent Bellman-Ford closures. No terminal
whole-cycle relaxation survives. The original cap-five certificate is
preserved as a smaller control.

Frozen certificate: `diagonal_n2_zone_cap6_window3_bound2_mod2.certificate.json`.
SHA256: `fcb9159777582678b8e73c24006499d1f4c9947cff8adecaf234e9f41e8f5a32`.
Independent result:
`../audits/diagonal_n2_zone_cap6_window3_bound2_mod2_independent.json`.
Cap seven has not been excluded: the next producer hit its explicit state
limit and reports UNKNOWN. No cap-ten conclusion is drawn from the
standard104 positive control.
