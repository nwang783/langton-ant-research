# The complete radial square inventory has a WHITE-start local ordering

24 October 2026. Exact port-model realization; independent audit pending. NOT a full ant orbit or finite seed construction.

## Result

The complete central2×2 projection of the summable r=1/2 radial flow, multiplied by32, can be realized by the exact four-cell ant dynamics starting with all four cells WHITE and ending all WHITE, provided an external supplier chooses the successive incoming ports. There are96 entry episodes and288 reads. At EACH cell, the successive actual local turn word is(RL)^36, with counts

    inner L30, outer L6, entry R18, exit R18.

These are precisely TWICE the15/3/9/9 inventory discussed in the earlier square component note. Thus the full central inventory is not ruled out even by exact local visit alternation and all-WHITE initialization. What this model omits is the globally realizable exterior path between the prescribed ports.

## An explicit construction, not a flow solver

Label the square vertices cyclically0=(0,0),1=(1,0),2=(1,1),3=(0,1), in the sector whose internal directed cycle is L. An external entry at a BLACK cell gives a single outer L and exits. An entry at a WHITE cell gives R, then successive inner L turns through black cells, then a final R at the next white cell and exits.

A preparation/cleanup packet based at vertex v, from all WHITE, is:

1. enter v: RR writes v and v+1;
2. enter v: outer L clears v, leaving just root r=v+1 BLACK;
3. eventually enter r with its BLACK color: outer L clears r and restores all WHITE.

Before step3, a pure inner circulation based at a one-BLACK root r consists of four entries

    r+2, r+1, r, r-1  (indices modulo4).

Their words are RR, RLLLLR, RR, RLLLLR. They restore the same one-BLACK root. At every vertex they add two inner L turns, one entry R, and one exit R, with no outer L.

Run three sweeps of the preparation/cleanup packet, each sweep using v=0,1,2,3. In the first preparation only, insert fifteen copies of the pure inner circulation before the final cleanup. The three sweeps contribute, per vertex, six outer L, three entry R and three exit R. The fifteen inner cycles add thirty inner L and fifteen of each crossing R. This yields the claimed table exactly.

The exact64-state local transition table from the prior note and a direct replay of this96-entry word both verify every color and heading. There is no search, assumed schedule, or averaged-flow approximation inside the square.

## Why this is not an actual finite-seed construction

After each exit, the actual ant would have to traverse the exterior and arrive at the NEXT specified entry with its actual heading, while preserving all earlier outside writes and satisfying every exterior first-read and revisit color. This packet does not supply those trajectories. Entry selection is an external control, not a legal ability of the autonomous ant.

The earlier literal empty-seed control supplies ONE genuine pure-circulation component and its324-read exterior connector. It does not supply the96-entry exterior protocol here. Nor does concatenating abstract copies prove a bounded-seed realization, a larger-box realization, or an infinite recurring circuit.

The precise conclusion is a scope reduction: for this central square, neither stationary balance nor exact single-patch alternation plus WHITE initialization excludes the radial inventory. A successful obstruction must constrain the causal exterior-port ordering or joint schedules of overlapping patches. The chronological last-exit-root lemma remains valid for the pure inner-L subpacket; the outer L turns here supply WHITE-root exits and evade its restricted premise.
