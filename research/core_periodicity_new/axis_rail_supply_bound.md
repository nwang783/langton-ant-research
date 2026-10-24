# A bounded standard-flight history cannot supply a long S rail

Status: approved by the independent auditor on 2026-10-22 at 22:19 UTC, including an independent six-cells-per-axis-line count.

Let S=RLLR. Suppose a finite-seed history is partitioned into r actual legal standard104 power blocks, with arbitrary phases and rotations, and a other individual updates. Let m be the initial black mass. If the resulting state executes S^N in any orientation, then

    2N <= m+a+116r.                                      (1)

There is no bound on the lengths or ages of the standard blocks. The partition must retain the complete actual history; arbitrary preexisting off-rail debris cannot be omitted.

## Proof

The audited standard_block_union_history.md gives an approximation U to the complete entry board B by a UNION of r finite settled standard rails, with

    |B symmetric_difference U| <= m+a+110r.

Each finite rail is a subset of a corresponding bilateral settled wake. In the canonical normalization that wake has twelve drift classes (t=x-y, e=x mod2):

    (-3,0),(-3,1),(-2,1),(-1,0),(0,0),(1,1),
    (2,0),(3,0),(5,1),(6,1),(7,0),(7,1).

For a fixed vertical line x=c, exactly six classes have e=c mod2, and each gives one black cell. For a fixed horizontal line y=c, exactly six classes have e-t=c mod2, again each giving one black cell. Hence every horizontal or vertical line meets a bilateral settled wake in exactly six black cells. Translation and quarter-turn rotation preserve this statement. Any axis line therefore meets the union U in at most6r black cells.

An S^N factor beginning at (0,0),N reads precisely two columns: its R reads are (0,y), and its L reads are (1,y), for y=0,...,2N-1. All these read cells are distinct. Thus all2N cells on the input line must be black at the factor's entry. In any orientation that input is an axis line l, and

    2N <= |B intersect l|
        <= |U intersect l|+|B symmetric_difference U|
        <= 6r+m+a+110r.

This proves(1).

## Scope

A fixed number of arbitrarily long standard flights, combined with a bounded-size trigger and a bounded number of other updates, cannot produce arbitrarily long S factors at fixed initial mass. In particular, an inward-spiral generator cannot obtain its first long straight S side from such a bounded-complexity standard-flight history.

The theorem does NOT bound the number of standard blocks or intervening nonstandard updates. An architecture with increasingly many intersecting old rails remains outside this obstruction. It also does not exclude an entirely different nonstandard consumer with drift parallel to a standard wake.
