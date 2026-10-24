# All standard-rail inputs for the short inverse104 scaffold

Author-certified 2026-10-23 11:45 UTC; the new rail-selector semantics is
pending independent review. The underlying local-image/chronology encoding
and its former single-rail and white cases are independently signed.

## Exact question

Fix V=complement(reverse(H)), where H is the literal standard104 word.
Start V at (0,0,W). At each of its104 coarse read phases independently choose
one internally ant-legal exact-pose replacement of length1,5,or9. The complete
palette has ten choices per coarse turn, as regenerated and independently
reviewed for the earlier short-refinement theorem. Each expanded word has
net displacement(-2,-2), final heading W, and unrestricted charge. Output
colors are entirely free. The word is then repeated periodically; this is
not an occurrence-dependent choice of images on different periods.

The new input is ANY compatible finite bundle of mature standard NE/SW
white-written rail outputs in the same conserved pose sector. Unlike the
previous25 translated single-wake cases, this allows several disjoint rail
profiles simultaneously. No cap, producer itinerary, or infinite initial
background is asserted to be physically realizable by this input relaxation.

## Complete finite geometric reduction

Orbit coordinates are (normal x-y, x parity), modulo(2,2). The union of every
potential read in the entire image architecture is exactly both parity
classes at normals[-8,6], hence30 classes. Its common longitudinal coordinate
floor(x/2) lies in[-2,2].

A standard NE or SW writer reads both parities at eleven consecutive normal
coordinates. Both endpoints are black in its output. Thus mature white-input
writers in one compatible bundle have pairwise disjoint complete read bands,
as proved in the independently signed prepared108 bundle lemma. A writer
whose black output never meets the potential read set has no effect on any
selected consumer word and may be omitted.

Anchor each remaining rail by one black-output class meeting one potential
consumer read class. Same-sector E/W physical headings require an even normal
translation, with either longitudinal x parity. The finite difference set
gives exactly48 oriented translated rail profiles. This is an exhaustive
anchor calculation, not a spatial radius. The geometric interval bound alone allows at most three contributing bands,
but the exact same-sector profile list has no compatible triple. Its385
compatible subsets consist of the empty set,48 singletons and336 pairs. No
cardinality cap is imposed in the encoding; pairwise geometric conflicts
exclude triples automatically.

## Boolean interface and chronology

There is one selector per rail profile. Two selected profiles whose complete
read bands overlap are forbidden;792 pairs are incompatible. At each of the30
potential read classes, the initial-black bit equals the OR of all selected
rail black bits there. The empty bundle is allowed.

The rest is the previously signed exact event encoding. One of ten images is
chosen at each coarse phase. On every read orbit, potential events are ordered
by (floor(x/2), coarse phase, local slot). If active, each event must read its
stated color and toggles the current bit. Inactive events do nothing. The
order is independent of the chosen image lengths because all local images
have the same coarse pose, all total periods have the same drift, and the
coarse/local lexicographic order is the actual within-period time order.

## Exact result and controls

The single CNF has9023 variables and37367 clauses. It is UNSAT. A separate
monotone RUP producer supplies316 additions, and the retained independent
checker verifies all316 with no RAT or deletions.

CNF SHA256:
210581a2ff761eb70b10001d404808d8c5588ef990630df035bf758521e680ed

RUP SHA256:
8b8dd69c30a73830acb54d5400c2cc84bbf9e3af13d3ccb52d77b58466bb14ce

The new OR/profile layer is directly checked on385 assignments: the empty
bundle, every single rail, and every compatible pair. The independent audit confirms that these385 assignments are exactly ALL
compatible rail subsets. The CNF imposes no explicit cardinality cap.
The nontrivial prepared108 word remains a SAT positive control when supplied
its independently verified11-black-class input instead of a standard bundle.
The actual literal complete histories are unchanged.

Files:
- synthesize_multirail_short_refinement.py
- multirail_short_refinement/architecture.json
- multirail_short_refinement/result.json
- multirail_short_refinement/all_bundles.cnf
- multirail_short_refinement/all_bundles.rup
- multirail_short_refinement/prepared108_positive.json

## Scope and next structural consequence

No word in this fixed104-phase1/5/9 architecture has a legal periodic bulk
input supplied by any compatible finite standard parallel-rail bundle. This
does not cover longer local images, different coarse paths, nonstandard
producers, or changing image choices from one period to another.

The separate finite-flight lifting theorem can use this result uniformly:
potential consumer normal support[-8,6] enlarges to U=[-18,16] for relevant
standard writer bands, giving70 full-drift classes. One perpendicular standard
strip meets U in at most22*70=1540 cells. The potential longitudinal span is4.
Conditional on the selector semantics and the lifting theorem, any actual
prefix consisting of standard flights and finite caps followed by n repeats
of any one selected word must satisfy

    |B| >= n-4-6 F_parallel-L_caps-1540 F_perpendicular.

The same constants work even if the selected periodic word varies between
members of a proposed family. This remains a finite-family periodic-consumer
statement, not an arbitrary nonperiodic return obstruction. The lift is being
reviewed separately; no global capture or bounded-defect conclusion follows.

## Independent signoff, 2026-10-23 11:50 UTC

`../../audits/check_multirail_short_cnf_independent.py/json` independently
regenerates all48 profiles,792 incompatibilities,30 OR-input bits, the entire
CNF and all316 RUP additions. It also verifies the exact385-subset inventory.
The stated fixed periodic short-refinement/multi-rail architecture is signed.
The occurrence-dependent choice of images between different periods remains
outside this theorem.
