# The heading-dependent identity/nine transport architecture

23 October 2026, 02:33 UTC. Complete finite conflict trees independently reconstructed
and signed. This is a scoped architecture exclusion, not a
classification of unit-scale models.

## Genuine new freedom and exact local alphabet

There are eight independent states (incoming heading, turn), ordered
N-R,N-L,E-R,E-L,S-R,S-L,W-R,W-L. Each may use either its one-step identity
or one of the six internally ant-legal, charge-preserving nine-step words
with the same final heading and the same unit displacement as that turn.
Images are interpreted in their own incoming-heading frame. Opposite
headings are NOT required to share images. The two palettes are

R: R; RRRRLLLLR; RLRRRRLLL; RLLRRRRLL; RLLLLRRRR;
   LLRRRRLLR; LLLRRRRLR.
L: L; RRRLLLLRL; RRLLLLRRL; LRRRRLLLL; LRRLLLLRR;
   LRLLLLRRR; LLLLRRRRL.

The images have variable length1 or9, so this is not the old pure identity
p(9n)=p(n). Instead its coarse checkpoints have state-dependent time lengths.
The current incoming-heading state supplies context genuinely absent from
the two-turn morphisms. Every image preserves exact charge and unit geometry.

## Root coverage

A first-state map preserves the incoming heading and maps its two turn
states into themselves. Hence every first-state cycle has length1 or2.
Global quarter rotation permits initial incoming north because all four
heading choices remain independent.

For a growing fixed root, its image must be one of the four nine-step
images starting with its own turn; the identity image does not grow.
Each of the other seven states has seven choices. We test both root turns,
covering2*4*7^7=6,588,344 ROOTED controller cases.

A two-cycle requires the N-R image to start L and the N-L image to start R.
Each has two choices. Both roots are tested for each of the four pairs,
with seven choices at each of the other six states:8*7^6=941,192 cases.
These counts include different roots of the same controller; they are not
counts of distinct controllers. Transient first-state letters are not new
rooted power-limits. No arbitrary shifted-language exclusion is asserted.

## Exact on-demand chronological trees

For a fixed root s, build its state fixed point from P=phi(P). The root is
known first, and each subsequently needed image is assigned only when the
coarse input cursor reaches its state. Expanding the nonidentity root leaves
a positive queue of known coarse states, so generation continues even if
some or all later images are identities. Every emitted fine letter is
checked immediately against the last turn at its lattice cell. A repeated
same turn is a literal contradiction on every initial coloring.

For a two-cycle use P=phi^2(P). A pending stack expands two levels lazily,
again assigning each original phi-image once. The root-pair images are
fixed first. All conflicts in these trees occur inside phi^2(root).

A pruned leaf with u unassigned states represents exactly7^u completions.
The leaf weights sum to the expected controller count in every root case.
No branch reaches the10,000-read cap, and no positive certificate is inferred
from a finite prefix.

Fixed roots:194 assignment-tree nodes and166 conflict leaves per root,
latest zero-based conflict43. Two-cycle roots: either71 nodes/61 leaves or
218 nodes/187 leaves, latest conflict50. Combined:1,544 nodes,1,324 conflict
leaves, covering7,529,536 rooted cases. No survivor.

## Frozen artifacts

- search_heading_transport.py/.json/.records.json: fixed-root trees.
  Record digest9520b496ad2c3a1156564fc68c043883091b6e66f9d28176a01d72226805b88c.
- search_heading_transport_cycles.py/.json/.records.json: two-cycle trees.
  Record digest359dd7e200aa3efb76a99e01b22bb6fd72362f746af892139f9b15fa0d88b8c5.

The cycle script imports the author's palette generator; that is code reuse,
not independent verification. An independent inventory and depth-eight literal replay checked every cube,
and pairwise-disjoint assignment cubes plus product volumes proved coverage.
See ../../audits/check_heading_transport_independent.py/json. Do not enlarge the local word length just
because this alphabet failed. The useful unresolved directions are different
local transport mechanisms or structural constraints on all-time reuse.
