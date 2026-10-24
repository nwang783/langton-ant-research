# Exploratory literal right-cap inverse search

Status: bounded exploratory controls only; not independently audited. No renewal candidate.

`search_eight_right_caps.cpp` searches the four right-cap words in one eight-pass excursion directly by chronological reads. Every previously unread patch bit is chosen on first read and thereafter toggles literally. The initial local cap is unrestricted on x=-4,...,width-1, y=-10,...,11, with white cells to its right. Cap paths remain in that strip and x=-4,...,width+5. Each cap must stop at its first positive-time requested target pose. Literal incoming and outgoing arm reads at x>=-4 are retained; arm reads left of that cut are omitted conservatively. This omission and the absence of left caps mean even a found prefix would not establish a complete excursion.

The first incoming A arm starts at(-4,0,E) and runs twice. Right-cap entry poses are (0,0,E),(0,2,E),(0,0,E),(0,2,E); requested exits are (0,8,W),(0,8,E),(0,10,W),(-1,9,W). Following each cap, the appropriate outgoing S/W arm is replayed far enough beyond the cut, then the next incoming B/A arm is replayed from the cut. The fourth outgoing S arm is also checked.

No final restoration or translated-cap constraint is imposed. Thus this search is only a relaxed prerequisite for one phase, not the already-excluded fixed-state renewal contract and not the still-open four-phase contract. It does not impose the necessary column charges either, so no accepted prefix could be promoted without further checks.

Current outputs:

- max cap length24, initial width4: EXHAUSTED, 781821 search nodes, 577 compatible first-cap completions, none surviving the second cap plus its following fixed arms.
- length28,width6: UNKNOWN at10000001 nodes;1493 first-cap completions.
- length32,width8: UNKNOWN at10000001 nodes;987 first-cap completions.
- length40,width12: UNKNOWN at10000001 nodes;34 first-cap completions.

The larger counts depend on depth-first branch order and are not comparative evidence. Capped searches are inconclusive. Words printed on unsuccessful runs are partial scratch candidates, not feasible four-cap outputs. The earlier SMT array searches also returned UNKNOWN. No computation remains running.

This inverse chronology search avoids the slow general SMT array encoding, but it still faces exponential cap geometry. A genuinely new mechanism or finite-state interface is preferable to simply increasing these caps indefinitely.
