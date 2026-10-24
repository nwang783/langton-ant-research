# Fixed initial anchors: port debt is a weighted actual separator-crossing ledger

23 October 2026, 18:19 UTC. Exact continuous-cursor identities, a nontrivial
first-entry/last-exit sufficient condition for amortization, and actual
all-parameter countercontrols. These are not a universal debt bound or a
capture proof.

## 1. Two fixed anchored regions

Use either z=x+y or z=x-y and its retained strict-clock head correction J.
Choose an INTEGER physical separator k and fixed clock centers

    A={q:z(q)<=k-1},   c_A=k-a,   a>=1,
    B={q:z(q)>=k},     c_B=k+b,   b>=0.

The centers stay fixed for the entire interval; they can be selected from
INITIAL seed/head normal coordinates. Define the piecewise head function

    H(X)=J_(c_A)(X) if z(p)<=k-1, else J_(c_B)(X).

Let N_k be the number of ACTUAL fine moves crossing this separator in either
direction during a finite continuous interval. The port debt P of the two
regions satisfies the EXACT identity

    P=H(X_t)-H(X_s)+kappa(a,b)*N_k,
    kappa(a,b)=(3^a+3^(b+1)-4)/2.                         (1)

This is an actual travel ledger, not an endpoint relaxation. Every crossing
costs the SAME positive integer in both directions.

Proof: the read region's center agrees with the center used in H before the
step. If the next head stays in that region, its J change is exactly the
change in H. Otherwise the difference is the center-switch jump at the actual
arrival pose. An A-to-B crossing arrives at z=k with epsilon_z(h_next)=+1,
giving the jump

    [f(a)+3f(b)]/2.

A B-to-A crossing arrives at z=k-1 with epsilon_z(h_next)=-1, giving

    [f(b+1)+3f(a-1)]/2.

Since f(r)=3^r-1 for nonnegative r, these are equal to kappa(a,b). Summing
changes of H telescopes and proves (1). The signs use the ACTUAL arrival
heading, so the continuous cursor is essential.

For the adjacent initial anchors c_A=k-1,c_B=k, one has kappa=1. If the
endpoint transverse head coordinate and heading agree, their H terms agree
and P=N_k exactly, however far the cursor traveled longitudinally.

## 2. Ordered anchored strips and a genuine sufficient ordering condition

More generally, partition all cells into finitely many ordered z strips with
integer boundaries k_j. Choose one fixed center c_i inside each strip, for
example from ordered initial-seed normal coordinates. At a boundary between
centers c_i<=k_j-1 and c_(i+1)>=k_j, put

    a_j=k_j-c_i, b_j=c_(i+1)-k_j,
    kappa_j=(3^a_j+3^(b_j+1)-4)/2.

Then the same proof gives

    P=Delta H + sum_j kappa_j*N_j.                        (2)

There are no unrecorded internal region visits. Infinite outer strips cause
no problem because only actual boundary arrivals enter the correction.
A uniform width-w strip partition with left-endpoint centers has constant
kappa_j=(3^w-1)/2.

A sufficient STRUCTURAL first-entry/last-exit condition is: for each fixed
separator, its actual side word contains no A-B-A-B subsequence (nor the
opposite B-A-B-A). In other words, no side is reentered while a second
later visit to the other side is still pending. This is a condition on the
actual continuous exposure order, not a postulated numerical P bound.
It forces N_j<=2. Consequently

    P <= Delta H + 2 sum_j kappa_j.                       (3)

For a same-transverse-pose return Delta H=0. This bounds the ENTIRE port debt
by the fixed initial-anchor palette independently of runtime, board mass,
complete-discrepancy size, or longitudinal travel. It is genuinely sufficient
for P amortization, but it is NOT asserted to hold on arbitrary ants.

For an arbitrary finite palette of M regions, a stronger common sufficient
condition is that its run-compressed visit word contains no alternating
A-B-A-B subsequence for any two distinct regions. Such a word has at most
2M-1 streaks. Proof: between successive appearances of its first label, the
other labels occupy disjoint alphabets; otherwise A-B-A-B occurs. Induction
on M gives the stated bound. Let H use the current read region's center. If BOTH center values at every
actual interface port have J magnitude bounded by a geometric constant L,
exact switching telescoping gives

    P <= Delta H + 2L(streaks-1) <= Delta H + 4L(M-1).

For a same-pose return Delta H=0. For a partition inside an initial-geometry
box plus one exterior region, all interface ports lie near that fixed box,
even when an exterior visit travels arbitrarily far. An unfinished final
exterior visit can have a distant endpoint, so its Delta H MUST be retained.
The missing hypothesis is the exposure ORDER, not a duration bound.

## 3. Planarity and initial anchoring do not supply that condition

It fails already on the actual blank ant. Let A be the initial head cell
{(0,0)} and B its complement. Actual reads at ticks0,1,4,5 have region labels
A,B,A,B. This uses one continuous ant, including the actual RRRR return at
tick4. Planarity does not make a fixed spatial region palette a stack.

The earlier actual blank ticks9..17 restored-bridge control remains relevant:
net-discrepancy components omit twice-read travel edges. Assigning new region
instances to every revisit can manufacture a noninterleaving word, but then
the number of regions is no longer fixed by initial geometry. Such a reset
is precisely the resource that would need an independent causal charge.

## 4. A single finite standard seed makes total anchored debt infinite

Normalize the retained canonical13-black standard104 source to physical
head(0,0,W). Its black board is exactly

    {(-2,-4),(-2,-3),(-2,0),(-1,-5),(-1,-2),(-1,-1),(-1,0),
     (0,-6),(0,-5),(0,-4),(0,0),(1,-3),(1,-2)}.

The retained exact infinite-word verifier certifies the standard104 word
forever, with drift(-2,-2). The two normal anchor values -1 and0 occur at
ORIGINAL black cells(-1,0) and(0,0). Use z=x-y, separator k=0 and those
centers. One exact standard period crosses the separator EIGHT times,
returns to the same transverse pose, and has P=8. Therefore

    P after n standard periods = 8n.

The trajectory is standard from the start. Its internal K count is zero;
only finite true-history boundary windows could precede that statement.
Hence a universal FINITE total positive-port-debt budget for this fixed
initial-anchor partition is FALSE even on one finite immediately capturing
seed. A useful global ledger must remove ordinary standard flux, or merge
whole standard read bands, while retaining their actual archived output.
Fixed initial anchors alone do not perform this renormalization.

## 5. Actual184 and394 families also violate constant-per-region charges

Use the SAME two regions t=x-y<0 and t>=0, with fixed centers -1,0. These
normal values occur among the original black seed families in both signed
constructions. The literal supplied period words give:

    standard104, SW at t=0:       8 crossings, P=8;
    nonstandard1564, entryN t=0:  4 crossings, P=4;
    nonstandard4352, entryW t=-5: 66 crossings, P=66;
    return15324, entryN t=6:     326 crossings, P=326.

Each drift is parallel to (1,1), so endpoint t and heading return and these
counts repeat exactly. The actual original184 family realizes n successive
1564 periods, giving P=4n on that subinterval with only TWO fixed anchored
regions and bounded normal interface ports. Its compressed region word is
B-A-B-A-B per period; concatenation has4n+1 streaks. Thus no first/last stack
condition can be inferred for these actual nonstandard episodes.

The signed original394 two-phase family has3M+4 outward4352 periods and M
return15324 periods. Those genuine bodies alone contribute

    66(3M+4)+326M = 524M+264

to the crossing/port ledger. This is not the total prefix debt: other actual
stages and endpoint head terms must also be retained. No hypothetical
prepared background is substituted for the finite original seed; transfer
of these supplied bodies is the signed finite-family theorem.

A stronger full-word affine check, using each manifest stage's actual normal
entry pose and its supplied repeat count, gives the following exact counts
for this cut. Subtract ONLY the explicitly supplied ordinary-standard stages
(H, H-prefix, and where present SW-standard/SW-partial); no generic factor
classification or physical archive deletion is implied:

    original184 prefix: total crossings144n+559;
      supplied standard crossings140n+490; residual4n+69.
    original394 two-phase prefix: total1148M+3498;
      supplied standard crossings624M+1712; residual524M+1786.
    original394 capture section: total1148M+3944;
      supplied standard crossings624M+1712; residual524M+2232.

Each repeated stage restores its heading and normal position, so its one-word
crossing count multiplies EXACTLY by the affine period count for every integer
parameter. Literal fixed stages contribute the displayed constants. This is
an actual-flux subtraction from an accounting ledger; every written standard
archive remains physically present for later interactions.

Thus removing the known standard flux is necessary but not sufficient:
residual repeated nonstandard exposures still grow with the initial
longitudinal preparation scale in both signed finite families.

These examples do NOT refute a bound depending on initial LONGITUDINAL
geometry: their seed radii grow with n or M. They refute a constant charge per
normal strip, region, anchor or profile, and demonstrate what the repeated
exposure term actually measures.

## 6. Coarsening shows why port debt alone is not the global resource

Conversely use one common clock center at the INITIAL head's t coordinate,
with no center switches. Its entire P is just the endpoint J difference.
For the signed184 prefix, start t=-37,W and end t=0,N. With c=-37,

    P=-3(3^37-1)/2,

independent of n. Its positive part is zero while its actual K count grows
as614n+92. For the394 two-phase prefix, start t=25,W and end t=6,N. With c=25,

    P=(3^19-1)/2,

independent of M, while actual K=86411+13269M. At that family's certified
capture section, t=30,N, the same common-center correction is instead
-3(3^5-1)/2. These are exact actual endpoint corrections, not a claim that
one may reset the field there.

So a good P bound is not sufficient by itself: these actual families have
such bounds already. Coarsening the center choice leaves their growing
archive credit in the FIELD term. Finer initial-anchored regions shift some
of that credit to repeated separator crossings. A global proof must control
the JOINT field credit and nonstandard port debt using initial longitudinal
geometry and literal causal supply, not merely optimize one term away.

The concrete open next premise is an independently paid bound on repeated
NONSTANDARD separator exposures after ordinary standard flux is removed,
together with a finite initial-geometric funding rule for the surviving
archive field. No such bound is proved here. Initial-root count, the new
at-most-three direct producer law, and mere planar read connectedness do not
supply it automatically.
