# A strict order for every finite one-sided driven block

Research date: 22 October 2026. Status: analytic theorem, independently audited, with exact finite exploratory checks. It is a new reduction-level observation, not an all-height barrier theorem or an autonomous ant counterexample.

## 1. The driven problem

Use the rectangle 0<=x<W, 0<=y<H in the sector where x+y odd cells are entered horizontally (H cells) and the other cells vertically (V cells). A driver may repeatedly start the ant at (0,y,E) for any odd y. A run is successful for continuation only when it stays inside the vertical boundaries and exits left; the next entry row is arbitrary. A vertical exit terminates its branch. A right exit is the target of the pristine-barrier search.

The driver changes no cell itself. Each excursion is the literal ant rule. The initial block coloring can be arbitrary for the theorem below, not necessarily white.

Set eta(x,y)=c(x,y) on H cells and 1-c(x,y) on V cells, and define the finite binary integer

   R(c)=sum_{x=0}^{W-1} sum_{y=0}^{H-1} 2^(Hx+y) eta(x,y).

Higher columns dominate lower columns, and higher rows dominate lower rows within a column.

## 2. Strict left-return theorem

Every vertically safe complete excursion from the left boundary back to that boundary strictly increases R.

Proof. Let x* be the rightmost column read in the excursion. Every visit to x* enters horizontally from the left, makes one vertical move within the column, and exits horizontally to the left. A right exit would read a column farther right, contradicting the definition of x*, and there are no entries from the right. The column reflection lemma therefore says that each visit moves one occupancy particle upward by one row: a lower eta=1 becomes 0 and the adjacent upper eta=0 becomes 1.

Each such move strictly increases that column's binary word sum_y 2^y eta(x*,y). At least one occurs. All columns to the right of x* are unchanged. The net binary increase at x* contributes at least 2^(H x*), while the entire collection of lower columns can decrease by at most 2^(H x*)-1. Hence R_after-R_before>=1. QED.

The proof makes no assumption about the driver's earlier or later choices, the time spent inside the block, its old colors, or a periodic trace. It applies even though the driver need not be realizable by a physical autonomous exterior.

## 3. Consequences

- The complete mask graph containing safe left-return transitions is a DAG for EVERY finite H,W and every starting coloring.
- A driven path in that fixed block makes at most 2^(HW)-1-R(initial) safe left returns before a vertical or right exit, or before it stops. This is a crude finite bound, not the sharp count of reachable masks.
- A complete finite invariant certificate remains a valid way to prove a width barrier. The strict order explains why its reachable mask graph has no directed cycles, but does not imply that right exits are absent.
- In an infinite half-strip, an infinite safe driven execution cannot remain in a finite horizontal prefix: its repeated left-return mask states would violate the finite-block bound; an infinite internal excursion would violate finite-domain escape. It must reach arbitrarily far right.

The last statement does not establish existence of an infinite safe driven execution, and does not turn one into an autonomous finite-seed ant.

## 4. Exact semidecidability and the remaining quantifiers

For fixed H,W the finite block's right-reachability problem is decidable by exploring its complete masks and entry rows. For blank initial colors let Reach(H,W) denote the existence of a finite vertically safe driven prefix reaching the right boundary. It is monotone in W: Reach(H,W+1) implies Reach(H,W).

Thus the existence of a finite pristine barrier at height H is

   exists W, not Reach(H,W),

which is c.e. uniformly in H. Failure at a fixed height is the co-c.e. statement forall W Reach(H,W). The all-height barrier candidate has a Pi_2 presentation forall H exists W not Reach(H,W). This is a presentation, not an undecidability or completeness result.

Failure of a barrier at fixed H is equivalent, nonconstructively, to existence of an infinite safe driven path reaching unbounded x. One direction is immediate. For the other, consider the finitely branching tree of safe step-by-step histories, including the finitely many driver choices at left exits. Every finite block has a finite bound on the total length of a safe history confined to it: there are finitely many left returns by the theorem, and each internal excursion has a finite uniform finite-domain escape bound. If Reach(H,W) holds for every W, this tree has arbitrarily long branches. Koenig's lemma yields an infinite path, and the finite-block bound forces its x-coordinate to be unbounded.

The path supplied by this compactness argument need not be a computable strategy or a finite controller. No effective extraction is claimed. In particular it does not furnish the finite autonomous exterior required for a physical strip-confined orbit.

An actual finite-seed tail confined to height H and unbounded horizontally would imply failure of the pristine barrier property at H (choose virgin blocks beyond its finite support and use the actual exterior chronology as a driver). The converse is not established.

## 5. Computations and a sector caveat

analyze_barrier_graph.py independently reconstructs small complete left-return graphs using the existing exact two-read local transition. The known barriers at (H,W)=(4,3),(5,3),(6,5),(7,6),(8,8) have respectively 8,14,77,184,9438 reachable masks and maximal return counts 4,5,13,15,38. All are DAGs; no extrapolation to larger heights is made.

The exploratory (H,W)=(3,1) case in that script uses H rows at odd y. It is NOT the height-three bottleneck sector from the earlier proof (which has H rows on both boundaries), and it has a right exit. This is not a contradiction or a height-three counterexample: the correct barrier can be placed at the other x parity. The all-height candidate may choose either parity; translating the rectangle by one column exchanges them. Always retain the sector when stating a particular certificate.

## 6. The height-only barrier language is nevertheless recursive

Let B(H) mean that some finite pristine barrier width exists at height H, with the compatible sector specified above. For H'<=H, every safe driven crossing of a height-H' block embeds in the height-H block by adding white rows above it. The entry rows remain compatible and the same literal prefix never reads the added rows. Consequently

   B(H) implies B(H') for every H'<=H.

Thus {H>=1:B(H)} is either all positive integers or a finite initial segment. As a fixed mathematical set it is recursive: in the first case the constant YES program decides it; in the second, comparison with its finite cutoff decides it. This does not give us that program, its cutoff, or a proof of which case holds.

In particular a computable many-one reduction of HALT to the height-only predicate B(H) cannot exist. A uniformly variable family of rules or backgrounds could have different complexity, but is not this fixed problem.

This is compatible with its earlier c.e. presentation and with the Pi_2 presentation of the universal statement. A presentation is an upper bound, not a hardness theorem. The universal assertion that the downward-closed set is all integers can remain mathematically unresolved even though each possible resulting set is recursive.

If barriers exist at every height, their minimum width function is total computable by finite search. If there is a failing height, only finitely many minimum widths exist, so that partial function has a total computable extension by a finite table. Again, this is a nonuniform existence statement, not an algorithm we currently know how to instantiate for arbitrary heights.
