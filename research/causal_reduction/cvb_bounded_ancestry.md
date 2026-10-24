# Uniform bounded ancestry inside C/V/B intervals

## Status

A new conditional structural theorem for the recovered macro subsystem. It is not a proof that arbitrary ant trajectories enter that subsystem. The finite exclusion certificate below is checked with complete nine-bit color states and separately reproduced with BDDs. The independent audit has passed the finite closures, the unbounded type/depth argument, the boundary-bud convention, and an independent literal reconstruction of the sharp witness.

The sole inherited nontrivial lemma is the independently audited fresh-V-tip theorem in `../word_stabilization/cvb_finite_fuel_theorem.md`. Literal C/V/B strings and all short-word conflicts used below are reproduced in `certify_cvb_ancestry.py`.

## 1. Statement

Consider any finite physically feasible concatenation of C,V,B, with an arbitrary finite or infinite board at its entry. Form its **cut token forest** as follows:

- Retain the cursor nodes and token parent edges from `forest_theorem.md` whose R-production and L-consumption occur in this interval.
- A node consuming an entry-time black token is a new cut root at depth zero. The entry cursor is also a cut root.
- Record every token produced during the interval but still black at its end as a boundary bud attached to its producer. These buds need NOT be permanent in the full future.

Depth counts ordinary parent-child edges from a cut root. A boundary bud adds one to its producer's depth. Virtual initial-edge roots are not counted as another depth level.

**Bounded-ancestry theorem.** Every cursor node and every boundary bud in this cut forest has depth at most eight. The bound is independent of interval length, entry black mass, and black lifetime ages. It is sharp for cursor nodes: the feasible word CCCVV has a node of depth eight.

In particular, no chain of nine internal token-parent edges is possible in a C/V/B interval. The bud-inclusive bound additionally counts the artificial final edge to each boundary bud. This is stronger than the finite-fuel duration bound in a different direction: arbitrarily many entry tokens and arbitrarily many V blocks do not permit deeper internal genealogy.

## 2. Node types and elementary macro geometry

Write Mj for the node beginning just after phase j-1 of macro M, with zero-based physical phases. A node is **positive** if it writes at least one R-token during the interval.

The positive nodes in C are C4,C6,C11; in V they are V4,V6,V11,V14. Their R-run lengths are respectively (1,4,4) and (1,4,2,4). Nonpositive nodes have no offspring and can only add one final depth level.

The following are immediate from the literal read tables and the determinant-ten coarse lattice:

1. C11 has the unique internal parent C6. V11 has the unique internal parent V6.
2. C4 and V4 cannot parent ANY positive C/V node in a different macro. Their one written cell cannot coincide with any first-L cell followed by R in another C/V macro at any allowed relative coarse pose. Internal positive children are also absent.
3. A V11 token cannot parent C4 or V4 by the same exact lattice equation.
4. V14 is a cut root, by the inherited fresh-tip theorem: its entering L is V phase 13 at (1,2).

For item 2, a target L that is not the first read of its cell in its macro necessarily consumes a token written inside that same macro, so only first-read target sites need the lattice test.

## 3. New finite local last-writer exclusions

Both C6 and V6 enter by consuming the common phase-5 cell q=(1,0). That is its first read in the macro.

**Producer-type lemma.** If this input token was produced earlier in the C/V/B interval, its producer is one of C11, V14, or B70.

**C11 separation lemma.** If its producer is C11, every complete macro strictly between that producer's C macro and the consumer's C/V macro is C. In particular, no V or B may intervene.

### Complete finite certificate

Use the nine-cell patch

`P={0,1,2} x {-1,0,1}`.

The coarse center geometry is exactly that in the inherited C/V/B proof. Enumerate all centers from which some macro can read a patch cell by the determinant-ten equations, retaining all four headings. This gives 57 head states including OUT. Every omitted-center macro avoids the patch. OUT is allowed to return to every retained head with an omitted predecessor; this is a conservative overapproximation, not a connectivity assumption.

For the producer-type lemma, initialize with the outputs of every macro whose last q-read is R and whose producing node is NOT one of C11,V14,B70. Every patch cell read by the producer macro has its forced post-color; all unobserved bits are arbitrary. There are 68 initial complete-color states. Preserve q by forbidding intervening macros that read it. The union of all such paths has 9,706 reachable states, and none permits the target C or V at its normalized pose.

For the separation lemma, initialize instead from every C11 producer. Add a flag indicating whether a non-C intervening macro has occurred. OUT can set that flag nondeterministically, so outside excursions cannot hide a V or B. There are 64 initial and 64 reachable complete states. No flagged state permits the target C or V.

`certify_cvb_ancestry.py` reconstructs all literal motions, sensitive centers, inverse boundary predecessors, macro color guards, and closures, then separately verifies inductive closure and target exclusion. `cvb_ancestry_certificate.json` contains both complete reached-state lists. BDD implementations are discovery cross-checks, not a replacement for this explicit closure proof.

## 4. Short grammar and the optional B prefix

Same-cell repeated-letter conflicts, explicitly checked in the certificate, imply:

- CCCC cannot be followed by any of C,V,B.
- V C^k B and B C^k B are impossible for k=0,1,2,3.
- CCB and CCCB are impossible.

Hence a B, if present, is the first macro or follows one initial C. There is at most one B.

Additional checked conflicts are VCCCV, BCCCV, VCCCC, BCCCC. Thus:

- An initial C-run has at most four blocks, and at most three if another block follows.
- A C-run after V or B has at most three blocks if terminal, and at most two if followed by V.

The two possible B prefixes are finite: B and CB. Direct exact genealogy gives maximum positive-node depths three and four, respectively. In either prefix B70 is a cut root of depth zero. Other nodes in those prefixes have depth at most five. A later C/V node6 can inherit from B only through B70, by the producer-type lemma.

## 5. Depth proof

Any positive C/V ancestry chain, apart from final nodes of type 4, must follow

`C6 -> C11 -> ... -> C6 -> C11 -> V6 -> V11`

or a subchain thereof. Each C11-to-node6 edge stays within the same intervening all-C run by the separation lemma. The only possible other internal entrances are roots V14 or B70; entry-time black tokens also start at depth zero.

For an initial C-run of k blocks, its deepest C11 has depth at most 2k-1. If terminal, k<=4, giving depth at most seven. If a V follows, k<=3, and its V6,V11 have depths at most 2k and 2k+1, hence at most six and seven.

For a C-run following V or B, an inherited V14 or B70 entrance has depth zero. Its deepest C11 has depth at most 2k. A terminal run has k<=3, so depth at most six. A run followed by V has k<=2, so the following V6,V11 have depths at most five and six. Fresh entry roots only reduce these bounds.

Therefore every positive node6 has depth at most six, and every node11 has depth at most seven. A C11 of depth seven can occur only in a terminal initial CCCC run, so it cannot parent a later macro's node4 inside the interval. A V11 cannot parent node4 by item 3. Every other possible parent of a node4 has depth at most six, including the explicitly checked B-prefix nodes. Thus every positive node4 also has depth at most seven. Nodes V14,B70 are roots, and all other B-prefix positive nodes have depth at most four.

Every positive node therefore has depth at most seven. Any nonpositive cursor child or boundary bud adds only one, giving the bound eight. The explicit feasible word CCCVV attains eight. QED, using the stated inherited fresh-tip lemma. The new certificate and this depth argument passed independent audit on 22 October 2026.

## 6. What this narrows, and what it does not

Inside any C/V/B interval, a single cut root can have at most

`1+4+...+4^8 = 87,381`

cursor descendants. This is deliberately much weaker numerically than the known total-duration fuel bound, but it applies per root and controls genealogy rather than time.

In a five-macro stream, no infinite ancestry ray can be contained in one C/V/B interval. More strongly, every segment of nine internal parent edges must span a U or Q occurrence if all its chronological intermediate macros belong to the five-macro stream. This locates a necessary renewal gate in the remaining subsystem. The gate may merely lie inside a token's long dormant lifetime: it need not itself be a node of that ancestral ray.

This does NOT prove finitely many ancestry ends or bounded global bush depth. U and Q can recur, and their role in enabling dormant tokens to reactivate remains the unsolved part. Nor may boundary buds be discarded; they can be consumed and branch after the interval ends. No statement is made about arbitrary trajectories with infinitely many adjacent bad ten-windows.

## Simplification after audit

The common-star producer and C11-separation lemmas may be replaced by the stronger elementary immediate-predecessor identity in `macro_seam_identity.md`: the RRRR terminal suffix and the next LLLLRL prefix fix that parent exactly. The audited closure is retained, but no claim of novelty or global strength attaches to these forced seam mechanics. The fresh-V and finite-depth argument remain substantive.
