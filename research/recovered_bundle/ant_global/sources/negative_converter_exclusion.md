# A finite exclusion of narrow backward converters of the standard wake

Working computer-assisted result, 21 October 2026. This note specifies the
mathematical reduction, the complete finite search, and its limits. It does
not prove the highway conjecture or stability under arbitrary perturbations.

## 1. State and exact proposed theorem

Use headings N,E,S,W numbered 0,1,2,3. A white read turns right; a black
read turns left. A complete update flips the read cell and moves one step.
Put `s=x-y`, and label a translation class under `(2,2)` by `(s,r)`, where
`r=x mod 2`. The invariant heading sector is `h-x-y mod 2`.

The standard highway in `../root/standard.json` starts at the origin facing
west and has displacement `(-2,-2)`. Its settled wake U has the following
black classes, recorded by x parity on each row:

| s | black x parities in U |
|---:|---|
| -3 | 0,1 |
| -2 | 1 |
| -1 | 0 |
| 0 | 0 |
| 1 | 1 |
| 2 | 0 |
| 3 | 0 |
| 4 | none |
| 5 | 1 |
| 6 | 1 |
| 7 | 0,1 |

There are twelve black classes. These bits are independently recovered by
counting the odd visit classes of the standard word, without reading the
stored class table. The same word also passes the independent infinite-word
check as a forward highway after a half-turn of the plane.

A periodic converter here means a bi-infinite actual ant trajectory whose
position and heading repeat after P updates with full displacement `(2,2)`.
Each physical cell is visited finitely often. Its color before its first
visit is prescribed by U. The color after its last visit defines a second
`(2,2)`-periodic field V. Cells outside the visited strip retain their U color.

**Proposed theorem.** There is no such converter satisfying all three
conditions:

1. Its sector is the standard highway's sector, `h-x-y = 1 mod 2`.
2. Its entire trace lies in `-3 <= s <= 7`.
3. V has fewer than twelve black translation classes.

The period is unrestricted in the theorem. The proof below reduces it to a
finite set of exact possibilities. The final accepted search uses only the
elementary port equations in Section 3. It does not depend on the new
third-row charge theorem, the root analysis's clock screen, signed lane charges,
or any inherited chronology implementation.

## 2. Immutable guardrails and complete output inventory

On an odd s row, the specified sector gives incoming heading N or S. At
`s=7`, any first arrival from inside the band has heading S. The row is all
black. Its black turn goes E to `s=8`, outside the band. Thus no cell on
`s=7` is visited. At `s=-3`, the first incoming heading is N and the black
turn goes W to `s=-4`. This row is also unvisited.

Consequently both guardrail rows remain fully black. Every candidate V has
these four black classes. The actual path is confined to `-2 <= s <= 6`.

At either of these new extreme rows, the arrival sector permits an inward
turn only on black. The initial black cells comprise precisely the r=1
class. A visited cell there is therefore read once, on black, and becomes
white. No initially white cell there can be visited. In particular each
extreme row has either zero or one event per full period.

For each translation class, the signed turn count equals its final black
indicator minus its initial black indicator. Summing gives

    #R - #L = |V|-|U| = |V|-12.

The heading returns after a period, so this number is divisible by four.
If `|V|<12`, the only options are 0,4,8. The guardrails exclude zero. There
is exactly one mass-four output: the four guardrail classes. For mass eight,
choose four of the eighteen classes on rows -2 through 6. The inventory is
therefore exactly

    1 + binom(18,4) = 3,061

labelled outputs. We enumerate all of them, including those which other
necessary conditions would immediately eliminate. No lane symmetry is used.

## 3. Exact row ports give a finite period bound

Let `v_s` and `u_s` count the black classes in V and U on row s, and put
`Delta_s=v_s-u_s`. Let `I_s` be the number of crossings from s to s+1 during
one period. Because the transverse displacement is zero, this also equals
the number of crossings from s+1 to s. Let `N_s` count events on row s.
Then

    N_s = I_(s-1)+I_s,
    P = 2 sum_(s=-2)^5 I_s,
    I_(-3)=I_6=0.

At an even s row, a white event uses one port toward the upper row; a black
upper corner uses two. At an odd s row, a black event uses one such port and
a white upper corner uses two. Counting lower ports as well gives

    (3 I_s-I_(s-1)-(-1)^s Delta_s)/4 in Z_(>=0),
    (3 I_(s-1)-I_s-(-1)^s Delta_s)/4 in Z_(>=0).       (1)

These are simply corner counts. No initial whiteness is assumed.

In particular,

    I_s <= 3 I_(s-1)-(-1)^s Delta_s,
    I_(s-1) <= 3 I_s-(-1)^s Delta_s.                  (2)

Starting with the zero crossing count at either outer end, (2) gives finite
integer upper bounds on every I. This supplies a finite search domain before
any chronology search is run. The extreme-row observation also gives

    I_(-2)=1-v_(-2),  I_5=1-v_6.

The nonzero I values must form one contiguous interval: a single trajectory
cannot occupy two portions of the strip separated by an uncrossed edge.

Finally, P is divisible by four. The directions alternate between the two
coordinate axes, so there are P/2 horizontal updates. A horizontal net
displacement of two forces P/2 even. More precisely, the outgoing (and
incoming) direction totals must be

    N=E=P/4+1,  S=W=P/4-1.                            (3)

`conversion_full_row_screen.py --ports-only` enumerates every nonnegative
integer crossing tuple satisfying (1), the zero exterior counts, contiguous
support, the extreme counts, and `P>0`, `P=0 mod 4`. Its backward bounds are
obtained recursively from (2). All arithmetic is exact.

The complete accepted inventory contains:

| Stage | Count |
|---|---:|
| labelled output fields | 3,061 |
| outputs with at least one row profile | 658 |
| row profiles | 30,431 |
| maximum possible P in these profiles | 216 |

The 658 outputs comprise the single mass-four output and 657 mass-eight
outputs. This table is a finite arithmetic result, independently reproducible
from the short script and the listed U bits. It is not a claim that any
profile is chronologically realizable.

## 4. Exhausting physical chronology on an arbitrary input field

`conversion_chronology.cpp` is a new, compact enumerator. It takes U,V and
the exact `N_s` values of one row profile. It does not assume a white input.

For a class `(s,r)`, choose a visit count n with

    n = U_(s,r) xor V_(s,r) mod 2.

The counts of the two classes on a row sum to `N_s`. A representative cell is
`q=(r,r-s)`. Its visit k, starting at k=0, reads the color

    c_k=U_(s,r) xor (k mod 2).

The code enumerates the incoming side of every visit. If `a=1` means arrival
from row s+1, then the sector fixes its heading exactly:

| row parity | a=0 | a=1 |
|---|---|---|
| even | E | W |
| odd | S | N |

The color then fixes its outgoing heading. Thus every possible physical
event at that class is included, with no left/right choice discarded.

Rows are assembled from top to bottom. For a fixed pair of neighboring
physical cells, departures and arrivals must match in chronological order.
The outgoing events already exposed on the upper row therefore match the
chosen incoming events of the new row in their order. The reverse directed
crossings are matched in the same way. No independent permutation of these
crossings is possible in a real trajectory.

Each attachment records its exact translation shift ell. An edge from node
i at its representative cell to node j at its representative plus
`ell*(2,2)` imposes

    time_j + ell*P = time_i+1.                       (4)

Partial graphs have at most one predecessor and successor per event, hence
are disjoint paths unless a cycle has already closed. A closed component
before all P events have been assembled cannot later join the rest and is
rejected. For each open path, (4) fixes each event time up to one additive
path constant. Consecutive visits to the same physical cell must be at least
four updates apart. The code checks the resulting exact difference
inequalities for a positive cycle. This is a necessary ordering test only;
it never assumes the inequalities suffice to construct a trajectory.

It also rejects partial counts exceeding the direction totals (3) or P/4
events in any of the four coordinate-parity classes. Both are necessary
identities for a complete period with displacement `(2,2)`.

At completion, all P events must form one directed cycle with total lift
one. Following it assigns a physical time to every representative-cell
event. Every class's times must strictly increase with its visit rank. These
checks, together with the colors and geometric edges already fixed, are
sufficient to reconstruct the full bi-infinite orbit.

Thus a real converter yields one branch of the enumeration. Every complete
branch is either rejected by a necessary condition or produces an explicit
word for independent verification. This is finite exhaustive enumeration
over a proved finite domain, not simulation up to an arbitrary horizon.

## 5. Independent positive controls and completion audit

The solver is checked on three realizable cases:

| Case | P | input mass | output mass |
|---|---:|---:|---:|
| ordinary standard highway after a half-turn | 104 | 0 | 12 |
| color-complemented, reflected standard highway | 104 | 22 | 10 |
| two-row `RLRL` staircase | 4 | 2 | 2 |

The second and third tests require nonwhite input colors. They check the
arbitrary-substrate behavior of the enumerator.

`conversion_controls_and_verifier.py` checks each returned word independently
by ordinary coordinates. If the word's event i occurs at `q+ell*(2,2)`,
then the corresponding visit to the fixed physical representative q has
time `i-ell*P`. Sorting these finitely many times checks the entire repeated
trajectory at that cell, including all translated copies. The verifier
checks alternating colors starting at U, the final field V, the exact drift,
and the heading sector. It does not call the gluing code.

The final completion counts, run records and hashes are recorded in
`negative_converter_coverage_audit.json`. No timeout, interrupted run or
positive-control stop is accepted as an exclusion. The full search logs are
`conversion_ports_chronology_results.txt` and
`conversion_ports_resume_results.txt`; together they contain every one of
the 30,431 profile IDs exactly once. All records report complete exclusion.
There were 29,348,386 partial checks and no solutions. Their common complete
input inventory is `conversion_ports_chronology_inputs.txt`.

The independent coverage audit also counts every allowable row profile with
a separate dynamic program. It uses the universal crossing bounds
`(1,5,17,53,53,17,5,1)` obtained from `I_next<=3 I_prev+2` in both directions,
rather than the generator's output-dependent backward bounds. For each of
the 3,061 output fields, its entire period-count distribution agrees exactly
with the enumerated profiles. Necessary membership, uniqueness, and equal
cardinality certify equality of the finite row-profile sets.

This is an internally checked computer-assisted result. It has not been
formally verified or externally reviewed. No priority claim is made.

## 6. What this result does and does not resolve

The result excludes a specific mechanism: a same-sector ant cannot march
back through a settled standard trail, remain within its original band,
repeat with full advance `(2,2)`, and reduce the number of black classes left
behind. Reversal alone gives an eraser in the opposite sector; the present
statement concerns the sector that a real forward perturbation preserves.

The restrictions matter. A converter could widen its path, have a different
full displacement, leave twelve or more black classes, or fail to repeat.
None of those cases is classified here. The result therefore does not imply
stability under all finite perturbations, a uniform bound on nonstandard
events, or capture from every finite initial black set.

## Reproduction

From the shared workspace root:

```sh
python ant_global/sources/conversion_full_row_screen.py --ports-only
g++ -O3 -std=c++17 ant_global/sources/conversion_chronology.cpp -o ant_global/sources/conversion_chronology
ant_global/sources/conversion_chronology ant_global/sources/conversion_ports_chronology_inputs.txt 45 0 > ant_global/sources/conversion_ports_replay_results.txt
python ant_global/sources/conversion_controls_and_verifier.py
python ant_global/sources/audit_negative_converter_coverage.py --results conversion_ports_replay_results.txt
```

The 45-second argument is a reporting limit per profile. The audit accepts
only records marked `complete`; a timeout leaves a proof obligation open.
It does not alter the mathematical search domain.

With no `--results` argument, the audit checks the two retained accepted logs.
The replay command above uses a different filename so those logs are preserved
and no duplicate profile ID is introduced. The executable is included among
the hashed artifacts; the compilation command regenerates it when needed.
