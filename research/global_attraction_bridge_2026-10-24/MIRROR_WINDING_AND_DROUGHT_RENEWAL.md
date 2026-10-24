# Pointwise mirror winding conservation and an actual drought-renewal test

24 October 2026. Author proof and exact controls; independent audit requested.

## Result and scope

For every finite BLACK board in the classical initial-E sector, resolve its frozen flipping-mirror pairings into oriented circuits. At every unit plaquette center, the **sum of the circuits' signed winding numbers is exactly the checkerboard baseline value**: -1 at even lower-left corners and 0 at odd ones. This remains true after every actual ant update.

This is stronger spatial information than a total cycle count, but it is not a decreasing resource. It gives an exact reconnection classification and an exact area ledger. The proposed monotone consequence fails on a genuine completed pristine record drought in the 22-cell MT control: positive winding area increases from 137 to 139 over 294 updates, before canonical capture. Its 45 opposite-orientation splits create 99 area units, while 40 opposite-orientation merges cancel 97. No input field or old archive is discarded.

The frozen-loop transposition representation and non-LIFO controls are already retained in `first_principles_2026-10-21/ant_rethink/switching_geometry/tait_cursor_and_loop_surgery.md`. This note does not claim those as new. The pointwise winding formulation was not found explicitly there; no historical novelty claim is made. It remains a finite-board invariant and a precisely scoped failed monotonicity attempt, not a proof of renewal control or attraction.

## 1. Exact frozen pairing model

Coordinates and headings are N=0, E=1, S=2, W=3. The ant starts at `(0,0),E`. WHITE turns R, BLACK turns L, then the physical ant flips the cell and moves.

For a **frozen** board B, define `F_B(p,h)` by the same turn and move, but with no flip. There are two admissible incoming states at each cell: E/W at even cells and N/S at odd cells. A mirror pairs the four physical edge ends in one of the two noncrossing quarter-turn pairings. Rounding each vertex inside a disk of radius less than 1/4 gives disjoint oriented embedded circles, possibly with several circles touching the same original grid vertex before rounding.

The baseline empty board has clockwise unit-square circuits around precisely the plaquettes with even lower-left corners. Each admissible state lies on one four-step baseline circuit.

For a finite B, let U be the union of the baseline circuits through the two admissible states of every black cell. Then `|U|<=8|B|`. At each changed cell the two outgoing images are swapped. Hence `F_B` maps U to itself and equals the baseline map on its complement. All changed circuits are finite and contained in U. If a current cursor state is outside U, its circuit is an untouched four-step baseline circuit; it may be added to U without changing any relative quantity below.

This proves finiteness without truncating the plane or assuming that the cursor's active component is the whole relevant field.

## 2. Pointwise winding theorem

For a frozen circuit C and a plaquette center z, let `w_C(z)` be its signed winding number, positive counterclockwise. Rounding vertices does not change it because all rounding disks avoid all plaquette centers. Every rounded circuit is Jordan, so its nonzero winding values are all +1 or all -1.

At each physical cell, the two admissible states use exactly its two allowed outgoing unit edges, independently of the current mirror sign. A flip only exchanges which incoming state uses which outgoing edge. Thus a flip preserves the entire oriented unit-edge 1-chain of the affected circuit family. Winding is additive on this chain. It follows, for every z, that the total winding of that family is unchanged.

Only finitely many baseline circuits are altered. Therefore the global sum at z is well-defined by replacing that finite family in the baseline, and

`sum_C w_C(i+1/2,j+1/2) = -1 if i+j is even, and 0 otherwise.`

Equivalently, the number of clockwise circuit interiors containing each center exceeds the number of counterclockwise interiors by exactly its checkerboard indicator. This is a pointwise relative identity, not an infinite subtraction of two undefined totals.

The theorem is stated for finite perturbations only. Arbitrary infinite mirror backgrounds can have open trajectories, and no winding sum for such trajectories is asserted.

## 3. Exact local reconnection classification

At a read cell p, write `a=(p,h)` and `b=(p,h+2)`. The flip swaps their successor images. If a and b are on different frozen circuits, they merge; if on one circuit, it splits. The true ant moves to `F_B(a)`, using the old board, and the new frozen pairing is evaluated after the flip. Static circuits are not being mistaken for the physical trajectory.

Let D(C) be the set of plaquette centers with nonzero winding in C. For the pair of circuits on the two-circuit side of a surgery:

* If their orientations agree, their D sets are disjoint. The one-circuit D set is their union, with the same orientation.
* If their orientations are opposite, one D set is strictly contained in the other. The one-circuit D set is their difference and has the larger domain's orientation.

Proof: pointwise conservation says that the one circuit's winding function is the sum of the two. The one circuit can have only values 0 and one fixed sign. Equal-sign overlapping domains would create ±2. Opposite-sign nonnested domains would create both +1 and -1. Equality of opposite domains would leave an empty one-circuit winding domain. Zero winding on every unit face would force its closed grid-edge 1-chain to be zero, whereas this nonempty circuit uses each physical edge in only its allowed direction, with no reverse-edge cancellation. Thus the claimed alternatives are exhaustive at plaquette centers.

The domains here are sets of plaquette centers. No statement about microscopic regions inside the changed vertex disk is needed. Spatial nesting in this one surgery is not chronological LIFO ordering: old circuits can be reattached non-LIFO as in the retained actual controls.

## 4. A finite defect-area quantity and its exact update

Define the integer signed grid area

`A(C) = sum_z w_C(z) = (1/2) sum_edges (x*y_next-x_next*y)`.

For a finite BLACK board define

`P(B) = sum_C max(A(C),0)`.

Only finitely many counterclockwise circuits exist, so P is finite. It counts counterclockwise enclosed plaquettes with multiplicity, not a union area and not a count of BLACK cells. In any finite affected baseline universe U,

`sum_changed |A(C)| - |U|/4 = 2 P(B)`.

The formula is independent of enlarging U by untouched baseline circuits. Thus it also describes a renormalized absolute winding-area excess.

The complete surgery ledger is:

1. Equal-orientation merge or split: P does not change.
2. Opposite-orientation merge of circuits with absolute areas a and b: `Delta P=-min(a,b)`.
3. The inverse opposite-orientation split: `Delta P=+min(a,b)` for the two new absolute areas.

These are exact identities, not estimates. In particular a new counterclockwise region has compensating clockwise winding in precisely the same plaquettes. That compensation can come from an expanding current circuit; it need not be an original black input, a permanent output, or a new independent resource. Nothing in the identity prevents cancellation and later recreation.

## 5. Literal controls retain the entire field

### Blank input

The complete empty-seed orbit is replayed for 10,081 reads. Selected P values are:

* cuts 0,8,52: 0;
* first completed union-record gap longer than 104, cuts 355 to 509: 2 to 0;
* certified canonical cuts 9977 and 10081: 220 and 222.

The cut-9977 to cut-10081 comparison must not be interpreted as an indefinitely repeated full-field area increment. These are two actual cuts, and old stationary field can still affect frozen connectivity without being physically read. Their all-future turn continuation is verified separately against the complete board.

### MT with n=100

The original 22-cell seed is taken literally from the signed `SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json`, not manufactured at an interior cut. The full board is replayed through cut 109168 and its infinite standard tail is checked against every retained BLACK cell.

Record events use the rectangle containing the **entire initial seed and all earlier head positions**. Thus prepared remote cells cannot be hidden outside the record hull. The first completed gap longer than 104 is exactly

`[33345,33639]`, length 294.

At its endpoints:

* complete BLACK masses are 3101 and 3125;
* P is 137 and 139;
* all 104 possible canonical phases are rejected by the actual future at cut 33639, each within 22 reads. Hence no point of this gap had entered an all-future canonical tail.

All 294 actual flips are classified using their complete frozen circuits. There are 117 equal-orientation merges, 92 equal-orientation splits, 45 opposite-orientation splits, and 40 opposite-orientation merges. The latter two classes create 99 and cancel 97 positive area units, respectively. Their net is exactly +2. The first positive event is the R read at tick 33347, cell `(421,442)`: a circuit of area -11 splits into areas -13 and +2.

The changed positive-winding multiplicity is supported on 14 plaquettes: eight gain one and six lose one. These are not asserted permanent defects. The same completed gap shows that even the sign-sensitive area excess is not a nonincreasing pre-capture record-drought potential.

For context only, the much longer completed gap `[40071,109168]` has P values 170 and 504. It ends after certified capture, so it is **not** used as a pre-capture monotonicity counterexample. No all-n formula for P is inferred from other MT samples.

## 6. What this does and does not constrain

The new exact restriction is geometric: a proposed finite mirror reconnection cannot create an uncompensated winding domain, merge overlapping equal-sign domains, or merge nonnested opposite-sign domains. A putative renewal construction can be tested against these whole-domain conditions.

The failed stronger claim was concrete: P cannot increase across a completed, still-noncanonical, pristine union-record gap longer than 104. The literal MT gap refutes it. The weaker signed winding theorem survives because all gains are compensated pointwise.

No injective charge of compensating domains to original inputs, forever-abandoned cells, or distinct outstanding lifetimes is established. Such a charge would need a separate chronology argument surviving the 99/97 reuse in this single gap. The frozen pairing domains depend on the whole current field, not only a local guard. This package therefore supplies a sound local-to-global identity and a bounded exact falsifier of its simplest renewal use, not global attraction.

## Reproduction and audit boundary

`mirror_pairing_geometry.py` constructs complete finite affected universes and all their circuits, with exact integer winding at every enclosed plaquette. `check_mirror_winding_renewal.py` checks all 512 three-by-three finite boards and all 4608 one-cell surgeries on them, then 119249 actual whole-field updates in the two named controls. The stored fields, record lists, phase rejections and 294-step surgery ledger are in `MIRROR_WINDING_RENEWAL_CHECKED.json`.

The small finite cases test the implementation, not the universal proof's coverage. The universal pointwise and surgery statements are proved above. The named MT history does not establish an all-parameter geometric classification or arbitrarily many completed droughts.
