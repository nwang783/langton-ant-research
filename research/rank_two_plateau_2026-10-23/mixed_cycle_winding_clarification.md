# Mixed paired-R cycle winding qualification

23 October 2026, 12:54 UTC. Clarification requested by the independent
auditor; the original frozen main note remains unchanged.

A homogeneous R2 dependency cycle has one node per physical class, is
embedded, and has actual-edge winding exactly1. Its exact identity is
P=ell+4Q, as stated in Section3 of second_R_gate_or_corridor.md.

A cycle of the FULL paired-R graph may instead contain both R0 and R2
at one physical class. Its physical projection need not be simple.
Strict paired-R chronology guarantees POSITIVE INTEGER actual winding k,
not k=1. Its exact telescoping identity is

    k*P=ell+4Q.

The strengthened same-face-gate q>=4 can be used within Q in this identity.
It does not license replacing kP with P, and it does not license adding
costs over separate paths without a disjoint charge. The homogeneous R2
cycles used in the conditional A/B/C subtraction are unaffected.
