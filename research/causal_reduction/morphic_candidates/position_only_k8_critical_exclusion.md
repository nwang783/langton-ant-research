# Critical-area eightfold position inflation

Status, 22 October 2026, 21:39 UTC: independently certified end-to-end. All 2,784 exact root refinements have checked monotone-RUP refutations, with zero UNKNOWNs. A separate no-import audit rebuilt all 154 legal eight-step images, the complete 5,161-node root tree, every original CNF clause multiset, and all 42,696 proof additions with a different propagation checker. No SAT solver is trusted. See audits/check_position_k8_rup_independent.py/json and position_k8_rup_independent.log.

## Independently certified scoped theorem

There is no ant path on ANY initial coloring satisfying

    p(8n) = (2+2i) p(n) for every n >= 0,

where p(0)=0 and the initial heading is north. There is NO heading-equality
hypothesis. The same conclusion for scale2-2i follows by reflecting the plane
across the vertical axis and complementing every cell color. This transformation
preserves initial north heading and ant dynamics while conjugating the scale.
It is legitimate here only because the claim covers arbitrary initial colorings;
it would not preserve a finite-black-background hypothesis by itself.

Already512 turns are impossible under the identities through n=64. This does
not address affine/time-shifted inflation, paired-time-only inflation, or other
position-only scales. Scale k9,a=3 is separately excluded for finite support
by position_only_k9_record_exclusion.md. It is not the highway conjecture.

## Reduction and exact encoding

Every eight-turn block has displacement a times the corresponding coarse step.
Its heading need not agree with the coarse heading at either endpoint. Enumerate
all internally alternating eight-letter words with the required displacement,
using the ACTUAL fine entry heading. Enforcing literal alternation while choosing
the first eight images gives exactly2,784 self-consistent64-turn words, in5,161
search nodes. The complete list is position_only_prefixes_k8_a2_2.json, generated
by enumerate_position_only_prefixes.py with status COMPLETE, not a node cap.

For each fixed64-turn coarse word, choose64 eight-letter images. At fine boundary
i, the heading has parity8i, so a Boolean variable chooses north or south. More
generally the implementation represents boundary heading as (ki mod2)+2b_i.
Each image choice fixes its entry and exit heading bits, and b_0=0. Its entry
position is a*p(i); its endpoint is required to be a*p(i+1). Thus the choices
are exactly continuous fine paths with the required positional identity, without
restoring the omitted heading equality.

For every physical fine cell, ordered potential macro reads carry shared before
and after color variables. A selected nonempty internally alternating read word
fixes its first and final colors. A selected image that misses the cell preserves
its color. Initial colors are free. One-hot image choices and the fixed initial
eight choices complete an exact Boolean formulation of a512-turn refinement.

position_only_refinement.py implements this CNF and direct solver. All2,784 cases
are UNSAT, zero UNKNOWN, as recorded in
position_only_refinements_k8_a2_2_summary.json and the per-case JSONL. Three known
feasible position-only prefixes, including a heading-changing k9 model, are
forced SAT and literally replayed in position_only_refinement_controls.json.

## Completed proof certificates

certify_position_k8_plain_rup.py writes the explicit original-ID CNF, calls the
untrusted plain first-UIP producer, and separately checks every learned clause
by monotone RUP through the empty clause. It requires zero RAT/deletion steps.
It saves compressed original CNFs, proofs, hashes, fixed prefixes, and individual
checker counts under position_k8_rup/. Its final manifest has status ALL_2784_MONOTONE_RUP_CERTIFICATES_VERIFIED.
All 42,696 additions pass RUP; maximum 708 per case. Every proof ends with a
checked empty clause, with zero RAT or deletion steps. Generation and checking
took 1,781.936 seconds. Manifest SHA256:

    514d7ff5c361b1fcd183996b77c370f4c7a6311564775127a63734e2a165e054

The new encoding must receive its own independent geometry review even though
the proof producer/checker machinery is already audited for the older headed
k9 result. The latter result does not imply this one.
