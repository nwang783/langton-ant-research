# Stage 4: signed clocked sheet coupling and exact old-stock escapes

23 October 2026, 16:57 UTC. This is an addendum to the frozen stage-3
handoff, not an edit of any earlier signed theorem.

## Independently approved since stage 3

- Chronological sheet exchange and connected cycle graph:
  chronological_stream_sheet_exchange.md, SHA
  fd20e425b8a6bbc3aefd5eca06b4d443c1d2bdfde5f1d2d69c25d5c4d62af484.
  R0/L3 preserve level, L1/R2 exchange adjacent levels. The repair gives
  connected adjacent-sheet graph with N2-C+1 nonnegative even.

- Exact cycle clocks and bridge signs:
  stream_sheet_clocks_and_bridge_sign.md, SHA
  552d5aa8cc604cb3899291d688f016652fcd00ab6108e24eb44efa86ea9efe84.
  Delta may exceed P. Cut windings are -floor(Delta/P) and its complement
  1+floor(Delta/P). A top-sheet leaf forces Delta=4.

- Boundary-aware side cut:
  K1_boundary_crossing_and_side_cycle_cut.md, SHA
  89ad6e574dd58f886596ce49769bb0e1cbc5f3d3d5887741e1bef17c1386864f.
  The separate R0/R2 cut gives one RIGHT -1 cycle and gcd(ell,2) LEFT
  cycles of winding 2/gcd(ell,2). A naive interleaving crossing count is
  already met by the selected boundary L1/R2 pair and forces no new
  deep supplier.

- Causal sheet label of old L3 stock:
  L3_stock_sheet_monotonicity.md, SHA
  83c184749163db0e059562ef69c2cf392c1d580a7dbdafdc9170968d66c15cce.
  If the exchange is s,s+1, L3 is s for opposite L1/L3 headings, and
  s-1 for same headings. Equality is exactly retained in BOTH row-5
  nearby-return fuel cells. Selected LEFT/RIGHT L3 are c_left/c_right.

- Necessary topology of a row-5 renewal:
  row5_renewal_requires_sheet_topology.md, SHA
  8c01ff7d31c79c3a66fe336e402a5896dce9c87f922672bd0a9a430af6850ea9.
  Its downward middle-to-lower exchange forces nonzero even graph
  excess, another middle-sheet node, OR a positive essential lower-sheet
  cycle with a compensating negative same-sheet cycle. Several renewal
  sites may share this SAME geometry: there is no additive charge.

The independent reconstruction of the sheet interface is in
/workspace/shared/langton/audits/check_stream_sheet_exchange_independent.py/json.
All other scopes and the approved leftmost branch-or-straight theorem
remain as in stage3_handoff_1631.md. No K>=2 result is claimed.

## Exact prepared countercontrol, data not independently replayed

prepared_W20_sheet_star_control.md, SHA
9e7a9aa90116a8643937575fc91ef88ab2c2b4b870280eafaf87714aef6cc730,
with py/json, projects the THREE EXISTING prescribed W20 profiles only.
It gives a zero-excess star with one middle +1 node and four-edge leaves.
Half the lower leaves are actual all-white old-L3 cleanup, while half
contain two explicit singleton-black-L fuel reads. Their graph signatures
coincide. The abstract one-root star exclusion under row-5 renewal is
independently approved; this prepared profile projection itself was not
separately replayed by the auditor. It is NOT a white front.

## New geometric classification awaiting review

penultimate_max_adjacent_contour_orientation.md, SHA
a2170bdce45e58734901f1ebb215f7ac5f7b58ab26deafe2cac8567a3133ec22.
A sheet M-1 cycle with an adjacent right max C face is essential or, if
contractible, counterclockwise around a LOW stock hole. The proposed
proof uses the exact penultimate smoothing at max/max contacts, which
joins the high C sectors. It does not import the top-sheet smoothing.
Only the max-adjacent node is classified, not every new middle node.
No fresh root, fuel budget or complete white connector follows.

## Remaining structural target

The leftmost K=1 component still allows actual LEFT max birth trees and
strict straight gates. The signed row-5 supplier can close the apparent
fuel deficit locally using OLD L3. The clocked sheet graph now specifies
what additional canonical topology that renewal must carry. A new
contractible middle cycle may be a stock-hole escape, not a fresh max
component. Its causal R0/R2 supplier history, with equality sheet steps,
is the concrete unresolved class. Zero homology, graph excess and leaf
count alone are NOT resource bounds.
