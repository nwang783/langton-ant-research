# Exact low-height summaries with transverse displacement modulo four

Status: independently signed as audit KL. The independent replay regenerated both literal unit graphs, checked every finite derivation and residue-specific grammar closure, and all16,777,216 k5 port profiles. Artifacts: audits/low_k3_residue_independent.json and audits/low_k5_residue_independent.json. No record exclusion is claimed.

Use a cutoff L for which every complete context of a packet begun at q<=L misses the retained color patch, and all its residual inputs/outputs have height<=F. Every low excursion then preserves every retained color/origin bit and every high-token multiplicity. It changes high-token or watched-token C-ages only by adding the total C count, saturated at4.

Besides exact low head height, retain the head transverse coordinate t modulo4. A packet has exact head changes(delta_q,delta_t), and delta_q and delta_t have the same parity. Expand its height-counter change -delta_q into a private monotone unit chain of length n=abs(delta_q), or one zero edge if delta_q=0. For a nonzero chain, put transverse residue1 on its first n-1 edges, and delta_t-(n-1) modulo4 on its last edge. Every unit edge then has odd transverse residue. A zero-height edge has even transverse residue. Whole-packet transverse displacement is unchanged modulo4.

Consequently ANY balanced unit path has even transverse residue, including paths between private intermediate vertices. Its only possible residues are0 and2. The private transverse values are bookkeeping, not intermediate physical ant positions; original-to-original paths still consist of complete physical packets.

For each balanced vertex pair retain TWO independent maximum saturated C counts, one at residue0 and one at residue2. Identity has(residue0,C0); zero edges have their exact even residue and C weight. Concatenation adds residues modulo4 and saturated C counts; push/interior/pop adds the two unit-edge residues and the interior residue. The finite-lattice least fixed point is exact by the same balanced-walk grammar proof as the unannotated theorem. Every finite maximum is attained by a genuine finite unit walk and hence, at original endpoints, by a packet walk. Different residues are never merged before the maximum is taken.

The finite port formula remains R(pop R)^k(push R)^l with k<=entry_depth and l=exit_depth-entry_depth+k. In this product all four transverse residues are kept, since unmatched steps may have odd net height. Each physical port pair has at most two residue profiles of the parity forced by its depth difference. A summary edge carries(delta_t modulo4, maximum saturated C count for THAT delta_t). At an actual source residue t0, its destination is t0+delta_t modulo4.

Initial low head height and transverse position are arbitrary. Initially all high residual places are empty, all retained high colors are white, and initial ages are mature. Therefore the initial-low prefix query needs only projected low-port reachability; every compatible transverse source residue is allowed. The projected initial port set must agree with the unannotated compiler.

For U1 phase1 at the current I48/F=-10 control, the maximum complete-context offset height is8, while the sparse14 patch minimum height is-2. The existing L=-18 gives L+8=-10<-2. Thus every low packet misses all14 retained colors, independently of transverse position. This is a composability check, not an exclusion.

## Implemented controls

- `build_low_height_residue_unit_graph.py`: literal packet/unit-chain expansion and odd-unit-residue bookkeeping.
- `weighted_residue_dyck_summary.cpp`: exact two-profile balanced closure, finite derivation DAG, sparse root IDs. Dense byte weights avoid hash work on failed improvements.
- `check_weighted_residue_dyck_summary.py`: separate check of EVERY finite derivation and every identity/zero/concatenation/push-interior-pop closure obligation. It also checks that forgetting residues gives exactly the old unannotated balanced matrix.
- `compile_low_height_residue_ports.cpp`: finite exact port products, with all four residues in temporary vectors. Output header RESIDUE_PORTS NP NE NI 4; next NI initial IDs, then NP heading/DFA/depth rows, then NE source/target/delta_t/max_C rows.

Executed k3 controls:444 unit vertices,19,485 balanced residue pairs,23,870 finite proof nodes;208 ports,45,161 residue edges,162 initial ports. Full balanced closure and full unannotated port projection pass.

Executed k5 controls:4,300 unit vertices,815,243 balanced residue pairs,939,427 finite proof nodes;2,048 ports,2,836,493 residue edges,1,301 initial ports. Full balanced closure and full port projection pass. Artifacts are under `chronology_dcuv/delayed_height_probe/low_k{3,5}_residue_*`.

These are exact finite-control relaxation summaries, not complete ant paths. They do not enforce unretained low-cell colors, prove that a chosen low word is physically feasible, or settle U1/V1 or universal capture.
