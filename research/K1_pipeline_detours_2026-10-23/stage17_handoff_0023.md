# Stage 17: typed top-output rail capacity and deep-root separation

24 October 2026, frozen at 00:23 UTC. Continues stage16_handoff_0015.md.
All three new theorem/clarification notes below have independent PASS.
No earlier frozen source was edited, and no front or parameter scan
was performed.

## 1. Positive-flat output is not available to a half-turn rail

The full canonical inventory gives five possible upper rail-parent
profiles and nine lower-child profiles, retaining ALL odd cases. Every
odd upper profile has a negative-flat/same-R/singleton witness at z/y/v.
Every odd lower profile has a same-R witness at l or s; the positive-
flat a=SNN case always has a separate l=SSS witness.

Thus a rail can stop using only five physical offsets. Their four
rotations give12 offsets,6 per parity. The exact source nonmerge and
periodicity argument remains unchanged. Residual U stops still inject
into their leaf's unique actual parent. The typed theorem0a9e95c9 gives

    H <=6(Nodd-Npos)+|U| <=7(Nodd-Npos)-n_Sanc,

where Npos counts positive-flat three-read classes (L1=R2, not R0).
The U payment uses negative-flat entries, same-R strict helpers and
singletons, and is disjoint from Npos. This is a single output union,
not an added early/rail charge. H requires the COMPLETE initial rail
interface, not an arbitrary relaxed RIGHT row.

## 2. The dangerous uninspected next-parent odd case is explicitly closed

Before D4 activation, lower a=NNSN would give a prospective next parent
with SE a=NNSN and NE z=EEWE. ALL110 canonical profiles/four rotations
give five completions, ALL born at a. One has odd WWW/NSN left corners;
it is still born at a. The actual identities then form a physical
canonical cycle, so a=NNSN is excluded without assuming those unknown
corners even. Clarification83e9c7f freezes this certificate. It was
independently reconstructed as part of the main audit.

## 3. The rail payment is restricted to top output

Let Q count non-positive-flat odd classes incident to a GLOBAL maximum
C face at M, and T the positive-flat odd classes incident to M. Count
physical classes once, so Ntop=Q+T. Every typed rail witness is on
maximum U_n or R_n. Every O/C/H/S output paying U also touches its
assigned maximum. Therefore the stronger bound holds (eb620d9f):

    H <=7Q-n_Sanc.

All exact six-mode early reservations E from stage16 also touch M,
with E>=2n_A. Interface3 sources give two positive-flat outputs, so
if n3=nS3+nR3,

    Ntop >=B :=max(E, 2n3+ceil((H+n_Sanc)/7)).

Use MAX because non-positive early and rail payments may overlap.
This height/type partition is not an original-seed budget.

## 4. Top output cannot root a deep lower band

At an odd class touching C=M the exact incident unshifted L levels are
M-1/M-1 for singleton, M-1/M-2 for opposite-R three-read, and M-2/M-3
for same-R three-read. Hence no Ntop class can touch L<=M-4.

Under K1, suppose k_j ACTUAL DISTINCT spatial inter-maximum bands
have verified minima<=M-j, with j>=4. At most Nodd-Ntop such bands can
have odd roots; all the rest have their own disjoint reverse cuts.
The same signed physical current partition gives, D=||d||_infinity,

    P >=6D+4jD max(0,k_j-Nodd+Ntop)
      >=6D+4jD max(0,k_j-Nodd+B).

For strict-pit bands j=5, the increment is20D per unrooted band. The
result does NOT manufacture k_j from late branches or renewals. Shared
minima within a band count once, and arbitrary overlapping components
at different levels are not added. No cross-Gamma or general K1
exclusion follows.

Independent reports:
- audits/check_half_turn_typed_nonpositive_capacity_independent.py/json;
- audits/check_top_output_deep_band_partition_independent.py/json.

## 5. Next exact structural lead

An edge-used-three-times graph appears to pair top same-R odd outputs
within the same L=M-3 plateau. This would reduce ordinary lower-root
capacity further, but it is NOT used or promoted in this handoff.
It still needs an explicit finite-quotient/plateau-preservation proof.
