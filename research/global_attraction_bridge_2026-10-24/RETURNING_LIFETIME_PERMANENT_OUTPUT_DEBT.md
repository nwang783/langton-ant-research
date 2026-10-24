# Large returning lifetimes require live spatial stock or irreversible output

24 October 2026. AUTHOR analytic application of the retained axial transport charge, with complete finite/infinite controls; independent audit requested. The charge itself and the bounded-age-to-translation theorem are retained premises, not new results. No eventual boundedness hypothesis is asserted for arbitrary seeds.

## 1. Definitions and the two-leg inequality

Work with the COMPLETE actual finite board B_t at every pre-update cut. Let C*(t) be its black lifetimes that will eventually be consumed, and write L_t=|C*(t)|. A permanent R birth means a specific lifetime born by R whose cell is never read again in this actual future. It is not an output predicted to escape by comparison with a different board.

Fix a genuinely R-born lifetime at cell q, born at update b and next read, black, at update d. Put a=b+1. The lifetime is BLACK and future-consumed at EVERY cut a,...,d. Choose any maximum-radius cut tau in that interval, and put

    D = max_{a<=t<=d} ||p_t-q||_infinity,
    P = number of permanent R births during updates [a,d).

Then D>=1 and the following exact resource inequality holds:

    P + L_a + 2 L_tau + L_d >= 4D.                       (1)

The endpoint d is BEFORE the marked L, not after it. The marked birth itself is not included in P and would not count as permanent anyway. No cap on active components, no ordinary-epoch language, and no nesting/stack assumption is used.

Consequently, if the true future-relevant mass at those three cuts is at most M, then

    P >= 4(D-M).                                        (2)

A large excursion that really RETURNS to its marked black cell cannot be paid only by indefinitely reusing a bounded number of relevant bits without producing permanent output. This is a lower bound on actual irreversible output, not a decreasing initial-seed fuel claim.

## 2. Proof with the exact cursor correction

For any interval [u,v), let K(u,v) count the distinct cut-u black lifetimes consumed during that interval. Let P(u,v) count permanent R births during it. Two elementary facts are exact:

    |B_v|-|B_u| = L_v-L_u+P(u,v),
    |B_v|-|B_u|+2K(u,v) >= |B_v symmetric_difference B_u|.

The first holds because a currently forever-unread lifetime never changes status or disappears: only a new permanent R birth increases that part of the board. The second holds because every bit removed from B_u retires its original lifetime; consumption followed by rebirth only makes K larger.

The signed retained transport-debt theorem, with comparison board B_u and zero height, gives

    |B_v symmetric_difference B_u| >= 2||mu_v-mu_u||_infinity,
    mu_t = p_t - dir(h_t)/2.

Apply these statements to a -> tau and tau -> d and sum. For any chosen coordinate i,

    L_d-L_a+P+2K(a,tau)+2K(tau,d)
      >= 2(|mu_tau,i-mu_a,i|+|mu_tau,i-mu_d,i|).

The marked q lifetime survives both intervals. Therefore

    K(a,tau)<=L_a-1,       K(tau,d)<=L_tau-1.

Substitution yields the slightly sharper endpoint-sensitive statement

    P+L_a+2L_tau+L_d
      >= 4+2(|mu_tau,i-mu_a,i|+|mu_tau,i-mu_d,i|).         (3)

Choose i and sign s with s(p_tau,i-q_i)=D. Immediately after its R birth,

    mu_a = q + dir(h_a)/2,

whereas mu_d=q-dir(h_d)/2. Thus both signed endpoint midpoint coordinates relative to q lie in [-1/2,1/2]. The peak midpoint has signed coordinate at least D-1/2. Since D>=1, it is at least both endpoint coordinates. The sum of the two distances is therefore at least 2D-2. Equation (3) gives (1).

This also handles a zero-length first leg tau=a. Such a case can only have D=1. Its first transport/K/P contributions are zero, and the displayed inequalities remain valid. A consumed R lifetime cannot have D=0 because the birth update moves to a neighboring cell.

## 3. A spatially distributed version

Fix the coordinate/sign chosen above. Let J be the integer axial lines strictly separating p_tau from BOTH p_a and q. There are at least max(0,D-2) such lines.

For each r in J, the retained strict-line charge gives two bit discrepancies on EACH leg. Let L_t(r) count relevant current lifetimes on that line and P_r count permanent births there during [a,d). The same lifetime accounting gives

    P_r + L_a(r) + 2L_tau(r) + L_d(r) >= 4.              (4)

No assertion about a particular cell persisting between crossings is needed. The head may cross a line many additional times and the carrying cells may change.

If L_a,L_tau,L_d<=M, at most M of these common separating lines can have P_r=0, because each such line needs at least four units of the displayed live-stock weight and the total weight is at most 4M. Hence at least

    max(0,D-2-M)

DISTINCT separating lines receive a permanently unread R lifetime during this returning episode. This is an explicit geometrically distributed output obligation, not merely a renamed count of old-input exchanges.

## 4. Overlap-safe amortization, without LIFO ancestry

Assume L_t<=M for EVERY cut in a finite interval [T,U], where M>=1. Take any finite collection F of consumed R lifetimes with births at least T and deaths at most U. Let D_l be each lifetime's maximum return radius, and let P_total count permanent R births in [T,U).

Then

    4 * sum_{l in F} max(0,D_l-M) <= M * P_total.         (5)

To prove this, keep only lifetimes with D_l>M and sum (2). A permanent birth at update s can lie in [b_l+1,d_l) for at most M of the selected lifetimes: every one of them is a distinct currently black, eventually consumed lifetime at cut s, hence belongs to C*(s). Thus the sum of their individual P counts is at most M times the actual permanent birth count. This proves (5).

Nested and interleaved lifetimes, ordinary non-LIFO returns, shared helpers and reattachments are all allowed. The overlap factor is explicit and comes from the supplied bound on the ENTIRE future-relevant cohort, not a bound on one active component. The same permanent output is not silently charged once to arbitrarily many overlapping returns.

Equation (5) is an amortized resource inequality, but its right side is NOT finite original fuel. A finite seed can produce infinitely many permanently unread black cells, as a standard highway does. No contradiction or global attraction conclusion is inferred from this lower production cost alone.

## 5. A distinct sufficient route to the dynamic stale-memory target

Here is a conditional consequence with precise orbit-dependent hypotheses. Suppose that after some cut T:

1. L_t<=M at EVERY later cut;
2. every consumed R lifetime born after T contains at most P0 permanent R births before its consumption.

Then every such lifetime has radius

    D <= R = floor(M+P0/4).

A direct finite first-return clock bounds its age. Throughout cuts a,...,d-1, its head lies in the fixed (2R+1)-square about q but is not at q. The q bit remains BLACK. With N=(2R+1)^2, there are at most

    4(N-1)2^(N-1)

possible inside-board/heading/head states. A repeated one would force the same closed read cycle forever, never reaching q, contradicting the actual later consumption. Exterior bits are untouched during that repeated segment. Thus

    d-b <= 4(N-1)2^(N-1)+1.                             (6)

This finite-return argument does not need to assume boundedness of the whole orbit. After discarding the finitely many old-at-T consumptions, the retained stale-memory theorem applies and gives an eventual NONZERO TRANSLATING PERIODIC TAIL. It does not identify that tail as canonical104.

Neither hypothesis is proved universally. Both use actual complete futures, so this is not presented as an effective finite-state algorithm for arbitrary inputs. Bounded relevant cardinality alone is insufficient for this argument: its spatial positions can spread far apart, and P0 can grow. Bounded active-component mass is still weaker and must not be substituted for hypothesis 1.

## 6. Adversarial exact controls

`check_return_permanent_output_debt.py` directly simulates eight named complete inputs, proves every terminal infinite word by exact ray-parity changes, classifies every current lifetime's eventual first read or never-read fate, and checks (1) and (3) for EVERY R-born consumed lifetime completed in each bounded trace. It also checks (5) by explicit overlap multiplicities, not by assuming disjoint intervals.

The controls include the fourteen-cell defect and correctly filled guard, the blank ant, the four-cell port, its ninety-cell protected recovery, and the full twenty-cell feedback seeds n=20,80,400. The total is 322855 physical updates and 142797 completed R lifetimes.

For the twenty-cell R60 target, the three controls have respectively:

| n | age | maximum radius | permanent births during lifetime | L_a,L_tau,L_d |
|---:|---:|---:|---:|---|
| 20 | 10904 | 97 | 1291 | 31,37,61 |
| 80 | 48344 | 397 | 5611 | 31,37,61 |
| 400 | 248024 | 1997 | 28651 | 31,37,61 |

Their observed full-prefix relevant-mass maximum is 77. At n=400 there are 23 completed returns with radius above this M; their excess radii sum to 44231. The summed permanent-output count with multiplicity is 660538, and the largest overlap at a permanent birth is 23, explicitly below M. These named checks are not an all-parameter inference.

The paired-wake example is correctly classified: its four later-read births are NOT permanent in the defective orbit, even though they are permanent in the filled comparison. The proof never imports the comparison's output credit. Standard tails remain allowed, and the earlier 184/20 prepared controls are not reinterpreted as noncapturing orbits.

## Evidence and exact remaining gap

The underlying midpoint/strict-line charge is the signed result in `global_capture_bridge_2026-10-23/live_cursor_transport_debt.md`, Sections 1--3, based on the retained axial separator proof. The permanent/relevant balance is the exact identity in the independently checked paired-wake note. The final bounded-age implication is retained from `sources/kehao95-core/memory_feedback/proof/stale-memory.md`.

This application isolates a real alternative for unbounded late consumed ages: unbounded spatial returns must be accompanied by large relevant stock at the selected cuts or large, distributed, ACTUALLY permanent output during those returns. Under a sustained relevant-mass cap, the output costs admit the explicit overlap-safe charge (5). Proving universal bounds or an incompatibility of this output organization with continued nontranslation remains open. Global finite-seed standard104 attraction remains UNSOLVED.
