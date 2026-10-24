# Exact retrospective compact-recurrence bridge, with the missing global premise explicit

Independent analytic scope note, 24 October 2026, 10:18 UTC. This is a structural reduction, not a new proof of global attraction, a novelty claim, or a computable recognition algorithm.

## Definitions

Consider one actual classical Langton-ant orbit from a complete finite black board. At the pre-update cut t write B_t for the ENTIRE current black set, p_t for the actual head and h_t for its incoming heading. Define

C*(t) = {q in B_t : q is read at some time s >= t}.

This is the set of actually future-read CURRENT black lifetimes, not an active component, a template's future input set, or a finite-horizon approximation. A current black cell first read later is necessarily consumed at that first read. Define rho(t) = max({||q-p_t||_infinity : q in C*(t)} union {0}). Every B_t and C*(t) is finite, but no uniform bound on either is assumed.

## 1. Exact pruning and equality of complete relevant states

Replacing the complete board B_t by C*(t), leaving every other site WHITE and retaining the actual pose, reproduces the ENTIRE future orbit. Indeed, before a hypothetical first discrepancy, the only initial differences are black cells that the original future never reads. The shared path cannot encounter one of those cells. This first-difference induction is valid for every finite prefix, hence for the infinite future.

Consequently, if two cuts s<t in the SAME orbit satisfy

h_s=h_t and C*(t)-p_t = C*(s)-p_s,

determinism and translation covariance imply, for every k>=0,

turn_(s+k)=turn_(t+k), h_(s+k)=h_(t+k),
p_(t+k)-p_(s+k)=p_t-p_s.

Thus the actual future starting at s has period P=t-s in its turn/heading stream and full translation d=p_t-p_s. The original full boards at the two cuts need NOT be translates: their forever-unread archives may differ. It is the two complete pruned finite boards whose literal futures coincide.

## 2. Infinitely many bounded-radius cuts suffice

Suppose some finite R has rho(t)<=R at infinitely many cuts. The normalized pairs (C*(t)-p_t,h_t) then have at most

4 * 2^((2R+1)^2)

possibilities. Two of these cuts have the same pair, so Section 1 gives a translating periodic future. This is a count of states at the selected cuts, NOT a bound on elapsed time between them, a finite-horizon way to compute C*, or a uniform R for all inputs.

The full drift d cannot be zero. For completeness, a bounded ant trajectory is impossible even on an arbitrary fixed initial coloring. Its nonempty finite set I of infinitely read cells has a cell q maximizing x+y. Eventually neither its north nor east neighbor is ever visited again. The invariant (p_x+p_y+h) modulo 2 fixes the incoming AXIS at each physical cell. At q, a vertical incoming axis then permits only entry from south and exit west, requiring L on every sufficiently late visit. A horizontal incoming axis permits only entry from west and exit south, requiring R on every sufficiently late visit. Both contradict the alternating colors of repeated reads. A zero-drift periodic future would be bounded, so d!=0.

## 3. Converse and exact geometric divergence alternative

If the actual future is P-periodic up to nonzero translation d, then for every sufficiently late cut t its future turn/pose stream at t+P is the translate by d of that at t. The complete relevant set is determined by this future: a cell is in C*(t) exactly when its FIRST future read is L. Therefore C*(t+P)=C*(t)+d, and rho(t) is eventually periodic and bounded.

For any one finite-seed orbit, the following are therefore equivalent:

1. Its actual future eventually translates periodically, with no requirement that it is canonical104.
2. rho(t)<=R for infinitely many cuts, for some finite orbit-dependent R.
3. rho(t) is eventually uniformly bounded.

In particular, an orbit that does NOT eventually translate periodically must satisfy rho(t)->infinity: for every fixed R, only finitely many cuts have rho(t)<=R. This is stronger than merely saying that the relevant radius is unbounded, but it is still retrospective because C* uses the true whole future.

## 4. Exact interface to controller classification

A nonzero-drift periodic future from a finite initial board yields a complete WHITE translating front after discarding its finite transient. For each phase class there are finitely many visits to any one physical cell; sufficiently far translated physical copies avoid every original black input and have their actual first read WHITE. The finite class histories consequently satisfy the complete WHITE alternating history and ordinal conditions. No width, visit cap, growth, or period bound follows from this construction.

Therefore a sufficient two-part route to universal canonical104 attraction is:

A. Prove that every finite-seed orbit has infinitely many cuts with uniformly bounded ENTIRE relevant radius, with the bound allowed to depend on the orbit.
B. Prove that every complete WHITE translating front that can arise from a finite seed has the canonical104 future, up to phase and genuine spatial symmetry.

Neither A nor B has been established. The current small-active exit, restricted-language three-RAW simplicity, fixed standard directed-inventory rigidity, and specific drift/growth interfaces do not supply A or B. In particular, a noncanonical translating controller would have bounded relevant radius; one cannot replace “nontranslating” by “noncanonical” in Section 3 without a separate uniqueness theorem.

## 5. Corpus counterchecks and limits

- The all-parameter sixteen-cell family has identical entire normalized 285-cell contact states across DIFFERENT initial boards. This correctly fixes their future but says nothing about their very different preceding return ages or permanent production.
- The two paid module concatenations have first relevant state297 and second285 in the SAME orbit. They do not satisfy the repeated-state premise, even though their local protected templates coincide. The 12 additional still-relevant input lifetimes must not be cropped away.
- Bounded cardinality of C*, bounded active-w mass, repeated local core shape, a bounded protected window, or a fixed number of input components do not imply a bounded radius for the ENTIRE relevant set. No such substitution is made.
- The standard-written wake launch obstruction concerns one exact regeneration protocol and does not force A. The conditional no-reentry separator is sufficient for capture but no occurrence theorem is supplied.
- This note does not furnish a universal or computable bound, a stopping-time certificate, an amortized resource decrease, a permanent-output capacity bound, or a new empirical claim about closeness to solving the conjecture.

The exact task left by this bridge is to rule out genuine long-term divergence of the entire relevant spatial span (or otherwise force compact recurrent relevant states), while separately closing unrestricted translating-front uniqueness. Calling that missing premise “compactness” is not a proof of it.
