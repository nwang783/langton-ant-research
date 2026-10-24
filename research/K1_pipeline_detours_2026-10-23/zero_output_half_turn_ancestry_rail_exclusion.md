# A zero-output half-turn forces a periodicity-incompatible ancestry rail

23 October 2026. Complete WHITE cap-four translating front with actual full P,d and N_odd = 0. Assume the displayed actual half-turn mode of 4670f374. The theorem below needs no selected Gamma or K = 1 premise once that local mode is established. It is a conditional exclusion of THIS zero-output mode, not of general K = 1 fronts or odd-output defects.

## 1. Initial full interface

Use physical face indices and physical cell coordinates separately, even when their integer pairs agree. Put

    D_n = (-4-2n,0), n >= 0.

Initially D_0 is the half-turned actual positive duplicator Q2. Its four cell histories, in NW,NE,SE,SW order, are

    SSNS, EEWE, SNNN, WWEW.

Its canonical parent is the NW diagonal face U_0 = (-5,1); its two actual children are the NE face L_0 = Q1 = (-3,1) and SW face R_0 = (-5,-1). Its associated opposite leaf T_0 = (-3,-1) is the previously signed R leaf.

The NE child L_0 has physical SW k_0 = (-3,1) = EEWE and NW j_0 = (-3,2) = NNNS. It is TERMINAL, with NE EWEE and SE g_0 = (-2,1) = NSSS. The full two histories k_0,j_0 are essential below; the upper low height alone is not sufficient.

The opposite leaf T_0 has physical NW SNNN, NE WWEW, SW WEWW and SE SSSN. In particular its SW cell has exactly one E input. These are complete histories from the signed mode, not just port counts.

## 2. Induction invariant, including ranks and modes

At stage n set x = -4-2n. Carry ALL of the following:

1. D_n = (x,0) is an ACTUAL positive all-four duplicator, with NW w = (x,1) = SSNS, NE k = (x+1,1) = EEWE, SE m = (x+1,0) = SNNN and SW h = (x,0) = WWEW.
2. Its actual parent is U_n = (x-1,1). Its actual NE child is L_n = (x+1,1), with known SW k = EEWE and NW j = (x+1,2) = NNNS. This also fixes the opposite upper C face (x,2) at b = M-2.
3. Its actual SW child is R_n = (x-1,-1), through the negative canonical contact h = WWEW.
4. Its associated opposite leaf is T_n = (x+1,-1), with NW SNNN, NE WWEW, SW WEWW, SE SSSN.

For n >= 1 the induction will prove L_n = U_(n-1), a degree-one canonical face, and T_n = R_(n-1), a terminal leaf. The INITIAL L_0 is terminal instead; that is the eventual periodicity defect.

Zero-output saturation, already signed in 56b51121, says every flag-one leaf is the opposite I leaf of a unique ACTUAL positive D4. Also any face with an actual flag-one child must itself have incoming flag one: an incoming-zero face with such a child would be a positive O producer with an odd canonical entry. Therefore the seven complete even flag-one canonical profiles exhaust every new parent used below.

## 3. The upper parent is rigid only after keeping k and j

At U_n the SE corner is w = SSNS. Its NE corner v = (x,2) faces the strict other C height b. The complete w.S input inventory requires three S departures from v. Zero output and the height difference two force a four-read history with two R headings E, leaving EEEW or EWEE.

The complete even canonical-face inventory at the two possible LEFT birth corners retains precisely two candidates for U_n:

    SW z=(x-1,1) EEWE, NW y=(x-1,2) NNNS,
    SE w=SSNS, NE v=EEEW or EWEE.

The second candidate is NOT excluded by height alone. It fails by the retained full NE-child histories k = EEWE and j = NNNS. If v = EWEE, exact ordinal ports give the impossible clock cycle

    w.L1 -> k.R0 (+1),
    k.R0 -> k.L1 (>=4),
    k.L1 -> j.R0 (+1),
    j.R0 -> j.L1 (>=4),
    j.L1 -> v.L1 (+1),
    v.L1 -> w.L1 (+1).

Thus a time would be at least twelve greater than itself. Every arrow except the two same-cell rank gaps is an actual consecutive physical step. In particular v.L1 is the SECOND S departure and must feed w.L1, not another chosen occurrence.

Hence U_n is uniquely

    SW EEWE, NW NNNS, NE EEEW, SE SSNS.

Its canonical birth is SW z, from the maximum face D_(n+1) = (x-2,0). Its only actual child is D_n through w; the other non-entry corners are strict. Thus U_n has degree one and flag one. Its NW y = NNNS fixes the next upper opposite C face (x-2,2) at b. Both required physical child histories k,j have therefore propagated, not merely the low face height.

## 4. The SW child forces the next actual duplicator

At R_n the NE canonical entry is h = WWEW. Its NW corner a = (x-1,0) is flat between R_n and the already known D_(n+1). The complete S input of a comes from z = EEWE and occurs once. Its SE corner l = (x,-1) must emit E exactly once, matching the E inventory of the known SW cell of T_n = WEWW.

The complete seven-profile even inventory gives

    l=SSSN;
    (SW s, NW a) = (WWWE,NNSN), (WEWW,NNSN),
                   or (WEWW,SNNN).

D_(n+1) already has actual flag-one child U_n. With NE z = EEWE, the same complete canonical inventory says that if a = NNSN, then a is D_(n+1)'s canonical incoming contact from R_n. But the actual canonical edges already include

    D_(n+1) -> U_n -> D_n -> R_n.

Adding R_n -> D_(n+1) would be a finite PHYSICAL canonical cycle. Strict birth increase around these four distinct physical faces forbids it. This argument does not discard an essential quotient cycle by assuming primitivity.

Therefore a = SNNN and s = WEWW. R_n is a flag-one terminal leaf: its two other non-entry corners are strict, and a is positive rather than a child contact. Saturation forces R_n = I(D') for an ACTUAL positive all-four duplicator. The mandatory positive flat a corner and the whole I profile recover D' uniquely as D_(n+1), not as an arbitrary earlier face.

Consequently D_(n+1) has the half-turn profile NW SSNS, NE EEWE, SE SNNN, SW WWEW, both canonical children U_n and R_(n+1), and associated opposite leaf R_n. All four induction clauses hold at n+1. In particular L_(n+1) = U_n has degree ONE, SW EEWE and NW NNNS; T_(n+1) = R_n has exactly the stable complete leaf profile needed for the next E-port count.

The certificate zero_output_half_turn_parent_rail_interfaces.py/json reconstructs these translation-invariant interfaces from the seven even flag-one profiles. It keeps both upper candidates and rejects exactly v = EWEE by its positive ordinal clock cycle. The lower interface has three R candidates and ten R/parent pairs: eight produce the forbidden physical canonical cycle, one cannot be the required positive duplicator after leaf saturation, and exactly one remains. This is a fixed local proof, not a front scan.

## 5. Exact full-drift quotient contradiction

The induction forces every D_n for n >= 0, with fixed y = 0 and x decreasing by two. Each is active and incident to an actual read. A complete translating front has only finitely many active physical face classes modulo the ACTUAL full drift d.

If d is not horizontal, no two D_n are congruent modulo integer multiples of d. This gives infinitely many active quotient classes, impossible.

If d = (a,0), a != 0, choose N >= 1 and an integer k with

    k d = (-2N,0).

For example N = |a| and k = -2 sign(a) work. Then D_N = D_0 + k d, and the actual full translation sends its NE child to

    L_N = L_0 + k d.

But L_0 = Q1 is terminal, while L_N = U_(N-1) has canonical degree one. Equivariance of the actual canonical parent graph forbids that.

There is also a direct heading contradiction, avoiding any graph-role convention: L_0's physical SE corner g_0 = (-2,1) has complete history NSSS. Its translated cell (-2-2N,1) is U_(N-1)'s SE corner, which the induction forces to have complete history SSNS. The actual full-drift relation preserves COMPLETE chronological headings up to the time shift kP, so those two histories cannot disagree even at R0.

This handles quotient recycling explicitly. A strict spatial decrease alone was not used as a contradiction. Neither a primitive period nor a primitive drift was substituted.

## 6. Scope and correction of the finite-motif interpretation

Therefore the displayed half-turn mode cannot occur in a complete WHITE cap-four translating front with N_odd = 0. No K = 1 or Gamma membership is used in the induction after the initial actual mode is supplied. Cross-Gamma transfer cannot reset the proof: the propagated actual parent/child identities and full local histories are independent of how one labels essential cycles.

The earlier signed 29334de0 result remains correct as a FINITE LOCAL motif. Its activation association points back to an already known face, but its external parent was left open. The present induction closes that open ancestry; the finite motif was not a complete global realization or a terminal resolution of the parent problem.

This does not exclude positive output, U-defect interruptions, general zero-output fronts without this mode, or general K = 1 fronts. It is not an original-fuel bound. The next step must keep the remaining repeated-route and lower-counterflow alternatives rather than silently claiming a full front exclusion.

Dependencies: global canonical flag inventory d1f7304b; opposite-leaf saturation and source recovery 9868024f and 56b51121; exact initial half-turn gate 4670f374; signed finite LOCAL parent motif 29334de0. The ordinal cycle, induction invariant and quotient contradiction are explicit above.
