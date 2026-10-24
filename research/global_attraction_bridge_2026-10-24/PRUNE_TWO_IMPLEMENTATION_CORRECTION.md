# Prune2 implementation correction before independent signoff

24 October 2026. The mathematical argument in RELEVANT_PRUNING_COMPUTABILITY_INTERFACE.md is unchanged. The initially frozen implementation296bd654 was not independently signed.

Its candidate search unnecessarily asserted that a freshly certified future104 word equals the104 word recently observed in the past. A past canonical word segment does not by itself license that phase equality across a possible interruption boundary. Although the six supplied controls did not exercise this assertion, it was not a justified total-algorithm obligation.

The separate immutable v2 implementation accepts the ACTUAL freshly certified future word when it is a cyclic canonical phase, then constructs its actual read rays. The past repetition is only a candidate filter. Acceptance still requires full-field infinite parity, and eventual capture of every at-most-two-black comparison ensures the filter eventually reaches a valid tail. No claim about the full arbitrary input's capture is introduced.

prune_two_original_inputs_v2.py and check_prune_two_original_inputs_v2.py supersede the v1 executable for the total-interface claim. The fresh v2 controls reproduce the same six original-input outcomes, sparse-radius answers and exact no-hit tests. The frozen v1 files remain unchanged for provenance.
