# Planar-structure continuation: result index

This directory contains research from 22 October 2026. It does not claim a
proof of the full finite-seed highway conjecture.

## Completed analytic results

- `finite_white_episodes.md`: every episode confined to finite components
  of the white dual-edge graph exits in finite time, with explicit bounds.
  `audit_white_episodes.py` and `white_episode_audit.json` give the exact
  local/exhaustive audits. The dynamics on the infinite white component
  remains the main unresolved case of this route.
- `mass_four_escape.md`: hypothetical recurring four-black states have a
  fixed recurrent pose, four escaping cells and an exposed southwest
  L-corner at the first distant collision. This is a geometric component
  of the joint chronology proof.

## Completed parametric computer-assisted result

- `exceptional_rectangle_proof.md`: for every integer n>=200, the seed
  `{-33-2n,8+2n} x {-14-2n,41+2n}` reaches a standard NW highway at
  `T=728n+200304`; the northeast corner is never read. Also proves the
  required one- and two-bit parent interfaces, with uniform archive/read
  bounds and exact infinite tails.
- `extract_exceptional_template.py`: finite candidate-word generator.
- `exceptional_rectangle_template.json`: literal fixed words and affine
  period counts, used only as a witness by the following verifier.
- `certify_exceptional_rectangle.py`: exact all-parameter color and
  infinite-tail verifier, retaining the full field.
- `exceptional_rectangle_affine_certificate.json`: successful result.
- `exceptional_affine_fields.json.gz`: complete symbolic field snapshots
  at stages 4, 8 and 13, for independent reconstruction.
- `probe_exceptional_corners.py`, `exceptional_corners_probe.json` and
  `exceptional_three_four_probe.json`: earlier individual finite-seed
  certificates; these are not the source of the all-parameter inference.

The parametric verifier imports the existing affine-ray engine from
`../../ant_continuation/wake_clock/certify_four_scatterer_prefix.py` and its
dependencies. Keep the complete research bundle when reproducing it.

The full recurrence reduction and independent guard audits belong in
`../chronology`; in particular see `mass4_first_collision*`,
`mass4_later_collision_guards*` and `exceptional_stage_core_audit*`.

## Negative controls

- `two_white_columns_counterexample.json`, independently replayed by
  `verify_white_strip_reset.py`: a 16-black input crosses two initially
  white columns and leaves both entirely white again after 127 updates.
  This refutes the proposed unconditional width-two white-strip barrier.
  Initial support is present on both sides of the strip.
- `internal_pose_repeat.json`: a finite-white-component episode can repeat
  an incoming pose; the first 2x2 dual-square example returns in four steps
  with a changed field and exits at six.
- `internal_linear_bound_counterexample.json`: a 6x6 white dual component
  with 24 black boundary edges has first exit 148>4*36, refuting the proposed
  universal 4N exit-time bound.

## Literature assessment

- `two_black_corridor_assessment.md`: primary-source scope and limitations
  of the public all-position two-black artifact hosted by imfinn. A third-index preservation
  theorem, multi-parameter first-read coverage, a larger track language,
  and a termination/closure theorem are needed for arbitrary-finite
  induction.
- `source_two_black_revised.md`, `source_Par.lean`, `source_Perp.lean`:
  primary source snapshots with original repository paths and blob IDs
  recorded in the assessment.
- `source_paper_main.tex`: the inspected Jillhewar source, relevant to
  Tait-graph topology and the known additive-charge framework.

The complete third-party source snapshots are excluded from the delivered
archive. Its `SOURCES.json` records their links and reviewed content hashes.

