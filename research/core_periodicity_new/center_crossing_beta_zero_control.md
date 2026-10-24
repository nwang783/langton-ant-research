# An actual center crossing with no incidence-rank increase

23 October 2026, 14:06 UTC. This finite positive control prevents an unsupported
strengthening of the atomic center-turning theorem. Independent reconstruction
is requested. No path generation or capped search is part of this certificate.

## Literal control

Start the ant at (0, 0, N) with exactly these ten black cells:

    (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, -1),
    (0, 0), (0, 1), (0, 2), (1, -1), (1, 0).

It executes the five complete retained packets

    DC, DC, DC, D, V,

with their actual next marker. The raw length is 103, the raw-plus-marker
length is 114, and the raw endpoint is (2, -1, E). There are three C atoms.
The direct simulator verifies every microscopic turn from this explicit board.
At every full packet boundary, a second ordered-residual replay verifies that
the physical black set is exactly the transformed core plus the current
residual identities.

## Proper auxiliary center crossing

Use the corrected center p + rot_h(-1/2, -1/2), as in the signed turning note.
The first D-base chord, inside the first DC, runs from (-1/2, -1/2) to (1/2, 1/2).
The final V chord runs from (-3/2, 1/2) to (3/2, -1/2). They meet at (0, 0),
strictly inside both chords, with parameter 1/2 on each. Their cross product
is -4, so the contact is a proper transverse crossing rather than a touch,
overlap or shared endpoint. These atoms are nonadjacent.

Thus actual center-chord planarity is false, even for a short complete factor.
This is not a full-pose return, and it does not invalidate the signed theorem
that every actual closed center polygon must self-contact.

## The crossing does not increase all-input beta

Initialize the all-input incidence graph with one distinct component per
entry residual identity, excluding the five-cell core. For each packet, join
all components of its consumed residual inputs and attach all fresh outputs.
The packet's beta increment is its input count minus the number of distinct
input components. Every increment in this control is zero.

The final V consumes (2, 0), a surviving output of the first DC, together with
the entry residual at (1, -1). Their components are still distinct, so this V
merges two components rather than reconverging inside one component. There is
exactly one component merger and no beta increase in the whole control.

Consequently neither a proper center crossing nor the first such crossing can
automatically be charged to positive incidence rank. A possible stronger
charge to beta increase OR component merger is not proved here. Nor would a
per-crossing count automatically give a finite budget: one packet may create
several crossings, and old geometry can be crossed repeatedly.

## Exact limitation

This is a finite, funded factor-entry control, not a closed excursion, not a
renewable mechanism, and not an unfunded V1 or U1 example. It does not settle
whether a closed excursion's compulsory crossing must carry some stronger
chronological obstruction. It identifies precisely why auxiliary planarity
and a simple crossing-to-beta charge are insufficient.

Working files: check_center_crossing_beta_zero_control.py and
chronology_dcuv/center_crossing_beta_zero_control.json.
