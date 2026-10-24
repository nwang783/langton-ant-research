# Executed exact Presburger read-set and supplied-template controls

2026-10-23 04:13 UTC. Independently analytically and computationally signed on 2026-10-23 04:21 UTC.
No nontrivial growing model is accepted. This is not the general automatic
canonical-template extractor or the ant-to-XOR-graph compiler.

The system already contains libisl0.27 with exact GMP arithmetic. The code
uses the retained ownership-safe isl_exact.py wrapper from the source tree.
No installation  was performed. Resource errors propagate
as errors, not as empty sets or successful certificates.

## Exact read sets

presburger_read_set_solver.py builds the full quantified Euler-count formula
for a finite weighted occurrence graph at A=I, then lets libisl eliminate
all edge-count and connectivity-rank variables. The connectivity witness
assigns integer ranks with the start at zero; each used nonstart vertex has
an incident positive-count edge to a strictly lower rank. This is equivalent
to weak support connectivity and avoids enumerating all vertex cuts.

It includes zero-length walks, all possible terminal vertices, parallel
edge deduplication for existential reachability, flow balance, exact depth,
and both spatial displacement equations. It does not infer chronology.
The right-five control's computed all-depth set is exactly the origin at
depth0 and the four unit-square sites at every positive depth. Two identity
controls also match their all-depth symbolic sets. There are882 additional
literal point checks through depth5.

## Complete supplied-template induction

presburger_template_validator.py checks A=I typed image geometry, accessible
letters, exact read sets, base turn colors AND exact zero-depth output toggle,
all child-frame agreements, complete output XOR equality, and the same finite
root input B for all depths. A nonerasing first-letter-fixed root with image
length>=2 is required before a growing model can be accepted.

Two correct identity templates pass every frame/base/output check, but are
rejected as nongrowing. A forged identity template with no output flip is
rejected by the base-output check. Exact period-two canonical parity boards
for the geometric but illegal R^(5^r) model satisfy all base/output identities
and fail eight child-frame checks. Thus the test distinguishes algebraically
correct flip accounting from actual chronological ant legality.

The input I/O formulas are supplied complete Presburger board relations;
no claim is made that the implementation discovers them. Current controls
have finite fibers. No accepted nontrivial example or general finite-seed
existence algorithm follows from these controls.

Independent replay:553 all-position depth-fiber equalities over38 graph
families,24 template controls, and8 malformed inputs. See the separate
auditor artifact audits/presburger_pipeline_independent.json.
