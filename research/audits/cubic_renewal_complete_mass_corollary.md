# Complete-board mass corollary of the signed cubic renewal theorem

Independent analytic addendum, 23 October 2026, 22:57 UTC.

Dependencies: geometric proof `simple_path_turning_2026-10-23/PROOF.md`, SHA 8647be7a9158e11985f60a7643c64411d0cd396e73449ed02032c084f7e7303f; application `global_renewal_archive_2026-10-23/cubic_global_w_renewal.md`, SHA 9bcf5c2a045fcedb1a5d6d7182df5bdb75ddc2d7a71f03fac2374019bda2eb16; independent application report `check_cubic_global_renewal_independent.json`, SHA ba23ee0891c4ae1c07134ef04212fd197e9ce7ae8a0c4830190eab0f1a21290d.

For an arbitrary actual finite-support interval starting with complete black mass m, let E count the signed w-exceptional complete blocks through the interval end, and let m_T be the COMPLETE mass there. The last epoch starts with M_E <= (sqrt(m)+4E)^2. Its completed ordinary blocks add at most 8sqrt(M_E)+3. Its unfinished R-only fringe adds at most four. Therefore

    m_T <= M_E + 8sqrt(M_E) + 7
        <= (sqrt(m)+4E+4)^2 - 9.

The same bound applies at each earlier time using its own completed-block count. In particular the maximum complete mass up to a time with E exceptional blocks is bounded by the same expression. All remote/passive cells are included. Together with the signed time bound,

    T <= 16(E+sqrt(m)/4+1)^3,

this gives quadratic complete-mass growth and cubic elapsed-time growth in the number of actual archive renewals. Since E <= D, the weaker replacements with D (actual cycle-erasing L updates counted once) also hold.

These are growth bounds, not monotone mass descent, a bound on E, a nonstandard-defect budget, an initial-position-free capture time, or standard-highway classification. No statement that mass diverges follows.
