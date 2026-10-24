# Six-C first contacts reduce to one U-to-V endpoint gate

Status: author exact reconstruction PASS, 2026-10-23 14:54 UTC. This reduces a concrete first-contact history obligation; it does not exclude the final gate or bound global fuel.

## Canonical geometry

Use the independently signed first-contact horizon1412: at a chronological first corrected-center self-contact, take the OUTGOING earlier chord and INCOMING later chord. Their parameters satisfy0<=s<1 and0<t<=1. At entry C-clock gap6, the strict angle condition is alpha(first)<alpha(last), and the later heading is S relative to earlier N.

Independent exact parallelogram bounds, sector and rational-determinant tests leave eight geometries:

- firstV, laterD orC at(0,0,S), s=0;
- firstU, laterD orC at(0,0,S), s=0;
- firstU, laterD orC at(0,2,S), s=1/2;
- firstU, laterV at(0,2,S), s=0;
- firstU, laterV at(0,4,S), s=1/2.

Every later parameter is t=1. There are no parallel cases in the strict angle ordering, so no collinear family is omitted. These bounds are derived from contact parallelograms, not guessed spatial or word-length cutoffs.

## Seven concrete history obstructions

For each case except the last, a fresh residual output of the source V/U base lies in the later atom's WHITE/core complete context, rather than an input. That identity must retire STRICTLY BEFORE the later atom. It cannot silently become core.

Enumerate its possible first consuming base at source C-age0..6. The actual full producer is one of V/VC/VCC or U/UC/UCC. Source and target full input/output roles, signed HB/count-five clauses, source completion, sector and heading are all retained. Any consuming BASE chord with a CLOSED contact with the source chord already gives an earlier nonadjacent contact, forbidden for the chronological first contact. All eligible such contacts occur at age3,5 or6 and are nonadjacent.

The remaining necessary endpoint checks are exact and unbounded in zero-run length:

- At age6, there is no C left before the later S-heading atom. Test exact zero-C displacement in the D/V/U semigroup(1,1),(1,3),(0,4) in that heading.
- At age5, there is one C left, taking W toS. Work from the consuming BASE exit, not its full-tail endpoint. Any zero-C W prefix has displacement(-dW-3vW-4uW,dW+vW), that C adds(-1,0), and any zero-C S suffix adds(-dS-vS,-dS-3vS-4uS). The X equation bounds dW,vW,uW,dS,vS by B=-deltaX-1; solve the remaining uS from the exact Y equation modulo4. This is a complete finite arithmetic test of that one-C geometric overapproximation, not a bounded path search.

For internal C targets, a consuming full packet is allowed to finish AFTER the target cut. The BASE-exit zero/one-C tests remain necessary even then, because they count only actual C atoms before the target. We conservatively permit the C to stand alone and arbitrary zero-C ordering, admitting more paths than the full grammar. No no-hit inference depends on a forbidden internal-tail completion assumption.

For each of SEVEN cases, at least one forced source output has NO timely noncontact clearer after these tests. Hence that case necessarily already had an earlier closed contact and cannot be the first contact. The specific hard outputs are all in the JSON. The complete check comprises13,524 full-source/input/age tuples; no fresh root, beta cost or support-mass decrease is inferred.

## The one remaining gate is genuinely different

Only firstU(0,0,N), laterV(0,4,S) remains. The center contact is the midpoint of U's chord and the endpoint of V's chord. The later complete context touches ONLY the two source outputs

- source(-1,2) at the later V's selected input(1,2);
- source(0,1) at its lower input(0,3).

Thus neither old identity is forced to retire BEFORE the final V; they may retire AT it. The strict-clearance argument used for the other seven cannot be applied to this case.

All eighteen full-source/target-tail old-cohort queries are explicit. Both old identities survive the individual HB/count-five tests for source U orUC and target V,VC orVCC. Source UCC's old selected identity is HB-excluded, but this alone does NOT eliminate that whole geometry because replacement may be possible for V/VC targets. These are necessary static eligibility tests, not actual chronological realization or a renewable cycle.

One particular tail combination IS excluded: sourceUCC to targetVCC. TargetVCC requires both inputs of produced age>=5. Any replacement of either source output would have birth clock>=2, because its old produced identity cannot retire at age0/1; at goalclock6 that replacement has age<=4. Hence both inputs must still be the original old source identities. The selected one is signed HB-excluded for UCC, contradiction. This small corollary neither eliminates sourceU/UC toVCC nor UCC toV/VC.

## Scope

With the signed horizon, any chronological first center contact of gap6 must have this U-to-V endpoint geometry, with the stated unresolved origin alternatives. There is no factor-first exemption or initial-age loophole in the seven exclusions because each tracked identity is a genuine fresh source output. No claim is made that the surviving gate is attainable, impossible, or repeatable. Other first-contact gaps and global capture remain separate.

Replay: check_six_C_first_contact_reduction.py and chronology_dcuv/six_C_first_contact_reduction.json. Inputs bind the signed canonical horizon, literal masks, protected HB, cap-five counted relation and corrected-center geometry. No new closure or larger ant search is run.
