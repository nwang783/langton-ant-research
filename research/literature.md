# Langton's ant: primary-source research map

Checked 22 October 2026. This is a research map, not a proof of the highway conjecture. Public preprints, formal artifacts, computations, and independently checked deductions are distinguished below. Source PDFs and extracted text are in `sources/`; upstream repositories were read, not modified.

## 1. Exact target and logical distinctions

The target is the square-grid two-state ant, reading its current cell, turning right on white and left on black, flipping the cell, and moving one unit. Initially only finitely many cells are black. Every such state, with arbitrary ant pose, should eventually have the **specific standard blank-start 104-step turn/read word**, modulo phase and rotation/translation, repeated with diagonal displacement of two units in each coordinate. Stationary debris may remain behind: whole-board equality to a translate is not the claim. Exchanging left/right is reflection, not a distinct conjecture. Entry-time numbers 9976/9977/9978 require checking indexing conventions.

Do not replace this by any of the following weaker assertions: unbounded trajectory; eventual escape from every finite set; some periodic drifting trace; a 104-step observation recurrence without identification of the standard word; or a conditional classification of already periodic tails.

## 2. Established sources and their useful boundaries

### Unboundedness and finite confinement

* Bunimovich and Troubetzkoy, *Recurrence properties of Lorentz lattice gas cellular automata*, Journal of Statistical Physics 67 (1992), 289–302. The classical ant cannot have a bounded visited set, even on arbitrary initial backgrounds. The corner argument is also explained in [Gale's 1993 article](https://ics-websites.science.uu.nl/docs/vakken/b2nb/stuff/The%20industrious%20ant%20-%20D.%20Gale%20-%201993.pdf) and [Gale–Propp–Sutherland–Troubetzkoy, 1995](https://www.math.stonybrook.edu/preprints/ims95-1.pdf). This does not prove finitely many returns to each finite set. The historical name in Gale is Cohen–Kong, not Cohen–Kung.
* Kossi Roland Etse, [*How Long Can The Escaping Ant Be Confined?*](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.49), MFCS 2026, LIPIcs 386, article 49, published 21 August 2026; [preprint](https://arxiv.org/abs/2606.26677), 25 June 2026. Proposition 2 forbids repeated **color configurations** within a confined trajectory segment, not merely repeated full states. Consequently a connected domain with d cells has an exponential escape bound. Theorem 5 gives the square bound (n+1)!, and exact strip results include 6(n−1) for 2-by-n and 10n−4 for 3-by-n. Fixed-height strips have polynomial bounds. These concern confinement before first exit, not later re-entry or highway capture.

Transferable ingredient: the non-repetition proof uses parity of visits and incompatible extreme corners. The missing global lemma would need to charge **re-entry**, not merely prove another first-exit bound.

### Computation and undecidability

Gajardo–Moreira–Goles, [*Complexity of Langton's Ant*](https://arxiv.org/abs/nlin/0306022), Discrete Applied Mathematics 117 (2002), 41–50, DOI [10.1016/S0166-218X(00)00334-6](https://doi.org/10.1016/S0166-218X(00)00334-6); arXiv posting 13 June 2003. Finite circuit gadgets establish P-hardness of prediction/cell visitation. Their universal-computation and undecidability constructions use infinite, finitely described backgrounds. They do **not** prove undecidability for arbitrary finite black perturbations. The conclusion explicitly leaves that finite-support issue open and observes that the highway conjecture would imply a positive decidability result.

Transferable ingredient: compose gadgets only after checking the exact exit interface and preventing return. Complexity is a warning against guessing short uniform transients, not an obstruction to proving eventual regularity.

### Symbolic traces and hyperbolic geometry: use with an audit flag

Anahí Gajardo, [*A symbolic projection of Langton's Ant (Extended Abstract)*](https://dmtcs.episciences.org/2312/pdf), DMTCS AB(DMCS), 2003, 57–68. The finite-word realizability criterion is exact: at consecutive visits to any one cell, the read/turn symbols must alternate. The paper gives an arc-group presentation and studies the cancellation congruence R^k=L^k=1 on regular k-face/d-valence tessellations. Its nested prime-loop factorization is a potentially useful alternative to local-energy arguments.

**Important independent audit warning:** page 65 states both H44⊂H45 and a four-visits-per-cell bound for the hyperbolic model. A direct square-ant replay and an independent Möbius-model computation produced a small apparent conflict with the four-visit claim. Therefore this project is **not using** that claim or its putative consequence, convergence of the free-product stack to a boundary ray, as a proved lemma. See `literature_work/symbolic_lift_audit.md` and its reproducible witness. Resolving the exact hypothesis/convention or identifying an erratum is required before transfer. The elementary trace criterion does not depend on this issue.

### A genuine finite-support theorem on other tessellations

Gajardo–Goles–Moreira, [*Generalized Langton's Ant: Dynamical Behavior and Complexity*](https://www.dim.uchile.cl/~anmoreir/oficial/langton_stacs.pdf), STACS 2001, LNCS 2010, 259–270, DOI [10.1007/3-540-44693-1_23](https://doi.org/10.1007/3-540-44693-1_23), Theorems 4–5: on planar equal-face-size graphs with vertex degree at least five and square or larger faces (or degree at least six and triangular faces), the future is constrained to a tree of tiles, and finite-support starts eventually have periodic drift of period (k−1)(k+1). Square-faced hyperbolic graphs therefore have period 15. This is not the degree-four square lattice. The conference paper states the result but gives only a short geometric development, so its full proof is not independently reconstructed here.

Useful obstruction to a naive transfer: assuming that stated finite-support theorem, a hyperbolic realization of the nonconstant standard 104-periodic square-ant word cannot have finite support. An eventual 15-periodic word that is also 104-periodic must be constant, because gcd(15,104)=1. Thus finite square support does not become finite hyperbolic support even in the desired highway regime. The correct finite-fuel variable must retain projected-site fibers.

## 3. New public finite-support work: useful, but separate from peer-reviewed status

These sources were already present in the recovered research handoff. Their scope was checked against current statements; this literature pass is not a fresh independent rebuild of every formal artifact.

### Hao Ke: core repository

[Repository](https://github.com/kehao95/langtons-ant-core), read at commit `22e0c9edcc566a4c2f7a9bf92f5cd05c19199617`.

* `one_black/PROOF.md`: all positions of one initially black cell, not just a bounded box. Blank-prefix encounters reduce to finitely many leaves and future encounters to 22 affine frontier channels. The 13 October 2026 fixed-standard-word bridge strengthens the conclusion to the actual canonical trace; `one_black/lean/StandardTrace.lean` is explicit about this.
* The integer clock gives a strictly increasing potential on finite-support states and decidability of reaching a **specified complete state**. It does not decide local visitation or prove capture. Its exponential weights make it unsuitable as an unexamined compactness/properness substitute.
* `four_cell_port/PROOF.md`: a sharp half-plane escape restriction with at most three black cells, and a four-cell gate. Arbitrary finite protected prefixes can be extended, by adding four sufficiently far cells, to a highway-forming state. This changes the input and is not a proof that the original input succeeds.
* Guarded scattering trains compose arbitrarily many **compatible protected gadgets**, including exact wake-readback treatments. They do not prove stability under an arbitrary finite cluster. This distinction matters for any proposed induction on the number of defects.
* The public all-age one-bit highway-stability reduction has 739 cases, but its numerical certificate was absent in the inspected upstream package. The recovered private continuation contains a reconstructed certificate. Public theorem claims and private reconstruction should not be conflated.

### Two initially black cells

imfinn, [revised two-cell theorem](https://github.com/imfinn/langton-two-black/blob/95e896e3035e992e48ce9d28a5ded8568c86e835/paper/TWO_BLACK_CELLS_REVISED.md), revised 5 October 2026; repository commit `95e896e3035e992e48ce9d28a5ded8568c86e835`.

The stated Lean theorem covers at most two initially black cells with no distance bound, through one- and two-corridor reductions. Its formal terminal predicate gives repeated position/heading/read-color observations with period 104 and diagonal drift; it does not by itself identify the particular standard word or prove minimal period. A separate native check compares the canonical word. `TRUST.md` records 61 native-generated axioms and the usual three Lean axioms, and explains the compiler/native-code trust boundary. No independent clean rebuild was performed in this literature pass.

### Conditional periodic-tail restrictions

[Atharva Jillhewar's repository](https://github.com/Atharva12456/langtons-ant-highway), pinned in the recovered work at `76a7e234e577d992d086c204c3dea00ae72cf10a`, gives residue/signed-growth restrictions and machine-assisted exclusions of classes of periodic candidates. Later closure work in the core repository rules out additional low-growth possibilities. These are valuable conditional classifications but do not establish entrance into a periodic regime. Do not silently promote “every candidate in this class is excluded” to “the standard highway is inevitable.”

## 4. Counterexamples to overly broad variants

* Gajardo–Lutfalla–Rao, [*Ants on the highway*](https://arxiv.org/abs/2409.10124), posted 16 September 2024; Natural Computing 24 (2025), 497–509, DOI [10.1007/s11047-025-10018-9](https://doi.org/10.1007/s11047-025-10018-9). Highway multiplicity can be unbounded across generalized rules, and one nonclassical rule has infinitely many highways. Very rare computational outcomes are evidence that naive random tests can miss behavior, not evidence against the classical RL conjecture.
* Victor Lutfalla, [*Sideways on the highways*](https://arxiv.org/abs/2505.05426), 8 May 2025. Finite seeds for multicolor rules LLRRRL and LLRLRLL yield horizontal highways, growing rectangles or cones, and infinite highway families. The paper labels its constructive arguments as proof sketches. These examples refute a universal claim across arbitrary multicolor rules, not the classical two-color rule.

Transferable ingredient: build exact local widgets with a global non-interference invariant. The difficult part for classical RL is showing that an arbitrary seed decomposes into such widgets.

## 5. What the OpenAI release actually supports

The [official announcement](https://openai.com/index/sharing-ai-progress-in-mathematics/) is dated 6 October 2026. The [primary repository](https://github.com/openai/math) currently describes 719 manuscripts in 372 problem families, with approximately 4,000 problems posed during the evaluation, and about three hours of ChatGPT Pro thinking compute per result on average. Approximately 42% have a top-line formalization. These counts are not 719 independently accepted resolutions of famous open problems, and the repository explicitly distinguishes verification statuses. The index does not identify a Langton-ant solution.

Two released abridged reasoning summaries were actually read, rather than using the announcement as motivational evidence:

* [Characteristic-two direct finiteness](https://github.com/openai/math/blob/main/reasoning_traces/kaplansky-direct-finiteness-characteristic-two.pdf): preserve precise failed-route obstructions; switch between proof and counterexample search; use one algebraic defect to organize reductions; replace a heavy geometric route by a more local combinatorial/Euler certificate; repeatedly audit gluing, independence, and finite-model obstructions. The release describes a proposed proof, not an independent verification performed here.
* [Semidefinite-threshold NP-hardness](https://github.com/openai/math/blob/main/reasoning_traces/basic-semidefinite-threshold-np-hardness.pdf): fix exact quantifiers and conventions first; attack gadgets with explicit cheating strategies; isolate a local decoder/slice bottleneck; establish uniform parameters before global composition; use distinct limiting inequalities rather than informal “small enough” choices.

Concrete transfer: every candidate ant proof should expose a named closure lemma, an adversarial test that could refute it, and a small independent verifier where finite enumeration is claimed. Neither release supplies a reason that extra elapsed reasoning time alone guarantees success, nor permits importing probabilistic independence into a deterministic ant orbit.

## 6. Precise next lemma targets, ordered by relevance

1. **Arbitrary-cluster scattering closure.** Given a canonical highway plus finitely many forward virgin defects and the complete old wake, prove a well-founded decrease through scattering events, or exhibit a counterexample to the proposed decrease. Existing one-bit/guarded-train results do not supply this closure.
2. **Finite-fuel macro boundary.** For the exact five-macro admissible component, show every infinite nonstandard macro ray creates infinitely many globally first-left projected sites. Existing all-white completion and finite-seed trace equivalences make this statement meaningful; a local marker count is insufficient if the path can revisit old wake.
3. **Return charging from confinement.** Strengthen the corner/parity argument to a charge for distinct returns through an expanding contour, retaining the full interior readback. First-exit bounds alone cannot close this route.
4. **Repair the symbolic geometric transfer.** Independently derive a valid bound or obstruction on repeated reduced-prefix states in C4*C4, with projected-site parity retained. Do not rely on the four-visit claim until its audit is resolved. Even a genuine lifted escape theorem would still need the finite projected-first-left hypothesis to force the boundary ray to be standard-periodic.

All four are proof targets, not established results. No source located here establishes the full finite-support standard-highway conjecture.
