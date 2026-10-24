# A controller-free obstruction at radix13 and rectangle3 by5

23 October 2026, 00:34 UTC. New analytic proof and tiny exhaustive control,
submitted for independent review. This does not resolve the highway conjecture.

## Statement

No finite-black-seed classical ant path satisfies

    p(13n)=diag(3,5)p(n)   for all n>=0.

The same holds with the matrix negated, and after swapping coordinate axes.
No equality of headings is assumed. No substitution, finite controller,
coarse-vertex separation, or repeated image choice is imposed.

## Fresh predecessor

Use the signed rectangular fresh-record bounds in
`../../computability/rectangular_fresh_record_bounds.md`. The vertical
multiplier is5, ell=3, the north-macro south budget is1, and the predecessor
must cross exactly one pristine intermediate row. Its first arrival from
that row to the final record row therefore has the forced word F=RRRRLR.
It ends at the aligned endpoint: an extra horizontal move is excluded by
the odd vertical-displacement macro's movement-axis parity; a further
vertical move cannot return to this height with no south move remaining.

Normalize that endpoint to(0,0,N). Immediately before F, its entry row y=-1
and every higher row were pristine white. This follows from the first-entry
property, not merely from the endpoint being a record. The F reads are

    (1,-1):R, (2,-1):R, (2,-2):R,
    (1,-2):R, (1,-1):L, (0,-1):R.

Thus after F, (1,-1) is white, and (2,-1),(2,-2),(1,-2),(0,-1)
are black. Every other cell on or above y=-1 is white. Cells below y=-1
not listed here may have ARBITRARY colors. Ignoring all earlier predecessor
history only enlarges the set of allowed continuations.

The coarse ant's next read at its north record is fresh R, so the next fine
macro must have displacement(3,0). It starts north and lasts13 moves, hence
its exact compass counts are N3,E5,S3,W2.

## Eleven-read contradiction, without exhaustive search

The first four turns are forced RRRL, ending at(0,-2,S), having spent
one west move and two south moves. Only one further west and one further
south are available. The next cell may be either color.

1. If the fifth turn is L, the reads at(1,-2) and(1,-1) force L,L,
   reaching(0,-1,W). That cell is now white, forcing R to(0,0,N).
   The origin is black from the first read, forcing L and a THIRD west
   move at the ninth move.

2. If the fifth turn is R, it spends the second west move and reaches
   (-1,-2,W). If the sixth turn is L, it spends the third south move.
   The next two turns must L,L to avoid a third west or fourth south,
   reaching(0,-2,N). That cell is black from the fifth read, forcing L
   and a THIRD west move at the ninth move.

3. If the fifth and sixth turns are R,R, the ant reaches(-1,-1,N),
   a still-white cell in the pristine entry row. It forces R to(0,-1,E),
   which is white and forces R to(0,-2,S). The latter is now black and
   forces L to(1,-2,E). That F cell is black, forcing L to(1,-1,N).
   That cell is black from the third read of the next macro, forcing L
   and a THIRD west move at the eleventh move.

These cases exhaust the only two unknown cells. All contradict W<=2 or
S<=3 inside the13-step macro. Hence the claimed inflation is impossible.

The negated-matrix case uses the coarse ant p and the rotated fine ant -p,
just as in the already reviewed signed rectangular bounds; turning signs
and the fresh-row argument are unchanged. Global180-degree rotation selects
an unbounded north sign without interchanging the two multipliers.

## Independent-style finite control, not a proof substitute

`probe_k13_fresh_local.py` directly branches unknown initial cell colors,
without reusing controller images. It rejects the first east macro in18
recursive nodes, even though the requested test allows a second south macro.
The larger coupled coarse/fine mechanism in that file is not needed here.

`check_k13_fresh_420.py` independently represents headings and positions as
complex numbers and lists all420 movement words with7 horizontal slots
(E5,W2) and6 vertical slots(N3,S3). It copies the frozen F output per word,
assigns each previously unknown lower-row cell the first required color, and
checks subsequent read consistency. Every word fails by zero-based read10.
No fine exit-heading restriction is imposed. The raw420 conflicts and source
are frozen alongside the summary JSON.

## Eventual affine extension

The same proof excludes, for any integers c and vector d in Z^2 and any
orientation-preserving quarter rotation rho, an identity

    p(13n+c)=rho diag(3,5)p(n)+d   for every n>=n0,

where the asserted indices are nonnegative. Coordinate-swapped rectangles
are excluded as well. This is still a finite-support ant theorem.

To make the reduction explicit, use the fine ant
q(t)=rho^(-1)(p(t)-d). Its initial coloring remains finite, and its aligned
endpoints satisfy q(13n+c)=diag(3,5)p(n). The two macro displacement types
still have exactly the compass counts used above; no heading equality or
time-zero phase is needed. Discard the finite early fine history before
13n0+c and choose a coarse north record high enough that the entire required
fine pristine band lies above that early history and every initial black
cell. The same predecessor/F/east-macro argument applies verbatim.

Such arbitrarily high records in one sign of the5-coordinate do exist.
For rho=0 or180 degrees, iterating n->13n+c gives an expanding affine scalar
recurrence on each spatial coordinate. Boundedness of a coordinate would
force all sufficiently late values to equal its affine fixed point, which
is incompatible with quarter-turn movement. For rho=90 or270 degrees,
(rho diag(3,5))^2=-15I, so iterating the relation twice gives the same
conclusion for both coordinates. A global half-turn selects the north sign.
This also justifies the high-record choice without assuming a preexisting
vertical drift direction.
