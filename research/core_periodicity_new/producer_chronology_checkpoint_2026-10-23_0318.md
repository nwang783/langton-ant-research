# Chronology checkpoint, 2026-10-23 03:18 UTC

## Useful new result

The historical-record approach now has two independently signed finite EVENT exclusions. Auditor `check_dcuv_record_peak_independent.py` reconstructs literal base graphs, the exact fixed potential/phase/threshold, fused known-origin guards/resets, and separate reset-BDD invariants for original pilot cases01 and17. Counts4,488 and1,544,264. These exclude only specified strict-historical-record events, not unrestricted protected transfers. No unproved H is used.

The complete DCUV theorem and global finite-seed standard104 conjecture remain open. The earlier complete D/C/V exclusion and its mass-only cubic bound remain signed and unaffected.

## New protocol

`chronology_dcuv/historical_record_protocol.md` explains the auditor-approved reduction. Define a historical maximum of every entering/exiting core, every output at creation (even subsequently retired), and every initial-identity activation. Initial activation weight I dominates all target input demands. An unfunded strict new peak T must consume only produced identities. Anchor at their earliest last producer and protect one such q. Every source/strict-intermediate full packet peak is strictly below T. Track all target input origins; the goal requires all known produced. No intermediate unproved-event filtering or least-gap mutual family is needed. OUT omits geometric cuts conservatively.

All target types must have at least one input; otherwise directly check created peak<=entering core. Current recurrent-eight types all have inputs. Four source global phases are explicit. Initial activation cuts are not represented in the current finite models, a conservative loss of information that may admit genuine finite histories whose earlier activation already funded the target. Do not confuse a record over core/output values alone with a record over the full historical maximum.

## Frozen numerical candidates

1. Original saturated fixed-DCV candidate `chronology_dcuv/potential_extend_dcv_policy01_saturated.json`, SHA fd913df5bb6fed6b7d452e337bac423363cbebe95f49c01ad16b4ca68103cd6c. Direction(1,3), core offsets[2,52,54,-8], I110, locally computed activation jump K130. Record inventory4,129 alignments in `record_peak_inventory01.json/.tsv`. Old individual-transfer obligations1077→775 after output saturation. Input-sponsor normalization can further lower individual requirements, but does not alter record thresholds.
2. Symbolic's canonical head-only record candidate `record_head_offset_search/head_1_1.json`: direction(1,1), core offsets[0,22,20,10], created peak equals new core, every output saturated to that new-core peak. I28. No individual input-transfer inequalities are required by this record-only formulation. Exact builder gives1,651 alignments in `record_head_offset_search/inventory_1_1.json/.tsv`. A bounded36,666-offset search per direction found this candidate, not a global optimum. Raising individual32 peaks by0..100 yielded no further count reduction. Direction(1,3) head-only gives1,707 instead.
3. Symbolic's alternate individual-transfer optimized policy02 has445 obligations but worse4,553 record alignments. It remains separate and is not substituted into frozen original certificates.

## Tools and experiments

- `chronology_dcuv/build_record_peak_inventory.py PROFILE POTENTIAL PREFIX`: exact phase/alignment inventory, filters signed HB clauses, target nonrecord peaks and source peak>=goal. No proof of remaining rows.
- `add_resource_record_peak_fused.py BASE.json PREFIX POTENTIAL PHASE`: independently reviewed on cases01/17. Color+known-origin at all target inputs only; source outputs/init/install code3, unknown black1, white0. Strict near peak cut; outer goal all known; no H.
- `record_peak_pilot/`: original weight sourceD→D/U18 phase rows,9 no-hit9 abstract witnesses. Every local no-hit invariant verified. Independent signed subset01/17.
- `record_peak_both/`: full source∪target color refinement of9 witnesses adds no-hit cases15 and18;2 remain witnesses,5 cap750k. Thus11/18 locally close,7 remain open/capped. Do not imply all11 independently signed.
- `expand_resource_patch_poses.py BASE PREFIX MARGIN`: extends exact pose set without more color cells, keeps all old near poses and adds sector-compatible patch rectangle+margin. No separate wrapper audit yet. Case13 margin12 has1,682 explicit poses and still witnesses, delayed32→61 steps,27,444,959 assignments. No benefit beyond a tighter countermodel.
- `add_resource_record_peak_labels.py FUSED_RECORD PREFIX 'all|x,y;...'`: discovery-only signed-HB producer-signature quotient. Unknown class0 stays separate from every produced class, even empty signatures; all goal input labels must be nonzero. No H. Originalcase02all5 signed-label cells gives23vars and the same50,972-state depth14 witness. No separate implementation audit yet.
- `record_head_pilot/`: canonical head-only sourceD→U7rows. Cases5 and7 trivially exhaust (4states each), other5 witness. No complete family.
- `chronology_dcuv/probe_record_geometry_closure.py INVENTORY OUTPUT CAP`: exact color-free infinite-pose BFS with protected q, signed source/target subpair guards, and fixed record cuts. Finite exhausted pose sets prove event impossibility; cap/path do not. This is new discovery code, not independently audited.

## Other progress and coordination

Symbolic independently computed count0..3/overflow protected DCUV kernel: all1,188 upper-input alignments exclude count0..3 provisionally, so stubbornD rows need>=6 and>=5 C turns by heading. Independent audit pending at this checkpoint. This is not full absence.

SourceDC JOINT batch finished13 abstract witnesses11caps, zero closures. Earlier individual4/24 closures do not imply joint clauses. Individual interleaving retries all capped and added none.

Symbolic is checking whether finite explicit controls contain all-produced-input events or actual unfunded records; include initial activation values in historical M. It owns numerical offset work and counted kernel. Auditor owns record semantic/invariant checks. Two signed record-event controls are retained, not a global theorem.

## Processes

  Preserve all frozen originals.
