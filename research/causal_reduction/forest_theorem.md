# Exact finite-root token forest

## 1. Conventions and inherited local equivalence

Normalize by translation/rotation to ant at (0,0), heading north; take white/R, black/L, flip then move. The checkerboard-axis sector is then fixed. In coordinates with headings N,E,S,W=0,1,2,3, the Tait cursor is `v=p+o_h` with

`o_N=(0,-1), o_E=(-1,-1), o_S=(-1,0), o_W=(0,0)`.

A physical black cell q=(x,y) is a present Tait edge

- `{(x,y-1),(x-1,y)}` if x+y is even;
- `{(x-1,y-1),(x,y)}` if x+y is odd.

The Tait vertices have odd coordinate sum. A physical R inserts the missing edge incident to the cursor, keeps the cursor fixed, and advances its port clockwise. A physical L deletes the present edge, crosses to its other endpoint, and advances clockwise there. This exact reformulation is inherited, not assumed to imply capture.

Call the time interval starting at the input, or immediately after an L, and ending with the next L a **cursor node**. All its R writes occur at one Tait vertex. Except possibly the initial node, the arriving edge was just deleted. Consequently the number r of inserted edges is in {0,1,2,4}. The initial node may also have r=3. Every node finishes within five physical updates.

## 2. Token parentage theorem

Give every initially black edge its own virtual root. The initial cursor node is one additional root. Each R insertion creates one token, labeled by its producing cursor node and insertion slot. The token persists until that edge's next read, if any. At its consuming L, the next cursor node is made the child of its producer. If the consumed token was initially black, its child is attached to that token's virtual root. If a token is never consumed, record an eternal terminal bud instead of a child.

**Theorem.** This creates an exact rooted forest with at most |B_0|+1 roots. Every ordinary node has exactly r offspring when terminal buds are counted, with r in {0,1,2,4} except for the possible initial r=3. Each non-root cursor node has one parent, strictly earlier in physical time. A parent-to-child displacement is either zero or one Tait-lattice edge. No lifetime or written information is omitted.

**Proof.** Every L deletes exactly one present edge. That edge either survived from the input or was most recently inserted by one unique R. No intermediate read can occur during the token's lifetime, because the first such read would delete the token. Thus parentage is unique. If the token was created inside the immediately preceding cursor node, its child still begins only after the consuming L; in particular the isolated-star r=4 case creates no self-cycle. Parent node time is strictly less than child node time, so there are no directed or undirected ancestry cycles. Every insertion has exactly one eventual child or one eternal bud, and no token can be used twice. The finite input gives the stated roots.

If a producer is at v and its inserted edge is {v,w}, consumption from v places the child at w. Consumption from w places the child at v. These are respectively a forward and backward consumption. This proves the displacement statement. QED.

The r values are **not** the number of descendants or a monotone resource. An r=4 node copies its label into four physical edge lifetimes. An initial bit can therefore have arbitrarily many generations of descendants. The blank orbit itself has one root and an infinite forest.

## 3. Productive-ray obstruction, with finite side branches retained

Assign each bad ten-turn window to the cursor node containing its final update. (Initial-window indexing changes finitely many marks only.) Each node contains at most five updates and thus at most five such marks.

Call a node productive if its descendant subtree contains infinitely many marks.

**Corollary.** Infinitely many bad ten-turn windows imply an infinite parent-child ray all of whose nodes are productive.

**Proof.** The forest has finitely many roots, so one root has infinitely many marked descendants. It has finitely many children, so at least one child has infinitely many marked descendants. Repeat. Strictly increasing node times give an infinite ray. QED.

Crucially, the ray itself need not have infinitely many marks. A comb can carry all marks on finite bushes attached to an unmarked spine. Any argument that ignores such bushes is incomplete. Nor must different marks descend from different input bits.

Conversely, the existence of a productive ray implies infinitely many marks by its definition. Thus this is an exact structural obstruction, not a solved finiteness theorem. It replaces an unsound defect-only last-writer graph with a complete physical genealogy.

A crude universal depth estimate is available: if N cursor nodes have occurred, maximum ancestry depth d satisfies

`N <= (|B_0|+1)(4^(d+1)-1)/3`.

This records unavoidable self-reproduction, not disorder: it also holds on the standard highway.

## 4. Why literal cycles and quotient cycles differ

The exact forest has no directed cycle because time increases. A finite quotient, for example by translation and period, CAN have cycles: these represent new tokens produced by later copies of earlier nodes. The standard highway has two such renewable cycles, proved separately in `standard_forest.md`.

Therefore merely proving that literal last-writer ancestry is well-founded backwards does not rule out infinite forwards renewal. A successful rank must exempt the standard renewable cycles and control all the retained branches, not simply forbid cycles in a graph whose edges already point forward in time.

## 5. Unproved temptations explicitly excluded

None of the following has been established:
- every genealogical ray escapes every finite set;
- the forest has at most two infinite ends;
- a productive ray itself visits infinitely many bad windows;
- all forward producer-child steps eventually point in one direction;
- a finite number of roots bounds descendants or branch count;
- standard two-spine geometry follows from r=4 alone;
- bounded side-branch depth bounds the time before a side token is consumed.

In particular a token on a side branch may wait arbitrarily long before consumption. A depth-only condition is not a black-lifetime bound.
