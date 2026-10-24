# Local energy ranks for the five-macro branch

## Scope

The target is the large cyclic component of the exact finite-word graph in
which no two consecutive length-ten highway-defect events occur. The graph
and its five marker-to-marker words are established by the independent files
in `../factor_language/`. This note does not prove capture of that component,
and does not prove the full highway conjecture.

We used 995 actual 149-turn marker histories, rather than mixing states of a
minimized automaton. Combining a history with its next macro eliminates 45
edges by direct contradictory cell reads. The remaining 2,702 edges have 166
different local color contexts for the energy change. Unknown colors are
allowed to vary freely. Thus an inequality verified on each context applies
to every actual trajectory using that edge.

## The proposed rank

For a finite black set B, let

    E(B) = sum_z w(pattern of B on z + {0,1,2}^2).

The all-white pattern has weight zero. Every other weight is nonnegative.
Consequently E(B) is finite and nonnegative. In the first ansatz, weights are
constant under quarter rotations, leaving 139 variables.

For each port history s, allow an arbitrary real constant phi(s). The desired
edge inequalities are

    E(B_after) - E(B_before) + phi(target) - phi(source) <= -cost(edge).

We considered three sufficient nonnegative costs:

| Cost | C | V | U | Q | B |
|---|---:|---:|---:|---:|---:|
| Every macro | 1 | 1 | 1 | 1 | 1 |
| Fold macros | 1 | 0 | 0 | 1 | 1 |
| Defect events | 0 | 1 | 0 | 1 | 0 |

Every-macro decrease would directly exclude an infinite path. Fold decrease
would force an eventual U/V tail, which the separate exact U/V fuel theorem
excludes on finite support. Defect-event decrease would force finitely many
length-ten defects; the existing ten-factor capture theorem would then apply.

## Exact negative result for the first ansatz

No such nonnegative, quarter-rotation-invariant 3-by-3 pattern energy plus
arbitrary 995-port potential can satisfy the context-wise inequalities for
**any nonzero nonnegative cost assigned by macro type**.

This is now an exact finite certificate, rather than only floating-point LP
infeasibility. The certificate uses 159 explicit context assignments from the
search. Its strictly positive integer multipliers have these properties:

* Their aggregate coefficient of every port potential is exactly zero.
* Their aggregate coefficient of every nonnegative pattern weight is
  nonnegative.
* Their total multiplier on each of C, V, U, Q and B is strictly positive.

Multiplying and adding the requested edge inequalities would therefore give
a nonnegative number bounded above by a strictly negative number. This is a
contradiction. The independent verifier rebuilds the supported pattern-count
changes directly from the cell sets and does not import the LP row builder.

The certificate and verifier are:

* `../wake_clock/fold_farkas_certificate.json`
* `../wake_clock/verify_fold_farkas.py`
* `../wake_clock/fold_farkas_verification.json`

This result excludes this particular finite local rank. It does not exclude
larger patches, signed energies that remain bounded below, stronger history
contexts, or other structural arguments.

## Sector-dependent extension

The ant preserves sigma = (-1)^(heading + x + y), with N,E,S,W numbered
0,1,2,3. A more general global energy uses a weight for both a patch and the
phase sigma*(-1)^(patch-origin x + patch-origin y). Quarter rotation changes
both the pattern and the phase. Imposing covariance under that joint action
leaves 271 nonzero pattern classes.

At a normalized port with head (0,0), heading N, sigma is +1. Therefore the
oracle uses phase (-1)^(patch-origin x + patch-origin y). This construction
is compatible with translating and rotating any physical port to the
normalized frame. It removes an unnecessary symmetry restriction from the
first ansatz.

For defect-event cost, exact finite-context separation generated 6,268
context cuts. A simplex solve then reached its 30-second limit. A subsequent
interior-point solve reported infeasibility on the same explicit system.
Unless a rational dual certificate is supplied, that status is **numerical
infeasibility**, not an exact exclusion theorem. The earlier sector run with
positive cost on every macro was interrupted after 25 separation rounds;
its nonconvergence is not an infeasibility result.

The result and compact cut set are `sector_compact_event_result.json` and
`sector_compact_event_cuts.json.gz`.

The exact ordinary-rank dual was also tested against the 271 sector columns.
It has negative aggregate coefficients on 104 of them, so that certificate
does not establish sector infeasibility. This reuse check is exact and is
saved as `../wake_clock/fold_farkas_sector_reuse_check.json`.

## Bounded head correction

A final targeted extension adds

    P(B,p,h) = sum_{r in {-1,0,1}^2} a_r 1_B(p + Rot_h(r)),

where all nine coefficients may have either sign. This is uniformly bounded
in absolute value by sum_r |a_r|, independently of B. Thus E+P+phi remains
bounded below. Its macro change adds only unary color factors, and does not
increase the exact oracle's elimination width. The radius-one correction is
not already fixed by the 149-turn port history: each history leaves at least
one of those nine bits unknown.

The radius-one sector-dependent defect-event search generated 7,821 context
cuts. At separation round 11, the interior-point LP solver reported
infeasibility. This is again **numerical infeasibility**: no rational dual
certificate was recovered for the enlarged ansatz. No valid rank was found.
The complete compact system is saved in
`head1_sector_compact_event_cuts.json.gz`, with the final solver status in
`head1_sector_compact_event_result.json`.

## Search and verification method

For each candidate set of weights, finite binary variable elimination
maximizes the energy change over every unknown bit assignment in a context.
The largest conditioned elimination width is seven. Returned maximizing
assignments are re-evaluated directly. Floating weights give a floating
evaluation of a complete finite maximization problem; integer weights give
exact arithmetic, with an explicit overflow bound.

The LP has one auxiliary upper-bound variable z_c per context. Its constraints
are a_witness*w <= z_c and z_c+phi(target)-phi(source) <= -cost(edge).
This avoids repeating a local pattern-count row for many graph edges.
Every actual inequality is checked again against the exact maximizer before
a candidate can be accepted. A successful candidate is scaled, rounded to
integer coefficients, and independently re-maximized before it is called a
certificate. No candidate has passed that final acceptance step as of this
note's initial writing.

Reproduction scripts:

* `local_energy_search.py`: initial unconstrained-neighborhood discovery.
* `energy_cegis.py`: fast heuristic separator for that preliminary ansatz.
* `conditioned_rank.py`: original explicit-edge LP and exact separator.
* `conditioned_rank_compact.py`: equivalent compact LP, sector and head options.
* `../factor_language/exact_local_energy.py`: exact finite-context oracle.
* `../factor_language/conditioned_macro_contexts.py`: geometric context export.

The initial 34,941 explicit edge cuts are stored once in
`conditioned_rank_cuts.json.gz`. The ordinary strict and fold result files
both reference that shared compressed file.

## Separate finite periodic-word audit

`search_macro_cycles.py 12` enumerated physically consistent graph cycles
through twelve macros. It visited 1,583,401 feasible-prefix nodes. Exactly
801 cyclic macro words passed the infinite periodic-background revisit test;
all are U/V mixtures. Their required initial-black ray count is 5 times the
number of U macros plus 2 times the number of V macros. No cycle containing
C, Q or B passed the test within this finite depth.

The 801 survivors are precisely the binary necklaces in U and V of lengths
one through twelve. This is a finite audit, not an exclusion of fold-containing
periods of arbitrary length, and not an exclusion of aperiodic paths. The
data are saved in `macro_cycles_12.json`.
