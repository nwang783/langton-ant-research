# A fixed-band obstruction to passive tangential-wake recycling

Status: author checked; submitted for independent audit. The finite-seed standard104 conjecture remains unsolved.

## Result

Consider the exact blank-collision model with its standard104 absorbing certificate. Let p be the head at a nonterminal event boundary, let x be that event's selected first old black input, and retain the complete old field. For every head/read position q in the completed macro, including the actual L successor, and every coordinate normal n,

    n·q <= max(n·p, n·x) + 29.

For every diagonal normal n in {(1,1),(1,-1),(-1,1),(-1,-1)}, the same statement holds with 48. Applying this to -n supplies the lower bound. Every newly emitted black cell satisfies the same bound. No claim bounds the old unread field, which is retained without alteration.

Consequently, fix a tangential input band L <= n·x <= U. If the initial head is in [L-1,U+1] and every selected input in a sequence of completed nonterminal macros stays in this band, the entire head path during these macros stays in [L-30,U+30] for axis n, or [L-49,U+49] for diagonal n. The band may be arbitrarily long tangentially and contain arbitrary, repeatedly generated material. No bound on its black mass, diameter, number of events, or input waiting times is assumed.

This rules out a precise passive architecture: an arbitrarily long tangential standard wake, with endpoint caps of uniformly bounded normal width, cannot produce unbounded outward record levels if all subsequent consumed old inputs remain in the wake/cap band. A successful growing-shuttle or ladder countercontrol must generate and later consume genuine black lifetimes outside that band. The statement does not rule out such a ladder and is not a pristine-record budget.

## Exact finite geometry

Use the independently certified empty reference from head (0,0), N: prefix C of length 9977, followed by H of length 104 with drift d=(-2,-2). Let A be the maximum n-projection among prefix read positions, and B,b the maximum/minimum among first-period tail read positions. The following complete table is reconstructed from the literal turn words:

| n | A | B | b | n·d | K |
|---|---:|---:|---:|---:|---:|
| (1,0) | 29 | -14 | -19 | -2 | 29 |
| (-1,0) | 19 | 19 | 14 | 2 | 19 |
| (0,1) | 22 | 10 | 2 | -2 | 22 |
| (0,-1) | 22 | -2 | -10 | 2 | 22 |
| (1,1) | 35 | -5 | -15 | -4 | 35 |
| (-1,-1) | 21 | 15 | 5 | 4 | 21 |
| (1,-1) | 48 | -18 | -28 | 0 | 48 |
| (-1,1) | 34 | 28 | 18 | 0 | 34 |

Here K=max(0,A,B) when n·d<=0, and K=max(0,A,B-b) otherwise. These constants are sufficient; no minimality claim is needed. Proper rotations merely permute normals within each class.

## Proof of the macro bound

Translate p to zero and rotate the heading to N. Up to but not including the selected old contact x at time t, the physical path equals the empty reference. This is the exact first-collision induction, not a restricted word cover. The contact position also equals the empty-reference read position at t.

If t is in C, every earlier position has projection at most A <= K. If t is in the tail and n·d<=0, every tail position is at most B, hence every earlier position is at most K. Both cases imply the claimed upper bound with max(0,n·x).

If t is in tail period k and n·d>0, every preceding tail read has the form q_j+l d with l<=k. Writing x=q_i+k d gives n·(q_j+l d-x)<=B-b. Prefix positions are bounded by A. Therefore all reads through t satisfy the stated bound. Every emitted black cell is a previously read cell, so the same bound holds for the entire newly emitted field. The actual L successor differs from x by one unit step, of normal projection at most 1. Since all K>=1 it satisfies the same bound. This proves the statement for arbitrarily long flights, without scanning their length.

After each macro the entry to the next is one step from the previously selected input. Thus input-band membership ensures every event entry lies in [L-1,U+1], which proves the padded-band corollary independently of the event count. Full untouched archives are not deleted to obtain this result.

## Pristine-record interpretation and limitations

At a genuine current pristine record cut q inside a macro but before its collision, the selected input x is still black, and therefore n·x<n·q. If the record level exceeds the macro-entry level by more than K, the bound forces

    n·q-K <= n·x < n·q.

This identifies an old-at-event-entry live input in the preceding K layers. Crucially, it is the input selected for a FUTURE collision, not necessarily an input already consumed by the record cut. No backward-time or injective past-charge conclusion is licensed. If the whole input band is behind the record by more than its padding, such a selected input must be outside that band.

A no-collision event is a certified blank-prefix/standard tail, not a completed nonterminal macro. An exact standard certificate at an event boundary also terminates this research model. Neither should be treated as an infinite supply of bad events. Raw collisions do continue along standard104, so the absorber is essential.

This result tests only the passive-band condition. Fresh template production can violate that condition and move selected inputs outward. The existing 14-cell defect regeneration control shows why simply counting current guard defects is not a substitute for accounting for such production. No monotone fuel, all-seed capture theorem, or mass-only pristine-record budget is asserted.

## Reproduction

Run `python check_collision_normal_span.py`. It physically replays C and one H, checks all finite inequalities proving the all-period geometry, verifies rotation closure, and exercises 20 full-field collision controls including flights near 104 billion moves without expanding them. Dependencies are the independently signed blank-collision and absorbing-model packages. The accompanying manifest binds all local proof artifacts and source hashes.
