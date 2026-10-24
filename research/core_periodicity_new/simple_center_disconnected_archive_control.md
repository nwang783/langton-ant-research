# A simple center history can have split live component archives and enter their hull

23 October 2026 16:43 UTC. Actual finite-board scope control; independent
replay requested. No search completeness or minimal-mass claim.

The word UCC,V,V,V,VCC,V,V is physically legal from nineteen initial black
cells, with all other cells white, initial head(0,0,N):

    (-5,-6),(-4,-7),(-4,-3),(-3,-6),(-3,-4),(-3,0),
    (-2,-3),(-2,-1),(-2,3),(-1,-1),(-1,0),(-1,1),
    (-1,2),(-1,4),(0,-1),(0,0),(0,2),(0,3),(1,0).

Direct replay verifies196 raw turns and the actual following M11. Raw exit
is(-2,-2,N), with59 black cells,54 residual identities and four C atoms.
All initial fourteen residual roots are present in the incidence graph.
Its rank is ZERO, with four final historical components.

The corrected-center path has eleven actual chords. Exact tests of all55
closed segment pairs give only the ten adjacent common endpoints; all45
nonadjacent pairs are disjoint. It is a SIMPLE path.

Nevertheless one historical component has exactly two8-connected pieces
of CURRENT live residual cells:

    {(-5,-3),(-5,-2),(-5,-1),(-4,-1),(-3,-1)}
    {(-3,-5),(-3,-4),(-2,-5),(-1,-5),(-1,-4),(-1,-3)}.

The third V at(-3,-1,S) initially produced the first archive and its bridge
identity(-3,-2). The final V at(-3,-5,N), clock four, consumes that bridge
identity at age two plus a new entry root, and installs its new six outputs.
The five dormant original outputs remain in the old archive. Thus removing
one true input can disconnect a historical component's live support even
on a simple center history. Historical connectivity is not current spatial
connectivity; ghost wires cannot simply be discarded by declaration.

There is also an exact convex-hull limitation, observed by the chronology
analysis. The final corrected center is(-5/2,-5/2). All three points
A=(-5,-1), B=(-3,-1), C=(-1,-5) belong to this SAME live component, and

    center = (1/8)A + (1/2)B + (3/8)C.

All coefficients are positive and the triangle is nondegenerate. Hence a
simple center can lie STRICTLY INSIDE one current component's convex hull.
This rules out a naive current-connectivity or hull-separation invariant.
It does not refute the targeted U-multicomponent lemma: this word's only
U-family packet is the first UCC, which consumes five distinct entry roots.
There is no later U, renewal, infinite trajectory or rank-budget claim.

The checker directly reconstructs the first-L seed, fine-step board, every
ordered remove/install identity and component update, all three actual
produced-input HB/count clauses, all eleven raw atomic cuts and all55 exact
segment pairs. Discovery search is not a proof dependency.

Checker: check_simple_center_disconnected_archive_control.py.
Data: chronology_dcuv/simple_center_disconnected_archive_control.json.
