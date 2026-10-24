# A finite chronology-window certificate for unit diagonal drift

23 October 2026. Independently signed analytic and executable cap-seven
exclusion. Full drift is (1,1); no period or width
cutoff is imposed. Cap eight is not excluded by the present certificate.

## Cap-free balance reduction

The quotient and directed port equations are exactly those in
`cap_four_unit_diagonal_drift.md`. Starting from an empty even row, they
force equal R incoming-heading counts on every even row and equal L
incoming-heading counts on every odd row, at any visit cap.

For cap seven the complete white histories satisfying these identities
number61 on even rows (empty, 3 or4 reads with opposite R headings, or
7 reads with two R headings of each kind), and27 on odd rows (empty,
single R, or4/5 reads with opposite L headings). The exact nearest-row
count relation has676 directed edges. No history is removed for having
an inconvenient period or clock size.

## Sound local chronology obstructions

For four consecutive row classes, match every internal directed-edge
traversal to the arrival of the same ordinal. These are literal arcs of
the global event permutation, with seam voltages0,+1,-1 as previously
specified. All local event indices remain their chronological indices.

A finite internal successor segment has length L<P if its vertices are
distinct and its endpoints are distinct events in the one global period.
If it runs from event j to event j' at the same cell class and has voltage
w, the representative clock difference is L-wP. Consequently:

- if j<j', any w>0 makes the required positive difference negative;
- if j>j', any w<=0 makes the required negative difference positive.

Either witness rejects the window, without knowing P.

An internal directed successor cycle is a sealed component of the global
permutation. If any other window event lies outside it, the window is
impossible because a genuine front has only one event cycle. If it contains
all active window events, a genuine front would have to have no other
active events anywhere. Its total voltage must then be1 and all local
chronological orders must hold. The implementation explicitly checks this
exception and raises a potential-front result rather than rejecting it.
No such exception is encountered in the cap-seven certificate. Cycles of
nonpositive voltage or voltage other than1 cannot be whole front cycles.

## Finite transfer certificate and all-width bridge

A transfer node stores the parity and exact histories of the last three
rows, plus accumulated voltage modulo2. Starting from three empty rows,
append every count-compatible next history and reject exactly the four-row
windows with one of the preceding witnesses. Shift by one row and repeat.
There is no truncation on the number of rows or on an integer clock.
The stored voltage parity is unnecessary for the strongest final result,
but is preserved as a control.

The complete reachable graph has18 nodes and18 accepted edges. Only the
two all-empty boundary-parity nodes can reach an all-empty node again.
No node containing a nonempty history can do so. The101 rejected outgoing
extensions consist of70 wrong-order segments and31 sealed cycles.
Every compatible outgoing extension from every reachable node is included
in the accepted or rejected list.

Any finite-width full-drift front can be padded by three empty rows below
and above. Its successive four-row windows satisfy the necessary tests,
unless a window contains the entire valid front, which is separately
recognized rather than rejected. Hence it would yield a nonempty path
from an empty node back to an empty node. The finite graph rules this out.
This is an all-width, all-period exclusion, with an independently reconstructed
exact finite certificate, not a search horizon.

Producer: `probe_diagonal_window_transfer.py`.
Frozen summary: `diagonal_cap7_window4.json`.
Full records: `diagonal_cap7_window4.certificate.json`.
A separate three-row version also has no nonempty returning state, but its
211-node certificate is larger and is not needed for the four-row proof.

Independent audit: `audits/check_cap7_diagonal_window_independent.py/json`.
The auditor began with all510 unpruned parity histories and4,472 physical
nearest-row edges, rather than trusting the balance filter. Independent
complex-coordinate geometry, rank matching and explicit cycle clocks
recover all18 states,18 accepted edges,101 rejected extensions and the
two empty returning states.
