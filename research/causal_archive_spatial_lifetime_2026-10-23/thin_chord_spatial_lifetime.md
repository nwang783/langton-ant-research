# A thin-chord causal archive horizon: 294 C increments

23 October 2026, 19:24 UTC. Author proof and exact lattice controls; independent
review requested. This is a quantitative strengthening of the signed 2323-C
produced-identity lifetime theorem, not a finite-seed capture theorem. No new
trajectory search, larger counted-age table, or component/root budget is used.

## 1. Geometric statement

Use the corrected-center checkerboard lattice of an actual simple D/V/U/C
atomic factor. Translate its first center A to zero. Then all atomic entry
centers lie in

    Lambda = {(x,y) in Z^2 : x+y is even}.

All actual atomic chord vectors belong to the following twelve-vector set:

    S = {rot_h(1,1), rot_h(1,3), rot_h(0,4) : 0<=h<4}.

The D and C vectors coincide. Every vector has coordinate span at most four.
For a nonzero endpoint displacement d=B-A in Lambda, define the FINITE set

    Q(d) = {s in Lambda : [s,s+v] meets [0,d] for some v in S},
    M(d) = |Q(d)|.

These are possible geometric entry sites, not asserted feasible ant roles.
A site occurs only once even if several of its candidate vectors meet [0,d].
The exact closed-segment intersection convention includes endpoints, tangency,
and overlap, so it is conservative under a sufficiently small perturbation.

**Thin-chord theorem.** If n is the number of C atoms on a finite injective
actual center subarc from A to B, then

    n <= 4 M(B-A) + 11.                                  (1)

For A=B, injectivity instead says the subarc is empty and n=0.
There is no bound on the number of zero-C atoms, path diameter, or duration.

The site count admits an explicit ALL-DISPLACEMENT linear bound. Put

    D = ((d_x+d_y)/2, (d_x-d_y)/2),
    g = gcd(|D_x|,|D_y|).

The lattice change (x,y)->((x+y)/2,(x-y)/2) sends Lambda bijectively to Z^2.
Every possible atomic vector lies in the physical L1 ball of radius4, hence
in the transformed square[-2,2]^2. Therefore Q(d) is contained in the lattice
points of the swept square

    K_D = [0,D] + [-2,2]^2.

For nonzero D this integral convex polygon has area16+4(|D_x|+|D_y|)
and boundary lattice count16+2g. Pick's elementary lattice-point identity
then gives

    M(d) <= 25 + 4(|D_x|+|D_y|) + g
          = 25 + 4*max(|d_x|,|d_y|) + g.

The area formula follows by sweeping the square along D; when both coordinates
are nonzero its boundary consists of four surviving axis edges of total lattice
length16 and the two translates of D, each of lattice length g. The axis-parallel
case is the corresponding rectangle and has the same formula. Thus (1) implies

    n <= 16*||d||_infinity + 4g + 111
      <= 20*||d||_infinity + 111.                        (1a)

This is a linear nearby-return turning bound for arbitrary simple actual
center subarcs, rather than the previous quadratic endpoint-rectangle bound.
The exact Q(d) count is smaller and is used for the294-C literal corollary.

## 2. The closing bridge has only M(d) crossings, not rectangle-area cost

Let P be the given finite simple polygonal center subarc and assume A!=B.
Choose W arbitrarily close to B, not on its final chord, so that the short
segment B--W meets P only at B. Such a disk exists by injectivity and finiteness:
every nonincident closed chord has positive distance from B. The closing
bridge is B--W--A, with its long second leg arbitrarily close to [B,A].

All possible atomic chords that can meet such a bridge have entry sites in a
fixed finite rectangle: the A/B coordinate rectangle expanded by five suffices
when |W-B|_infinity<1, because atomic coordinate spans are at most four. Among
these finitely many possible chords, those disjoint from [A,B] have strictly
positive distance from it. Therefore W can be chosen sufficiently close to B
that the long segment W--A meets ONLY candidate chords whose closed segment
already meets [A,B]. In particular their entry sites belong to Q(d).

Choose W generically in this sufficiently small open disk. It can avoid the
finitely many bad lines producing collinearity, passage through an atomic
vertex other than intentional A/B, tangency, an opposite endpoint corner, or
self-contact between the two closing segments. The short segment has no
crossing of P. The long segment meets each straight atom at most once, and
injectivity makes all its atom entry sites distinct. Hence the closed polygon
P followed by B--W--A has at most

    k <= M(d)

ordinary transverse self-crossings. No rough area estimate is used. The
argument does not choose a bridge that depends on an unproved avoidance of
old residuals: it is an auxiliary geometric closing curve, not ant motion.

The elementary crossing/turning inequality is |I|<=k+1, obtained by resolving
transverse self-crossings into at most k+1 simple Jordan polygons. The signed
atomic tangent lift gives exactly

    T_open = pi*(n-e_last)/2 + alpha(first)-alpha(last),

where e_last is one if the last atom is C and zero otherwise, and all alpha
values lie in [0,pi/4]. Thus |T_open-pi*n/2|<=3*pi/4. The three new principal
closing corners contribute at most 3*pi in absolute value. Consequently

    pi*n/2 <= 2*pi*(k+1) + 15*pi/4,
    n <= 4*k + 11.5,
    n <= 4*k + 11 <= 4*M(d)+11.

The tiny short leg is the improvement over the earlier arbitrary interior W:
it has no crossings, so one entry site is not charged for two bridge legs.

## 3. Exact producer-consumer specialization

Take a residual identity freshly installed by a full packet and later consumed
by a full packet in this SAME simple actual factor. Normalize the source
full-entry pose to (0,0,N). For source output slot o, consumer input slot i,
and consumer relative heading h, put

    p = o - rot_h(i),
    A = (-1/2,-1/2),
    B = p + rot_h(-1/2,-1/2),
    d = B-A.

The ordered source-included/consumer-excluded C age is exactly n on this
source-entry/consumer-entry center subarc. The literal retained-eight geometry
has 68 output slots, 23 input slots, and 3,128 sector-compatible alignments
among 6,256 raw alignments. They give exactly 72 distinct d values.

Exact closed-segment intersection over Lambda gives

    max M(d) = 71,
    max (4*M(d)+11) = 295.

The only three role alignments attaining M=71 have source UCC output(0,7),
consumer U, UC or UCC input(-1,4), relative heading S, consumer head(-1,11),
and center displacement d=(0,12). Their C age is congruent to2 modulo4,
because every C changes the heading by -1. Thus their age is at most294.
Every other alignment has a smaller geometric bound. Therefore every actual
produced-input transfer in the stated simple-factor scope has

    source-included C age <= 294.                        (2)

No claim is made that any maximizing static role is physically feasible or
that age294 is attained. Most literal role alignments are not actual transfers;
retaining them only weakens the upper bound.

For exact reproduction, a candidate entry site meeting [0,d] must lie in its
coordinate rectangle expanded by four, so the finite enumeration domain is
proved. The checker records every candidate entry site, its intersecting
vectors, every literal role, its heading residue, and its rounded age bound.
There is no hidden age cutoff or path search.

## 4. Causal archive consequence and exact scope

A produced residual identity still current more than294 C increments after
its full source entry cannot be consumed later within the same simple factor.
The ordered complete-context ledger also keeps such an unconsumed identity
outside all later complete contexts there. It is permanently unread within
that factor. This applies to all complete recurrent-eight factors beginning
U, UC or UCC by the signed U-entry center-simplicity theorem.

For a current occupied primal fence whose boundary consists entirely of such
old produced residual identities, the signed coupled-cursor gate theorem
therefore provides permanent archive shielding, with actual w on the outside.
For mixed old-center/produced-edge fences, its existing strict Jordan geometry
and28-cell fine-path buffer remain necessary and unchanged.

More generally a canonical frozen white-dual archive at an actual full-packet boundary
cannot be reloaded after ALL its boundary identities are older than294,
provided every one is a produced residual identity from this same factor.
At the first physical L crossing, the boundary black cell would be read inside
a later complete context; the age theorem forbids this. Boundary edges in the
transported core, untouched entry identities, or sources before the chosen
factor boundary do not have this certificate.

This is a genuine stronger spatial lifetime / causal reuse restriction. It
still does NOT bound C count, U count, total permanent archives, root-component
rank, independent chain births, or raw duration. A single permanent U unit
cycle still encloses no physical integer cell, and infinitely many disjoint
permanent genuine U stars/cycles are not excluded. No universal stabilization
claim follows merely from lowering the archive horizon.

## 5. Dependencies

- Signed atomic tangent-lift theorem: core_periodicity_new/
  atomic_center_turning_frozen_20261023_1400/manifest.json.
- Signed U-entry simplicity: core_periodicity_new/
  U_entry_simplicity_frozen_20261023_1616/manifest.json.
- Signed literal residual masks: core_periodicity_new/chronology_dcuv/
  literal_residual_geometry.json, also bound by the signed2323-C theorem.
- Previous theorem and ordered-context consequence: core_periodicity_new/
  simple_center_C_lifetime_frozen_20261023_1719/manifest.json.
- Gate shielding: spatial_cursor_2026-10-23/
  coupled_dual_cursors_and_gate_memory.md.

The existing sources are not edited. This note asserts an explicit new
quantitative deduction within their hypotheses, not a literature priority.
