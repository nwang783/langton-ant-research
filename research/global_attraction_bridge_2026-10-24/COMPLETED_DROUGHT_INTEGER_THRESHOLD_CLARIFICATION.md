# Integer threshold scope clarification

24 October 2026. This addendum narrows one convention in the frozen completed-drought projection proof, without changing its event lists or family counts.

In Section 2's coarse finite-template bound, H is a NONNEGATIVE INTEGER, with H at least every repeated period and the tail period. Since durations are integers, each gap >H then occupies at least H+1 updates, which justifies the denominator H+1. For a real threshold H, that denominator would instead be floor(H)+1. The exact indicator formulas for the named families are unchanged.

This addendum is mandatory with COMPLETED_DROUGHT_COUNTS_MANIFEST.json (6ef8a4682c7e9f6908b9653385c58d366d630d6153af2432b17ecd4962826a17). Independent report check_completed_drought_counts_independent.json (16afbb301276f7ef6bf6e67eab7f6e7cd1ab47b2bea270fc081c67e341e9ee67) explicitly checks the integer convention.
