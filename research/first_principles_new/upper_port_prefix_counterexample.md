# Upper two-row port abstraction is too weak

22 October 2026. Exact literal counterexample, not a renewable cap.

Start at (2,3,N) on a completely white board and run RRRRLRRRRLRRRR. Every read is legal. The final pose is (1,2,S); row3 is black exactly at 0,1,2,3 and row4 exactly at 1,2. Both negative half-rows remain white. Thus the first row3 white site is r=4, whereas the first row4 black site is s=1. Both proposed endpoint implications r<=s and A_s=0 fail.

As an upper-two-row interactive subsystem, the successive north entries are at x=2,2,0. The corresponding upper words are RR, LRRRRL, RR. The lower bridges are each RR in row2, so these ports even admit a single legal physical realization with initially white lower cells. No upper read escapes above row4.

This disproves an invariant based solely on arbitrary bottom-port interactions and clean negative upper half-rows. It does NOT disprove the mixed-shuttle cap conjecture: the prescribed cap entry/return pose and outgoing W20 guard are absent. Any proof of that conjecture must use these additional chronological obligations. The literal read certificate is upper_port_prefix_counterexample.json.
