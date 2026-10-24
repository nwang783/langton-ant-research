# Adjacent two-flat pair gates leave only RR open

24 October 2026. Complete WHITE histories of at most four reads are
assumed at EVERY displayed and count-closure cell. No period, drift,
critical-level or global-maximum assumption is used by this local cover.
Author result pending independent review. It does not classify every
possible global two-flat circle.

## Exact physical gate and its complete domain

Take a b-path, not an arbitrary tree path, with the following roles:

    all-N 3/4 sink, V, flat RIGHT F, middle, flat RIGHT G, V, 2->3/4 source.

The two end RIGHT contacts may independently have three or four reads.
Both outer V contacts are flow-two LEFT WWEE, up to physical rotation.
Both flat contacts independently have their complete X=EEWW or Y=EWWE
history, rotated to their own incoming cycle heading.

The middle is either empty (RR), a single LEFT O/U/V (RLR), or two
LEFT contacts each independently O/U/V (RLLR). Thus the cover includes
all 16 + 48 + 144 = 208 complete primary choices. It is deliberately an
overapproximation: no critical last-LEFT or singleton-U exclusion is
needed. Normalize the initial sink to (-1,-1), incoming N, and then draw
EVERY next physical b edge. This fixes every coordinate and rotation.
The executable records them, not merely turn words.

Add a cell only when it completes two already known neighboring ports,
and iterate that operation to closure. The resulting finite forced
corner sets have 8,16,12 cells for RR,RLR,RLLR respectively. These are not
imposed search radii. At each added cell retain the empty history and
ALL 1..4-read alternating WHITE histories on its physical incoming axis.

Match the complete counts across all internal physical edges, including
zero counts. Then match ordinal ONE to ordinal ONE, and so on. Every
forced literal return to the same PHYSICAL cell must reach its NEXT
complete rank, not any later or earlier rank. Remaining same-cell gaps
are at least four; exact successor edges take one time step.

## Exhaustive local result

Arc consistency followed by complete finite enumeration leaves precisely
170,592 count-compatible completed patches. The outcomes are

- 170,240 literal skipped/reversed-rank or closed-event returns;
- 288 positive exact-clock cycles;
- 64 necessary OPEN patches.

All 64 open patches are RR. Every RLR and RLLR patch is excluded already
by literal physical ranks or clocks. The independent stream/global-M
check and critical-side check in the executable are never needed to
remove an additional patch: there are zero survivors before either could
supply an extra exclusion. In particular arbitrary ages at the open
ports cannot repair the excluded finite successor routes.

For RR there are 16 primary sink/source/flat choices and exactly four
necessary completions of its two unknown corners. In the normalized
coordinates these are

    (-1,0) = WEW or WEWE;
    ( 2,0) = SSS or SSSS.

All other cells carry the recorded primary histories. These complete
local port/clock networks remain OPEN at their exterior ports. They are
not physical board factors, complete WHITE fronts, assigned global phase
schedules or regenerative controllers. No passive supplier is declared
fresh, paid or absent.

## Remaining global composition question

The cover applies only when the displayed immediate outside contacts
are a high sink and high source with the stated singleton V caps.
A global reduction to that exact gate must separately establish these
roles, account for full-drift quotient aliases and retain all other
branches. The result does not prove that every pair of flats is adjacent,
that all flat clusters are finite, or that a third flat is globally
required. The surviving RR gate is the next constructive exterior target.

Files: check_two_flat_pair_reader_closure.py/json. The checker imports
only the retained fixed physical-port/clock utility from
flat_flow2_symbolic_row_with_odd_left.py; there is no period scan.
