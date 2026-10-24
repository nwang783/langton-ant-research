# Continue the research without losing or repeating work

## Snapshot boundary

The exact collection start and end are recorded in `manifests/snapshot_summary.json`. The retained mathematical audit was current through the 24 October 2026 20:43 UTC checkpoint. This is a fixed snapshot, not a promise that later work is already backed up. Sources were checked for changes during collection and again afterward; `manifests/source_stability.json` records the result.

## Catch up after this snapshot

1. Start from the committed artifact manifest, using `source_sha256` when present and otherwise `sha256` to identify each original research artifact. Do not use filesystem timestamps alone as proof of identical bytes.
2. Compare the continuing research tree with those hashes. List additions, modifications, and missing artifacts before copying anything. A missing file is not permission to delete its preserved evidence.
3. Read the new dated audit entries and corrections. Record each claim's exact scope, dependencies, negative controls, and whether its replay is complete, pending, rejected, or inconclusive. Do not infer completion from a filename.
4. Wait for a live output to finish, or label it incomplete. Hash each copied file before and after collection. Never overwrite a frozen certificate in order to make a check pass.
5. Review new prose and logs for unrelated communication, personal information, credentials, and administrative material. Keep the research content and record any privacy transformation with separate original/export hashes.
6. Add compact source/proofs/results to Git. Put large evidence and generated binaries in separately verified archives, with exact file-level hashes and a verified remote location. Never treat a manifest alone as backup of the bytes.
7. After explicitly registering reviewed changes in the artifact manifest, run `python3 tools/refresh_indexes.py`. It verifies current Git artifact hashes and regenerates the experiment index and exact-duplicate map from the new export hashes. Reuse existing identical content, but retain the paths and experimental context needed to interpret it.
8. Run the snapshot integrity checker and appropriate scoped replays in a disposable copy. Commit a dated status change and update the archive-location record only after the remote bytes are actually verified.

## Privacy transformations and frozen proof hashes

Some prose originally mixed mathematical content with unrelated communication or operational details. The published prose removes those details. Its exported SHA-256 is therefore intentionally different from the original source SHA-256; both are explicitly recorded in the artifact manifest.

The snapshot verifier checks the exported bytes and reports how many transformed artifacts it checked. It does not claim those bytes satisfy an original frozen manifest's old digest. A historical checker that hashes a transformed prose dependency can therefore fail before its mathematical checks run. That is an expected provenance mismatch, not evidence that the mathematical theorem failed, and not permission to silently alter the frozen certificate.

The original research sources remain retained separately. Where a replay needs their original digest, use authorized original sources or a separately reviewed replay adapter that explicitly recognizes the recorded transformation. Record such a replay as using a transformed dependency, not as original-hash verification. No such adapter or repository-wide replay is claimed by this snapshot.
