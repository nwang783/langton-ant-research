# A genuine axial record imports one fresh clockwise unit loop

24 October 2026. Corollary of the finite-board frozen-mirror representation and the pointwise winding surgery theorem. Independent audit requested. This is not a new occurrence theorem.

Let a finite-seed classical ant reach a strict axial record beyond the rectangle containing its entire initial BLACK support and all earlier head positions. Write p for the current head and n for the outward signed coordinate normal. Its incoming heading is n, its current cell is WHITE, and every current BLACK cell lies strictly in `n.q<n.p`.

Let a be the actual admissible incoming state at p and b the opposite incoming state. In the frozen current mirror field:

1. b belongs to the untouched clockwise four-step unit-square circuit on the fresh side of the record line. Its four cells all lie in `n.q>=n.p` and are WHITE.
2. The frozen circuit containing a is wholly in `n.q<=n.p`. It is distinct from b's circuit and is clockwise.
3. The actual R update merges these two circuits. If the active circuit had length L and signed grid area -A, the new active circuit has length `L+4` and area `-(A+1)`.
4. The global positive-winding area P is unchanged by this record update.

## Proof with the whole old field retained

After rotation take n=E and p=(0,0). The b-state has incoming W and follows the four WHITE cells `(0,0),(0,1),(1,1),(1,0)` before returning to b. Its domain is the one forward plaquette.

The old a-state has incoming E. Every modified baseline circuit comes from a BLACK cell with x<0 and therefore has all physical states at x<=0. Its containing frozen circuit consequently stays on that old closed half-plane. If it is untouched, its own baseline square also lies there. Thus its plaquette domain is disjoint from the forward unit-square domain.

The flip joins these distinct circuits. The exact surgery classification permits merging disjoint nonempty domains only when the orientations agree. The forward unit loop is clockwise, so the active one is too. Signed winding and lengths add. The true next head belongs to this merged circuit because the physical update uses the old successor and only then regards the flipped frozen field.

All other normals and the other checkerboard sector follow by translation and quarter-rotation, with the baseline coloring carried along. No reflection or invariant-sector reversal is used.

## Why this is not a renewal charge

A record injects four active boundary states but no positive winding area. Subsequent interior surgeries can detach circuits, import old ones, and generate or cancel positive winding. The signed MT countercontrol shows such generation during a still-noncanonical completed drought. Detachment is not permanence and the imported unit loop is not an independently consumable old lifetime.

For any finite interval the retained active-length ledger may therefore separate record imports (`4` each) from all other merges and splits. It still needs a new non-reuse or chronological estimate on those other terms. This corollary identifies the fresh boundary interface; it does not bound how often a bounded clock window occurs.

## Exact controls

`check_mirror_pristine_record.py` independently replays the complete 10,081-read blank and 109,168-read MT100 histories from their original seeds. At every stored augmented-hull record it checks the entire current BLACK half-plane premise, the two full frozen circuits, their orientations and domains, and the actual merger. Every record carries a digest of the complete current field. The full trajectories and infinite futures are bound by the parent winding package. No prepared port is omitted from the initial record hull.
