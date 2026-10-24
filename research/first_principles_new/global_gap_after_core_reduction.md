# The exact remaining global gap after the core reduction

22 October 2026. Coordination note summarizing proved reductions, not a proof of the highway conjecture. All affirmative claims below point to independently reviewed derivations in this folder.

## An equivalent two-part target

For every standard square-ant trajectory from a finite black seed, the full highway conjecture is equivalent to the conjunction of:

A. Its limiting reduced free-product core is eventually periodic.
B. Every finite-seed translating-periodic turn tail is the standard104 tail, up to cyclic phase and physical rotation.

The forward implication is immediate from standard104. For the reverse implication, A gives eventual translating periodicity by `periodic_core_decoration_stabilization.md`, with no extra assumption that decorations stabilize; B then selects standard104.

Thus decoration stabilization is no longer a third independent global task. The remaining tasks are core attraction and periodic-front uniqueness. Neither is proved here.

## Effective content of periodic-front uniqueness

`fixed_core_realizability_decidable.md` gives a terminating finite decision procedure for each supplied periodic core q. It eliminates arbitrary decoration lengths and arbitrary temporal periods using seed-independent eventual bounds and a complete-crossing-history splice. There are effectively finitely many primitive translating turn tails over q.

Consequently periodic-front uniqueness restricted to any finite list of core words, or to any supplied bound on core stage period, is decidable. The mathematical search bounds are enormous and have not been used for a complete catalog. No global bound on core period is known.

Even the assertion that the standard reduced core has no nonstandard full decoration is still a classification obligation, not a consequence of the bridge alone.

## Geometric sufficient conditions now available

* A core in any fixed-width strip, with uniformly bounded longitudinal retreat, forces a translating-periodic full tail. For non-axis strips the new finite-cap route directly bounds all decorations. For axial strips the complete-row-history route handles unbounded proposed longitudinal decorations.
* An axial core in a fixed-width strip with uniformly bounded TOTAL root events per transverse row also suffices, without assuming retreat.
* Eventual periodicity of the core satisfies the required conditions and yields the exact equivalence with full translating periodicity.

These are implications, not proofs that arbitrary finite-seed cores satisfy the hypotheses. In particular, physical unboundedness of the core does not imply Euclidean transience, strip confinement, bounded retreat, or an asymptotic direction.

## What the new endpoint ledger does and does not control

`one_sided_cap_forward_depth.md` proves an unconditional historical extent envelope: a finite core prefix of spans Dx,Dy encloses its complete physical read history in its bounding box enlarged by m+6Dy+67 horizontally and m+6Dx+67 vertically, where m is the finite mass at the initial permanent cut.

Under bounded northeast core retreat, all east/north G depths are uniformly bounded. Future reads avoid the strict southwest quadrant behind the core. The only remaining possible unbounded archived accesses are west/south arms. Without an oblique-strip or related supplier restriction, those arm lengths remain uncontrolled.

The envelope concerns historical size, not current head-to-root distance. It gives no transience or bounded-retreat conclusion.

## Key safeguards against circular reductions

* Proper convergence in the free-product boundary is not Euclidean escape.
* Finite physical black support does not imply finite autonomous lifted support; even a standard104 front generates new first-black lifted cosets forever.
* Completed G fingers restore their strict interior colors, but not necessarily token ancestry. Color restoration cannot be treated as deletion of all causal history.
* Endpoint particle ranks apply only when other events are excluded from the relevant whole region. A statement about the cut line alone does not prevent remote barrier repair.
* Complete crossing histories, including every return, are required for splicing. Matching first arrivals is not sufficient.
* A finite-state argument must first bound the relevant stored information. The two backward arms are not automatically finite-state merely because the core has bounded northeast retreat.

The principal source files are `periodic_core_decoration_stabilization.md`, `axial_core_periodicity_bridge.md`, `bounded_core_dwelling.md`, `fixed_period_core_uniform_bounds.md`, `fixed_core_realizability_decidable.md`, and `one_sided_cap_forward_depth.md`.
