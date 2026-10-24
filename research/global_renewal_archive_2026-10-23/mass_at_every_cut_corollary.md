# Full mass at every actual prefix cut

Immediate deduction from independently signed cubic_global_w_renewal.md
(9bcf5c2a),23 October2026. No new external or finite-search premise.

On an arbitrary actual interval with entry mass m, let E_t count its completed
exceptional blocks by time t. Let b_t denote the COMPLETE current black mass,
including every passive component, unread cap and earlier write. Then

    b_t <= (sqrt(m)+4(E_t+1))^2.

Indeed at the final ordinary epoch entry, the signed recurrence gives
M_E<=(sqrt(m)+4E_t)^2. Its completed ordinary blocks raise mass by at most
8sqrt(M_E)+3, and its terminal R-only prefix by at most4. Hence

    b_t<=M_E+8sqrt(M_E)+7
       <=(sqrt(M_E)+4)^2
       <=(sqrt(m)+4(E_t+1))^2.

The same weaker bound follows with the total dual cycle-erasure count D_t
because E_t<=D_t. This is a quadratic complete-board growth bound in the
actual renewal clock, not mass descent and not an original-mass upper budget
on renewals. It does not distinguish standard from nonstandard renewals.
