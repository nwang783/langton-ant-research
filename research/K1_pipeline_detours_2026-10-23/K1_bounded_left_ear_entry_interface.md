# The exact two-entry demand of a bounded LEFT K=1 ear

23 October 2026, 18:06 UTC. General interface extracted from the pending
row-5 two-exit obstruction. This is an entry-clock requirement, not a
fuel charge, and no particular deep-detour inventory is assumed.

## Exact hypotheses

Use a complete translating front with the signed canonical first-L
circle Gamma and K=1 crossing pipeline. Let a finite forward PHYSICAL
Gamma arc and a simple physical crosscut chi in LEFT bound a bounded
LEFT Jordan disk Omega. Suppose the selected contacts on that arc are
exactly v_j,...,v_k in lifted order. The crosscut contains no selected
contact. Count EVERY actual entry through chi, not a selected sheet or
an abstract flow. The cursor is outside Omega at sufficiently negative
time by nonzero full drift and a finite per-period trace.

## Entry-clock demand

If k>=j+1, before the departure R0_(j+1) there must have been at least
TWO entries through chi. More precisely:

1. a first chi entry occurs before R0_j;
2. a further chi entry occurs strictly between R0_j and R0_(j+1).

Indeed the Gamma boundary crossings are R0 exits and R2 entries, and
K=1 gives

    R0_j < R0_(j+1) < R2_j.

All R2 indices on the arc are >=j, with increasing actual times. There
is no Gamma entry before either of those two exits. The cursor cannot
exit twice without an intervening entry, so both entries must use chi.
Any additional chi exits only require further entries; they cannot
relax this demand.

Dually, if k>=j+1, there must be at least two chi exits after the last
Gamma exit R0_k: one strictly between R2_(k-1) and R2_k, and one after
R2_k. The pipeline gives R0_k<R2_(k-1)<R2_k; there is no later Gamma
exit. This uses the future-outside condition as well.

This interface holds for arbitrary crosscut multiplicity and arbitrary
side detours, provided its complete crossing list is used. It retains
one-R and source-L histories without turning any into a free entry.

## Rank-3 locking corollary

Suppose k>=j+1, a boundary contact v_j has an actual L3, and a local
supplier forces

    T3(v_j)=t+c, with c<4.

Since T3(v_j)-T2(v_j)>=4, the two-entry demand occurs before t+c-4.
If the crosscut has at most ONE actual entry before that time, the
configuration is impossible. This statement keeps c signed and does
not assume the supplier event at t is itself an entry unless its
literal geometry proves it.

For the specific signed row-5 return, c=2 and t=T2(O). Its only possible
chi entries before t are O.R0; O.R2 is at t and O.L3 later. Thus the
necessary two-entry demand fails. The interface does not by itself
classify the boundary ports of other straight-gate suppliers or ban all
LEFT folds. Those still require literal complete-history reconstruction.
