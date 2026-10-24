# Langton's ant: first-principles continuation, 21 October 2026

## Status

The full finite-support highway conjecture is not proved in this record.
There is no counterexample and no proof of undecidability or independence.
Failure of the routes tested here is not an impossibility theorem.

The work below concerns the classical rule: turn right on white, turn left
on black, toggle the current cell, then move one unit. The initial black
set is finite. All claims about total black count include the entire board,
including distant old cells.

The strongest completed result is a uniform, explicit upper bound on the
frequency of small black counts. It is a global statement about every finite
input, but it does not establish eventual highway formation. The proofs were
reviewed independently within this investigation. They have not received
external mathematical review or proof-assistant verification. No novelty or
priority claim is made.

## 1. Explicit global occupation theorem

Let M_t be the total number of black cells. Define

    D_0=1,  D_K=2K D_(K-1)+1,
    C_K=2(K+1)9^K.

For every finite initial field, every starting time s, every integer K>=0,
and every integer N>=1,

    #{t in [s,s+N): M_t<=K}
      <= min(N, C_K N^(1-1/D_K)).

Thus each fixed small-count set has uniformly vanishing occupation density.
The associated mean bound is

    (1/N) sum_(t=s)^(s+N-1) M_t
      >= (K+1)(1-C_K N^(-1/D_K)).

In particular, the mean black count diverges uniformly as the interval
length grows. This permits infinitely many sparse returns to small count.

The proof has three main steps. A complete centered finite state cannot
repeat. There are finitely many small states whose black cells are all near
the ant. At every other small state, a sufficiently distant black cell can
be removed in a comparison trajectory for a fixed interval during which
it cannot be read. The comparison lowers the black count by one. An
induction over K gives the bound.

Complete proof: `constructive_alternatives/explicit_low_mass_occupation_bound.md`.
An independent compactness and invariant-measure proof of the qualitative
conclusion is in `switching_geometry/bounded_mass_theorem.md`.
The final independent mathematical audit is `root/final_proof_audit.md`.
It found no substantive gap in the occupation, signed-cut, mass-ceiling,
or bounded-retreat proofs. Its suggested clarification of the clock-count
sign convention has been applied.

## 2. Exact displacement and mass-ceiling bounds

Jillhewar's existing signed-column potentials imply, for any two times s,t,

    2 max(|x_t-x_s|-1,0) <= |B_s symmetric_difference B_t| <= M_s+M_t,

and the same statement for y. Consequently

    ||p_t-p_s||_infinity <= (M_s+M_t)/2+1.

All ant positions in an interval during which M_t<=K therefore fit in one
square with K+2 lattice cells per side. Applying Ke's existing square escape
clock yields the following explicit consequence:

    Every state with M_0<=K exceeds K by some time
    1<=t<=U(K),
    U(K)=(39*3^K-2K^2-12K-21)/2.

No bound on the initial cells' coordinates or diameter is assumed.
The two-endpoint use of the signed potentials and this application of the
escape clock were derived and checked here. The underlying potentials and
clock are prior work, cited in the full note.

Complete proof, all eight local cut equations, and limitations:
`constructive_alternatives/signed_cut_and_explicit_mass_bound.md`.

## 3. Exact small mass-ceiling times

Let T(K) be the maximum first time the black count exceeds K, over every
initial state with at most K black cells and arbitrary cell coordinates.
The completed exhaustive searches give:

| K | T(K) | Root search nodes |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 3 | 4 |
| 2 | 5 | 13 |
| 3 | 7 | 41 |
| 4 | 13 | 143 |
| 5 | 15 | 452 |
| 6 | 25 | 1,548 |
| 7 | 35 | 5,288 |
| 8 | 45 | 18,885 |
| 9 | 55 | 70,023 |
| 10 | 65 | 270,104 |
| 11 | 75 | 1,073,808 |
| 12 | 87 | 4,398,716 |
| 13 | 123 | 18,429,288 |
| 14 | 137 | 78,832,244 |
| 15 | 151 | 342,849,656 |

A physical finite turn word is realizable below ceiling K exactly when
successive reads at each cell alternate, and

    number_of_first_L_cells + max_prefix(#R-#L) <= K.

The maximum includes the empty prefix. The first-L cells form the unique
minimal initial seed on the read footprint. Additional initially black
cells outside that footprint only raise every black count. This proves
that the enumeration covers all coordinates, rather than a fixed box.

Every retained maximum-length word was independently replayed from its
literal seed. Its actual next update exceeds K. A separate implementation
that fixes the initial black count agrees at K=6,8,10,12. No time or node
limit was counted as completed coverage.

Code and evidence: `root/bounded_mass_tree.cpp`, `root/mass_bound_*.json`,
`root/audit_mass_witnesses.py`, `root/mass_witness_audit.json`, and
`switching_geometry/mass_ceiling_search.py` with its retained JSON records.

## 4. Sufficient geometric conditions for periodicity

Two complete conditional arguments were established.

* If retreat is bounded in two independent linear coordinates, then all
  previously written black cells that can still affect the future lie in
  a fixed finite window about the ant. Repetition of a reduced state then
  forces eventual periodicity up to nonzero translation.
* If the ant escapes in one direction and all sufficiently far cuts have
  uniformly bounded complete crossing histories and crossing-height range,
  then two equal crossing histories can be spliced. Determinism forces an
  eventual translation period. This gives periodicity under confinement to
  a fixed non-axis strip or a finite union of such strips.

Neither argument proves its geometric hypothesis for arbitrary finite
inputs. Neither classifies every periodic trace as the standard highway.

Full proofs: `constructive_alternatives/bounded_directional_retreat.md` and
`constructive_alternatives/oblique_strip_pumping.md`.

## 5. Attempts to close the remaining gap

### Exact graph dynamics

The Tait graph cursor has a direct compressed rule. It inserts r absent
edges, then deletes and crosses the first present edge, with
r in {0,1,2,4}. It never immediately backtracks at this compressed level.
The exact local check covers every arrival port and edge mask.

This does not give an abelian process, a last-in-first-out loop stack, or
permanently frozen loops. Small literal blank-start witnesses disprove
those simplifications. The resulting argument recovers the old no-corners
restriction on recurrent cells, without proving transience.

See `switching_geometry/tait_cursor_and_loop_surgery.md`.

A further exact return-map test retains boundary colors, every frozen
entrance-to-exit connection and path length, every interior loop length
and orientation, and total black count. Even this summary is insufficient:
two explicit five-by-five boards with two black cells give different actual
first exits after 35 and 18 updates. Their ordered encounters with physical
switches differ. The full witness and verifier are in
`switching_geometry/finite_boundary_summary_obstruction.md` and
`switching_geometry/verify_fixed_boundary.py`. This excludes that particular
summary, not a richer chronological return map.

### Boundary-count candidate disproved

The proposed global inequality M-2 Delta_A<=2m+1 for a completed fresh cap
is false. One initial black cell at (-2,16), with ant (0,0),N, gives
M=8 and Delta_A=2 after 7,849 updates at the appropriate diagonal cap.
A separate one-black example gives four consecutive top cells and
Delta_A=0, so a simple endpoint-of-run correction does not repair it.
Both were independently replayed. These are counterexamples to a proposed
lemma, not counterexamples to the highway conjecture.

### Feedback attempts

The 22 first-hit phases of a single marker on the standard highway were
checked with complete infinite-tail and old-wake guards. Only phase 72
reverses directly. Paired reversals can cancel lane displacement, defeating
a simple monotone-lane argument.

Fourteen selected paired-reversal inputs and all 359 selected single-cell
corrections near one source collision were exactly captured by a highway.
Six corrections revisited an old marker; independent full-seed replays
confirmed that the surrounding read field did not regenerate the original
scattering response. These are finite certified families, not a universal
perturbation theorem.

See `defect_dynamics/README.md` and its code and JSON evidence.

### Direct periodic-word synthesis

A direct finite-support chronology formulation orders visits in each
translation class from the leading end and requires R,L alternation.
It reconstructs a finite initial seed and supports an independent infinite
tail check. It is described in `defect_dynamics/direct_periodic_chronology.md`.

The fixed standard 104-word passes. The fixed axial T24 word fails its
first-read conditions. The completed bounded axial solver runs are recorded
with their literal SAT/UNSAT/UNKNOWN statuses. Timeouts are not exclusions.
No alternative periodic word was found. The separate root connector search
also found none in its stated restricted finite word family.

### Endpoint conditions do not determine a physical trajectory

At fixed pose (0,0),E, the four-cell patterns

    {(-n,-n),(-n,n+1),(n+1,-n),(n+1,n+1)}

pass all of the inspected signed-cut constraints and all-center diagonal
clock inequalities for expansion to larger n. Even the separate projected
clock-gain counts admit nonnegative integer assignments. These are only
endpoint models. A subsequent all-size argument in
`defect_dynamics/four_corner_family_exclusion.md` excludes every proposed
transition B_n to B_m at the stated pose, and certifies standard-highway
capture for every member of this particular family. For n>=21 all four
cells are never read by the blank trajectory. The exceptional parameters
0,...,20 have completed exact infinite-tail certificates. This does not
cover arbitrary four-black patterns. It demonstrates that endpoint
compatibility still leaves a necessary physical visit-order test.

### A clock restriction on erasing old wakes

The transverse clock gives an all-period exclusion of a clean periodic
eraser of the standard wake in the same invariant orientation sector as
the writer. If a repeat consumes k standard deposits and writes an output
deposit E in P_E>0 updates, its exact signed field balance requires

    A(E)-k*W >= P_E.

For the retained canonical seed and clock center, W=856. Thus E cannot be
empty. If every output cell stays within transverse radius R, then

    |E|*(3^R-1) >= 856*k+P_E.

The full finite-endpoint version also allows an arbitrary fixed controller
at the end of an n-period input wake. Its initial clock is n*W+C. Any
T-step endpoint with K black cells and head and board within radius R must
satisfy

    (K+1/2)*(3^R-1) >= n*W+C+T.

The intermediate path is unrestricted. All old endpoint cells are retained
in the signed accounting. This still permits unbounded transverse spread,
and it does not make an output residue immune to later visits. The proof
and exact controls are in
`constructive_alternatives/transverse_clock_residue.md` and
`constructive_alternatives/check_transverse_clock_residue.py`.

### Why zero density does not imply finitely many returns

An explicit compact countermodel preserves finite support in both time
directions, changes one board bit per update, has no periodic state, and
has uniform zero density of every bounded-mass set. Yet one finite-support
orbit returns to exactly one black bit at times (2*4^j+1)/3 for every j>=0.
It is a conjugate of binary addition using adjacent-bit differences.

This is not an ant trajectory: among other differences, it can change a
distant bit without physically walking there. Its role is limited to
showing why the compactness, no-repeat, and zero-density arguments alone
cannot prove pointwise mass divergence. The exact construction and the
remaining sufficient excursion-radius criterion are in
`constructive_alternatives/pointwise_mass_recurrence_gap.md`.

## 6. Current primary-source status

The new source check located `imfinn/langton-two-black`, revised manuscript
of 5 October 2026. Its Lean theorem covers arbitrary placements of at most
two initially black cells and proves eventual period-104 observations with
diagonal drift. Exact standard-word identification is separate computational
evidence. The manuscript explicitly leaves arbitrary finite inputs open.

https://github.com/imfinn/langton-two-black

The key inherited cut and clock sources are pinned in the relevant notes.
No claim of priority for the added consequences follows from this limited
source comparison.

## 7. Reproduction and trust

The research archive retains source code, run summaries, exact witnesses,
and internal audit notes. 

From the archive root, a short witness replay uses only Python:



The full root mass search can be rebuilt, for example, with:



Higher K searches grow quickly. The retained K=15 run traversed more than
342 million nodes. The C++ implementation is intended for the checked small
range; integer and stack limits must be reviewed before extending it.

The direct SMT experiment used z3-solver 5.3.1.0 (API version 5.3.1). The
downloaded dependency and compiled binaries are omitted from this archive.
Install that package in the chosen Python environment before running the
SMT controls. Solver UNSAT reports in this exploration have not been
converted to separately checked proof certificates.

## Remaining target

The proofs constrain stored information and several possible geometric
forms. They do not prove that nonstandard interactions occur only finitely
often. A global argument must still control future reads of old cells, or
prove another condition that forces eventual periodicity. Classification
of all finite-support periodic traces is a further obligation for the
standard period-104 conjecture.
