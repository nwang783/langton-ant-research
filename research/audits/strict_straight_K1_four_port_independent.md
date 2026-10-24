# Independent review: strict straight K=1 four-port obstruction

23 October 2026, 14:20 UTC. PASS, with the exact extra hypotheses retained.

Reviewed note SHA256 f49f6899774e5de77928fdbb8cc6a332f77c123ea330cbfaabfd097891e9a5f1. Its prerequisite strict_straight_K1_port_reduction.md has SHA256 bb74260a83605e83ea2267e45aa3daac6cbaa07992d392dfbdaa965487a710fc. The latter's Sections1–3 are analytically verified independently of its optional short-factor enumeration.

The prerequisite uses a complete WHITE cap-four translating front, actual full drift, K=1, straight selected contacts v_i=(-i,i), and EVERY immediate LEFT C neighbor strictly below the global maximum M. Ordinal matching forces v incoming N,N,S,N and z incoming W,W,W,E, both full RLRL histories. In particular h(G_i)=M-2. The key chronology check is that an E arrival for z's L1 would feed v_i's L1 before the signed preceding right excursion ends, impossible. Its alternative W arrival forces the third W supplier at v_(i-1), hence L3; this L3 is not silently discarded. The resulting deep q_i history is R(S),L(N),R(N), optional L(N), with later q ports not yet visited during D_i.

The new proof uses only that unbounded reduction. Both q_i west departures R0 and L1 occur before q_(i+1)'s first visit. The recipient u_i cannot turn R on either W arrival, because that would enter q_(i+1). They are therefore exactly L1 and L3. Its interleaved R0 and R2 cannot arrive W either: each would be an additional earlier west arrival, while the first two west arrivals have already been identified as the two L reads. Thus u_i has incoming E,W,E,W, all four departures S.

Its two R reads choose H_i rather than G_i, forcing H_i=M. The south recipient b_i has four S arrivals and hence exactly those four reads by cap four. Its two R reads choose NW H_i, requiring h(H_i)-h(H_(i-1))=2. Direct coordinates show that its other SE face is precisely H_(i-1), which also equals M. Contradiction.

No bounded word length, period, radius, prepared-color argument or loop deletion enters this final proof. Independent short-factor controls in check_strict_K1_deep_ports_independent.py/json remain valid but are unnecessary. No claim excludes bent selected curves, K>1 or equal-M LEFT neighbors. This is not a general cap-four or finite-seed capture theorem.
