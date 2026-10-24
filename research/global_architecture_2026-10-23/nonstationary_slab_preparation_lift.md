# Finite standard preparation cannot fund an unbounded changing short scaffold

23 October 2026. Exact boundary/ownership extension of the signed finite-flight
lift. The five-period slab's semantic, inherited-color and physical chronology
audit is independently signed. The new quantitative physical lift is submitted
for separate review; it is not inferred merely from a checked RUP certificate.

## Statement

Use the same inverse104 coarse scaffold V at(0,0,W), drift(-2,-2). In EACH
coarse period, independently replace EACH of104 coarse turns by any of the
ten exact-pose legal images of length1,5,or9. No image choice is required to
repeat in another period. Let N such coarse periods follow any standard-flight
itinerary on its ORIGINAL finite initial board B. With canonical H powers,
L total non-H preparation reads and parallel/perpendicular flight counts,

    |B| + 12*F_parallel + 2L + 3080*F_perpendicular >= floor(N/5).

Arbitrary cyclic standard phases add104 preparation reads per flight. A
uniform coarser consequence is

    |B| + 2L + 3288F >= floor(N/5).

Flight lengths and offsets are arbitrary. This covers occurrence-dependent
choices in this exact palette/scaffold, unlike the fixed-P corollary. It does
not cover changing coarse scaffolds, other images or unrestricted ant dynamics.

## Precise finite premise

The construction analysis's five-period encoding has520 independent exactly-one
image choices. Every cell reachable by ANY allowed earlier coarse period has
an arbitrary entry-color bit. Only genuinely new cells receive the OR of a
compatible finite standard-rail bundle's mature black profiles. Outputs are
free. The reported CNF has44983 variables/183663 clauses and a787-addition
monotone RUP refutation. The premise needed here is the SEMANTIC validity of
this complete finite relaxation and its UNSAT proof.

Source note: `../causal_reduction/unit_scale/nonstationary_short_slab_obstruction.md`.
Source geometry: `nonstationary_short_slab/architecture.json` in that directory.
Independent premise audit: `../audits/check_nonstationary_short_slab_independent.py/json`.
This lift introduces no new solver horizon or palette bound.

## 1. New-cell ownership is disjoint between five-period slabs

Use full-drift class a=(x-y,x mod2), representative(e,e-a_0), and common
physical level k=floor(x/2), relative to the consumer start. Let L_a be the
minimum possible period-zero level over ALL legal image choices and phases.
An occurrence in coarse period r has level l-r.

For a slab starting at period5b, any possible earlier read of orbit a has
level at least L_a-5b+1. The prescribed-new cells of the slab are exactly

    L_a-5b-j, j=0,1,2,3,4.

The minimum-level potential phase in each of the five periods proves all five
cells occur in the potential slab support. No other slab cell below the
earlier-reach threshold is possible. Thus there are150 prescribed-new cells,
five on each of30 potential orbits. Their sets are pairwise disjoint across
different b. This property concerns ALL potential earlier reads, so it remains
valid under changing image choices and arbitrary actual inherited debris.

The arbitrary inherited entry bits are a relaxation of the real earlier
consumer history. They are not a reset and are not asserted to have a separate
physical realization.

## 2. Fixed preparation defects spoil at most twice as many slabs

All possible period-zero offsets lie in[-2,2]. The full potential read-level
interval of slab b is therefore

    I_b=[-6-5b, 2-5b],

nine consecutive levels. Any one physical level lies in at most TWO intervals
I_b, since starts differ by five and three such windows have empty intersection.

As in the signed finite-flight theorem, mark:

* at most6 endpoint-fringe levels per parallel standard flight;
* every cap-read level, at most L;
* every perpendicular read in U=[-18,16], at most1540 cells per such flight.

U has70 full-(2,2) classes and a perpendicular standard strip22, hence1540.
It contains every relevant parallel writer band, including each possible
black-endpoint clash witness, not just the consumer strip.

Consequently at most

    12*F_parallel + 2L + 3080*F_perpendicular

slabs contain any marked level. Overlaps only improve this estimate.

## 3. One consistent bundle applies throughout a good slab

Avoiding marked endpoint levels makes every parallel writer complete or
absent at every level of I_b. More is needed than pointwise maturity: the
slab encoding uses ONE fixed bundle for all its new cells. Here that follows
because canonical H endpoint widths are always2 or3, never zero. A contiguous
I_b containing both a complete and an absent level would have to cross a
nonempty marked fringe. Thus each writer's active status is constant across
the whole good window, even for a flight shorter than a fringe width.

No cap or perpendicular writer reads U in this window. At every level the
complete first-R histories therefore preserve earlier black endpoints against
all later parallel writers. Relevant active bands are pairwise disjoint and
their final colors are one compatible, conserved-sector standard bundle
throughout I_b. Irrelevant writers cannot repair an overlap witness: their
own first R at that black cell would already be impossible.

## 4. Each good slab costs a distinct INITIAL black cell

Suppose a good slab's150 new cells contain no extra initial black outside
the active writers' read bands. New-cell ownership shows no earlier consumer
period touched them. Active writer histories fix their output exactly; absent
writers, caps and perpendicular flights never touched them. Hence their entry
colors equal the single compatible rail bundle.

Give every inherited bit its actual entry color and every image selector its
actual chosen value. All finite chronological chains then satisfy the slab
encoding, contradicting the UNSAT premise. Therefore a legal good slab must
contain at least one extra cell from the ORIGINAL B among its new cells.

New sets of different slabs are disjoint, so these black cells cannot be
charged twice. There are floor(N/5) complete slabs. Subtracting the possible
bad slabs proves the inequality. No bound on ant duration or number of
general interactions is assumed.

## Scope and dependencies

The layer of free inherited bits deliberately admits histories beyond actual
ones; UNSAT of that relaxation is enough. SAT would have been only finite
feasibility, not an infinite schedule. The derived five-period range and its
new-cell ownership must both remain part of the premise.

The physical lift depends only on signed standard-flight endpoint geometry,
the fixed-strip intersection count, first-R black persistence, and the stated
slab contract. It neither assumes a bounded number of collisions from a
bounded number of components nor changes the global capture status.
