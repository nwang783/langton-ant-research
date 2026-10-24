# When a smaller spatial quotient is actually justified

23 October 2026, 05:08 UTC. Independently signed elementary reduction (audit JI).

A supplied full drift must not be silently replaced by its primitive
direction. There is, however, an exact sufficient condition for reduction.
Suppose a complete white translating front has full period P and drift
 d=k*e, with k a positive integer. Assume translation by e preserves the
ENTIRE ordered incoming-heading history at every physical cell, including
its length; equality of mere counts or final colors is insufficient.
Then the front itself has period P/k and drift e. In particular k divides P.

Proof. A physical event is the pair (cell, its local read rank). Every
actual event has exactly one successor, determined by its outgoing heading
and the matched ordinal on the physical directed edge. Translation by e
preserves all local event data and all these ordinal matchings. Thus it
commutes with the physical successor map. The complete front's physical
events form one bi-infinite successor orbit; no event is repeated, because
its cell and local rank fix its unique read time. Translation by e must
therefore shift this orbit by a single integer T, independent of event.
Its kth power is translation by d, whose time shift is P. Hence k*T=P,
so T=P/k is a positive integer. Headings and turns are preserved too.

This is a condition, not a universal reduction. Applying it to full axis
(4,0), the signed unit-axis exclusion shows that at least one complete
cell history must differ from the history two cells horizontally away.
Similarly a front at full diagonal (2,2) must break translation symmetry
by (1,1), because the full-unit-diagonal theorem excludes that smaller drift.
Neither conclusion bounds how many classes must break the symmetry.
