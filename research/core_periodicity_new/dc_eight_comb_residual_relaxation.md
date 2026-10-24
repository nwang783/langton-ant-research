# Eight residual DC combs: packing is not the full packet ledger

2026-10-23 09:12 UTC. This is an explicit countermodel to a WEAKER residual-rewrite packing abstraction. It is not a physical ant path, not a full five-cell-core ledger, and not a noncapture construction.

Let one abstract C clock tick per event. There are eight initial residual identities. For root r in{0,...,7}, put h_r=−r modulo4 and ell=floor(r/4). In heading-normalized coordinates choose

P_(r,0)=(100,100+epsilon_h+10ell), epsilon_h=(1−h) modulo2,

then rotate by h_r in the physical plane. Root r is updated only at clocks r+8j. Its continuing spine points are

P_(r,j)=P_(r,0)+Rot_h(3j,j).

At that event consume the one identity at P_(r,j), and install the four literal DC residual outputs relative to its input:

Rot_h(2,−1), Rot_h(2,2), Rot_h(3,0), Rot_h(3,1).

The last is P_(r,j+1), the next spine identity; the other three remain dormant buds. The implied DC source head is P_(r,j)−Rot_h(0,1).

## What the relaxation satisfies exactly

- Every event uses the actual DC one-input/four-output residual rewrite, so current residual mass is8+3k after k events.
- Every produced parent on a spine has source-start C age8. Initial identities are exempt.
- The implied source heading is h=−clock modulo4, exactly the recurrent-eight heading rule. The head sector x+y+h is fixed even: the chosen parity epsilon_h and the even-sum spine advance(3,1) ensure it. Choosing the superficially simpler spine advance(3,0) would FAIL this sector test and is not used.
- All residual cells are distinct. In one normalized comb, spine x coordinates are0 modulo3, while two bud families have x=2 modulo3. The third bud family shares x=0 modulo3 but differs from the next spine in y. Equal-x comparison separates all times. The two parallel roots of one heading have normalized y shift10, larger than every possible equal-x bud offset difference. The four heading classes lie in disjoint outward quadrants.
- Parent-child L-infinity distances are at most3, and each root's spine is monotone. The radius from its initial root is at most3*floor(k/8)+3, so it respects a positive linear speed bound stronger than LB's2/3.
- The repeated spine transfer DC output(3,2) -> DC input(0,1), same heading, C age8, is unexcluded by the signed marginal role graph. The exactage4 hole is respected. No forbidden LH VCC→D→VC history is used.

These facts show that finite roots,+3 mass per C, ages>=5, bounded local residual rewrites, marginal producer-role constraints and collision-free residual packing do not ALONE force a finite budget.

## Precisely where physical packet structure is missing

The unique live cursor does not jump to the scheduled next root. The imposed DC endpoint is not the next scheduled source pose; the discrepancy grows linearly with the comb generation. Inserting real intervening packets is a new problem, not an allowed silent transport.

More locally, even two successive updates of ONE comb cannot simply inherit the complete DC context. The next same-heading DC head is shifted by(3,1) in source coordinates. Two old source outputs then occupy its required OLD CORE:

source output(3,1) -> target core offset(0,0),
source output(2,0) -> target core offset(−1,−1).

Both are still dormant residual identities in this relaxed construction. The exact signed ledger requires residual identities disjoint from the five-cell core, so these identities would have to be genuinely consumed/retired by intervening packets. They cannot be silently relabeled as core or discarded. The other dormant output(2,3) is at target offset(−1,2), outside that core.

Thus the construction intentionally fails core transport and mandatory sibling clearance, before claiming any complete white-context realization. These are real coupling conditions to investigate. No theorem that includes them is refuted. Dormant buds are all retained; their failure is not hidden by deleting unused branches.
