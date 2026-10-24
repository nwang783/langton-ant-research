# Outermost physical exit basin: exact lower edge and the open four-output target

24 October 2026. Author analytic reduction and exact premise controls; independent review pending. The proposed conclusion O_outer>=4 is NOT proved or disproved here.

## 1. Target and safe global cases

Take a complete WHITE translating front under the usual rule. Quotient by the ACTUAL full drift Zd. Let C_1,...,C_k be the physical last-departure basins ordered by their embedded essential last spines, as in the signed path-adjacency theorem. O_i counts permanent R outputs whose PHYSICAL read classes lie in C_i. All actual earlier crossings between basins are retained.

The target is O_1>=4 and O_k>=4, without any visit, period or width cap. It is not a statement about active-C forests, emitted BLACK-support components, lifetime circuits, or every non-extreme basin. If k=1, the retained global complete-WHITE g>=8 already proves this target for that one basin. The remaining question concerns genuine multiple-basin fronts; no theorem that k>=2 is assumed.

## 2. A derived singleton in each outer basin for non-axis drift

Assume both coordinates of d are nonzero and put n(p)=det(d,p). Let S_1 be the lowest essential last spine and a=min n(S_1), taken over the complete full-drift cycle. The open half-plane n<a lies in its negative exterior. Every point with n=a that is not on S_1 also lies in that exterior: a sufficiently small neighborhood of that point avoids S_1 and meets n<a. No monotonicity of the spine is used.

Every other basin is connected to its own higher essential spine by its selected last edges and avoids S_1. It lies on S_1's positive side. Therefore every read cell in another basin has n>a. Since S_1 itself is part of the read footprint, every GLOBAL minimum of the complete read footprint belongs to C_1. The symmetric argument puts every global maximum in C_k. This is a minimum of the COMPLETE READ FOOTPRINT, not the odd output, field color, or C/L stream potential.

At such a minimum, the preceding movement must have negative n increment and the following movement positive n increment. The incoming-axis invariant fixes one axis at this physical cell, and the outgoing axis is its perpendicular. Because both coefficients of n are nonzero, there is exactly one permitted incoming heading and exactly one permitted outgoing heading. Thus every visit would have the same turn. Complete WHITE first-read ownership forces that turn to be R, and color alternation forbids a second visit. The cell is an actual permanent singleton R output. The maximum is analogous.

Consequently

    O_1>=1 and O_k>=1                 (non-axis drift only).

For axis drift, a step along the boundary can have zero normal increment. The constant-heading singleton argument then fails; no axis extension is silently made. The live full drift(3,1) is covered by the non-axis conclusion.

## 3. Exact flux residue, not a positivity claim

For the cut between C_1 and C_2, let J(h) be outgoing minus incoming actual crossing counts in the SAME physical direction h, using N0,E1,S2,W3. Put Phi=sum_h h J(h), and let Q_1 be the actual heading-branch-cut count already defined in cdff2e60. Then

    O_1 = 4 Q_1 + Phi                 (complete WHITE).

At the upper outer basin the analogous identity uses minus the final adjacent-cut flux. Fixed-heading Phi is additive across cuts, unlike principal block-angle Psi. Changing the heading branch cut changes Phi by a multiple of four, so its residue here is intrinsic to that accounting.

Thus a hypothetical counterexample with 1<=O_1<=3 must have

    Phi = O_1 (mod4), in {1,2,3}.

Eliminating those three small-output possibilities would prove the requested lower bound. Proving Phi=0 mod4 for every WHITE outer basin would be a SUFFICIENT, potentially stronger route; it is NOT known and is not equivalent to the target. A basin with five outputs, for example, would satisfy the target but violate that proposed divisibility.

## 4. Actual first/last boundary chronology retained

For each actual crossing u -> v at time t, use the physical copies of their first and last read clocks A_u,B_u,A_v,B_v. Since this edge is not u's selected last departure, its exact NEXT same-cell read exists. Hence

    A_u <= t,       B_u >= t+4,
    A_v <= t+1 <= B_v.

The next-source gap is a positive multiple of four, with its full translation voltage and ordinal retained. R crossings create a lifetime consumed at the next L; L crossings consume an earlier same-cell R lifetime and require a later restoring R. These owners stay in u's basin, but the intervening movement need not. If the target read is its first read, complete WHITE forces actual R at time t+1. None of these relations cancels the movement flux modulo four.

The standard positive control makes the gap visible. In the supplied frame its only first-arrival crossing is L31 in the low 4-output basin to first R32 in the high 8-output basin. Its only first-R departure crossing is first R38 in the high basin to R39 in the low basin. The previous source histories, future source reads and all other six crossings are retained. No monotonicity of first-arrival crossings is inferred from these two events. The independent auditor reports no retained theorem imposing that monotonicity.

## 5. Complete prepared premise checks

Standard's outer output counts are4 and8; its only ordered cut has Phi=4 in the supplied frame. Proper rotations preserve the counts and the zero flux residue. The supplied prepared10/80/1564/4352 controls each have one basin and retain their original complete backgrounds; they are not WHITE counterexamples.

As a stronger premise check, take the exact supplied standard word in reverse chronological order and exchange R/L. Its stable histories are genuinely alternating, but its two outer basins have

    (O,I,charge,Phi,Q) = (0,7,-7,13,-5),
                         (0,5,-5,-13,2).

Thus their cut residues are1 and3, and neither has a permanent output. This is NOT a WHITE realization. The self-contained certificate supplies the entire13-cell forward cap and12 forward BLACK input rays, every stable class history and every boundary clock. One period maps that whole infinite input field exactly to its translate, with no omitted output bits. The unique minimal finite field for N copies is precisely the13-cell cap plus the first N cells on every ray; it has13+12N BLACK cells and leaves exactly the translated13-cell cap. The all-N statement follows directly from the finite class thresholds and exact one-period bit relation, not extrapolation from the independently replayable N=1,2,3,5 controls.

These negative charges and nonzero residues show why the WHITE hypothesis matters; they do not decide the WHITE-only residue or four-output questions. Reversal is not being used as physical return transport in the forward standard controller.

## 6. A retained local interface is not a completed counterexample

The independently signed unconditional drift(3,1) minimum cover already includes the complete named histories

    T0=S, T1=WE, T2=SS, T3=EEW, T4=SSNN.

Their selected last arrows are0->1->4->5, 2->1, 3->6. Only T0 among the known classes feeding the first chain is odd. All higher classes remain UNKNOWN, and may provide further outputs in that same eventual outer basin. This is an explicit necessary OPEN interface, not a complete basin with one output, and not a refutation of O_outer>=4. It demonstrates that the first few read-minimum rows alone have not already settled the target.

In the live middle-short family, the five low outputs are already signed to lie in the basin containing the global minimum, hence in C_1. Only three outputs remain. If the requested four-output bound were established, that family would therefore be forced to have k=1. It would NOT be excluded without another independently proved obstruction to a single basin.

Artifacts: `certify_outer_exit_component_minimum.py` and `outer_exit_component_minimum_certificate.json`. No general output lower bound beyond the stated non-axis singleton, no new translator, and no global attraction claim is made.
