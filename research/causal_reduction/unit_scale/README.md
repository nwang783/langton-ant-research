# Nonexpanding time-renormalization countermodel branch

23 October 2026, 01:58 UTC. No counterexample. This branch deliberately leaves
the expansive-matrix setting rather than increasing its bounded searches.

## Why the previous obstructions do not automatically apply

A uniform refinement with p(kn)=p(n), or a unit Gaussian rotation of p(n), can
have prefix radius O(log n) while revisiting bounded endpoints infinitely.
The infinite-distinct-cell step in expanding first-visit fuel arguments fails.
The exact bounded-carry verifier for expansive matrices is not a validator for
this class. An O(log n) mass bound is compatible with an O(log n) radius bound;
the area/curvature argument does not itself give a finite-support contradiction.
This resembles a two-sided stationary-memory construction rather than a growing
geometric copy. No autonomous mechanism has yet been built.

## Exact all-length reduction for two turn images

Let phi(R)=u,phi(L)=v have the same length k>1, with u starting R. Require the
usual heading-preserving geometry: from incoming north, u ends heading east
with displacement a*E, and v ends heading west with displacement a*W, where a
is a unit Gaussian integer. Then refining any word preserves its coarse final
heading and multiplies its integrated displacement by a. The fixed-point path
satisfies p(kn)=a*p(n), h(kn)=h(n).

Let e_R=#R(u)-#L(u), e_L=#R(v)-#L(v), and set

    lambda=(e_R-e_L)/2,    b=(e_R+e_L)/2.

The heading conditions imply e_R=1 mod4 and e_L=-1 mod4; in particular k is
odd. Let E_r(R),E_r(L) be the signed excesses of the r-th refined letters.
Their mean S_r and half-difference D_r obey the exact recurrences

    S_r=k*S_(r-1)+b*D_(r-1),    D_r=lambda*D_(r-1),
    S_0=0, D_0=1.

Every prefix position of phi^r(R) is a sum of r bounded offsets rotated by
powers of a. Its radius is O(r), so it reads at most O(r^2) distinct cells.
Consecutive reads at one cell alternate, on ANY initial coloring. Therefore
an ant-legal refined prefix must have |E_r(R)|=O(r^2).

The prolongable image u cannot be all R: heading preservation would give
k=1 mod4, hence k>=5, and its reads0 and4 would demand R at the same cell.
It cannot be all L because it starts R. Thus |e_R|<k and |lambda|<k. Solving
exactly,

    E_r(R) = b*(k^r-lambda^r)/(k-lambda) + lambda^r.

The polynomial cell ceiling first forces b=0, then |lambda|<=1. But then
lambda=e_R=1 mod4, so lambda=1. We conclude:

    e_R=1 and e_L=-1.

Thus EVERY ant-legal infinite word in this entire unit-scale heading-preserving
two-image class is exactly charge-preserving, not merely the examples chosen
for a search. This conclusion does not use finite support. For a rooted
first-letter cycle, apply the polynomial cell ceiling on its subsequence of
refined prefixes. The exceptional values lambda=+k or -k require both images
to be monochromatic and opposite. Their refined excess has magnitude k^r,
already contradicting that ceiling. Otherwise |lambda|<k and the same exact
formula forces b=0 and lambda=1 along the cycle subsequence. No geometric
expansion is needed.

For finite support, this means black mass at times k^r equals the initial
mass plus1. That is NOT a contradiction: the endpoints a^r E stay bounded.
Do not import the expansive midpoint argument at this step.

The prolongable-root reduction has passed independent analytic review; the
root-cycle sentence above explicitly handles the monochromatic exceptions.

## Small controls, not an all-length absence claim

At unit scale a=1 and radix5, all internally legal heading-preserving right
images have excess-3, so none passes the exact charge condition.

At radix9, exactly six internally legal right images have displacement E,
final heading E and excess1; there are six analogous left images with excess-1.
Four right images are prolongable, yielding24 independent pairs. Every one
has a literal cell-color conflict by zero-based read28.
`probe_charge_preserving_nine.py/.json/.records.json` freezes these controls.
Digest:5c67177ee6b87a10213e168bb729120b50833a30f08cb1859a361ca3457c502f.

The stronger occurrence-dependent, heading-free pure identity was also tested
with the existing exact position-only chronological DFS, allowing scale1:

- k5: complete27-node tree,84 terminal conflicts, max4 completed macros,
  latest conflict22.
- k9: complete101-node tree,1,518 terminal conflicts, max5 completed macros,
  latest conflict53.

The frozen outputs are `position_only_unit_k5.json` and
`position_only_unit_k9.json`. These arbitrary-initial-coloring exclusions have passed an independent
fine-step DFS reconstruction, without using the macro-image palette. It
exhausted421/8,105 fine-step nodes, with exactly27/101 accepted macro-boundary
nodes and matching maximum macro depths4/5. The independent artifacts are
`../../audits/check_unit_position_identity_independent.py/json`. No bound
was hit. The implementation is the already frozen
`../morphic_candidates/search_position_only_inflations.py`, called with
scale(1,0) rather than its default expanding-scale inventory.

Do not infer a general unit-scale exclusion or applicability of the expanding
matrix automaton. The next useful task is structural all-time certification
or a genuinely new unit-scale mechanism, not an endless sequence of larger
finite radix scans.

## A concrete nonuniform transport attempt, and a false invariant control

The nine-step right image RLLLLRRRR is a real local transport: starting from
three black corners (1,0),(0,1),(1,1), its first five reads erase that seed,
then its last four create a four-black square at the adjacent checkpoint.
We fixed this image and allowed an independent left image of length13,
net displacement W, final heading W and charge-1. The142 raw geometric left
words all fail internal read alternation. Thus this concrete variable-length
pairing is locally empty, before any long substitution test.
`probe_nonuniform_transport.py/.json` freezes the inventory.

A tempting all-length transport congruence is FALSE. At lengths1,5,9,13,
every internally legal word ending at(1,0,E) happened to have its L count
0 mod4. But the legal17-step word RRRLRRLRLRRLRRLRL has the same endpoint
and heading with six L turns. Hence the empty length13 charge class is only
a short local obstruction, not a proved mod8 rule. Do not extrapolate it.


## Current scope update (23 October, 03:27 UTC)

The analytic charge reduction now covers unequal two-turn image lengths,
with reducible and root-cycle exceptions explicitly handled in
`nonuniform_charge_reduction.md`; independent review is signed.
`prefix_charge_graph.md` gives the separately signed all-length negative-
cycle obstruction and two-turn ballot restriction.

The eight-independent-heading identity/nine controller exclusion is fully
signed, including first-state two-cycles. More strongly,
`occurrence_transport_exclusion.md` has a signed charge-free addendum:
no actual ant on any initial coloring admits nontrivial position-AND-heading
retiming from the same time-zero state with every delay at most9. Every
occurrence chooses independently; there is no fixed-controller assumption.
This does not cover positive initial offsets, changed boundary headings,
other spatial rotations, or any delay of13 or more.

The signed matrix dichotomy in the sibling `matrix_candidates` directory
shows why finite-order/stationary refinements remain a substantive residual
branch after eliminating intermediate shear/saddle/singular architectures.
No unit-scale finite-seed construction has passed.


## Structural all-length closure (23 October, 05:18 UTC)

The earlier fixed finite-order residual status is superseded by the independently
signed `primitive_perron_clock_obstruction.md` and
`finite_order_uniform_obstruction.md`. EVERY fixed uniform absolute-direction
substitution with finite-order spatial matrix is impossible on ANY initial
coloring, without symmetry, heading preservation or image-length bound. A
physical adjacent-pair lift handles arbitrary boundary heading maps. Positive
clock increments expose a genuine Perron pole, while bounded signed cell
occupation forces a semilinear denominator; analytic continuation gives the
contradiction. The half-turn uniform matrix dichotomy consequently retains
only fully expansive matrices with rho(A)<k<=|det A|.

The separately signed `nonuniform_exact_charge_obstruction.md` also excludes
ALL fixed eight-physical-state unit-pose/unit-position exact-charge controllers
with arbitrary unequal image lengths, including identity states. Combining it
with `nonuniform_charge_reduction.md` excludes every fixed heading-preserving
two-turn common-Gaussian-unit morphism with growing rooted limit, again on any
coloring. These are all-length theorems, not extrapolations of the short scans.

The local unequal-incidence21/29 transports in
`checker_axis_transport_structure.md` remain valid controls, but no fixed
recursive collection of exact-charge physical-state transports can grow legally.
The independently signed `typed_nonstationary_transport_obstruction.md` further
closes arbitrary level schedules in the elementary identity/nine alphabet,
with every legal finite composed word bounded by41.

Genuine remaining unit-scale construction freedoms include additional context
labels with reducible nonuniform transport components, nonconserving images,
or broader nonstationary phase schedules. No growing finite-seed model is
known. The automatic forced-seed theorem in the computability directory can
in principle decide any supplied fixed unit presentation, but is not an
integrated practical synthesis engine.


## Charge-free and nonuniform direction closure (23 October, 05:37 UTC)

The exact-charge restriction in the immediately preceding update is now
superseded by the signed `unique_parent_origin_lemma.md` and the computability
analysis's `finite_power_exact_validator/all_physical_unit_controllers_obstruction.md`.
ALL fixed undecorated eight-state unit-pose controllers are excluded, without
charge preservation or equal image lengths. Its safe finite-order extension
retains coarse incoming/final-heading compatibility.

A separate signed argument in `nonuniform_direction_finite_order_obstruction.md`
then removes that heading compatibility for FOUR absolute direction letters.
Every fixed nonerasing finite-order direction substitution is impossible on
any coloring, even with arbitrary unequal lengths, no symmetry, and changing
periodic boundary headings. It uses a terminal direction SCC and exact positive
Perron-vector lumping of actual adjacent pairs, NOT the physical origin lemma.

Additional hidden/context labels and genuinely level-varying controllers remain
outside both results. A useful structural residual is a drifting recursive
cycle in a reducible nonuniform decorated presentation. No actual complete-field
transport cycle or finite-support countermodel has been constructed.

### Positive hidden-label construction (05:56 UTC)

`decorated_oblique_hairpin.md` is a genuine all-depth oblique out-and-back
family with a one-read far cap, independently certified by complete histories
and Presburger chronology. A literal RRR completion closes the pose. Its exact
input/output/XOR counts are6r,6r+4,10r+4. It needs an increasing prepared rail
and is NOT a renewable finite-seed construction. This is the current concrete
hidden-state residual, rather than a longer bounded primitive inventory.

### Axial positive component and cycle-geometry filters (06:18 UTC)

`decorated_axial_hairpin.md` is independently signed at all depths. It uses the
known eight-step outward sweep and a uniquely selected eight-step return to
transfer an entire black row across two unchanged alternating rails. Exact
input/output/XOR counts are4r+2,4r+3,4r+7. It is prepared, interior-root and
not renewable. Its directly matched same-strip half-turn inverse has the wrong
pose sector.

`recursive_cycle_geometry.md` is also signed. Every fixed growing hidden-label
unit-spatial root must balance all reachable simple-cycle displacement vectors,
and these vectors cannot all lie on one oblique line. Opposing axial directions
or genuinely two-dimensional cycle geometry remain. These filters explain why
the local positive components cannot be promoted to a root without new machinery.

### Capped axial transport and its exact eventual capture (06:44 UTC)

`axial_domino_transport.md` now gives two independently signed all-r closed
excursions. G_r has length8r+8 and moves a distant vertical black domino to
the near end while restoring every other cell; its COMPLETE XOR is4. H_r
has length8r+12 and adds four cells at the two ends of a prepared rod. Neither
is renewal. The full actual continuation of H_r from its exact minimum seed
J_r is now independently certified in `domino_growth_capture.md`: for every
r>=20, standard104 capture occurs at time60r+777, pose(2r+2,7,N), drift(-2,2).
The proof checks every read for all parameters and all future tail periods.

The next constructive obligation is a genuinely new bulk/phase mechanism.
`period_two_rail_conversion_filter.md` records the row-charge consequence
that creating/erasing alternating rows in a period-two finite-interface front
requires full drift divisible by8. This analytic corollary is independently signed;
no prepared alternating-rail converter or expanding frame has been built.

### Exact expanding frame, but no renewable pose (07:34 UTC)

`chamfered_frame_nearrenewal.md` now gives an independently signed two-parameter
complete-board expansion: W_(r,k)=((LRRL)^r (RL)^k R)^4 maps I_(r,k) exactly to
I_(r,k+1)+(0,1). Its pose is wrong by the invariant sector, including all natural
rotated starts. The positive field identity is not an autonomous renewal.

`chamfered_capture.md` separately certifies the actual minimum seeds for every
r,k>=10: standard104 capture at36r+8k+291, pose(2r+1,4,N), drift(-2,2). Both
results are audit KN. Changed or multi-phase/multi-read assemblies remain open.
