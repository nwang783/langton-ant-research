# Reproducibility guide

## Integrity and a finite smoke check

From the repository root, with Python 3:

```sh
python3 tools/verify_snapshot.py
python3 tools/smoke_check.py
```

The first command verifies every Git-contained artifact against the export manifest and explicitly reports that separate bulk data was not checked. The second reconstructs the canonical word's 84 length-ten factors and replays the supplied 13-cell canonical fixture for 100 periods. It is a finite sanity check, not proof of eventual behavior for arbitrary finite seeds.

For separately restored evidence:

```sh
python3 tools/verify_snapshot.py --bulk-root /path/to/restored/research
```

The archive should restore relative paths into a separate research directory. Verify the archive SHA-256 before extraction, extract only a trusted archive into an empty directory, then check all file hashes. The alias manifest records historical duplicate aliases without exporting machine-specific absolute symlinks.

## Replaying historical checkers

1. Locate a theorem's frozen manifest and latest audit entry. Read every stated assumption and mandatory correction.
2. Verify the exact checker, input, report and dependency hashes. A transformed prose file has both source and export hashes in the manifest; do not silently substitute its export hash for an original certificate's expected digest.
3. Work in a disposable copy, not the frozen evidence tree. Several historical checkers write their report beside their own source, so even a successful replay may overwrite a retained report if run in place.
4. Restore the required bulk files and pinned upstream source dependencies. Python's standard library covers many scripts; some branches require C++, Z3 or other packages. Check imports and each branch's README before installing anything.
5. Inspect the checker for historical absolute paths. Some files are portable via their own location; others need path adaptation in the disposable copy. The original source is preserved for hash comparison. This snapshot does not claim every historical checker has been ported or rebuilt.
6. Run Python without `-O`; many exact checks use assertions. Record compiler/interpreter and solver versions, command, seed/parameters, output, runtime, exit status, and report digest.
7. Compare exact reports, or explain expected environment/path-only differences. A passing replay establishes the stated finite certificate or certificate check, not the missing analytic reduction or the universal conjecture.

## Environments and provenance

`manifests/environment.json` records the packaging environment, not a claim that every historical run used those versions. `manifests/replay_results.json` lists only checks actually executed for this snapshot. Historical audit reports retain their own stated scope and trust boundary.

## Continuing without repeating searches

Search `manifests/experiments.jsonl` by topic and inspect earlier manifests, parameters and negative controls before rerunning. Exact duplicate artifacts are listed separately. Add a new dated manifest for changed hypotheses or code. Keep rejected hypotheses and UNKNOWN/timeouts visible; do not overwrite immutable certificate bundles or reclassify them based only on file names.

For the exact collection cutoff, safe catch-up procedure, and distinction between export-hash integrity and original frozen-proof hashes, see [Continuing research](CONTINUING_RESEARCH.md).
