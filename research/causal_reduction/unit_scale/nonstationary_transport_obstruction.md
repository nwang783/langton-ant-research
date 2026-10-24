# No growing nonstationary directive in the elementary unit-transport alphabet

23 October 2026, 04:14 UTC. Complete finite local certificate and analytic
coverage independently signed. The auditor regenerated all twelve primitives
and replayed all 576 conflicts using complex headings and no author imports.
No finite-support assumption is needed. This is not a classification of all unit-scale refinements.

## The exact alphabet

Each phase independently substitutes R and L by either that same one-letter
identity or one of its six internally legal length-nine unit-geometry images
with charge+1/-1. These are the complete six-word palettes in the earlier
unit-nine inventory. There are49 phase morphisms, including the simultaneous
identity. Every image preserves its own letter; every nonidentity image
contains BOTH letters. All phases have the same unit spatial geometry and
preserve the incoming-to-final heading relation of their coarse letter.

There is no heading-dependent image choice within one phase in this note.
The phase itself may vary arbitrarily, nonperiodically and noncomputably with
refinement level. In particular we do NOT assume the intermediate phase words
are themselves ant trajectories.

## Local composition certificate

For EACH of the48 nonidentity phase maps f and EACH of the12 nine-step
primitive words w, the expanded word f(w) has a same-color consecutive read
at one physical cell. Thus it is impossible on every initial coloring.

The576 cases all fail by zero-based read37. They include cases where only
one of f(R),f(L) is nonidentity; no hidden requirement that both expand is
imposed. Their expanded lengths can be as large as81.

The no-import author inventory and exact trace are in
`transport_composition_closure.py`. Its complete closure has49 states and97
legal edges; all2304 ordered nonidentity map pairs have at least one illegal
image. No safety cap is reached. Frozen full-closure digest:

    a10dd579ddc0cd16e8bc4ac2e90904e40bd907f6ab0e3b8696f4946079503dc0

The smaller certificate is `check_transport_two_active_levels.py` and its
JSON/records output. It shares the author trace routine, so it is NOT an
independent replay. Independent replay and coverage are recorded in
`../../audits/transport_composition_independent.json`.

## All-depth consequence

Take ANY finite composition

    h=phi_0 o phi_1 o ... o phi_(r-1),

in the conventional order: phi_0 is OUTERMOST. Apply it to one root letter.
Discard outer identity levels and let f be the outermost nonidentity map.
Write the remaining inner composed root word as v. If |v|=1, then f(v) has
length at most nine. If |v|>1, inspect the last effective expansion in the
construction of v, working from the root outwards. At that step at least one
letter is replaced by a literal primitive nine-image w. Every later inner
phase has no effect on the current whole word, by the choice of the last
effective expansion. Hence w is still a contiguous factor of v.

The local certificate makes f(w) internally illegal, so f(v) is illegal.
A same-cell read conflict inside a literal factor cannot be repaired by a
prior history, a different initial heading, or a finite/infinite initial
coloring: changing the incoming heading only rigidly rotates its geometry.
This argument never assumes that v, or any other intermediate word, is legal.

Consequently EVERY internally legal finite composed root word has length
at most9. No growing rooted directive limit in this alphabet can be an ant
trajectory, on ANY initial coloring. Arbitrary phase periods, arbitrary
nonperiodic schedules and arbitrary total composed image lengths are covered.

The OUTERMOST-first argument is essential. One must NOT infer that an illegal
intermediate INNER word remains illegal after a further outer substitution;
such a transformation could in principle repair it. The proof instead locates a literal primitive factor of the fully composed inner word, then
applies the fixed outermost nonidentity map to that factor.

## Construction boundary

This closes the proposed alternating two-phase transport construction without
increasing a word-length cutoff. It strictly extends the fixed two-turn unit-
nine exclusion, but does not subsume the eight-independent-heading theorem.
Heading-dependent phase images, additional decorated states, other local
transport primitives, changed boundary headings and other spatial matrices
remain outside this finite alphabet. No counterexample or universal ant
claim follows.
