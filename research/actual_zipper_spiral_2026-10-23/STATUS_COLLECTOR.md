# Collector continuation status

Original paired-forest spiral PROOF.md (47ca17aa) is independently PASSED and
unchanged. The collector and exact ledger continuation independently PASSED all-parameter
analytic review and fresh full-board fixed controls. The separate first-reimport
follow-up below remains only a fixed finite control.

Independent report: ../audits/check_detoured_collector_independent.json.
No frozen proof or ledger file was changed by this status update.

Author proof: one_component_paired_forest_collector.md
SHA256: ed7197b2f981ab73ef47df9a9c30d9a190bd739540bdd7cc19aae1875606956c.
It claims actual spacing-eight epochs with ONE initial w tree and ONE final
dormant w tree, both complete black graphs forests, no cycle events, full
charged collector mass M, gain>=0.5 sqrt(M)-4. New marked w vertices fund the
gain; no output fragmentation or cycle births are necessary.

Exact active/dormant accounting and Euler BOOKKEEPING, not a monotone or
global progress theorem: epoch_component_ledger.md
SHA256: 9996e812118f628afd909c9245e061dc8d13f4b8b0afef90db1342d12bc5e2b3.
Universal quantitative consequence remains consumption of at least
((G-3)_+/8)^2 epoch-entry old bridges for gain G.

Fixed q = 1, 2, 3, 4, 8, 16, 32 controls at scale 8, with both initially passive and
initially connected collectors, all passed. The q = 32 connected case charges
M = 4479 including 2176 path + 2300 collector + 3 connector edges, runs 4382 actual
updates, gains 30, and has one final 4509-edge tree, A_w = 31, births/erasures = 0.
Helper check_collector.py SHA256: 853e71568c6db9b87adc01bf991e4852758cebeb5552a03f561a120d2db3c7cd.
check_detoured_collector.py SHA256: fe2a269a3dc1223aa2f38d8f989aa1c9098c13a11a247c40a8d99511b3966f77.
detoured_collector_controls.json SHA256: 2bde4e5390af6fba26326285714655ba01390807b8d63c1f8d3e20efef11c00f.
Explicit full-board witness q = 8 SHA256: 21b1759d4d62302c5612a60cb003b459e69328540bb173979f71121889c02661.

First-reimport follow-up is a fixed-family finite control, not a universal
routing restriction: q = 1, 2, 3, 4, 8, 16, 32 all have next prefix RRRRLLLLRLRRRRL.
The first R4L really imports the huge archive, but the next four ordinary
blocks L, L, L, RL reduce active mass F+3, F+2, 3, 2, 0, where F was archive mass.
The next R4L enters an isolated component. This shows why this construction
does not immediately concatenate near-extremal epochs.
check_collector_first_reimport.py SHA256: 4246331f0162dc30f0e4d71f26954c8298d4b1948b10dcdfe0d34ea6dbbf1a47.
collector_first_reimport_controls.json SHA256: 9930cae5bb18deb3b843fd76004f1b166b94cd86b39598f328af253468b7f4ae.

No sharpness of the global cubic bound, repeatable growing epoch sequence,
scalar complete-mass descent, or LIFO archive law is asserted.
