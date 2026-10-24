# Exact one-shot reflection by a perpendicular mature104 wake

23 October2026,07:52 UTC. Independently signed KU all-parameter/all-future
certificate, including the fixed322-cell trimming. This is a useful physical routing component, NOT
an unchanged reusable mirror, autonomous assembly, or counterexample.

## Precisely specified finite initial boards

 R denotes a physical counterclockwise quarter rotation here,
not an ant turn letter. For integers n,m>=30:

1. Translate R^2 S to(-2n,-2n), with incoming E, and execute H exactly2n times.
   Call the resulting COMPLETE finite black board Old_n. Its head would be
   at(2n,2n,E); that head is NOT part of the new initial state. This definition
   constructs a finite mature NE-directed wake, including BOTH endpoint fringes.
2. Add the disjoint thirteen-cell seed R S translated to(-2m+1,2m).
3. The actual single ant starts at(-2m+1,2m,S), on the union of these two boards.
   The initial mass is24n+26. No infinite background or external reset is used
   DURING the claimed trajectory; this is a specified finite initial seed.

The old generator and the actual starting ant have the SAME invariant pose
sector1. Thus the local mechanism is not the opposite-sector reverse trick.
Nevertheless no actual path preparing Old_n and placing the head at the new
start has been constructed or assumed.

## Exact routing statement

The actual turn word from that finite state is

    H^(m-10) C H^infinity,

where C is the fixed19,872-turn word in `highway_wake_reflector_collision.json`.
The incoming prefix ends at(-19,20,S), independently of n,m. C ends at
(-31,-10,N). Hence the final canonical104 tail starts at

    time104m+18,832, pose(-31,-10,N), drift(-2,+2).

The incoming drift is(+2,-2), so this is reflection into the opposite diagonal
direction, not a quarter turn. The line x+y changes from1 to-41, a transverse
shift of-42. The old wake lies in the perpendicular NE direction. Parameter
thresholds30 are sufficient, not claimed minimal.

## Full collision ownership, including damage to the reflector

C reads exactly2,416 distinct cells, inside the fixed box[-42,26]×[-38,27].
Its complete XOR has1,260 cells, ALL explicitly listed in the frozen JSON.
Of these,1,099 cells become black and161 become white, so C adds938 black cells.
The final mass at the tail start is24n+12m+844.

In particular152 old black wake cells are erased. Inside the old wake's complete
black strip -7<=x-y<=3, there are298 changed cells. None of these changes is
silently discarded. The parametric whole-board postcondition is

    Entry_(n,m) symmetric_difference X_C,

where Entry_(n,m) is the exact old-plus-incoming-prefix board, and X_C is the
fixed1,260-cell XOR. Both full Presburger relations are recorded in the
certificate, including remote untouched seeds, mature wake, and approach trail.

The old reflection guard is NOT restored. The first changed old-strip input
site encountered in a replay of C is(-1,5), at collision read671 (zero-based).
It is required initially black and is white after the collision. The same
C guard therefore cannot simply be reused, even if its incoming approach pose
were supplied again. This is a narrow concrete guard failure, not a ban on
repair, different phases, or a fresh translated unused part of a longer wake.
No compound mirror, recurring memory element, or renewable route is claimed.

## Exact verification, not sampled highway detection

`certify_highway_wake_reflector.py` constructs Old_n by XORing all104 affine
read stripes of H^(2n) into its translated seed. It similarly constructs the
incoming prefix parity. Exact set comparisons prove the old wake misses every
incoming-prefix read for ALL n,m>=30, so the retained standard104 certificate
supplies that entire prefix. The two input seeds are exactly disjoint.

The fixed C is retraced geometrically, every same-cell turn alternation checked,
and its complete first-L/first-R guard is compared against the parametric entry
board. Its full XOR is then applied. Finally all104 infinite-tail slot families
are checked against that COMPLETE resulting board, with every earlier same-cell
read XORed in. There are262 nonempty prior tail relations and no bad color set.
Tail repetitions are unbounded integer variables, not a finite horizon.

The152 erased old cells and298 changed strip cells are themselves checked as
constant sets for all n,m, not merely counted in a sample. Resource errors are
failures, never accepted empty sets. Source and word hashes are in the JSON.

Eight translation phases of a perpendicular wake were finite discovery controls.
Only the stated same-sector reflecting phase is promoted to an exact family.
The other phases' observed routing is not an audited classification theorem.

## Exact trimming to a fixed finite scatterer (separate addendum)

`extract_highway_wake_mirror.py` intersects the entire future read set (the
fixed C plus every future104 read) with Old_n. The result is exactly one
CONSTANT set of322 black cells, independent of n,m>=30, lying in
[-38,19]×[-36,24]. Every other old-wake cell is never read by the claimed
trajectory, including its prefix. Deleting precisely those irrelevant cells
therefore changes no turn at any time.

Consequently the same reflection can be realized by a fixed322-cell scatterer
plus the disjoint thirteen-cell incoming standard seed, for EVERY m>=30.
Total initial mass is335, independent of the approach distance. The complete
postcollision mass is12m+1153, and the full parametric postcondition is recorded
in `highway_wake_mirror_minimal.json`. The word, pose, tail and1,260-cell XOR
are unchanged. The constant322 set is minimal among SUBSETS OF THIS old wake
for preserving this prescribed trajectory, not claimed minimal among arbitrary
reflectors or all possible routing words.

The truncation proof is a precise read-set ownership argument, not a heuristic
cropping of a long simulation. It does not improve guard renewal: the152 erased
old black cells and other permanent changes remain. A fresh incoming interface,
repair mechanism, and placement by the same continuing ant are still absent.
