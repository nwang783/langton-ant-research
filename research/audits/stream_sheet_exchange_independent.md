# Independent review: cap-four sheet exchange and chronological bridge signs

Reviewed 2026-10-23 16:33 UTC. Exact scoped PASS, not a resource bound.

Bound notes:
- chronological_stream_sheet_exchange.md: fd20e425b8a6bbc3aefd5eca06b4d443c1d2bdfde5f1d2d69c25d5c4d62af484
- stream_sheet_clocks_and_bridge_sign.md: 552d5aa8cc604cb3899291d688f016652fcd00ab6108e24eb44efa86ea9efe84

The independent local checker solves the four face-difference equations from the incoming/outgoing edge counts, rather than assuming the author's R-count formula. It covers all 30 complete WHITE histories with at most four reads in one incoming checker axis; rotation supplies the other axis. Chronological occurrence labels are C height minus ordinal plus one. At a two-R cell, interchanging the outgoing successors of L1 and R2 preserves each label, and their levels differ by exactly one. All remaining successors already preserve label. The repaired local arcs are ordinary turns; when a level has two arcs, both are R or both L, so disjoint corner roundings exist. No intersection or primitive-winding assertion is made for the unrepaired mixed-rank paths.

Globally, each repaired permutation cycle has a fixed label. The graph joining cycles by exchanged outgoing pairs has no loops. If it were disconnected, a union of its node-cycles would be invariant under both the repaired permutation and every exchange transposition, hence under the actual successor. This contradicts the single actual P-cycle. Comparing permutation signs gives N2=C-1 modulo two, so its connected cycle excess is even. Threshold flow has exterior jump one only on j=c_right. All top maximum-face ports are positive by the already signed face-positivity theorem; that premise, not an unrestricted local assertion, supplies the four-edge top cycles.

For a repaired transition, actual departure-time increments are 1+Delta for incoming L1 to outgoing R2 and 1-Delta for the reverse exchange. Summing them around a lifted repaired cycle gives kP=ell+sum signed Delta. In particular, the actual physical return span Delta must not be replaced by its residue modulo P.

Cut only one exchange from the actual P-cycle. If Delta=mP+r, 0<r<P, the outgoing-L1 side follows r actual steps and closes at the spatial translate -m*d; the other side has P-r steps and winding 1+m. Delta cannot be a positive multiple of P, because that would place the same physical cell at a nonzero translate. These cut cycles need not be embedded. If the exchange is a graph bridge, all other transpositions stay within the two graph components, so those components have exactly the two cut-cycle supports and these total windings. Applying the same permutation parity argument inside each component gives even excess separately. A top-sheet four-edge leaf has winding zero, must be the outgoing-L1 side, and therefore has m=0, r=4, Delta=4.

The graph may have unbounded even excess; zero-homology sheets may contain oppositely winding essential cycles. Neither observation is a paid fuel, finite-root, or global capture statement.
