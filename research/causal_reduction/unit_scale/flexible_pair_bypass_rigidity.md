# Minimal bypass rigidity with arbitrarily changing pair alignment

23 October 2026, 14:23 UTC. Author semantic proof plus solver-independent RUP replay; independent semantic review requested. This removes the fixed-pair-alignment assumption of the signed earlier theorem. It does not enlarge the bypass palette.

## 1. Architecture

Use the fixed inverse104 coarse path V from short_refinement_scaffold_inputs.json, with incoming W, drift(-2,-2), and charge -12 per period. At ANY coarse index i, a nonidentity tile may replace the two turns at i,i+1 by either of the two signed minimal ten-read endpoint-bypass words in minimal_pair_bypass_geometry.json. Nonidentity tiles may not overlap. Every uncovered coarse index contributes its unchanged one-read turn.

Thus the pairing alignment can change at every occurrence. There is no stationary equality, global even/odd tiling, controller, or prescribed initial-color profile. The fine path preserves the exact coarse pose at every tile boundary but avoids the intermediate coarse pose inside each bypass. Every choice may depend on all preceding history.

Then every legal one-sided infinite schedule in this architecture has NO nonidentity tile whose start index is at least312. In particular it cannot run from a finite initial black seed, because its remaining ordinary V tail consumes12 black cells per104 reads.

## 2. Derived finite overlap and exact boundary coverage

For each of104 possible coarse start phases, trace its unchanged read and both two-turn bypasses, including the phase103 pair crossing into the next period. On every full-drift orbit (x-y,x mod2), the possible longitudinal levels floor(x/2) span at most THREE. There are30 potential orbits. Thus same-cell histories involve periods in an index interval of length at most four; the central period's full radius-three neighborhood consists of seven periods. The exact per-orbit extrema are retained in flexible.architecture.json.

The finite clause system has coarse indices0,...,727. Nonidentity tiles are allowed to start at EVERY index -1,...,727. The optional tile at -1 covers the left boundary index0, and the optional tile at727 extends across the right boundary. There is no spurious identity read at -1 or728. These two explicit optional crossing tiles are necessary: simply cutting a changing tiling at a prescribed period boundary would otherwise omit an actual half-tile.

For each start i there are two choice bits x_(i,0),x_(i,1), at most one true, and their OR b_i. Adjacent b_i,b_(i+1) cannot both hold. For each internal index0<=i<=727, its monomer bit satisfies

    m_i <=> not b_(i-1) AND not b_i.

Consequently every assignment is an exact continuous tiling of all internal coarse indices, with optional complete boundary-crossing tiles. Conversely every actual global schedule restricts to such an assignment.

At least one bypass with start312,...,415 is required, exactly the central period. ALL274 possible read cells have unconstrained initial colors; no final color is constrained.

## 3. Literal chronology circuit

Possible reads are grouped by their ACTUAL physical cell and ordered by (coarse tile start, local read index, turn). For one start, alternative tiles and its monomer are mutually exclusive. Across starts, nonoverlap makes this lexicographic order exactly the physical read order. Simultaneous equal-index alternative events are harmless because only one alternative is active.

An event's activity is the OR of its contributing tile choices. An active R requires current white, an active L requires current black, and its successor color is current XOR activity. These are ordinary truth-table CNF clauses. No approximate clock, aggregate flow, periodic read folding, or finite visit cap is used.

The resulting instance has30889 variables and104237 clauses. It is UNSAT. A separate monotone RUP producer emits764 additions; the retained independent generic checker validates every addition with no RAT or deletion steps.

CNF SHA256: afcdd55569dfaefa309321c566f89ea0f2c1705f28ac3194bf2c8c1c87b19cc3
RUP SHA256: 88b9b970f61386b160697806820c37494d6262241f0c8a6fa32778a2940ed92d
Source SHA256: 4f976662470e2ab15509fa56f4e0ae7cc24090185b5726c6d3629a37d53805d9

## 4. Infinite-schedule consequence

Suppose a bypass starts at any coarse index i>=312. Shift the seven-period window by104r, where r=floor(i/104)-3>=0. Its actual tiling, including either crossing boundary tile when present, is one of the finite assignments. The actual entry colors realize every finite read, regardless of what happened before the window. The chosen bypass lies in the central period, contradicting UNSAT. No hypothesis about fresh white input or untouched inherited memory is needed.

Once all late tiles are monomers, the remaining actual path is V repeated. Its turn excess is -12 per period, so the total number of black cells decreases by12 per period. This is impossible indefinitely from a finite black field. Arbitrary infinite prepared input is not thereby excluded for the identity tail.

The signed time-reversal conjugacy separately gives a FORWARD-H corollary: every infinite schedule using these same minimal endpoint bypasses, now with arbitrarily changing tilings of H, is eventually the ordinary H tail. Reverse a sufficiently interior finite window, use the exact inverse-pose map and the palette's minimality, and absorb the cyclic phase shift in a finite prefix. No exact forward index312 is claimed. This says eventual standard behavior within this architecture, not nonexistence of its forward finite-seed paths.

## 5. Controls and limits

check_flexible_pair_controls.py compares35 complete physical tilings with direct literal traces and the entire Boolean event recurrence, including both optional boundary crossings, sparse/dense random choices and changing parity. Every physical event order agrees and every failed demand clause matches literal failure. The all-monomer positive is inverse104^7, length728, minimum input97; it satisfies the circuit when the central-bypass clause is omitted.

Files: check_pair_bypass_flexible_tiling.py, check_flexible_pair_controls.py, pair_bypass_flexible_tiling/flexible.{architecture.json,cnf,rup,result.json}, controls.json.

No arbitrary two-turn image, larger bypass, heading-changing tile, overlapping replacement, changed coarse path, or nonperiodic coarse trajectory is covered. This is a derived finite local certificate for one analytically minimal geometric palette, not a period or length scan and not a global highway proof.
