# A cap-four top C-face component must be essential

23 October 2026. Independently analytically signed by the audit analysis.
It is a necessary condition, not a cap-four exclusion.

Let a complete white-input translating front have at most four visits at
every physical cell. Use the signed shifted stream height H and its global
maximum M. There is at least one clockwise face C with H(C)=M: the signed
global-maximum defect theorem supplies a unique maximum corner, and every
such unique maximum is at a C face.

Form a graph of the C faces with H=M, joining two when they share a primal
vertex. The graph is invariant under the full drift d. It has finitely many
face classes, all in a finite-width strip. Indeed the two exterior C-face
heights are c_low and c_low+1, whereas M>=c_low+2.

**Claim. Every component of this graph is essential on the full-drift
cylinder. Equivalently, each of its physical lifted components is infinite.**

For a primal vertex incident to such a face F, let r_F,r_G be the counts of
R visits turning around F and the opposite clockwise face G. The local
formula gives H(F)-H(G)=r_F-r_G. Hence r_F>=r_G. If r_F=0, both R counts
are zero. White alternation then makes the history empty, and its L-face
shifted heights exceed the C-face height by one, contradicting H(F)=M.
Therefore r_F>=1.

If H(G)<M, then r_F>r_G. Since there are at most two R reads in a cap-four
history, this forces r_G=0. The first read is R and turns around F. If
H(G)=M, then F and G belong to the same graph component, and the first R
turns around one of them. Thus every vertex incident to a fixed component
has its first R turn around an M-face in that same component.

Let V be the set of primal vertices incident to one fixed physical lifted
component. All vertices in V are read, as just shown. At the first visit to
p in V, its predecessor cell q lies on the boundary of the M-face around
which that first R turns. Hence q also lies in V. If F(p) is p's first
physical read time, then

    F(q) <= F(p)-1.

Every event has a predecessor because the front is bi-infinite. Therefore
V cannot be finite: taking a vertex with least F would contradict the
inequality. A finite C-face component would have finite V, so every
physical lifted C-face component is infinite.

Finally, the cylinder graph has finitely many vertices. A lifted component
of a finite voltage graph is infinite exactly when the corresponding
cylinder component has a closed walk of nonzero voltage. If every cycle
has zero voltage, path voltage from a fixed base is well defined and each
base vertex has only one lift in that component, making the lift finite.
The converse follows by repeating any nonzero-voltage closed walk. Since
the C-face adjacency graph is embedded in the cylinder, a nonzero-voltage
closed walk contains an essential cycle after decomposition into simple
cycles. This proves the claim.

The result does not prohibit an essential top plateau: such a plateau may
extend indefinitely along the drift. It justifies excluding contractible
or finite top C-face islands in cap-four synthesis, provided the imposed
height is known to be the GLOBAL maximum.

## Signed addendum: every C-superlevel set has no finite component

The same argument applies to EVERY integer threshold k, not just M.
In the physical plane form the graph of clockwise faces with H(C)>=k.
No nonempty component of this graph can be finite.

Suppose S were such a finite component. Let V consist only of the
actually read primal vertices incident to S. A finite nonempty face set
has a boundary corner whose opposite C face is outside S. At this corner
the inside C height is strictly larger, hence its R count is positive;
thus V is nonempty. At every boundary vertex the strict inequality and
cap four force the outside R count to zero. Its first R is therefore
around an inside face. At an internal vertex both C faces lie in S, so
any first R again belongs to S. The predecessor of the first read at any
p in V is a read vertex in V with strictly smaller first time. This is
impossible for a finite nonempty V. Empty internal vertices must be
omitted from V, and have no role in the predecessor argument.

Above both exterior C heights the cylinder superlevel graph is finite,
so each component must be essential by the earlier voltage argument.
The assertion does not exclude essential ridges, even nested ones.
