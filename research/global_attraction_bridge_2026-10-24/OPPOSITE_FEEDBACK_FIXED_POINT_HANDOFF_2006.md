# One actual self-written-feedback fixed-point task

24 October 2026, 20:06 UTC. The result is frozen for independent audit, not yet independently signed at this handoff cut.

Manifest OPPOSITE_FEEDBACK_FIXED_POINT_MANIFEST.json
SHA72a19c30ae323f04b3cabd39033fb96a80071d268b0a5d642ac8f943867c4497.
Proof OPPOSITE_FEEDBACK_FIXED_POINT_OBSTRUCTION.md.
Checker check_opposite_feedback_fixed_point.py.
Data OPPOSITE_FEEDBACK_FIXED_POINT_CHECKED.json.

## Exact target

Smallest signed 24-cell opposite(3,3) feedback: first contact49729 at(112,105),N; second55541 at(44,177),N. The 5812-read actual word W restores N, drifts(-68,72), and is tested as a whole-state translated recurrence, not as a cropped matching kernel.

## Strongest obstruction

W² is impossible on ANY board: prescribed relative cell(-69,68) has consecutiveR reads5733 and6745=5812+933 with no intervening visit. 6745 is the earliest intrinsic same-letter consecutive-read conflict in the desired two-copy word. FirstR is actual global55462 at(43,173); second is counterfactual because actual continuation already differs.

## Full renewal equations

For full-drift class r, let ell be the minimum SPATIAL index among one-copy read cells r+k d, and t(k) the visit parity. The prescribed infinite future footprint is k>=ell. A whole finite recurring relevant field must obey s(k−1)=s(k) XOR t(k) for k>=ell+1. Finite support gives s=0 at large k, hence s(k)=XOR_{j>k} t(j). The excluded ell layer can leave future exposure.

All 1160 classes give a unique 35-cell algebraic candidate. It fails the first required L: the normalized head is WHITE. Its 620-cell candidate output is unachieved parity output, NOT actual permanent output. The 115 stable first-L classes and 30 bulk equal-letter adjacencies are exact diagnostics only.

The marker orbit has only phase 0,L. The actual first marker R5605 at(112,105) dies at49729. The second marker R18845 at(44,177) is already old before the first contact and dies at55541. The third required marker(-24,249) is WHITE in both full contact fields. W does not produce the next marker.

## Full actual field and prefix constraints

Fresh replay of all 57885 actual reads, full snapshots, all fates and the complete infinite canonical tail matches the signed source. Actual C* changes234→144, with90 old survivors and54 new relevant births. The shifted first C* differs by170 missing and80 additional cells. This comparison is not used as a counterfactual pruning oracle.

The desired next W first-read constraints are evaluated on the COMPLETE second board, not a C* crop:61 missing BLACK and66 interfering BLACK cells. The earliest actual failure is offset2 at(43,178): wanted L, actual WHITE/R. Its historical last read18971L fixes WHITE under any preserved prehistory. Earlier reads18835R/18843L/18847R/18955L/18963R are retained.

## Scope

Only this exact loop and its fixed-word recurrence are excluded. A different loop word, alternate preparation, intervening repair, or longer multi-interface cycle remains open. This is not a collective controller enumeration or universal regeneration obstruction. The main conjecture and gross leaf bound remain open.

The auditor has received the frozen package. Add a separate binding on PASS; do not edit frozen files.
