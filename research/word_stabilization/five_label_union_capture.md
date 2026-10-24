# Capture after deleting a five-label set of adjacent defects

Status: the complete compact bridge and all invoked sole-label theorems are independently audited. The five-label UNION statement is signed end-to-end. The full highway conjecture remains open.

## Statement

Let S={RRRLLRLLRLR, LLRLRLLRRLL, RRRRLRLLRLL, RRRLRRRRLRL, RRRLRRRRLRR}. For a finite-support Langton ant, eventual standard104 capture is equivalent to finitely many K events labelled outside S. Here K(t)=J(t-1)J(t), with J a bad cyclic-standard-ten window ending at t. No spacing condition is imposed.

## Complete bounded marker trees

Choose the12-letter markers M=LLLLRLRRRRLR, N=RRRLLRLLRRRR, and L+p,R+p for every p in S. Every finite word is checked by literal square-lattice current-read consistency: consecutive reads of the same cell must alternate L/R. Every internal K window must have its label in S. These conditions are both necessary for a true trace; read consistency is also sufficient for some initial board on its finite read set.

Starting with empty history, enumerate until the FIRST marker endpoint. The whole finite tree has19,290 recursive nodes, no node-cap truncation and no unexplored horizon leaf. Maximum unmarked depth is90. Separately seed each physically feasible marker and enumerate until the next marker endpoint strictly after that seed. Including the initial tree, the total is20,679 nodes, no cap or horizon frontier, maximum unmarked depth91. Thus every infinite permitted physical suffix reaches a marker and has infinitely many subsequent marker returns. These are complete finite trees, not bounded searches being extrapolated. A conservative92-turn hitting bound suffices.

Shift every marker cut twelve reads backward. The exact raw return set contains69 triples(start marker,end marker,raw word), recorded in direct_five_signed_labels.returns.tsv. Raw words can be shorter than twelve, but raw+end marker begins with its exact start marker; this handles overlapping marker occurrences. All raw lengths are positive. Every genuine infinite trace with eventual labels in S yields an infinite raw-block path.

## Four-block physical history graph

Enumerate every marker-compatible raw-block word of length4 that is physically feasible together with its actual final marker. There are3,493 words, giving887 length-three history vertices. An edge maps(a,b,c) to(b,c,d) and emits raw label d. Thus every actual infinite marked path, after its first three blocks, is a path of this finite graph.

The graph has only two cyclic components. Discovery stores their exact history sets, all internal labelled edges, and explicit maps of each history to quotient classes:

1.43 histories,85 edges, eleven raw words. Its quotient is EXACTLY the previously audited six-state/twelve-edge graph in single_k_rrrllrllrlr_port_quotient.json, with identical word and marker indices. Every internal raw+marker word permits only the K label RRRLLRLLRLR.
2.65 histories,210 edges, seven raw words. They are exactly the literal seven words of monochromatic_seven_word_fuel.md. This history quotient has13 classes, not the52 classes of the older149-history presentation. No inclusion into that52-state grammar is claimed or needed. Every internal raw+marker word permits only the K label RRRLRRRRLRR.

Contracting those two exact history sets leaves a DAG. Every infinite path therefore eventually stays in one component, where its K labels are eventually one of the two already signed sole labels. Invoking the corresponding global sole-label theorem proves standard capture. In particular, the argument does not infer the union statement merely because each singleton was known.

The end-marker context covers all eleven-letter K windows beginning in the corresponding raw block, including boundaries and overlapping markers. Hence checking the entire raw+marker word really proves the eventual label restriction for each recurrent component.

## Frozen artifacts

The allowed set, counters and conventions are in direct_five_signed_labels_config.json. Complete return DFS: direct_defect_set_returns.cpp and direct_five_signed_labels.{log,returns.tsv}. Four-history enumerator: analyze_direct_macro_histories.py. Its complete history list, component history sets, internal edges and explicit quotient maps are in direct_five_signed_labels_history4_{words,summary}.json and direct_five_signed_labels_history4_scc{0,1}_port_quotient.json. SHA bindings are in five_label_union_manifest.json.

This still does not prove that K labels outside S occur only finitely often on every finite seed, nor does it prove that all12 possible isolated-pair labels may be deleted together.

## Independent replay

../audits/check_five_label_union_independent.py/json reconstructs the current-color return trees with no search cutoff, then tests all87,307 marker-compatible four-block paths without prefix-feasibility pruning. Exactly3,493 are legal. Contracting the43/65 recurrent history sets gives a781-vertex DAG. Their exact internal K-label sets are respectively {RRRLLRLLRLR} and {RRRLRRRRLRR}.
