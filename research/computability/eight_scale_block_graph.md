# Successive-scale block graph for eventual diagonal inflation

Status: discovery-only necessary graph, 2026-10-22. It is CYCLIC, not an exclusion and not an infinite trajectory construction. No new independently audited bounded-search theorem is asserted.

The existing pure-root512-turn exclusion is in
`../causal_reduction/morphic_candidates/position_only_k8_critical_exclusion.md`.
It concerns p(8n)=(2+2i)p(n) from n=0, not an eventual affine relation.

Consider instead

    p(8n+c)=(2+2i)p(n)+b, n>=N.

For a sufficiently late t, define t_(j+1)=8t_j+c. These times tend to infinity. From j>=1 they all have the same parity, so their physical headings lie on one fixed axis. Normalize each local heading to north, using a half-turn if needed. The length8 word U_j starting at t_j has displacement in {(2,2),(2,-2),(-2,2),(-2,-2)} after normalization: it is the image of one coarse move from the previous scale.

The64-turn block starting at t_(j+1) refines U_j positionally. Subtracting the affine endpoint identities cancels b. Independent normalization at consecutive levels changes the scalar by at most a half-turn, so the scale is either +(2+2i) or -(2+2i). Its first8 letters are U_(j+1). No shifted full-orbit self-similarity is asserted.

Thus an eventual affine orbit gives an infinite path in the following finite graph. Vertices are all internally alternating8-turn words from north with diagonal displacement(±2,±2). Edge U->V means there exists an internally alternating64-turn refinement of U, with one of those two scales, whose first8 letters are V. Initial colors are unrestricted for this necessary test.

`eight_scale_block_graph.py` builds the exact finite CNF using the causal analysis's free-heading refinement encoder. Each SAT edge is then independently literally replayed within the script, including all8 positional boundary identities. Discovery output `eight_scale_block_graph.json` has:

-34 vertices;
-578 eligible source/target/scale calls;
-453 SAT edges and zero UNKNOWN results;
-many directed cycles, including12 self-loop edges.

The cycles show that THIS abstraction cannot exclude eventual affine inflation. They are not sufficient for an actual infinite path: different edge witnesses can disagree on longer overlapping blocks and on their inherited physical board. The graph also imposes no finite-black-fuel condition.

The positive-real pure-root theorem does not automatically cover the negative-real scalar. Rotating an entire trajectory conjugates neither complex scalar sign nor its argument, because complex multiplications commute. Reflection conjugates the scalar but requires complementing board colors to preserve the classical ant rule. Any use of negative-real scales therefore needs its own proof or an explicit valid reduction.

The unused `search_eight_phase_controllers.py` prototype was deliberately not run after learning of the existing pure-root exclusion. No computational result is attached to it.
