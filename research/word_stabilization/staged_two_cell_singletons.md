# Two further sole-defect-label capture theorems

Status: independently verified end to end on 2026-10-22. These are two SEPARATE global singleton theorems, not a union with each other or with the six-label theorem.

## Statements

For each p separately in {LRRLRRRRLRL, RRRLRLLRRRR}, a finite-support Langton ant whose sufficiently late adjacent-bad-ten events K all have label p eventually has the standard104 turn stream.

K is defined using the84 cyclic ten-factors of the canonical W104 pinned in the manifest. A K label is the eleven-letter word whose first and last ten-letter subwords are both outside that language. Transient windows before the eventual cut are irrelevant.

## Complete marker coverage and finite-history bridge

Use the twelve-letter markers M=LLLLRLRRRRLR, N=RRRLLRLLRRRR, L+p and R+p. The exact current-color recursion in direct_monochromatic_returns.cpp branches only on physically permitted next reads, rejecting a K label other than p. Its initial unmarked tree and every first-return tree terminate with no cutoff frontier:

- p=LRRLRRRRLRL:18,678 initial nodes,19,454 total nodes,30 raw returns, maximum unmarked depth91.
- p=RRRLRLLRRRR:18,692 initial nodes,19,484 total nodes,26 raw returns, maximum unmarked depth91.

Fresh snapshot replay is byte-identical to the frozen return files. The maximum-depth and node caps are never reached; the proof depends on complete exhaustion, not on the cap.

Every permitted infinite physical trace therefore has infinitely many these markers and decomposes into the listed raw returns, each followed by its actual endpoint marker. All physically feasible marker-compatible four-return words are enumerated. Their de Bruijn history graphs are finite overapproximations of real traces. The full recurrent-component decomposition and literal history-to-quotient maps are in the frozen history4 JSON files.

For the first label the only recurrent component has575 history vertices and maps to86 quotient states over28 raw words. For the second it has366 history vertices and maps to47 quotient states over22 raw words. Contracting each claimed recurrent history set must leave a full DAG in the independent check; SCC sizes alone are not the bridge certificate.

## Context ownership and spatial proof rules

A context type (A,B) owns only RAW A. Its target first-read footprint is A followed by the actual B followed by B's endpoint marker. Every proper pair subinterval inherits the same real right context. The source LAST and every intermediate reader use only their owned RAW words. All selected fuel marks occur inside the owned RAW A.

The finite spatial certificates use the already reviewed least-actual-index-gap induction, now with the analytically reviewed odd-reader and two-cell transition rules. Every physically feasible gap1 or gap2 type is removed from the proposed forbidden family. At larger gaps, a certificate either:

1. excludes every successor/predecessor combination through a strictly smaller forbidden pair;
2. excludes every odd-multiplicity reader that could bridge equal source-LAST and target-FIRST letters;
3. proves that the exact two-bit target pre-color is unreachable from the exact source post-color using any intermediate RAW-reader transition not already forbidden by a strict subpair.

The third rule permits arbitrary order and spatial teleports. It is therefore an overapproximation of actual intermediate histories, not a claim that the transitions compose geometrically. See multi_cell_spatial_inference.md for the argument.

## Staged fuel deletion

A certified first-L mark is unread by every earlier owned raw block, so it names a distinct entry-black cell. Every marked context can therefore occur only finitely often from finite entry mass. After its last occurrence, restart the trajectory at a fresh finite-mass cut in the remaining graph. This restart is essential: the next stage does not assert freshness relative to the original earlier cut.

### Label LRRLRRRRLRL

The initial127-context kernel has3,931,561 clauses and certifies89 raw-marked context types. Only23 selected marked contexts are required: after deleting these23, every recurrent vertex already belongs to the original unmarked set. The dependency-cone certificate with2,835,600 clauses proves just those23 marks; it may replace the full search kernel.

The sole remaining recurrent component has28 context types. Its independent finite certificate has135,994 clauses and charges13 types. The next recurrent component has7 context types; its9,472-clause certificate charges two. The only remaining cycle is [1,6,5] in that final seven-type graph, with raw lengths15,45,44. Its concatenated104-letter word is exactly phase89 of the manifest's canonical W104, with translation(2,2) and restored heading.

### Label RRRLRLLRRRR

The initial89-context kernel has1,506,295 clauses and certifies51 raw-marked types. Only25 selected marked contexts are required; deleting them leaves no recurrent originally marked vertex. The1,023,737-clause dependency cone proves those25 marks.

The residual graph has a17-context component and two single-context loops. The17-context certificate has56,328 clauses and charges8 types. Its remaining recurrent components are the standard104 cycle [3,16,14] with raw lengths15,45,44, and the pure U28 loop.

The other two initial loops are pure V18 and T16=RRRRLRLLRRRRLLRL. Exact drift-orbit chronology proves that none of these three pure periodic tails is possible from finite support. Their restored-heading displacements and numbers of distinct first-L drift classes are:

- V18: displacement(1,3), two first-L classes.
- U28: displacement(0,4), five first-L classes.
- T16: displacement(0,2), three first-L classes.

For each class, sufficiently far translated cells have a complete, fixed chronological read list beginning L. Distinct translates are distinct initially black physical cells. This is an all-period arithmetic argument, not a finite simulation. The exact orbit lists and canonical standard-cycle comparisons are saved in staged_two_cell_periodic_certificates.json.

## Independent verification targets

The frozen manifest lists both complete marker trees, every four-history word and quotient map, all stage inputs, all spatial proof rows, all selected raw marks, and every graph pruning step. The cone extractor and greedy charge selector are untrusted discovery tools: their outputs can be checked directly without trusting their algorithms. In particular, the independent check should verify every cone row against the cone itself, every marked overlap, the full residual SCC/DAG claims, and the exact periodic-ray chronology.

Universal finiteness of forbidden events remains open. Even if both singleton statements are signed, their union is a separate theorem requiring a new bridge and possibly new recurrent-language arguments.

## Independent signoff

The independent no-import literal C++ verifier and complete graph reconstruction passed all five spatial stages and both global bridges. Entry points are ../audits/replay_staged_singleton_clauses_independent.py and ../audits/check_staged_singleton_bridges_independent.py. The C++ proof checker is ../audits/check_literal_spatial_clauses.cpp. The original reviewed manifest hash is c56da6b266b51f4af694f9c854279e254ee22b870ae2264707d9cc51bf0c0056. Current manifest changes after signoff update status and crosslinks only; the actual proof rows, marks, return words, graphs and periodic certificates are unchanged.
