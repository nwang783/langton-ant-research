# Directed finite palettes characterize translating periodicity, not the global gap

23 October2026. Analytic corollary of the independently accepted exact finite-
front theorem at SHA71628c306bf... . The fixed-board determinism implication
was separately independently checked before this note was frozen. No graph
implementation audit or universal capture conclusion is imported.

## 1. A specified board has one physical future

Use the hypotheses of `directed_palette_finite_front_decision.md`: a finite
supplied palette Sigma, one incoming/outgoing heading, common nonzero drift D,
and a background T periodic along D with known period p. Let m be the exact
front bit count, V=p*2^m, and M the maximum supplied literal block length.
Fix ONE specified finite set of color changes to T.

**Corollary.** If the actual ant admits any infinite Sigma-block decomposition,
its PHYSICAL literal turn trace is eventually periodic with a nonzero drift.
The statement permits completely occurrence-dependent palette choices.

Proof. After the last exceptional fresh input, its exact front state follows
an infinite finite-graph path. There is a finite path from that state to a
cycle. By the exact transition sufficiency proof, following this path and then
repeating the cycle is a genuine literal execution on the SAME supplied board,
not a new board selected for the cycle. The ant's literal dynamics is
DETERMINISTIC, so its future turn word must equal that ultimately periodic
execution. A cycle of k>=1 blocks has displacement kD, which is nonzero.
Retired debris stays present and never affects any continuation in this
architecture. QED.

The chosen periodic macro schedule need not equal the original decomposition:
a single ultimately periodic physical word can have alternative macro parses.
Thus it remains incorrect to claim that EVERY accepted directive schedule is
periodic. The stronger conclusion here concerns the unique physical ant word.

## 2. Effective bounds and a finite catalog

A simple graph path to a simple cycle uses at most V-1 entry edges and at most
V cycle edges. Hence, after the final exceptional fresh-input block:

    physical preperiod length <= (V-1)*M,
    physical translating period length <= V*M.

These bounds are deliberately coarse and apply only under the stated
infinite-decomposition promise. Cap coordinates can delay the final exceptional
fresh input arbitrarily; no uniform initial-time bound from cap mass is claimed.

Choose one simple cycle from every cyclic strongly connected component of the
periodic graph. Up to cyclic shift and primitive-root reduction, this finite
effective list contains every eventual PHYSICAL period type admitted by any
finite color-change cap over T in this architecture. Indeed, from any vertex
of a cyclic component one can reach its chosen cycle, and fixed-board
determinism identifies the physical continuation. The list may overcount and
is not a cap-launch or producer construction. Its size is at most V.

## 3. Exact scope for finite-seed research

For an actual finite-seed ant state X, the following are equivalent:

1. X has an eventually nonzero translating periodic literal trace.
2. At some finite time, its entire remaining trace admits a decomposition into
   one supplied finite palette whose blocks restore one heading and share one
   common nonzero displacement.

For2=>1 apply Section1 with all-white T and the COMPLETE actual finite board
at that time as the finite cap. Every previously written black cell remains
on that board. For1=>2 choose the one-word palette consisting of one
heading-restoring translating period.

The finite-seed bounded-memory special case is already contained in the
retained stale-memory predictor framework; it is not relabeled a new global
periodicity theorem. The exact colored-front treatment additionally handles
periodic prepared inputs and arbitrary nonstationary macro parsing.

Consequently this entire directed architecture, even with arbitrary changing
directives, can supply only eventual translators. It can still find a
NONSTANDARD periodic finite-seed counterexample if one exists and is launched
legally. It cannot represent a genuinely non-eventually-periodic finite-seed
counterexample at all. A universal proof using this route requires BOTH:

- a justified eventual directed-palette representation, equivalently an
  eventual-translation theorem by the equivalence above; and
- classification of every resulting finite-seed translator as standard104.

Neither premise is proved here. Increasing local palette horizons does not
remove either quantifier. This is a precise strategic limitation, not evidence
that a global reduction is impossible or that the ant is undecidable.
