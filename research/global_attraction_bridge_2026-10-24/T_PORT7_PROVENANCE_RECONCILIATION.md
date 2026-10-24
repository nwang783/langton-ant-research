# T7 manifest reconciliation

24 October2026,13:56 UTC. This is a provenance correction, not a new mathematical claim or an audit result.

The originally submitted T7 manifest hash was

    0e8dbf82450a2109fc466a200dab7ec181603179f2397a979d8889cb532abaed.

It selected `T_PORT7_ABSORBING_GUARD.md`, SHAcaeee278ec0ff3ccd083d4687e0d134a0de2da8cb92783c67d65da8647e18c6c. The independent checker later stopped before replay because the same manifest path contained different bytes, hash

    36a1328ef12c76cdab5d7314f0f88e4e7dd0a989e3bc147ebd3512f52518cdae.

Those bytes selected `T_PORT7_ABSORBING_BRANCH.md`, SHA5e3f884c3beb03ee0156dd450cf412d73fa03031a7d46907fa65238b16545043, and changed descriptive status/claim/scope fields. The cause and writer of that replacement are not established by this note. No file modification is attributed to anyone without evidence.

Both versions are now separately preserved:

- `T_PORT7_ABSORBER_MANIFEST_V1_0e8dbf82.json`: reconstructed from the original submitted construction and unchanged source files; its hash is exactly the ORIGINAL submitted0e8dbf82... hash, byte-for-byte.
- `T_PORT7_ABSORBER_MANIFEST_V2_36a1328e.json`: direct byte copy of the later observed manifest, hash36a1328e....

Every shared checker, checked dataset, run log, recovery-word file and dependency hash is identical between the two versions. The original GUARD proof remains unchanged. No mathematical counterexample or changed computation was found in this reconciliation.

The audit requested here is explicitly for immutable V1 and its original GUARD proof. The replacement-path spelling is not an instruction to silently change audit scope. V2 and its alternate proof are retained for review but are not promoted to independently checked status by this note. Any later signoff should name its exact selected manifest and this reconciliation binding.
