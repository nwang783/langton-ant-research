# Minimal heading defects: exact local classification

Author certificates, independent semantic review pending (23 October 2026).
This is distinct from preserving the full coarse pose: only the positions at
the ends of two coarse turns are retained, while the boundary heading may be
the coarse heading or its opposite. The pairing alignment stays fixed.

## 1. Exact minimal local geometry

Normalize a coarse pair's incoming heading to north. Its endpoint has both
coordinates odd. Every fine replacement therefore has length 2 modulo 4.
An endpoint whose final heading is the coarse final heading has a unique
length-two path, for either incoming heading sign. It resets the heading.
An endpoint whose heading is opposite cannot be reached in two moves.
The minimum is six moves: the three vertical directions are (y,y,-y), while
the three horizontal directions contain two x and one -x. There are exactly
three geometric paths, all with six distinct read cells, hence all internally
legal on their required local colors. Changing the incoming heading sign
changes only the first turn, not these physical paths.

The supplied architecture allows precisely these MINIMAL transitions:
length-two reset or any of the three length-six flips, from either incoming
sign. It does not include longer reset/flip routes. Adjacent boundary signs
must match; this is not an independent image selection that ignores headings.

Full primitive fields and all312 single flip/reset contexts are retained in
minimal_pair_heading_bridge.json. Only one of those contexts is prepared-
periodic legal, and it is the already known P108 unit-image insertion.

## 2. The genuine escape versus removable square insertions

If the first horizontal move is -x, the six-read path is a genuine backward
route. The other two paths first execute the coarse pair's two physical moves,
then a four-move square at its endpoint. Such a square returns to the same
cell with opposite incoming heading and flipped cell color.

If no backward routes occur, choose each coarse boundary BEFORE its optional
square rather than after it. Combining that square with the first move of
the next coarse pair gives a five-read unit-pose image. Internal alternation
at the square's source forces precisely RLLLL for a coarse R or LRRRR for a
coarse L; otherwise the source would read the same color twice. Every other
coarse move is unchanged. Thus these heading defects can be recut into the
old five-read unit alphabet, but this statement must not be applied to the
backward route without excluding it.

## 3. Stronger seven-period local classification

Every physical cell can be used by coarse periods whose indices differ by
at most THREE; this is derived from the complete phase footprints. Consider
seven periods with independent choices for all364 pairs and all365 boundary
heading signs, including BOTH free endpoint headings. Give EVERY physical
cell an arbitrary initial color and leave the final board unrestricted.

A literal color circuit groups events by physical cell, ordered by
(period index,pair index,local read index). A selected event must see its turn
color and flip that same bit. Pair choices constrain their incoming and
outgoing heading signs. This is exact finite chronology, with no periodic
choice equality or prepared-input premise.

For the central period, the complete result is:

* Pair alignment0: only the unchanged inverse104 is possible.
* Pair alignment1: only unchanged inverse104 or one specified P108 assignment
  is possible. P108 is the same old L->LRRRR insertion, at coarse phase30 of
  this cyclic cut. Both central boundary headings are the coarse headings.

To certify completeness, forbid those one/two entire central assignments.
Both problems are UNSAT. The CNFs have61,517/61,518 clauses and13,722/13,698
variables. Monotone RUP proofs have2,062/1,021 additions; the retained generic
independent checker accepts both without RAT or deletions.

Consequently, subject to semantic audit, EVERY one-sided infinite legal
schedule in this exact minimal-heading architecture has, after its first
three periods, only identity periods (alignment0) or arbitrary V/P108 periods
(alignment1). This is stronger than just ruling out stationary controllers.
Their charges are -12 and -8, so no such infinite schedule can start from a
finite black seed, regardless of input shape or previous finite preparation.
No claim is made for changing pair alignments, other scaffolds or nonminimal
heading transitions.

Sources: check_heading_defect_backward_window.py,
check_heading_defect_local_classification.py,
heading_defect_local_classification/cut{0,1}.cnf/rup/result.json.
The intermediate backward-route-only and stationary-controller certificates
are retained but are not needed once this stronger result is reviewed.

## 4. Genuine nonstationary prepared positives

The two accepted central words are not merely formal allowances. EVERY
sequence of V and P108 is internally ant-legal on its inferred prepared input.
This can be proved by complete same-cell locality: every pair of reads at the
same cell lies within four coarse periods; all16 binary four-period words are
legal. The retained stronger controls replay all128 seven-period binary words.
Thus arbitrary aperiodic schedules are possible on suitable INFINITE prepared
boards. This does not imply finite-support realization or autonomous choice
on a common fixed board.

There is also an exact disjoint local-field explanation. In alignment1 start
at(0,0,S), let D=(-2,-2), and let V be the cyclically shifted inverse104.
P108 replaces the L at phase30, read at p=(1,7,N), by LRRRR. The four affected
cells are the square

    p=(1,7), q=(0,7), u=(0,8), v=(1,8).

The baseline infinite-period histories at those physical cells, relative to
the insertion's period, are:

    p: (-1,10,R),(-1,14,L),(-1,26,R),(0,30,L)
    q: (0,31,L)
    u: no baseline reads
    v: (-1,13,L).

The inserted square adds R reads at q,u,v,p before resuming the old phase31
L at q. Hence it removes q from the initial black demand and adds p,u,v to
the final black set. At the first period, the absent period-minus-one reads
are simply omitted; the same statement remains true. All squares translated
by rD are disjoint. Therefore modifications at different periods do not
interfere, giving exact COMPLETE field formulas for any n>=1 and set S of
P108 periods:

    I_S = I_V(n) minus {q+rD : r in S},
    O_S = O_V(n) union {p+rD,u+rD,v+rD : r in S},
    XOR_S = XOR_V(n) symmetric-difference the corresponding four-cell squares.

The baseline has input mass12n+13 and output mass13; so these become
12n+13-|S| and13+3|S|. In particular the arbitrary binary choice costs linear
prepared fuel even though it is genuinely nonstationary. The full local
histories, not merely mass accounting, justify the independence.

Controls: check_heading_defect_controls.py and
heading_defect_local_classification/controls.json. Thirty-seven fixed
assignments compare the entire color circuit with literal paths (five legal
positives); all128 binary seven-period words are replayed with complete fields.
