# Chronology checkpoint, 2026-10-23 05:11 UTC

## Useful signed progress

Canonical DCUV funding-aware record coverage is **eleven of thirteen**. The new
independently signed cases are DC3, VCC0 and UCC0. Only V1 and U1 remain open.
The three use original far initialization, not first-far funding. Their frozen
far-height/k5/live-pruned certificates are in `chronology_dcuv/global_record_far_height/`:
`dc3_plus2_k5_live`, `t6h0_context_k5_live`, `t9h0_context_k5_live`.
The whole finite-seed standard-highway conjecture remains UNSOLVED, as does the
full DCUV restricted tail theorem until the final two events close.

The exact conditional quantitative assembly is independently reviewed:
`chronology_dcuv/record_conditional_quantitative_assembly.md` and
`record_conditional_constants.json`. At common activation weight I>=28, complete
13-case coverage would give R=ceil(18+(I+6)(m-5)/2),
t=floor((2R+1)^2/3), raw duration<=20R(t+1)+28t. The literal shifted prefix
maximum is14, despite unshifted absolute diagonal radius8. I48 remains only a
hypothetical final choice, not an established bound for V1/U1.

## New refinements and their exact status

- `refine_record_far_transverse_bands.py` adds finite transverse bands to the
  signed far-height graph without adding colors. Its sparse V1 control is
  independently reconstructed. Default bands are (-infinity,0], [1,8], [9,infinity).
  Full V1/U1 default-band models both cap at2m BDD nodes; these are not closures.
- The eleven signed permissions alone still allow a nonphysical geometric pump,
  even with the exact k5 factor grammar. Word [5,0,1,4,7,1,5,4] drifts(1,-1),
  with initial directional maxima[28,26,28,14]. Direct literal replay conflicts
  at rawstep191, packetindex8, cell(0,-1). Frozen negative control:
  `chronology_dcuv/oriented_record_geometry_dfa5_east_pump_replay.json`.
- Symbolic analysis froze a selective k5 DFA excluding the actual illegal factor
  [4,0,5,5,5,4]. It has137 states instead of full k6's527. Sparse14 V1 with
  first-far funding, selective DFA and transverse bands still witnesses.
- A new global resource invariant is analytically approved: globally whiten all
  initial residuals of activation>=S; then every initial residual height is
  <=F=floor((S-I-1)/2). Maintain a monotone upper bound Q on ALL residual heights.
  A packet needs every input height<=Q and updates Q to max(Q,all output heights).
  Core cells are excluded. Strict peak cuts give a finite Q range. This rejects
  the selective-DFA sparse witness at its SECOND far packet, not merely a
  missing local color. Geometry+k5+Q alone still has abstract countercontrols.
- `refine_record_global_residual_height.py` is the frozen uncompressed generator.
  Sparse14 control adds5 Q bits, range[-10,11], for19 total bits. Joint low-bin
  source/destination/input/output inequalities are enumerated exactly. Its
  history-preserving BDD engine capped; no theorem result.
- `compress_record_global_height_relations.py` exactly groups the finite Q
  relation into guarded identity or fixed-output cubes. Every binary Q truth
  table, including unused codes, is checked against the frozen relation. A
  compressed v3 backward run is active at this checkpoint. This implementation
  still needs independent reconstruction; analytical protocol alone is not a
  completed exclusion.

## Coordination and ongoing work

Symbolic analysis covers U1's counted C-age refinement and selective illegal-factor
DFAs. It also supplied independently controlled mid-layer-GC backward engines
v2/v3; v2 could thrash near its GC threshold, so use v3. Both exact statuses and
exported complement invariants passed200 local random controls. An exported
forward invariant must still pass independent verification before any claim.

Global analysis covers transverse bands and global Q. No additional colors or larger
node caps are being treated as proof. 