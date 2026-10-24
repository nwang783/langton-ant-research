# An eight-pass controlled builder target

Status: proposed interface architecture,22October2026. The fixed same-phase cap contract is now EXCLUDED at EVERY cap height by the independently audited isolated row11 charge in eight_pass_phase_obstruction.md. A replacement cap-state cycle needs period divisible by4. Such a cycle still needs endpoint XOR span at least19 by the separately audited mirrored-builder hull bound. No periodic controller is constructed. The stable bulk identities
are checked, but NO left cap, right cap, renewable builder or counterexample has
been constructed. This is not the withdrawn white-input-front claim.

## Existing hardware and the eight bulk passes

Let the two-column-periodic hardware I have solid black rows0 and9, odd-x black
cells in rows1 and2, and all other rows white. Its even/odd column masks are
(513,519). Each column has alternating vertical black charge0, appropriate to a
completed RIGHT EXCURSION returning left, not to a one-way white-input front.

Use A=LRLLRRRRLLRL, B=RRRLLLLRLLLLRLLLLRRRRLRRRRLR,
S=RLLR and W=LLRLRRRRLRRRRLLLLRLL. The stable passes are:

1. A east: solid row0 moves to3; catalyst rows1,2 restore.
2. S west: solid row9 moves to8.
3. B east: solid row3 moves to0; catalyst rows1,2 restore.
4. W west: solid row8 moves to11 through white rows9,10.
5. A east: solid row0 moves to3 again.
6. S west: solid row11 moves to10.
7. B east: solid row3 moves to0 again.
8. S west: solid row10 moves to9.

Thus the complete infinite-periodic bulk profile returns to I. The low-band
passes use only rows0..3; the upper return passes use only rows8..11. This
separation avoids the interference that ruins the analogous shorter vertical
cycle. The bulk read height is12, beyond the known height-nine pristine barrier.

## Exact port convention

Let L be a fixed positive even integer giving room for a left cap, and let
R=L+2n. All ports below have sector1. The east passes start at(L,0,E) for A
and(L,2,E) for B, ending at the corresponding R ports. Return passes begin:

    S1: (R,8,W), ending(L,8,W),
    W:  (R,8,E), ending(L,8,E),
    S3: (R,10,W), ending(L,10,W),
    S4: (R-1,9,W), ending(L-1,9,W).

Each pass repeats its word n times. The one-column shift for S4 is essential
for sector compatibility. Stable bulk guards do not determine finite endpoint
bits; every one of those interface cells must be supplied by the caps.

The desired complete controlled excursion starts at(0,2,E) and exits first at
(-1,1,W). Five left-cap segments connect this entry, the four return ports, the
next east-pass ports, and the final exit. Four right-cap segments connect each
east endpoint to the next return start. All cap histories must be physically
legal on the SAME changing board, and the left cap must restore after the full
excursion. They cannot be certified independently while forgetting earlier flips.

## Regeneration contract to synthesize

Seek a finite family C_n consisting of a fixed left cap, n hardware tiles I,
and a translated fixed right cap, with exact controlled return map

    (C_n,(0,2,E)) -> (C_(n+3),(-1,1,W)).

The six-column growth is not arbitrary. The entry/exit row charge increments
are +1 modulo4 on rows1 and2 and zero on every other row. Adding three I tiles
contributes -3=+1 modulo4 on those catalyst rows, while each solid-row increment
has zero alternating sum. New columns have charge0, and the black mass grows
by18, congruent to2 modulo4 as required for E-to-W total turning. These are
necessary checks only. A two-column increment would fail the row-charge test.

All eight bulk passes have zero mass excess. Therefore the combined cap history
must create18 net black cells. Its total bulk duration is112n. A constant cap
word length would give an affine counted return word, suitable for the exact
ordered-event or incidence-arrangement certificate once a candidate exists.

## Why this would matter, and what remains missing

If the contract held for all sufficiently large n, initialize the right half
with C_n and the left half with its half-turn under

    T(x,y)=(-1-x,3-y).

The ports match exactly. Alternating right and left excursions would grow both
axial endpoints and return to(0,2,E) after every pair. This would be an autonomous
finite-seed orbit with no translating periodic tail. Both endpoints grow, so it
does not satisfy the one-sided-CPU or single-moving-window exclusion contracts.
The external reset is NOT claimed physical before this full gluing is proved.

At present only the eight stable bulk transformations and necessary port/charge
constraints are available. The fixed cap equations, complete-field restoration,
new-hardware creation and no-interference obligations remain entirely open.

## Audited hull obstruction discovered after the bulk check

The computability analysis's mirrored-builder span theorem, independently signed
by the auditor, imposes an additional necessary condition. For fixed ports
r=2,s=1, the gluing half-turn has vertical center S/2=3/2. Suppose the COMPLETE
net advancing-right-end XOR is confined to a bounded-width window with vertical
span H, while the left fringe and old bulk restore. The two mirrored end
patches are the only net changes of a closed paired excursion. At every fixed
central column their convex hull converges to the vertical interval
[S/2-H/2,S/2+H/2]. The finite closed-history hull theorem confines every read
to that hull. Since the W20 arm reads a fixed mature bulk cell on row11 in
every sufficiently large pair, H>=19 is necessary.

Consequently caps and their complete XOR confined to rows0..11 cannot work.
This is a new scoped obstruction, not a failure of the eight bulk identities.
A prospective cap with net XOR spanning, for example, rows-9..11 has H=20 and
is not rejected by this necessary inequality. Any lower bits must genuinely
move with the cap: stationary unused spectators do not enlarge the net XOR.
No assertion of existence is made at H=19, H=20, or any other height.

## Stronger later obstruction: same-phase caps fail at every height

See `eight_pass_phase_obstruction.md`. The complete right-end row11 charge
changes by-1 modulo4 per eight-pass excursion. Every right-cap segment has
endpoint poses below row11, so changing its height does not alter this modular
restriction. Same-phase even-translated caps are impossible at all heights.
The prospective taller SAME-CAP suggestion in the preceding section is therefore
superseded. A four-phase (or multiple-of-four-phase) cap controller is not
excluded; it would require genuinely changing cap and left-fringe states.
