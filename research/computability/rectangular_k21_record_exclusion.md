# Controller-free exclusion of rectangular inflation (k,a,b)=(21,3,7)

2026-10-23 00:35 UTC. Status: all315 local tree nodes and the full analytic
eventual-affine proof independently signed at00:36 UTC. No finite-controller
or uniform-image assumption is used.

## Statement and record geometry

There is no finite-support actual ant with, for every sufficiently large n,

    p(21n+c)=sigma*diag(3,7)p(n)+d,

where c is an integer, d a lattice vector, and sigma is+1 or-1. Coordinate
rotations cover the swapped diagonal. The signed affine comparison and
existence of arbitrarily high records are exactly as in Section5 of
`rectangular_k33_record_exclusion.md`, with21,3,7 in place of33,3,11.

At a sufficiently high coarse north record, its predecessor fine macro has
displacement(0,7), length21, and direction counts N9,S2,E5,W5. Before that
macro starts, the row one below its endpoint and everything above it are
pristine: k=4*5+1 and7-5-1=1 in the signed fresh-band calculation.

## Only two possible ending histories

From the first hit of that pristine row until the first hit of the endpoint
row, the one-row climb spends either1 or2 south moves. The audited complete
crossing catalogs show its word is respectively

    F=RRRRLR,             G=RRRLLLLRLR.

If it is G, every south move is spent. No further vertical motion can return
to the endpoint row; a single extra horizontal move is impossible because
the21-step vertical macro must have vertical last movement. Thus it ends G.

If it is F, at most one south move remains. Any nonempty same-height suffix
must have equal positive counts of north and south, hence exactly one each.
Axes alternate, and both suffix entry and macro exit have vertical incoming
axes, so the suffix has exactly4 moves. But F's first four continuation
turns are forced R,R,R,L: the three initially white reads at the endpoint,
its east neighbor and F's now-white entry are followed by F's black western
cell. Their movements are east,south,west,south, spending TWO south moves.
This is impossible. Hence this case ends exactly F as well.

## No required next macro

The high coarse north record reads R, so its next macro must move east by3
in21 steps. Both possible preceding tails end facing north, and therefore
the next macro must have exact direction counts

    (N,E,S,W)=(5,7,5,4).

Normalize the F or G entry to(0,0,N). Replay the tail on the initially white
upper half-plane, assign any needed lower colors, and retain only the cells
read by that tail. All other cells below0 are allowed arbitrary colors;
unread cells on or above0 remain white. This relaxes every earlier constraint.

`check_k21_fresh_tails.py` explores the entire finite continuation tree under
those conditions, branching only on initially unknown lower colors and
stopping a branch when it would exceed one required direction count. The
F tree has166 nodes and the G tree149. Neither has a21-read continuation.
The full trees and the forced four-read post-F test are saved in the matching
JSON file. Thus neither possible predecessor can lead to the required next
macro, proving the exclusion.

This is stronger than the separate exhaustive length21 half-turn image scan.
It still does not exclude arbitrary finite-seed nonperiodic paths, arbitrary
directive limits without an inflation identity, or other rectangular scales.

Independent audit artifact: `../audits/k21_fresh_tails_independent.json`.
The auditor regenerated the whole tree with immutable boards and complex
headings and separately reviewed the forced post-F suffix and affine records.
