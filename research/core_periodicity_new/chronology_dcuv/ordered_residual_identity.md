# Ordered residual identity with internally recycled black cells

Status: exact analytic identity and finite controls; independent audit requested. No mixed-language exclusion is claimed.

Let a literal macro A be followed by its actual M11 marker. Let F be the finite complete-context read set, B0 its forced entry-black subset, Delta the RAW odd-read set, K the entry five-cell black core, and K' the rotated/translated endpoint core. Literal checking gives K subset B0 and K' subset B0 symmetric-difference Delta.

Define I=B0 minus K and O=(B0 symmetric-difference Delta) minus K'. An arbitrary compatible complete entry board has the form B0 union X, with X disjoint from F. Both cores and all RAW writes lie in F. Consequently its residual set E, obtained by removing K, equals I union X; the post-RAW residual set E', obtained by removing K', equals O union X. Therefore

    E' = (E minus I) union O.

The order matters. First remove every input and its producer label, then install a NEW producer label at every output. This is valid even if I and O intersect. A black cell read an even positive number of times is not an untouched survivor of its earlier producer.

For D/C/U/V maximal-C packets, the U, UC and UCC input/output intersection is exactly {(-1,2)}. Their common inputs are {(-1,1),(-1,2),(0,2),(0,3),(-1,4)}. Every output, including the recycled cell, has last RAW read R. The D/C/V packet data have empty input/output intersections. All ten packet types are retained in `literal_residual_geometry.json`; no recurrence pruning is part of this identity.

## Complete-context protection of a surviving label

Suppose a token produced by packet A remains labelled by A until packet B consumes it. At every strict intermediate packet its physical cell q is black and lies outside that packet's entry core, because it belongs to the residual set. If that complete RAW+M11 context touched q, its required first read would be L, so q would belong to that packet's input set I. The ordered update would remove the old label, contradicting its survival. Thus every strict intermediate COMPLETE context avoids q.

This argument applies unchanged when some packets have I intersect O nonempty: removal destroys the old label before recreation. It justifies the protected-pair premise and dynamic producer-label clearing rule in the expanded alphabet, but does not transfer any D/C/V forbidden relation into D/C/U/V. Every expanded-alphabet relation must be proved using the expanded reader set.

## Controls

`build_dcuv_residual_ledger.py` derives every set from literal integer-coordinate words. `replay_dcuv_residual_ledger.py` independently uses complex-coordinate current-color execution, checks exact full-board equality after every packet, and verifies ordered token removal/reinstallation. Its depth-eight tree includes35,994 feasible marked factors and69,326 internally recycled transactions; two distant unread black cells are added to each control seed. No bounded tree is substituted for the all-board set identity above.
