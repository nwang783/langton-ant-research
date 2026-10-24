# Exact four-channel ownership interface of the middle-short C core

24 October 2026. Author algebraic corollary submitted for independent checking.
Assume the now independently signed three-face coincident C core6a240f5a
(report9f0a6ffa), including its exact six open T0..T10 interfaces. Higher fields,
clocks and routes remain unspecified. This is NOT a finite controller state.

## The complete core event inventory

Take all reads whose active C face belongs to the full-drift classes C1,C3,C5.
There are exactly24 reads per period:14 R and10 L. This is a complete active-face
inventory, not the set of all reads at its boundary cells. For example the S
reads at T8 occur outside the core and MUST remain outside in this accounting.

The actual one-step successor graph induced on these24 events has four open,
event-disjoint components. Name them by their first event:

X: T7.R2, word RLRRRRLRRRRL, length12.
Y: T4.L3, word LLRLRRRRL, length9.
Z: T7.L1, word L, length1.
W: T5.L3, word LL, length2.

Every phase, physical read position, full integer lift and boundary neighbor is
stored. In particular Y and W cross representative seams; their voltages are
not discarded by writing the short words. These channels exhaust the complete
core. They are genuine contiguous actual-read channels, not lifetime circuits.

The exterior interval from X to Y is exactly ONE L read, T7.L3. It consumes
the BLACK lifetime written at X's first event T7.R2, with exact age12.
The other three maximal exterior intervals remain unrestricted.

## Two possible cyclic orders, not arbitrary permutations

For T8=NNSNSSSS the core order in the actual event cycle is

    Y, W, Z, X, Y.

For T8=NNSSSNSS it is

    Y, Z, W, X, Y.

To verify this without choosing a period: set A(C5)=0. Then the RRRRL end of Y
occupies0..4, X starts at P-17, and the LLRL beginning of the next Y occupies
P-4..P-1. The third N arrival of T8 is n, so W occupies n-1,n on the preceding
physical translate of C3. Z is T7.L1, immediately after T8's other S/L departure.
The complete T8 ranks put W before Z in the first profile and after Z in the
second. All gaps and translates remain physical.

The two core orders are not the four lifetime-boundary matching types. No
one-to-one correspondence or compatibility of every combination is asserted.

## Three crossing BLACK lifetimes, with exact owners

Pair each complete WHITE physical cell's R reads to their actual next L reads.
Of the14 R writes in the core:

- nine are consumed inside the core;
- three are permanent outputs, at T0,T1,T2;
- two are consumed outside, namely T6.R2 -> T6.L3 and T7.R2 -> T7.L3.

There is exactly one imported lifetime consumed in the core:

- T8.R2(S) -> T8.L3(N) for NNSNSSSS;
- T8.R4(S) -> T8.L5(N) for NNSSSNSS.

Its producer is on C9 and its consumer is on C5, at the SAME physical T8 cell.
It is an opposite-heading owner, not initial BLACK fuel or a fictitious reverse
WHITE root. The two exports have actual R producers inside the core and L
consumers on C7. No source identity is omitted.

Thus the exact local mass identity is

    core (R-L)=4 = three permanent outputs + two exports - one import.

The five other permanent output classes are T6,T7,6c+1,6a+2,6a+4, all outside
the core. The exterior's update imbalance is therefore also4: five permanent
outputs + its one export to the core - its two imports from the core.

These are exact lifetime identities, NOT a monotone stock or paid-input budget.
The exterior may regenerate the imported lifetime and reuse old outputs. Its
three unknown intervals are not themselves complete WHITE translating words,
so the general growth>=8 theorem cannot be applied to their imbalance4.
Nor does subtracting the core's C-edge circulation physically splice the ant.

## A small first-entry consequence at C7

All six signed interfaces start T10 with SN. Therefore the upper SS alternative
in the signed C7 first-parent list is unavailable. C7 really first activates
through T7.L1 from C5, at T10.N/L1. That first active read is L, with its actual
previous producer T10.S/R0 on C11.

C11 has thus already been active before C7 is discovered. This does not prove
it lies in a different first-parent basin: a spatial ancestry path is still not
an actual chronological subarc. Both the old producer and the whole higher
region must be retained. The later terminal-C7 channels and their one possible
old-owner exception remain exactly as signed in10b4b262.

## Scope and reproduction

certify_middle_short_C_core_ports.py
middle_short_C_core_ports_certificate.json

The checker rebuilds the full physical ordinal successor graph for all six
interfaces, selects active sectors rather than cropped cells, reconstructs all
four channels and boundary voltages, and checks every internal/export/import
lifetime. The two core descriptions are independent of the unspecified higher
completion. No period search or new row-domain expansion is performed.

The live constructive/obstruction target is now explicit: complete the three
unknown exterior intervals in one of these two orders, with their precise
owners, complete full odd inventory and all unread fields. Their lengths,
higher visit multiplicities and cross-period preparations are not bounded here.
No new controller, four-type exclusion or general first/last connectivity result.
