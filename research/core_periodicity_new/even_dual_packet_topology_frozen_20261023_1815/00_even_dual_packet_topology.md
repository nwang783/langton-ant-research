# Literal even-dual packet topology

23 October 2026, 18:15 UTC. This is a local topology table, not a historical
incidence embedding or a new U-component theorem.

Use the independently signed active-center even dual: physical cells are
diagonal edges of one half-integer checkerboard lattice. Work in the
normalized sector zero and scale vertices by two, so a cell (x,y) is the edge

    (2x,2y) +/- (1,1)   if x+y is even,
    (2x,2y) +/- (1,-1)  if x+y is odd.

Translation and quarter rotation carry this table to every actual sector and
marked pose. Directly from the literal input and output masks:

* Every full-packet input edge set is a tree. The D-family input has one
  edge, the V-family input has two, and the U-family input has five.
* Every genuine full-packet output edge set is connected.
* D, DC, V, VC and VCC output edge sets are trees.
* U, UC and UCC output edge sets are unicyclic. In all three cases their
  unique cycle consists of the physical cells

      (1,0), (1,1), (2,0), (2,1).

The output (vertex, edge) counts in packet order D, DC, V, VC, VCC, U, UC,
UCC are (2,1), (5,4), (7,6), (10,9), (13,12), (9,9), (12,12), (15,15).
The attached C tails add trees to these local output graphs without adding
another output cycle. The checker also records, but does not interpret as a
global invariant, the before and after local graphs with the actual K5 core.

## Why this does not close the component question

The graph in this table is the CURRENT occupied-edge graph, not the
historical all-input incidence graph. Distinct initial residual identities
are distinct incidence roots even if their physical edges already meet.
Conversely, later input retirement can disconnect the live edge archive of
one historical component. The signed split-archive example does exactly
that. Joining pieces by all K5 edges also fails as an inductive predicate:
the artificial equal-color opposite-leaf D example loses its core connection
without either residual edge being touched.

Thus connected output graphs are a legitimate local ingredient for a
core-port construction, but they do not provide such a construction. In
particular, a U output cycle is not proved permanent, a scarce initial-root
resource, or a new incidence cycle. No component-merger or U-count bound is
claimed here. A successful invariant still needs the history of the courier
ports, including how a connector passes around the factor-entry endpoint
versus the current center path.

Reproduction: run check_even_dual_packet_topology.py. It computes connected
components, Euler cycle ranks and leaf-pruned cycle edges from the literal
masks, rather than hard-coding edges. Its expected topology is checked
against the finite table stated above.
