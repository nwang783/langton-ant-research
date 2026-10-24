# A root-free shallow valley forces an unmatched positive G3 sink circle

24 October 2026. Complete original WHITE cap-four K1 front, actual full
P,d and required positive odd output. Assume a locally minimal original
L plateau Q at m=M-3 has no odd incident corner. This is a conditional
local structure, not a zero-output whole-front family or realization.
Pending independent review.

Use the signed root-free reverse axis rail2ca8c002. In its genuine
physical coordinates the reverse drift is (0,2a), a>=1, and

    Z_k=(0,2k) WWWE, Y_k=(0,2k+1) NNNS,
    A_k=(1,2k) NNSN, B_k=(1,2k+1) EEWE.

## 1. Exact original histories and physical G3 cycle

Apply the signed read-event reversal, not naive incoming-head reversal.
The ORIGINAL histories at these same physical cells are

    Z_k SSNS, A_k EEEW, B_k SSSN, Y_k WWEW.

Their triple-use ports give the complete directed path

    Z_k -> A_k -> B_(k-1) -> Y_(k-1) -> Z_(k-1),
        E       S           W           S.

Every port has right C height M and left L height M-3 in the SAME
plateau Q. All four vertices have exactly one G3 input and one G3
output, so this path cannot escape into another G3 branch. Repetition
therefore gives a specific G3(M) cycle. In the actual full quotient its
4a cells are distinct (x=0/1 and parity distinguish the four roles), and
its physical displacement is original d=(0,-2a). Its winding is +1.
No primitive reduction from a to1 is used.

The canonical middle-ordinal node of this cycle is sheet M-1. Its
physical corner word is LEFT, RIGHT, RIGHT, LEFT repeated, or cyclically
LLRR. This is NOT the max-C face-birth word, so the signed no-LL birth
law does not prohibit it.

## 2. Full physical ordinal table, retaining R0 and L3

At each edge, the lists name complete chronological ranks at its source
and target:

    Z_k -> A_k:       (1,2,3) -> (0,1,2)
    A_k -> B_(k-1):   (0,2,3) -> (0,1,2)
    B_k -> Y_k:       (0,2,3) -> (0,1,3)
    Y_k -> Z_k:       (1,2,3) -> (0,1,3).

In EVERY row the middle occurrence is source R2 -> target L1.
Consequently the repaired circle is everywhere incoming L1 -> outgoing
R2, with no negative/outgoing-L1 incidence. It is a SINK of the signed
exchange-clock network: every incident exchange points from the other
node's outgoing L1 into this node's outgoing R2.

Every one of these exchanges is UNMATCHED in the stronger79dcbbd4
sense. A source-side L1/R2 pair is shifted to ranks0/1, or the target
pair is fed by source ranks2/3; other edges lack one of ranks1/2.
Thus the entire essential circle survives removal of all exactly
matched physical-port exchange pairs. This is an explicit remaining
rank-shift mechanism, not evidence that the connected-core argument
has excluded essential assembly.

## 3. Actual forward wait intervals partition one full period

For each successive physical edge v->w on this circle,

    T1(w)=T2(v)+1.

Following the full winding-one cycle and summing gives exactly

    P=4a+sum_(4a cells v) [T2(v)-T1(v)].

All actual L1-to-R2 waits are positive multiples of four. They and the
single connecting physical edges occur successively and partition ONE
actual P interval. Therefore every individual wait is <P; that bound is
a consequence, not an assumption. The dependent P>=20a=10||d||_infinity
is a clock lower bound only, not added to overlapping current budgets.

This exact continuous-cursor partition retains the R0 and L3 reads in
the displayed ordinal table: those reads occur inside other waits or
on their connecting edges. They are not discarded as unused suppliers.
No original-fuel ownership or fresh-root claim follows.

## 4. Why the necessary sink pattern is not a positive front

The retained prepared W20 control already has an all-positive middle
node of this abstract type, with four-edge upper/lower leaves and
zero graph excess. One lower leaf is old WHITE L3 stock; the other uses
two explicit BLACK singleton-L fuel reads. That finite prepared control
is NOT a complete original WHITE front. Neither this table nor the
partition identity repairs its input supply.

The signed one-sided odd-or-deeper alternative dd171052 still applies
to Q's reverse rail: actual original odd output must lie to its LEFT,
or a deeper local minimum exists there. Different rails may share those
defects or minima. The present statement identifies one particular
positive G3 cycle forced by Q; it does not classify every G3 cycle in
the same L plateau, forbid negative components elsewhere, or exclude a
complete K1 front.

Companion rootfree_axis_rail_original_triple_cycle.py/json independently
reverses the four prescribed histories and computes all port ordinals.
It is one fixed interface, not a front, period or supplied-drift scan.
