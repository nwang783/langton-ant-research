# Exact1564 standard-writer selector and noncrossing routing boundary

## Finite complete-profile result

The fixed1564 wave requires one initial color on each of its557 full
(14,14) read classes. On mapping these requirements to old-d classes
(t=x-y,a=x mod2), they are consistent and constrain167 classes:
60 black and107 white. Only three of the170 possible parity classes in
the full read band[-54,30] are unconstrained.

Consider parallel standard104 WRITERS only: an actual clean SW or NE
standard leg whose settled wake is left untouched in one common bulk.
Each writer contributes its complete12-black-class profile. Both drift
orientations are included, not a time-reversed inverse104. In a common
physical sector its possible transverse translations are even delta and
its parity shift is either a=0 or1. Cyclic phase shifts change its front
but not the full settled profile.

Enumerate every such complete writer profile whose hull intersects
[-54,30]. Reject it if ANY of its twelve black classes is required white.
The result is EXACTLY FIVE profiles:

    SW [-40,-30], parity shift0;
    SW [-28,-18], parity shift0;
    SW [-16, -6], parity shift1;
    SW [ -2,  8], parity shift0;
    NE [ 14, 24], parity shift1.

Here SW parity shifts refer to canonical forward mask, and NE to its
proper180-degree rotation; exact masks are stored in the selector JSON.
Each contributes a different set of exactly12 required black classes.
They uniquely cover all60 required blacks. There is NO neutral standard
writer with support in an internal unread-profile gap. Thus there is no
alternative useful orientation or placement hidden by the earlier bulk
count. Any additional neutral parallel writer must lie WHOLLY outside
[-54,30], not between these five active writers.

The finite enumeration is exhaustive: each standard mask occupies both
extreme levels of its eleven-level hull, so a mask meeting the wave range
has delta between explicit extrema. Those bounds, both orientations,
both parity shifts and all even deltas are checked. The stronger
common-untouched-bulk hypothesis makes distinct writers' eleven-level
read strips disjoint by the signed packing lemma. Arbitrary intervening
bulk edits or overlapping nonstandard wake cancellations are outside this
selector statement. Perpendicular standard writers intersect future
(14,14) read rays only finitely many times and cannot replace any positive-
density parallel input profile; finite effects belong in the cap.

Code/data: `select_1564_standard_writers.py/json`.

## Minimal exterior helpers with fixed original endpoints

A full seven-leg snake with these fourSW/oneNE active writers needs two
additionalNE return legs to have net oneSW strand. Both helpers must be
exterior. Their three order types are: both below, one on either side, or
both above the active profiles. Exact noncrossing opposite-orientation
port matchings at both caps were enumerated for all three cases.

Keep the inherited-history endpoints: oldside start is SW[-28,-18] and
remote finish is SW[-16,-6]. In EACH helper-placement case each cap has
one noncrossing local matching, but joining the two matchings leaves
closed components rather than one path visiting all seven writers.
There is no connected seven-leg disjoint-support preparation with these
fixed endpoint roles. This is a finite minimal-helper result; arbitrary
numbers of additional exterior writer pairs were NOT classified.

## A real noncrossing escape if endpoint roles change

Profile uniqueness is NOT a global topological impossibility theorem.
Take exteriorNE strips[-72,-62] and[42,52]. Change the oldside start to
SW[-40,-30] and the remote finish to SW[-2,8]. There IS a noncrossing
seven-leg ordering:

    SW[-40], NE[-72], SW[-28], NE[42], SW[-16], NE[14], SW[-2].

The JSON records both cap matchings exactly. All arcs can be loop-erased
within their disjoint supports to give this geometric snake. This is
only a topological witness, not an ant trajectory or a cap construction.
In particular the finalSW writer would still have to launch the correct
wave kernel, with strict-past ownership and every earlier rail retained.

## The immediate final-writer join is NOT fresh

At the fixed wave seed pose(-6,-6), north, the finalSW[-2,8] profile has
exactly four matching canonical H phases:11,19,23,39, at the longitudinal
copies specified in `wave_join_from_last_writer.json`. For each, form its
TRUE strict-past standard field and keep the other four whole black
bands. Infer the exact finite XOR needed on every future1564 read ray
and every eligibility boundary.

The four required masks have respectively7,6,7,8 cells. They require
5,4,6,3 erasures respectively, and7,6,7,3 strict-past read overlaps.
Consequently NONE is an additions-only fresh cap at this prescribed cut.
The simple two-toggle full-band normal form is not a preplaced passive
cap on a genuine incomingSW front. A verified finite scattering prelude
could still prepare it; it is not excluded by this direct-join test.

These results close the finite profile selector and identify exact
remaining geometric/causal obligations. They establish neither bounded-
original-mass preparation nor impossibility of such preparation.
