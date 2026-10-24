# The signed-cut arrays recover the incoming edge

This is an elementary consequence of the previously audited signed-column invariant, not a new conserved quantity. It clarifies the domain of the rank obstructions. The analytic reconstruction was independently checked by the auditor on2026-10-22 at20:23 UTC.

Use chi(x,y)=(-1)^(x+y). For each integer column j, subtract the current checker-signed black column sum from the conserved mod4 column charge, obtaining the pose correction C_j. The formulas in ../first_principles_2026-10-21/ant_rethink/constructive_alternatives/signed_cut_and_explicit_mass_bound.md give

    C_j=2 for j<x,
    C_j=0 for j>x,
    C_x=-chi for h=N, 0 for h=E, chi for h=S, 2 for h=W.

For the row array D_j, rotate the whole pose clockwise once, replacing(x,y,h) by(y,-x,h+1), and use the same formula. Thus

    D_j=2 for j<y,
    D_j=0 for j>y,
    D_y=0 for h=N, chi for h=E, 2 for h=S, -chi for h=W.

If the incoming edge is vertical, C has exactly one odd entry, which identifies its column. D has a single2-to0 step, which identifies the half-integer vertical midpoint. If the incoming edge is horizontal, D has the unique odd entry identifying its row, and the step in C identifies its horizontal midpoint. Therefore the two arrays uniquely determine the unoriented incoming edge.

The two possible oriented poses on that edge are X and I(X). They have identical correction arrays; direct substitution also verifies this. They have opposite invariant sectors. Consequently the current board, the conserved charge arrays, and the sector uniquely determine the full pose.

A useful corollary is that the black board cannot repeat along a finite-seed forward orbit. Equal boards at two times give equal correction arrays, hence the same incoming unoriented edge. Sector preservation forces the same orientation and therefore the identical full state. Determinism would produce a bounded full-state cycle, forbidden by the ant's unboundedness theorem. This is an injectivity statement along one orbit, not a well-foundedness theorem for K renewals.

In particular, a seed-dependent function on boards inside one fixed charge/sector class can encode an arbitrary function of full states. Calling such a function board-only does not remove the directed-pose dependence. The universal board-only rank obstruction concerns one function required to work across all finite states of a sector, not a separately chosen function for each invariant orbit.
