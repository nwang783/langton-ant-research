# Langton ant continuation — 22 October 2026

## Main result and scope

The full finite-seed highway conjecture remains **unproved and undisproved by
this work**. This bundle contains a computer-assisted proof of the following
partial theorem:

> For every finite initial black set and every initial pose, the current
> black mass is at least five at all sufficiently late times.

Read `chronology/eventual_mass_five.md` for the complete reduction and its
certificate dependencies. The Word report at the archive root develops the
argument and the other results in a single document. The result has exact
integer/rational checks and independent implementation audits. It is not a
Lean formalization or an externally peer-reviewed publication. No priority
claim is made.

The theorem does not prove that mass tends to infinity. It does not prove
capture from every input with at most four black cells. It does not give a
bound on the last small-mass return in terms of the initial mass alone.

## Model

The plane is Z^2. North is (0,1). White turns right, black turns left; the
read cell flips and the ant moves one unit in the new heading. A state keeps
the entire finite black set. Headings N,E,S,W are 0,1,2,3 in the primary
checker. The independent audit instead uses complex-coordinate unit vectors.

## Proof map

1. `chronology/axial_separator_proof.md` proves signed row/column charges and
   the sharp midpoint displacement bound
   `|B_s XOR B_t| >= 2 ||m(X_t)-m(X_s)||_infinity`.
2. `chronology/low_mass_recurrence.md` proves that every clock increment type
   occurs within `2K+4` updates from mass at most K, and that bounded-mass
   recurrence forces all four critical clocks to diverge. It analytically
   excludes infinitely many visits to mass at most three.
3. `chronology/mass4_first_collision.md` uses the complete canonical one-bit
   certificate to force the first distant collision in any hypothetical
   mass-four recurrence to have phase 72.
4. `chronology/eventual_mass_five.md` proves the exposed southwest corner,
   guards every remaining input bit and the complete old field, excludes
   nine ordinary channels at each later collision, and forces the rectangle
   `{-33-2n,8+2n} x {-14-2n,41+2n}` with n tending to infinity.
5. `planar_structure/exceptional_rectangle_proof.md` proves capture for that
   rectangle for every integer n>=200, at a certified time
   `728n+200304`. It also proves the one-/two-bit parent prefixes and tails
   used in the reduction. The northeast corner is never read.
6. `chronology/exceptional_stage_core_audit.md` independently reconstructs
   phase-correct canonical cores and checks the full XOR archives on every
   future incoming-highway read, for every n>=200.

The main eventual-five proof does not depend on accepting or rebuilding the
separate public all-position two-black Lean artifact. That artifact is used
only as external context and for the conditional application in
`chronology/low_mass_local_limit.md`.

## Reproduce the principal checks

Use ordinary Python 3.12 execution, with assertions enabled. Core proof
checkers use the standard library. Run the following commands from the
archive root, which contains both `ant_continuation/` and
`ant_continuation2/`:

```sh
python3 ant_continuation2/chronology/axial_separator.py
python3 ant_continuation2/chronology/forcing_and_small_mass.py
python3 ant_continuation2/independent_audit.py
python3 ant_continuation2/chronology/mass4_first_collision.py
python3 ant_continuation2/planar_structure/certify_exceptional_rectangle.py
python3 ant_continuation2/chronology/mass4_later_collision_guards.py
python3 ant_continuation2/chronology/audit_exceptional_stage_cores.py
python3 ant_continuation2/independent_rectangle_audit.py
```

The all-parameter rectangle checker took about 80 seconds in the research
workspace. It uses the retained literal witness
`planar_structure/exceptional_rectangle_template.json` and the prior exact
affine engine in `ant_continuation/wake_clock/`. The witness generator
`extract_exceptional_template.py` is included but need not be run to verify
the saved witness. Its two sampled inputs only generated the candidate;
they are not the all-parameter proof.

The independent rectangle audit replays 1,256,840 updates at n=200,201,500,
compares nine entire symbolic fields, and separately proves the supplied
infinite tails. These three evaluations audit the implementation; the affine
checker proves the family for all n>=200.

Earlier certificate reconstruction and C++ audit commands are in
`../ant_continuation/README.md`. Every prior dependency is included. No
third-party complete source prose is needed to run these main checkers.

## Other results

- `chronology/low_mass_local_limit.md`: along bounded-mass recurrence, at
  least four black cells escape every fixed finite set. A fixed-pose local
  limit has mass at most K-4. Finite-time continuity does not imply
  continuity of eventual highway capture.
- `chronology/axial_separator_proof.md`: a quantitative lower bound on the
  running maximum of black mass, of order `log T / log log T`.
- `planar_structure/finite_white_episodes.md`: finite white components cannot
  trap the active dual vertex forever, with explicit entry-mass/width bounds.
- `fold_geometry/double_c_fold_lemma.md`: `F V^n F V^m F`, F=CC, is infeasible
  for all n,m>=0. Its mixed U/V generalization fails on a finite input.
- `fold_geometry/arbitrary_lookahead_obstruction.md`: one tested local
  potential fails even after arbitrarily long prescribed legal futures.
- `fold_geometry/fold_geometry_status.md`: exact restricted results, the
  fuel-hull conjecture, and the limits of capped potential searches.
- `planar_structure/two_black_corridor_assessment.md`: primary-source scope
  of the public two-black result and the missing multi-corridor obligations.

## Status of exploratory data

`maxplus/` contains early failed potential prototypes. `circuit_probe/`
contains finite circuit probes. The large `fold_geometry/` search records
retain literal finite counterfields; none is a successful general invariant
or a certificate that every possible invariant is impossible. All searches
have stopped. The obsolete duplicate port-search checkpoint is not included:
its counterfield prefix is contained in the final refinement record and
its unique weights/logs are retained in
`maxplus_port_head_sft_checkpoint_metadata.json`.

See `STATUS.md` for the remaining proof obligations. `SOURCES.json` records
reviewed source links and hashes. The archive-wide `MANIFEST.json` hashes
every included file except itself. Complete third-party source snapshots,
compiled executables, caches, and internal document-preview files are omitted.

The optional report builder needs Pandoc, python-docx and Matplotlib. It can
be run as `python3 ant_continuation2/report_source/build_report.py` from the
archive root. It does not affect the mathematical certificates.
