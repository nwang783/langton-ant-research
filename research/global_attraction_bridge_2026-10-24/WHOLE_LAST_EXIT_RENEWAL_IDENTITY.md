# Whole-history last exits: exact rewiring, and a drought-renewal obstruction

24 October 2026. Author proof and complete-field controls; independent audit pending. Global attraction remains UNSOLVED.

## 1. The entire last-exit forest has only one root

At cut t, include EVERY historical head position p_0,...,p_t, not just a chosen patch or current active component. For each vertex other than the current head p_t, draw its last actual departure edge. Delete the old departure edge of p_t, if it has one. Call the resulting directed graph T_t.

T_t is one arborescence directed toward p_t. To verify this, an edge v->w with w not the root is followed by a read of w later than the last departure of v. Thus last-departure times strictly increase along non-root edges, excluding a cycle. Every vertex has one outgoing edge except the root, and all vertices consequently reach that same root.

At a completed pristine record drought, the new endpoint p_t has never been read before, so no old root-edge deletion is needed to describe the final tree. In particular the whole-region root count is ALWAYS ONE. The multiple BLACK-root requirement for separated restored patches cannot be applied as if the whole historical region were a disjoint union of those patches.

Unvisited original BLACK cells remain on the complete board. They are not vertices of this head-history tree until actually reached, and they must not be discarded or presumed irrelevant.

## 2. Exact chronological tree-rewrite identity

Write ell_t for the number of vertices of T_t with indegree0, counting the root if the tree has only that vertex. In the fixed ant sector each physical vertex has only two permitted incoming neighbors. Hence every tree indegree is0,1,or2, and the finite tree identity gives

    ell_t = 1 + number of indegree2 vertices of T_t.           (1)

For a unit update from current root p to q:

- If q is new to the head history, append p->q and make q the root. The leaf count does not change.
- If q is old, let q->r be its OLD last-exit edge. Remove q->r, add p->q, and make q the root. Before this exchange let d_t be tree indegree. Then EXACTLY

    ell_(t+1)-ell_t = [d_t(r)=1] - [d_t(q)=0].                (2)

The first indicator records creation of a new leaf when a sole incoming edge at r is removed. The second records loss of a leaf when the new edge enters q. They may both occur and cancel. This is a real ordered exchange of the old last-exit tree, not an arbitrary static rewiring. The removed edge is the one at the actual arrival site.

Consequently over any interval[s,t], if A counts the first indicator and B the second,

    ell_t-ell_s = A-B.                                       (3)

At a completed pristine record, the final move is to a new vertex and contributes zero to(2). All branching renewal during that drought is accounted for by its earlier old-site arrivals.

An old arrival q can be WHITE or BLACK. If BLACK, the next update consumes its current R-born lifetime; if WHITE, the next update creates a fresh lifetime. Both arrival colors can create a leaf, with either R or L at the departing root. In the literal empty-seed orbit all four cases occur, first at departure updates7,16,132,136. Thus the exchange term is not simply an old-BLACK-input count.

## 3. Exact fixed-cohort/output ledger, explicitly only bookkeeping

For an interval[s,t], let C be the number of distinct lifetimes BLACK at cut s that are consumed during the interval. Let O be the set of read vertices whose LAST read in this interval is R. Those are exactly the interval-born BLACK identities still present at cut t. Divide them retrospectively into:

- P: genuinely permanent R outputs, never read again;
- F: outputs that will actually be consumed later.

Then, retaining all unvisited old cells,

    |O|=P+F,
    |B_t|-|B_s|=P+F-C,
    |C*(t)|-|C*(s)|=F-C.                                   (4)

Here C*(u) is the ENTIRE actually future-consumed current BLACK cohort. Internal births that die before t cancel; unvisited old identities persist. These are exact mass/lifetime bookkeeping identities, NOT an independent capture inequality.

Equations(3)-(4) isolate what a proposed charging theorem would still have to prove: a relation between the chronological edge-exchange current A-B and actual permanence or input renewal. No such sign is silently inferred.

## 4. A complete pristine drought refutes a natural net-resource charge

Take the EMPTY seed at(0,0), heading E. Cuts11 and20 are consecutive pristine union records: NORTH at(-1,2), then WEST at(-2,2). There is no record in between. The nine turns are

    R R R L L L L R L.

Use the ENTIRE historical tree at both cuts, including all earlier head positions. Its leaves rise2->3, its indegree2 vertices rise1->2, and its root count stays1. The new leaf is(0,2).

The complete current BLACK masses and entire future-relevant populations are both7 at11 and6 at20. The three old-cut inputs consumed in the drought are

    R3 at(-1,0), consumed15;
    R8 at(0,0), consumed16;
    R10 at(-1,1), consumed14.

The two surviving new outputs are

    R12 at(0,2), consumed124;
    R18 at(-1,1), consumed30.

Thus C=3, F=2, P=0, and the relevant stock DECREASES by1 while the tree gains a leaf and a branch.

There is not even a permanently abandoned WHITE cell available as payment. EVERY vertex in the entire cut20 head-history region is read again by124. The certificate gives a literal later read for each of the11 vertices. All current BLACK identities at cuts11 and20 are also explicitly consumed by124. These claims require no unknown-future pruning oracle or infinite-tail assumption.

Therefore both candidate inequalities fail on this completed pristine drought:

    positive leaf increase <= permanently abandoned cells
                              + positive net growth of whole C*;

    leaf increase <= permanent R output + change in whole C*.

Their right sides are respectively0 and-1, while leaf increase is1. The explicit current-input replacements prevent treating chronological branching as a monotonically growing stock of permanent or outstanding input.

This does NOT refute charging the increase to GROSS newly emitted F identities: F=2 here. Such a charge would still need a separate argument that prevents those lifetimes from being consumed and replaced in later droughts. It also does not refute a different spatial/amortized potential.

## 5. Full-field regressions and scope

The checker rebuilds the entire historical tree from the original seed, never resetting it at the named cuts. It verifies every edge exchange and all named full fields, plus exact infinite canonical parity for four complete trajectories:

- empty seed, including the tiny drought and the earlier5710..6042 self-written square circulation;
- MT n100 and137, each with both its completed pristine drought and its permanently pinned-hull interval;
- the explicit11-cell exterior factor, continued to the sufficient canonical cut20000 solely to classify its whole earlier output lifetimes. This is not asserted to be the earliest capture cut.

For MT100's completed drought the tree gains1859 leaves, with4890 permanent R outputs and whole relevant stock change-1063. Its pinned-hull interval gains1336 leaves, with3528 permanent R outputs and relevant change-787. These genuinely realize the permanent-output branch, unlike the tiny zero-permanence countercontrol.

For the11-cell factor's inner cycle[5,66], the full historical tree gains2 leaves, permanent output is0, and whole relevant stock grows by11. This is a finite input-replacement branch, not a regenerated exterior. The actual subsequent port failure from the earlier certificate remains unchanged.

The separate possible bound ell(T) <= C+|O|+1 for an interval-reset last-exit tree is UNPROVED here. Bounded tests have not decided it. It is not needed for any statement in this package and must not be used as a premise.

The useful outcome is the exact whole-tree chronological exchange current and a literal failure of its simplest net-resource interpretation. Root multiplicity supplies no hidden fuel. Universal control of repeated drought renewal, compact-return occurrence, and canonical104 uniqueness remain open.
