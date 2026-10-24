# An exact FIN reduction for infinite-board capture, with its finite-seed boundary

2026-10-22,23:34 UTC. Status: Sections1--5 independently analytically audited, including effective-F_sigma and uniformly total computable-board completeness. This is a representation/domain separation, NOT a finite-seed universality or undecidability theorem.

## 1. Statement

Let FIN be the set of binary streams with only finitely many1s. There is a computable continuous map

    F : {0,1}^N -> {0,1}^{Z^2}

such that, at one fixed launch pose,

    x in FIN  iff  F(x) eventually follows standard104
              iff  F(x) has any eventually periodic turn stream.

Moreover, finite1 input streams produce FINITE capturing black sets, while infinite1 streams produce genuinely aperiodic boards. Every individual output cell is computable from a finite input prefix with a known spatial bound. The negative outputs necessarily have infinite black support.

The construction uses only the already audited exact standard-tail certificate and effective four-cell exterior completion. It does not ask the ant to simulate the input stream's computation.

## 2. Maintained data and effective stages

Enumerate all infinite eventually periodic binary turn words w_j=u_j(v_j)^infinity, with v_j nonempty. Repetitions in this enumeration do not matter. Start from any explicitly certified finite capturing seed B_0 at the chosen pose, with its finite transient and cyclic104 tail description. Maintain:

- a finite black set B, with a certified and explicitly described eventual standard turn stream;
- a protected finite turn prefix through time T;
- the number j of1s already processed, so the first j candidate words have been permanently excluded by this protected prefix.

At input position n, a0 leaves the data unchanged. A1 processes w_j.

The current actual infinite stream is explicitly ultimately periodic. Equality with w_j is decidable by comparing the finite transients and then a common finite period. If the streams differ, find a finite distinguishing time, extend T to include it, and do not change B.

If they are equal, choose a square Q containing:

- every old black cell;
- every read/pose cell of the protected prefix;
- the radius-n square about the origin.

The current capturing path is unbounded. Find its first future READ at a cell q outside Q. That cell has never been read before and is initially white, because Q contains the old black set and all earlier protected reads, and this is the first later exit read. Add q to B. This leaves all earlier turns unchanged and changes that first read from R to L, hence creates a finite distinguishing prefix from w_j.

Now apply the effective four-cell exterior-completion theorem to B union{q}, using a larger protected square containing all its reads through the new distinguishing time. It adds four new black cells outside this square and supplies a certified standard tail. The resulting new B contains the old B, preserves all earlier distinguishing prefixes, and is again certified capturing. All five new cells lie outside the radius-n square. Update T and j.

The finite standard-tail description supplied by completion makes the next equality test effective. Even if one uses only the constructive four-cell seed output, the exact positive tail semidecider is guaranteed to terminate on that output and supplies the needed description. No unknown capture test or conjecture is used at any stage.

## 3. The limit and both directions

The finite black sets only increase. Define F(x) as their union.

For a fixed cell q with sup norm R, stages with input index n>=R cannot change q, because every new cell lies strictly outside the radius-n square. Thus its final color is decided by simulating only the finitely many earlier input stages. All these stages terminate. This proves computability and continuity; no unbounded lookahead in x is required.

If x has finitely many1s, the maintained set changes only finitely often and the final board is one of the certified finite capturing seeds.

If x has infinitely many1s, every candidate w_j is eventually processed. At its stage a finite disagreement with w_j is found or created. Every later stage preserves that prefix, and the pointwise limit board also preserves every read in it. Hence the limit trajectory differs from EVERY eventually periodic turn stream. It is genuinely aperiodic, and in particular noncapturing.

The output support in this second case is infinite. If only finitely many cells had ever been added, the maintained board would eventually stop changing and would still be one of its certified finite capturing seeds. Its ultimately periodic stream would appear as some later candidate and require a further addition, contradiction. This conclusion does not assume the finite-seed highway conjecture.

## 4. Effective F_sigma completeness

`infinite_board_topology.md` already places both capture H and eventual periodicity P in effective F_sigma. FIN is an effective F_sigma-complete set under computable continuous reductions; an elementary verification is as follows.

Given a uniformly effective sequence of closed sets C_j in Cantor space, inspect at stage n the first n finite refutation tests for candidate sets C_0 through C_n. Let a_n be the least j<=n not yet refuted, using n+1 if all these candidates are refuted. The sequence a_n is nondecreasing. Emit1 whenever it changes and0 otherwise. If the input belongs to some C_j, the least true candidate eventually stabilizes after all smaller false candidates are refuted, so only finitely many1s occur. If it belongs to none, a_n tends to infinity and changes infinitely often. Each emitted bit depends on finitely many input bits, uniformly effectively. Thus membership in the union of the C_j reduces to FIN.

Combining this with Section1 proves that H and P are both effectively F_sigma-complete on arbitrary cell-query boards. This is stronger than just saying they are not open or not G_delta. It is still a different domain from finite black lists.

## 5. A countable-index consequence and the exact caveat

Given an index e for a c.e. set W_e, form a computable binary stream x_e which emits1 exactly when a NEW element is enumerated at that stage. Standard finite-stage simulation can ensure at most one new element per stage. Then x_e belongs to FIN exactly when W_e is finite.

The construction above gives a uniformly TOTAL computable board B_e=F(x_e), and

    W_e finite iff B_e captures iff B_e is eventually periodic.

Thus even on this explicit uniformly computable family of arbitrary boards, the capture index set is FIN-complete at arithmetical level Sigma2. This does not require noncomputable physical backgrounds.

However, it is NOT a reduction to the exact finite-seed problem: negative instances produce infinite support, and the board-description algorithm itself computes the input enumeration. It is not an autonomous computation performed by an ant launched from a finite list. Even on positive instances, no computable radius bound on the final finite black set is supplied.

The representation issue is real even without ant dynamics. From a Turing machine e, define a total computable board whose only possible black cell is(t,0), where the machine halts for the first time at step t. Every such board has at most ONE black cell, but uniformly extracting its complete finite black list from its program index would decide halting. A promise of finite support in an oracle/program representation does not automatically provide the finite list used by the finite-seed conjecture.

## 6. Sparse backgrounds and arbitrarily long standard episodes

Independently analytically audited,2026-10-22 23:39 UTC.

The construction can obey two additional conditions simultaneously.

First, at input stage n require the protected square to contain the radius-2^n square. Every newly added black cell is then strictly outside that radius. There are at most five additions per stage: one distinguishing marker and the four exterior-port cells. Consequently, for every output and R>=1,

    |F(x) intersect [-R,R]^2| <= |B_0| + 5(1+floor(log_2 R)).

Any fixed computable increasing unbounded separation function can replace 2^n. The larger protected squares do not affect termination of the stage or the continuity proof. In particular this genuine undecidability/unrecognizability reduction survives on an explicitly uniformly computable family with extremely sparse, zero-density black backgrounds. Zero density is not finite support.

Second, after processing the j-th1, extend the protected finite prefix through a new cyclic standard104 episode of at least104(j+1) turns, beginning after the previously protected prefix. The maintained capture certificate provides such an episode effectively, after whatever finite transient the new capturing seed has. Protect ALL read cells of the enlarged prefix, as before.

For an infinite-one input, these protected episodes survive in the limiting trajectory. Its turn stream is therefore genuinely aperiodic but contains arbitrarily long standard episodes. No claim about the frequency or asymptotic density of defects follows. For a finite-one input the last finite board still captures permanently.

Both refinements preserve every equivalence and completeness statement above. Their point is the exact domain boundary: very sparse infinite hardware and arbitrarily convincing finite highway episodes still do not make a board a finite seed.
