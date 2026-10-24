# Actual full axis-four fronts require at least seven complete reads

Independent terminal acceptance: 23 October 2026, 20:15 UTC.

## Exact conclusion
There is no complete WHITE translating Langton-ant front with actual full displacement (4,0) in which every physical cell has at most six complete reads. Proper quarter rotations give the same statement for (0,4), (-4,0), and (0,-4). There is no strip-width or period ceiling. This uses the actual full drift, not a primitive or smaller quotient.

## Certificate and independent replay
The frozen candidate remains unchanged at `general_flux_d4_0_first_return_w3_real_cap6_N32_M64_mod2.certificate.json`, SHA256 c873e7a20f8a842ddf91583ee950653fa1236fcc0cd5ba0e525ae4ce173de21b. The independent checker is `../audits/check_general_multirow_first_return_real_resumable.py`, SHA256 551465d91122cfe3b381ad1394826e8b07b7618118689a3625b9a4b438676666. Its independently reviewed physical-return reference is `../audits/check_first_return_windows_independent.py`, SHA256 d7af1b2c3ebf5404d30c0b53cf90d394f831fa97998e27c99b0d64155cc6a0ae.

The replay reconstructs all complete local histories and physical port joins, filters by the exact zero transverse cut flux, reconstructs successor splicing and three-row first-physical-return tests, and uses independent infinitesimal Bellman-Ford strict-clock closure. Finite clock saturation only weakens constraints. The fixed normalized clock scale is 32, outward bound 64, and seam modulus 2. The minimum-period premise P >= 32 comes from the already signed KR cap-five exclusion and LC physical-return packing, not from this cap-six result. The later P >= 40 bound and generic first-cell monitor are not premises.

Both parities independently yield 225,703 internally matched zero-flux row histories. Every listed state is reachable from the unique initial state, and every one of the 44,617 states has its COMPLETE possible outgoing set independently reconstructed. The replay checked 275,110,753 extensions and recovered exactly 56,622 edges, with 1,555,347 shortest-path closures and at most 40 transition nodes. No possible whole-front outcome survives.

 The final durable checkpoint has next_source = 44,617, the same totals and completed source chain f616f501d8d7cc0468bc858da7706de9f6daed906c54c9ba8031d8024e919eb5. Its internal checksum and all three frozen input hashes were rechecked at acceptance. Earlier interrupted sessions 6279 and 42534 remain UNKNOWN and supply no terminal evidence.

Final report: `../audits/general_flux_d4_0_first_return_w3_real_cap6_N32_M64_mod2_resumable_independent.json`, SHA256 ca2177d2e8b575b01add26208c4314bd3f7c746a2793027d9b13e9718bcbf9b2.
Final checkpoint SHA256: 544a6bae0e10af1e9c72dd8092906c8b192afa6bc1e828329a7a56b306bf4455.

## Boundaries
This excludes this actual full drift under cap six only. It does not exclude axis-four fronts at arbitrary read caps, assert period 104 minimality, imply eventual periodicity, or settle finite-seed capture. The universal finite-seed standard-highway conjecture remains open.
