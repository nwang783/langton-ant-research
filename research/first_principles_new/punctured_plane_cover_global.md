# Exact punctured-plane interpretation of the free-product coset model

22 October 2026, global-constraints analysis. This identifies the covering geometry. It does not prove that square-ant colors lift autonomously, nor the highway conjecture.

## 1. The fixed-sector midpoint graph

Fix the sector in which even physical cells have vertical incoming edges and horizontal outgoing edges; odd cells have the reverse. Every undirected edge of the physical square grid then has exactly one permitted orientation. Identify a head state with the midpoint of its incoming directed physical edge. The two incoming headings allowed at one physical cell correspond to two opposite midpoints on its boundary.

From an incoming midpoint at a cell, draw the R and L transitions as quarter-turn arcs to the two outgoing midpoints. These arcs lie inside that physical cell. The resulting undirected midpoint graph is a square medial graph with two types of faces:

1. A face around an original unit plaquette has four consistently directed transitions, all R or all L. The R and L types alternate among neighboring plaquettes.
2. A face around an original physical cell is a diamond. Its boundary alternates a forward transition and a reverse transition. From either incoming corner, one half-boundary is R followed by reverse L; the other is L followed by reverse R.

Attach a disk to every face of the first kind, but not to the physical-cell diamonds. Call the resulting complex Y. This is a convenient pinched CW model of a plane punctured at every physical cell. One may thicken the meeting points without changing its homotopy type.

A direct equivalent description avoids the word “punctured”: each filled plaquette disk meets exactly four neighboring disks, at four distinct midpoint vertices, with no triple intersection. Replace each disk by the four-arm tree connecting its center to its four meeting vertices. This is a homotopy equivalence fixing the meeting vertices. The resulting incidence graph is the ordinary dual square lattice. In particular its universal covering graph is the four-regular tree.

## 2. Universal cover as a tree of squares

Let G = C4 * C4, with generators R and L. Form X by taking the Cayley graph of G and filling each R four-cycle and each L four-cycle with one disk, not four duplicate relation disks. Each vertex lies in exactly one R-square and one L-square. The incidence graph of these squares is the Bass–Serre tree: its vertices are the left cosets g<R> and g<L>, and the edge joining them is indexed by g.

The free-product normal form shows this incidence graph is a tree. Therefore X is simply connected: every finite loop lies in a finite tree of disks, and a finite tree of disks joined at vertices is contractible.

Starting from any physical midpoint state, follow the labeled word g to obtain a midpoint in Y. The relations R^4 = L^4 = 1 hold physically, so this defines a map X -> Y. It maps each filled square isomorphically to its corresponding plaquette disk and preserves the local cyclic arrangement at all vertices. It is a covering map. Equivalently, lift the four-regular incidence graph to its tree and replace each lifted vertex by the corresponding labeled square. Thus X is precisely the universal cover of Y, not merely a metaphorical tree approximation.

This statement concerns topology and labeled head motion. It does not say that deleting an R^4 or L^4 subword preserves a square ant's lamp history. Such a deletion usually changes four lamps and is not a legitimate dynamical reduction.

## 3. Cosets are lifted physical-cell boundaries

Put h = R L^(-1) = R L^3 and H = <h>. Start at an incoming midpoint of one physical cell, represented upstairs by g. Traversing half of that cell's diamond boundary is R followed by reverse L. Hence its lifted incoming corners are exactly

    g, g h, g h^2, ... and g h^(-1), g h^(-2), ... .

The intervening outgoing corners are g h^k R. Since h is a nontrivial cyclically reduced free-product word, it has infinite order. A lift of the diamond boundary is consequently a bi-infinite line, and its incoming corners form exactly the right coset gH.

Every component of the preimage of a physical-cell diamond has this form. Two distinct lifts of the SAME physical-cell diamond are disjoint, because they are different components of the preimage of that embedded cycle. This is stronger than saying merely that two arbitrary coset boundary lines have limited overlap; lifts of different physical cells can meet.

After collapsing filled squares to their incidence stars, each such lifted diamond is the lift of a four-edge facial cycle of the dual square grid. It becomes a bi-infinite geodesic in the four-regular covering tree. Thus the unresolved physical no-A-B-A statement can be phrased exactly: an ant trajectory cannot meet one of these geodesic lifts A, then a distinct lift B of the same dual face, then A again, in the chronology of visits to that physical cell.

## 4. A useful but conditional first-violation reduction

Suppose one could prove no A-B-A for every autonomous coset-ant trajectory, regardless of its initial coset lamps. Then the square-ant no-A-B-A property would follow by a first-violation argument.

Indeed, before the earliest A-B-A arrival in a square-ant trajectory, the visits to each physical cell are grouped into contiguous blocks of distinct cosets. Give each coset the color seen at its first visit. Within its single chronological block, physical color alternation is exactly autonomous coset-lamp alternation. Thus the entire lifted trajectory up to the alleged violating arrival is a legal autonomous coset trajectory. The autonomous no-A-B-A theorem would forbid that arrival. No choice of the lamp read at the final arrival is needed for this argument.

At present the autonomous no-A-B-A premise has not been established. It may be false for unrestricted initial coset lamps. If it is false, this reduction diagnoses the extra property that must use physical compatibility of distinct coset lamps, rather than the abstract tree geometry alone.

## 5. What remains missing

The covering construction supplies no parity theorem for shared physical lamps. A physical update changes the shared color seen at every lift of that cell, whereas an autonomous coset update flips only the one visited lift. A geometric proof still needs a chronological separation or parity statement. An innermost-bigon or planar noninterleaving argument is a plausible route, but no such lemma is claimed here.

Even a legal autonomous lift would only make the abstract six-visits-per-coset result applicable. Distinct cosets can project to one physical cell, and a finite physical seed can lift to infinitely many initially black cosets. Therefore neither physical transience nor standard highway attraction follows from this covering description alone.
