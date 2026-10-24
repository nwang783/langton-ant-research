# Exact obstruction to a naive doubled-edge forest lemma

22 October 2026. Finite exact counterexample, not a periodic front and not an infinite multiplicity-three trace.

## The false local assertion

It is not true that the directed edges traversed at least twice in a finite multiplicity-three ant history form a forest, even if every vertex of the asserted cycle was initially white and finishes its complete RLR history within the prefix.

## Witness

Use coordinates east=x+, north=y+, initial ant position (0,0) heading north, right on white. The initial black set is

    {(-2,0), (-2,1), (-2,3), (-1,3)}.

The first 47 turns are

    RRRRLRRRRLRRLRRLRRLLRRRRLLRRLRRLRRLRRRRLRRRRLLL.

No physical cell is read more than three times in these 47 turns. The ant then reaches (0,3), where the next read would be the fourth, so this witness does not extend as a globally cap-three trace.

Already by time 37 inclusive, the directed doubled-edge graph contains the counterclockwise unit-square cycle

    (0,2) -> (-1,2) -> (-1,1) -> (0,1) -> (0,2).

All four vertices were initially white. Their complete histories within the prefix, using zero-based read time and incoming heading, are:

    (0,2):  (20,R,N), (24,L,N), (36,R,S)
    (-1,2): (17,R,E), (25,L,W), (37,R,W)
    (-1,1): (6,R,N),  (18,L,S), (26,R,S)
    (0,1):  (7,R,E),  (19,L,E), (23,R,W).

The edge-crossing times are respectively

    (0,2) -> (-1,2): 24,36
    (-1,2) -> (-1,1): 17,25
    (-1,1) -> (0,1): 6,18
    (0,1) -> (0,2): 19,23.

Thus all four are opposite-heading triple types. The directed doubled-edge cycle turns L at every vertex, but its middle L events are not one closed time-ordered ant excursion. One must not infer a chronological closed orbit from the existence of this spatial cycle.

The finite witness is directly replayable from the four-cell seed. The discovery probe is `probe_cap3_double_cycles.py`; its search bounds do not enter the validity of the displayed counterexample. The stronger assertion that such cycles cannot recur indefinitely in a finite-seed cap-three trace remains unproved by this example.
