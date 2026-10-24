# Entire relevant radius at a read and at complete cohort renewal

24 October 2026. AUTHOR exact evolution lemma and a finite-seed renewal countercontrol; independent audit requested. Every relevant set below is retrospective and refers to the actual complete future, not an observable local component.

## 1. Exact one-step law

Let C*(t) be the currently BLACK lifetimes consumed at or after cut t in the actual future. Put

    rho(t)=max_{q in C*(t)} ||q-p_t||_infinity,

with rho=0 for an empty set. Then EVERY finite-seed ant history satisfies

    |rho(t+1)-rho(t)| <= 1.

At a BLACK/L read the current head cell p_t is removed from C*. At a WHITE/R read p_t is added exactly if that newly born identity is eventually consumed; otherwise C* is unchanged. Every other current lifetime and its future fate are unchanged. This is an exact retrospective state update, not an effective oracle for deciding whether the new R belongs to C*.

Before moving the head, adding or removing p_t cannot alter a positive maximum distance about p_t. Empty/head-only cases have maximum0. The subsequent unit move changes each remaining distance by at most1; an added head cell has new distance1. These observations prove the bound in every case.

In particular, the consumption of an old lifetime cannot itself cause a large collapse of the head-relative radius. At the instant of consumption that lifetime is at distance0. Any remote radius is carried by OTHER future-consumed identities. A claimed compact return at a last-read event must account for those other identities.

## 2. Persistent escape gives two-sided long-lifetime coverage, not nesting

After the finitely many future-consumed original inputs have retired, every member of C*(t) is R-born. If a radius-maximizing member is born at update b, consumed at update d, and is present at cut t, then

    t-b >= rho(t),       d-t >= rho(t).

The first inequality follows because the head was at its cell at the birth update; the second because it must reach the same cell at the death update. Both use actual unit-speed motion. For rho=0 the inequalities remain harmless.

Consequently, the retained nontranslation alternative rho(t)->infinity implies that EVERY sufficiently late cut lies far from both endpoints of some genuinely consumed R lifetime. It does not merely say that isolated long return intervals occur.

This conclusion alone does NOT imply unbounded simultaneous nesting. As a purely temporal NON-ANT countermodel, take

    b_n=n^2,        d_n=(n+2)^2-1,
    alive cuts b_n+1,...,d_n, n>=1.

Only two intervals can be alive at once, and consecutive intervals properly interleave rather than contain one another. Nevertheless, for each integer t in[n^2,(n+1)^2-1], n>=2, at least one live interval has

    min(t-b_j,d_j-t) >= n.

For t-n^2<=n use j=n-1; otherwise use j=n. The required clearance diverges at every late cut while overlap multiplicity stays2 and no interval contains another.

This is NOT claimed to be an ant orbit, a spatial construction, or a counterexample to attraction. Indeed the signed at-most-two-black theorem makes clear that actual full ant geometry imposes restrictions absent from this interval schedule. It only prevents a false deduction of nested lifetimes from two-sided temporal coverage alone. No finite causally closed remote-debt cycle is inferred from interval data.

## 3. A literal complete-cohort renewal need not be uniformly compact

A natural candidate mechanism is that after every member of a chosen full relevant cohort has been consumed, the newly produced cohort must be geometrically compact, perhaps under a uniform entire-population cap. The signed sixteen-cell moving-module family refutes the UNIFORM version of that claim even when the chosen cohort is the ENTIRE original relevant board.

For every even n>=20, use the independently signed sixteen-cell seed with G ports at

    (0,0),E;
    (7n-1,7n),N;
    (5n,9n-4),W;
    (n+5,5n),S.

All sixteen original black identities are eventually consumed, so C*(0) is exactly that whole16-cell seed. The four G-source first-read offsets are1,22,32,58. The signed all-parameter reference-word and port-ownership proof gives the fourth port entry

    T3=676n-821.

Its last original input is consumed at T3+58. Thus the COMPLETE original-cohort renewal cut is

    tau=1+max original death=676n-762.

The exact G pose after59 updates is(1,2),S. Rotating into the fourth port gives the true renewal pose

    p_tau=(n+7,5n-1), heading W.

At this same cut, the genuinely R-born marker

    q=(3n,3n+3), birth156n-59, death780n-1207

is still BLACK and future-consumed. Its remaining wait is104n-445>0, and

    ||p_tau-q||_infinity = 2n-4.

Therefore

    rho(tau) >= 2n-4,

although the entire relevant population is at most432 for ALL time and every parameter. Initial black mass16 and the relevant-population cap432 are fixed while the radius at complete cohort retirement diverges.

It follows that no bound depending only on original cohort size and entire-population cap can force compactness at this renewal event. The conclusion is not about an unvisited head record, active-component mass, a cropped field, or a partially retired cohort.

## 4. Full-history controls

The new checker replays the complete n20/40/80 histories and certifies their infinite tails against every retained black cell. Using actual future lifetimes, it reconstructs C* at every finite cut with exact extrema heaps and checks the one-step radius law throughout. It records the complete full field and true relevant set at renewal, and the cuts immediately before and after it.

| n | Complete renewal cut | True pose | Measured whole rho at renewal | Whole relevant count | Marked lower bound |
|---:|---:|---|---:|---:|---:|
|20|12758|(27,99),W|76|254|36|
|40|26278|(47,199),W|116|254|76|
|80|53318|(87,399),W|196|254|156|

The measured sharper radii are named controls, not a newly asserted all-n formula. The unbounded lower bound2n-4 and cap432 follow for all even n from the signed full-field family and the exact local59 pose.

## 5. What this changes, and what it does not

A single consumption cannot delete remote radius because the consumed cell is at the head. Even COMPLETE replacement of an original full cohort need not yield a uniform compact cut: the replacement population can include genuinely self-written, far-away inputs whose future consumption is certified.

This does not refute the orbit-dependent compact recurrence criterion. Every member of the displayed family eventually captures, after which its entire relevant radius is bounded. It does not produce one orbit with rho(t)->infinity, and it does not refute an eventual bound that depends on the complete initial geometry of that single seed.

The remaining global obligation is to force compact recurrence, or otherwise exclude persistent spatially remote cohort renewal, using ant-specific geometry and chronology. Temporal interval coverage and last-input retirement alone do not supply that step. Translating-tail canonical uniqueness remains separate from compact recurrence.
