# Capture for the LRRLRRRRLRR adjacent-defect label

Status: independently audited end to end on 2026-10-22. This is a signed sole-label capture theorem, not a full-highway proof.

## Global claim

A finite-support ant whose sufficiently late K events all have eleven-letter label p=LRRLRRRRLRR eventually follows standard104.

Use M=LLLLRLRRRRLR, N=RRRLLRLLRRRR, and L+p,R+p as equal-length markers. The complete first-marker and next-marker physical trees visit18,453 initial nodes and19,006 total nodes, with no cap/horizon frontier and maximum unmarked depth91. They produce23 raw return types. The same marker-gluing argument as five_label_union_capture.md covers every actual infinite suffix, even when returns are shorter than the markers.

Every marker-compatible physical six-block history, including its actual last marker, is retained. There are13,042 such histories and4,019 five-block history vertices. The only cyclic components have2,3 and945 vertices. The first two have no K labels in any raw+endpoint-marker word, so their infinite finite-support paths invoke the already audited finite-K capture theorem. The third has2,987 edges and exactly8 raw return types.

## Forced packet contraction

The third component has a78-state labelled quotient. Its words use only M and P=RLRRLRRRRLRR. At a P-source, the unique raw word is F=RLRRLRRRRLRRRR of length14 and it ends at M. M-to-P words are E=LLLLRLRRR of length9 and G=LLLLRLRRRRLRLLLLRRR of length19. Therefore the two forced pairs are

    EF = V LRRRR, length23,
    GF = U LRRRR, length33.

Every infinite path has infinitely many M ports: all13 non-M quotient states form a DAG, and each actual P return immediately reaches M. Contracting these forced returns yields65 M-port states and224 labelled edges with seven literal packets:

    C, V, V+=V LRRRR, U, U+=U LRRRR, Q, B.

Their indices are0,1,2,3,4,5,6, with lengths15,18,23,28,33,64,74. This contraction, not just longer lookahead, is important: the raw8-word two-successor and three-successor spatial kernels were empty. No conclusion was drawn from those failed certificates.

## Finite-factor theorem and certificate

Consider a physically realized finite packet factor following this65-state graph, with its actual next complete packet and that next packet's required M marker supplied after the last counted packet. Entry mass m means the complete board's black mass at the first counted packet. Each context(A,B) owns only RAW A; source LAST and intermediate-reader coverage use RAW A. Target FIRST uses A+B+M, with the raw A endpoint retained.

There are29 contexts,123 context edges, and525 literal-feasible short triples. The exact least-index-gap spatial kernel has193,515 candidate overlaps,160 feasible short types, and179,483 stable forbidden pairs after17 rounds. No assumed freshness family is used. Every intermediate-reader pose is enumerated without a spatial cutoff, and all proper subpairs inherit the actual successor context.

The proved raw markers are:
- context(C,C):(-1,0), phase1;
- V and V+ with any permitted successor:(1,2), phase13;
- U and U+ with any permitted successor:(0,3), phase23;
- Q and B with any permitted successor:(-1,0), phase1.

Every marked cell is first read L inside its own raw packet and is unread in every earlier raw packet of the factor. Hence

    c00+n1+n2+n3+n4+n5+n6 <= m.

Only C packets not followed by C are uncharged; their successor is V or V+, and is charged. Thus uncharged packets cannot be consecutive. The factor has at most2m+1 counted packets and at most89m+15 raw turns, because charged packets have length at most74 and uncharged packets length15. Consequently the recurrent8-word component admits no finite-support infinite path. The remaining global components have no K, completing the proposed sole-label theorem.

The freshness and finite-factor bounds require the inherited packet graph and actual right context. They are not asserted for arbitrary concatenations of the seven packet words.

## Artifacts

The independent inputs are frozen by extended_star_packet_manifest.json: direct_monochromatic_returns.cpp; direct_mono_lrrlrrrrlrr.{log,returns.tsv}; analyze_direct_macro_histories.py and the complete history6 words and component files; contract_marker_port_quotient.py and direct_mono_lrrlrrrrlrr_packets_port_quotient.json; the generic spatial checker and29-context geometry, grammar, proof rows and marker queries.

## Independent reconstruction

The separate literal-geometry and complete global-bridge checks are `../audits/check_extended_star_context_independent.py/json` and `../audits/check_extended_star_bridge_independent.py/json`. They reconstruct the spatial induction obligations, raw marks, complete return tree, physical history graph, contracted DAG and packet maps without relying on discovery helper geometry. The audit signs the stated finite-support theorem only; universal defect finiteness remains open.
