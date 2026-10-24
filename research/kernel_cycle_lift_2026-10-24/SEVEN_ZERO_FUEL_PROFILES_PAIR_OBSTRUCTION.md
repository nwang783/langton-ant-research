# No pair of the seven residual cap-six zero-fuel profiles has a full-board lift

24 October 2026. Exact targeted physical-composition certificate. The seven
candidate returns below are each individually realized from a finite board.
ALL49 ordered immediate pairs are incompatible with one unchanged complete
initial board. The fuel rank and exhaustive profile-filter coverage are
separate dependencies owned by the kernel analysis, not inferred from this test.

## 1. The supplied seven candidates

The compact source is
`../reframe_finite_seed_2026-10-24/cap6_seven_zero_fuel_profiles.json`.
Its seven exact ordered full-component paths are

    78       RRRRLRL        seed {(-1,1)}
    4554     RRRRLRLL       seed {(-2,1),(-1,1)}
    4555     RRRRLRLL       seed {(-2,-1),(-2,1),(-1,1)}
    4866     RRRRLRRLL      seed {(0,1),(0,2)}
    4895     RRRRLRLRL      seed {(-2,2),(-1,1)}
    5169     RRRRLRLRL      seed {(-2,-1),(-2,2),(-1,1)}
    33389    RRRRLRRLRL     seed {(0,1),(1,2)}.

Every control starts at head(0,0),N with empty complete active w component
in fixed sector1. Every fine-cut active component matches the supplied
ordered path and has at most6 edges; the final active component is empty.
The controls do not add, erase, reposition or translate any mid-run cell.
All outputs, residual input edges and older passive components stay present.

The separate author rank assigns weight1 to singleton components and corner
dimers, weight2 to straight dimers, and0 to other types. After independent
physical/output-trap filters it is reported nonincreasing on93 candidates,
strictly decreasing on86, with exactly these seven zero-drop paths. This
note does NOT take LP feasibility or that reported coverage as proof. It
proves the missing spatial obstruction for the seven specified paths.

## 2. Exact arbitrary-exterior pair theorem

**Theorem.** No ordered pair from the seven supplied paths can be realized by
one complete finite initial black board, with the physical head/heading
continued between the two returns and every proposed complete active
component retained. This includes self-pairs and all mixed pairs. The
compatible-pair graph has NO edges, not merely no detected short cycles.

**Proof method.** Use the independently signed complete-port/read-parity
criterion from TWO_CLEAN_RETURNS_OBSTRUCTION.md Section3. A proposed complete
active component C_t requires C_t black and every other incident port of
its vertices OR the cursor white, including an isolated cursor. Pull each
required current bit back to the initial board through the parity of the
actual earlier reads at the same physical cell. Opposite pulled-back bits
at one cell are an immutable contradiction for EVERY board; unread exterior
cells cannot repair it.

The physical pose is advanced at EVERY actual update. The second return's
local profile is rotated and translated by that actual pose, not put at a
fresh favorable placement. The checker visits every port at every fine cut,
including the seam and final empty cut.

For all49 pairs it obtains such a contradiction. The following compact rows
summarize the complete witness matrix; full per-cell bits, earlier read
parities and both cut owners are in the certificate:

* First78: cell(-1,0), cuts1 and11, for EVERY second profile.
* First4554: contradiction at second return's cut1 (global9), at cell
  (-1,-1) except second4866/33389, which use(-2,-1).
* First4555: second return's cut1 (global9), at(-2,-1) except second4866
  uses(-2,-2) and second33389 uses(-3,-2).
* First4866: second return's cut1 (global10), at(-2,1) for second78/4895/5169,
  at(-2,0) for second4554/4555, and at(-2,2) for second4866/33389.
* First4895 or5169: cell(-2,1), cuts1 and13, for EVERY second profile.
* First33389: cell(0,2), cuts1 and14, for EVERY second profile.

Each row covers exactly seven second profiles. Each witness consists of two
opposite required INITIAL colors at the displayed physical cell. Therefore
all49 pairs are excluded. QED.

Some conflicts expose a surviving R-born output edge; others already expose
incompatible placement of initial unread module members at the first update
of the second path. Neither kind is a mere abstract shape/type mismatch.
They concern the actual complete field at fixed coordinates and actual
current lifetimes. The R/L word alone need not yet have failed.

## 3. What the conditional integration would prove

Suppose separately verified kernel coverage ensures every sustained-cap6
trajectory reaches infinitely many empty-active cuts, and every full return
is either physically impossible, output-trapped, or one of the93 ranked
profiles. At empty cuts the sum of the stated nonnegative integer weights
over all complete passive components is finite. Larger nonimportable
components may remain present with weight0; they are not deleted.

Nonincrease and strict unit drops permit only finitely many strict-drop
returns. Any hypothetical sustained-cap6 tail would therefore eventually
have consecutive returns drawn only from the seven zero-drop paths. The
pair theorem forbids even two such returns. This would close sustained-cap6
only AFTER coverage, rank and trap dependencies are independently checked.

This is a small-cap global necessity, not a proof of general bounded-active
attraction, standard104 classification or universal capture. The conditional
proof must not be promoted before those separate dependencies pass audit.

## 4. Auditable artifacts

`finite_component_profile_lift.py` is the pure helper implementing the already
signed finite full-profile realization criterion. Consistent finite paths
construct the minimal actual finite seed and replay the complete field, with
whole-component import and literal birth/consumption provenance. Inconsistent
paths return the two exact initial-bit requirements.

`check_seven_cap6_profiles.py` reproduces all seven individual boards and all
49 ordered pair tests. `seven_cap6_profiles_certificate.json` retains all
single traces, all49 explicit contradictions, the empty compatibility edge
set, and a source hash. No large all-return enumeration, generic board scan,
mid-run additions or moved archives are used. Because there is no compatible
pair at all, no pairwise-compatible cycle is being mistaken for a full
spatially composable infinite orbit.
