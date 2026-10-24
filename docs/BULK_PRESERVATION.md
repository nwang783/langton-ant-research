# Bulk evidence preservation

## Completed locally

The snapshot separates compact Git artifacts from 9,489 large generated research artifacts totaling 25,911,709,017 uncompressed bytes. The latter were streamed into a tar archive, compressed with Zstandard, then split into ordered parts below 2 GB each. Exact compressed size and every part's SHA-256 are in `manifests/bulk_archive.json`.

Every archived file was streamed back out and compared with the pre-copy SHA-256 and byte size: all 9,489 matched, with no missing or unexpected files. See `manifests/bulk_verification.json`. The concatenated split parts were also verified against the complete archive digest.

The compact snapshot independently verifies all 41,996 Git-contained research artifacts. The full local inventory also accounts for upstream source references, rebuildable caches, administrative records excluded from publication, and 67 historical aliases. No original research file was deleted or changed. Source sizes and modification timestamps remained unchanged through the collection verification.

An additional 139 generated ELF executables (5,192,096 bytes uncompressed) are preserved in a small separately checksummed build-artifact archive, not source Git. All 139 archive members were verified against their original hashes before the exported executable copies were removed. No original research files were removed. Together the archives cover 9,628 artifacts.

## Remote availability

**The bulk archive is currently local only.** A remote repository containing this manifest alone is not a remote backup of the large evidence. Do not claim full off-machine preservation until both archive parts have been uploaded to an authorized destination and verified there. Record their verified download locations and checksums in a later commit.

Recommended preservation is a private repository for source, compact results, and manifests, plus restricted release assets or object storage for the two binary archive parts. Repository visibility and archive access must match the user's authorization. The archive can be restored with the recorded part order and verified using `tools/verify_snapshot.py --bulk-root`.

## Why not put everything in Git?

Multi-gigabyte machine outputs make cloning and review impractical. The manifest preserves their exact identity without pretending the bytes are already in Git. Byte-identical duplicates are recorded, and small checkers plus finite replay controls provide navigable starting points. The data is not presumed regenerable merely because a script exists: some historical environments or source dependencies still need reconstruction.

Third-party cloned source trees and paper PDFs are reference-only rather than indiscriminately redistributed. The original local copies and complete private inventory are retained. Their publicly useful provenance is in `docs/SOURCES_AND_RIGHTS.md` and `manifests/source_references.json`.
