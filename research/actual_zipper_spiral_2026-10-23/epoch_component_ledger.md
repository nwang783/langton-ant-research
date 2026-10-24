# Full-state ordinary-epoch ledger: exact accounting, not a global progress theorem

23 October 2026. Author derivation. This note preserves all actual physical
black cells and both black graphs. It does not quotient away component
interiors, assume LIFO reactivation, or charge passive archives for free.

## 1. Active old fuel versus retained outputs

Consider n complete ordinary R^r L blocks (r<=2 and each L a w bridge), with
no final incomplete R tail. The entry may be a proper post-L cut or an
arbitrary first partial block with the separately stated first correction.
Let:

- M be complete entry black mass;
- C be the complete entry active w component, with a edges;
- d=M-a be total entry passive-component mass;
- P be the n consumed initial w bridges (the actual vertex-simple path);
- F be the final active component, an exact initial-edge subset, with f edges;
- Q be the initial active edges neither consumed nor retained in F, with p edges;
- R be the number of actual R updates, and G=R-n the complete mass gain.

Exact far-side inheritance gives the FULL lifetime decomposition

    C = P disjoint-union Q disjoint-union F,
    a = n+p+f.

Every initial passive edge and every edge of Q survives but is outside F.
All R-created lifetimes survive, and all lie outside F. Consequently the
final dormant board is the actual union of entry passive edges, Q, and ALL
R writes, though its components can merge and have arbitrary internal graphs.
Its exact mass is

    D_final = d+p+R = d+p+n+G.

Thus

    active old fuel loss = a-f = n+p,
    final complete mass = f+D_final = M+G.

This is not scalar COMPLETE-mass descent: complete mass may grow. Nor does
it say outputs fragment into small components. A huge imported archive may
be attached before an L and left behind after it. Component sizes at the
R-prefix fine cuts can greatly exceed the post-L active old suffix sizes.

The signed-path upper bound supplies, safely including the first-block
correction and n0/1,

    G <= 8 sqrt(n)+3,
    n >= ((G-3)_+/8)^2,
    a-f >= ((G-3)_+/8)^2.

So a large positive gain does consume quadratic *epoch-entry old input*.
This input may itself have been generated or reactivated at earlier renewals;
it is NOT a once-only initial-seed budget. Non-LIFO reactivation and long
serial releases remain fully allowed.

## 2. Exact paired Euler bookkeeping

For each of the two black graphs k, start with every endpoint of every
entry black edge, together with the corresponding current cursor. Retain
these marked vertices forever within this interval, even if they become
isolated. Add a vertex when it is first encountered as an R-edge endpoint.
Let A_k count newly marked vertices; let C_k count ALL marked components,
including isolated vertices. Let B_k count R insertions whose endpoints are
already connected (cycle births), and D_k count L deletions of nonbridges
(cycle erasures). Let beta_k be full black cycle rank.

Euler's formula and the elementary edge updates give EXACTLY

    Delta beta_k = B_k-D_k,
    Delta C_k = A_k+B_k-D_k-G.

For ordinary w epochs D_w=0, but D_z can be positive. These are exact Euler
BOOKKEEPING identities, not a new monotone resource or progress theorem.
Marked-vertex growth, merging of pre-funded components, and birth/death of
cycles can trade against each other. Neither graph may be discarded.

A small actual-cursor consequence: when n>=1, the last bridge L separates
its two marked endpoints, so C_w(final)>=2. Hence

    G <= A_w+B_w+C_w(entry)-2.

With one entry component this reads G<=A_w+B_w-1. The detoured collector
family below attains equality with B_w=0 and A_w=G+1. Thus the independent
new-vertex term cannot simply be suppressed or replaced by cycle births.
This sharp bookkeeping inequality alone supplies no global renewal density.

## 3. Executable controls show why stronger naive tradeoffs fail

All collector resources below are physically present and included in M.
Both the initially passive and initially root-attached variants retain every
collector cell. The root attachment is a three-edge path, not a free link.

A. Pure spaced spiral (independently passed proof47ca17aa): final w output
is n-1 tiny stars. Here A_w=R=n+G, B_w=0, Delta C_w=n. This illustrates
fragmentation but does not prove it is necessary.

B. Standard outside collector: connect all R-arm tips by an initial w path
one unit outside the spiral. Every straight block attaches its root to this
same archive; at a corner the second R arm creates a w cycle behind the
departing bridge. All final edges belong to one huge dormant w component.
The connected-entry variant has M=2n+2(q-1)+3, A_w=0, B_w=q-1=G+1,
Delta C_w=1. For q32,n1088 this is entry active mass2241, final one dormant
component2271, no cycle erasures, and exactly31 w-cycle births. The opposite
graph remains a forest in the fixed controls.

C. Detoured outside collector: avoid each second corner-arm tip so that it
becomes a new vertex instead of a second connection to the archive. Then
all final edges still belong to one huge dormant w TREE, both graphs remain
forests, and no cycle is born or erased. The connected-entry variant has
A_w=q-1=G+1, B_w=0, Delta C_w=1. Thus positive square-root gain need not force
output-component fragmentation OR cycle creation. It can be paid by actual
new marked vertices against a fully pre-funded collector. An all-parameter
construction and local paired-graph proof are in
one_component_paired_forest_collector.md.

Concrete q8 control: n160 old path edges +188 collector edges +3 connector
edges gives one initial active tree of mass351, passive mass0. The actual
326-update ordinary epoch has G6, consumes160 edges, prunes191 old active
edges into the collector, and ends with active mass0 and ONE dormant tree
of357 edges. Both full graph ranks, all cycle births, and all cycle erasures
are zero. It creates exactly7 new marked w vertices. All mass and both graph
terms are charged; no background source was cropped or introduced for free.

These controls invalidate the naive stronger tradeoffs, not the exact
quadratic old-input cost. They also do not realize a repeatable sequence of
near-extremal epochs or establish sharpness of the global cubic bound.
