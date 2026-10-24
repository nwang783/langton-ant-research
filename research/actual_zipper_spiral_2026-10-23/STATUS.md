# Actual paired-forest spiral zipper status

The all-parameter spacing-four construction in PROOF.md independently PASSED.
Frozen proof SHA256: 47ca17aa70bbb2a01720ce86066bee05120fd5f9890fe05d278bc357ff4faae2.

It proves actual maximal ordinary erasure-free epochs of entry mass M with
mass gain at least sqrt(M)-3, retaining both full boards as forests at every
fine cut. Signed path turn is q-1 and exact first-block correction is -1.
The preceding universal signed-turn theorem is unchanged.

Independent report/checker:
/workspace/shared/langton/audits/check_actual_zipper_spiral_independent.json
/workspace/shared/langton/audits/check_actual_zipper_spiral_independent.py
The reviewer reconstructed 3,797 literal updates and 1,864 complete L cuts,
checking both graphs and the complete retained dual-chain invariant.

This is sharp one-epoch square-root growth, not a sharp global cubic renewal
construction. No repeatable concatenation or infinite finite-seed orbit is
proved. Optional alternative entry and collector variants are NOT covered
by this independent PASS and have separate files/status.
