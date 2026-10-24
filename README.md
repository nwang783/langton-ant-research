# Langton's ant: research record and reproducible evidence

**Status: UNSOLVED.** This repository is a versioned research snapshot, not a proof of the universal finite-seed highway conjecture. No finite-seed counterexample has been established.

## Exact question

On the square lattice, the ant turns right on white, left on black, flips the current cell, then moves one unit. Starting from an arbitrary finite black set and arbitrary ant pose, must its turn stream eventually equal a cyclic phase of the canonical 104-step highway word, up to translation and quarter-turn rotation?

Unbounded motion, sparse defects, some repeating motion, or a finite successful simulation do not settle this question. Stationary debris may remain behind a highway; whole-board translation is not required.

## Start here

- [Research index](docs/RESEARCH_INDEX.md): routes, results, open obligations, and where to find evidence.
- [Current status and corrections](docs/STATUS.md): accepted scope, superseded claims, and negative controls.
- [Status taxonomy](docs/STATUS_TAXONOMY.md): what “checked,” “conditional,” and “open” mean.
- [Reproducibility guide](docs/REPRODUCIBILITY.md): integrity checks, replays, and their limits.
- [Continuing research](docs/CONTINUING_RESEARCH.md): snapshot cutoff, catch-up, deduplication, and transformed-hash caveats.
- [Research audit chronology](research/audit.md): dated mathematical audit entries. Later corrections supersede earlier claims.
- [Recovered research index](research/RECOVERY_INDEX.md): provenance and historical missing artifacts. It is historical, not the latest status.
- [Public-release checklist](PUBLIC_RELEASE_CHECKLIST.md): remaining privacy, provenance, and licensing decisions.
- [Literature map](research/literature.md) and [source provenance](docs/SOURCES_AND_RIGHTS.md).
- [Artifact manifest](manifests/artifacts.jsonl), [exact duplicates](manifests/duplicate_artifacts.json), and [experiment index](manifests/experiments.jsonl).

## What is preserved

The Git snapshot contains research prose, executable source, compact results, negative controls, and corrections. Large generated evidence is deliberately separate from Git, with every included artifact's exact size, SHA-256, and storage disposition recorded. See [bulk preservation](docs/BULK_PRESERVATION.md). A manifest is not a substitute for the bytes: archive publication and availability are reported separately.

The original research tree is retained unchanged. Administrative conversation material is not published. Prose that needed privacy cleanup is explicitly marked in the artifact manifest with both its source and exported hashes. Source-code and certificate integrity must not be confused with mathematical correctness.

## Avoid repeating work

Before starting a search, consult its topic directory, experiment index, audit chronology, and rejected or inconclusive attempts. Match the exact seed, rule convention, parameter bounds, hypotheses, and source hash. A timeout is not UNSAT. An UNSAT solver response is not an independently checked refutation unless a proof trace and checker establish it. Do not treat an old “pending” entry as current when a later signed correction or completion exists.

Future updates should add a dated result and manifest, preserve failed attempts and countercontrols, and state the exact open implication. Commit before launching an expensive new branch and commit the terminal result afterward. Do not overwrite a frozen certificate.
