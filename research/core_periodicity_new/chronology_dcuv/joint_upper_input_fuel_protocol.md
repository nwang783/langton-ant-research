# Joint upper-input fuel, distinct from individual freshness

Status: analytic least-gap protocol reviewed by the independent auditor on 2026-10-23 at 02:19 UTC. No complete finite certificate family is available. DCUV tail exclusion remains open.

## Candidate conclusion

For a finite-support marked DCUV factor with a fixed initial packet boundary, every U, UC or UCC packet consumes at least one identity from the initial residual set through one of the three local input cells

`T = {(-1,4), (0,2), (0,3)}`.

This does NOT assert that any particular member of T is always initial. Identities are those of the signed ordered residual ledger: remove all inputs first, then install a fresh identity at each RAW output, including the U input/output overlap at (-1,2).

If proved, the conclusion bounds the number of U-family packets by the number of initial residual identities. No identity can pay twice because consumption removes its old identity. Consequently only finitely many U macros occur. After restarting beyond the final U macro, the signed DCV finite-tail theorem excludes an infinite remaining tail. This is a conditional route to DCUV finiteness, not a present DCUV theorem.

## Least-span bad event

A bad consumer has all three T identities born at earlier packets rather than at the fixed factor entry. For each consumed identity, take its actual last producer. Let s be the earliest of those three producer indices, and t the consumer index. Pick a T identity whose last producer is s as the protected anchor q. Choose a bad event with minimum t-s.

Every strictly intermediate complete context avoids q, by the signed residual-token protection lemma. Normalize the source packet at the origin with north heading. Its type, q output slot, target type, target pose, and target input slot give one of the finite aligned producer-to-T rows. A row already forbidden by the signed ordinary/protected kernel is impossible. The remaining rows form the finite outer-event universe.

The normalized family is not a family of individually forbidden transfers. Each member means: no protected source-to-consumer factor at this alignment can have all three target T identities produced at or after the source boundary.

## Finite abstraction

At any retained watched cell, keep the fused state:

- 0: white;
- 1: black with unknown origin (including an initial identity);
- 2: black with outer-source origin;
- 3: black with internal origin.

Initially, precisely retained outer-source RAW outputs receive state2. Other retained source-context cells receive their literal post-RAW color,0 or1; cells outside the source context may start either0 or1. All watched cells lie in the retained color patch.

For a packet transition, test the literal complete-context entry colors. A complete-context touch retires the old origin. Then a RAW residual output installs state3, while other touched cells receive their literal post-RAW color with unknown origin. This remove-then-install order includes recycled U cells. Unseen OUT packets miss the entire patch and preserve every retained state; arbitrary OUT reentry remains an overapproximation.

At a strict intermediate U-family packet, the family may reject the transition only when all three local T cells are watched and have known origins2/3. The three actual producers then lie at or after s, so this consumer's earliest-last-producer span is less than t-s. If any input is untracked or unknown, that joint-family rule may not reject it.

At the outer goal, require all three T cells watched and all three origins known. This is the tested bad event, not a rule rejecting that event. The protected anchor remains an outer-source identity up to the consumer. Unlike the individual-freshness model, the joint model does NOT reject an outer goal merely because a particular input has internal origin.

A complete family of no-hit invariant certificates, all generated against this SAME joint-event induction semantics, would exclude a least-span bad event and prove the fuel conclusion.

## Target-prefix scope

U+M11 is a literal prefix of UC/UCC+M11. The source and strict intermediates must stay actual complete packets. The outer consumer may be tested by its U context prefix; no artificial non-C successor is required at the shortened U endpoint. Thus certificates for all base-U aligned upper inputs can cover the matching UC/UCC target events under the audited uniform prefix interpretation. Source extensions are NOT identified: their outputs, end poses and histories differ.

## Current artifacts and limits

- `add_resource_joint_upper_fuel_fused.py`: conditional model generator.
- `upper3_post_D_tests/joint4_fused.*` and `joint6_fused.*`: two source-D probes. Both have abstract witnesses. These do not refute the conclusion and do not certify it.
- `add_resource_upper_freshness_fused.py`: separate, stronger INDIVIDUAL freshness semantics. Do not mix its clauses or goal rules with this joint model.
- `hypothesis_U_upper3_post_dccc.tsv`: the 1188 aligned rows used to check geometric completeness. Its individual-freshness name does not grant its rows the joint semantics automatically; each model explicitly declares which event family it uses.

The all-ten profile and the post-DCCC nine-type profile remain immutable. Any eight-type recurrent profile must wait for the separately checked literal DCC/DCCC boundary theorem, rather than importing the old DCV pruning.
