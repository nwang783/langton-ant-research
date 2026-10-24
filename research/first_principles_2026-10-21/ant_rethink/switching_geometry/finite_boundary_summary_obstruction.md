# Frozen boundary data do not determine the true first-exit map

## Status

This note gives an exact finite counterexample to one proposed reduction of
the Langton-ant return problem. It does not prove or refute the highway
conjecture. It does not exclude a richer return map that retains chronological
information. Both example boards have only two black cells.

The proposed summary of a finite region records:

1. all colors on its boundary;
2. the frozen routing map from each admissible entrance to its exit;
3. the length of each corresponding frozen boundary path;
4. the lengths and orientations of all closed frozen loops inside;
5. the total number of black cells.

Even this summary does not determine the true ant's next exit.

## 1. Definitions and witness

Use Cartesian coordinates with north increasing y. The true rule turns right
on white, left on black, toggles the current cell, and moves. A **frozen** walk
uses the same turns but does not toggle cells.

Let

    D = {0,1,2,3,4} x {0,1,2,3,4},
    B1 = {(0,1),(1,1)},
    B2 = {(0,1),(1,2)}.

All other cells, including every cell outside D, are white. In both boards,
the only black boundary cell of D is (0,1). Both complete black sets have
cardinality two.

Work in the sector in which even-checker cells receive vertical arrivals
and odd-checker cells receive horizontal arrivals. The entrance of interest
is (0,1), heading east, having just entered from (-1,1).

## 2. The complete frozen summaries agree

The following table lists every admissible entrance and its frozen exit.
The results and lengths are identical for B1 and B2. Length counts updates
inside D before the first move outside D.

| Entrance cell | Heading | Exit cell | Heading | Length |
|---|---|---|---|---:|
| (0,0) | N | (1,-1) | S | 2 |
| (0,1) | E | (-1,0) | W | 10 |
| (0,3) | E | (-1,2) | W | 2 |
| (0,4) | S | (-1,4) | W | 1 |
| (2,0) | N | (3,-1) | S | 2 |
| (2,4) | S | (1,5) | N | 2 |
| (4,0) | N | (5,0) | E | 1 |
| (4,1) | W | (5,2) | E | 2 |
| (4,3) | W | (5,4) | E | 2 |
| (4,4) | S | (3,5) | N | 2 |

Each board also has six closed frozen loops inside D, each of length four.
They all turn right at every step. A four-step grid loop must use four equal
turns; an all-left loop would need four black cells, whereas each board has
only two. Thus their orientations agree as well.

The ten boundary paths use 26 admissible directed states; the six loops use
the other 24. These account for all 50 admissible directed states in D.

## 3. The true first exits differ

Start at (0,1), heading east.

| Board | True first exit | Heading | Updates |
|---|---|---|---:|
| B1 | (1,5) | N | 35 |
| B2 | (-1,4) | W | 18 |

The exact true turn words are

    B1: LRRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLR
    B2: LRLRRRRLRRRRLLLLRL

All positions before the last move stay inside D. Thus the different endpoints
are first exits, not merely different later observations.

The literal verifier `verify_fixed_boundary.py` checks the full frozen
summaries, equal boundary colors, equal initial masses, true words, lengths,
and first exits. Its retained result is `verify_fixed_boundary.json`.
The exact witness data are also in `fixed_boundary_counterexample.json`.

An earlier manual message counted the first displayed word as 34 updates.
The literal verifier caught that transcription error. The correct length is
35; the word and exit were unchanged.

## 4. What information was lost

The frozen entrance path from (0,1),E has length ten in both boards. In B1 it
visits (1,1) twice; in B2 the corresponding repeated internal cell is (1,2).
Those repetitions occur in different positions along the ordered path.

With frozen colors, the detours reconnect to the same boundary output. The
true ant toggles the physical cells. Its later visit therefore reads a color
changed by the earlier visit, and the chronological splicing differs.

A complete return description must retain enough information about repeated
physical switch identities and their order to reproduce these changes.
Boundary connectivity, boundary colors, path lengths, loop lengths, loop
orientations, and total mass do not retain that information.

This counterexample uses the ordinary fixed sector throughout. No physical
grid edge is traversed against its allowed direction. The no-retracing
constraint does not make this summary sufficient.

## 5. Exact scope of the obstruction

The example disproves a universal first-exit rule based only on the listed
summary. It applies to a finite domain. It does not by itself disprove a
specialized summary for the exterior of a core along a more restricted class
of reachable states, nor does it rule out a summary that includes ordered
switch-incidence data.

For the global finite-support problem, the unresolved step is to control
that richer data as excursions write into new white territory and later
return. It can contain growing paths and many repeated-switch incidences.
No bound on that complexity, and no well-founded progress rule for its
successive core returns, was established here.

Even a finite list of boundary exit types would not by itself prove
transience: a repeated boundary type could still conceal longer exterior
excursions. A valid reduction must also control those lengths and the retained
, or prove a mechanism that eventually prevents another core
return.

No general transience, bounded-retreat, finite-end, or strip theorem follows
from this finite counterexample.
