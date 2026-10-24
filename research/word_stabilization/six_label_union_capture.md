# Six-label adjacent-defect deletion by extended-star packets

Status: independently audited end to end on 2026-10-22. The complete six-label UNION theorem is signed. No full-highway claim.

## Global statement

Let S={RRRLLRLLRLR, LLRLRLLRRLL, RRRRLRLLRLL, RRRLRRRRLRL, RRRLRRRRLRR, LRRLRRRRLRR}. For a finite-support ant, eventual standard104 capture is equivalent to finitely many adjacent-bad-ten events K with labels outside S.

## Complete compact bridge

Use M,N and L+p,R+p for all p in S. The exact first-marker return trees complete19,308 initial nodes and20,715 total nodes, with no cap or horizon frontier and maximum unmarked depth91, and give88 raw returns. These complete finite trees cover every actual eventual suffix. For marker-compatible words, raw+end-marker begins with its prescribed start-marker; reverse induction on a chain shows that all intermediate marker contexts occur literally in the full concatenation. Thus testing physical feasibility of every prefix plus its endpoint marker cannot discard a feasible full history.

The complete physical six-macro history list has62,863 words and16,630 five-block vertices. Its only cyclic history components are:
1.167 vertices,327 edges, the same eleven raw words and exact six-state/twelve-edge quotient as the signed RRRLLRLLRLR theorem. Every raw+marker word has K labels only RRRLLRLLRLR, so that already signed GLOBAL theorem handles any infinite finite-support path there.
2.1,083 vertices,3,426 edges, ten raw words, with an80-state/254-edge quotient.

Contracting these exact history sets must leave a DAG; the full graph, history sets, internal labelled edges and explicit quotient maps are stored for independent reconstruction.

## Eight M-return packets

The second component uses M and two extra markers, each with a unique14-turn return to M. Its15 non-M quotient states form a DAG. First returns to the65 M states contract the graph to65 states and239 edges with exactly eight packets:

    0 C15, 1 V18, 2 V+=V LRRRR (23), 3 U28,
    4 X30=LLLLRLRRRRLRLLLLRRRRLRRRRLRRRR,
    5 U+=U LRRRR (33), 6 Q64, 7 B74.

All packets start and end at the same required marker M. No assertion is made for arbitrary concatenations; the inherited65-state graph is part of the theorem.

## Finite fuel theorem

Consider a physically realized finite packet factor in this graph, with an actual full next packet and that next packet's required M marker after the last counted packet. There are32 overlapping successor contexts,133 context edges and574 literal-feasible short triples. As before, each context owns only its first raw packet; source LAST and intermediate-reader coverage use that raw packet, while target FIRST includes its actual successor and M.

The unconditional least-index-gap certificate has230,460 candidate overlaps,184 feasible short types and213,558 stable forbidden pairs after21 rounds. The following local sites are first read L inside RAW and are unread in every earlier raw packet of the factor:
- context(C,C):(-1,0), phase1;
- V,V+:(1,2), phase13, for every permitted successor;
- U,U+:(0,3), phase23, for every permitted successor;
- X30,Q,B:(-1,0), phase1, for every permitted successor.

Their charges are pairwise distinct entry-black cells. If m is the complete-board black mass at factor entry, then

    c00+n1+n2+n3+n4+n5+n6+n7 <= m.

Only C packets not followed by C are uncharged; their actual successor is V or V+, hence charged. Thus at most2m+1 packets and89m+15 raw turns occur in any counted factor. This excludes every finite-support infinite path in the second component. The first component captures standard104 by its already signed sole-label theorem, proving the UNION6 statement.

## Scope and frozen inputs

The same packet theorem also excludes the newly studied individual label LRRLRRRRLRR. Its separate seven-packet artifact is extended_star_packet_capture.md, but the UNION6 proof does not depend on that singleton being signed first. All counts, literal words, physical histories, contractions, spatial clauses and scripts are bound in six_label_union_manifest.json. The original generic spatial checker is unchanged. The broad full88 spaced-K exploration and dynamic variants are not dependencies.

This does not establish universal finiteness of K labels outside S. Dense clusters and the six other possible isolated-pair labels remain outside this theorem.

## Independent reconstruction

The separate literal-geometry and complete global-bridge checks are `../audits/check_six_label_context_independent.py/json` and `../audits/check_six_label_bridge_independent.py/json`. They reconstruct the spatial induction obligations, raw marks, complete return tree, physical history graph, contracted DAG and packet maps without relying on discovery helper geometry. The audit signs the stated finite-support theorem only; universal defect finiteness remains open.
