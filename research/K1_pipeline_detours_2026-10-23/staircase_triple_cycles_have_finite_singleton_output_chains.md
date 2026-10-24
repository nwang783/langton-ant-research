# Every diagonal-staircase G3 circle has a finite outward singleton-R chain

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d, positive output retained. All C levels and both winding signs are
allowed. This theorem is conditional on DIAGONAL STAIRCASE geometry,
not arbitrary G3 circles. Pending independent review.

Normalize one staircase circle to the NE physical route

    A_k=(k,k) -> B_k=(k+1,k) -> A_(k+1).

Its full winding w is+1 or-1; for ell=2a cells the actual full drift is
d=w*(a,a). Retain BOTH complete modes at every corner, independently:

    A_k: NNNS or NSNN;
    B_k: EEWE or WEEE.

The chosen G3 C level is c, and low L level c-3. The signs need not be
constant, periodic on a smaller quotient, or inherited by a later row.

THEOREM: this circle belongs to a finite, explicitly typed outward chain
of parallel staircase G3 circles. A chain terminates at an actual WHITE
singleton-R output cell, not BLACK input fuel or an unproved root.
Different starting rows on the SAME chain are not different payments.
In particular a staircase G3(M) circle has such an adjacent singleton
immediately; it cannot shield outward through a higher row.

## 1. A row extends exactly unless it already has singleton output

Let U_k=(k+1,k-1), V_k=(k+2,k-1). Every allowed B profile has exactly ONE
outgoing S use and exactly ONE incoming W use. Therefore U_k has exactly
one incoming S and one outgoing W. The complete WHITE cap-four list is

    U_k=S, NNNS or NSNN.

The singleton S is an actual R read, hence odd output. The other modes
are four-read complete RLRL histories. The shared NW C face at U has
height c, and its exact face levels are

    U=S:    opposite C=c-1, both L=c-1;
    U=NNNS or NSNN: opposite C=c+2, both L=c-1.

If ANY U is singleton, this row is a terminal row. Otherwise EVERY U
has the A interface: incoming N and outgoing E both have flow THREE.
Consequently V_k has incoming E3 from U_k and outgoing N3 into U_(k+1).
The complete WHITE possibilities are precisely

    V_k=EEWE or WEEE.

Thus U/V are a new, entire G3(c+2) staircase circle with the SAME physical
orientation and full winding. It cannot split into paths, enter a
source/sink, or change the port type: every new vertex has one triple
input and one triple output. Both signs remain allowed at every new
A and B; no homogeneous or canonical-parent condition is propagated.

## 2. Full invariant carried under iteration

At outward depth n the coordinates and level are

    A^n_k=(k+n,k-n), B^n_k=(k+n+1,k-n), c_n=c+2n.

If no singleton occurs at that row's U ports, section1 forces EXACTLY
this interface at depth n+1. This is the entire induction hypothesis:
complete four-read modes, both triple ports, level c_n and the same
actual full d. It uses no guessed ancestry, birth rank or component
membership. The next row may have completely different sign choices.

The actual full quotient cannot recycle an outward row: x-y increases
by2 each time, while actual diagonal d preserves x-y. Within each row,
only k shift by a gives the full translation w*d. Roles A/B are separated
by checker parity and normal coordinate.

The global C maximum M is finite. If all U remained four-read at depth
n, the next level c+2(n+1) would have to be <=M. Hence a singleton occurs
after at most floor((M-c)/2)+1 outward checks. This is a finite height-
bounded terminal argument with explicit preserved modes and quotient
closure, not a contradiction from spatial decrease alone.

## 3. Exact chain-component ownership, with no per-renewal charge

A nonterminal row has a unique next row, translated by(1,-1) and raised
by2. A next row has at most one possible geometric predecessor, the
inverse translation and level shift. Therefore the finite row graph
is a disjoint union of paths, not a branching ancestry forest.

A terminal singleton S at physical position u recovers its immediate
inner row: A positions are u-(1,-1)+(j,j), j integer, with the fixed NE
B offsets. Its NW C height gives that row's level. Its unique R heading
also fixes the quarter-rotated frame; other frames require other
singleton headings. This recovery commutes with actual full drift.
Consequently different maximal outward-chain components cannot use
the same singleton-R full-quotient class. One may choose one terminal
class per component, giving an injection into actual singleton-R output.

This does NOT inject every starting G3 circle, repeated renewal, gate,
or all arbitrary G3 components into separate output classes. Several
rows on one chain share its terminal defect. The reservation may also
overlap older singleton-output payments and is not added to them.
There is no initial-fuel bound or complete-front exclusion.

## 4. Relation to the homogeneous-negative exclusion

For the homogeneous negative inner row, the actual local clocks retain
ONLY U=NNNS at every k, not the other two alternatives. The higher row
then forces the literal third-strand factor L3->L3->R2 that contradicts
the negative full drift, as signed a31d409e proves. The present result
keeps all genuine mixed modes and provides their finite terminal role,
without claiming that an all-positive or mixed staircase front exists.

The companion staircase_triple_outward_terminal_inventory.py/json checks
all1..4 WHITE local histories, exact side ports and all face levels.
There is no period, drift, width, radius, seed or multiplicity scan.
