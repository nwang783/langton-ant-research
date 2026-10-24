# A disconnected joint-forest ladder: geometry survives, actual colors do not

24 October 2026. Author construction and six-leaf cover; independent audit
pending. This is a proof-method countercontrol and a failed fixed-geometry
construction, NOT a literal disconnected-union ant trajectory.

## 1. The precise open connectivity question

The undirected union of the actual first-C-entry and last-C-exit forests is
connected in all five retained standard/prepared controls. This does not prove
connectivity in every actual controller. The single event cycle does not by
itself supply a path in its extremal subgraphs. The following example shows
that even planar C-lattice geometry and nonbacktracking do not repair that
logical gap. Actual read alternation is still essential.

## 2. One explicit planar, nonbacktracking periodic C walk

Use square coordinates (n,j) on the C lattice, with physical lower-left face
coordinates

    c(n,j)=(n-j,n+j-1).

Write A_n=(n,0), B_n=(n,1), L_n=(n,-1), H_n=(n,2). Take the following exact
17-transition path, then translate it by one n unit and repeat:

    A0,A1,L1,L0,A0,B0,B1,H1,H0,B0,A0,A1,B1,H1,H0,B0,B1,A1.

Each transition is a C-lattice nearest-neighbor step. There is no immediate
reverse edge, including at the seam. Its full physical drift is(1,1).
The graph is an embedded four-row ladder, although the walk revisits vertices.

With first/last times measured ONLY in C-transition indices here, its four
full-drift face classes have first-parent and last-successor rows as follows:

- A_n: first parent A_(n-1), last successor A_(n+1).
- L_n: first parent A_n, last successor A_n.
- B_n: first parent B_(n-1), last successor B_(n+1).
- H_n: first parent B_n, last successor B_n.

Thus the undirected first/last union has exactly two components, {A,L} and
{B,H}, each with an essential first cycle and an essential last cycle. These
are data of the abstract C walk, not actual ant clocks. Inserting any R-only
stays at a C face preserves this first/last occurrence ordering and the graph
voltages. It changes the actual ant period, which is NOT17.

## 3. All possible ant-word expansions of this fixed C geometry

Fix the initial actual head at(1,0), incoming E, active C face A0. This is also
the cursor supplied by the previous translated terminal L step. R stays at
the same active C face and advances one corner clockwise; L changes the C
face by the specified diagonal edge. The minimal R counts before successive
L moves are exactly

    0,2,2,2,1,2,0,0,0,1,0,0,1,0,0,0,2.

An actual ant can never read five consecutive R: four R return to the initial
head pose, whose just-flipped cell is then BLACK. Therefore each positive
entry1/2 in this list is forced. Each zero can be either0 or4, corresponding
to no clockwise lap or one complete RRRR lap. No larger or other exponent is
possible without changing the prescribed C walk.

There are nine such zero positions, indexed by C-step blocks
0,6,7,8,10,11,13,14,15. Their512 choices exhaust this ONE geometry. Every
expansion has the same head-pose translation(1,1) and restored incoming E;
its ant period would be30+4b for b chosen laps. This is not a period scan or
an assumed visit cap. Other C walks and additional C excursions are not in
the family.

The general no-immediate-C-backtrack fact also follows from the cursor: just
after entry, the entry edge is WHITE. Exiting immediately back would require
three R then L at that WHITE edge, impossible. Our chosen ladder already
passes this elementary constraint, so its failure occurs later in actual
color ownership, not at a concealed backtrack.

## 4. Transparent six-leaf exclusion on arbitrary initial boards

Let the nine bits, in the above order, choose zero/four R. The following six
prefixes partition all512 choices; omitted suffix bits remain arbitrary.
Every witness is two consecutive reads of the SAME physical cell with the
SAME turn. Since each actual read flips the bit, this is impossible regardless
of the initial board, including infinite prepared backgrounds.

    prefix0000 : L11 andL19 at(0,0).
    prefix0001 : R13 andR17 at(-1,1).
    prefix0010 : L11 andL23 at(0,0).
    prefix0011 : R13 andR21 at(-1,1).
    prefix01   : R1 andR17 at(1,1).
    prefix1    : R2 andR14 at(0,-1).

The prefix partition covers4*32+128+256=512 cases. Each stored witness includes
every intervening geometric read, so an unrecorded repair cannot be inserted
without changing the prescribed C walk. The checker also gives the complete
minimal finite BLACK field realizing every prefix up to (but not including)
its failing read, and the whole field at failure. Extra unread initial bits
cannot alter the already fixed color at the witness cell.

Consequently this specific nonbacktracking ladder C pattern cannot be an actual
ant factor at all. It is not merely excluded as an eventual translator, and
WHITE versus prepared input does not rescue it.

## 5. Exact conclusion

Planarity, nearest-neighbor C geometry, nonbacktracking and extremal-clock
voltage information alone permit disconnected first/last unions. The actual
ant color rule rejects this explicit construction by short source-ownership
contradictions. Neither fact settles whether every ACTUAL ant front's union
is connected. A proof of that statement must use the missing color chronology,
not the already falsified geometric inference.

No alternative controller, general disconnected-union exclusion, finite macro
alphabet, canonical104 forcing or universal finite-seed entry is claimed.

Artifacts: certify_disconnected_C_ladder_attempt.py and
 disconnected_C_ladder_attempt_certificate.json. The six prefix traces, full
finite fields, exact C forest and all512 geometry/coverage checks are retained.
