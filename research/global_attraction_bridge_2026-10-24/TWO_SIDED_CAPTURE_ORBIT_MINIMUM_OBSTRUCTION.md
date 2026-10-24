# A two-sided capturing orbit never enters the at-most-two-input class

24 October 2026. AUTHOR exact construction and all-future proof. Independent audit requested. This is a countercontrol to one proposed reversible mass-minimum reduction, not a counterexample to highway attraction.

## 1. Falsifiable mechanism and result

A reversible finite-support orbit has an attained minimum of its nonnegative integer full black mass over all integer times. One might hope that, after discarding black cells never read in EITHER time direction, some cut has at most two black cells; the signed all-position two-black theorem would then handle the whole forward orbit.

That mechanism is FALSE. The ordinary four-cell port

    G={(0,-1),(1,1),(1,3),(2,2)}, head(0,0), heading E,

has an exact two-sided finite-support orbit with all of these properties:

1. Its forward future is canonical104, as already certified.
2. Its reverse-conjugate future is also canonical104, certified below from cut1040.
3. The minimum FULL black mass over ALL integer times is EXACTLY4, attained only at original times0 and2.
4. At every integer cut there is NO currently black cell whose physical site is never read in both time directions. Two-sided deletion therefore removes nothing.
5. Even the ENTIRE forward-relevant population C*(t) has minimum EXACTLY4 over ALL integer times, again attained only at0 and2.

Thus neither moving backward to a mass minimum, deleting bidirectionally unread black archive, nor waiting for a <=2 whole-future-relevant cohort can connect this orbit to the signed at-most-two-black class. The orbit is nevertheless capturing. This does not exclude larger-class arguments, other potentials, or the exact canonical basin parametrization.

## 2. Exact time-reversal conjugacy with the actual cursor

Let F be the physical ant update and v_h the unit vector in its incoming heading. Define the edge-reversal involution

    R(B,p,h)=(B,p-v_h,h+2).

Then R squared is the identity, and

    F inverse = R F R.

To verify the latter, put r=p-v_h. If r is black in the post-update field, the inverse must flip it white and use previous heading h-1; if it is white, the inverse flips it black and uses heading h+1. Applying R,F,R gives exactly these two cases.

R changes the pose invariant (p_x+p_y+h) modulo2. It is therefore not a physical detour, routing operation, same-sector time reversal, or an edit allowed during the actual forward history. It is used only to CERTIFY the unique mathematical negative-time orbit with the correct transformed cursor.

For X0=(G,(0,0),E), the reverse-conjugate initial state is

    R X0=(G,(-1,0),W).

If Y_n=F^n(R X0), then the original negative state is X_{-n}=R Y_n. The complete black fields are equal; the actual poses are related by R, not by simply reversing the word at the same pose.

## 3. Complete certificates at both ends

The checker replays the full390-read forward G prefix. Its terminal word is cyclic canonical H, with drift(2,2), and exact infinite phase-ray parity checks use the COMPLETE terminal black field. Its finite black-mass minimum is4, only at cuts0 and2.

It separately replays1040 physical updates from R X0. The complete terminal reverse-conjugate state has

    head(13,-16), E, full black mass150,

and passes a canonical104 infinite certificate with drift(2,-2). The actual original negative endpoint is therefore

    time -1040: head(12,-16), W, the same full150-cell field.

A fresh actual FORWARD replay of1040 updates from that negative endpoint reproduces the original G field and pose. At each intervening cut, both the complete field and edge-reversed pose match the independently stored reverse-conjugate state. The forward word equals the reverse-order complement of the reverse-conjugate word, as required by the physical flips; it is not silently identified with that word.

For each certified tail, the exact mass increment over104 updates is12. Let delta_i be the signed R-minus-L count in its first i updates. At epoch k and phase i, its full mass is

    endpoint_mass + 12*k + delta_i.

The finite104-phase minimum is strictly greater than4 for both endpoints. Therefore later epochs in either certified time direction can never reach mass4. The complete finite replays supply all remaining times. This proves the exact all-integer minimum and its only two attaining cuts without a numerical horizon assumption.

## 4. No bidirectionally unread black archive exists

All four initial G inputs are genuinely consumed in the ordinary future, at reads1,22,32,58.

Take any negative cut t<=0 and a currently black cell q. If it changes before time0, its first such change is an actual read consuming that current black lifetime. If it does not change, it remains one of the four black G cells at time0, and is consumed later. Hence

    C*(t)=B_t for EVERY t<=0.

In particular, no negative-cut black cell is unread in both directions.

For a positive cut, any current black lifetime either descends from one of the original four inputs, all of which have a future consumption, or was born at an actual R read at some earlier nonnegative time. In the latter case its physical cell is already read in the past, even if this new black lifetime is permanent in the future. Thus again no currently black physical site is unread in both directions. Removing any current black cell therefore changes at least one half of the actual two-sided trajectory.

This is a statement about actual reads in this one orbit. It does not pretend that future permanence forbids a historical birth, or discard black output merely because it is irrelevant to the positive-time future.

## 5. Stronger whole-future-relevant minimum

For t<=0, Section4 gives C*(t)=B_t, already bounded below by4.

For0<=t<=390, the checker records genuine lifetime identities and all their future fates, including terminal lifetimes whose first consumption lies on the certified infinite ray tail. The resulting ENTIRE relevance profile has minimum4, attained only at0 and2.

At the terminal positive tail, the checker obtains all104 exact pruned phase fields from complete full-board ray certificates. Their sizes range from11 to22. After104 updates the exact pruning is the original pruning translated by the actual drift. Equivalently, first-future-read colors determine the same periodic pruning directly from the already certified infinite word. Hence these phase sizes hold at every later epoch.

The global all-integer lower bound |C*(t)|>=4 is therefore exact. This gives a concrete limitation of the newly total Prune2 interface: running it at every cut of this captured orbit always returns the at-least-three-original-input branch. Its totality is useful, but eventual success of its exact-small-pruning branch is not a universal capture mechanism.

## 6. Scope and provenance

The G forward port and its one-sided property are retained results. The new finite leaf is its fully certified reverse-conjugate continuation, followed by the two-ended minimum and no-bidirectional-pruning argument. The data and checker retain all extra output and the true cursor sector.

No negative answer to the finite-seed highway conjecture, noncanonical translating controller, undecidability claim, universal mass bound, or bound on the number of inverse ancestry steps follows.
