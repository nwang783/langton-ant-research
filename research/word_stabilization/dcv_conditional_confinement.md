# A conditional finite-transfer reduction for D/C/V confinement

Status: the conditional argument, literal packet geometry, all integer inequalities, coordinate margins, and the ordinary 3,873-pair kernel have passed an independent implementation audit. The crucial transfer exclusions remain UNPROVED. This is not a D/C/V exclusion theorem. Independent artifacts: `../audits/check_dcv_conditional_potential.py/json` and `../audits/dcv_packet_ordinary_kernel.json`.

Use maximal packets D C^k and V C^k. The exact short grammar leaves recurrent types D,DC,V,VC,VCC; DCC cannot have a next packet and DCCC cannot have a preceding packet. An infinite tail can therefore be restarted after these finite boundary exceptions. Every packet has its actual M11 right context.

The independently audited residual ledger writes the board as the rotated/translated five-cell core K plus a disjoint finite residual set E. A packet removes its listed residual inputs, creates its listed residual outputs, and leaves every other residual token unchanged. Give each created output a permanent producer-packet/slot label until it is consumed. Give the residual cells at the chosen initial cut an initial label.

For a fixed global coordinate y, define a max potential consisting of:

- the doubled coarse-center height plus a heading offset c_h;
- for every residual cell q, twice q_y plus a label-dependent integer weight.

A created output's weight is w_(packet,slot,heading). If a packet consumes it as input j, its weight must be at least u_(consumer,j,heading). All initial tokens receive I, the maximum of the finitely many u values.

The local packet inequalities say that the new core value and every new output value are at most the maximum of the old core value and the consumed input lower bounds. Unchanged tokens retain their values. Thus the global max potential cannot increase, provided every actual producer-to-consumer transfer respects the corresponding u<=w inequality.

`dcv_packet_maxplus_optimized.json` supplies integer weights. `check_dcv_conditional_confinement.py dcv_packet_maxplus_optimized.json dcv_conditional_confinement_optimized.json` independently of the SMT solver checks all 148 packet-output inequalities and every one of the 19 recurrent transfer types observed in the exhaustive marked mass-20 tree. The latter observations are NOT used as an all-length theorem.

The ordinary pose-pair relation and the provisional protected-token relation leave a finite set of possible transfer poses. The exact 69 remaining poses which violate this potential are listed under `unproved_bad_transfers` in `dcv_conditional_confinement_optimized.json`. If all 69 were proved impossible, every transfer inequality would hold. The protected relation itself still needs an independent implementation replay before it can be used as a certified premise; alternatively include its 80 additional excluded bad poses in the required hypothesis.

Apply the same potential to all four rotated coordinates. The arithmetic witness gives core-position margins at most 9 and residual-black margins at most 13 from the initial black coordinate extrema, at packet boundaries. Bounded packet lengths also bound every intervening read position. Hence the entire active board and trajectory are confined to a fixed finite box (the unchanged initial debris is finite as well).

Finally D adds no black cells, each C adds three, and each V adds four. A confined finite board cannot support infinitely many C or V operations. An eventual pure-D tail has nonzero displacement (1,1) per macro and cannot be confined. Therefore the stated transfer-exclusion hypothesis would exclude every infinite finite-support D/C/V tail.

This reduction permits all existing finite recycling controls, including DCCCV, DDCDCDCDV, and DCVCCVV. It does not assert a fresh black input at every V, nor a monotone scalar black mass.

The fully independently checked sufficient hypothesis consists of 149 bad transfer poses after the ordinary relation. The provisional protected relation partitions these into its 80 excluded poses and the 69 explicit remaining targets. Neither subset is silently assumed proved.

## Signed refinement, 2026-10-23 00:08 UTC

The corrected anchored-patch batch now independently excludes 22 of the 69 residual targets. The auditor rebuilt all 69 finite graphs from literal complex-coordinate traces, verified every target tuple, and independently exhausted all 22 negative graphs (52,438,714 reached states in total). The exact removed original indices are 6,8,9,10,11,13,25,29,32,37,38,57,58,59,60,61,63,64,65,66,67,68.

The same arithmetic potential and margins therefore require only the 47 targets listed in `dcv_conditional_confinement_anchored47.json`. The source-patch model retains exact fixed source-context colors and exact near-patch poses; excursions outside the patch may return arbitrarily through any geometrically possible boundary port. Exhaustive no-hit reachability is an all-length exclusion. An abstract hit is not a physical witness.

Independent audit: `../audits/replay_dcv_anchored_v2_independent.py/json` and `../audits/protected_patch_replays/`. Discovery files: `dcv_anchored_transfer_v2/manifest.json`. The old version-1 generalized batch had a target-heading normalization error and is explicitly withdrawn for nonzero target headings; it is not used here. This reduction still does not establish D/C/V exclusion or the universal highway conjecture.

### Further signed refinement, 2026-10-23 00:13 UTC

The full24-cell VC source patch independently excludes original cases45–56 and69 as well. The35 signed exclusions leave exactly34 requirements in `dcv_conditional_confinement_anchored34.json`; the same original integer potential and margins9/13 apply unchanged. The full-VC audit reconstructs the literal graphs and explicitly exhausts1,999,527 reached states, independently of the symbolic BDD search. See `../audits/replay_vc24_transfers_independent.py/json`.

The earlier22 exclusions also have independently signed4–9-cell replacements requiring40,041 reached states total, in `dcv_anchored_transfer_min/` and `../audits/replay_minimized_dcv_transfers_independent.py/json`. These are smaller proofs of the same claims, not extra exclusions.

## Signed refinement at 2026-10-23 00:28 UTC

The source-union-target patch invariants for original indices 27 and 34 have independently passed literal model reconstruction and a separate C++ symbolic inductiveness checker (audit GA). Thus 37 of the original 69 transfer exclusions are now proved, leaving 32, recorded without changing the original potential in `dcv_conditional_confinement_anchored32.json`. The frozen new 38-row auxiliary relation `dcv_anchored_signed38.tsv` contains these 37 and the original off-list DC upper-output case; the older signed36 file is unchanged.

The counted protected-kinematic theorem (audit FX) independently excludes counts 0,1,2,3 for all original69 tuples. Every remaining transfer would therefore require at least four C macros from source start to target start. Counts at least four remain unexcluded. No D/C/V finite-tail or global mixed-K theorem is asserted.

### Signed companion refinement at 2026-10-23 00:34 UTC

Cases26 and30 are now independently signed via exact untouched-source-output flags and a canonical XOR/clear inductive checker (`../audits/source_flags26_30_independent.json`). Only already signed clauses25 and34 are needed as applicable on-list companion dependencies. Thus39 of69 are excluded,30 remain; see `dcv_conditional_confinement_anchored30.json`. `dcv_anchored_signed40.tsv` freezes these39 plus the off-list original control. No unsiged mutual induction premise is used for these two.
