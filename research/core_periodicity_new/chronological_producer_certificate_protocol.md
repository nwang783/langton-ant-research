# Chronological producer certificates for protected packet pairs

Status: analytic protocol reviewed by the independent auditor. Numerical generators require independent reconstruction before any new finite family is signed. This is a conditional proof method, not a solution of the finite-seed highway conjecture.

## 1. Family induction

Fix the recurrent packet alphabet D, DC, V, VC, VCC, their literal RAW words and actual M11 right contexts. Let H be a finite family of normalized output-to-input protected-pair tuples. A tuple specifies source type A, target type B, the target pose relative to A, and a source residual output q which is a target residual input.

Assume some H occurrence exists in an actual recurrent packet tail. Choose one with minimum packet-index gap over ALL tuples in H and all occurrences. Strict intermediate packets avoid q in their complete RAW+M11 contexts by the audited residual-token lemma. Every H occurrence whose endpoints lie between the outer endpoints and whose gap is strictly smaller is therefore absent. This supplies the only induction hypotheses used below. In particular, a source-to-outer-target occurrence has equal gap even if its distinguished output differs from q; it must never be removed by H.

Each tuple has a separate finite overapproximation of these least-gap histories. If every tuple's accepting set is unreachable, the hypothetical least-gap occurrence is impossible and every row in H is excluded. Previously signed forbidden relations can be used freely within their exact scope.

## 2. Colored patch and outside collapse

Fix a finite set P of physical cells. A finite head-pose set contains every sector-compatible pose at which any recurrent packet's complete context meets P. A pose outside this set is OUT. At a finite pose, a packet imposes its literal first-read requirements on P and XORs its RAW odd-read set on P. All other colors remain unchanged.

The initial cube is the actual source-context first-read constraint, translated by source RAW parity to the post-source boundary. The accepting action checks the target's complete entry guard. Intermediate actions avoid the designated q and satisfy the signed source/intermediate/target restrictions.

A real OUT packet neither reads nor changes P. Collapse arbitrary outside excursions by preserving the patch and allowing every finite reentry pose which has an outside predecessor. This deliberately permits impossible excursions; it cannot omit a physical one.

## 3. Forward producer labels

Choose watched cells inside P. At each watched cell retain either unknown or a producer descriptor: packet type, output slot, heading and an explicit outer-source-origin tag. The exact producer pose follows from the physical watched cell minus its rotated local output coordinate. Initial labels identify only genuine outputs of the outer source. Every complete-context touch clears the old label; a current packet output then installs its new INTERNAL producer descriptor.

Consequently any surviving descriptor certifies a black cell immediately after that producer's RAW and complete-context avoidance since that producer. When a packet consumes the watched cell as a residual input, the signed protected producer-to-consumer relation applies. H may additionally apply at a strict intermediate consumer, because the producer was the outer source or later. At the outer target, H applies only to INTERNAL-origin labels. ALL outer-origin labels are exempt there, even if they denote a different output from the designated q. Internal producers which revisit exactly the outer source geometry remain internal.

OUT preserves labels because watched cells lie in P. Unknown labels are always permitted and impose no producer relation.

## 4. Signature quotient

For a frozen base model, H and signed relation, list every modeled input-consuming transition, not merely reached transitions. Two internal producer descriptors may share a class if their rejection truth values coincide on every such transition. The signature includes the outer-goal induction exemption. Outer-origin descriptors are kept separate. Empty-signature internal descriptors may be forgotten as unknown.

Clearing depends only on the current physical context, and installation only on the current packet/output pose. Thus the signature equivalence is a transition congruence for the information inspected by the model. Every class certificate records its exact physical producer members, exact rejection signature, output-to-class map, frozen base hash and frozen H/signed hashes.

If H is later weakened while keeping the old partition, reject a class only when EVERY member is still forbidden. This is a conservative coarser model. It is not legitimate to reuse an old signature merely because its class identifier is unchanged.

## 5. Backward target-input flags

Alternatively, reverse the exact colored graph. Its start is the target-entry guard cube; its goal is the original post-source cube. XOR reversal uses the transformed guard v XOR (flip AND mask), and all OUT identity transitions are reversed as well.

A flag for a target residual input cell in P starts at1 and certifies that all already-reversed later strict intermediate complete contexts avoided it. At a reversed intermediate producer, live1 and the target's input-black condition supply the protected producer-to-target premise. Signed clauses always apply; H applies because this producer is strictly after the outer source. Clear flags on every complete-context touch. Never H-filter the outer-source goal.

## 6. Forward prophecy product

The same suffix information can be intersected with the forward producer model relationally. Initialize each suffix bit unconstrained and require1 at the outer target goal. If a strict packet misses its flagged cell in the complete context, preserve the bit. If it touches the cell, require the before-bit0 and permit after-bit0 or1. This is exactly the forward relational reverse of backward clearing.

Producer-to-target clauses test the AFTER-bit: after1 certifies avoidance by all later strict intermediates. A forbidden pair removes that branch. The outer source is not a transition in this forward model and is never H-filtered. OUT preserves every prophecy bit. Every flagged cell must belong to P.

## 7. Numerical certificate obligations

A computational signoff needs independent checks of:

1. Literal words, endpoints, first-read guards, RAW parity, residual slots and complete-context footprints.
2. Every physical frame normalization and sector restriction.
3. Exact frozen H/signed membership and the least-gap scope of each predicate, including every outer-origin goal exemption.
4. Producer initialization, clearing, installation, quotient memberships and signatures.
5. Reverse/prophecy transformations and each relational branch, when present.
6. Initial-cube containment in the supplied invariant, closure under EVERY transition and OUT identity, and disjointness from every accepting guard.
7. Same-final-H no-hit coverage for every proposed unproved family row. Capped searches, bounded absence and abstract witnesses do not discharge rows.

The reset-BDD verifier checks inductive closure rather than trusting search termination or state counts. Counts and depths are diagnostics only. Independent literal feasible controls must remain admitted; observed controls are not silently treated as forbidden hypotheses.
