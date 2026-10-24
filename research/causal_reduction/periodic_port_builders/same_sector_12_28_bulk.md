# A same-direction, same-sector periodic bulk inverse pair

Status: stable drift-class identities independently checked on22 October2026.
No renewable cap, autonomous finite-seed orbit, or counterexample is claimed.

Use north/east/south/west headings0/1/2/3, right on white and left on black.
The invariant pose sector is x+y+h modulo2. Let I have a solid row0 and odd-x
black cells in rows1,2; let M have a solid row3 and the same alternating rows.
All other read cells are white. These denote stable periodic bulk profiles,
not a promise about an unprepared epoch-zero interface.

    A = LRLLRRRRLLRL, from(0,0,E), drift(2,0), sector1.
    B = RRRLLLLRLLLLRLLLLRRRRLRRRRLR, from(0,2,E), drift(2,0), sector1.

A converts I to M. B converts M to I. Both restore rows1 and2. A's complete
per-cell histories in those rows are RL at even x and LR at odd x. B's are
RLRLRL at even x and LRLRLR at odd x. On the removed solid row the history
is L; on the added solid row it is R. Thus every class alternates with the
stated initial/final bit. No time reversal or sector change is involved.

The exact finite drift-class computation is check_12_28_pair.py. Independent
no-import complex-coordinate replay is audits/check_12_28_bulk_independent.json.

## A finite controlled composition

For every n>=1, prepare:

- cells(-2,1),(-2,2),(-1,2),(-1,3);
- the I bulk on columns0,...,2n-1;
- no other black cells.

A^n runs from(0,0,E) to(2n,0,E). If the head is EXTERNALLY reset to(0,2,E),
B^n then runs to(2n,2,E). This is a controlled read-history identity, NOT an
uninterrupted ant orbit. The bulk is restored except in the last two columns.
The total initial/final black mass is4n+4. The complete XOR is four cells at
the left interface and their translate by(2n,0):

    {(-2,1),(-2,2),(-1,1),(-1,3)} + { (0,0), (2n,0) }.

Here the plus denotes the union of the two translates, not a claim that their
colors agree. A direct two-column local verification proves the all-n statement:
A maps tile masks(1,7) to(8,14); B uses a two-tile window and maps

    left(6,12), right(8,14) -> left(0,6), right(7,13),
    left(7,13), right(8,14) -> left(1,7), right(7,13).

The first line starts the B sweep; the second propagates its finite interface.
Finite controls through n50 are saved, while the two local identities provide
the induction. The external reset is a missing hardware operation, not a
legal ant step. An autonomous completion must also respect the independently
audited compact-export obstruction and all complete-field endpoint obligations.
