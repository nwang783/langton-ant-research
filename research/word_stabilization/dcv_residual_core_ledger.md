# An exact residual-token model for D/C/V

Status: independently audited by ../audits/check_dcv_residual_model_independent.py and its JSON report, including all 16,355 feasible marked factors through nine macros. This is a representation and research reduction, not an exclusion theorem.

Use the canonical D10, C15, V18 words and the actual right marker M11=LLLLRLRRRRL. At every marked boundary the five cells

K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}

are black in the local north frame. The other first-read cells of M11, {(1,1),(2,0),(2,1)}, are white. Remove the translated/rotated K from the complete board, calling the remaining black set E.

For a macro followed by the actual M11, the exact operation on E is to remove the listed input cells and add the listed output cells; every other E cell is unchanged. Full first-read white guards are essential and are saved in dcv_residual_core_resources.json. All coordinates below are in the macro's entry north frame.

- D: endpoint(1,1,N), input{(0,1)}, output{(2,0)}.
- C: endpoint(0,1,W), no input, output{(1,2),(2,0),(2,1)}.
- V: endpoint(1,3,N), input{(0,3),(1,2)}, output{(0,0),(0,1),(1,0),(2,0),(2,1),(2,2)}.

This follows by XORing the literal odd-read set, then subtracting the new five-cell core. Every input is outside the old core, every output is outside the new core, and the two listed sets are disjoint. All outputs have their last RAW read R. An input can first be read only in the actual following marker; it is already a black cell incorporated into the new core at the boundary. Thus the representation does not assert that every conceptual token removal is a RAW read.

For packets D C^k or V C^k, the C steps remove no residual tokens, so the input sets remain the same while each C contributes three more outputs. The exact seven-packet lists, endpoints, and guards are in dcv_residual_core_resources.json.

Label every residual black token by either its initial entry-black cell or the macro/packet which last deposited it. A token disappears when selected as an input, and every output receives a new label. For a marked factor beginning with the five-cell core and its minimal seed, the entry mass is exactly five plus the number of input removals whose token came from the initial residual set. With arbitrary additional unread black cells, only the corresponding lower bound on entry mass is asserted. This is ordinary finite-set accounting, not a freshness theorem for a particular input.

The exact replay in replay_dcv_residual_resources.py checks complete board equality E=B minus the current core after every packet. In DCVCCVV, the two inputs of the final V are both deposits of the initial DC packet. In DDCDCDCDV they come from the initial D and the following DC. Therefore a useful rank must allow finite multi-input recycling.

Two tempting simplifications fail:

1. Whole L-token ancestry depth is unbounded even for D^n: its phase5 star has depth n-1, while each period after the first still needs a separate new black side input.
2. A nonnegative linear weight on isolated producer/output and consumer/input types does not decrease on every recurrent packet in the current forbidden-pair overapproximation. The LP failure is only a failure of that coarse abstraction, not a physical recurrent trajectory.

The next target is a coupled-resource rank retaining which two V inputs can be supplied together, or a geometry-aware bound on how many outputs of one source can actually be consumed later. No such rank is claimed here.
