# General heavy-edge routing from complete white alternation

23 October 2026, 08:04 UTC. Independently signed analytic extension (audit KT addendum).
These are necessary flow-graph structures, not front exclusions.

Let f(e) be the complete directed physical edge traversal count in a
bi-infinite complete initially-white front. The checker sector makes every
used physical edge directed consistently. A vertex with n complete reads
has ceil(n/2) R and floor(n/2) L turns. If a path uses one incoming port
of count u and one outgoing port of count v, their overlap contains at
least u+v-n reads. Every overlapping read makes that same R or L corner.

## A. Cap4m: no finite physical cycle at flow at least3m

For an integer m>=1, suppose n<=4m everywhere and keep edges f>=3m.
Each vertex has at most one retained incoming and outgoing port since
2(3m)>4m. At an internal vertex, the overlap has at least6m-n reads of one
turn type. If n<=4m-1, this exceeds ceil(n/2), impossible. Hence n=4m.
Both retained port counts are exactly3m, since increasing either would
make the overlap exceed2m. At a R corner, all2m R reads use that corner;
at a L corner, all2m L reads use that corner.

Thus the clockwise-first-R/counterclockwise-last-L finite-polygon argument
of cap_four_count_three_cycle_exclusion.md applies verbatim: the retained
flow graph has no finite physical directed cycle. Essential cylinder
cycles/infinite lifts remain possible. Edges of count>3m are isolated
retained edges, since they cannot meet an internal retained vertex.

## B. Cap4m+1: every heavy component is an arc of at most three edges

For m>=1, suppose n<=4m+1 everywhere and keep edges f>=3m+1.
Again each retained in/out degree is at most one. An internal vertex needs
overlap at least6m+2-n. This is impossible for n<=4m, so n=4m+1. The overlap
is then at least2m+1. An L corner is impossible because there are only2m L
reads. A R corner uses ALL2m+1 R reads, and both retained ports have count
exactly3m+1. Therefore every internal retained vertex turns R and its first
read uses that high-flow corner.

Four successive right-turning unit edges form the boundary of one unit
clockwise face and return to their physical starting vertex. Such a cycle
is impossible: each vertex's first read has its predecessor at the preceding
cycle vertex, contradicting the least first-read time on those four cells.
A directed simple path in which every internal corner is R therefore has
at most three edges. No infinite physical retained component exists, and
hence no retained directed cycle can be essential on any full-drift cylinder.
Edges of count>3m+1 are isolated retained edges.

For capFIVE (m1), every edge of count at leastFOUR belongs to a clockwise
unit-face boundary arc of length1,2 or3; a countFIVE edge is isolated.
This has no drift, period or width bound and makes no reflection argument.
It does not say such an arc is an actual front or forbid larger lower-flow
networks. A cap-three doubled-edge cycle is outside these hypotheses,
which deliberately avoids the earlier false forest assertion.
