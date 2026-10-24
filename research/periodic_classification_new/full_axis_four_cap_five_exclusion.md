# Full axis-four cap-five exclusion

23 October 2026, 07:55 UTC. Independently signed complete replay (audit KR).

The theorem excludes every complete white-input translating front
with at most five reads per physical cell and actual full drift (+4,0), at
EVERY period and strip width. Genuine quarter rotations cover
(±4,0),(0,±4). It uses no primitive divisor or reflection.

Use exact complete local white histories, ordinal physical edge matching,
the signed processed-path connectivity, and the independently reviewed
fixed-scale adaptive strict real clock relaxation. The minimum physical
period is16 by the signed g>=8 plus paired-left displacement bound. The
clock scale stays64; the saturated number of exposed full-drift events
refines the period lower bound, and the upper normalized increment is
ceil(64/max(16,exposed_saturated_at64)). This does not cap P at64.

Each consecutive two-row window also obeys signed proper-path chronological
order. In addition, a literal successor path's first return to its exact
physical starting cell (same full-drift quotient cell, cumulative seam
zero) must hit its next complete rank. A whole-window sole voltage-one
cycle is retained as a possible front, not silently discarded.

Frozen producer: probe_axis4_first_return_adaptive_zone.py.
Core: probe_adaptive_real_zone_core.py.
Literal filter: axis4_first_return_window.py.
Certificate: axis4_first_return_adaptive_real_w2_cap5_N16_S64_M128_mod2.certificate.json.

The full reachable graph has6,624 states and7,770 accepted edges after
5,328,690 tested extensions. It has no possible-front outcome. Parameters
are local visitcap5, actual full drift(+4,0), fixedscale64, minimumP16,
clippingM128, voltage modulus2, literal window2, exposed-read saturation64.
The certificate stores every reached state, not a guessed invariant.

This strengthens the previously signed cap-four
axis-four result by one visit. It does not exclude cap six, any all-cap
axis-four front, general cap four, or the finite-black-seed conjecture.

## Simpler fixed-scale candidate, preferred for proof replay

A second COMPLETE graph uses only the already signed KD fixed-N normalized
real core, N16/M32/q2, plus the same first-return filter. It closes in
3,010 states and3,587 accepted edges after2,439,861 extensions. No adaptive
counter or new clock quantization is needed. Frozen certificate:
axis4_first_return_normalized_real_w2_cap5_N16_M32_mod2.certificate.json.
Producer: probe_axis4_first_return_real_zone.py. Pending independent replay.

## Independent complete replay

Audit KR independently rebuilt all64,311 internally matched row histories
per parity and replayed EVERY5,328,690 extension using physical complex
coordinates, independent first-return checks and infinitesimal Bellman-Ford
strict clock projection. It recovered exactly6,624states/7,770edges, with
no possible whole-front outcome. The frozen adaptive certificate SHA256 is
0574ff0581e24798e8f5c308fa096b6da6733a8beeb5afb55a028faa04033f60.
The smaller fixed-real graph is an author simplification, not needed for
the validity of the independently replayed theorem.
