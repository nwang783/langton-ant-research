# Exact white-edge boundary dynamics

Status: fresh exploration. The representation and permutation identities below are direct algebra. No attraction or transience conclusion is asserted.

Fix the heading/checkerboard sector and identify the appropriate checkerboard family of face centers with the ordinary square dual lattice. If the physical ant is at p with forward vector f and right vector r, its active dual vertex is v=p-(f+r)/2. The physical cell p is the dual bond {v,w}, where w=p+(f+r)/2. White cells are present edges; black cells are absent edges.

- Reading white (R) deletes the tested edge and crosses from v to w.
- Reading black (L) inserts the tested edge and remains at v.
- The next tested dart is the counterclockwise successor of the current dart after L, or of the reverse arrival dart after R.

This is exact for arbitrary fields and does not use any symbolic-language hypothesis. A finite black field gives a cofinite present-edge graph with one infinite component and finitely many finite components.

Let D be all oriented dual darts, alpha reverse a dart, and sigma rotate it counterclockwise at its tail. For a present-edge graph G, let alpha_G act as alpha on present edges and as the identity on absent edges. The ribbon-boundary permutation is

    P_G = sigma o alpha_G.

The dynamics from dart d is

    d_next = P_G(d),
    P_G_next = P_G o (d alpha(d)).

Thus each update switches the two successor arrows at the tested edge. If d and alpha(d) lie in different boundary cycles, those cycles merge. If they lie in the same cycle, it splits, and the new active cycle is the one containing alpha(d), while the cycle containing the old d is detached. The latter follows by writing the old cycle as d -> A -> alpha(d) -> B -> d: after the switch the two cycles are d -> B -> d and alpha(d) -> A -> alpha(d), and the head advances to the first dart of A.

Because G differs from the full square lattice in finitely many edges, every boundary cycle is finite. The graph itself has an infinite component, but its ribbon boundary has only finite cycles. Therefore the entire question can be restated as the deterministic growth, splitting, and merging of one marked finite boundary cycle, interacting with initially elementary four-dart cycles and finitely many defects.

This reformulation by itself is not a finite-state reduction: the marked cycle may grow without bound, and previously detached cycles may later rejoin. A correct proof must control that reattachment, rather than silently treating detached cycles as frozen.

## Provenance and tested obstructions

The medial boundary-loop formulation itself is not new: Atharva Jillhewar's 2026 primary preprint, *Finite-Support Periodic Highways of Langton's Ant*, Section 4, states the same conjugacy and split/merge surgery in the complementary finite black-edge Tait graph. The explicit marked successor convention above is independently derived, but must not be advertised as a new attraction theorem. Source: https://doi.org/10.21203/rs.3.rs-10516269/v1 .

The following easy-looking stronger assertions are false, with literal blank-input counterexamples saved by the independent dual simulator:

1. Finite white components need not be trees. At time 1200 there is a four-vertex, four-edge white component with dual vertices (6,1),(6,2),(7,1),(7,2). Its cycle rank is one. See `component_probe.py/json`.
2. The active finite black Tait component need not be a tree or unicyclic. At time 140 its cycle rank is already three; at time 9430 the active component has 472 vertices, 533 edges, and rank 62. See `active_black_probe.py/json`.
3. A unit-size or small fixed cutoff on the instantaneous active boundary is not justified by the initial support alone. The blank orbit's active boundary at time 10000 has 136 darts, and another explicitly saved finite seed has 1672 darts at that time. These examples do not refute the existence of some unknown support-dependent bound; they refute the naive unit-loop reduction. A useful eventual bound still needs a theorem.

These checks are used only to refute the stated invariants, not as evidence for the full conjecture. They preserve every white/black edge and compute complete components/cycles at the indicated finite times.
