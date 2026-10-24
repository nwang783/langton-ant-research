# Mixed W20/S shuttle: exact conditional axial-front construction

Status: conditional construction target and elementary interface derivation;
independent analytic audit passed 22 October 2026 for gluing and the wake budget. NO cap pair or counterexample is known. This is not a claim
that finite-seed attraction is false.

## Bulk geometry

Use headings N,E,S,W = 0,1,2,3 and R on white. Set

    W = LLRLRRRRLRRRRLLLLRLL,
    S = RLLR.

From heading E, W drifts (-2,0) and S drifts (2,0). The complete infinite
westgoing W front moves a solid input row y=0 to y=3: the two x parities have
read strings L in row0, RLRL in rows1/2, and R in row3. The eastgoing S front
moves its solid input row one unit north. Its path from (0,0,E) reads
(0,0)R,(0,-1)L,(1,-1)L,(1,0)R and ends (2,0,E).

Therefore W^n followed by S^n at height4 has a neutral, renewable middle:
W erases the input row0 and writes row3; S erases row3 and writes row4.
In the infinite time history with vertical drift4, middle classes have
white-first alternating histories RL on rows0/3 modulo4 and RLRL on rows1/2.
The first R on row0 is the preceding period's S output.

## The two finite caps and exact conditional gluing theorem

Seek finite words K and J with geometric interfaces

    K : (0,0,E) -> (0,4,E),
    J : (0,0,E) -> (0,0,E).

Define two local all-period histories, always translating the cap by (0,4):

* Left: incoming W periods at starts (2k,0,E), k>=1, in chronological order
  k decreasing; K; outgoing S periods at starts (2k,4,E), k>=0, k increasing.
* Right: incoming S periods at starts (-2k,0,E), k>=1, k decreasing; J;
  outgoing W periods at starts (-2k,0,E), k>=0, k increasing.

The right local cut places J between the just-completed S sweep and the next
period's W sweep. It is a cyclic cut of the same proposed full front.

Group physical read events modulo (0,4), i.e. by (x,y mod4). Within a class,
order by decreasing local y, then by within-period chronological phase. Require
every nonempty complete class to start R and alternate. This is an exact finite
check: beyond the finitely many cap columns plus the arm endpoint offsets,
the arms have the automatic middle histories above.

IF both caps pass these local conditions, THEN for every sufficiently large n

    P_n = W^n K S^n J

is a finite-seed translating front of drift (0,4), starting with heading E.
Its period length is 24n+|K|+|J|. To prove this, choose n so that the finite
left and right exceptional column ranges are disjoint after placing the left
cap at x=-2n and right cap at x=0. Quotienting by vertical drift preserves
x, so every full-front read class belongs to exactly one local cap range or
to the automatic middle. The local arm histories agree with the finite arms
inside their own exceptional ranges. Thus every full-front class starts R
and alternates. The standard inverse periodic-front construction then supplies
a finite initial board: in each class seed exactly the finite interval whose
initial phase parity requires black. There are finitely many classes and
finitely many seed sites in each.

The converse holds for all sufficiently separated fronts in this precise
architecture: their local classes must satisfy the two conditions. The
result would be nonstandard because its nonzero drift is axial, whereas a
standard104 front's drift is diagonal under every quarter-turn.

There is no assertion that a suitable K or J exists. No finite successful
prefix would replace these all-period conditions.

## All-length cap wake budgets

Let delta(A)=#R-#L in cap A. In a valid complete class, white-first alternating
reads have excess0 or1, and excess1 is exactly a permanently black wake class.
The fixed arms have total excess +2 at the left and -2 at the right. Thus

    g_left  = delta(K)+2,
    g_right = delta(J)-2.

Both caps restore their heading, so each delta is0 modulo4, and each g is2
modulo4. More information comes from the exact alternating-row charge:
for arbitrary a(y), f(x,y)=(-1)^x a(y), its signed turn sum along a finite
path equals minus the endpoint pose correction modulo4. The complete
formula and elementary step check are in `../alternating_row_charges_mod4.md`.
Choose a periodic a selecting a row residue modulo4. For J the pose correction
is zero. For K it changes by2 in each residue. The arms' signed excesses,
ordered by row residues0,1,2,3, are

    left arms:  ( 2, 1,-1,0),
    right arms: (-2,-1, 1,0).

Therefore the alternating x-charge of the final black wake is, modulo4,

    left wake:  (0,3,1,2),
    right wake: (2,3,1,0).

A charge2 needs at least two black cells; a charge1 or3 needs at least one.
Hence each wake has at least4 cells. Since g is2 modulo4, in fact

    g_left>=6, delta(K)>=4,
    g_right>=6, delta(J)>=8.

Thus any cap pair would have at least12 black wake classes per period. Clean
or minimal two-cell wakes are impossible at every cap length. Debris-emitting
renewal is not excluded. These charge budgets do not assume bounded cap length
or any finite search outcome.

## Initial controls

`mixed_shuttle_caps.py` directly constructs all complete histories. All167
physically feasible K words through16 and all124 physically feasible J words
through16 fail. The simplest left near-miss is LLRLRRLR, whose only bad class
is(-1,3):L. A right near-miss is RRRRLRRRRLRRRRLL, whose only bad class
is(-1,0):RRL. These are precise failed candidates, not partial counterexamples.
The script and numerical exclusions have not yet been independently audited.
