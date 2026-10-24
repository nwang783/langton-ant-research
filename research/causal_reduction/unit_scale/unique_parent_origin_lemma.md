# A unique physical parent occurrence stays at the origin

23 October 2026, 05:23 UTC. Independently signed analytic lemma at 05:27 UTC.

Let W be an internally ant-legal finite image of one physical heading/turn
state s. It has the parent's unit displacement, incoming heading and final
heading. Its signed turn charge is NOT restricted.

If W contains the physical state s exactly once, that occurrence is read at
the origin of the image.

## Proof

Normalize the parent to N-R. The final displacement and final heading are
both E, so the final move is from the origin to E. Consequently the last read
is at the origin. The first read is also at the origin.

The exact geometric incidence identity in
`computability/finite_power_exact_validator/unit_transport_incidence.md`
says that, after subtracting the coarse parent, opposite-heading copies of
each same-turn/axis class have equal counts. In particular

    count(N-R)-1 = count(S-R).

If N-R occurs exactly once, S-R never occurs. Every read of the origin has a
vertical incoming heading, by checkerboard axis parity. Therefore every R
read at the origin must be the unique N-R occurrence.

For length one the conclusion is immediate. For a longer image, the first
and last reads are distinct occurrences of the origin. Internal ant legality
makes its successive turns alternate, so among those reads at least one is
R. That R is the unique N-R occurrence, proving its position is the origin.

Rotations cover the other R parents. For an L parent, the same argument uses
count(parent)-1=count(opposite-heading L), and alternation forces an L at the
origin. Equivalently this follows by the corresponding incidence equation;
no reflection symmetry of the ant is assumed.

## Immediate terminal-singleton consequence

For a fixed physical-state controller, suppose an active state s has one
self occurrence and every other state in its image is an identity state.
Then its image is U s V with that self occurrence at offset zero. Both U and
V have zero displacement and preserve their respective entering headings.
Their letters are fixed by substitution. Thus

    phi^r(s) = U^r s V^r.

At least one of U,V is nonempty because s is active. These arbitrarily long
blocks stay in one fixed finite footprint. They cannot all be internally
ant-legal, by the standard finite-domain escape/strict clock theorem, which
applies on any initial coloring. This does not assert anything about a
unique DECORATED parent: another decoration of the same physical state may
provide the origin read, so that extension would be invalid.
