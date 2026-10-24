# Additional primary universality source

Source: Diego Maldonado, Anahi Gajardo, Benjamin Hellouin de Menibus and Andres Moreira, *Nontrivial Turmites are Turing-universal* (2017), arXiv:1702.05547v1.

Primary text: https://arxiv.org/html/1702.05547
PDF: https://arxiv.org/pdf/1702.05547

The introduction and Section 5 explicitly present their strengthening of the 2002 construction using a periodic background with finitely many input perturbations. This is not a claim that 2017 first suggested periodic backgrounds: the indexed primary-text excerpt of the 2001 Complexity article, https://www.dim.uchile.cl/~anmoreir/oficial/langton_compx.pdf , already describes adding stop marks to replace the trapezoid by a periodic tiling. Direct PDF retrieval of that earlier article currently returns 403, so its detailed construction has not been independently rechecked here. This remains infinite physical support, not the all-white exterior in the highway conjecture. Section 1 explicitly separates that conjecture from infinite-configuration universality.

Section 2's wires are single-use. Section 5 explains that construction cells are visited at most twice. Therefore this is not a reusable finite circuit or a finite hardware-growth mechanism.

Section 4 proves circuit-based P-completeness of bounded-time cell visitation. Its encoding uses binary time, but the authors explicitly measure complexity with respect to the numerical time value, so do not silently restate the upper bound as polynomial in binary input length.

Research implication: the later stronger simulation still does not provide the missing finite-support compiler. A renewable circuit, or a constructor producing fresh circuitry as needed, remains an additional obligation.

## Quantitative obstruction to transferring this construction to finite support

Added 2026-10-22, after the global two-visit theorem was independently audited. The primary HTML text was rechecked directly, particularly Section 1 (the RL specialization), Section 2 (single-use wires), and Section 5 (at most two visits to each construction cell): [primary article](https://arxiv.org/html/1702.05547).

The exact global theorem in `../core_periodicity_new/higher_reuse_count_bound.md`, Section 5, gives

    t <= 90 m^2 + 348 m + 326 <= (10m+20)^2

for any t-read classical-ant prefix with at most two reads per physical cell, starting from m black cells. This theorem is specific to the two-color classical ant; it is not being asserted for all Turmites.

Let w be a finite prefix of the classical-ant specialization of the 2017 construction, and let f(w) count its distinct first-read-L cells. Copy those cells, and only those cells, into an otherwise white board. Exact first-visit/alternation induction reproduces w, so the theorem applies with m=f(w). Consequently

    f(w) >= max(0, ceil((sqrt(t)-20)/10)).

Thus an infinite legal trajectory retaining this at-most-two-visit architecture necessarily consumes infinitely many initially black physical cells. No finite-support replacement can reproduce its entire infinite turn/pose trace, regardless of how cleverly its finite hardware is laid out. The conclusion also applies after any finite autonomous setup prelude: the board at the end of that prelude still has finite black mass, so an ensuing infinite cap-two tail is impossible.

This is an actual obstruction to preserving the published construction, not just an absence of a published finite-support version. It does NOT exclude a compiler that changes the physical visit pattern, introduces recurring construction work, or uses third-and-later visits. Nor does it disprove the paper's periodic-background universality result, the finite-circuit P-completeness result, or universal computation by a different finite-seed architecture. In particular, finite circuit instances can use increasing finite black mass, entirely consistently with the bound.

Audit checkpoint, 2026-10-22 22:12 UTC: the independent auditor accepted this transfer deduction, emphasizing that m counts the distinct entry-black cells actually read in the chosen interval, not the total infinite background.
