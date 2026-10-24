# Exact fuel and diagonal flux for a mixed U/V run

Let W be any nonempty word over U,V with u U blocks and v V blocks, all in
the common north-facing before-marker frame. Then W is physically realizable
from a minimal finite seed of exactly

    4 + 5u + 2v

black cells. This is an exact first-L count, not a lower bound on a larger
word in which cells may have been read before this run.

The first block has nine first-L cells if U, six if V. After either possible
predecessor, each subsequent U adds precisely the five first-L cells

    (-1,0), (-1,1), (-1,2), (0,2), (0,3),

in its own frame. Each subsequent V adds precisely (-1,0) and (1,2).
Every other first-L cell was read by the immediately preceding block and
has the correct opposite last letter, as the four literal pair interfaces
UU,UV,VU,VV verify. Each block's largest read y equals its final head y.
All the displayed new cells except (-1,0) lie strictly above every earlier
block. The cell (-1,0) lies on the immediately preceding block's highest row
but is absent there; still earlier blocks lie strictly below it. Therefore
no nonadjacent overlap can add another constraint. This proves both exact
fuel and arbitrary mixed-order feasibility by induction.

There is also a useful net-flux identity. Restrict the black field to cells
with x+y=3 mod4 and count its black cells separately on each diagonal x-y=d.
A north-facing U changes none of these diagonal counts. A north-facing V
reduces the count on d=p_x-p_y-1 by exactly one and changes no other such count.
Here p is that block's entry head; all entry sums are 0 mod4 in this frame.

The exact changed cells of the selected residue class are:

- U removes black at (-1,0),(0,-1), and adds black at (1,2),(2,1).
  These are two transports by (2,2), each preserving x-y.
- V removes black at (-1,0),(0,-1), and adds black at (2,1).
  The second source transports by (2,2); the first is consumed.

This net identity holds on every coloring on which the block is feasible.
A half-turn exchanges residue classes 1 and3 and reverses the transports.
It does not supply a full-five finite-fuel invariant: opposite-heading U
blocks create tokens in the other class, and folds change the direction.
The locations and ordering of such newly created fuel remain essential.
