# Two exact scaffolded periodic-refinement exclusions

Author certificate, 2026-10-23. Independent analytic/encoding audit is pending. No general Langton-ant highway theorem is claimed.

## 1. Architecture and complete local inventory

Fix the retained standard104 turn word H, with incoming heading W, so its displacement is(-2,-2). At each of its104 literal read phases independently, replace the coarse turn by a finite turn word with exactly the same net displacement and final heading as that one coarse turn. The images need not be shared between equal turns or headings. First and last turns are not prescribed. The complete internally ant-consistent inventory at lengths1,5,9 has ten choices per turn:

R: R; RLLLL; LLLLR; RRRRLLLLR; RLRRRRLLL; RLLRRRRLL; RLLLLRRRR; LLRRRRLLR; LLLRRRRLR; LLLLRLLLL.

L: L; RRRRL; LRRRR; RRRRLRRRR; RRRLLLLRL; RRLLLLRRL; LRRRRLLLL; LRRLLLLRR; LRLLLLRRR; LLLLRRRRL.

The charge of an image is unrestricted. Internal alternation is a necessary condition for any larger legal trajectory, so discarding internally inconsistent words loses no candidate in this bounded architecture. Geometry forces these odd lengths to be1 mod4; no other positive length at most9 has the same final heading.

### White-front conclusion

Among all10^104 phase assignments, the only assignment whose complete translating spatial-orbit histories start white and alternate is the identity assignment. Equivalently, there is no nonidentity white-input periodic front obtained by these refinements of H.

This is a statement about the fixed coarse path and the stated palette. It does not exclude longer images, different coarse paths, arbitrary periods, arbitrary white fronts of drift(2,2), or nonperiodic paths. Cyclic phase changes and proper rotations of this same presentation are harmless symmetries, not new architecture.

### Prepared reverse-wake conclusion

Let rev=swapRL(reverse(H)), start at(0,6,W), and let the input be the full mature NE104 wake profile generated from origin0. This is the sector-correcting translation(1,6) of the exact reverse presentation starting at(-1,0,W). No assignment from the same short-image palette gives a legal prepared periodic front here. This is ONLY that one transverse/longitudinal translation class. The identity case already fails the known reverse-wake profile comparison; the nonidentity class has the RUP certificate below.

## 2. Exact chronology without an unknown period variable

For the common displacement d=(-2,-2), spatial orbits are indexed by

  a(q)=(qx-qy, qx mod2),  i(q)=floor(qx/2).

A literal read at offset q in period0 reappears at q+n d. For a fixed cell, its read time is j+P i(q), up to a common constant, where j is its actual index in the chosen period and P is that period's length. Therefore possible reads in an orbit are ordered by

  (i(q), coarse phase, local image slot).

This order does NOT depend on the unknown chosen lengths. Only one image is active at a coarse phase, so mutually exclusive potential reads at one slot cause no ambiguity.

For every orbit, begin with its prescribed input bit. Each selected event must read that bit and then toggles it. Unselected events do nothing. The last bit is the free output profile. These are precisely the complete bulk first-color and alternation constraints. There is no output or mass filter in the synthesis.

The CNF uses an exactly-one selector for each phase, an OR gate for every potential event's selectors, and one XOR bit update per event. The reading constraint is conditional on that event being active. A final clause asks for at least one nonidentity image in the white-front test.

## 3. Explicit monotone RUP certificates

`certify_short_refinement_rup.py` builds the CNF directly, not by asking an SMT solver to translate it. The retained plain first-UIP producer is untrusted; the separately implemented `check_drat` verifies the emitted proof. Both proofs have no RAT additions and no deletions.

- White short palette:8945 variables,36194 clauses,3574 checked RUP additions.
- Reverse short palette at(1,6):same dimensions; the empty clause itself is RUP, so unit propagation alone rejects it.

Files are under `short_refinement_rup/`. Each JSON binds the exact CNF and RUP hashes. The SMT implementation is a discovery cross-check, not the sole source of UNSAT.

## 4. Nonvacuous positive controls

Identity H on white reconstructs the retained104 front exactly.

Identity rev in its ORIGINAL opposite physical sector reconstructs the exact reverse104 front and erases its mature wake. This is not a same-sector construction.

A genuinely nonidentity prepared control replaces rev's zero-based letter31, L, by LRRRR. Its period is108, displacement(-2,-2), heading W is preserved, and its charge is-8. At start(0,6,W), all23 spatial-orbit histories alternate. Its required black profile has11 classes and its output has3. `reverse108_prepared_control.json` gives the literal word and complete input/output profiles. The encoding accepts this exact nonidentity assignment when supplied its correct profile. It is NOT a consumer of the standard wake and supplies no finite-seed launch.

## 5. A different, fuel-free local positive primitive

The actual blank ant executes the52-letter word

  RRRRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLLR

and returns to(0,0,N) with the origin white and12 black cells elsewhere. Earlier returns to the original pose at times4 and16 have the origin black. Consequently appending R gives a53-read unit R transport needing no initial black cell. Starting with L and then performing this blank excursion gives an exact unit L transport needing only the original L cell black. Both add12 charge relative to the coarse turn.

This disproves an attempted extrapolation that every nontrivial local pose-preserving delay must consume prepared black fuel. It does NOT establish a compatible periodic refinement.

A separate two-choice-per-phase control, identity versus precisely this anchored blank excursion, is also white-front impossible. Its direct CNF has11233 variables and38898 clauses, with a three-addition verified RUP proof. Files: `probe_blank_return_refinement.py`, `blank_return_refinement.json`, `certify_blank_return_refinement_rup.py`, and `short_refinement_rup/white_blank_return.*`. This is one explicit positive primitive tested in a fixed architecture, not an exhaustive image-length53 search.

## 6. Complete same-sector translated reverse family

The single translated reverse conclusion in Section1 has now been closed over ALL translations, without changing the image palette or increasing a horizon.

For the unshifted reverse scaffold at(-1,0,W), the union of all possible read orbits has normal coordinates[-9,5], both longitudinal parity classes. The mature forward wake's black support has normals[-7,3]. Any translated potential read can encounter a wake black class only when its normal shift lies in[-12,12]. Conserved same-sector parity requires an odd normal shift. Both x parities therefore give exactly24 possible overlap classes. Their translations are tx in{0,1}, ty=tx-normal, for odd normal in[-11,11]. Every other same-sector translation presents white input on ALL possible selected read orbits and is represented by one additional white case.

`certify_reverse_short_all_translations.py` reconstructs the finite list by exact differences of the two orbit supports rather than by scanning a radius. It includes the identity assignment in every CNF. All25 cases have verified monotone RUP proofs, with250 additions in total and at most45 in a case. The manifest and full proofs are under `reverse_short_all_translations/`.

Thus no member of this complete phasewise short-refinement reverse family is a same-sector consumer of the standard mature wake, at any translation, even when its output profile is entirely free. The same first-color statement is the needed premise for a fixed-cap H^n C P^n bounded-fuel obstruction: a stable mismatch inside the producer-read strip is an eventual chronology contradiction, whereas a required black class outside that strip needs linearly many initial black cells. A fixed literal cap can affect only boundedly many such cells. The separate all-n pump framework owns that composition inference; this note supplies its complete bounded P-family premise.

`short_refinement_scaffold_inputs.json` freezes the full H/reverse words, local image inventories, headings, displacements and wake input independently of imported generators. SHA256: 5304733d40c7e53072626e354ef5c1f1af24b366095538be9770fac59304ebc3.
