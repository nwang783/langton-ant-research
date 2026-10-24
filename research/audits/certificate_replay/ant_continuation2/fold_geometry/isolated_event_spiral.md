# An aperiodic infinite-background spiral with isolated J10 events

Date: 22 October 2026. This is not a finite-seed counterexample. It identifies a limitation on a possible geometric proof for the five-block component H.

## Statement

Use the before-marker U, C, and V blocks certified in the first continuation. There is a computable infinite initial coloring whose ant turn stream is

\[
\prod_{i=0}^{\infty} U^{5\cdot2^i}CV.
\]

This stream is physically consistent, has infinitely many C turns, is not eventually periodic, and has no adjacent forbidden length-ten windows. Its forbidden windows are exactly the isolated events supplied by the V blocks, apart from any choice of finite history before time zero. After a finite prefix its 149-history path is in the nonstandard component H.

Its first K complete spiral legs require exactly

\[
m_K=4+25(2^K-1)+2K
\]

initially black cells in their read footprint. Thus this construction necessarily uses infinitely many initially black cells. Every finite prefix is realized by its finite first-L seed.

In particular, **there is no uniform bound on the number of turns based on physical five-block feasibility alone**, valid for arbitrary initial colorings or for all finite prefixes independent of their seed mass. An H capture proof must exploit finite support or a resource depending on the initial field. This does not rule out a turn bound depending on seed mass.

## Exact local geometry

All coordinates are before-marker coordinates, with north initially (0,1). U has length 28, displacement (0,4), unchanged heading, and read footprint in [-1,2] x [-1,4]. Let D=CV. Direct tracing gives D length 33, displacement (-3,2), final heading west, and footprint in [-3,2] x [-1,3]. The finite word UCVU is physically feasible.

Consequently the leg

\[
F_i=U^{n_i}D,\qquad n_i=5\cdot2^i,
\]

has displacement (-3,4n_i+2), turns left, and has footprint contained in

\[
[-3,2]\times[-1,4n_i+3]
\]

relative to its start and heading.

Two consecutive legs can interact only at the checked UCVU interface. In coordinates of the earlier leg, its successor starts at (-3,4n_i+2), facing west. The entire successor footprint has x<=-2, while the earlier U rail has x>=-1. The earlier D can meet only the first U of the successor: later successor U copies have x<=-6, while D has x>=-3. Within the earlier leg, D meets only its final U copy because D's minimum height is 4n_i-1 and every earlier U copy ends at height at most 4n_i-4. Thus all adjacent interactions are contained in UCVU.

## Separation of all nonadjacent legs

Write S=16^k. The four starts in group k are

\[
\begin{aligned}
p_{4k}&=(8S-8,-4S+4),\\
p_{4k+1}&=(8S-11,16S+6),\\
p_{4k+2}&=(-32S-13,16S+3),\\
p_{4k+3}&=(-32S-10,-64S+1).
\end{aligned}
\]

Their headings are respectively north, west, south, east. Adding the four rotated displacements returns the heading and gives the first formula with S replaced by 16S, so these formulas hold for every k by induction.

Their complete read rectangles are:

| Leg | x interval | y interval |
|---|---|---|
| 4k | [8S-11,8S-6] | [-4S+3,16S+7] |
| 4k+1 | [-32S-14,8S-10] | [16S+3,16S+8] |
| 4k+2 | [-32S-15,-32S-10] | [-64S,16S+4] |
| 4k+3 | [-32S-11,128S-7] | [-64S-1,-64S+4] |

The bounding extrema of all rectangles through a complete group are exactly [-32S-15,128S-7] x [-64S-1,16S+8]. Comparing with the preceding group, and omitting the immediately preceding rectangle, gives these sufficient separation bounds:

1. For leg 4k, k>=1, all earlier nonadjacent rectangles have x<=S/2-6. Its own minimum x is 8S-11. The gap is positive because (15/2)S>5.
2. For leg 4k+1, k>=1, all earlier nonadjacent rectangles have y<=S+8. Its own minimum y is 16S+3. Use 15S>5.
3. For leg 4k+2, k>=1, all earlier nonadjacent rectangles have x>=-2S-15. Its own maximum x is -32S-10. Use 30S>5.
4. For leg 4k+3, all earlier nonadjacent rectangles have y>=-4S-1. Its own maximum y is -64S+4. Use 60S>5.

The empty earlier sets for the first two legs need no check. In group zero, leg 2 is disjoint from leg 0 because its maximum x is -42 and leg 0's minimum x is -3. The fourth inequality also covers group zero.

Thus no nonadjacent pair of legs interacts. Combined with the exact adjacent-interface check, this proves alternating requested colors on every successive visit to each cell for the entire infinite word.

## Initial coloring and exact fuel

Make a cell initially black precisely when its first requested letter in the infinite word is L, and make every other cell white. The proved alternation property makes this a well-defined coloring that realizes the complete infinite word. It is computable because the spiral rectangles eventually lie beyond any fixed cell, so only finitely many explicitly computable legs can read that cell.

The local footprint checks give the following first-L counts. The first U costs nine initial black cells, each subsequent U in a straight run costs five, C at the end of a nonempty U run costs one, and the following V costs one. At the interface CVU, the next U costs exactly five new initial black cells. All other interactions are absent by the separation proof. Hence a concatenation of K legs costs exactly four common initial cells plus five per U and two per CV pair. Summing n_i gives the formula for m_K.

## Factor-language claims and limits

Each block starts with the 12-letter marker M=`LLLLRLRRRRLR`. Its completed marker-to-marker word has no internal occurrence of M. Exact inspection of M followed by each after-marker word shows no forbidden ten-window for U or C, and exactly one for V. That V event ends at after-marker index 1, or equivalently at before-marker index 13. Events in distinct V blocks are separated by 28n_{i+1}+33 updates, so no two are adjacent and their gaps tend to infinity.

An eventually periodic binary event sequence with infinitely many events has bounded gaps. Therefore this stream is not eventually periodic. The W104 and T24 components are simple periodic cycles, so the exact finite graph classification forces this physical infinite stream eventually into H.

The construction proves neither a finite-support obstruction path nor capture of H. It does rule out trying to transplant the source ten-language three-fold contradiction to all H turn sequences without a finite-support premise. The unresolved task remains to show that **every** physically consistent infinite turning path in H needs infinitely many first-L cells, including paths whose later legs reuse earlier wakes rather than separating as this spiral does.
