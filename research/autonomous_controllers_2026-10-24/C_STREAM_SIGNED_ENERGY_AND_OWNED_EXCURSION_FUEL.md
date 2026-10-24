# C-stream signed energy and actual owned excursion fuel

24 October 2026. Author exact identity and controls; independent audit pending.
This is a signed conservation/transfer law, not a Lyapunov function, a finite
macro alphabet, a no-input detector, or a replacement winding budget.

## Extremal-height scope check

The signed C-entry scaffold does not supply a discovery cycle at the global
C maximum. In actual standard104, the complete active-C heights, after one
common normalization, range0..4. Its two discovery cycles have constant heights
3 and2, whereas active face(1,-2) has height4. Thus neither discovery cycle
attains even the active-C maximum. Choosing the higher discovery cycle does
not make every other active C face lower. This is NOT a statement that the
height4 face is on a particular geometric exterior side.

The all-cap local bridge is

    h(C_parent)-h(C_child) = R_same-R_opposite

for a WHITE SAME-heading R0/L1 discovery. Cycle telescoping only forces the
SUM of these imbalances to be zero. Standard tree edges with histories WWEEEE
and WWEWWEEWEE already have imbalance−1. Neither local first-R maximality nor
a finite exterior-return alphabet follows. The actual standard10/94/14/90
excursions and their high multiplicities remain valid.

## The exact quadratic identity

Fix an actual stable heading-restored translating word with FULL nonzero
period/drift(P,d). It may be complete WHITE or prepared BLACK-first. At each
full physical read class p choose one of its two arrival headings as '+', the
opposite as '−'. For definiteness use N for a vertical-arrival class and E for
a horizontal-arrival class. Write epsilon=±1 for a read's heading and

    a_p = sum over R reads at p of epsilon_R.

The unrestricted directed-port equations and the periodic face stream give

    h(C_plus)-h(C_minus)=a_p.

This is the cap-free local stream tuple, not its cap-three/cap-four exclusion.
At an L read, the active C face crosses from the epsilon_L end to the other,
so its height change is −a_p epsilon_L. R leaves active C unchanged. The full
period translates the active face by d, preserving h. Therefore

    sum_L a_p epsilon_L = 0.                         (1)

Also, directly by collecting R reads classwise,

    sum_R a_p epsilon_R = sum_p a_p^2 =: E.          (2)

Retain every actual R→NEXT-L lifetime, with its true physical source and full
period offset. Let D be twice the sum a_p epsilon_R over owned lifetimes whose
consumer has the OPPOSITE incoming heading. Let O be the sum a_p epsilon_R over
permanent last-R outputs. Let I be the sum a_p epsilon_L over BLACK-first L
inputs. A class beginning L and ending R contributes separately to I and O.

A same-heading owned lifetime contributes equal birth and consumption charge;
an opposite-heading one contributes a birth-minus-consumption difference
2 a_p epsilon_R. Every R is either a lifetime source or a permanent output,
and every L is either owned or a BLACK input. Subtracting(1) from(2) proves

    E = D + O - I.                                  (3)

No cap, width bound, period bound or phase-first shortcut is used. E is
nonnegative, but D, individual source charges, O and I are SIGNED quantities.
They are not BLACK masses. In particular I=0 does not mean no BLACK inputs.

## Exact transfer on excursions and connectors

Partition the actual period into contiguous blocks, retaining cyclic cuts and
every event. For each owned L in block t, record the actual R source phase,
its source block s, and its full owner-period offset k. Define

    F_(s,t,k) = sum of a_p epsilon_R on those actual source pairs.

Keep each individual lifetime as well as this aggregate; zero or negative
weights do not erase its owner. Let B_s be the R-birth charge in block s,
O_s its permanent output charge, I_t its input charge, and D_t the opposite-
heading owned charge consumed in block t. The exact two balance equations are

    B_s = sum_(t,k) F_(s,t,k) + O_s,
    Q_t = sum_(s,k) F_(s,t,k) - D_t + I_t,             (4)

where Q_t is the sum a_p epsilon_L of the block's L reads. Geometry gives

    Q_t = h(C_start)-h(C_end).                       (5)

For EACH actual closed head-pose excursion, Q_t=0 separately. Connector
charges are their exact C-height drops and telescope around the period. This
is the requested cross-period fuel transfer: a BLACK read in a neutral
excursion is charged to its actual R source, possibly in another block of a
previous full period, not mislabeled as a fresh seed input.

There is an optional decorated-stock interpretation on finite fields. Tag a
BLACK cell by the heading of its actual most recent R, and give it charge
 a_p epsilon_owner. An explicitly unowned initial BLACK cell needs its own
stated tag convention; it must not be silently relabeled R-born. Equations(4)
are the finite change-of-stock bookkeeping, not an assertion that all colored
states have these extra historical tags. For infinite prepared fields we use
ONLY the finite event-flux sums above; no divergent global stock sum is
subtracted or treated as translation-invariant. All unread passive BLACK
strands remain unchanged, and do not become owned or consumed inputs.

## Adversarial exact controls

All five supplied complete histories, all R owners, first-L inputs, permanent
outputs, and full period offsets are reconstructed. Their(E,D,O,I) are:

    standard104:   (60,52,8,0)
    prepared1564: (782,462,320,0)
    prepared4352: (2402,1706,689,-7)
    prepared10:   (5,4,1,0)
    prepared80:   (44,26,16,-2).

Prepared10 has ONE genuine BLACK-input class despite I=0. Prepared1564 has197
BLACK-input classes despite I=0. Prepared80 retains both inputs: phase15 has
charge0, while phase21 has charge−2 and remains distinct from the later output
phase77 in its class. Hence the identity passes the signed S3 counterexamples;
it supplies no input-count or WHITE unit-winding exclusion.

The source weights also have genuinely negative terms in the WHITE standard:
R43→L51 has birth charge−1 and opposite headings. The neutral E8 excursion's
three externally supplied lifetimes have charges2,3,−1, with sources R45,
R62 from the PREVIOUS period(time−42), and R43. Its birth charge is3 and its
opposite-owner charge is4. The92-read excursion has birth charge56 and opposite
charge48. All corresponding consumption Q values are0; the connectors retain
the remaining signed terms. No positive payment per neutral excursion follows.

The prepared80 partition contains all five actual RRRLLLLR closed excursions
and ALL intervening routers. Every excursion individually has Q=0, while the
full owner matrix keeps actual recycling and the two unowned roots. The growth
12, S3, complete field and infinite input requirements of that wave are not
changed by this calculation.

## Verification and remaining gap

certify_C_stream_owned_fuel_energy.py and
C_stream_owned_fuel_energy_certificate.json reconstruct the five full graphs,
standard12/88 and8/92 partitions, prepared10, and prepared80's five excursions.
The certificate retains every source pair, every signed block-matrix entry,
all input/output roots, and80 common-rotation/full-power controls. Full powers
multiply all four charges and E by the power, with full drift residues retained.

The identity is a classification constraint conditioned on a supplied stable
word, not a computable global invariant of an arbitrary unknown orbit. It is
an exact consequence of the physical stream and actual lifetime ownership.
No claim of priority relative to all literature is made. A useful further
inequality would have to control the signed opposite-owner transfer or the
exterior connector heights without discarding negative or zero-charge roots.
No such inequality or finite alphabet is established here.
