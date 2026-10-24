# Checker parity halves the safe rail-defect multiplicity

23 October 2026. This is a conditional arithmetic sharpening of the rail capacity 63ee2ab8. It adds no new source interface or disjointness claim. The core rail capacity must be independently signed before this sharpening is promoted.

The actual FULL period P returns the incoming heading. Since every turn is a quarter turn, P is even. The displacement therefore satisfies d_x + d_y even. Hence checker parity is well defined for physical cell classes modulo the actual full drift.

All stopping D faces belong to the same C checker-face lattice. In the normalization used in the rail proof their lower-left face indices have even coordinate sum. The twenty affine physical-cell offsets listed in 63ee2ab8 split into exactly ten even-sum and ten odd-sum offsets.

Fix an odd-output cell class [v]. For a candidate stopping C face [D] with v = D + s modulo full drift, s must have the parity of v. Thus only ten of the twenty offsets can give a C-face candidate. Because clean rails have distinct stopping D classes, this odd cell can be selected for at most ten odd stops, not twenty. In a normalization with the other C-face parity, the opposite ten offsets are selected; the count is unchanged.

The U-stop count remains at most |U|. Consequently the strengthened bound is

    H <= 10 N_odd + |U|
      <= 11 N_odd - n_Sanc.

In particular H <= 11 N_odd without the optional family. The same exact initial interface, aggregate-output scope and non-additivity caveats apply. This is not an original-fuel budget or an assertion that an arbitrary branch is an H source.

The affine offsets are rotations about the physical face center (1/2,1/2), not rotations of cell coordinates about a primal vertex. Their twenty-entry union is independently specified in half_turn_rail_defect_offsets.json. No primitive period is used.
