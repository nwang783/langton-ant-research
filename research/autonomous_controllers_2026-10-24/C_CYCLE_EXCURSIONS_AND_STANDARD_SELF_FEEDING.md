# Actual C-cycle excursion normal form and standard self-feeding

24 October 2026. Author proof and complete literal control; independent audit
pending. This is an exact decomposition of an existing controller, NOT a new
controller, a physical deletion operation, or a WHITE winding theorem.

## The all-cap normal form

Use the signed active-C scaffold ACTIVE_C_FIRST_ENTRY_LAST_EXIT_OWNERSHIP.md
1ae8a8e5, independent report317e4dce. Choose one of its WHITE-owned first-entry
cycles. Traverse it in the direction of actual discoveries, opposite to its
parent arrows. Let R_i be the first R of the selected read cell and L_i its
first L. The first-entry proof gives the SAME incoming heading and physical
position at R_i and L_i, with no intervening read of that cell.

Consequently the actual word on [R_i,L_i) is a nonempty closed head-pose
excursion. It starts R, leaves its root BLACK, returns to exactly its original
position and heading, and has positive length divisible by4. Its BLACK growth
is a multiple of4, but is NOT asserted positive. Other cells may carry stock
created earlier, including in other excursions or periods.

These excursions are genuinely EVENT-DISJOINT. The interval from the first
activation of one cycle face to the first activation of its child contains
that child's entire selected R_i/L_i excursion. Those first-activation
intervals concatenate in actual time, and the signed full-winding −1 clock
identity makes their total length exactly one period P. Thus, after a suitable
period cut, the whole actual period is

    E_1 K_1 E_2 K_2 ... E_m K_m,

where each E_i is the closed-pose word [R_i,L_i), and each nonempty K_i is the
actual connector beginning with L_i and ending immediately before R_(i+1).
Every update is retained exactly once. The K_i may contain arbitrary excursions
and multiplicities of their own; their lengths are not bounded here.

Erasing the E_i preserves the GEOMETRIC endpoint, heading and full drift of
the remaining connector word, since each erasure is a closed head-pose factor.
It does NOT preserve colors, BLACK fields, lifetime owners, or ant legality.
No physical removal, independent module, or finite-state transfer is inferred.
This is stronger than a relaxed clock decomposition: every listed interval is
an actual contiguous part of the same ant event cycle.

## Exact standard104 control

Use the retained standard word and coordinates with incoming N at phase0,
full drift d=(-2,2). One selected C cycle gives closed excursions

    E8  = RRRLLLLR, phases46 through53, growth0;
    E92 = phases56 through147, growth12.

There are only four remaining connector updates. At the phase45 cut, exactly

    standard104 = R E8 L R E92 L = A10 B94,
    A10 = RRRRLLLLRL,   B94 = R E92 L.

The complete E92 and B94 words are in the certificate. The other C cycle gives
an actual12-read growth4 excursion and an88-read growth8 excursion, again with
four connectors. Thus even this known WHITE controller contains a genuine
neutral discovery excursion; no strict positive-growth charge per excursion
is available without an additional hypothesis.

A10 is precisely the isolated prepared10 word whose infinite repetition has
one required BLACK-input class and lifetime winding S=3. Inside standard104
its ownership is DIFFERENT. Its two external BLACK reads are:

- L50 at(-5,1), owned by R62 of the PREVIOUS full standard period, at time−42.
  The physical equality is p62-d=(-5,1), and the age is92.
- L51 at(-4,1), owned by the actual R43 two steps before A10 begins; age8.

The two BLACK cells left by A10 are also not permanent outputs of the full
controller:

- R47 at(-4,3) is consumed at L107, which is phase3 of the next standard word,
  but lies within the SAME B94 block; age60.
- R53 at(-5,2) is consumed at L65 within that B94 block; age12.

All four of these are literal same-physical-cell source matches with exact
full-period offsets. The complete46 owned lifetimes have block counts

    A10 -> A10 : 3
    B94 -> A10 : 2 (both from the preceding A10/B94 period)
    A10 -> B94 : 2
    B94 -> B94 :39.

All twelve permanent output roots of the full standard period occur in B94.
Thus the known WHITE controller genuinely self-feeds the prepared10 module.
Neither its isolated BLACK-input root nor its isolated permanent-output root
can be retained as such after inserting it into a larger exact controller.
This is the precise physical ownership reason not to assign the isolated
module's S=3 to the complete standard lifetime graph, whose S is1.

## Whole-field finite realization and future certificate

The checker begins from the literally empty board and reconstructs every step.
It uses the already certified blank capture at9977, then selects the standard
period frame10289. The A10 cut is10334, the B94 cut10344, and the next period
cut10438. Their complete BLACK fields have758,758,770 cells respectively;
all fields, head poses,104 literal updates and46 actual R owners are stored.

At the A10 cut, precisely two of its read cells are initially BLACK. Its
complete local transformation leaves precisely two BLACK read cells and
retains ALL756 unread BLACK cells unchanged. Those two local outputs are then
actually consumed in B94 as stated above. No cropped interface is substituted
for the real board. The exact all-future periodic checker certifies the full
104-word continuation both at capture9977 and at the phase45 cut10334.

The geometric coordinates in the preceding section are normalized to headingN
at phase0. The complete blank realization has its genuine different absolute
position/heading; the certificate verifies the exact rotated physical owners
rather than identifying these coordinate systems silently.

## Scope and constructive obligation

This gives a concrete regenerative architecture and a meaningful replacement
interface: a prospective alternative may replace the large excursion only if
it satisfies ALL physical source matches, full fields, drift-orbit histories
and future repetition, not merely the two visible fuel cells. The existing
fixed-inventory rigidity theorem already covers the unchanged complete standard
inventory, and the earlier one-pose reorderings cover their stated permutation
family. No larger replacement family has been exhausted here.

The all-cap decomposition does not bound excursion lengths or connector state.
It does not establish a debt sign, WHITE S1, a different primitive controller,
or global finite-seed entry into a highway. In particular prepared10's cheap
isolated winding and standard's actual recycling are compatible facts, not a
counterexample to either controller conjecture.

## Artifacts

certify_C_cycle_excursion_normal_form.py
C_cycle_excursion_normal_form_certificate.json

The checker rebuilds both decompositions, the five supplied-word controls,
60 rotation/power controls, and the complete blank-board realization. It uses
the retained exact finite-support periodic checker, not an observed finite
repeat. Exact dependency hashes are embedded in the JSON.
