# A head-record timing bridge to translation, and its exact compactness boundary

24 October2026. Author analytic theorem and complete all-parameter controls; independent audit pending. This does not prove universal attraction or canonical104 uniqueness.

## 1. Positive theorem: bounded record gaps force bounded memory

Fix one axis normal a in{E,W,N,S} for which the head makes infinitely many strict historical records. Use integer record levels k, and let tau_k be the first cut at which a·p=k. Beyond the initial head maximum these are consecutive strict records, because a unit grid step cannot skip a level.

Suppose for some integer H>=1 and all k>=k0,

    tau_(k+1)−tau_k <= H.                            (1)

Then every R lifetime born at update b>=tau_k0 and consumed at update d>b satisfies

    d−b < H^2.                                      (2)

Proof. Choose k,j with tau_k<=b<tau_(k+1) and tau_j<=d<tau_(j+1). The shared birth/death cell q has a·q<=k. At the death cut, at most H−1 unit updates have occurred after the j-th record, so

    a·q = a·p_d >= j−(H−1).

Hence j<=k+H−1, and

    d < tau_(j+1) <= tau_(k+H) <= tau_k+H^2 <= b+H^2.

This uses actual head geometry and the same physical cell at birth/death. It does not assume nested lifetime intervals, bounded relevant mass, bounded active components, or a word-language cover.

Choose k0 also beyond the original black hull, so tau_k0 is pristine. Every current black cell there has normal coordinate<k0. By tau_(k0+H), every later head has normal coordinate at least k0+1, using (1). Thus none of those old current black cells can be consumed later. At all cuts after tau_(k0+H), every actually future-consumed current black lifetime was born after tau_k0 and satisfies (2). The unit-speed bound gives

    rho(t) < H^2.

The onset of this radius bound is no later than tau_k0+H^2. This explicitly handles the old-cohort transfer; no infinitely old initial lifetime is assumed to vanish by definition.

Exact one-time pruning preserves the whole future. There are only finitely many normalized whole relevant fields and headings inside radius H^2. Two cuts repeat, forcing an exact translating periodic future. Its drift has POSITIVE projection in a, since the records in that direction continue to infinity. This proves eventual translation, not canonical104 classification.

For example, a conservative conditional state count is4*2^((2H^2+1)^2); it gives a finite period/onset bound once the GLOBAL hypothesis (1) is supplied. Observing (1) for a long finite window does not certify its eventual validity or the whole future pruning.

## 2. Converse and a head-only characterization

An eventual translating pose/turn future of period P and drift d with a·d>0 has eventually bounded record gaps in a. In late periods, the normal head trace is a fixed finite phase trace translated by a·d each period. The record phases consequently repeat, and at least one occurs per period. The largest circular phase gap is at most P.

Therefore, for a fixed direction with infinitely many records, eventual bounded gaps are equivalent to eventual translation with positive drift projection in that direction. A genuinely nontranslating finite orbit must have arbitrarily large consecutive record gaps in EVERY direction where records occur infinitely often.

The qualification about infinitely many records is essential. The argument says nothing about a direction with a final record. Classical unboundedness supplies at least one infinite-record direction for a finite-seed orbit; it does not make all four directions recurrent.

This is an operational head-timing reduction, not a proof of the bounded-gap occurrence premise. Translating-tail uniqueness remains separate.

## 3. Compact record limits and a stronger geometric alternative

Normalize a pristine a-record cut by translating the head to0; its incoming heading is a. The entire current forward half-plane a·q>=0 is WHITE. Allowing arbitrary old-side colorings, including infinite support, gives a compact product space

    X_a={B subset {q:a·q<0}, head0, heading a}.

Finite-time ant trajectories depend on finitely many initial cells. For H>=1, the set D_(a,H) of states whose head crosses the record line a·p>0 by time H is therefore clopen in X_a. The next-record domain D_a=union_H D_(a,H) is open, but need not be closed.

Let Omega_a be the nonempty compact set of local accumulation points of the normalized full states at the successive a-record cuts of ONE finite orbit. If every state in Omega_a eventually makes another a-record, compactness gives one H with Omega_a subset D_(a,H). Clopenness then puts all sufficiently late actual record states in D_(a,H). Their consecutive gaps are bounded by H, and Section1 gives translation.

Equivalently, a nontranslating finite orbit has a record-limit state whose future NEVER crosses that record line again. Directly: select actual record gaps tending to infinity, take a locally convergent subsequence of their full starting fields, and use finite-time continuity. For every finite time horizon the limiting head stays on the old side; hence it does so forever.

Such a limit is not a stopped ant. It may move unboundedly inward or tangentially, and may even capture into a perfectly standard highway in that direction. Its initial support may be infinite. None of those possibilities contradicts finite-seed attraction. The missing global question is whether ONE finite source can renew these increasingly long waits often enough to have such a trapped limit in its own record-limit set.

## 4. Outward translating limits are robust and finite-source attainable

There is a useful sufficient alternative to controlling every first-return time. Suppose a state X in X_a has a complete finite-prefix/periodic-translation future with drift d and a·d>0. Its whole old-side read set F is finite.

Indeed, if the finite prefix has L reads and tail phase points q_i,0<=i<P, then the old-side tail sites satisfy

    a·q_i + k*(a·d) < 0,  k>=0.

Each phase contributes only finitely many k; a crude count is

    |F| <= L + sum_i max(0,ceil(-(a·q_i)/(a·d))).

Any state in X_a agreeing on all initial colors of F has the SAME complete future. Every remaining old-side difference is unread and the entire forward half-plane is already WHITE. Thus the basin of positive-a translating futures is OPEN relative to X_a. Moreover, keeping only the finitely many initially BLACK cells in F yields a finite initial board with that exact future. Infinite old-side support is not an obstacle to finite-source attainability in this positive-drift case.

Consequently, if ANY member of Omega_a has a positive-a translating future, some actual record cut agrees on its finite old-side exposure and the original orbit itself eventually translates. This does not require first proving a bound on its whole retrospective rho.

The orientation premise has exact content. For a specified valid infinite future word, finite old-side exposure is both sufficient and necessary for a finite spatial cylinder in X_a to force that WHOLE word. If the old-side exposure is infinite, choose one uninspected old-side read cell, flip its initial color, and obtain the same observed initial cylinder but a different turn at its first read. This is why an inward translating local limit does not supply the outward capture bridge.

The global problem has not been replaced by a proved occurrence theorem. It remains unknown whether every finite orbit has an infinite-record normal whose record-limit set contains an outward translator, or equivalently avoids all never-returning record-limit states as in Section3. The advantage of the reformulation is a precise local-limit target and an exact timing-to-memory implication, without a C* oracle or a guessed finite language.

## 5. Exact sharpness control: next-record waits can escape to infinity

The signed22-cell M→T family gives a quantitative obstruction to treating D_N as closed, even after all original inputs have retired.

In the fixed T trace, the LAST north record before the inward SW exit is at offset8470, head(3,33), heading N relative to q_T. All original inputs were consumed by offset6000. At this genuine pristine record the entire future-relevant field is

    (q_T+L) union R,

where L has296 cells, and R is the same786-cell fixed old cohort. Thus the whole population is1082 and rho=2n+100. Every current forward north-half-plane cell is WHITE.

There is NO subsequent north record during the remaining T trace, the SW return, or the localized postcollision recovery. The latter's maximum absolute y is250, below the old record level2n+262. In the final NW tail the first new north record is the exact phase43, period n+22. Its cut is

    next_N = 82601+312n,
    previous_N = 29671+104n,
    gap = 52930+208n.

At that next record the entire current pruning has only13 cells and radius5, with the canonical phase14 NW future. Each finite orbit therefore does return compactly; the wait is merely unbounded ACROSS the family.

The normalized full fields at the earlier record converge locally to an explicit infinite old-wake field:104 backward standard phase rays XOR a fixed finite T-history mask. For every n, its difference from the actual normalized full record field is supported entirely in

    y <= -2n-30.

This is an exact whole-half-plane source/synthetic-history bound, not a fixed-radius sample. The limit remains genuinely pristine. Its entire future equals the pure T continuation and NEVER makes another north record. Its complete pruning is the finite296-cell local profile, of radius48; the786 remote inputs escape to infinity. The checker also runs that296-cell finite pruned limit through its complete SW certificate.

Hence actual full record states in D_N can converge to a state outside D_N. The control is within genuine finite-source histories, has fixed original mass22, contains no remaining original inputs at the selected cuts, and retains all their archives. It shows exactly why the return-time compactness premise in Section3 cannot be obtained by silently closing D_N or by discarding distant future input.

## 6. Verification and boundaries

The analytic proof of (2) uses only integer record geometry. Its passage to translation invokes the already signed exact pruning recurrence theorem. The checker separately rebuilds the all-parameter sharpness family: three complete futures n100,137,500 through their NEXT north record,477747 physical updates, all current lifetime fates, every full field and infinite tail parity; all exact phase equations locating the next record; the whole296/786 input partition; and the full local-limit ray formula. The all-n result uses the signed M→T source and finite/infinite geometry, not interpolation from three runs.

No bound on record gaps, lifetime age or rho is asserted for an arbitrary finite orbit. The across-family control is not one orbit with unbounded late gaps. A terminal record-limit state is not itself a noncapture certificate, and no infinite-background limit is assumed to satisfy finite-support hypotheses. Canonical104 uniqueness and the actual global occurrence/renewal problem remain open.
