# Three one-minimum growth-eight interfaces cannot complete

24 October 2026. Author all-cap local theorem with an exhaustive finite
certificate, submitted for independent review. No whole-front period, width,
or visit bound is imposed. The fourth one-minimum branch is NOT excluded here.

## Statement and exact IDs

In the signed full diagonal-two read-minimum normalization, full drift is
(2,-2), incoming axes have the indicated invariant sector, and t=x+y. At growth
eight the signed 100-case necessary remainder contains four one-minimum cases.
The present theorem excludes these three exact complete lower interfaces:

    ID (1,[0,0]): (W,empty); (N,SS);  (WE,WWE).
    ID (1,[1,0]): (W,empty); (N,SS);  (WEW,WWE).
    ID (3,[3,0]): (W,empty); (NS,SS); (WEWWW,WWEE).

The semicolon separates consecutive t=-1,0,1 rows, with lane x=0 first.
All strings are incoming headings in complete WHITE read order R,L,R,L,... .
These are not local factors with arbitrarily truncated last reads.

Thus, if only one minimum class is read in a hypothetical complete WHITE g8
front with this full drift, the only remaining coarse interface is

    ID (3,[3,1]): (W,empty); (NS,SS); (WEWWW,WWEEW).

This is a necessary interface, not a color-compatible finite controller. The
three excluded IDs are explicitly checked against the prior 100-case set and
removed, leaving 97 necessary open coarse interfaces: one one-minimum, twenty-two
one-quadruple F4, and seventy-four two-quadruple F4. All other drift types remain
open. The result neither proves g>=12 nor forces the standard footprint.

## Three derived rows, with every exterior port open

Starting with each fixed lower interface, complete the two physical quotient
classes at levels t=2, then t=3, then t=4. No history at t>=5 is specified.
All current upper ports retain their full multiplicities and ordinal labels.
A missing/empty class is allowed whenever the exact mandatory ports permit it.
In particular support termination is not silently forbidden.

For an even-level vertical-axis cell, let I be its mandatory incoming N count,
J its mandatory outgoing W count, and X its number of R reads arriving N.
Then J=ceil(n/2)+I-2X implies n<=2(I+J).
For an odd-level horizontal-axis cell, take I as its incoming E count and J as
its outgoing S count. Then J=floor(n/2)-I+2X implies n<=2(I+J)+1.
Both bounds follow from the already fixed physical lower ports. The largest
bound used here is 32, not a cap assumed elsewhere in the front.

Every lower successor chain that leaves an unknown upper cell and returns to
that SAME PHYSICAL cell, with no intermediate read there, gives an exact
consecutive-rank equation: the specified incoming-port ordinal is immediately
after the specified outgoing-port ordinal. All full drift lifts and complete
lower paths are stored. Chains with unequal physical endpoints impose no such
identity, even when their quotient class agrees.

## Complete helper generation, not a heuristic domain

Each upper history has precisely two possible incoming headings. The certificate
enumerates their entire binary prefix tree to the derived bound. A prefix keeps
its two exact accumulated mandatory port counts, the immediately preceding
outgoing ordinal (or none), and any incoming ordinal required at the next read.
A branch is pruned only if it exceeds a mandatory count or violates one of the
literal consecutive-rank equations. A completed word is retained whenever both
counts are exact and no required next read is pending. Both final parities are
retained, and a complete word may also be extended if the bound permits it.

Induction on prefix length proves that every complete history satisfying the
counts and first-return equations is generated exactly once. No DP memoization,
solver result, seed sample, or unproved chronological ordering is used. The
certificate retains all generated words and every pair, including all rejected
ones. Surviving pairs become precisely the parent set of the next row.

## Finite cover and transparent rejection reasons

The three rounds have these total pair counts and remaining open counts:

    ID(1,[0,0]): 8 -> 8, 44 -> 22, 411 -> 0.
    ID(1,[1,0]): 14 -> 11, 429 -> 120, 13066 -> 0.
    ID(3,[3,0]): 12 -> 8, 244 -> 48, 3519 -> 0.

Across all rounds there are 11,155 actual skipped-rank first returns; 5,963 full
g8 residue-budget failures; 284 explicit positive rank-clock cycles; and 128
closed event components. The 217 intermediate OPEN outcomes are propagated,
not declared realizable or silently discarded.

Every skipped-rank witness is an uninterrupted physical successor path with
no intervening read at the repeated physical cell, but with nonconsecutive
complete ranks. Every clock witness is an explicit cycle of inequalities
X_v>=X_u+C+K*P, having K>=0 and C+K*N>0, where N is the number of named read
events and every complete period P>=N. It therefore fails for every possible
period, not merely a tested P value.

Of the closed components, 125 have winding -1 and force positive length=-P.
The other three have winding +1 BUT have additional named events outside the
component. They are proper closed components, incompatible with the one actual
full quotient event orbit. Winding +1 alone is not treated as a contradiction.
Every component and its outside-event count are retained.

The residue test uses all ten nonnegative full parity inventories summing to
eight and satisfying the signed congruences in the earlier signed cover.
Each failed subset stores a violated parity bin for EACH of the ten vectors.
Complete named odd-read classes must be a subset of the full odd inventory;
no partial subset is assumed balanced or identified with a physical wake.

## Dependencies and limits

`certify_one_minimum_three_branches.py` and
`one_minimum_three_branches_certificate.json` contain the complete recursive
cover, all physical first-return paths, generated helper domains and rejection
witnesses. `ONE_MINIMUM_THREE_BRANCH_SHA256SUMS` binds these and the retained
literal ordinal graph producer, signed 227-case source and signed 100-case
source. The proof does not depend on any discovery scan or historical width-ten
metadata. The independently signed source results remain necessary premises;
the present cover's independent status must be checked separately.
