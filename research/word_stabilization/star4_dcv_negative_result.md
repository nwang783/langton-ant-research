# Complete dual-star refinement: negative result

A targeted four-cell inference was tested on the D/C/V maximal-C-run packet language. The four tracked physical cells form a2x2 square, hence a complete dual-vertex star. It retains all16 star-color states and exact raw-macro partial transitions, excluding reader poses only by strict smaller-gap pairs. This is the same sound finite-color rule with four rather than two cells; no finite-radius exterior assumption is made.

The resulting closure is exactly the old two-cell closure:7,392 candidate pairs,71 short types,3,873 surviving clauses after21 rounds. Every final row is an ordinary neighbor or odd-reader clause; no new four-cell certificate survives. The only fresh marks belong to the exceptional initial DCCC packet and therefore do not exclude an infinite recurrent D/C/V tail.

Files:generic_star4_spatial_kernel.cpp and seven_sub_dcv_star4_kernel.*. This is a precise negative result for this abstraction, not a physical counterexample. Further enlarging the same patch without new global information is not currently justified.
