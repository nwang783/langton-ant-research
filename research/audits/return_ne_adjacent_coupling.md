# Independent completion of the six return-NE adjacent-corner classes

Status: independently reviewed analytic coupling, supported by fresh complete-field color replays and an independent literal affine-geometry checker. This note preserves the stopped analysis's original files unchanged.

## Scope and dependencies

Use `u=x-y`, `z=x+y`. Fix an integer `m>=100`, choose one fresh phase
`r in {15,29,45,56,62,72}`, and retain

    s=(-2m+6,-2m-43)+Q_r,

where `Q_r` is the phase-r read of canonical W104 starting at the origin heading east. Let `k>=100`, `n=m+k`, and

    Q=(-2m-2k-33,-2m-2k-14)=(l,b).

The recurrence conclusion is conditional only on the already established mass-five fixed-pose, divergent-critical-clock, remote-incidence and favorable-ten scattering hypotheses. It excludes these six fixed retained-core classes from such a recurrent subsequence. It does not prove arbitrary finite-seed capture.

The original return-NE package already excludes fourteen phases, and its separately audited opposite package excludes 70 and 75. The six classes here complete all twenty-two return-NE phases at ages m>=100. The quantifier is fixed s (hence fixed m), followed by sufficiently large remote parameters and axial gaps; no uniform threshold over all retained cells is asserted.

The full exact color computations are the six `scattering/return_ne_frontier/adjacent/certificate_r*.json` files and `certificate_cycle72.json`. Fresh independent executions produced identical outputs, bound in `audits/return_ne_adjacent_replay/replay_manifest.json`. The independent checker `audits/check_return_ne_adjacent_geometry.py` imports none of the color engine: it reconstructs every affine read endpoint, pose, elapsed time, initial bit, complete finite-prefix half-plane bound, infinite tail and relevant phase72 intersection. It binds the replay/source/template hashes and actual certificate output fields.

## First remote contact after the retained bit

The complete two-bit q+s parents have bounded finite/archive u ranges and z<=35. Their outgoing directions are NW for 15,45,72 and SE for 29,56,62. Thus the only possible next cycle corner is respectively A=(l,t) or C=(r_x,b). Before that contact the opposite corner D misses by the positive z-clock: in a four-cycle z(D) tends to +infinity, since Q and D are the only favorable z cells outside the fixed core. The other adjacent corner misses by its divergent u coordinate.

Every ordinary first hit lies in the audited favorable sector and escapes: the corresponding 58-unit outward-u guard misses the complete bounded-u archive, the retained core and the other corners by the positive axial gaps. Therefore only phase72 needs further analysis. Intersecting the actual parent phase72 ray with the required row/column forces exactly the following extra black cell T:

| r | T | Parent phase72 epoch |
|---|---|---|
|15| A=(l,-2m+2k+1) | k-12 |
|45| A=(l,-2m+2k-11) | k-20 |
|72| A=(l,-2m+2k-33) | k-16 |
|29| C=(-2m+2k-12,b) | k-29 |
|56| C=(-2m+2k-12,b) | k-31 |
|62| C=(-2m+2k-24,b) | k-33 |

All epochs are nonnegative throughout the stated domain. These are exact equalities, not estimates inferred from a local infinite model.

The three-cell certificates start at time zero with exactly {s,Q,T}; they retain the entire inherited history. Their first T times are `104m+312k+c_r`, with c_r respectively 74914,73298,112022,72328,67172,67036 in the table order above. All prefix z maxima are 35.

## Complete three-cell outputs

Headings N,E,S,W are 0,1,2,3; phases refer to the fixed canonical W.

| r | Capture time | Capture pose, heading, phase | Tail |
|---|---|---|---|
|15|104m+520k+168039|(-2m-2k-68,-2m-2k+3), W, 0|SW|
|45|104m+520k+165799|same, W, 0|SW|
|29|104m+416k+132511|(-2m,-2m+47), E, 99|NW|
|56|104m+416k+127355|same, E, 99|NW|
|62|104m+416k+126907|(-2m-6,-2m+41), E, 99|NW|
|72|104m+416k+174812|(-2m-30,-2m-102), S, 0|SE|

For 15 the entire future has u<=76,z<=35; for 45 it has u<=66,z<=35. For 29,56,62 the finite prefix and all its written/initial cells have u>=-82, while the entire future has z<=35. Their infinite NW tails have fixed z ranges [-4m+43,-4m+53] for 29/56, or [-4m+31,-4m+41] for 62. For 72 the finite prefix and its whole stationary archive have u<=106; its SE tail has fixed z in [-4m-135,-4m-125]. These archive statements include every initial bit and all earlier writes, not only the last local packet. The growing new standard tail is handled by the ordinary scattering theorem, not incorrectly placed in the stationary archive.

## Four-cycle coupling for 15 and 45

Write J=r_x-l and H=t-b; both tend to +infinity. With the forced A, put e=1 or -11 respectively. The two unused corners satisfy

    u(C)=J-19,
    z(D)=J-4m+e-33.

For fixed m both escape the entire three-cell read region, whose u and z have constant upper bounds. Hence adding C,D changes no read, and the complete five-cell field has the same permanent SW capture.

## Four-cycle coupling for 29,56,62

With forced C let e=-12,-12,-24 respectively. The unused corners satisfy

    u(A)=-19-H,
    z(D)=H-4m+e-14.

Thus neither is read in the finite three-cell prefix, and D also misses the NW tail by z. If A misses the tail, capture is permanent. If A meets it, its parity is (odd,odd), whereas the returned phase72 ray is (even,even). Both have the same checker parity, and the independently reconstructed fresh-phase list shows precisely the ten favorable phases; therefore the hit is one of the nine ordinary ones.

Its outgoing NW guard lies in u<=u(A)+58. This misses the complete stationary archive u>=-82 and the retained cell for large H. It misses D because

    u(D)-u(A)=r_x-l=4k+e+33 -> +infinity.

The incoming mature NW rail and new impact packet are already included in the ordinary scattering theorem. No old archive is erased. Therefore every possible continuation captures.

## Four-cycle coupling for 72

After the forced A, t=-2m+2k-33 and H=4k-19. The unused corners obey

    u(C)=J-19,
    z(D)=J-4m-66.

They miss the finite three-cell prefix for large J; D also misses the SE tail by z. An ordinary C contact escapes in u>=u(C)-58, beyond the stationary archive u<=106, and away from D since u(C)-u(D)=H tends to +infinity.

The sole exceptional possibility is the phase72 ray of the actual returned SE tail. Its base is (-2m-22,-2m-104); intersecting y=b forces epoch k-45 and

    C=(-2m+2k-112,b),
    D=(-2m+2k-112,-2m+2k-33).

The full time-zero five-cell certificate covers exactly {s,Q,A,C,D} for every independent m,k>=100. It first reads C at

    104m+520k+170204,

never reads D (including the infinite tail), and captures NE at

    104m+624k+217977,
    pose (-2m+39,-2m-36), E, phase100.

This is a complete-field proof, not an extrapolation of the SE model through the next interaction.

## Both four-edge strand orientations

The incidence theorem gives either

1. A=(l,t0), Q=(l,b), C=(r_x,b), D=(r_x,v0), with t0,v0 fixed and r_x->+infinity; or
2. C=(r0,b), Q=(l,b), A=(l,t), D=(s0,t), with r0,s0 fixed and t->+infinity.

A forced NW phase72 hit for 15,45,72 requires the displayed A height to grow as +2k. It is impossible in orientation 1: the bounded-height A misses the parent's fixed-z NW tail, while C,D miss by divergent u/z. In orientation 2 the forced A is permitted. After it, C has u->+infinity and D has z->+infinity. For 15/45 these miss the entire future. For 72, C also has z->-infinity and therefore misses the SE tail's fixed z range; D misses all reads by z.

A forced SE phase72 hit for 29,56,62 requires the displayed C abscissa to grow as +2k. It is impossible in orientation 2. In orientation 1 it is permitted, but afterward A has u->-infinity and z->-infinity, while D has z->+infinity. These miss the finite prefix and the NW tail's fixed z range.

Thus neither strand orientation supports recurrence. No absolute sign was imposed on an unanchored cycle coordinate: cycle arguments use only the divergent J,H gaps and, before the first extra contact, the established z-clock conclusion.

## Conclusion

All six residual return-NE classes are excluded under the established mass-five incidence hypotheses. Together with the separately signed fourteen parent classes and two opposite classes, this completes all22 return-NE fresh classes for fixed m>=100. This does not extend the age threshold, prove a uniform bound in s, classify arbitrary cores, or settle the full finite-seed conjecture.
