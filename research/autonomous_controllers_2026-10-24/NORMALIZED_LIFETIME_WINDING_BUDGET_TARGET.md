# A representation-invariant winding input-budget target

24 October 2026. The candidate inequality below is UNPROVED. This note proves
its representation invariance, specifies exact shared-lifetime data, and
records supplied controls. It is not a classification result.

## Precise proposed inequality

Use the signed all-cap non-axis lifetime boundary graph. Let I be the number
of consumed BLACK-input roots and O the number of permanent-output read
roots per FULL period(P,d). A BLACK-first even history contributes one of
each; these are distinct endpoints. Unread passive BLACK strands are not
consumed inputs and are not charged to I. Put

    m = gcd(|dx|,|dy|),
    S = sum_C |w_C|,

where the sum is over all boundary cycles and w_C is their FULL-drift voltage.
Zero-winding cycles contribute0; actual internal lifetime components remain
retained separately. The test target is

    m*(S-1) <= 2*min(I,O).                              [UNPROVED]

The signed mod2 total-homology theorem gives S odd and S>=1. Thus the target
says that each extra pair of essential strands costs at least m consumed
inputs AND m outputs. No injection or resource ownership proving that cost
has been established. In particular, do not assert S=1 for WHITE fronts.

If the target were proved, the signed four middle-short WHITE types020d0dbc
would be excluded, since I=0 and S>=5. This is its concrete intended target,
not a consequence currently available.

## Exact period-power invariance

Replace the representation(P,d) by(qP,qd), q a positive integer. Physical
histories do not change, but each old full-drift class splits into q classes.
Consequently I,O,m are multiplied byq.

For a boundary cycle of winding w, its q-fold cover has gcd(q,|w|) cycles,
each of absolute winding |w|/gcd(q,|w|). This follows by following one lift
around the cycle: its sheet label changes by w moduloq. For w=0 there are
q zero-winding copies. Therefore S stays EXACTLY unchanged. Both sides of
the proposed inequality are multiplied byq, so truth or failure is invariant.

This is why sum(max(0,|w|-1)) with an unnormalized I count was not selected:
it changes when a high-winding component splits in a power representation.
For example, the prepared10 component of winding3 becomes three winding1
components in its30-read full-period representation, but S remains3.

Genuine quarter rotations preserve m and all absolute windings. Phase cuts
only change voltage gauges and root labels. The complete FULL drift graph is
always reconstructed; m is merely a normalization statistic, not permission
to replace that graph by a primitive-direction quotient.

## Supplied exact controls

The supplied controls give:

- Standard104: m2, I0, O12, S1, both sides0.
- Prepared10: m1, I1, O1, S3, both sides2.
- Prepared1564: m14, I197, O301, S1, sides0 and394.
- Prepared4352: m26, I406, O590, S1, sides0 and812.

For each, the executable reconstructs powers1,2,3,5 under all four genuine
quarter rotations, and three phase cuts. The exact covering formula, all
root counts and both candidate sides are checked. The1564/4352 full input,
output, passive strands and finite XOR caps remain the signed normal-form
dependency in lifetime_boundary_graph_certificate.json. The infinite input
requirement is not removed or replaced by a finite field.

These are controls only. Their agreement is not evidence of exhaustion or
a proof of the inequality. No additional period scan is a theorem premise.

## Full shared-lifetime multiplicity, not cancellation by name

Augment alpha union beta with the actual sigma edge i→i+1 at every unmatched
input or output root i, including the exact period seam. Every event vertex
then has degree2. These expanded circuits are the boundary cycles together
with the original internal alpha/beta cycles; every phase event is retained.

For each actual owned BLACK lifetime e, let ell_e>0 be its R-to-next-L age.
It is a multiple of4, since a same-cell return with alternating step axes has
length divisible by4. The alpha edge and its beta conjugate have the SAME
positive elapsed-time value ell_e, though they may belong to DIFFERENT
expanded circuits and may be traversed with equal or opposite signs.

Orient an expanded circuit C arbitrarily. Let r_C be its signed number of
unmatched actual sigma steps, each of elapsed time1. Let n_C,e be the sum of
the traversal signs of e's alpha and beta copies lying in C. It can be
-2,-1,0,1,2. Exact clock telescoping gives

    w_C*P = r_C + sum_e n_C,e * ell_e.                  [EXACT]

The JSON retains EVERY lifetime owner phase, consumption phase, full voltage,
age, both owning circuits, and both signs. It does not identify the two
copies merely because they have the same physical owner.

For the chosen orientation of the standard essential circuit, w=-1,r=0,
and the signed lifetime-age sum is -104. Among all46 actual owned lifetimes,
12 have both copies in the same circuit with equal signs,12 have them there
with opposite signs, and22 are split between circuits. Thus even the genuine
WHITE standard controller defeats naive cancellation of shared copies.

Prepared10 has w=3,r=-2, signed lifetime-age sum32. Its four lifetimes have
two equal-sign same-circuit pairs and two opposite-sign pairs. These exact
identities do not yield a sign or upper bound on the age sum; lifetime ages,
interior components and their incidence remain unbounded in general.

## Frozen data

explore_normalized_lifetime_winding_budget.py
SHA256 2ac5ceeb4fe5aa59fed2e1f5e75cc831945703220c05c1264b98ce0260e9e82e
normalized_lifetime_winding_budget_controls.json
SHA256 688708114d220166f2728ff3d1e59565b90412992da7e5ac8a622422675046d3

Author controls are complete. Independent review of the representation law
and identities is separate from the unproved input-budget target. No claim
of independent PASS for this note is made here.
