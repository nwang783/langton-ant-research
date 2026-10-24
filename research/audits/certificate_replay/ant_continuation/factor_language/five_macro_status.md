# Five-macro reduction for tails with no adjacent forbidden ten-windows

Date: 21 October 2026. Status: exact finite graph reduction and a proved infinite-class exclusion. The finite-seed highway conjecture remains unresolved.

## Convention and source theorem

White causes R, black causes L, then the cell flips and the ant moves. The initial heading is north, with coordinates north=(0,1), east=(1,0). Let F be the 84 cyclic length-10 factors of the standard 104-turn highway word. A J event is a ten-turn factor outside F. The condition studied here is that no two consecutive ten-turn factors are both J events.

The existing source `kehao95/langtons-ant-core`, `factor_language/proof/ten.md`, proves that a finite-support orbit with no future J events eventually enters the standard highway. Our graph enlargement below permits infinitely many isolated J events. It does not assume their number is finite.

## Exact graph coverage

`no_adjacent_defects.cpp` enumerates all physically feasible 150-turn words with no adjacent J events. Physical feasibility is checked exactly: successive reads of each geometrically determined cell must alternate L and R. This condition is necessary and sufficient; the cells first read as L form a finite seed realizing the word.

The exhaustive run finishes, without reaching its node cap, after 6,866,831 DFS nodes and outputs 304,468 words. Prefix/suffix overlap gives a graph on 270,902 length-149 histories. `no_pair_graph.py` finds precisely three cyclic strongly connected components:

| Component | Vertices | Internal edges |
|---|---:|---:|
| Existing T24 periodic mode | 24 | 24 |
| Standard W104 | 104 | 104 |
| Enlarged nonstandard component H | 34,712 | 36,277 |

Every infinite no-adjacent-J orbit eventually stays in one of these components. T24 requires infinitely many initially black cells, by the existing source's periodic-mode calculation. W104 is the intended conclusion. Hence the remaining case is an infinite physically realizable path within H.

The marker is M=`LLLLRLRRRRLR`, of length 12. There are 995 **actual length-149 histories** in H ending in M. Removing them leaves an acyclic graph. `verify_five_macros.py` independently verifies this directly on all 34,712 histories, without using minimized quotient states. It enumerates all 2,747 paths from one actual marker end to the next. There are exactly five distinct appended words, of lengths 15, 18, 28, 64, and 74. Thus every infinite path in H has infinitely many markers, with marker gaps at most 74.

This coverage is a finite exhaustive certificate, not an assertion that every graph path is a realizable ant orbit. Long-range revisits impose additional physical constraints beyond the 150-step windows.

## The two marker cuts

The ant state attached to a graph port is immediately **after** reading M. Consequently an appended port-edge word is `rest+M`. The geometric macro footprints instead use the ant state immediately **before** reading M and the word `M+rest`. These are conjugate cuts of the same concatenation. They have equal lengths but different displacements and first-read requirements.

`no_pair_port_words.json` and `five_macro_actual_ports.json` contain after-marker edge words. `five_macro_footprints.json` contains before-marker blocks. `verify_five_macros.py` explicitly checks the relation `before=M+after[:-12]` for all five words.

All geometry below uses the **before-marker** convention, starting at (0,0) facing north:

| Block | Length | End position | End heading |
|---|---:|---:|---|
| C | 15 | (0,1) | west |
| V | 18 | (1,3) | north |
| U | 28 | (0,4) | north |
| Q | 64 | (-4,-4) | south |
| B | 74 | (-3,-5) | south |

The full exact strings, read traces, first-read requirements, last reads, and parity changes are in the JSON certificates. The names U and V designate the two forward, heading-preserving blocks. C, Q, and B will be called turning blocks only as a description of their geometry.

The actual marker-port graph is part of the certificate. Arbitrary concatenations of the five words overapproximate H. Eliminating all such physical concatenations would be a sufficient but stronger target; an argument restricted to the graph can use the additional history constraints.

## Theorem: exact fuel for every U/V mixture

For any nonempty word consisting of a copies of U and b copies of V in any order, the exact minimum number of initially black cells needed to realize it is

\[
4+5a+2b.
\]

In particular, no infinite U/V mixture, periodic or aperiodic, is realizable from finite black support. A complete U/V segment beginning with m black cells lasts at most

\[
28a+18b\le 9(m-4).
\]

The constant 9 is attained by pure V segments.

### Proof

Let the common four initial cells be

\[
A=\{(0,0),(-1,-1),(0,-1),(1,0)\}.
\]

The additional black cells needed by a first U or V block are respectively

\[
F_U=\{(-1,0),(-1,1),(-1,2),(0,2),(0,3)\},\qquad
F_V=\{(-1,0),(1,2)\}.
\]

Let s_j be the starting position of block j. Each U adds (0,4) to s_j and each V adds (1,3), without changing heading. Directly tracing either block proves:

1. Its read footprint has y between -1 and its endpoint height, relative to its start.
2. On its highest row it reads exactly the two sites whose x coordinates are its endpoint x and endpoint x+1.
3. Its four translated successor-A sites have last read R, so they are black at the next block boundary.
4. The blocks UU, UV, VU, and VV are each physically feasible; their exact first-read-L sets are A union F_first union translated F_second.

Every nonadjacent pair of block footprints is disjoint: two advances increase start height by at least 6, while the first footprint ends at height at most 4 and the third begins at height at least 5. Thus all consistency interactions are internal to one block or cross one of the four verified adjacent interfaces. The four interfaces therefore prove feasibility for every finite mixture by induction.

Every point of F_U or F_V with positive relative y lies strictly above all preceding footprints. The only zero-height fresh point is (-1,0); the preceding block's highest-row description proves that it too is unread. Distinct fresh sets occupy disjoint height bands. Accordingly the complete first-read-L set is exactly

\[
A\;\cup\!\bigcup_j(s_j+F_{X_j}).
\]

The union is disjoint and has size 4+5a+2b. Initial black cells at these sites are necessary, and making precisely these cells black suffices. The time bound follows from 28<=9*5 and 18=9*2. This proves the theorem.

`verify_uv_fuel.py` checks precisely the finite block/interface facts used in this proof; it is not a long-sample extrapolation.

## Consequence and remaining obligation

Suppose a finite-support orbit has only finitely many adjacent pairs of J events and does not enter W104. After its last such pair, and after finitely many component transitions, it must stay in H. The exact marker reduction and the U/V theorem imply that its macro sequence must contain infinitely many occurrences of C, Q, or B.

The remaining obligation is to exclude, for finite support, an infinite **physically consistent** path in H with infinitely many C/Q/B occurrences. The present work does not supply a decreasing resource, a uniform fold bound, or a proof of a finite fuel halo for this branch. Bounded-depth cycle tests and bounded-seed searches are exploratory evidence only.

Together with `isolated_last_event_theorem.md`, the rigorous progress is:

- a final J event cannot be isolated on its left;
- the infinite isolated-event alternative reduces to five exact macros;
- every arbitrary aperiodic tail made solely of U and V is excluded by an exact initial-black count;
- all remaining finite-support obstruction paths in this enlarged language must turn infinitely often.

The general conjecture also still requires proving that adjacent pairs cannot occur infinitely often. Even a full exclusion of H would therefore be an intermediate theorem, not the full finite-seed highway conjecture.

## Independent T24 obstruction

`verify_t24.py` checks the 24-cycle word `RRRLLRLLRRRRLLRRRRLLRLLR` directly. It returns to its heading and moves by (2,0). For each n>=0, the cells (2+2n,-3) and (3+2n,-1) are first read as L in repetition n, at zero-based phases 7 and 22 respectively. The full per-cell phase lists show that every other read of either cell occurs later. Hence these two rays must already be black at the start of an infinite repeated tail. Finite support is impossible. The check does not depend on the source attraction theorem.

## History-conditioned local-energy search

`conditioned_macro_contexts.py` normalizes each actual after-marker port to head (0,0), north. The 149-turn history determines the current color of every cell it read. The next macro's first-read requirements fix its other read cells. Forty-five of the 2,747 candidate graph edges are physically inconsistent on this full concatenation and are discarded; 2,702 survive. Their energy-relevant surrounding constraints reduce to 166 distinct contexts. No unsupported feasibility assumption is made about the unknown outside colors: they remain arbitrary, so the resulting inequalities cover a superset of complete fields.

`exact_local_energy.py` maximizes a candidate energy change over every assignment of the unknown outside cells by exact binary variable elimination. For 3x3 pattern counts the largest conditioned factor has eight bits (elimination width 7), despite individual contexts having as many as 70 unknown bits. Integer weights use exact int64 arithmetic with an explicit overflow bound. One 15-bit context was additionally audited against all 32,768 assignments by an independent simultaneous enumeration.

The attempted form is a nonnegative rotation-invariant weighted sum of nonwhite 3x3 patterns, plus a potential on the 995 finite port histories. A positive uniform decrease on all retained edges would exclude infinite H tails. The search has concluded without a positive certificate.

The ordinary rotation-invariant 3x3 ansatz is **exactly excluded** for every nonzero nonnegative cost assigned by macro type. A 159-context integer Farkas certificate cancels every port-potential coefficient, leaves every nonnegative pattern-weight coefficient nonnegative, and has positive total multiplier on each of C,V,U,Q,B. The independently verified certificate is in `../wake_clock/fold_farkas_certificate.json`, with verifier `../wake_clock/verify_fold_farkas.py` and result `../wake_clock/fold_farkas_verification.json`.

The checkerboard-sector extension with 271 pattern weights was also explored, using a cost only on V and Q. After 6,268 explicit context cuts, an interior-point LP solve reported infeasibility. A final extension added nine signed coefficients for a bounded head-local correction on relative cells {-1,0,1}^2; it reported infeasibility after 7,821 cuts. These two outcomes are **numerical infeasibility only**: no exact dual certificate was recovered. The ordinary exact dual does not certify either extension. The earlier sector run requiring decrease on every macro was interrupted and has no infeasibility conclusion.

The local-energy search is closed at these targeted tests. Its complete scope and statuses are recorded in `../global_structure/macro_energy_status.md`. No valid rank was found, and the infinite C/Q/B branch remains open.
