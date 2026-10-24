# Arbitrary S/T mixtures: saturated ports force finite small-component fuel

24 October 2026. Author universal lemma and exact controls, submitted for
independent audit. This is not a minimal-seed-only argument and does not assume
periodic macro words. All passive fields and real lifetimes are retained.

Write S=RRRRLRLRL and T=RRRRLLLLRLRL. Assume an actual finite-board trajectory
is, from some empty-active cut onward, an infinite concatenation of these two
words, each an empty-to-empty first return, with active w mass<=7 at every cut.
We prove this is impossible.

## 1. Every preceding block supplies the same real hook

Normalize each block entry to (0,0),north in sector k=1. S ends at(-3,2),west;
T ends at(2,2),north. The last R of S writes(-2,1); the last R of T writes(1,1).
Their final L reads a different cell. At the next normalized entry, both these
surviving R-born edges have cell coordinate h=(-1,-1).

Thus every block after the first has a genuinely existing black hook at h.
It is not an assumed input marker or a recolored bit. It may initially appear
to have other attachments; the next saturation argument determines its COMPLETE
component. No claim that it was black in the original initial seed is made.

## 2. Four R updates pin the complete initial activated field

An empty w root has four white incident cells and forces four R updates. These
add four distinct black root-star edges P={(0,0),(1,0),(1,-1),(0,-1)}. Under
cap7, at most THREE preexisting black edges can join them.

The inherited hook plus the current word's first-L requirements force:

    B_S={(-1,-1),(-1,1),(-2,2)};
    B_T={(-1,-1),(-1,0),(2,1)}.

All these cells were unread during the first four updates. In each case all
three black edges are connected to the new root star. Therefore the complete
active component at cut4 is EXACTLY P union B_Y, of size7. Any additional
black attachment, no matter how remote its continuation, would exceed the
cap. Every unlisted edge incident to this component is white.

Before those updates the complete old activated components are therefore:

- in S: the straight dimer{(-1,1),(-2,2)} and the hook singleton{(-1,-1)};
- in T: the corner dimer{(-1,-1),(-1,0)} and singleton{(2,1)}.

These are complete components, not selected subsets. Other exterior components
may exist but are disjoint from this activated field.

## 3. Every intermediate attachment is determined, except the final one

### Current block S

L at update4 removes(0,0). It leaves the straight dimer active and detaches the
complete four-edge archive

    E4={(-1,-1),(0,-1),(1,-1),(1,0)}.

R at update5 writes(-1,0). Its other w endpoint is(-3,-1), already in E4, so it
MUST reimport that complete archive. No different exterior component can be
substituted: E4 was just separated from the exact cut4 component. The resulting
active component again has seven edges.

L at update6 removes(-1,1), leaving only{(-2,2)} active and emitting exactly

    E5=E4 union {(-1,0)},

a complete five-edge archive. Thus there is no unspecified passive attachment
at this earlier R. E5 stays on the actual board.

R at update7 writes q=(-2,1). This is the only remaining possible unknown
import: its other endpoint may be isolated or carry a complete dormant
component D. The last L removes(-2,2) and reaches the empty seam, leaving the
COMPLETE last-tooth component E={q} union D.

### Current block T

The four L updates at4,5,6,7 remove respectively(0,0),(-1,0),(-1,-1),(0,-1).
Because the cut4 field was complete and exact, their remaining active fields
are determined without outside input. At cut8 the three-edge active component
is{(1,0),(1,-1),(2,1)}.

R at update8 writes(0,0) toward w vertex(-1,1). This vertex is isolated: its
incident cells(-1,0) and(0,0) were just deleted, while(-1,1) and(0,1) were
white boundary ports of the complete cut4 component and have not been read.
Thus this R imports NOTHING, even with arbitrary unread exterior.

L at update9 removes(1,0), emitting the exact straight dimer{(0,0),(1,-1)}
and retaining only the active singleton{(2,1)}.

R at update10 writes q=(1,1), the only remaining possible unknown import D.
The last L removes(2,1), reaches the empty seam, and emits the complete last
tooth E={q} union D.

## 4. The next block pins that final import completely

For either current word, q is the inherited hook h=(-1,-1) in the NEXT entry
frame. Apply section2 to the next block.

- If the next word is S, the three old forced edges are h and its disjoint
  first-port straight dimer. They already exhaust the old-edge budget3.
  Their fixed three-edge graph has h as a separate singleton. Therefore E is
  EXACTLY{q}, with no attachment, and the current final R imported nothing.

- If the next word is T, its three forced old edges form exactly the hook corner
  plus the separate required singleton. Thus E is EXACTLY the hook corner.
  The current final R imported exactly one singleton connector. In current
  coordinates that connector is(-3,1) after S and(1,2) after T.

A hidden attachment cannot be absorbed into the same budget: it would add an
edge beyond the fixed three-edge graph. The forced graph's distinct components
cannot become connected without such an additional edge. The connector cell
is unread during the current word. It is a real already-black lifetime when
imported, not free material created at the seam. It need not be an original-
seed lifetime. The earlier complete-field steps show it was not silently
modified by another import in the current block.

This handles ALL later-R attachments and arbitrary unread exterior. Between
imports/emissions every other complete passive component is unchanged. There
are no silent passive merges: an R addition is the only possible new contact,
and each such addition was handled above.

## 5. Universal exact ledger and nonperiodic termination

At empty-active cuts let K be the total number of COMPLETE black w components
of size one or two. Larger components have weight zero, but remain on the board.
For finite support K is a finite nonnegative integer.

The preceding pinning proves the following complete profile ledger for a current
block Y and its successor Z. The inherited input hook is included. The optional
connector is a complete singleton import exactly when Z=T.

    YZ   activated old small components     emitted small components   K drop
    SS   straight dimer + singleton        singleton                    1
    ST   straight dimer + two singletons   corner dimer                 2
    TS   corner dimer + singleton          straight dimer + singleton   0
    TT   corner dimer + two singletons     straight dimer + corner      1

The S four-edge detachment/reimport and five-edge output all have weight zero;
none is erased. T's straight dimer and final tooth are complete. All unchanged
passive components cancel in the ledger, including arbitrary distant archives.

Thus K never increases and decreases on every case except TS. Two TS cases
cannot be consecutive because the next current word after TS is S. Every two
consecutive interior blocks therefore decrease K by at least one. An infinite
S/T tail contradicts finite nonnegative K. This excludes arbitrary aperiodic
mixtures, not merely repetitions of a chosen word or cycle.

## 6. Controls and scope

st_interior_ledger.py replays the four representative complete fields:
SS uses B_S; ST uses B_S union{(-3,1)}; TS uses B_T; TT uses B_T union{(1,2)}.
It checks every complete active component, actual imports/emissions and lifetime
ownership, final hook components, peak cap7 and exact drops1,2,0,1. These are
controls of the universal pinning proof, not a substitute for it.

This lemma alone assumes the S/T tail. Its use in a global cap-seven exit
assembly also requires the separately audited kernel/nonempty-return bound,
58-word completeness, sound word filters, exact word-pair graph and exclusion
of its other recurrent component. No cap-eight enumeration or highway-capture
claim is made here.
