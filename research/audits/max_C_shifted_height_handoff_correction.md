# Correction to the rank-two structural handoff

23 October 2026, 12:28 UTC. The frozen 12:24 handoff says that at the global C maximum M, adjacent **shifted** L heights are at most M-1. That word is incorrect. The exact signed consequence is

    max_C h = max_all H = M,
    H(L) <= M,
    h(L) = H(L)-1 <= M-1.

The equality of maxima follows from the independently signed global-H unique-maximum-corner theorem: such a corner is necessarily clockwise C. Thus it is the UNSHIFTED L height that is bounded by M-1. Singleton-R and other local contacts with shifted H(L)=M are permitted. The boundary flow h(C)-h(L)>=1 and activity of maximum-C corners remain valid. The signed cap_four_top_plateau_essential.md uses the correct combined-H maximum and also proves activity directly by excluding the empty-corner case H(L)=M+1.

No signed exclusion or clock certificate uses the incorrect strict shifted inequality. The handoff and open rank-two target note are research guidance, not a new theorem. Keep all source-L rank1/3 suppliers; do not remove shifted-equality cases. Frozen historical files are preserved unchanged.
