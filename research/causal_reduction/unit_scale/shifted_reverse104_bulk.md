# Shifted exact-reverse104 bulk cannot reuse its forward wake

23 October 2026, 08:59 UTC. Independently signed LF exact finite profile addendum.
This concerns only translated copies of the exact time-reversed standard104
sweep. It is not an exclusion of different return words or prepared rails.

Use the retained H with heading E and displacement D=(2,2). A cell orbit
modulo ZD is identified by (x-y,x mod2). Its complete chronological H read
history is obtained by sorting each slot j at p=rep+iD by j-104i.
All22 orbit histories begin R and alternate. Twelve have odd length; their
complete mature wake black profile is

    (-7,0),(-7,1),(-6,1),(-5,1),(-3,0),(-2,0),
    (-1,1),(0,0),(1,0),(2,1),(3,0),(3,1).

The exact reverse word is complement(reverse(H)), with heading W and start
(-1,0), the J transform of the forward checkpoint at0,E. It drifts(-2,-2).
Sorting its slot histories by j+104i gives precisely the twelve displayed
black-input classes, and the other ten read classes must start white.
This verifies the complete bulk precondition, not just the odd toggles.

A translation t=(tx,ty) acts on classes by

    (z,e) -> (z+tx-ty, e+tx mod2).

If even the required BLACK classes are supplied by the same forward wake,
the twelve-element set must map into itself and hence onto itself. Its
finite z-support forces tx=ty. A one-black class, for instance z=-6,
then forces tx even. Therefore the ONLY matching translations are t in ZD.
These all have even coordinate sum and preserve the wrong reversal sector.
Every sector-repairing translation has odd coordinate sum, so it fails.
Changing the cut phase of the reverse sweep merely shifts its start along
the same geometric bulk and does not change this conclusion.

The frozen exact profile also quantifies the missing input. Normalize tx to
0 or1 modulo D. If the transverse shift lies outside[-10,10], all twelve
required black classes are absent. Within that exact overlap range, all
same-sector classes are enumerated in the JSON: at least SEVEN black cells
per period must be added and at least TEN input colors per period must be
changed in total. The total minimum10 is achieved by t=(1,6), with eight
missing blacks and two unwanted blacks. These minima need not occur at the
same translation. Thus a fixed finite cap cannot repair a long bulk segment;
the necessary repairs grow linearly, apart from bounded endpoint effects.

The bi-infinite profiles used here are local limits of long finite wakes,
not allowed infinite initial backgrounds or completed infinite operations.
No physical turnaround cap is inferred. The separate concrete experiment
in same_sector_wake_return_n30.json places a W-heading ant at the mature E
front's position, not at the J-reversed position. It captures NE after9701
steps, by an exact complete-board periodic-tail check; this one sample is
not used in the profile theorem.

Artifacts: check_shifted_reverse104_bulk.py, shifted_reverse104_bulk.json.
