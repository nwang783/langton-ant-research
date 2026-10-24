# No board-only defect-renewal rank, even nonlinear

23 October2026. An exact first-principles obstruction to a specified rank
projection, not an actual infinite ant cycle and not universal noncapture.

Let S=RLLR, n>=3, and write

    B_R={(1,y):0<=y<2n}, B_L={(0,y):0<=y<2n}.

## 1. Two genuine finite-board physical factors

Start X_R=(B_R,(0,0),N). Exactly S^n is legal, ends at(0,2n),N, and maps the
ENTIRE finite black board to B_L. Each period consumes(1,2j),(1,2j+1) and
writes(0,2j),(0,2j+1), with no other reads or initial blacks.

Start instead X_L=(B_L,(1,2n-1),S). The proper180-degree rotation of the same
word, still S^n with unchanged R/L letters, is legal, ends at(1,-1),S, and
maps the ENTIRE finite board back to B_R. This time each pair of black tokens
moves one unit east. No background is dropped, complemented or relocated.

These are different initial POSES, so they do NOT concatenate into one
physical ant cycle. The construction never claims head teleportation is legal.
It is instead a projection obstruction for ranks that ignore those poses.

All four cyclic ten-factors of S-infinity are bad standard104 ten-factors.
Therefore every eleven-window wholly within either supplied factor ends at K.
In particular each factor contains at least4n-10 events, and its LAST read is
a K event. True inverse-history choices can add earlier events but cannot
remove these internal events.

## 2. Consequence for the EXACT renewal map

Let R_K be the total physical map to the complete state immediately after the
first future K, preserving/reconstructing true inverse history. Suppose a
natural-valued rank rho obeys strict descent on every nonterminal R_K edge.

Because the last read of S^n is K, repeated R_K applications starting at X_R
reach EXACTLY its supplied final state; none of the events or seams is skipped.
Thus if rho depends only on the black board, rho(B_L)<rho(B_R). Applying the
same reasoning to X_L gives rho(B_R)<rho(B_L), contradiction.

Both starting poses have the SAME conserved sector: their position sums are
0 and2n, and both headings are vertical. Hence this contradiction also rules
out functions of(board, conserved sector).

Thus NO function of the black board ALONE, even augmented by that conserved
sector, can be a universal strictly descending K-renewal rank. This rules out arbitrary nonlinear board-only
functions, not merely weighted sums or linear black mass.

There is an even shorter obstruction for translation-invariant board-shape
potentials: B_L=B_R-(1,0), so the first factor alone leaves ANY such value
unchanged while containing positive K. Diameter, convex hull shape, black
moments centered at the board's own centroid, and every translation-invariant
encoding of its complete shape have this defect as current ranks.

## 3. Exact scope

A rank using head POSITION, an anchor genuinely carried as additional state,
or richer history metadata is not excluded. A globally common fixed anchor
is only a parameter of a board-only function and does not evade the argument.
Conserved sector alone does not repair this projection; heading plus sector
also fails by the stronger argument below. The original
finite state includes precisely this pose information, so a computable
full-state rank remains logically equivalent to universal capture by the
retained renewal theorem.

Nor does this disprove a numerical bound stated in terms of INITIAL geometric
shape plus head distance: a bound need not be a monotonically descending
board-only current potential. The obstruction concerns a proposed rank
projection, not all possible spatial bounds.

The two finite transformations are controlled in
`check_board_only_renewal_rank_obstruction.py/json`. Their all-n proof is the
four literal S coordinates and the proper rotation above, not finite sampling.


## 4. Heading AND sector still do not rescue a position-forgetting rank

Let T=LRRL, the two-letter cyclic shift of S. A literal T period at(0,0),N
consumes(0,0),(0,1) and writes(-1,0),(-1,1), ending at(0,2),N. Thus T^n
moves a vertical black row one unit west, just as S^n does, but with its
incoming cursor ON the row instead of one unit west of it. It too ends at K.

Write B_x={x}x[0,2n-1]. Fix x0 and sigma=(x0-1) mod2. For every k>=0:

* S^n from(B_(x0-2k),(x0-2k-1,0),N) maps the board to B_(x0-2k-1).
* T^n from(B_(x0-2k-1),(x0-2k-1,0),N) maps it to B_(x0-2k-2).

Both factors preserve heading N AND conserved sector sigma. Since the last
read of each is K, strict R_K descent would imply

    rho(B_x0,N,sigma) > rho(B_(x0-1),N,sigma)
      > rho(B_(x0-2),N,sigma) > ... .

This infinite descent is impossible in the natural numbers. Therefore even an
arbitrary nonlinear function of(complete board, heading, conserved sector)
cannot be a universal K-renewal rank when cursor POSITION is forgotten.

The displayed infinite path exists ONLY in the pose-forgetting projection.
After each actual factor the cursor has y=2n; the next supplied factor starts
at y=0. Nothing here permits that reset physically. A valid projected rank
would nevertheless have to obey every one of the individual genuine finite
transition inequalities, which is why the projection itself is impossible.
