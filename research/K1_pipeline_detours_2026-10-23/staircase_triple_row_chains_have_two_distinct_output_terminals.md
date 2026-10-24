# Staircase G3 row chains have distinct singleton and opposite-R output terminals

24 October 2026. Complete WHITE cap-four front, actual full P,d and
positive output. Any C level and either winding sign. This is restricted
to DIAGONAL STAIRCASE physical G3 circles, not arbitrary cycles.
Pending independent review. Extends signed9190569a directly in original
WHITE histories; no global reverse-WHITE premise is used.

Normalize A_k=(k,k), B_k=(k+1,k), physical orientation NE, with both
A modes NNNS/NSNN and both B modes EEWE/WEEE retained. The C level is c.

THEOREM: each maximal connected staircase row-chain is finite and has
TWO different terminal output types:

- outward/SE: an actual singleton-R class;
- inward/NW: an opposite-R three-read odd class.

Both terminal classes recover the same row-chain uniquely. Different
maximal chains have disjoint terminal classes, but several starting
circles on ONE chain share them. No per-renewal or initial-fuel count
is inferred.

## 1. Retained outward end

Signed9190569a proves that U_k=(k+1,k-1) is S/NNNS/NSNN. A singleton S
terminates the prescribed outward row continuation. Otherwise the
complete U/V ports force an entire parallel staircase G3(c+2) row,
translated by(1,-1), with BOTH A/B sign choices still allowed. Finite
global C maximum gives an outward singleton after finitely many rows.
Its position and its single R heading recover the immediate inner row.

## 2. Original-WHITE inward end, including every odd possibility

Put W_k=(k,k+1), the missing corner of the RLR unit face between
A_k,B_k,A_(k+1). Every A mode has exactly one outgoing W and one incoming
S. Thus W has exactly one incoming W and exactly one outgoing S.
The complete WHITE cap-four possibilities are precisely

    EEW, WEE, EEWE, WEEE.

All have both C faces at c-2 and their shared SE L face at c-3. In the
three-read cases the opposite NW L face is c-4; in the four-read cases
it is c-5. The first two histories are genuine opposite-R odd outputs,
not prepared BLACK helpers.

If some W is three-read, the inward straight-row continuation stops
at that actual odd class. Otherwise ALL W are four-read B modes with
incoming E3/outgoing N3. The next cell X_k=(k,k+2) is forced by incoming
N3 and outgoing E3 to be NNNS or NSNN. Consequently X/W form an entire
parallel staircase G3(c-2) row, translated by(-1,1), with both signs
retained. There is no hidden source/sink or mode selection.

Each inward extension lowers the row's low L height by2. The global
minimum L height is finite, so an opposite-R three-read terminal occurs
after finitely many inward steps. This is finite height termination,
not a forbidden spatial-only or first/last ancestry regress.

## 3. The SAME finite path graph is followed from both ends

An inward four-read continuation is a previous row whose outward U
cells are the known four-read A cells of the current row. Thus it is
EXACTLY the predecessor in the row graph of9190569a, not a new unrelated
lower-level component. Every row has at most one geometric predecessor
and at most one successor. Height changes by2; the transverse coordinate
x-y changes by2 while diagonal full d preserves x-y. No row can fold
back by the actual quotient or form a cycle.

This yields one finite path component with a lowest and highest row.
Other bent G3 components or alternate currents outside this prescribed
row family are not claimed to terminate there.

## 4. Actual output ownership and the top/non-top distinction

An inward terminal at physical w has history EEW or WEE; in both, its
L1 incoming heading is E. This heading fixes the quarter-rotated frame.
Its position recovers the immediate outer row, whose B positions are
w+(1,-1)+(j,j), j integer. Its equal C heights recover that row's level
as terminal_C+2. Full drift equivariance preserves this recovery.

Therefore two distinct maximal row chains cannot use the same inward
odd class, just as signed9190569a proves for the outward singleton.
The two terminal types are disjoint by full history length and R-heading
type. If n_chain counts maximal row-chain components, safely

    N_singleton_R >= n_chain,
    N_opposite_R_three_read >= n_chain,
    N_odd >= 2*n_chain.

These are output capacities only and are not added to overlapping old
reservations. They do not count one payment for each intermediate row.

If a chain reaches global C level M, its outward terminal is immediately
adjacent to that M row and is TOP. Its inward terminal has BOTH incident
C heights at most M-2, so is necessarily NON-TOP. Thus for the number
n_top_stair of distinct staircase G3(M) circles,

    N_top_singleton_R >= n_top_stair,
    N_odd-N_top >= n_top_stair.

There is at most one M row on each chain because levels increase by2.
This locates two different actual defect types; it does not manufacture
new minima, prove root ownership of every supplier, exclude a general
WHITE front, or assert that a surviving mixed row has a realized exterior.

Companion staircase_triple_two_terminal_inventory.py/json reconstructs
all direct original-WHITE inward histories and their exact face levels.
No front, period, drift, width, radius or seed scan is performed.
