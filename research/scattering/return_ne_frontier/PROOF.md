# The return-NE retained-core band: exact cap transfer and fourteen exclusions

Status: the exact local checkers and fifteen independent finite-seed controls pass. Independent analytic review is requested. Eight matching-exceptional classes remain open in this package.

## Setting and scope

Use u=x-y,z=x+y. Let q_n=(-2n-33,-2n-14), and let Q_r be the phase-r read of canonical W from the origin heading east, so its drift is NE=(2,2). The retained bit is

    s_m=(6-2m,-43-2m)+Q_r,
    m>=100, n-m>=100.

The already audited far_sw_core interface covers all22 fresh phases. It keeps the complete q_n history and compares it with an incoming mature NE front plus a bilateral old SW rail. In source coordinates obtained by counterclockwise rotation, the latter is the previously audited NW-plus-SE-rail model. The comparison strip is the entire |z-z(O_m)|<=200, not a finite window.

Thirteen model futures remain in that strip. Four other classes13,14,27,89 rejoin the complete original trajectory up to a protected finite scar. This package supplies the missing complete two-cell capture for the other five classes28,60,61,70,75 and derives fourteen retained-core recurrence exclusions. It does not claim all22 recurrence exclusions.

## Complete old-field decomposition

Write E for the exact702-cell blank residual at time9977, after removing the canonical SW core at O0=(-15,10). Its support satisfies -21<=z<=35 and -34<=u<=48.

After the first n+8 SW periods and the exact51118-turn exceptional q_n recovery, remove both its incoming and outgoing canonical cores. The resulting complete finite packet is G_n=G0+(-2n,-2n), with z(G0)<=7. The checker computes G0 by XOR from the actual word, initial q cell, and both cores, rather than replacing it with only its fresh writes.

At the retained-core epoch O_m=(6-2m,-43-2m), the actual full field is

    E XOR old_SW_deposits[0..n+7] XOR G_n
      XOR incoming_NE_core(O_m)
      XOR incoming_NE_deposits[1..n-m].

The ideal local model instead has the full bilateral old SW rail and the entire incoming NE past. Thus their exact difference consists of E, the two omitted old-SW half-rays, G_n, and incoming NE deposits at indices>=n-m+1. No old component is erased.

The old SW rail lies in -28<=u<=-18. The five local recoveries and their subsequent NE flights all have u>-18. Every G_n cell has z<=-4n+7; every omitted incoming deposit has z<=-4n-32. Since n-m>=100, both lie strictly below every post-core model read. Finally the local recoveries lie below z=-21, and their NE approach remains below that level until the selected fixed cap pose. These exact bounds transfer the local model through the complete approach, including after it exits the original strip.

## A reusable full-half-plane cap interface

At each chosen cap pose, the ENTIRE actual finite field agrees on z>=-250 with

    E XOR semi-infinite_old_SW_deposits
      XOR mature_incoming_NE_front.

The checker separately bounds every omitted packet, old endpoint, recovery write, initial moving core, and missing incoming-past deposit below -250. It is an equality of fields on an unbounded half-plane, not an assumption that an apparently stable front has forgotten its history.

The five cap entries are:

    r28: (-27,-78), time208n+66185;
    r60: (-21,-84), time208n+62313;
    r61: (-1,-102), time208n+92097;
    r70: (-20,-85), time208n+67647;
    r75: (-26,-79), time208n+63171.

All headings are east, phase0. The entry times are independent of m because the earlier and later flights cancel their m dependence exactly.

Each complete cap model is checked twice: with its infinite deposition rays, and with a complete finite100-deposit kernel. Every finite read and infinite tail stays in z>=-125. Hence all five ENTIRE futures transfer to the actual two-cell seeds, retaining the actual history below the comparison region. Their permanent NE captures are

    r28: time208n+69617, pose(37,-6), west, phase32;
    r60: time208n+62729, pose(-13,-76), east, phase0;
    r61: time208n+92513, pose(7,-94), east, phase0;
    r70: time208n+68063, pose(-12,-77), east, phase0;
    r75: time208n+113611, pose(46,1), east, phase0.

Three tracks miss E completely; the other two genuinely scatter at it. None of these five requires a hidden lower-endpoint return. Fifteen complete literal two-cell controls at three parameter pairs match the formulas and pass an independent finite-field infinite-tail checker. Those controls are not the universal proof.

## Ten parity-based recurrence exclusions

Assume the previously audited critical-clock, favorable-ten sector and remote-incidence lemmas. Fix m, then let the four remote checkpoint cells escape. The retained core is unread by the blank trajectory. Any recurrent mass-five sequence therefore forces the first far SW contact to be q_n. Before the fixed retained-core hit, every other remote corner misses the q_n prefix by its bounded u-strip and z upper bound.

The checker includes all original history, the complete local recovery, any flight/cap interaction, the partial phase-zero advance and the canonical outgoing core in its stationary-archive bounds. In particular, a bound on the visible local packet is not substituted for a bound on the full archive.

For phases32,38,46,47,55,57,71, the outgoing NW or SE front could only encounter its corresponding adjacent corner, A or C. The phase72 fresh ray has the WRONG coordinate parity for that corner. The exact fresh-phase calculation shows that every possible contact instead lies in the nine favorable ordinary channels. Their58-unit outward-u guards miss the complete bounded-u archive, the fixed retained core, and the remaining corners by divergent axial gaps. Four-edge cases either miss the tail by its fixed-z strip or have the same ordinary escape.

For phases28,60,61, the full cap output is NE and stays in a bounded u-strip. Both adjacent cycle corners have u tending to opposite infinities, so only the opposite NE corner D can collide. Its parity is(even,odd), opposite in both coordinates to q_n=(odd,even). All three returned phase72 rays have parity(odd,even), so they cannot hit D exceptionally. Every actual hit is ordinary; its future lies in z>=z(D)-58, above the complete stationary archive and both adjacent corners by their divergent axial gaps. Every four-edge orientation has all three unused corners outside the whole bounded-u parent.

This excludes precisely

    28,32,38,46,47,55,57,60,61,71.

No absolute sign of an unanchored upper row is assumed. The cycle uses the z-clock for D before a new corner is hit, and only the justified axial gaps for later ordinary escapes.

## Four protected scars

The already audited far_sw_core/return_scars certificate treats13,14,27,89. Their full perturbed fields rejoin the q_n parent up to a finite scar below z=-93, while all reference reads after segment3, including the intermediate q and q+a parents and the entire final rectangle, stay above that bound. Thus the usual incidence coupling is unchanged: ordinary corners escape, exceptional corners force a_n and then c_n, a four-edge strand cannot realize the full forced chain, and the four-cycle captures. The finite scar is preserved and proved invisible, not deleted.

Together these give fourteen recurrence exclusions:

    13,14,27,28,32,38,46,47,55,57,60,61,71,89.

The remaining eight classes are15,29,45,56,62,70,72,75. Their outgoing phase72 ray has the matching parity, so an additional exceptional-corner analysis is genuinely required. This package does not close the entire negative-z arm or prove the arbitrary finite-seed conjecture.

## Reproduction

Run certify_caps.py, certify_bridge.py, certify_mass5_interfaces.py and finite_controls.py. The manifest pins the cap words and exact outputs. The local parallel-model and prior full-history strip certificates are explicitly hash-bound. The opposite-corner discovery files are separate and are not proof inputs.
