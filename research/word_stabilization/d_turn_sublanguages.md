# Two additional finite-fuel D/turn sublanguages

Status: independently replayed certificates on 2026-10-22, with the final-D boundary identity made explicit below. No original-port premise is used. These are restricted language theorems, not a solution of the full seven-word language.

## D,C,U: a genuine two-cell-rule application

The seven packet types are D,DC,DCC,DCCC,U,UC,UCC. A packet owns its entire raw word; its target also includes the actual next M11=LLLLRLRRRRL. The one-state graph initially admits every packet, and exact physical pair/triple checks provide the only short controls. A factor starts non-C and has this actual final marker. Literal C^4 M11 and U C^3 M11 are infeasible, so these packets cover every such factor over D,C,U.

The two-cell engine stabilizes at7,510 forbidden spatial pairs among8,111 candidates, after removing47 short types. The final certificate has6,801 ordinary neighbor clauses,707 odd-reader clauses, and TWO two-cell transition clauses. The unmodified single-cell engine and the odd-reader-only engine both stabilize at4,556 clauses and fail to certify the needed marks. Thus the two-cell rule supplies a genuine new conclusion, rather than merely a different certificate for an old result.

The selected marks are:

- D: (0,1), phase11 in the actual next marker.
- DC,DCC,DCCC: (0,1), phase11, inside the first C.
- U: (0,2), phase12; (0,3), phase23.
- UC,UCC: those two U inputs and (-1,4), phase29, in the first C.

Every mark is a first-L input in its target context and is unread by every earlier packet. For a D packet, its mark is the next packet's phase1 input. No selected mark of that next packet is its phase1 cell, so no double charging occurs. More distant packets cannot share it because that next packet has already read it. This also covers a final D whose mark lies in the actual terminal marker.

The first packet additionally needs its five common startup black cells at phases0,1,2,3,5, namely (0,0),(-1,0),(-1,-1),(0,-1),(1,0). These are disjoint from every selected mark, by direct comparison in the first packet and freshness for later packets. Hence

5 + n_D+n_DC+n_DCC+n_DCCC+2n_U+3n_UC+3n_UCC <= m.

Every packet's length is at most55 times its weight, and mass gain at most9 times its weight. Thus raw length <=55(m-5), exit mass <=10m-45. If the removed final macro is D, its endpoint (1,1,N) equals its phase6 R-read cell, with no later read of that cell in D. Its next actual turn is therefore forced L. D followed by that forced turn is M11, so even the short final D supplies the required actual right marker without adding to the retained raw length. Removing at most four initial C macros and the final macro then gives the conservative arbitrary finite D/C/U-word bound55m+473. In particular no finite-support infinite D/C/U tail exists.

## D,C,F,Q,B: ordinary-rule certificate

The thirteen packets are D,DC,DCC,DCCC and A,AC,ACC for A=F,Q,B. Literal A C^3 M11 is impossible for these three A, and C^4 M11 is impossible. The ordinary unchanged engine closes52,837 clauses among53,398 candidate types, with57 short types.

Use (0,1), phase11, for every D-based packet, and (-3,-1), phase42, for every F/Q/B-based packet. All are certified fresh. The same external D-mark ownership argument applies because none of the next packet's selected marks is its phase1 input. Five startup cells are again disjoint. Thus packet count <=m-5 and raw length <=104(m-5). Trimming initial C and final macro gives the conservative arbitrary finite-word bound104m+862. No finite-support infinite D/C/F/Q/B tail exists.

## Consequence within the seven-word language

The independently accepted restricted certificates imply that any infinite finite-support seven-word tail needs infinitely many U or V (by the second theorem) and infinitely many V or F or Q or B (by the first). Together with the already signed no-D and C-free theorems, it also needs infinitely many D and infinitely many C. This does not prove that any of these events is finite.

## Artifacts

- seven_sub_dcu_{port_quotient,grammar}.json and seven_sub_dcu_kernel.input.
- seven_sub_dcu_patch2_kernel.tsv and its summary/fresh files.
- generic_patch2_spatial_kernel.cpp and multi_cell_spatial_inference.md.
- seven_sub_dc_fqb_{port_quotient,grammar}.json and seven_sub_dc_fqb_kernel.input.
- seven_sub_dc_fqb_plain_kernel.tsv and its summary/fresh files.
- d_turn_sublanguages_manifest.json.

The independent replay records are ../audits/check_d_turn_sublanguages_independent.py, ../audits/check_d_turn_dcu_independent.json, and ../audits/check_d_turn_dc_fqb_independent.json. The two-cell clauses use source DC, target U or UC at pose(3,-1,N), and cells(2,1),(2,2). Their allowed two-bit transition graph cannot reach the target colors.
