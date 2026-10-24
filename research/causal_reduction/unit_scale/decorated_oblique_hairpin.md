# A genuine all-depth decorated out-and-back transport

23 October 2026, 05:47 UTC. Exact local construction with independently signed
complete-history proof and separate all-r Presburger chronology verification. This is NOT a finite-seed countermodel,
not a growing prolongable root, and not a renewable complete-field device.

## The family

Use incoming north, R on white and L on black. Put

    U = LRLLLLRRRRLRRL,       V = RLRRLL,       q=(-1,3).

For every integer r>=1, the literal word

    W_r = U^r R V^r

is internally ant-legal. It starts at(0,0,N), ends at(1,0,E), and has length
20r+1. U preserves incoming N and drifts by q; V preserves incoming E and
drifts by -q. The central R is read at r q and moves east.

Thus a decorated recursive state b of physical type N-R can have the image
U b V, with all other read labels identities. Its iterated images are these
W_r (depth zero is b). The unique recursive LABEL is at nonzero offset q,
although other copies of its physical state occur in U. This genuinely escapes
the just-signed undecorated unique-parent-origin lemma.

The initial21-step word is the independently signed local control R21 from
`checker_axis_transport_structure.md`; the recursive occurrence is its read14.
No new longer primitive was searched. Among all nine nonzero-offset same-parent
decorations of the three signed21/29 words, eight fail already at depth2 and
this one survives. The frozen narrow inventory is
`probe_decorated_transport_cycles.py/json`.

## Complete all-r read histories

For each tile index i=0,...,r-1, translate the following twelve cells by i q.
Their COMPLETE chronological read strings in W_r are:

    cell       3x+y    history
    (-2,0)       -6    L
    (-2,1)       -5    LR
    (-2,2)       -4    R
    (-1,0)       -3    RLR
    (-1,1)       -2    LRL
    (-1,2)       -1    L
    ( 0,0)        0    LRL
    ( 0,1)        1    RL
    ( 0,2)        2    L
    ( 0,3)        3    R
    ( 1,1)        4    R
    ( 1,2)        5    R

The remaining read cell is r q, whose sole read is the central R.

Proof of completeness: trace the14 reads of U and the6 reads of V. U supplies
all table events of classes -6 through1, except the final L in classes0 and1.
For V copy k=0,...,r-1, put i=r-k-1. Its six reads supply exactly the missing
L events in those two classes and the single reads in classes2 through5,
translated by i q. All U copies precede the central R and all V copies, so
the displayed history order is exact. The twelve values3x+y are distinct and
translation by q preserves them. Two different tiles of one class differ by
nonzero q, so none overlap. The only same-class endpoint is r q, outside the
index range of the class0 table cells. Thus no read is omitted or duplicated.
Every displayed string alternates, proving legality for ALL r, without any
finite-depth extrapolation or assumed infinite initial periodic board.

## Exact input, output, and fuel requirement

Let

    I={(-2,0),(-2,1),(-1,1),(-1,2),(0,0),(0,2)},
    O={(-2,1),(-2,2),(-1,0),(0,3),(1,1),(1,2)}.

The unique minimum input black set is

    I_r = union_(0<=i<r) (I+i q).

Starting with precisely I_r and every other cell white gives the word W_r and
complete final black set

    O_r = union_(0<=i<r) (O+i q) union {r q}.

Both six-cell tile families are disjoint. Therefore the exact input and output
masses are6r and6r+1, the visited support has12r+1 cells, and the complete XOR
has10r+1 cells. These statements follow directly from the first and final
letters of the complete table, not from sampled mass counts.

In particular this family CANNOT be supplied from a uniformly bounded number
of black cells. Every one of its6r first-L positions is a forced input, even
if arbitrary extra untouched cells are allowed. The recursive label is interior,
so its power images are not nested prefixes of an infinite root word either.
A separate wrapper, preparation of growing input rails, all output changes,
and an autonomous return/renewal mechanism would still be required.

## What the construction contributes

This is an actual opposite-drift bulk pair with a one-read far cap, not exact
time reversal and not the same-direction A12/B28 control. It shows that the
new drifting-hidden-state residual is nonempty at the all-r LOCAL legality
level. It also illustrates its main obstacle: substantial prepared rail fuel
and distributed lasting changes, not merely a missing short cap.

The oblique direction and10r+1 complete XOR are essential when applying clocks;
one must not pretend that only the single far endpoint changed. No finite-fuel
or full-recursive realization is claimed.

## A literal three-step return to the original pose

The three cells (1,0),(1,-1),(0,-1) lie outside the read support and both
prepared tile fields for every r>=1. They are initially white. Appending RRR
to W_r therefore returns the head from(1,0,E) to(0,0,N). Thus

    G_r=U^r R V^r RRR

is an actual closed-pose excursion of length20r+4, with input I_r and output

    O_r union {(1,0),(1,-1),(0,-1)}.

Its mass rises from6r to6r+4, and its complete XOR has10r+4 cells.
This closure also passes independent analytic review. This completion uses literal legal updates, NOT
an external reset. The distributed tile transformation and growing prepared
fuel remain; it is not a renewable cycle. A fixed core could only be proposed
after its complete input/output compatibility is separately checked.

The extra three cells are easy to distinguish from the table: their invariant
classes3x+y are3,2,-1, respectively, and each is the corresponding table
representative shifted by -q, outside the allowed i>=0 tile range.

Independent original-family artifacts:
`audits/check_oblique_hairpin_independent.py/json` and
`computability/finite_power_exact_validator/hairpin_presburger.json`.
